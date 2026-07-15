import os
import json
import csv


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
    gold = {
        900: {"C11_M1": 261.9, "C11_M2": 261.9, "C11_T1": 261.9, "C11_T2": 261.9,
              "C44_M1": 148.1, "C44_M2": 148.1, "C44_T1": 148.1, "C44_T2": 148.1},
        1000: {"C11_M1": 255.68, "C11_M2": 255.68, "C11_T1": 255.67, "C11_T2": 255.67,
               "C44_M1": 146.47, "C44_M2": 146.47, "C44_T1": 146.47, "C44_T2": 146.47},
        1100: {"C11_M1": 249.50, "C11_M2": 249.49, "C11_T1": 249.45, "C11_T2": 249.44,
               "C44_M1": 144.85, "C44_M2": 144.85, "C44_T1": 144.84, "C44_T2": 144.84},
        1200: {"C11_M1": 243.36, "C11_M2": 243.34, "C11_T1": 243.24, "C11_T2": 243.21,
               "C44_M1": 143.24, "C44_M2": 143.24, "C44_T1": 143.21, "C44_T2": 143.21},
        1300: {"C11_M1": 237.27, "C11_M2": 237.21, "C11_T1": 237.06, "C11_T2": 236.99,
               "C44_M1": 141.64, "C44_M2": 141.63, "C44_T1": 141.58, "C44_T2": 141.58},
        1400: {"C11_M1": 231.23, "C11_M2": 231.11, "C11_T1": 230.90, "C11_T2": 230.77,
               "C44_M1": 140.04, "C44_M2": 140.03, "C44_T1": 139.95, "C44_T2": 139.95},
        1500: {"C11_M1": 225.25, "C11_M2": 225.04, "C11_T1": 224.77, "C11_T2": 224.55,
               "C44_M1": 138.46, "C44_M2": 138.44, "C44_T1": 138.33, "C44_T2": 138.32},
        1600: {"C11_M1": 219.33, "C11_M2": 219.01, "C11_T1": 218.68, "C11_T2": 218.35,
               "C44_M1": 136.88, "C44_M2": 136.86, "C44_T1": 136.71, "C44_T2": 136.69},
        1700: {"C11_M1": 213.48, "C11_M2": 213.01, "C11_T1": 212.64, "C11_T2": 212.15,
               "C44_M1": 135.31, "C44_M2": 135.28, "C44_T1": 135.09, "C44_T2": 135.06},
        1800: {"C11_M1": 207.70, "C11_M2": 207.05, "C11_T1": 206.65, "C11_T2": 205.97,
               "C44_M1": 133.75, "C44_M2": 133.71, "C44_T1": 133.47, "C44_T2": 133.43},
        1900: {"C11_M1": 201.99, "C11_M2": 201.13, "C11_T1": 200.71, "C11_T2": 199.81,
               "C44_M1": 132.21, "C44_M2": 132.15, "C44_T1": 131.86, "C44_T2": 131.81},
        2000: {"C11_M1": 196.34, "C11_M2": 195.26, "C11_T1": 194.83, "C11_T2": 193.68,
               "C44_M1": 130.67, "C44_M2": 130.59, "C44_T1": 130.25, "C44_T2": 130.17},
        2100: {"C11_M1": 190.83, "C11_M2": 189.44, "C11_T1": 189.02, "C11_T2": 187.56,
               "C44_M1": 129.14, "C44_M2": 129.05, "C44_T1": 128.65, "C44_T2": 128.55},
        2200: {"C11_M1": 185.37, "C11_M2": 183.67, "C11_T1": 183.28, "C11_T2": 181.48,
               "C44_M1": 127.62, "C44_M2": 127.51, "C44_T1": 127.04, "C44_T2": 126.92},
        2300: {"C11_M1": 180.00, "C11_M2": 177.95, "C11_T1": 177.61, "C11_T2": 175.44,
               "C44_M1": 126.11, "C44_M2": 125.97, "C44_T1": 125.45, "C44_T2": 125.31},
        2400: {"C11_M1": 174.73, "C11_M2": 172.30, "C11_T1": 172.02, "C11_T2": 169.44,
               "C44_M1": 124.62, "C44_M2": 124.44, "C44_T1": 123.86, "C44_T2": 123.67},
        2500: {"C11_M1": 169.55, "C11_M2": 166.70, "C11_T1": 166.51, "C11_T2": 163.48,
               "C44_M1": 123.13, "C44_M2": 122.93, "C44_T1": 122.27, "C44_T2": 122.05},
        2600: {"C11_M1": 164.46, "C11_M2": 161.18, "C11_T1": 161.09, "C11_T2": 157.58,
               "C44_M1": 121.66, "C44_M2": 121.41, "C44_T1": 120.69, "C44_T2": 120.43},
        2700: {"C11_M1": 159.47, "C11_M2": 155.73, "C11_T1": 155.76, "C11_T2": 151.74,
               "C44_M1": 120.21, "C44_M2": 119.91, "C44_T1": 119.12, "C44_T2": 118.81},
        2800: {"C11_M1": 154.59, "C11_M2": 150.35, "C11_T1": 150.51, "C11_T2": 145.96,
               "C44_M1": 118.74, "C44_M2": 118.41, "C44_T1": 117.55, "C44_T2": 117.19}
    }
    return {
        "gold": gold,
        "tolerance": 1.0,
        "series_cols": ["C11_M1","C11_M2","C11_T1","C11_T2","C44_M1","C44_M2","C44_T1","C44_T2"]
    }


# === block: score_0 (check id='compare_values') ===
def score_0(artifact, step, ctx):
    rows = artifact
    row_by_T = {}
    for r in rows:
        try:
            t = int(float(r["T"]))
            row_by_T[t] = r
        except:
            pass
    gold = ctx["gold"]
    tol = ctx["tolerance"]
    total = 0
    correct = 0
    for T, gold_row in gold.items():
        if T not in row_by_T:
            continue
        row = row_by_T[T]
        for col in gold_row:
            total += 1
            try:
                if abs(float(row[col]) - gold_row[col]) <= tol:
                    correct += 1
            except:
                pass
    if total == 0:
        return 0.0
    return correct / total


# === block: score_1 (check id='monotonic_trend') ===
def score_1(artifact, step, ctx):
    if len(artifact) < 2:
        return 0.0
    series_cols = ctx["series_cols"]
    try:
        sorted_rows = sorted(artifact, key=lambda r: int(float(r["T"])))
    except:
        return 0.0
    violations = 0
    n_series = len(series_cols)
    n_pairs = len(sorted_rows) - 1
    for col in series_cols:
        for i in range(n_pairs):
            try:
                v1 = float(sorted_rows[i][col])
                v2 = float(sorted_rows[i+1][col])
                if v2 > v1 + 1e-6:
                    violations += 1
            except:
                violations += 1
    total_checks = n_series * n_pairs
    if total_checks == 0:
        return 0.0
    return max(0.0, 1.0 - violations / total_checks)


_SCORERS = {
    'compare_values': score_0,
    'monotonic_trend': score_1,
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
