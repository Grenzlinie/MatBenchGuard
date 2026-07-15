import os
import json
import csv

# === author imports / helpers ===
import json


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
    return {}


# === block: score_0 (check id='defect_results') ===
def score_0(artifact, step, ctx):
    # Check artifact shape and gold presence
    if not isinstance(artifact, dict):
        return 0.0

    gold = step.get('gold')
    if not gold:
        return 0.0

    try:
        surf_g = gold['surface']
        deep_g = gold['internal_deep']
        shal_g = gold['internal_shallow']
        surf = artifact['surface']
        deep = artifact['internal_deep']
        shal = artifact['internal_shallow']
    except KeyError:
        return 0.0

    for d in (surf, deep, shal):
        if not all(k in d for k in ('defect_level','formation_energy','cbm_vbm_same_kpoint')):
            return 0.0

    # Tolerances: generous to accommodate legitimate DFT code/functional differences
    DL_TOL = 0.10   # eV
    FE_TOL = 0.30   # eV

    def soft_score(val, gold, tol):
        """1.0 if exact, linear drop to 0 at tol."""
        return max(0.0, 1.0 - abs(val - gold) / tol)

    s_dl_s = soft_score(surf['defect_level'], surf_g['defect_level'], DL_TOL)
    s_dl_d = soft_score(deep['defect_level'], deep_g['defect_level'], DL_TOL)
    s_dl_sh = soft_score(shal['defect_level'], shal_g['defect_level'], DL_TOL)

    s_fe_s = soft_score(surf['formation_energy'], surf_g['formation_energy'], FE_TOL)
    s_fe_d = soft_score(deep['formation_energy'], deep_g['formation_energy'], FE_TOL)
    s_fe_sh = soft_score(shal['formation_energy'], shal_g['formation_energy'], FE_TOL)

    s_bool_s = 1.0 if surf['cbm_vbm_same_kpoint'] == surf_g['cbm_vbm_same_kpoint'] else 0.0
    s_bool_d = 1.0 if deep['cbm_vbm_same_kpoint'] == deep_g['cbm_vbm_same_kpoint'] else 0.0
    s_bool_sh = 1.0 if shal['cbm_vbm_same_kpoint'] == shal_g['cbm_vbm_same_kpoint'] else 0.0

    fe_s = surf['formation_energy']
    fe_sh = shal['formation_energy']
    fe_d = deep['formation_energy']
    s_trend = 1.0 if (fe_s > fe_sh > fe_d) else 0.0

    # Weights: defect levels 0.15 each, formation energies 0.10 each, booleans 0.05 each, trend 0.10
    w = [0.15, 0.15, 0.15, 0.10, 0.10, 0.10, 0.05, 0.05, 0.05, 0.10]
    scores = [s_dl_s, s_dl_d, s_dl_sh, s_fe_s, s_fe_d, s_fe_sh, s_bool_s, s_bool_d, s_bool_sh, s_trend]
    return sum(a*b for a,b in zip(w, scores))


_SCORERS = {
    'defect_results': score_0,
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
