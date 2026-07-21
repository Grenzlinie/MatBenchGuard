import os
import json
import csv

# === author imports / helpers ===
import os, csv


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
    import os, csv
    total_path = os.path.join(outputs_dir, 'total_energies.csv')
    exchange_path = os.path.join(outputs_dir, 'exchange_parameters.csv')
    energies = {}
    try:
        with open(total_path, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                U = int(float(row['U_eff']))
                state = row['state'].strip()
                E = float(row['total_energy'])
                energies.setdefault(U, {})[state] = E
    except Exception:
        pass
    computed_J = {}
    for U in [5,6,7]:
        if U in energies and all(state in energies[U] for state in ['FM','AF1','AF2']):
            E_FM = energies[U]['FM']
            E_AF1 = energies[U]['AF1']
            E_AF2 = energies[U]['AF2']
            J_FHF_eV = (E_AF1 - E_FM) / 4.0
            J_pyz_eV = (E_AF2 - E_FM) / 4.0
            J_FHF_K = J_FHF_eV * 11604.5
            J_pyz_K = J_pyz_eV * 11604.5
            ratio = J_pyz_K / J_FHF_K if abs(J_FHF_K) > 1e-9 else 0.0
            computed_J[U] = {'J_FHF': J_FHF_K, 'J_pyz': J_pyz_K, 'ratio': ratio}
    reported = {}
    try:
        if os.path.exists(exchange_path):
            with open(exchange_path, newline='') as f:
                dr = csv.DictReader(f)
                for row in dr:
                    U = int(float(row['U_eff']))
                    reported[U] = {
                        'J_FHF': float(row['J_FHF']),
                        'J_pyz': float(row['J_pyz']),
                        'ratio': float(row['ratio_J_pyz_J_FHF'])
                    }
    except Exception:
        pass
    return {'computed_J': computed_J, 'reported': reported, 'energies': energies}


# === block: score_0 (check id='step_02_recompute') ===
def score_0(artifact, step, ctx):
    gold_J = step['gold_J_FHF']
    gold_ratio = step['gold_ratio']
    tol_J_rel = step['tolerance_J_relative']
    tol_J_range = step['tolerance_J_decay_range']
    tol_ratio_abs = step['tolerance_ratio_abs']
    tol_ratio_range = step['tolerance_ratio_decay_range']
    computed = ctx['computed_J']
    Ueffs = [5,6,7]
    scores = []
    for U in Ueffs:
        if U not in computed:
            scores.append(0.0)
            continue
        c = computed[U]
        # J_FHF magnitude score
        gold = abs(gold_J[Ueffs.index(U)])
        comp = abs(c['J_FHF'])
        rel_err = abs(comp - gold) / gold if gold != 0 else 1.0
        if rel_err <= tol_J_rel:
            sj = 1.0
        elif rel_err <= tol_J_range:
            sj = 1.0 - (rel_err - tol_J_rel) / (tol_J_range - tol_J_rel)
        else:
            sj = 0.0
        # ratio score
        g_ratio = gold_ratio[Ueffs.index(U)]
        diff = abs(c['ratio'] - g_ratio)
        if diff <= tol_ratio_abs:
            sr = 1.0
        elif diff <= tol_ratio_range:
            sr = 1.0 - (diff - tol_ratio_abs) / (tol_ratio_range - tol_ratio_abs)
        else:
            sr = 0.0
        scores.append((sj + sr) / 2.0)
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_1 (check id='step_03_consistency') ===
def score_1(artifact, step, ctx):
    computed = ctx['computed_J']
    reported = ctx['reported']
    Ueffs = [5,6,7]
    total = 0
    ok = 0
    for U in Ueffs:
        if U not in computed or U not in reported:
            continue
        c = computed[U]
        r = reported[U]
        good = True
        for key, frac, atol in [('J_FHF',0.05,5.0),('J_pyz',0.05,5.0)]:
            if abs(r[key] - c[key]) > frac * abs(c[key]) + atol:
                good = False
                break
        if abs(r['ratio'] - c['ratio']) > 0.05:
            good = False
        if good:
            ok += 1
        total += 1
    if total == 0:
        return 0.0
    return ok / total


# === block: score_2 (check id='step_03_structural') ===
def score_2(artifact, step, ctx):
    computed = ctx['computed_J']
    Ueffs = [5,6,7]
    for U in Ueffs:
        if U not in computed:
            return 0.0
        c = computed[U]
        if abs(c['J_FHF']) <= abs(c['J_pyz']) or c['ratio'] >= 1.0 or c['ratio'] <= 0.0:
            return 0.0
    return 1.0


_SCORERS = {
    'step_02_recompute': score_0,
    'step_03_consistency': score_1,
    'step_03_structural': score_2,
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
