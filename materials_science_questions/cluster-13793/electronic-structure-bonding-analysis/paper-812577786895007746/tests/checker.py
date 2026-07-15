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
    def prepare(outputs_dir, spec):
        ref_data = spec.get("reference_data", {})
        energies_ref = {r["cluster"]: r for r in ref_data.get("energies_and_gaps", [])}
        charges_ref = {r["cluster"]: r for r in ref_data.get("mulliken_charges", [])}
        return {"energies_ref": energies_ref, "charges_ref": charges_ref}


# === block: score_0 (check id='check_energies_and_gaps') ===
def score_0(artifact, step, ctx):
    def _safe_float(v, default):
        """Convert v to float, returning default if v is None or invalid."""
        if v is None:
            return default
        try:
            return float(v)
        except (TypeError, ValueError):
            return default

    energies_ref = ctx.get("energies_ref", {})
    gap_tol = _safe_float(step.get("gap_tolerance"), 0.1)
    bind_tol = _safe_float(step.get("binding_energy_tolerance"), 0.1)
    pristine_gap = _safe_float(step.get("pristine_gap"), 0.869)
    pristine_bind = _safe_float(step.get("pristine_binding_energy"), 6.083)
    special_tms = step.get("special_binding_tms", []) or []

    def _to_float(v):
        if v is None:
            return None
        try:
            return float(v)
        except (TypeError, ValueError):
            return None

    def _get_val(ag, key):
        # safely get a float from agent row, None if missing/non-numeric
        raw = ag.get(key)
        if raw is None:
            return None
        return _to_float(raw)

    agent_map = {row.get("cluster"): row for row in artifact if row.get("cluster")}
    total = 0
    satisfied = 0
    for cluster, ref in energies_ref.items():
        ag = agent_map.get(cluster)
        # gap similarity
        total += 1
        if ag is not None:
            gap_val = _get_val(ag, "gap_eV")
            gap_ref = _to_float(ref.get("gap_eV"))
            if gap_val is not None and gap_ref is not None and abs(gap_val - gap_ref) <= gap_tol:
                satisfied += 1
        # binding similarity
        total += 1
        if ag is not None:
            bind_val = _get_val(ag, "binding_energy_eV_per_atom")
            bind_ref = _to_float(ref.get("binding_energy_eV_per_atom"))
            if bind_val is not None and bind_ref is not None and abs(bind_val - bind_ref) <= bind_tol:
                satisfied += 1
        # gap inequality for TM clusters
        if cluster != "B36":
            total += 1
            if ag is not None:
                gap_val = _get_val(ag, "gap_eV")
                if gap_val is not None and gap_val < pristine_gap:
                    satisfied += 1
        # binding inequality for special TMs
        if cluster in special_tms:
            total += 1
            if ag is not None:
                bind_val = _get_val(ag, "binding_energy_eV_per_atom")
                if bind_val is not None and bind_val > pristine_bind:
                    satisfied += 1
    if total == 0:
        return 0.0
    return satisfied / total


# === block: score_1 (check id='check_mulliken_charges') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        charges_ref = ctx.get("charges_ref", {})
        charge_tol = float(step.get("charge_tolerance", 0.5))
        covalent_thresh = float(step.get("covalent_threshold", 1.7))
        agent_map = {row["cluster"]: row for row in artifact}
        total = 0
        satisfied = 0
        for cluster, ref in charges_ref.items():
            ag = agent_map.get(cluster)
            if ag is None:
                total += 2
                continue
            try:
                charge = float(ag.get("net_charge_e", 0))
            except:
                charge = 0.0
            # charge similarity
            if abs(charge - float(ref["net_charge_e"])) <= charge_tol:
                satisfied += 1
            total += 1
            # covalent condition
            if abs(charge) < covalent_thresh:
                satisfied += 1
            total += 1
        if total == 0:
            return 0.0
        return satisfied / total


_SCORERS = {
    'check_energies_and_gaps': score_0,
    'check_mulliken_charges': score_1,
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
