import os
import json
import csv

# === author imports / helpers ===
import os
import json
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
    gold_data = {}
    for step in spec.get("steps", []):
        gold_data[step["id"]] = step.get("gold_data", {})
    return {"gold_data": gold_data}


# === block: score_0 (check id='step04_formation_energies_and_lattice') ===
def score_0(artifact, step, ctx):
    compounds = artifact.get("compounds", [])
    refs = artifact.get("elemental_references", {})
    if not compounds or not refs:
        return 0.0
    Au = refs.get("Au_fcc", 0)
    Ni = refs.get("Ni_fcc", 0)
    Pd = refs.get("Pd_fcc", 0)
    Sn = refs.get("Sn_beta", 0)
    gold = ctx["gold_data"]["step04_formation_energies_and_lattice"]
    gold_map = {c["name"]: c for c in gold.get("compounds", [])}
    total_score = 0.0
    for comp in compounds:
        name = comp.get("name")
        if name not in gold_map:
            continue
        g = gold_map[name]
        E = comp.get("total_energy_per_fu")
        if E is None:
            continue
        if name == "AuSn4":
            E_ref = Au + 4 * Sn
        elif "Ni" in name and "Pd" not in name:
            if "0.75" in name:
                x_Ni, x_Au = 0.25, 0.75
            elif "0.5" in name:
                x_Ni, x_Au = 0.5, 0.5
            else:
                continue
            E_ref = x_Ni * Ni + x_Au * Au + 4 * Sn
        elif "Pd" in name and "Ni" not in name:
            if "0.75" in name:
                x_Pd, x_Au = 0.25, 0.75
            elif "0.5" in name:
                x_Pd, x_Au = 0.5, 0.5
            else:
                continue
            E_ref = x_Pd * Pd + x_Au * Au + 4 * Sn
        elif "Pd" in name and "Ni" in name:
            E_ref = 0.25 * Pd + 0.25 * Ni + 0.5 * Au + 4 * Sn
        else:
            continue
        dH = (E - E_ref) / 5.0 * 96.485307
        gold_dH = g["delta_H_kJ_per_mol_atoms"]
        err = abs(dH - gold_dH) / (abs(gold_dH) + 1e-09)
        if err <= 0.05:
            s = 1.0
        elif err >= 0.20:
            s = 0.0
        else:
            s = 1.0 - (err - 0.05) / 0.15
        total_score += s * (0.30 / 6.0)
        a = comp.get("a")
        b = comp.get("b")
        c = comp.get("c")
        V = comp.get("volume")
        ga = g["a"]
        gb = g["b"]
        gc = g["c"]
        gV = g["volume"]
        errors = [
            abs(a - ga) / (abs(ga) + 1e-09),
            abs(b - gb) / (abs(gb) + 1e-09),
            abs(c - gc) / (abs(gc) + 1e-09),
            abs(V - gV) / (abs(gV) + 1e-09)
        ]
        lattice_ok = all(e <= 0.02 for e in errors)
        total_score += (1.0 if lattice_ok else 0.0) * (0.10 / 6.0)
    ref_ok = all(isinstance(v, (int, float)) and v < 0 for v in [Au, Ni, Pd, Sn])
    total_score += (1.0 if ref_ok else 0.0) * 0.05
    # Scale up so that perfect match yields 1.0 instead of 0.45
    scale = 1.0 / 0.45
    total_score *= scale
    return min(1.0, total_score)


# === block: score_1 (check id='step06_elastic_and_thermodynamic') ===
def score_1(artifact, step, ctx):
    import os
    import json
    compounds = artifact.get("compounds", [])
    gold = ctx["gold_data"]["step06_elastic_and_thermodynamic"]
    gold_map = {c["name"]: c for c in gold.get("compounds", [])}
    total_score = 0.0
    tol_elastic = 0.10
    tol_moduli = 0.10
    tol_theta = 0.15
    tol_kmin = 0.15
    ef = ["C11", "C22", "C33", "C44", "C55", "C66", "C12", "C13", "C23"]
    mf = ["Bulk_modulus_VRH", "Shear_modulus_VRH", "Young_modulus", "Poisson_ratio", "Hardness"]
    for comp in compounds:
        name = comp.get("name")
        if name not in gold_map:
            continue
        g = gold_map[name]
        for f in ef:
            val = comp.get(f, 0.0)
            gval = max(1e-09, abs(g.get(f, 0.0)))
            err = abs(val - g.get(f, 0.0)) / gval
            s = 1.0 - err / tol_elastic
            total_score += max(0.0, s) * (0.15 / 9 / 6.0)
        for f in mf:
            val = comp.get(f, 0.0)
            gval = max(1e-09, abs(g.get(f, 0.0)))
            err = abs(val - g.get(f, 0.0)) / gval
            s = 1.0 - err / tol_moduli
            total_score += max(0.0, s) * (0.15 / 5 / 6.0)
        valD = comp.get("Debye_temperature", 0.0)
        gvalD = max(1e-09, abs(g.get("Debye_temperature", 0.0)))
        s = 1.0 - abs(valD - gvalD) / gvalD / tol_theta
        total_score += max(0.0, s) * (0.10 / 6.0)
        valK = comp.get("kmin", 0.0)
        gvalK = max(1e-09, abs(g.get("kmin", 0.0)))
        s = 1.0 - abs(valK - gvalK) / gvalK / tol_kmin
        total_score += max(0.0, s) * (0.05 / 6.0)
    trend_score = 0.0
    fpath = "/app/outputs/formation_energies_and_lattice.json"
    if os.path.exists(fpath):
        with open(fpath) as f:
            fdata = json.load(f)
        dH = {c["name"]: c["delta_H_kJ_per_mol_atoms"] for c in fdata.get("compounds", [])}
        nu = {c["name"]: c["Poisson_ratio"] for c in compounds}
        if dH.get("AuSn4", 0) > dH.get("Au0.75Ni0.25Sn4", 999) > dH.get("Au0.5Ni0.5Sn4", 999):
            trend_score += 0.05
        if dH.get("Au0.75Pd0.25Sn4", 0) < dH.get("Au0.5Pd0.5Sn4", 0):
            trend_score += 0.02
        if nu.get("AuSn4", 0) > nu.get("Au0.75Ni0.25Sn4", 999) > nu.get("Au0.5Ni0.5Sn4", 999):
            trend_score += 0.03
    total_score += trend_score
    return min(1.0, total_score)


_SCORERS = {
    'step04_formation_energies_and_lattice': score_0,
    'step06_elastic_and_thermodynamic': score_1,
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
