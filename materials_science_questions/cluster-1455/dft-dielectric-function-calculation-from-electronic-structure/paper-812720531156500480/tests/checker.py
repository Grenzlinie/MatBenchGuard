import os
import json
import csv

# === author imports / helpers ===
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


# === block: score_0 (check id='check_band_gaps') ===
def score_0(artifact, step, ctx):
        if not isinstance(artifact, dict):
            return 0.0
        gold = step.get('gold', {})
        gga_gold = gold.get('GGA_TS', {})
        lda_gold = gold.get('LDA', {})
        tol = gold.get('tolerance', 0.1)

        # --- GGA_TS ---
        gga = artifact.get('GGA_TS')
        gga_ok = False
        if isinstance(gga, dict):
            gap_type = gga.get('gap_type')
            direct_gap = gga.get('direct_gap')
            if gap_type == gga_gold.get('gap_type'):
                if gap_type == 'direct':
                    if isinstance(direct_gap, (int, float)) and abs(direct_gap - gga_gold['direct_gap']) <= gga_gold.get('tolerance', tol):
                        gga_ok = True

        # --- LDA ---
        lda = artifact.get('LDA')
        lda_subscore = 0.0
        if isinstance(lda, dict):
            gap_type = lda.get('gap_type')
            indirect_gaps = lda.get('indirect_gaps')
            if gap_type == lda_gold.get('gap_type'):
                if isinstance(indirect_gaps, list) and len(indirect_gaps) > 0:
                    sorted_gaps = sorted(v for v in indirect_gaps if isinstance(v, (int, float)))
                    if sorted_gaps:
                        smallest = sorted_gaps[0]
                        target_smallest = 4.91   # paper explicitly reports smallest indirect gap
                        lda_tol = lda_gold.get('tolerance', tol)

                        type_score = 1.0
                        smallest_score = 1.0 if abs(smallest - target_smallest) <= lda_tol else 0.0
                        # All gaps should lie within the paper's reported range 4.91–5.0 eV (extended by tolerance)
                        in_range = all(target_smallest - lda_tol <= v <= 5.0 + lda_tol for v in sorted_gaps)
                        range_score = 1.0 if in_range else 0.0

                        # Number of gaps is not penalised; it may vary with implementation.
                        lda_subscore = (type_score + smallest_score + range_score) / 3.0

        gga_score = 1.0 if gga_ok else 0.0
        lda_score = lda_subscore
        total = (gga_score + lda_score) / 2.0
        return min(1.0, max(0.0, total))


# === block: score_1 (check id='check_optical_constants') ===
def score_1(artifact, step, ctx):
    def score_optical_constants(artifact, step, ctx):
        if not isinstance(artifact, dict):
            return 0.0
        gold = step.get('gold', {})
        required_pairs = [
            ('GGA_TS', 'epsilon1_0'),
            ('GGA_TS', 'refractive_index_0'),
            ('LDA', 'epsilon1_0'),
            ('LDA', 'refractive_index_0'),
        ]
        correct = 0
        total = len(required_pairs)
        for func, key in required_pairs:
            func_gold = gold.get(func, {})
            if not isinstance(func_gold, dict):
                continue
            target = func_gold.get(key)
            tol = func_gold.get('tolerance', 0.2)
            if target is None:
                continue
            actual = artifact.get(func, {})
            if isinstance(actual, dict):
                val = actual.get(key)
                if isinstance(val, (int, float)) and abs(val - target) <= tol:
                    correct += 1
        return correct / total if total > 0 else 0.0


_SCORERS = {
    'check_band_gaps': score_0,
    'check_optical_constants': score_1,
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
