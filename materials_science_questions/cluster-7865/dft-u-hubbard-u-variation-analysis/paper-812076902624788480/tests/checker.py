import os
import json
import csv

# === author imports / helpers ===
import json, math


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
    gold_data = {}
    for step in spec.get("steps", []):
        if step.get("id") == "step1":
            gold_data = step.get("gold", {})
            break
    return {"step1_gold": gold_data}


# === block: score_0 (check id='step1') ===
def score_0(artifact, step, ctx):
    gold = ctx.get("step1_gold", {})
    if not gold or not isinstance(artifact, dict):
        return 0.0
    if "configurations" not in artifact or "derived_exchange_couplings" not in artifact:
        return 0.0
    configs = artifact["configurations"]
    if not isinstance(configs, list) or len(configs) != 4:
        return 0.0

    gold_cfgs = {c["magnetic_ordering"]: c for c in gold.get("configurations", [])}
    tolerances = gold.get("tolerances", {})
    gold_exch = gold.get("exchange", {})
    if len(gold_cfgs) != 4:
        return 0.0

    agent_cfgs = {}
    for c in configs:
        ordering = c.get("magnetic_ordering", "")
        if ordering not in gold_cfgs:
            return 0.0
        agent_cfgs[ordering] = c

    # sub-scores
    total_energy_score = 0.0
    spin_score = 0.0
    gap_score = 0.0
    n = len(gold_cfgs)
    tol_energy = tolerances.get("total_energy_meV", 10)
    tol_spin = tolerances.get("spin_moment_muB", 0.05)
    tol_gap = tolerances.get("band_gap_eV", 0.2)

    for ord_name, gc in gold_cfgs.items():
        ac = agent_cfgs[ord_name]
        diff_e = abs(ac.get("total_energy_meV", 0) - gc["total_energy_meV"])
        if diff_e <= tol_energy:
            total_energy_score += 1.0
        elif diff_e <= 3 * tol_energy:
            total_energy_score += 0.5
        diff_s = abs(ac.get("spin_moment_muB", 0) - gc["spin_moment_muB"])
        if diff_s <= tol_spin:
            spin_score += 1.0
        elif diff_s <= 3 * tol_spin:
            spin_score += 0.5
        diff_g = abs(ac.get("band_gap_eV", 0) - gc["band_gap_eV"])
        if diff_g <= tol_gap:
            gap_score += 1.0
        elif diff_g <= 3 * tol_gap:
            gap_score += 0.5

    total_energy_score /= n
    spin_score /= n
    gap_score /= n

    # ordering check
    afm_e = agent_cfgs["AFM"]["total_energy_meV"]
    faf_e = agent_cfgs["F+AF"]["total_energy_meV"]
    aff_e = agent_cfgs["AF+F"]["total_energy_meV"]
    fm_e = agent_cfgs["FM"]["total_energy_meV"]
    ordering_ok = (afm_e <= min(faf_e, aff_e, fm_e) and abs(faf_e - afm_e) <= 5.0 and (aff_e - afm_e) > 40.0 and (fm_e - afm_e) > 40.0)
    ordering_score = 1.0 if ordering_ok else 0.0

    # exchange recompute
    j_inter_mev = agent_cfgs["F+AF"]["total_energy_meV"] - afm_e
    j_intra_mev = agent_cfgs["AF+F"]["total_energy_meV"] - afm_e
    j_inter_K = j_inter_mev * 11.6045
    j_intra_K = j_intra_mev * 11.6045
    diff_j_inter = abs(j_inter_K - gold_exch.get("J_inter_K", 7))
    diff_j_intra = abs(j_intra_K - gold_exch.get("J_intra_K", 626))

    def eval_exch(diff, tol):
        if diff <= tol:
            return 1.0
        elif diff <= 3 * tol:
            return 0.5
        return 0.0

    jinter_score = eval_exch(diff_j_inter, tolerances.get("J_inter_K", 3))
    jintra_score = eval_exch(diff_j_intra, tolerances.get("J_intra_K", 50))

    final = (0.3 * total_energy_score + 0.15 * spin_score + 0.15 * gap_score +
             0.2 * ordering_score + 0.1 * jinter_score + 0.1 * jintra_score)
    return final


_SCORERS = {
    'step1': score_0,
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
