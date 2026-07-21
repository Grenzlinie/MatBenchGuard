import os
import json
import csv

# === author imports / helpers ===
import json, csv, os, math


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
        order_params_path = os.path.join(outputs_dir, 'order_parameters.csv')
        order_params = []
        if os.path.exists(order_params_path):
            with open(order_params_path, newline='') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    order_params.append({k: float(v) for k,v in row.items()})
        return {'order_params': order_params}


# === block: score_0 (check id='check_order_params') ===
def score_0(artifact, step, ctx):
        check_points = step.get('check_points', [])
        if not check_points:
            return 0.0
        import math
        order_params = ctx.get('order_params', [])
        passed = 0
        for cp in check_points:
            n_exp = cp['n']
            w_exp = cp['W']
            tp_exp = cp['t_perp_t']
            exp = cp['expected']
            tol = cp['tol_abs']
            found = None
            for row in order_params:
                if (abs(row.get('n',0)-n_exp) < 1e-6 and
                    abs(row.get('W',0)-w_exp) < 1e-6 and
                    abs(row.get('t_perp_t',0)-tp_exp) < 1e-6):
                    found = row
                    break
            if found is None:
                continue
            ok = True
            for key, exp_val in exp.items():
                actual = found.get(key, None)
                if actual is None:
                    ok = False
                    break
                t = tol.get(key, 0.0)
                if abs(actual - exp_val) > t:
                    ok = False
                    break
            if ok:
                passed += 1
        return passed / len(check_points) if check_points else 0.0


# === block: score_1 (check id='check_phase_consistency') ===
def score_1(artifact, step, ctx):
        order_params = ctx.get('order_params', [])
        thresholds = step.get('thresholds', {})
        m_thr = thresholds.get('m', 0.01)
        d_thr = thresholds.get('delta', 0.001)
        # compute expected phase for each t_perp_t=0.5 point
        exp_phase = {}
        for row in order_params:
            if abs(row.get('t_perp_t',0) - 0.5) > 1e-6:
                continue
            n = row['n']
            w = row['W']
            m1 = row.get('m_1', 0)
            m2 = row.get('m_2', 0)
            d1 = row.get('delta_1', 0)
            d2 = row.get('delta_2', 0)
            has_m = (abs(m1) > m_thr) or (abs(m2) > m_thr)
            has_sc = (abs(d1) > d_thr) or (abs(d2) > d_thr)
            if has_m and has_sc:
                phase = 'AFM+SC'
            elif has_m and not has_sc:
                phase = 'AFM'
            elif not has_m and has_sc:
                phase = 'SC'
            else:
                phase = 'unknown'
            exp_phase[(n,w)] = phase
        # compare with agent phase_diagram.csv
        total = 0
        matched = 0
        for row in artifact:
            n = float(row['n'])
            w = float(row['W'])
            phase = row['phase']
            total += 1
            if (n,w) in exp_phase and exp_phase[(n,w)] == phase:
                matched += 1
        return matched / total if total > 0 else 0.0


# === block: score_2 (check id='check_fermi_bands') ===
def score_2(artifact, step, ctx):
        required = step.get('required_features', [])
        if not isinstance(artifact, dict):
            return 0.0
        expected_keys = ['n=0.98','n=0.95','n=0.90','n=0.85']
        present = 0
        for key in expected_keys:
            if key in artifact:
                val = artifact[key]
                if isinstance(val, dict) and 'k_path' in val and 'energies' in val and 'features' in val:
                    present += 1
        struct_score = present / len(expected_keys) if expected_keys else 0.0
        feature_score = 0.0
        if required:
            total_keys = len(expected_keys)
            found_reqs = 0
            for key in expected_keys:
                if key in artifact and isinstance(artifact[key], dict):
                    feat = artifact[key].get('features', '').lower()
                    if all(r.lower() in feat for r in required):
                        found_reqs += 1
            feature_score = found_reqs / total_keys if total_keys else 0.0
        else:
            feature_score = 1.0
        return 0.6 * struct_score + 0.4 * feature_score


_SCORERS = {
    'check_order_params': score_0,
    'check_phase_consistency': score_1,
    'check_fermi_bands': score_2,
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
