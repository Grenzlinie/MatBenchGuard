import os
import json
import csv

# === author imports / helpers ===
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
        ctx = {}
        steps = spec.get("steps", [])
        for s in steps:
            ctx[s["id"]] = {
                "tol": s.get("tolerance", {}),
                "gold": s.get("gold_table", {})
            }
        return ctx


# === block: score_0 (check id='check_complex_zfs') ===
def score_0(artifact, step, ctx):
        tol = ctx["check_complex_zfs"]["tol"]
        gold = ctx["check_complex_zfs"]["gold"]
        if not artifact:
            return 0.0
        rows = {}
        for r in artifact:
            cid = str(r.get("Complex", "")).strip()
            if cid in ("1","2","3"):
                rows[cid] = r
        correct = 0
        for cid, gvals in gold.items():
            row = rows.get(cid)
            if not row:
                continue
            try:
                D = float(row.get("D_cm⁻¹", 0))
                ED = float(row.get("E_over_D", 0))
            except (ValueError, TypeError):
                continue
            if abs(D - gvals["D_cm⁻¹"]) <= tol.get("D_cm⁻¹", 0.5) and abs(ED - gvals["E_over_D"]) <= tol.get("E_over_D", 0.05):
                correct += 1
        # return fraction of matched rows (max 3)
        return correct / max(len(gold), 1)


# === block: score_1 (check id='check_dihedral_scan') ===
def score_1(artifact, step, ctx):
        tol = ctx["check_dihedral_scan"]["tol"]
        gold = ctx["check_dihedral_scan"]["gold"]
        if not artifact:
            return 0.0
        # Build list of (theta_deg, row) from artifact
        rows = []
        for r in artifact:
            try:
                theta = float(r.get("theta_d_deg", None))
                rows.append((theta, r))
            except (ValueError, TypeError):
                continue
        theta_tol = 0.05   # tight tolerance for dihedral angle matching
        correct = 0
        for gtheta_str, gvals in gold.items():
            try:
                target_theta = float(gtheta_str)
            except ValueError:
                continue
            # locate the artifact row with theta within tolerance
            best_row = None
            for theta, row in rows:
                if abs(theta - target_theta) <= theta_tol:
                    best_row = row
                    break
            if best_row is None:
                continue
            try:
                D = float(best_row.get("D_cm⁻¹", 0))
                ED = float(best_row.get("E_over_D", 0))
            except (ValueError, TypeError):
                continue
            if abs(D - gvals["D_cm⁻¹"]) <= tol.get("D_cm⁻¹", 0.5) and abs(ED - gvals["E_over_D"]) <= tol.get("E_over_D", 0.05):
                correct += 1
        return correct / max(len(gold), 1)


_SCORERS = {
    'check_complex_zfs': score_0,
    'check_dihedral_scan': score_1,
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
