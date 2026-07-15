import os
import json
import csv

# === author imports / helpers ===
import numpy as np
import csv
import json
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
    return {}


# === block: score_0 (check id='check_analytical_csv_structural') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) < 15:
        return 0.0
    cols = set(artifact[0].keys())
    required = {'mass_fraction_surfactant', 'critical_supersaturation', 'critical_diameter', 'surfactant_bulk_concentration'}
    if not required.issubset(cols):
        return 0.0
    ss_vals = []
    mf_vals = []
    for row in artifact:
        try:
            mf = float(row['mass_fraction_surfactant'])
            ss = float(row['critical_supersaturation'])
            if ss <= 0:
                return 0.0
            mf_vals.append(mf)
            ss_vals.append(ss)
        except (ValueError, KeyError):
            return 0.0
    # check monotonic decreasing: ss should decrease as mf increases
    if len(ss_vals) > 1:
        diffs = np.diff(ss_vals)
        # allow a tiny positive difference (up to 0.001) due to numerical noise
        viol = np.sum(diffs > 0.001)
        if viol / len(diffs) > 0.05:  # more than 5% violations -> fail
            return 0.0
    return 1.0


# === block: score_1 (check id='check_error_analysis_recompute') ===
def score_1(artifact, step, ctx):
    def read_csv_supersat(filepath):
        if not os.path.exists(filepath):
            return None
        rows = []
        with open(filepath, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    mf = float(row['mass_fraction_surfactant'])
                    ss = float(row['critical_supersaturation'])
                    rows.append((mf, ss))
                except (ValueError, KeyError):
                    return None
        return rows

    analytical = read_csv_supersat('/app/outputs/critical_properties.csv')
    iterative = read_csv_supersat('/app/outputs/iterative_reference.csv')
    if analytical is None or iterative is None:
        return 0.0
    # align by mass_fraction (allow small tolerance)
    anal_dict = {mf: ss for mf, ss in analytical}
    iter_dict = {mf: ss for mf, ss in iterative}
    max_diff = 0.0
    common_mfs = set(anal_dict.keys()) & set(iter_dict.keys())
    if not common_mfs:
        return 0.0
    for mf in common_mfs:
        diff = abs(anal_dict[mf] - iter_dict[mf])
        if diff > max_diff:
            max_diff = diff
    if max_diff <= 0.05:
        return 1.0
    else:
        return 0.0


_SCORERS = {
    'check_analytical_csv_structural': score_0,
    'check_error_analysis_recompute': score_1,
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
