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
    step0 = spec["steps"][0]
    return {"gold": step0["gold"], "tolerances": step0.get("tolerances", {})}


# === block: score_0 (check id='check_csv') ===
def score_0(artifact, step, ctx):
    import math

    # Get gold and tolerances from ctx
    gold = ctx["gold"]
    tolerances = ctx["tolerances"]
    structures = gold["structures"]

    # artifact is already a list of dicts from load_artifact
    rows = artifact

    # Build dict by structure name (lowercased)
    agent_data = {}
    for r in rows:
        name = r.get("structure", "").strip().lower()
        agent_data[name] = r

    # Helper to get float or None
    def to_float(v):
        if v is None or v == '' or v == 'NA' or v == 'N/A':
            return None
        try:
            return float(v)
        except (ValueError, TypeError):
            return None

    # Scoring sub-functions
    def score_lattice(struct_name, ref, agent):
        a_ref = ref["lattice_parameter_a_nm"]
        c_ref = ref.get("lattice_parameter_c_nm")
        a_agent = to_float(agent.get("lattice_parameter_a_nm"))
        c_agent = to_float(agent.get("lattice_parameter_c_nm"))
        rel_tol = tolerances["lattice_relative"]
        # Score a
        if a_ref is not None and a_agent is not None:
            diff = abs(a_agent - a_ref) / a_ref
            if diff <= rel_tol:
                score_a = 1.0
            elif diff <= 2 * rel_tol:
                score_a = max(0.0, 1.0 - (diff - rel_tol) / rel_tol)
            else:
                score_a = 0.0
        else:
            score_a = 0.0
        # Score c if applicable
        if c_ref is not None and c_agent is not None:
            diff = abs(c_agent - c_ref) / c_ref
            if diff <= rel_tol:
                score_c = 1.0
            elif diff <= 2 * rel_tol:
                score_c = max(0.0, 1.0 - (diff - rel_tol) / rel_tol)
            else:
                score_c = 0.0
            return 0.5 * (score_a + score_c)
        else:
            return score_a

    def score_dielectric(struct_name, ref, agent):
        rel_tol = tolerances["dielectric_relative"]
        scores = []
        for field in ["dielectric_eps0", "dielectric_epsinf"]:
            ref_val = ref.get(field)
            agent_val = to_float(agent.get(field))
            if ref_val is not None and agent_val is not None:
                diff = abs(agent_val - ref_val) / max(abs(ref_val), 1e-9)
                if diff <= rel_tol:
                    scores.append(1.0)
                elif diff <= 2 * rel_tol:
                    scores.append(max(0.0, 1.0 - (diff - rel_tol) / rel_tol))
                else:
                    scores.append(0.0)
        for field in ["eps0_11", "eps0_33", "epinf_11", "epinf_33"]:
            ref_val = ref.get(field)
            agent_val = to_float(agent.get(field))
            if ref_val is not None and agent_val is not None:
                diff = abs(agent_val - ref_val) / max(abs(ref_val), 1e-9)
                if diff <= rel_tol:
                    scores.append(1.0)
                elif diff <= 2 * rel_tol:
                    scores.append(max(0.0, 1.0 - (diff - rel_tol) / rel_tol))
                else:
                    scores.append(0.0)
        if not scores:
            return 1.0  # no applicable fields, treat as satisfied
        return sum(scores) / len(scores)

    def score_energy(struct_name, ref, agent):
        abs_tol = tolerances["energy_absolute"]
        fields = ["ionic_cohesive_energy_eV", "total_lattice_energy_eV"]
        scores = []
        for field in fields:
            ref_val = ref.get(field)
            agent_val = to_float(agent.get(field))
            if ref_val is not None and agent_val is not None:
                diff = abs(agent_val - ref_val)
                if diff <= abs_tol:
                    scores.append(1.0)
                elif diff <= 2 * abs_tol:
                    scores.append(max(0.0, 1.0 - (diff - abs_tol) / abs_tol))
                else:
                    scores.append(0.0)
            else:
                scores.append(0.0)
        if not scores:
            return 0.0
        return sum(scores) / len(scores)

    def score_ospe_consistency(struct_name, ref, agent):
        ospf_add = ref.get("ospf_addition", 0.0)
        ionic = to_float(agent.get("ionic_cohesive_energy_eV"))
        total = to_float(agent.get("total_lattice_energy_eV"))
        if ionic is None or total is None:
            return 0.0
        expected_total = ionic + ospf_add
        if abs(total - expected_total) < 0.001:
            return 1.0
        else:
            return 0.0

    # Compute overall scores
    lattice_scores = []
    dielectric_scores = []
    energy_scores = []
    ospe_scores = []
    total_energies = []

    for struct_key, ref in structures.items():
        agent = agent_data.get(struct_key.lower())
        if agent is None:
            lattice_scores.append(0.0)
            dielectric_scores.append(0.0)
            energy_scores.append(0.0)
            ospe_scores.append(0.0)
            continue
        lattice_scores.append(score_lattice(struct_key, ref, agent))
        dielectric_scores.append(score_dielectric(struct_key, ref, agent))
        energy_scores.append(score_energy(struct_key, ref, agent))
        ospe_scores.append(score_ospe_consistency(struct_key, ref, agent))
        total = to_float(agent.get("total_lattice_energy_eV"))
        if total is not None:
            total_energies.append((struct_key.lower(), total))

    avg_lattice = sum(lattice_scores) / len(lattice_scores) if lattice_scores else 1.0
    avg_dielectric = sum(dielectric_scores) / len(dielectric_scores) if dielectric_scores else 1.0
    avg_energy = sum(energy_scores) / len(energy_scores) if energy_scores else 1.0
    avg_ospe = sum(ospe_scores) / len(ospe_scores) if ospe_scores else 1.0

    # Ordering check
    ordering_score = 0.0
    energies_map = {k: v for k, v in total_energies}
    rock = energies_map.get("rock salt")
    wurt = energies_map.get("wurtzite")
    zb = energies_map.get("zinc blende")
    if rock is not None and wurt is not None and zb is not None:
        if rock < wurt < zb:
            ordering_score = 1.0
        elif rock <= wurt <= zb:
            ordering_score = 0.5
        else:
            ordering_score = 0.0

    sub_weights = {"lattice": 0.3, "dielectric": 0.3, "energy": 0.2, "ospe": 0.15, "ordering": 0.05}
    final_score = (avg_lattice * sub_weights["lattice"] +
                   avg_dielectric * sub_weights["dielectric"] +
                   avg_energy * sub_weights["energy"] +
                   avg_ospe * sub_weights["ospe"] +
                   ordering_score * sub_weights["ordering"])
    return final_score


_SCORERS = {
    'check_csv': score_0,
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
