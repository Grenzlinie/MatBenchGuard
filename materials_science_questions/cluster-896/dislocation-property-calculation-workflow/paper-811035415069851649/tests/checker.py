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
    def prepare(outputs_dir, spec):
        ctx = {}
        for step in spec.get('steps', []):
            sid = step['id']
            ctx[sid] = {
                'gold_values': step.get('gold_values', {}),
                'tolerance': step.get('target_tolerance', 0.02),
                'monotonic': step.get('monotonic', False),
                'peak_required': step.get('peak_required', False),
                'peak_range': step.get('peak_range', None)
            }
        # ensure monotonic flag for coated D
        if 'coated_torsional_rigidity' in ctx:
            ctx['coated_torsional_rigidity']['monotonic'] = True
        return ctx


# === block: score_0 (check id='homogeneous_torsional_rigidity') ===
def score_0(artifact, step, ctx):
    if artifact is None:
        return 0.0

    info = ctx[step["id"]]
    gold_vals = info["gold_values"]
    tol = info["tolerance"]
    data = {}
    la_key = "l/a"
    d_key = "normalized_D"

    for row in artifact:
        try:
            if not isinstance(row, dict):
                continue
            # find la key, stripping BOM
            la_val = None
            for k in row:
                if k.lstrip('\ufeff') == la_key:
                    la_val = str(row[k]).strip()
                    break
            if la_val is None:
                continue
            d_val = None
            for k in row:
                if k.lstrip('\ufeff') == d_key:
                    raw = row[k]
                    if raw is None:
                        continue
                    try:
                        d_val = float(str(raw).strip())
                    except (ValueError, TypeError):
                        continue
                    break
            if d_val is None:
                continue
            data[la_val] = d_val
        except Exception:
            continue

    scores = []
    for la_key_gold, gold in gold_vals.items():
        if la_key_gold in data:
            val = data[la_key_gold]
            rel_err = abs(val - gold) / max(abs(gold), 1e-12)
            if rel_err <= tol:
                scores.append(1.0)
            else:
                scores.append(max(0.0, 1.0 - (rel_err - tol)/tol))
        else:
            scores.append(0.0)
    if not scores:
        return 0.0
    return sum(scores)/len(scores)


# === block: score_1 (check id='homogeneous_sif') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        info = ctx[step["id"]]
        gold_vals = info["gold_values"]
        tol = info["tolerance"]
        data = {}
        for row in artifact:
            try:
                la = str(row["l/a"]).strip()
                val = float(row["normalized_SIF"])
                data[la] = val
            except:
                pass
        scores = []
        for la_key, gold in gold_vals.items():
            if la_key in data:
                val = data[la_key]
                rel_err = abs(val - gold) / max(abs(gold), 1e-12)
                if rel_err <= tol:
                    scores.append(1.0)
                else:
                    scores.append(max(0.0, 1.0 - (rel_err - tol)/tol))
            else:
                scores.append(0.0)
        if not scores:
            return 0.0
        return sum(scores)/len(scores)


# === block: score_2 (check id='coated_torsional_rigidity') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        info = ctx[step["id"]]
        gold_vals = info["gold_values"]
        tol = info["tolerance"]
        data = {}
        for row in artifact:
            try:
                la = str(row["l/a"]).strip()
                val = float(row["normalized_D"])
                data[la] = val
            except:
                pass
        scores = []
        for la_key, gold in gold_vals.items():
            if la_key in data:
                val = data[la_key]
                rel_err = abs(val - gold) / max(abs(gold), 1e-12)
                if rel_err <= tol:
                    scores.append(1.0)
                else:
                    scores.append(max(0.0, 1.0 - (rel_err - tol)/tol))
            else:
                scores.append(0.0)
        numeric_score = sum(scores)/len(scores) if scores else 0.0
        sorted_items = sorted([(float(k), v) for k, v in data.items() if k in gold_vals], key=lambda x: x[0])
        if len(sorted_items) >= 2:
            vals = [v for _, v in sorted_items]
            monotonic = all(vals[i+1] <= vals[i] + 1e-9 for i in range(len(vals)-1))
        else:
            monotonic = True
        monotonic_score = 1.0 if monotonic else 0.0
        return 0.8 * numeric_score + 0.2 * monotonic_score


# === block: score_3 (check id='coated_sif') ===
def score_3(artifact, step, ctx):
    def score(artifact, step, ctx):
        info = ctx[step["id"]]
        gold_vals = info["gold_values"]
        tol = info["tolerance"]
        data = {}
        for row in artifact:
            try:
                la = str(row["l/a"]).strip()
                val = float(row["normalized_SIF"])
                data[la] = val
            except:
                pass
        scores = []
        for la_key, gold in gold_vals.items():
            if la_key in data:
                val = data[la_key]
                rel_err = abs(val - gold) / max(abs(gold), 1e-12)
                if rel_err <= tol:
                    scores.append(1.0)
                else:
                    scores.append(max(0.0, 1.0 - (rel_err - tol)/tol))
            else:
                scores.append(0.0)
        numeric_score = sum(scores)/len(scores) if scores else 0.0
        sorted_items = sorted([(float(k), v) for k, v in data.items() if k in gold_vals], key=lambda x: x[0])
        if not sorted_items:
            peak_score = 0.0
        else:
            max_val = max(item[1] for item in sorted_items)
            peak_las = [item[0] for item in sorted_items if item[1] >= max_val - 1e-9]
            peak_la = max(peak_las) if peak_las else sorted_items[-1][0]
            if 0.3 <= peak_la <= 0.7:
                peak_score = 1.0
            else:
                peak_score = 0.0
        return 0.8 * numeric_score + 0.2 * peak_score


_SCORERS = {
    'homogeneous_torsional_rigidity': score_0,
    'homogeneous_sif': score_1,
    'coated_torsional_rigidity': score_2,
    'coated_sif': score_3,
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
