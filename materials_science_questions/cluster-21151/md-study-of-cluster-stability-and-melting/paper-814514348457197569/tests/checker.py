import os
import json
import csv

# === author imports / helpers ===
import yaml
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


# === block: score_0 (check id='step_ws_defects') ===
def score_0(artifact, step, ctx):
    rows = artifact
    required_cols = ["cell_type","recoil_energy_eV","temperature_K","avg_antisites","avg_vacancies","avg_interstitials"]
    if not rows or not all(col in rows[0] for col in required_cols):
        return 0.0
    eq_tol = 0.5
    eq_count = sum(1 for r in rows if abs(float(r["avg_vacancies"])-float(r["avg_interstitials"])) <= eq_tol)
    eq_score = eq_count / len(rows)
    data = {}
    for r in rows:
        c = r["cell_type"]
        e = int(r["recoil_energy_eV"])
        t = int(r["temperature_K"])
        data[(c,e,t)] = {d: float(r[d]) for d in required_cols[3:]}
    cells = ["pure_Fe", "Fe_Fe3C_inclusion"]
    energies = [100,500,3000]
    temps = [400,800,1000]
    def check_mono(vals, tol=0.5):
        for i in range(1,len(vals)):
            if vals[i] < vals[i-1] - tol:
                return False
        return True
    mono_energy = 0
    mono_energy_total = 0
    for cell in cells:
        for T in temps:
            if any((cell,e,T) not in data for e in energies): continue
            for d in ["avg_antisites","avg_vacancies","avg_interstitials"]:
                vs = [data[(cell,e,T)][d] for e in energies]
                if check_mono(vs): mono_energy+=1
                mono_energy_total+=1
    mono_temp = 0
    mono_temp_total = 0
    for cell in cells:
        for e in energies:
            if any((cell,e,T) not in data for T in temps): continue
            for d in ["avg_antisites","avg_vacancies","avg_interstitials"]:
                vs = [data[(cell,e,T)][d] for T in temps]
                if check_mono(vs): mono_temp+=1
                mono_temp_total+=1
    mono_total = mono_energy_total + mono_temp_total
    if mono_total == 0:
        mono_score = 0.0
    else:
        mono_score = (mono_energy+mono_temp)/mono_total
    return 0.7*mono_score + 0.3*eq_score


# === block: score_1 (check id='step_radial') ===
def score_1(artifact, step, ctx):
    artifact = yaml.safe_load(artifact)
    cond = "Fe_Fe3C_inclusion_3000eV_1000K"
    if cond not in artifact:
        return 0.0
    shells = artifact[cond]
    if not shells:
        return 0.0
    radius = [s["radius_center"] for s in shells]
    antisite_dens = [s["antisite_density"] for s in shells]
    vacancy_dens = [s["vacancy_density"] for s in shells]
    if not antisite_dens or not vacancy_dens:
        return 0.0
    max_idx_as = max(range(len(antisite_dens)), key=lambda i: antisite_dens[i])
    peak_radius_as = radius[max_idx_as]
    antisite_ok = (18 <= peak_radius_as <= 22) and (antisite_dens[max_idx_as] >= 1.5 * antisite_dens[0])
    max_idx_v = max(range(len(vacancy_dens)), key=lambda i: vacancy_dens[i])
    peak_radius_v = radius[max_idx_v]
    vacancy_ok = (18 <= peak_radius_v <= 22) and (vacancy_dens[max_idx_v] >= 1.5 * vacancy_dens[0])
    score = 0.0
    if antisite_ok: score+=0.5
    if vacancy_ok: score+=0.5
    return score


_SCORERS = {
    'step_ws_defects': score_0,
    'step_radial': score_1,
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
