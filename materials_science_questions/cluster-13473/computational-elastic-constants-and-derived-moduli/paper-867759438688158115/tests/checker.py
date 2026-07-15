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
    return {"gold": spec.get("gold", {})}


# === block: score_0 (check id='shear_modulus_check') ===
def score_0(artifact, step, ctx):
    gold_tables = ctx.get("gold", {})
    shear_gold = gold_tables.get("shear_modulus", {})
    rows = artifact
    if not rows or not isinstance(rows, list):
        return 0.0
    scores = []
    for row in rows:
        try:
            sys = str(row.get("system", "")).strip()
            Z = str(int(float(row.get("Z", 0))))
            G = float(row.get("G", 0))
        except:
            continue
        gold_val = shear_gold.get(sys, {}).get(Z)
        if gold_val is None:
            continue
        # relative tolerance 10%, absolute floor 0.01
        tol = max(0.01, 0.1 * abs(gold_val))
        if abs(G - gold_val) <= tol:
            scores.append(1.0)
        else:
            scores.append(0.0)
    expected_rows = 8  # 2 systems * 4 Z values
    if len(scores) == 0:
        return 0.0
    score = sum(scores) / expected_rows
    return max(0.0, min(1.0, score))


# === block: score_1 (check id='order_parameters_check') ===
def score_1(artifact, step, ctx):
    gold_tables = ctx.get("gold", {})
    order_gold = gold_tables.get("order_parameters", {})
    F_IS_gold = order_gold.get("F_IS", {})
    F_6_gold = order_gold.get("F_6", {})
    rows = artifact
    if not rows or not isinstance(rows, list):
        return 0.0
    scores = []
    for row in rows:
        try:
            sys = str(row.get("system", "")).strip()
            Z = str(int(float(row.get("Z", 0))))
            F_IS = float(row.get("F_IS", 0))
            F_6 = float(row.get("F_6", 0))
        except:
            continue
        # Check F_IS
        gold_F_IS = F_IS_gold.get(sys, {}).get(Z)
        fis_ok = False
        if gold_F_IS is not None:
            tol_F_IS = max(0.01, 0.05 * abs(gold_F_IS))
            if abs(F_IS - gold_F_IS) <= tol_F_IS:
                fis_ok = True
        # Check F_6
        f6_ok = False
        expected_F6 = F_6_gold.get(sys)
        if expected_F6 is not None:
            if abs(F_6 - expected_F6) <= 0.05:
                f6_ok = True
        # both must pass for that row to count as 1
        if fis_ok and f6_ok:
            scores.append(1.0)
        else:
            scores.append(0.0)
    expected_rows = 8
    if len(scores) == 0:
        return 0.0
    score = sum(scores) / expected_rows
    return max(0.0, min(1.0, score))


# === block: score_2 (check id='boson_peak_check') ===
def score_2(artifact, step, ctx):
    gold_tables = ctx.get("gold", {})
    bp_gold = gold_tables.get("boson_peak", {})
    rows = artifact
    if not rows or not isinstance(rows, list):
        return 0.0
    scores = []
    for row in rows:
        try:
            sys = str(row.get("system", "")).strip()
            Z = str(int(float(row.get("Z", 0))))
            w = float(row.get("omega_BP", 0))
        except:
            continue
        gold_w = bp_gold.get(sys, {}).get(Z)
        if gold_w is None:
            continue
        tol = max(0.01, 0.03 * abs(gold_w))
        if abs(w - gold_w) <= tol:
            scores.append(1.0)
        else:
            scores.append(0.0)
    expected_rows = 8
    if len(scores) == 0:
        return 0.0
    score = sum(scores) / expected_rows
    return max(0.0, min(1.0, score))


# === block: score_3 (check id='dos_consistency_check') ===
def score_3(artifact, step, ctx):
    import json, os
    # Load dos_data.json (artifact already provided as dict)
    dos_data = artifact
    # We need to read boson_peak.csv as well to get reported omega_BP
    # The checker scaffold will pass artifact for dos_data.json only; we need to access other files.
    # But we can load the file manually from /app/outputs/boson_peak.csv
    bp_path = "/app/outputs/boson_peak.csv"
    if not os.path.exists(bp_path):
        return 0.0
    import csv
    bp_rows = []
    with open(bp_path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            bp_rows.append(row)
    # Build dict: (system, Z) -> reported omega_BP
    omega_bp_reported = {}
    for row in bp_rows:
        sys = row.get("system", "").strip()
        try:
            Z = str(int(float(row.get("Z", 0))))
            w = float(row.get("omega_BP", 0))
        except:
            continue
        omega_bp_reported[(sys, Z)] = w

    required_keys = [
        "RN_Z6", "RN_Z7", "RN_Z8", "RN_Z9",
        "FCC_Z6", "FCC_Z7", "FCC_Z8", "FCC_Z9"
    ]
    scores = []
    for key in required_keys:
        if key not in dos_data:
            continue
        data = dos_data[key]
        freqs = data.get("frequencies", [])
        dos = data.get("dos", [])
        if len(freqs) < 3 or len(dos) != len(freqs):
            continue
        # compute reduced DOS: dos / w^2
        reduced = []
        for i, w in enumerate(freqs):
            if w > 1e-6:
                reduced.append(dos[i] / (w * w))
            else:
                reduced.append(0.0)
        if not reduced:
            continue
        max_idx = max(range(len(reduced)), key=lambda i: reduced[i])
        peak_freq = freqs[max_idx]
        # get reported omega_BP for this system and Z
        parts = key.split("_")
        if len(parts) != 2:
            continue
        sys, Z_str = parts[0], parts[1]
        Z = Z_str[1:]  # e.g. '6'
        rep_w = omega_bp_reported.get((sys, Z))
        if rep_w is None:
            continue
        # tolerance: bin width max (take first bin difference) or 0.02
        if len(freqs) > 1:
            bin_width = freqs[1] - freqs[0]
        else:
            bin_width = 0.02
        tol = max(2 * bin_width, 0.02)
        if abs(peak_freq - rep_w) <= tol:
            scores.append(1.0)
        else:
            scores.append(0.0)
    if not scores:
        return 0.0
    score = sum(scores) / len(required_keys)
    return max(0.0, min(1.0, score))


_SCORERS = {
    'shear_modulus_check': score_0,
    'order_parameters_check': score_1,
    'boson_peak_check': score_2,
    'dos_consistency_check': score_3,
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
