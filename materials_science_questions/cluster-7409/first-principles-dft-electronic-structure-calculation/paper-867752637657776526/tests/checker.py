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
    return {"gold": spec.get("steps", [])}


# === block: score_0 (check id='bulk_magnetic') ===
def score_0(artifact, step, ctx):
    gold = step["gold"]
    orders_gold = gold["orders"]
    e_gold = gold["relative_energies_meV_per_Ti"]
    m_gold = gold["magnetic_moments_muB_per_Ti"]
    tol_e = gold["tolerances"]["energy_meV_per_Ti"]
    tol_m = gold["tolerances"]["moment_muB_per_Ti"]

    agent_orders = artifact.get("magnetic_orders", [])
    agent_e = artifact.get("relative_energies_meV_per_Ti", [])
    agent_m = artifact.get("magnetic_moments_muB_per_Ti", [])

    if not (isinstance(agent_orders, list) and isinstance(agent_e, list) and isinstance(agent_m, list)):
        return 0.0
    if not (len(agent_orders) == len(agent_e) == len(agent_m)):
        return 0.0

    agent_map = {}
    for i, order in enumerate(agent_orders):
        if i < len(agent_e) and i < len(agent_m):
            ae = agent_e[i]
            am = agent_m[i]
            if ae is not None and am is not None:
                agent_map[order] = (ae, am)

    e_scores = []
    m_scores = []
    for i, order in enumerate(orders_gold):
        if order in agent_map:
            ae, am = agent_map[order]
            try:
                if abs(ae - e_gold[i]) <= tol_e:
                    e_scores.append(1.0)
                else:
                    e_scores.append(0.0)
            except (TypeError, ValueError):
                e_scores.append(0.0)
            try:
                if abs(am - m_gold[i]) <= tol_m:
                    m_scores.append(1.0)
                else:
                    m_scores.append(0.0)
            except (TypeError, ValueError):
                m_scores.append(0.0)
        else:
            e_scores.append(0.0)
            m_scores.append(0.0)

    e_avg = sum(e_scores) / len(e_scores) if e_scores else 0.0
    m_avg = sum(m_scores) / len(m_scores) if m_scores else 0.0
    return 0.6 * e_avg + 0.4 * m_avg


# === block: score_1 (check id='strained_energy') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold = step["gold"]
        comp_gold = gold["compressive"]
        tens_gold = gold["tensile"]
        tol_e = gold["tolerances"]["deltaE_meVperTi"]
        tol_c = gold["tolerances"]["c_axis_A"]

        agent_comp = artifact.get("compressive", [])
        agent_tens = artifact.get("tensile", [])

        def find_substrate(lst, name):
            for item in lst:
                if item.get("substrate") == name:
                    return item
            return None

        scores = []
        # compressive
        for cg in comp_gold:
            sub = cg["substrate"]
            ac = find_substrate(agent_comp, sub)
            if ac is None:
                scores.append(0.0)
                continue
            sc = 0.0
            if "c_axis_A" in ac and abs(ac["c_axis_A"] - cg["c_axis_A"]) <= tol_c:
                sc += 0.5
            else:
                sc += 0.2
            key = "E_A_AFM_minus_G_AFM_meVperTi"
            if key in ac:
                de = ac[key]
                if cg.get("deltaE_meVperTi") is not None:
                    if abs(de - cg["deltaE_meVperTi"]) <= tol_e:
                        sc += 0.5
                    elif de < 0:
                        sc += 0.3
                    else:
                        sc += 0.1
                else:
                    # LaGaO3: only sign and plausible range
                    if de < 0 and -20 <= de <= 0:
                        sc += 0.5
                    elif de < 0:
                        sc += 0.3
                    else:
                        sc += 0.1
            else:
                sc += 0.0
            scores.append(sc)

        # tensile
        for tg in tens_gold:
            sub = tg["substrate"]
            at = find_substrate(agent_tens, sub)
            if at is None:
                scores.append(0.0)
                continue
            sc = 0.0
            if "c_axis_A" in at and abs(at["c_axis_A"] - tg["c_axis_A"]) <= tol_c:
                sc += 0.5
            else:
                sc += 0.2
            key = "E_C_AFM_minus_G_AFM_meVperTi"
            if key in at:
                de = at[key]
                if abs(de - tg["deltaE_meVperTi"]) <= tol_e:
                    sc += 0.5
                elif de > 0:
                    sc += 0.3
                else:
                    sc += 0.1
            else:
                sc += 0.0
            scores.append(sc)

        # trend checks
        comp_deltas = []
        for sub_name in ["LaAlO3", "LaGaO3", "SrTiO3"]:
            item = find_substrate(agent_comp, sub_name)
            if item and "E_A_AFM_minus_G_AFM_meVperTi" in item:
                comp_deltas.append(item["E_A_AFM_minus_G_AFM_meVperTi"])
        trend_score = 0.0
        if len(comp_deltas) == 3:
            if comp_deltas[0] <= comp_deltas[1] <= comp_deltas[2]:
                trend_score = 0.5
            else:
                trend_score = 0.2

        tens_deltas = []
        for sub_name in ["BaTiO3", "LaScO3"]:
            item = find_substrate(agent_tens, sub_name)
            if item and "E_C_AFM_minus_G_AFM_meVperTi" in item:
                tens_deltas.append(item["E_C_AFM_minus_G_AFM_meVperTi"])
        if len(tens_deltas) == 2:
            if tens_deltas[0] >= tens_deltas[1]:
                trend_score += 0.5
            else:
                trend_score += 0.2

        avg = sum(scores)/len(scores) if scores else 0.0
        final = 0.7 * avg + 0.3 * trend_score
        return min(1.0, final)


# === block: score_2 (check id='band_gap') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold = step["gold"]
        target_bulk = gold["bulk_band_gap_eV"]
        tol = gold["tolerance_eV"]

        score = 0.0

        bulk_gap = artifact.get("bulk_band_gap_eV", None)
        if bulk_gap is not None and abs(bulk_gap - target_bulk) <= tol:
            score += 0.4
        elif bulk_gap is not None and bulk_gap > 0.0:
            score += 0.2

        strained = artifact.get("strained_band_gaps", [])
        if not strained:
            return score

        all_insulating = all(g.get("band_gap_eV", 0) > 0.05 for g in strained)
        if all_insulating:
            score += 0.2

        order = ["LaAlO3", "LaGaO3", "SrTiO3", "BaTiO3", "LaScO3"]
        gaps_map = {}
        for g in strained:
            gaps_map[g.get("substrate", "")] = g.get("band_gap_eV", 0)
        values = []
        for sub in order:
            if sub in gaps_map:
                values.append(gaps_map[sub])
        if len(values) == 5:
            if all(values[i] <= values[i+1] for i in range(len(values)-1)):
                score += 0.4
            else:
                score += 0.1
        elif len(values) >= 3:
            if all(values[i] <= values[i+1] for i in range(len(values)-1)):
                score += 0.2

        return min(1.0, score)


_SCORERS = {
    'bulk_magnetic': score_0,
    'strained_energy': score_1,
    'band_gap': score_2,
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
