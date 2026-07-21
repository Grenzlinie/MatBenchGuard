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
    gold = {}; 
    for s in spec.get("steps", []):
        if s["id"] == "critical_radii":
            gold["critical"] = {"values": s.get("gold", {}), "tolerances": s.get("tolerance_abs", {})};
        elif s["id"] == "validation_energy":
            gold["validation"] = s.get("gold", None);
            gold["tol_rel"] = s.get("tolerance_rel", 0.5);
    return {"gold": gold}


# === block: score_0 (check id='critical_radii') ===
def score_0(artifact, step, ctx):
    import csv, os, math

    def score(artifact, step, ctx):
        # Safely retrieve gold context
        try:
            gold_crit = ctx.get("gold", {}).get("critical", None)
        except Exception:
            gold_crit = None
        if not isinstance(gold_crit, dict):
            return 0.0

        gold_values = gold_crit.get("values", {})
        tolerances = gold_crit.get("tolerances", {})
        if not isinstance(gold_values, dict) or not gold_values:
            return 0.0

        if not artifact or len(artifact) != 3:
            return 0.0

        rows = {}
        for row in artifact:
            try:
                f = float(row["f"])
                r = float(row["R_u_star"])
            except (ValueError, KeyError, TypeError):
                return 0.0
            rows[f] = r

        expected_fs = [0.01, 0.02, 0.03]
        if set(rows.keys()) != set(expected_fs):
            return 0.0

        shape_ok = 1.0
        value_scores = []

        for fv in expected_fs:
            gr = gold_values.get(str(fv), gold_values.get(fv, None))
            if gr is None:
                value_scores.append(0.0)
                continue
            try:
                gr = float(gr)
                tol = float(tolerances.get(str(fv), 5.0))
            except (ValueError, TypeError):
                value_scores.append(0.0)
                continue

            r = rows[fv]
            if abs(r - gr) <= tol:
                value_scores.append(1.0)
            else:
                err = abs(r - gr)
                if err <= tol * 2.0:
                    val = max(0.0, 1.0 - (err - tol) / tol)
                else:
                    val = 0.0
                value_scores.append(val)

        value_score = sum(value_scores) / len(value_scores) if value_scores else 0.0

        # monotonicity check
        sorted_fs = sorted(expected_fs)
        r_list = [rows[f] for f in sorted_fs]
        monotonic = 1.0 if (r_list[0] >= r_list[1] >= r_list[2]) else 0.0

        total = 0.1 * shape_ok + 0.7 * value_score + 0.2 * monotonic
        return total


# === block: score_1 (check id='validation_energy') ===
def score_1(artifact, step, ctx):
    import json, os, math

    def score(artifact, step, ctx):
        gold_val = ctx["gold"]["validation"]
        tol_rel = ctx["gold"].get("tol_rel", 0.5)
        if not isinstance(artifact, dict):
            return 0.0
        if "f" not in artifact or "R_u" not in artifact or "E0_star" not in artifact:
            return 0.0
        try:
            f = float(artifact["f"])
            ru = float(artifact["R_u"])
            e0 = float(artifact["E0_star"])
        except (ValueError, TypeError):
            return 0.0
        shape_ok = 1.0 if (abs(f - 0.01) < 1e-6 and abs(ru - 30.0) < 1e-6) else 0.0
        # compare to gold
        gr = float(gold_val)
        if abs(gr) < 1e-20:
            val_score = 1.0 if abs(e0) < 1e-20 else 0.0
        else:
            err = abs(e0 - gr) / abs(gr)
            if err <= tol_rel:
                val_score = 1.0
            else:
                val_score = max(0.0, 1.0 - (err - tol_rel) / tol_rel)
        total = 0.1 * shape_ok + 0.9 * val_score
        return total


_SCORERS = {
    'critical_radii': score_0,
    'validation_energy': score_1,
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
