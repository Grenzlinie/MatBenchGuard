import os
import json
import csv

# === author imports / helpers ===
def is_within_tolerance(val, gold, tol_config):
    abs_tol = tol_config.get("abs")
    if abs_tol is not None:
        return abs(val - gold) <= abs_tol
    rel_tol = tol_config.get("rel", 0.15)
    abs_near_zero = tol_config.get("abs_near_zero", 0.02)
    near_zero_bound = tol_config.get("near_zero_threshold", 0.05)
    if abs(gold) < near_zero_bound:
        return abs(val - gold) <= abs_near_zero
    else:
        return abs(val - gold) <= rel_tol * abs(gold)


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


# === block: score_0 (check id='flux_kj') ===
def score_0(artifact, step, ctx):
    # scorer for flux_kj
            gold_rows = step["gold"]
            tol = step["tolerance"]
            total = len(gold_rows)
            if total == 0:
                return 1.0
            correct = 0
            for gref in gold_rows:
                rad = gref["normalized_patch_radius"]
                gold_val = gref["kJ"]
                found_match = None
                for row in artifact:
                    try:
                        r = float(row["normalized_patch_radius"])
                        if abs(r - rad) < 1e-6:
                            found_match = row
                            break
                    except (ValueError, KeyError):
                        continue
                if found_match is None:
                    continue
                try:
                    val = float(found_match["kJ"])
                except (ValueError, KeyError):
                    continue
                if is_within_tolerance(val, gold_val, tol):
                    correct += 1
            return correct / total


# === block: score_1 (check id='center_velocity') ===
def score_1(artifact, step, ctx):
    # scorer for center_velocity
            gold_rows = step["gold"]
            tol = step["tolerance"]
            total = len(gold_rows)
            if total == 0:
                return 1.0
            correct = 0
            for gref in gold_rows:
                rad = gref["normalized_patch_radius"]
                m_exp = int(gref["creep_exponent_m"])
                ctype = gref["contact_type"]
                gold_v = gref["v0_div_v_inf"]
                found_match = None
                for row in artifact:
                    try:
                        r = float(row["normalized_patch_radius"])
                        m_val = int(float(row["creep_exponent_m"]))
                        ct = str(row["contact_type"]).strip()
                        if abs(r - rad) < 1e-6 and m_val == m_exp and ct == ctype:
                            found_match = row
                            break
                    except (ValueError, KeyError):
                        continue
                if found_match is None:
                    continue
                try:
                    val = float(found_match["v0_div_v_inf"])
                except (ValueError, KeyError):
                    continue
                if is_within_tolerance(val, gold_v, tol):
                    correct += 1
            return correct / total


# === block: score_2 (check id='threshold') ===
def score_2(artifact, step, ctx):
    # scorer for threshold
            gold = step["gold"]
            tol = step["tolerance"]
            target_m = gold["creep_exponent_m"]
            target_d = gold["threshold_diameter_um"]
            for row in artifact:
                try:
                    m_val = int(float(row["creep_exponent_m"]))
                    if m_val == target_m:
                        val = float(row["threshold_diameter_um"])
                        if is_within_tolerance(val, target_d, tol):
                            return 1.0
                        else:
                            return 0.0
                except (ValueError, KeyError):
                    continue
            return 0.0


_SCORERS = {
    'flux_kj': score_0,
    'center_velocity': score_1,
    'threshold': score_2,
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
