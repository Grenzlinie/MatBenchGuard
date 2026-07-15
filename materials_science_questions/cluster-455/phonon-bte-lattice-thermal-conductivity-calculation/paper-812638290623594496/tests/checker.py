import os
import json
import csv

# === author imports / helpers ===
import csv, os, math


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


# === block: score_0 (check id='bulk_kpar') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        rows = artifact
        conditions = step.get('conditions', [])
        total = len(conditions)
        score_sum = 0.0
        for cond in conditions:
            T_target = cond['T']
            gold = cond['kappa_parallel']
            tol_rel = cond.get('tolerance_rel', 0.2)
            tol_abs_val = abs(gold * tol_rel)
            best_row = None
            min_diff = float('inf')
            for r in rows:
                try:
                    t = float(r.get('T', '').strip())
                    diff = abs(t - T_target)
                    if diff < min_diff:
                        min_diff = diff
                        best_row = r
                except (ValueError, TypeError):
                    continue
            if best_row is None or min_diff > 1.0:
                continue
            try:
                val = float(best_row.get('kappa_parallel', '').strip())
            except (ValueError, TypeError):
                continue
            if abs(val - gold) <= tol_abs_val:
                score_sum += 1.0
        return score_sum / total if total > 0 else 0.0


# === block: score_1 (check id='bulk_kperp') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        rows = artifact
        if not rows:
            return 0.0
        conds = step.get('conditions', [])
        total = len(conds)
        if total == 0:
            return 0.0
        score_sum = 0.0
        for cond in conds:
            target_T = cond['T']
            gold = cond['kappa_perp']
            tol = cond.get('tolerance_abs', 0.1)
            best_row = None
            min_diff = float('inf')
            for row in rows:
                try:
                    t = float(row.get('T', '').strip())
                except (ValueError, TypeError):
                    continue
                diff = abs(t - target_T)
                if diff < min_diff:
                    min_diff = diff
                    best_row = row
            if best_row is None:
                continue
            try:
                val = float(best_row.get('kappa_perp', '').strip())
            except (ValueError, TypeError):
                continue
            if abs(val - gold) <= tol:
                score_sum += 1.0
        return score_sum / total if total > 0 else 0.0


# === block: score_2 (check id='thin_film_numeric') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        rows = artifact
        expected = step.get('expected', {})
        tol_abs = step.get('tolerance_abs', 0.1)
        total = len(expected)
        score_sum = 0.0
        for thick_str, gold in expected.items():
            thickness = int(thick_str)
            best_row = None
            min_diff = float('inf')
            for r in rows:
                try:
                    t = int(float(r.get('thickness_nm', '').strip()))
                    diff = abs(t - thickness)
                    if diff < min_diff:
                        min_diff = diff
                        best_row = r
                except (ValueError, TypeError):
                    continue
            if best_row is None or min_diff > 1:
                continue
            try:
                val = float(best_row.get('kappa_perp', '').strip())
            except (ValueError, TypeError):
                continue
            if abs(val - gold) <= tol_abs:
                score_sum += 1.0
        return score_sum / total if total > 0 else 0.0


# === block: score_3 (check id='thin_film_monotonic') ===
def score_3(artifact, step, ctx):
    def score(artifact, step, ctx):
        rows = artifact
        vals = []
        for row in rows:
            try:
                thick = int(float(row.get('thickness_nm', '').strip()))
                kp = float(row.get('kappa_perp', '').strip())
                vals.append((thick, kp))
            except (ValueError, TypeError):
                continue
        vals.sort(key=lambda x: x[0])
        if len(vals) < 2:
            return 0.0
        for i in range(1, len(vals)):
            if vals[i][1] > vals[i-1][1] + 1e-9:
                return 0.0
        return 1.0


_SCORERS = {
    'bulk_kpar': score_0,
    'bulk_kperp': score_1,
    'thin_film_numeric': score_2,
    'thin_film_monotonic': score_3,
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
