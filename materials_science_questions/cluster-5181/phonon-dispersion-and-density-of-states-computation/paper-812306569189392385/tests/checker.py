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
    gold_table = None
    for step in spec.get("steps", []):
        if step.get("id") == "freq_match":
            gold_table = step.get("gold_table", [])
            break
    return {"gold_table": gold_table}


# === block: score_0 (check id='freq_match') ===
def score_0(artifact, step, ctx):
    gold_table = ctx.get("gold_table", [])
    if not artifact:
        return 0.0
    from collections import defaultdict
    rows_by_key = defaultdict(list)
    for row in artifact:
        kp = row.get("k_point", "").strip().lower()
        branch = row.get("branch", "").strip().upper()
        rows_by_key[(kp, branch)].append(row)
    scores = []
    for gold in gold_table:
        kp = gold["k_point"].lower()
        branch = gold["branch"]
        matching = rows_by_key.get((kp, branch))
        if not matching:
            scores.append(0.0)
            continue
        row = matching[0]
        freq_str = row.get("frequency_cm1", "")
        try:
            freq = float(freq_str)
        except Exception:
            freq = None
        if freq is None:
            scores.append(0.0)
            continue
        expected = gold["frequency"]
        tol = gold["tolerance"]
        dev = abs(freq - expected)
        if dev <= tol:
            s = 1.0
        else:
            over = dev - tol
            scale = 2 * tol
            s = max(0.0, 1.0 - over / scale)
        scores.append(s)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_1 (check id='structure') ===
def score_1(artifact, step, ctx):
    if not artifact:
        return 0.0
    # coverage: all required (k_point, branch) from hidden gold must be present
    gold_table = ctx.get("gold_table", [])
    required = set((g.get("k_point", "").strip().lower(), g.get("branch", "").strip().upper()) for g in gold_table)
    present = set()
    for row in artifact:
        kp = (row.get("k_point", "") or "").strip().lower()
        branch = (row.get("branch", "") or "").strip().upper()
        if kp and branch:
            present.add((kp, branch))
    if not required.issubset(present):
        return 0.0
    # LO-TO degeneracy at Gamma
    gamma_lo = None
    gamma_to = None
    for row in artifact:
        if row.get("k_point","").strip().lower() == "gamma":
            br = row.get("branch","").strip().upper()
            freq_str = row.get("frequency_cm1","")
            try:
                f = float(freq_str)
            except:
                continue
            if br == "LO":
                gamma_lo = f
            elif br == "TO":
                gamma_to = f
    if gamma_lo is not None and gamma_to is not None:
        deg_score = 1.0 if abs(gamma_lo - gamma_to) <= 5.0 else 0.0
    else:
        deg_score = 0.0
    # Gamma acoustic branches must be near zero
    acoustic = {"LA", "TA", "ZA"}
    zero_check = True
    for row in artifact:
        if row.get("k_point","").strip().lower() == "gamma":
            br = row.get("branch","").strip().upper()
            if br in acoustic:
                try:
                    f = float(row.get("frequency_cm1",""))
                except:
                    zero_check = False
                    break
                if abs(f) > 10.0:
                    zero_check = False
                    break
    acoustic_score = 1.0 if zero_check else 0.0
    return 0.5 * deg_score + 0.5 * acoustic_score


_SCORERS = {
    'freq_match': score_0,
    'structure': score_1,
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
