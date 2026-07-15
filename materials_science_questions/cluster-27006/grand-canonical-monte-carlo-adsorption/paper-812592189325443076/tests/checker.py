import os
import json
import csv

# === author imports / helpers ===
import csv, math


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
    return spec


# === block: score_0 (check id='structural_check') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    row = rows[0]
    golds = step.get('gold', {})
    if not golds:
        return 1.0
    total = len(golds)
    passed = 0.0
    for col, g in golds.items():
        val_str = row.get(col, '')
        if val_str.strip() == '':
            continue
        try:
            val = float(val_str)
        except (ValueError, KeyError):
            continue
        target = g.get('value', 0)
        tol = g.get('tolerance', 0)
        diff = abs(val - target)
        if diff <= tol:
            passed += 1.0
        else:
            overshoot = diff - tol
            frac = max(0.0, 1.0 - overshoot / (tol * 2.0 + 1e-12))
            passed += frac
    return passed / total


# === block: score_1 (check id='isotherm_check') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    # Helper to get pressure and loading
    def get_values(row):
        try:
            p = float(row.get('pressure_bar', 0))
            l = float(row.get('loading_cm3stp_per_g', 0))
            return p, l
        except (ValueError, KeyError):
            return None

    # Loading check at 0.1 bar
    candidates_01 = []
    for r in rows:
        v = get_values(r)
        if v is None:
            continue
        p, l = v
        if abs(p - step.get('ref_pressure', 0.1)) <= 0.01:
            candidates_01.append((abs(p - step.get('ref_pressure', 0.1)), l))
    if candidates_01:
        _, load_01 = min(candidates_01, key=lambda x: x[0])
        target_load = step.get('loading_threshold', 200.0)
        load_score = min(1.0, load_01 / target_load) if target_load > 0 else 0.0
    else:
        load_score = 0.0

    # Cusp check: loading difference between 0.05 and 0.03 bar
    candidates_03 = []
    candidates_05 = []
    p_low = step.get('cusp_pressure_low', 0.03)
    p_high = step.get('cusp_pressure_high', 0.05)
    cusp_diff_thr = step.get('cusp_diff_threshold', 20.0)
    for r in rows:
        v = get_values(r)
        if v is None:
            continue
        p, l = v
        if abs(p - p_low) <= 0.005:
            candidates_03.append((abs(p - p_low), l))
        if abs(p - p_high) <= 0.005:
            candidates_05.append((abs(p - p_high), l))
    if candidates_03 and candidates_05:
        _, load_03 = min(candidates_03, key=lambda x: x[0])
        _, load_05 = min(candidates_05, key=lambda x: x[0])
        diff = load_05 - load_03
        if diff >= cusp_diff_thr:
            cusp_score = 1.0
        elif diff > 0:
            cusp_score = diff / cusp_diff_thr
        else:
            cusp_score = 0.0
    else:
        cusp_score = 0.0

    return 0.5 * load_score + 0.5 * cusp_score


_SCORERS = {
    'structural_check': score_0,
    'isotherm_check': score_1,
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
