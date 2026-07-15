import os
import json
import csv

# === author imports / helpers ===
import json
import math

def comp_arr(agent_arr, gold_arr, tol_arr):
    if not isinstance(agent_arr, list) or len(agent_arr) != len(gold_arr):
        return 0.0
    scores = []
    for a, g, t in zip(agent_arr, gold_arr, tol_arr):
        diff = abs(a - g)
        scores.append(max(0.0, 1.0 - diff / t))
    return sum(scores) / len(scores) if scores else 0.0


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


# === block: score_0 (check id='lattice_parameters') ===
def score_0(artifact, step, ctx):
    agent = artifact.get("lattice_parameters")
    if not agent:
        return 0.0
    s_hgh = comp_arr(agent.get("HGH.LDA", []), step["target"]["HGH.LDA"], step["tolerance"]["HGH.LDA"])
    s_fhi = comp_arr(agent.get("FHI.LDA", []), step["target"]["FHI.LDA"], step["tolerance"]["FHI.LDA"])
    return (s_hgh + s_fhi) / 2.0


# === block: score_1 (check id='band_gaps') ===
def score_1(artifact, step, ctx):
    agent = artifact.get("band_gaps")
    if not agent:
        return 0.0
    s1 = comp_arr(agent.get("HGH.LDA", []), step["target"]["HGH.LDA"], step["tolerance"]["HGH.LDA"])
    s2 = comp_arr(agent.get("HGH.G0W0", []), step["target"]["HGH.G0W0"], step["tolerance"]["HGH.G0W0"])
    s3 = comp_arr(agent.get("FHI.G0W0", []), step["target"]["FHI.G0W0"], step["tolerance"]["FHI.G0W0"])
    return (s1 + s2 + s3) / 3.0


# === block: score_2 (check id='dielectric_constants') ===
def score_2(artifact, step, ctx):
    di = artifact.get("dielectric_constants", {})
    ph = artifact.get("phonon_frequencies", {})
    eps0 = di.get("epsilon0", [])
    eps_inf = di.get("epsilon_inf", [])
    wTO = ph.get("omega_TO", [])
    wLO = ph.get("omega_LO", [])
    if not eps0 or not eps_inf or not wTO or not wLO:
        return 0.0
    s_eps0 = comp_arr(eps0, step["target"]["epsilon0"], step["tolerance"]["epsilon0"])
    s_eps_inf_gold = comp_arr(eps_inf, step["target"]["epsilon_inf"], step["tolerance"]["epsilon_inf"])
    calc = [e0 * (wt**2) / (wl**2) for e0, wt, wl in zip(eps0, wTO, wLO)]
    s_cons = comp_arr(eps_inf, calc, [0.1]*len(eps_inf))
    return 0.4*s_eps0 + 0.2*s_eps_inf_gold + 0.4*s_cons


# === block: score_3 (check id='born_effective_charge') ===
def score_3(artifact, step, ctx):
    zstar = artifact.get("born_effective_charge", [])
    if not zstar or len(zstar) != 5:
        return 0.0
    return comp_arr(zstar, step["target"]["zstar"], step["tolerance"]["zstar"])


# === block: score_4 (check id='phonon_frequencies') ===
def score_4(artifact, step, ctx):
    ph = artifact.get("phonon_frequencies", {})
    wTO = ph.get("omega_TO", [])
    wLO = ph.get("omega_LO", [])
    if not wTO or not wLO:
        return 0.0
    sTO = comp_arr(wTO, step["target"]["omega_TO"], step["tolerance"]["omega_TO"])
    sLO = comp_arr(wLO, step["target"]["omega_LO"], step["tolerance"]["omega_LO"])
    return (sTO + sLO) / 2.0


# === block: score_5 (check id='thermodynamic_300K') ===
def score_5(artifact, step, ctx):
    th = artifact.get("thermodynamic_300K", {})
    cv = th.get("Cv", [])
    s = th.get("S", [])
    if not cv or not s:
        return 0.0
    sCv = comp_arr(cv, step["target"]["Cv"], step["tolerance"]["Cv"])
    sS = comp_arr(s, step["target"]["S"], step["tolerance"]["S"])
    return (sCv + sS) / 2.0


# === block: score_6 (check id='elastic_raw') ===
def score_6(artifact, step, ctx):
    ec = artifact.get("elastic_constants", {})
    c11 = ec.get("C11", [])
    c12 = ec.get("C12", [])
    c44 = ec.get("C44", [])
    if not c11 or not c12 or not c44:
        return 0.0
    s11 = comp_arr(c11, step["target"]["C11"], step["tolerance"]["C11"])
    s12 = comp_arr(c12, step["target"]["C12"], step["tolerance"]["C12"])
    s44 = comp_arr(c44, step["target"]["C44"], step["tolerance"]["C44"])
    return (s11 + s12 + s44) / 3.0


# === block: score_7 (check id='elastic_derived') ===
def score_7(artifact, step, ctx):
    ec = artifact.get("elastic_constants", {})
    c11 = ec.get("C11", [])
    c12 = ec.get("C12", [])
    c44 = ec.get("C44", [])
    if not c11 or not c12 or not c44:
        return 0.0
    def calc_B(c11, c12):
        return [(x+2*y)/3.0 for x,y in zip(c11,c12)]
    def calc_G(c11, c12, c44):
        GR = []
        GV = []
        for x,y,z in zip(c11,c12,c44):
            try:
                gr = 5*(x-y)*z / (4*z + 3*(x-y))
            except ZeroDivisionError:
                gr = 0.0
            GR.append(gr)
            GV.append((x - y + 3*z)/5.0)
        return [(gr+gv)/2.0 for gr,gv in zip(GR,GV)]
    B_calc = calc_B(c11, c12)
    G_calc = calc_G(c11, c12, c44)
    B_over_G_calc = [b/g for b,g in zip(B_calc, G_calc)]
    Cauchy_calc = [x-y for x,y in zip(c12, c44)]
    agent_B = ec.get("B", [])
    agent_G = ec.get("G", [])
    agent_BoG = ec.get("B_over_G", [])
    agent_Cauchy = ec.get("Cauchy_pressure", [])
    if len(agent_B)!=5 or len(agent_G)!=5 or len(agent_BoG)!=5 or len(agent_Cauchy)!=5:
        return 0.0
    tol_B = step["tolerance"]["B"]
    tol_G = step["tolerance"]["G"]
    tol_BoG = step["tolerance"]["B_over_G"]
    tol_Cauchy = step["tolerance"]["Cauchy"]
    sB = comp_arr(agent_B, B_calc, [tol_B]*5)
    sG = comp_arr(agent_G, G_calc, [tol_G]*5)
    sBoG = comp_arr(agent_BoG, B_over_G_calc, [tol_BoG]*5)
    sCa = comp_arr(agent_Cauchy, Cauchy_calc, [tol_Cauchy]*5)
    return (sB + sG + sBoG + sCa) / 4.0


# === block: score_8 (check id='nonlinear_optical') ===
def score_8(artifact, step, ctx):
    nl = artifact.get("nonlinear_optical", {})
    d36 = nl.get("d36", {})
    aTO = nl.get("alpha_omega_TO", {})
    aLO = nl.get("alpha_omega_LO", {})
    r_e = nl.get("r63_electronic", {})
    r_i = nl.get("r63_ionic", {})
    r_t = nl.get("r63_total", {})
    score_parts = []
    if "HGH.LDA" in d36 and "FHI.LDA" in d36:
        score_parts.append(comp_arr(d36["HGH.LDA"], step["target"]["d36_HGH"], step["tolerance"]["d36_HGH"]))
        score_parts.append(comp_arr(d36["FHI.LDA"], step["target"]["d36_FHI"], step["tolerance"]["d36_FHI"]))
    if "HGH.LDA" in aTO and "FHI.LDA" in aTO:
        score_parts.append(comp_arr(aTO["HGH.LDA"], step["target"]["alpha_TO_HGH"], step["tolerance"]["alpha_TO_HGH"]))
        score_parts.append(comp_arr(aTO["FHI.LDA"], step["target"]["alpha_TO_FHI"], step["tolerance"]["alpha_TO_FHI"]))
    if "HGH.LDA" in aLO and "FHI.LDA" in aLO:
        score_parts.append(comp_arr(aLO["HGH.LDA"], step["target"]["alpha_LO_HGH"], step["tolerance"]["alpha_LO_HGH"]))
        score_parts.append(comp_arr(aLO["FHI.LDA"], step["target"]["alpha_LO_FHI"], step["tolerance"]["alpha_LO_FHI"]))
    if "HGH.LDA" in r_e and "FHI.LDA" in r_e:
        score_parts.append(comp_arr(r_e["HGH.LDA"], step["target"]["r63_electronic_HGH"], step["tolerance"]["r63_electronic_HGH"]))
        score_parts.append(comp_arr(r_e["FHI.LDA"], step["target"]["r63_electronic_FHI"], step["tolerance"]["r63_electronic_FHI"]))
    if "HGH.LDA" in r_i and "FHI.LDA" in r_i:
        score_parts.append(comp_arr(r_i["HGH.LDA"], step["target"]["r63_ionic_HGH"], step["tolerance"]["r63_ionic_HGH"]))
        score_parts.append(comp_arr(r_i["FHI.LDA"], step["target"]["r63_ionic_FHI"], step["tolerance"]["r63_ionic_FHI"]))
    if "HGH.LDA" in r_t and "FHI.LDA" in r_t:
        score_parts.append(comp_arr(r_t["HGH.LDA"], step["target"]["r63_total_HGH"], step["tolerance"]["r63_total_HGH"]))
        score_parts.append(comp_arr(r_t["FHI.LDA"], step["target"]["r63_total_FHI"], step["tolerance"]["r63_total_FHI"]))
    if not score_parts:
        return 0.0
    return sum(score_parts) / len(score_parts)


_SCORERS = {
    'lattice_parameters': score_0,
    'band_gaps': score_1,
    'dielectric_constants': score_2,
    'born_effective_charge': score_3,
    'phonon_frequencies': score_4,
    'thermodynamic_300K': score_5,
    'elastic_raw': score_6,
    'elastic_derived': score_7,
    'nonlinear_optical': score_8,
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
