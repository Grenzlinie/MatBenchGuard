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


# === block: score_0 (check id='value_fidelity') ===
def score_0(artifact, step, ctx):
    gold_rows = step.get("gold_data", [])
    if not gold_rows:
        return 1.0
    tol = step.get("tolerances", {})
    ps_tol = tol.get("polaron_shift_meV", {})
    abs_tol_ps = ps_tol.get("abs_tol", 5.0)
    rel_tol_ps = ps_tol.get("rel_tol", 0.2)
    sw_tol = tol.get("spectral_weight_transfer_percent", {})
    abs_tol_sw = sw_tol.get("abs_tol", 10.0)

    # Build index from agent rows
    agent_index = {}
    for row in artifact:
        key = (row.get("tube_id", "").strip(), row.get("phonon_mode", "").strip(), int(float(row.get("temperature_K", 0))))
        agent_index[key] = row

    passed = 0
    for gold in gold_rows:
        key = (gold["tube_id"], gold["phonon_mode"], int(gold["temperature_K"]))
        agent_row = agent_index.get(key)
        if agent_row is None:
            continue
        try:
            ps_agent = float(agent_row.get("polaron_shift_meV", None))
            sw_agent = float(agent_row.get("spectral_weight_transfer_percent", None))
        except (ValueError, TypeError):
            continue
        ps_gold = float(gold["polaron_shift_meV"])
        sw_gold = float(gold["spectral_weight_transfer_percent"])
        diff_ps = abs(ps_agent - ps_gold)
        rel_ps = diff_ps / (abs(ps_gold) if ps_gold != 0 else 1.0)
        ps_ok = (diff_ps <= abs_tol_ps) and (rel_ps <= rel_tol_ps)
        sw_ok = abs(sw_agent - sw_gold) <= abs_tol_sw
        if ps_ok and sw_ok:
            passed += 1
    return passed / len(gold_rows) if gold_rows else 1.0


# === block: score_1 (check id='trends') ===
def score_1(artifact, step, ctx):
    def monotonic_non_increasing(values):
        """Return True if the sequence is non-increasing (each <= previous)."""
        return all(v2 <= v1 for v1, v2 in zip(values, values[1:]))

    def check_series(rows, sort_key_field, sort_numeric, phonon_mode, value_field):
        """Given a list of rows, sort by sort_key_field, extract value_field, and return True if monotonic."""
        filtered = [r for r in rows if r.get("phonon_mode", "").strip() == phonon_mode]
        if len(filtered) < 2:
            return None   # cannot check
        # Attempt to sort by sort_key_field
        sorted_rows = sorted(filtered, key=lambda r: float(r.get(sort_key_field, 0)))
        vals = []
        for r in sorted_rows:
            try:
                vals.append(float(r.get(value_field)))
            except (ValueError, TypeError):
                return False
        return monotonic_non_increasing(vals)

    rows = artifact
    if not rows:
        return 0.0

    # Extract zigzag rows (tube_id starts with 'zigzag_') and kataura rows (tube_id contains 'kataura')
    zigzag_rows = [r for r in rows if r.get("tube_id", "").startswith("zigzag_")]
    kataura_rows = [r for r in rows if "kataura" in r.get("tube_id", "").lower()]

    checks = []
    # Zigzag rows: diameter_nm
    if zigzag_rows:
        checks.append(check_series(zigzag_rows, "diameter_nm", True, "Gamma-LO", "polaron_shift_meV"))
        checks.append(check_series(zigzag_rows, "diameter_nm", True, "Gamma-LO", "spectral_weight_transfer_percent"))
        checks.append(check_series(zigzag_rows, "diameter_nm", True, "K", "polaron_shift_meV"))
        checks.append(check_series(zigzag_rows, "diameter_nm", True, "K", "spectral_weight_transfer_percent"))

    # Kataura rows: chiral_angle_deg
    if kataura_rows:
        checks.append(check_series(kataura_rows, "chiral_angle_deg", True, "Gamma-LO", "polaron_shift_meV"))
        checks.append(check_series(kataura_rows, "chiral_angle_deg", True, "Gamma-LO", "spectral_weight_transfer_percent"))
        checks.append(check_series(kataura_rows, "chiral_angle_deg", True, "K", "polaron_shift_meV"))
        checks.append(check_series(kataura_rows, "chiral_angle_deg", True, "K", "spectral_weight_transfer_percent"))

    # Filter out None (insufficient data)
    valid_checks = [c for c in checks if c is not None]
    if not valid_checks:
        return 1.0
    passed = sum(1 for c in valid_checks if c)
    return passed / len(valid_checks)


_SCORERS = {
    'value_fidelity': score_0,
    'trends': score_1,
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
