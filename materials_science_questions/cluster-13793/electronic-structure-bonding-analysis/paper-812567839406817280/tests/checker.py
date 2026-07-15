import os
import json
import csv

# === author imports / helpers ===
import csv
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


# === block: score_0 (check id='bulk_properties') ===
def score_0(artifact, step, ctx):
    rows = artifact
    ref = step["reference"]
    tol = step["tolerances"]
    total_props = 0
    correct_props = 0
    for row in rows:
        phase = row.get("phase", "").strip()
        if phase not in ref:
            continue
        expected = ref[phase]
        for key, exp_val in expected.items():
            if exp_val is None:
                continue
            val_str = row.get(key, "").strip()
            if val_str == "":
                continue
            try:
                val = float(val_str)
            except ValueError:
                continue
            tolerance = tol.get(key, 1e-6)
            if abs(val - exp_val) <= tolerance:
                correct_props += 1
            total_props += 1
    if total_props == 0:
        return 0.0
    return correct_props / total_props


# === block: score_1 (check id='interface_energetics') ===
def score_1(artifact, step, ctx):
    rows = artifact
    ref = step["reference"]
    tol = step["tolerances"]
    total_checks = 0
    passed_checks = 0
    for expected in ref:
        term = expected["termination"].strip().lower()
        stack = expected["stacking"].strip().lower()
        found = False
        for row in rows:
            if row.get("termination", "").strip().lower() == term and row.get("stacking", "").strip().lower() == stack:
                found = True
                # d0_nm: smaller is better -> val <= ref + tol
                key = "d0_nm"
                total_checks += 1
                try:
                    val = float(row.get(key, 0))
                except (ValueError, TypeError):
                    val = None
                if val is not None and val <= expected[key] + tol.get(key, 0):
                    passed_checks += 1
                # W_ad_J_per_m2: larger is better -> val >= ref - tol
                key = "W_ad_J_per_m2"
                total_checks += 1
                try:
                    val = float(row.get(key, 0))
                except (ValueError, TypeError):
                    val = None
                if val is not None and val >= expected[key] - tol.get(key, 0):
                    passed_checks += 1
                # gamma_int_J_per_m2: smaller is better -> val <= ref + tol
                key = "gamma_int_J_per_m2"
                total_checks += 1
                try:
                    val = float(row.get(key, 0))
                except (ValueError, TypeError):
                    val = None
                if val is not None and val <= expected[key] + tol.get(key, 0):
                    passed_checks += 1
                break
        if not found:
            total_checks += 3
    # ordering checks
    ti_on_row = None
    for row in rows:
        if row.get("termination", "").strip().lower() == "ti centre" and row.get("stacking", "").strip().lower() == "on":
            ti_on_row = row
            break
    if ti_on_row:
        ti_on_wad = float(ti_on_row.get("W_ad_J_per_m2", -1e9))
        ti_on_gamma = float(ti_on_row.get("gamma_int_J_per_m2", 1e9))
        all_wads = []
        all_gammas = []
        for row in rows:
            try:
                all_wads.append(float(row.get("W_ad_J_per_m2", -1e9)))
                all_gammas.append(float(row.get("gamma_int_J_per_m2", 1e9)))
            except (ValueError, TypeError):
                pass
        total_checks += 1
        if all_wads and ti_on_wad == max(all_wads):
            passed_checks += 1
        total_checks += 1
        if all_gammas and ti_on_gamma == min(all_gammas):
            passed_checks += 1
    else:
        total_checks += 2
    if total_checks == 0:
        return 0.0
    return passed_checks / total_checks


_SCORERS = {
    'bulk_properties': score_0,
    'interface_energetics': score_1,
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
