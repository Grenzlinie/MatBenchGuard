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
    return {"hidden": spec.get("hidden", {})}


# === block: score_0 (check id='step_compile') ===
def score_0(artifact, step, ctx):
    data = artifact
    hidden = ctx.get("hidden", {})
    gold = hidden.get("gold", {})
    tol = hidden.get("tolerances", {})
    w = hidden.get("weights", {})

    def ramp(target, value, falloff):
        if falloff <= 0:
            return 1.0 if abs(value - target) < 1e-9 else 0.0
        return max(0.0, 1.0 - abs(value - target) / falloff)

    sub = {}

    # 1. energy difference consistency: recompute from FM/AFM energies
    fm = data['fm_total_energy_per_fu_Ry']
    afm = data['afm_total_energy_per_fu_Ry']
    reported_ediff = abs(data['energy_difference_meV_per_fu'])
    computed_ediff_mev = (afm - fm) * 13605.7
    consistency_ok = abs(reported_ediff - abs(computed_ediff_mev)) < tol.get('ediff_consistency_tol_meV', 1.0)
    sub['ediff_consistency'] = 1.0 if consistency_ok else 0.0

    sub['ediff_gold'] = ramp(gold['energy_difference_meV_per_fu'], reported_ediff, tol.get('ediff_gold_falloff_meV', 2.0))

    # 2. Ni spin moment
    sub['ni_spin'] = ramp(gold['ni_spin_moment_muB'], data['ni_spin_moment_muB'], tol.get('ni_spin_falloff_muB', 0.4))

    # 3. total spin moment
    sub['total_spin'] = ramp(gold['total_spin_moment_per_fu_muB'], data['total_spin_moment_per_fu_muB'], tol.get('total_spin_falloff_muB', 0.4))

    # 4. band gap
    sub['band_gap'] = ramp(gold['band_gap_fm_down_spin_eV'], data['band_gap_fm_down_spin_eV'], tol.get('band_gap_falloff_eV', 0.5))

    # 5. exchange J
    sub['exchange_J'] = ramp(gold['exchange_J_K'], data['exchange_J_K'], tol.get('exchange_J_falloff_K', 6.0))

    # 6. Ni orbital moment
    sub['ni_orbital'] = ramp(gold['ni_orbital_moment_soc_muB'], data['ni_orbital_moment_soc_muB'], tol.get('ni_orbital_falloff_muB', 0.08))

    # 7. Pt orbital moment
    sub['pt_orbital'] = ramp(gold['pt_orbital_moment_soc_muB'], data['pt_orbital_moment_soc_muB'], tol.get('pt_orbital_falloff_muB', 0.05))

    # 8. effective paramagnetic moment: recompute from spin moment and Ni orbital moment
    M = data['total_spin_moment_per_fu_muB']
    S = M / 2.0
    spin_only_eff = 2.0 * math.sqrt(S * (S + 1.0))
    recomputed_eff = spin_only_eff + data['ni_orbital_moment_soc_muB']
    reported_eff = data['effective_paramagnetic_moment_muB']
    eff_consistency = abs(reported_eff - recomputed_eff) < tol.get('effective_paramagnetic_consistency_tol_muB', 0.3)
    sub['effective_paramagnetic_consistency'] = 1.0 if eff_consistency else 0.0

    sub['effective_paramagnetic_gold'] = ramp(gold['effective_paramagnetic_moment_muB'], reported_eff, tol.get('effective_paramagnetic_gold_falloff_muB', 1.0))

    # aggregate weighted sum
    total = 0.0
    for k in w:
        total += w[k] * sub.get(k, 0.0)
    return min(1.0, total)


_SCORERS = {
    'step_compile': score_0,
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
