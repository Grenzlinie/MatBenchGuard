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
        step = next(s for s in spec['steps'] if s['id'] == 'step_03')
        ctx = {
            'gold_ratio': step['gold_ratio_at_tc'],
            'ratio_tol': step['ratio_tolerance'],
            'gold_dists': step['gold_distortion'],
            'dist_tol': step['distortion_tolerance'],
            'intervals': step['intervals']
        }
        return ctx


# === block: score_0 (check id='step_03') ===
def score_0(artifact, step, ctx):
        rows = artifact
        # Gold values taken directly from the step spec (robust; ctx may be broken)
        gold_ratio = step['gold_ratio_at_tc']
        ratio_tol = step['ratio_tolerance']
        gold_dists = step['gold_distortion']
        dist_tol = step['distortion_tolerance']
        intervals = step['intervals']

        required_cols = {'tau','sigma','Gamma100','Gamma110','Gamma200','ratio','dbeta_beta'}
        if not rows or not required_cols.issubset(rows[0].keys()):
            return 0.0
        shape_score = 1.0

        # Ratio at tau=0
        ratio_score = 0.0
        for r in rows:
            tau_str = (r.get('tau') or '').strip()
            if not tau_str:
                continue
            try:
                tau = float(tau_str)
            except (ValueError, TypeError):
                continue
            if abs(tau) < 1e-12:
                ratio_str = (r.get('ratio') or '').strip()
                if ratio_str:
                    try:
                        r_val = float(ratio_str)
                    except (ValueError, TypeError):
                        pass
                    else:
                        if abs(r_val - gold_ratio) <= ratio_tol:
                            ratio_score = 1.0
                break

        # Distortion check: find rows with non-empty dbeta_beta near interval centers
        interval_scores = []
        for lo, hi, g_dist in zip([iv[0] for iv in intervals], [iv[1] for iv in intervals], gold_dists):
            mid_expected = (lo * hi) ** 0.5
            found_val = None
            for r in rows:
                dbeta_str = (r.get('dbeta_beta') or '').strip()
                if not dbeta_str:
                    continue
                try:
                    tau_f = float((r.get('tau') or '').strip())
                except (ValueError, TypeError):
                    continue
                if mid_expected > 0 and abs(tau_f - mid_expected) / mid_expected < 0.01:
                    try:
                        found_val = float(dbeta_str)
                    except (ValueError, TypeError):
                        pass
                    break
            if found_val is not None and abs(found_val - g_dist) <= dist_tol:
                interval_scores.append(1.0)
            else:
                interval_scores.append(0.0)
        distortion_score = sum(interval_scores) / len(interval_scores) if interval_scores else 0.0

        total = 0.05 * shape_score + 0.3 * ratio_score + 0.65 * distortion_score
        return total


_SCORERS = {
    'step_03': score_0,
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
