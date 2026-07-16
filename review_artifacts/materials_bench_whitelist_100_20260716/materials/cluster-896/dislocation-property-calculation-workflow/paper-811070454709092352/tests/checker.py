import os
import json
import csv

# === author imports / helpers ===
import csv, math, os


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
    gold_rows = spec["gold_rows"]
    return {"gold_rows": gold_rows}


# === block: score_0 (check id='step_04_results') ===
def score_0(artifact, step, ctx):
        artifact_rows = artifact  # list of dicts from csv
        gold_rows = ctx["gold_rows"]

        def find_row(epsilon, s_f, tol=1e-9):
            for row in artifact_rows:
                try:
                    e = float(row["epsilon"])
                    s = float(row["s_f"])
                    if abs(e - epsilon) < tol and abs(s - s_f) < tol:
                        return row
                except (ValueError, KeyError):
                    continue
            return None

        n_total = len(gold_rows)
        if n_total == 0:
            return 0.0

        p_ok = 0
        fd_ok = 0

        for gr in gold_rows:
            epsilon = gr["epsilon"]
            s_f = gr["s_f"]
            ref_P = gr["P"]
            ref_fd = gr["free_energy_derivative"]
            row = find_row(epsilon, s_f)
            if row is None:
                continue
            try:
                p_val = float(row["P"])
                fd_val = float(row["free_energy_derivative"])
            except (ValueError, KeyError):
                continue
            if abs(p_val - ref_P) <= 0.05:
                p_ok += 1
            if ref_fd != 0 and abs(fd_val - ref_fd) <= 0.15 * abs(ref_fd):
                fd_ok += 1

        p_score = p_ok / n_total
        fd_score = fd_ok / n_total

        # Trend checks
        def extract_ordered_values(s_f_val):
            points = []
            for row in artifact_rows:
                try:
                    s = float(row["s_f"])
                    if abs(s - s_f_val) < 1e-9:
                        eps = float(row["epsilon"])
                        p = float(row["P"])
                        fd = float(row["free_energy_derivative"])
                        points.append((eps, p, fd))
                except (ValueError, KeyError):
                    continue
            points.sort(key=lambda x: x[0])
            return points

        trends = []
        for s_f_val in [0.0, 0.10825]:
            pts = extract_ordered_values(s_f_val)
            if len(pts) >= 2:
                p_mono = all(pts[i][1] <= pts[i+1][1] for i in range(len(pts)-1))
                trends.append(p_mono)
                fd_mono = all(pts[i][2] <= pts[i+1][2] for i in range(len(pts)-1))
                trends.append(fd_mono)
            else:
                trends.append(False)
                trends.append(False)

        isotropic_rows = [r for r in artifact_rows if abs(float(r["s_f"]) - 0.0) < 1e-9]
        anisotropic_rows = [r for r in artifact_rows if abs(float(r["s_f"]) - 0.10825) < 1e-9]
        iso_greater = True
        for i_row in isotropic_rows:
            eps = float(i_row["epsilon"])
            p_i = float(i_row["P"])
            found = False
            for a_row in anisotropic_rows:
                if abs(float(a_row["epsilon"]) - eps) < 1e-9:
                    p_a = float(a_row["P"])
                    if p_i <= p_a:
                        iso_greater = False
                    found = True
                    break
            if found and not iso_greater:
                break
        trends.append(iso_greater)

        trend_score = sum(trends) / len(trends) if trends else 0.0

        total = 0.5 * p_score + 0.3 * fd_score + 0.2 * trend_score
        return min(1.0, max(0.0, total))


_SCORERS = {
    'step_04_results': score_0,
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
