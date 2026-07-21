import os
import json
import csv

# === author imports / helpers ===
import math
from io import StringIO


import os as _ff_os
import json as _ff_json


def _ff_validate_output_contract():
    """Return a list of shape violations against grading_spec['output_contract']."""
    spec_path = "/tests/grading_spec.json"
    if not _ff_os.path.exists(spec_path):
        return []
    with open(spec_path) as _f:
        _spec = _ff_json.load(_f)
    contract = _spec.get("output_contract", {}) or {}
    outputs = contract.get("outputs", []) or []
    out_dir = "/app/outputs"
    violations = []
    for out in outputs:
        base = str(out.get("file", "")).split("/")[-1]
        if not base:
            continue
        path = _ff_os.path.join(out_dir, base)
        if not _ff_os.path.isfile(path):
            violations.append("missing output_contract file: " + base)
            continue
        fmt = out.get("format", "")
        schema = out.get("schema", {}) or {}
        if fmt == "json":
            try:
                data = _ff_json.load(open(path))
            except Exception as exc:  # noqa: BLE001
                violations.append(base + ": invalid JSON (" + str(exc) + ")")
                continue
            required = schema.get("required", {})
            fields = required.keys() if isinstance(required, dict) else (required or [])
            if isinstance(data, dict):
                for field in fields:
                    if field not in data:
                        violations.append(base + ": missing JSON field '" + str(field) + "'")
        elif fmt in ("csv", "tsv"):
            import csv as _ff_csv
            delim = "\t" if fmt == "tsv" else ","
            try:
                with open(path, newline="") as _f:
                    cols = set((_ff_csv.reader(_f, delimiter=delim).__next__() or []))
            except StopIteration:
                cols = set()
            except Exception as exc:  # noqa: BLE001
                violations.append(base + ": cannot read table (" + str(exc) + ")")
                continue
            required_cols = schema.get("required_columns", []) or []
            for col in required_cols:
                name = col.get("name") if isinstance(col, dict) else col
                if name and name not in cols:
                    violations.append(base + ": missing table column '" + str(name) + "'")
    return violations


def _ff_contract_gate():
    """Zero the reward and exit if the submission violates the output_contract shape."""
    violations = _ff_validate_output_contract()
    if not violations:
        return
    _ff_os.makedirs("/logs/verifier", exist_ok=True)
    with open("/logs/verifier/reward.txt", "w") as _f:
        _f.write("0.0")
    with open("/logs/verifier/breakdown.json", "w") as _f:
        _ff_json.dump({"output_contract_violations": violations}, _f, indent=2)
    raise SystemExit(0)


def load_artifact(path):
    if not path or not os.path.exists(path):
        return None
    if path.endswith(".json"):
        try:
            with open(path) as f:
                return json.load(f)
        except Exception:  # noqa: BLE001
            return None
    if path.endswith(".csv") or path.endswith(".tsv"):
        delim = "\t" if path.endswith(".tsv") else ","
        with open(path, newline="") as f:
            return list(csv.DictReader(f, delimiter=delim))
    with open(path) as f:
        return f.read()


def prepare(outputs_dir, spec):
    params = spec['steps'][0]['params']
    return {'params': params}


# === block: score_0 (check id='calc_binding_energies') ===
def score_0(artifact, step, ctx):
    # constants from params
    p = ctx['params']
    ref = p['reference_binding_energies']
    S_Si = p['electronegativities']['S_Si']
    S_O  = p['electronegativities']['S_O']
    S_N  = p['electronegativities']['S_N']
    # The spec may carry a sign; we take the absolute value to match the paper's sign convention
    C_N  = abs(p['proportionality_constant_N1s'])
    tol = step.get('tolerance_abs', 0.02)

    # Mapping from tetrahedron number to (n_O, n_N) and bonding unit (k,m,p)
    # Derived from the paper's Table I and structural composition.
    n_O_dict = {1:0,2:0,3:1,4:0,5:1,6:0,7:2,8:1,9:0,10:2,11:1,12:3,13:2,14:3,15:4}
    n_N_dict = {1:0,2:1,3:0,4:2,5:1,6:3,7:0,8:2,9:4,10:1,11:3,12:0,13:2,14:1,15:0}
    bonding_kmp = {
        1: (1,0,0), 2: (3,0,1), 3: (2,1,0), 4: (3,0,2), 5: (6,3,2),
        6: (1,0,1), 7: (1,1,0), 8: (6,3,4), 9: (3,0,4), 10: (3,1,1),
        11: (2,1,2), 12: (2,3,0), 13: (3,3,2), 14: (6,9,2), 15: (1,2,0)
    }

    shift_per_O = (ref['SiO2'] - ref['Si_Si4']) / 4.0
    shift_per_N = (ref['Si3N4_Si2p'] - ref['Si_Si4']) / 4.0

    def compute_partial_charge(k, m, p):
        S_SiON = (S_Si**k * S_O**m * S_N**p) ** (1.0/(k+m+p))
        P_N = (S_SiON - S_N) / (2.08 * math.sqrt(S_N))
        return P_N

    P_N_ref = compute_partial_charge(3, 0, 4)  # Si3N4

    rows = artifact  # list of dicts
    correct = 0
    total_expected = 15
    for row in rows[:15]:
        try:
            num = int(row.get('tetrahedron_number', -1))
        except:
            num = -1
        if num < 1 or num > 15:
            continue
        # Si 2p3/2 binding energy
        eb_val = row.get('EB_Si2p3_2', '').strip()
        if eb_val == '' or eb_val.lower() == 'nan':
            continue
        try:
            eb = float(eb_val)
        except:
            continue
        n_O = n_O_dict[num]
        n_N = n_N_dict[num]
        expected_eb = ref['Si_Si4'] + shift_per_O * n_O + shift_per_N * n_N
        eb_ok = abs(eb - expected_eb) <= tol

        # N 1s shift
        delta_ok = True
        if n_N == 0:
            # no nitrogen expected, deltaEB_N1s should be missing or NaN
            delta_val = row.get('deltaEB_N1s', '').strip()
            if delta_val == '' or delta_val.lower() == 'nan':
                delta_ok = True
            else:
                try:
                    delta_agent = float(delta_val)
                    if math.isnan(delta_agent):
                        delta_ok = True
                    else:
                        delta_ok = False
                except:
                    delta_ok = False
        else:
            delta_val = row.get('deltaEB_N1s', '').strip()
            if delta_val == '' or delta_val.lower() == 'nan':
                delta_ok = False
            else:
                try:
                    delta_agent = float(delta_val)
                except:
                    delta_ok = False
                if delta_ok:
                    k, m, p = bonding_kmp[num]
                    P_N = compute_partial_charge(k, m, p)
                    expected_delta = C_N * (P_N - P_N_ref)
                    delta_ok = abs(delta_agent - expected_delta) <= tol
        if eb_ok and delta_ok:
            correct += 1

    score = correct / total_expected
    return score


_SCORERS = {
    'calc_binding_energies': score_0,
}


def _step_id(step, index):
    sid = str(step.get("id", "")).strip()
    if sid:
        return sid
    output = str(step.get("output_file", "")).split("/")[-1].rsplit(".", 1)[0]
    kind = str(step.get("kind") or step.get("metric") or "score").strip()
    base = "_".join(part for part in (output, kind) if part).strip("_")
    return base or ("check_" + str(index))


def main():
    _ff_contract_gate()
    with open("/tests/grading_spec.json") as f:
        spec = json.load(f)
    outputs_dir = "/app/outputs"
    ctx = prepare(outputs_dir, spec)
    steps = spec.get("steps", spec.get("checks", [])) or []
    breakdown = {}
    total = 0.0
    for index, step in enumerate(steps):
        sid = _step_id(step, index)
        output_file = str(step.get("output_file", "")).split("/")[-1]
        weight = float(step.get("weight", 0.0))
        artifact = load_artifact(os.path.join(outputs_dir, output_file)) if output_file else None
        fn = _SCORERS.get(sid)
        if fn is None:
            score = 0.0
        else:
            try:
                score = float(fn(artifact, step, ctx))
            except Exception as exc:  # noqa: BLE001
                score = 0.0
                breakdown.setdefault("_errors", {})[sid] = repr(exc)
        score = max(0.0, min(1.0, score))
        breakdown[sid or output_file] = {"score": score, "weight": weight}
        total += score * weight
    os.makedirs("/logs/verifier", exist_ok=True)
    with open("/logs/verifier/reward.txt", "w") as f:
        f.write(str(round(total, 6)))
    with open("/logs/verifier/breakdown.json", "w") as f:
        json.dump(breakdown, f, indent=2)


if __name__ == "__main__":
    main()
