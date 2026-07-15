import os
import json
import csv

# === author imports / helpers ===
import sys, os, subprocess
try:
    import numpy as np
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', '--no-cache-dir',
                           '-i', 'https://pypi.tuna.tsinghua.edu.cn/simple', 'numpy', 'scipy'])
    import numpy as np

try:
    from scipy import stats
except ImportError:
    # scipy may require numpy to be importable; re-install if needed
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', '--no-cache-dir',
                           '-i', 'https://pypi.tuna.tsinghua.edu.cn/simple', 'scipy'])
    from scipy import stats


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


# === block: score_0 (check id='step_1') ===
def score_0(artifact, step, ctx):
    # Scorer for step_1: recompute slopes and compare to paper references
    # Artifact is a list of dicts from the CSV file
    import csv, os, json
    import numpy as np
    from scipy import stats

    cases = {'no_bandstructure': [], 'with_bandstructure': []}
    for row in artifact:
        case = row.get('case', '').strip()
        strain = float(row['strain'])
        freq = float(row['frequency'])
        cases[case].append((strain, freq))

    # Minimum data points check (5 per case as per contract)
    for cname in cases:
        if len(cases[cname]) < 5:
            return 0.0  # insufficient data; cannot compute slopes

    # Compute slopes
    slopes = {}
    for case_key, pts in cases.items():
        pts_sorted = sorted(pts, key=lambda x: x[0])
        strains = [p[0] for p in pts_sorted]
        freqs = [p[1] for p in pts_sorted]
        slope, intercept, r_value, p_value, std_err = stats.linregress(strains, freqs)
        slopes[case_key] = slope

    sl_no = slopes['no_bandstructure']
    sl_wb = slopes['with_bandstructure']

    # Negativity check
    if sl_no >= 0 or sl_wb >= 0:
        return 0.0

    # Ordering check: with_bandstructure must be more negative
    if sl_wb >= sl_no:
        return 0.0   # ordering violated, reproduction not consistent

    # Relative distance to reference
    ref_no = step['ref_slope_no_bandstructure']  # -66
    ref_wb = step['ref_slope_with_bandstructure']  # -79
    tol = step['tolerance_rel']  # 0.15

    def rel_score(slope, ref):
        rel_diff = abs(slope - ref) / max(abs(ref), 1e-9)
        return max(0.0, 1.0 - rel_diff / tol)

    score_no = rel_score(sl_no, ref_no)
    score_wb = rel_score(sl_wb, ref_wb)

    # Final score as average of the two sub-scores
    final = (score_no + score_wb) / 2.0
    return final


_SCORERS = {
    'step_1': score_0,
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
