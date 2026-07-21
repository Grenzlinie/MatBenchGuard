import os
import json
import csv

# === author imports / helpers ===
import re
import math


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


# === block: score_0 (check id='center_deviation_trends') ===
def score_0(artifact, step, ctx):
    try:
        rows = artifact
        if not rows:
            return 0.0
        # Group by condition_label
        from collections import defaultdict
        groups = defaultdict(list)
        for r in rows:
            cl = r.get('condition_label','').strip()
            if not cl:
                continue
            try:
                pc = float(r.get('particle_count',0))
                val = float(r.get('r',0))
            except (ValueError, TypeError):
                continue
            groups[cl].append((pc, val))
        # Sort each group by particle_count
        for cl in groups:
            groups[cl].sort(key=lambda x: x[0])
        required = step['config']['required_conditions']
        params = step['config']['classification_params']
        early_range = params.get('early_range', 2000)
        drop_thresh = params.get('drop_threshold_ratio', 0.3)
        rise_thresh = params.get('rise_threshold_ratio', 1.2)
        # regex for expected label: epp_<num>_eps_<num>_height_<int>
        label_re = re.compile(r'^epp_([\d.]+)_eps_([\d.]+)_height_(\d+)$')
        correct = 0
        total = len(required)
        for cond in required:
            # Build expected label
            epp = cond['epp']
            eps = cond['eps']
            hgt = cond['height']
            expected_label = f'epp_{epp}_eps_{eps}_height_{hgt}'
            series = groups.get(expected_label)
            if series is None or len(series) < 5:
                continue
            r_vals = [v for _, v in series]
            r_start = r_vals[0]
            # Find minimum in first early_range particles
            min_val = None
            for pc, v in series:
                if pc <= early_range:
                    if min_val is None or v < min_val:
                        min_val = v
                else:
                    break
            if min_val is None:
                continue
            r_end = r_vals[-1]
            # Check for growth: r_start drops significantly then rises later
            is_growth = False
            if r_start > 0 and min_val > 0:
                drop = (r_start - min_val) / r_start
                if drop > drop_thresh and r_end > min_val * rise_thresh:
                    is_growth = True
            predicted = 'growth' if is_growth else 'nucleation'
            if predicted == cond['expected_regime']:
                correct += 1
        if total == 0:
            return 1.0
        return float(correct) / float(total)
    except Exception:
        return 0.0


_SCORERS = {
    'center_deviation_trends': score_0,
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
