import os
import json
import csv

# === author imports / helpers ===
import numpy as np


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


# === block: score_0 (check id='step_02') ===
def score_0(artifact, step, ctx):
    rows = artifact  # list of dicts from csv
    mode_col = 'mode'
    fields = ['n_eff', 'n_eff_coreless', 'delta_n_eff']
    gold = step.get('gold', {})
    tol = step.get('tolerance', 1e-6)

    total_checks = 0
    passed = 0

    for row in rows:
        m = str(row.get(mode_col, '')).strip()
        if m not in gold:
            continue
        target = gold[m]
        # backward compatibility: if target is a plain float, it is the n_eff gold
        if isinstance(target, (int, float)):
            try:
                v = float(row.get('n_eff', ''))
            except (ValueError, TypeError):
                continue
            total_checks += 1
            if abs(v - target) <= tol:
                passed += 1
            continue
        # otherwise assume target is a dict with one or more of the expected fields
        if isinstance(target, dict):
            for fld in fields:
                if fld not in target:
                    continue
                try:
                    v = float(row.get(fld, ''))
                except (ValueError, TypeError):
                    continue
                total_checks += 1
                if abs(v - target[fld]) <= tol:
                    passed += 1

    return passed / total_checks if total_checks > 0 else 0.0


# === block: score_1 (check id='step_03') ===
def score_1(artifact, step, ctx):
    rows = artifact  # list of dicts
    r_list = []
    a0_list = []
    api_list = []
    for row in rows:
        try:
            r_list.append(float(row.get('r_um', 0)))
            a0_list.append(float(row.get('amplitude_theta0', 0)))
            api_list.append(float(row.get('amplitude_theta_pi', 0)))
        except (ValueError, TypeError):
            continue
    if not r_list:
        return 0.0
    r = np.array(r_list)
    a0 = np.array(a0_list)
    api = np.array(api_list)
    checks = step.get('checks', [])
    sub_scores = []
    for chk in checks:
        name = chk.get('name')
        if name == 'max_offset':
            th = chk.get('threshold_r', 0.1)
            idx = np.argmax(a0)
            sub_scores.append(1.0 if r[idx] > th else 0.0)
        elif name == 'local_max_in_core2':
            rmin = chk.get('r_min', 29.0)
            rmax = chk.get('r_max', 36.0)
            mask = (r >= rmin) & (r <= rmax)
            found = False
            for i in range(1, len(a0)-1):
                if mask[i] and a0[i] > a0[i-1] and a0[i] > a0[i+1]:
                    found = True
                    break
            sub_scores.append(1.0 if found else 0.0)
        elif name == 'azimuthal_asymmetry':
            min_diff = chk.get('min_diff', 0.2)
            md = np.max(np.abs(a0 - api))
            sub_scores.append(1.0 if md > min_diff else 0.0)
        else:
            sub_scores.append(0.0)
    if not sub_scores:
        return 0.0
    return float(np.mean(sub_scores))


_SCORERS = {
    'step_02': score_0,
    'step_03': score_1,
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
