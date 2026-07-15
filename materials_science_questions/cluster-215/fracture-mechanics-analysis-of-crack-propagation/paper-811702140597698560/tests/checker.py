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


# === block: score_0 (check id='pt_table_verification') ===
def score_0(artifact, step, ctx):
    import csv, os

    def _find_row(rows, r, b, t):
        for row in rows:
            try:
                rv = float(row['r'])
                bv = float(row['b'])
                tv = float(row['t'])
            except (ValueError, KeyError):
                continue
            if abs(rv - r) < 1e-6 and abs(bv - b) < 1e-6 and abs(tv - t) < 1e-6:
                try:
                    return float(row['pt'])
                except (ValueError, KeyError):
                    return None
        return None

    optimal = step.get('optimal_row', {})
    ref_rows = step.get('reference_rows', [])
    weights = step.get('score_weights', {'optimal': 0.5, 'trend': 0.5})
    tol_rel = step.get('tolerance_relative', 0.10)

    # Optimal-condition score
    opt_score = 0.0
    opt_pt = _find_row(artifact, optimal.get('r'), optimal.get('b'), optimal.get('t'))
    if opt_pt is not None:
        threshold = float(optimal.get('pt_threshold', 0.97))
        if opt_pt >= threshold:
            opt_score = 1.0
        else:
            # partial credit: linear from threshold-0.17 to threshold
            lower = threshold - 0.17
            if lower < 0:
                lower = 0.0
            opt_score = max(0.0, (opt_pt - lower) / (threshold - lower))

    # Trend agreement score
    trend_scores = []
    for ref in ref_rows:
        rv = float(ref.get('r'))
        bv = float(ref.get('b'))
        tv = float(ref.get('t'))
        ref_pt = float(ref.get('pt'))
        agent_pt = _find_row(artifact, rv, bv, tv)
        if agent_pt is None:
            trend_scores.append(0.0)
            continue
        if abs(ref_pt) < 1e-9:
            trend_scores.append(0.0)
        else:
            re = abs(agent_pt - ref_pt) / abs(ref_pt)
            if re <= tol_rel:
                trend_scores.append(1.0)
            else:
                # partial credit, decays as error grows
                trend_scores.append(max(0.0, 1.0 - (re - tol_rel) / (5 * tol_rel)))

    if trend_scores:
        trend_score = sum(trend_scores) / len(trend_scores)
    else:
        trend_score = 0.0

    # Weighted combination
    final_score = weights.get('optimal', 0.5) * opt_score + weights.get('trend', 0.5) * trend_score
    return max(0.0, min(1.0, final_score))


_SCORERS = {
    'pt_table_verification': score_0,
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
