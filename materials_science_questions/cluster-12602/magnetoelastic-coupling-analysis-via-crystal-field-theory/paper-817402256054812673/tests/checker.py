import os
import json
import csv

# === author imports / helpers ===
import math
from collections import defaultdict


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
    steps = spec.get("steps", [])
    ctx = {}
    for s in steps:
        sid = s.get("id")
        if sid == "strain_emca_score":
            ctx["strain_emca_config"] = s
        elif sid == "emca_electron_count":
            ctx["emca_ecconfig"] = s
        elif sid == "surface_energies":
            ctx["surf_config"] = s
    return ctx


# === block: score_0 (check id='strain_emca_score') ===
def score_0(artifact, step, ctx):
    config = ctx["strain_emca_config"]
    alloys = config["alloys"]
    conv_B = config["conversion_B"]
    conv_C_prime = config["conversion_C_prime"]
    group = defaultdict(list)
    for row in artifact:
        alloy = row["Alloy"]
        strain = float(row["Strain"])
        e_total = float(row["E_total"])
        e_mca = float(row["E_MCA"])
        group[alloy].append((strain, e_total, e_mca))
    scores = []
    total = 0.0
    for alloy_name, target_data in alloys.items():
        if alloy_name not in group:
            continue
        entries = sorted(group[alloy_name], key=lambda x: x[0])
        if len(entries) < 3:
            continue
        strains = [e[0] for e in entries]
        emca = [e[2] for e in entries]
        e_tot = [e[1] for e in entries]
        # central slope
        if abs(strains[0] + 0.01) > 1e-4 or abs(strains[2] - 0.01) > 1e-4:
            dEd = (emca[2] - emca[0]) / (strains[2] - strains[0])
        else:
            dEd = (emca[2] - emca[0]) / 0.02
        B1_recomputed = dEd * conv_B
        # curvature
        delta = 0.01 if abs(strains[1])<1e-4 and abs(strains[2]-0.01)<1e-4 else (strains[2]-strains[0])/2
        curv = (e_tot[0] + e_tot[2] - 2 * e_tot[1]) / (delta**2)
        C_prime_recomputed = curv * conv_C_prime
        # B1 score
        B1_target = target_data["B1_target"]
        B1_tol = B1_target * target_data["B1_tol_pct"]
        B1_diff = abs(B1_recomputed - B1_target)
        if B1_diff <= B1_tol:
            b1s = 1.0
        elif B1_diff <= 2 * B1_tol:
            b1s = 1.0 - (B1_diff - B1_tol) / B1_tol
        else:
            b1s = 0.0
        # C' score
        C_prime_target = target_data["C_prime_target"]
        C_prime_tol = C_prime_target * target_data["C_prime_tol_pct"]
        C_diff = abs(C_prime_recomputed - C_prime_target)
        if C_diff <= C_prime_tol:
            cs = 1.0
        elif C_diff <= 2 * C_prime_tol:
            cs = 1.0 - (C_diff - C_prime_tol) / C_prime_tol
        else:
            cs = 0.0
        alloy_score = 0.5 * b1s + 0.5 * cs
        scores.append(alloy_score)
        total += 1.0
    if total == 0:
        return 0.0
    return sum(scores) / total


# === block: score_1 (check id='emca_electron_count') ===
def score_1(artifact, step, ctx):
    config = ctx["emca_ecconfig"]
    tol_1154 = config["checks"]["tolerance_1154_diff"]
    data = {}
    for row in artifact:
        ne = int(row["N_e"])
        plus = float(row["strain_plus1_E_MCA"])
        minus = float(row["strain_minus1_E_MCA"])
        data[ne] = (minus, plus)
    if 1154 not in data:
        return 0.0
    diff_1154 = abs(data[1154][1] - data[1154][0])
    ok_1154 = 1.0 if diff_1154 <= tol_1154 else 0.0
    ok_inc = 0.0
    if 1150 in data and 1158 in data:
        diff_1150 = abs(data[1150][1] - data[1150][0])
        diff_1158 = abs(data[1158][1] - data[1158][0])
        if diff_1150 > diff_1154 and diff_1158 > diff_1154:
            ok_inc = 1.0
        elif diff_1150 > diff_1154 or diff_1158 > diff_1154:
            ok_inc = 0.5
    return 0.5 * ok_1154 + 0.5 * ok_inc


# === block: score_2 (check id='surface_energies') ===
def score_2(artifact, step, ctx):
    config = ctx["surf_config"]
    checks = config["checks"]
    data = defaultdict(lambda: defaultdict(list))
    for row in artifact:
        orient = row["Orientation"]
        coverage = row["Ga_coverage"]
        adsorb = row["Adsorbent"]
        mu = float(row["mu_Ga"])
        gamma = float(row["Surface_energy"])
        data[(adsorb, mu)][orient].append(gamma)
    min_by_ads_mu = {}
    for (ad, mu), orient_gam in data.items():
        min_orient = {}
        for o, gammas in orient_gam.items():
            min_orient[o] = min(gammas)
        if ad not in min_by_ads_mu:
            min_by_ads_mu[ad] = {}
        min_by_ads_mu[ad][mu] = min_orient
    required_ads = checks["crossover_required_adsorbents"]
    cross_range = checks["crossover_range_muGa"]
    crossover_scores = []
    for ad in required_ads:
        if ad not in min_by_ads_mu:
            crossover_scores.append(0.0)
            continue
        found = False
        for mu in sorted(min_by_ads_mu[ad].keys()):
            if mu >= cross_range[0] and mu <= cross_range[1]:
                if '001' in min_by_ads_mu[ad][mu] and '110' in min_by_ads_mu[ad][mu]:
                    if min_by_ads_mu[ad][mu]['001'] < min_by_ads_mu[ad][mu]['110']:
                        found = True
                        break
        crossover_scores.append(1.0 if found else 0.0)
    score_cross = sum(crossover_scores) / len(required_ads) if required_ads else 1.0
    higher_scores = []
    for ad in set(min_by_ads_mu.keys()):
        for mu_check in [-2.0, -3.0]:
            if mu_check in min_by_ads_mu[ad]:
                g = min_by_ads_mu[ad][mu_check]
                if '111' in g and '001' in g and '110' in g:
                    if g['111'] > g['001'] and g['111'] > g['110']:
                        higher_scores.append(1.0)
                    else:
                        higher_scores.append(0.0)
    score_111 = sum(higher_scores) / len(higher_scores) if higher_scores else 0.0
    h2s_scores = []
    if 'H2S' in min_by_ads_mu and 'none' in min_by_ads_mu:
        for mu in [-2.0, -3.0]:
            if mu in min_by_ads_mu['H2S'] and mu in min_by_ads_mu['none']:
                for orient in ['001','110','111']:
                    if orient in min_by_ads_mu['H2S'][mu] and orient in min_by_ads_mu['none'][mu]:
                        diff = abs(min_by_ads_mu['H2S'][mu][orient] - min_by_ads_mu['none'][mu][orient])
                        if diff <= checks["H2S_similar_clean_tol"]:
                            h2s_scores.append(1.0)
                        else:
                            h2s_scores.append(0.0)
    score_h2s = sum(h2s_scores) / len(h2s_scores) if h2s_scores else 0.0
    return 0.4 * score_cross + 0.3 * score_111 + 0.3 * score_h2s


_SCORERS = {
    'strain_emca_score': score_0,
    'emca_electron_count': score_1,
    'surface_energies': score_2,
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
