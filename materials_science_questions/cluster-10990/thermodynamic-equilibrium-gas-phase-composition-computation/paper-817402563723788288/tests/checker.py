import os
import json
import csv

# === author imports / helpers ===
import math
import csv
import os


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
    import math
    spec_ref = spec.get("reference", {})
    coeffs = spec_ref["pressure_coefficients"]
    temperatures = spec_ref["temperatures"]
    expected_p = {}
    for sp in ['B','N','BN','B2N','N3','B2','B3']:
        A, Tc = coeffs[sp]
        expected_p[sp] = [A * math.exp(-Tc / T) for T in temperatures]
    expected_n2 = []
    for idx, T in enumerate(temperatures):
        sum_others = sum(expected_p[sp][idx] for sp in ['B','N','BN','B2N','N3','B2','B3'])
        p_n2 = max(0.0, 1.0 - sum_others)
        expected_n2.append(p_n2)
    expected_p['N2'] = expected_n2

    dp = spec_ref["droplet_params"]
    r0, n0, T_nucl, T_end, cool, m_B, k = dp["r0"], dp["n0"], dp["T_nucl"], dp["T_end"], dp["cooling_rate"], dp["m_B"], dp["k"]
    term1 = (2.0 * r0) ** (9.0 / 5.0)
    term2 = n0 ** (2.0 / 5.0)
    term3 = (2.0 * math.pi * k * (T_nucl + T_end) / m_B) ** (1.0 / 5.0)
    term4 = ((T_nucl - T_end) / cool) ** (2.0 / 5.0)
    D_m = term1 * term2 * term3 * term4
    D_ref_nm = D_m / 1.0e-9
    ctx = {"expected_p": expected_p, "temperatures": temperatures, "D_ref_nm": D_ref_nm}
    return ctx


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0
    req_cols = ['Temperature_K', 'p_B_atm', 'p_N_atm', 'p_BN_atm', 'p_B2N_atm', 'p_N2_atm', 'p_N3_atm', 'p_B2_atm', 'p_B3_atm']
    sp_names = ['B','N','BN','B2N','N2','N3','B2','B3']
    col_map = {col: col for col in req_cols}
    temps_expected = ctx['temperatures']
    expected = ctx['expected_p']
    rows_by_temp = {}
    for row in artifact:
        try:
            T = float(row.get('Temperature_K'))
        except (TypeError, ValueError):
            continue
        rows_by_temp[T] = row
    scores = []
    for idx, T in enumerate(temps_expected):
        if T not in rows_by_temp:
            continue
        row = rows_by_temp[T]
        for sp in sp_names:
            col = col_map.get('p_'+sp+'_atm', None) if sp != 'N2' else 'p_N2_atm'
            if col:
                try:
                    val = float(row.get(col, 0.0))
                except (TypeError, ValueError):
                    scores.append(0.0)
                    continue
                exp_val = expected[sp][idx]
                if exp_val == 0.0:
                    cell_score = 1.0 if abs(val) < 1e-15 else 0.0
                else:
                    rel_err = abs(val - exp_val) / abs(exp_val)
                    tol_rel = 0.2 if abs(exp_val) > 1e-6 else 0.5
                    if rel_err <= tol_rel:
                        cell_score = 1.0
                    else:
                        cell_score = max(0.0, 1.0 - (rel_err - tol_rel) / tol_rel)
                scores.append(cell_score)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    try:
        if isinstance(artifact, str):
            val_str = artifact.strip().split()[0]
        else:
            val_str = str(artifact).strip()
        D = float(val_str)
    except (ValueError, TypeError, AttributeError):
        return 0.0
    D_ref = ctx['D_ref_nm']
    tol_nm = 5.0
    if abs(D - D_ref) <= tol_nm:
        return 1.0
    else:
        return 0.0


_SCORERS = {
    'step_01': score_0,
    'step_02': score_1,
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
