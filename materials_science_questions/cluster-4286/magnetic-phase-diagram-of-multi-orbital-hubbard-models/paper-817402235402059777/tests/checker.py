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
    return {}


# === block: score_0 (check id='step1_vertex_convergence') ===
def score_0(artifact, step, ctx):
    def parse_float_or_none(val):
        try:
            return float(val)
        except (ValueError, TypeError):
            return None

    # Group rows by N_alpha, compute mean relative difference from frequency rows only.
    freq_rows = []
    for row in artifact:
        try:
            omega_idx = row.get('omega_index', '').strip()
            int(omega_idx)  # if it's numeric (frequency row)
            freq_rows.append(row)
        except ValueError:
            pass  # skip summary rows

    if not freq_rows:
        return 0.0

    from collections import defaultdict
    sum_rel = defaultdict(float)
    count = defaultdict(int)
    for row in freq_rows:
        n_alpha_val = row.get('N_alpha', '').strip()
        if n_alpha_val == '':
            continue
        try:
            N = int(n_alpha_val)
        except ValueError:
            continue
        rd = parse_float_or_none(row.get('relative_difference', ''))
        if rd is None:
            continue
        sum_rel[N] += rd
        count[N] += 1

    mean_rel = {}
    for N in sorted(sum_rel):
        if count[N] > 0:
            mean_rel[N] = sum_rel[N] / count[N]

    # Required N_alpha values
    required = [2, 4, 6, 8, 10]

    # Check thresholds
    score_n4 = 0.0
    score_n6 = 0.0
    score_mono = 0.0

    if 4 in mean_rel:
        if mean_rel[4] <= 1e-4:
            score_n4 = 1.0

    if 6 in mean_rel:
        if mean_rel[6] <= 1e-5:
            score_n6 = 1.0

    # Monotonic non-increasing: for consecutive N in required, if both present check decreasing
    mono = True
    values = [mean_rel.get(n) for n in required]
    for i in range(len(required) - 1):
        a = values[i]
        b = values[i+1]
        if a is None or b is None:
            mono = False
            break
        if a < b:
            mono = False
            break
    if mono:
        score_mono = 1.0

    total = 0.4 * score_n4 + 0.4 * score_n6 + 0.2 * score_mono
    return round(total, 6)


_SCORERS = {
    'step1_vertex_convergence': score_0,
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
