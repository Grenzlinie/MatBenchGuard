import os
import json
import csv

# === author imports / helpers ===
import math
import os
import json


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
    def mu_2D(m_eff, C2D, E1):
        e = 1.602176634e-19
        hbar = 1.054571817e-34
        kB = 1.380649e-23
        T = 300.0
        m0 = 9.10938356e-31
        eV_to_J = 1.602176634e-19
        m_eff_kg = m_eff * m0
        E1_SI = E1 * eV_to_J
        numerator = 2.0 * e * hbar**3 * C2D
        denominator = 3.0 * kB * T * (m_eff_kg**2) * (E1_SI**2)
        mu_SI = numerator / denominator
        return mu_SI * 1e4

    def mu_1D(C1D_eVcm, m_eff, E1):
        e = 1.602176634e-19
        hbar = 1.054571817e-34
        kB = 1.380649e-23
        T = 300.0
        m0 = 9.10938356e-31
        eV_to_J = 1.602176634e-19
        cm_to_m = 0.01
        C1D_SI = C1D_eVcm * eV_to_J / cm_to_m
        m_eff_kg = m_eff * m0
        E1_SI = E1 * eV_to_J
        numerator = e * hbar**3 * C1D_SI
        denominator = math.sqrt(2.0 * math.pi * kB * T) * (m_eff_kg**1.5) * (E1_SI**2)
        mu_SI = numerator / denominator
        return mu_SI * 1e4

    with open("/tests/grading_spec.json") as f:
        spec = json.load(f)
    gold_data = spec["gold"]
    sheet_gold = gold_data["sheet"]
    sheet_gold["mu_e_zigzag"] = mu_2D(sheet_gold["m_eff_e_zigzag"], sheet_gold["C2D_zigzag"], sheet_gold["E1_e_zigzag"])
    sheet_gold["mu_h_zigzag"] = mu_2D(sheet_gold["m_eff_h_zigzag"], sheet_gold["C2D_zigzag"], sheet_gold["E1_h_zigzag"])
    sheet_gold["mu_e_armchair"] = mu_2D(sheet_gold["m_eff_e_armchair"], sheet_gold["C2D_armchair"], sheet_gold["E1_e_armchair"])
    sheet_gold["mu_h_armchair"] = mu_2D(sheet_gold["m_eff_h_armchair"], sheet_gold["C2D_armchair"], sheet_gold["E1_h_armchair"])
    for nr in gold_data["nanoribbons"]:
        nr["mu_e"] = mu_1D(nr["C1D"], nr["m_eff_e"], nr["E1_e"])
        nr["mu_h"] = mu_1D(nr["C1D"], nr["m_eff_h"], nr["E1_h"])
    return {"gold": gold_data, "tolerances": gold_data["tolerances"]}


# === block: score_0 (check id='results_check') ===
def score_0(artifact, step, ctx):
    sheet = artifact.get("2D_sheet")
    nrs = artifact.get("nanoribbons")
    tolerances = ctx["tolerances"]

    # basic shape gate
    shape_ok = 1.0
    if not isinstance(sheet, dict) or not isinstance(nrs, list):
        shape_ok = 0.0
    else:
        required_2d = ["bandgap_HSE06", "bandgap_PBE", "m_eff_e_zigzag", "m_eff_h_zigzag", "m_eff_e_armchair", "m_eff_h_armchair",
                       "C2D_zigzag", "C2D_armchair", "E1_e_zigzag", "E1_h_zigzag", "E1_e_armchair", "E1_h_armchair",
                       "mu_e_zigzag", "mu_h_zigzag", "mu_e_armchair", "mu_h_armchair"]
        for k in required_2d:
            if k not in sheet:
                shape_ok = 0.0
        if len(nrs) < 4:
            shape_ok = 0.0
        else:
            req_nr = ["type", "N", "bandgap_PBE", "m_eff_e", "m_eff_h", "C1D", "E1_e", "E1_h", "mu_e", "mu_h"]
            for nr in nrs:
                if not isinstance(nr, dict):
                    shape_ok = 0.0
                for k in req_nr:
                    if k not in nr:
                        shape_ok = 0.0

    def check_field(val, ref, tol, rel=False):
        if rel:
            if ref == 0:
                return abs(val) < tol
            return abs(val - ref) / max(abs(ref), 1e-9) <= tol
        else:
            return abs(val - ref) <= tol

    def score_2d(sheet, gold_sheet):
        checks = [
            ("bandgap_HSE06", gold_sheet["bandgap_HSE06"], tolerances["bandgap_HSE06"], False),
            ("bandgap_PBE", gold_sheet["bandgap_PBE"], tolerances["bandgap_PBE"], False),
            ("m_eff_e_zigzag", gold_sheet["m_eff_e_zigzag"], tolerances["m_eff"], False),
            ("m_eff_h_zigzag", gold_sheet["m_eff_h_zigzag"], tolerances["m_eff"], False),
            ("m_eff_e_armchair", gold_sheet["m_eff_e_armchair"], tolerances["m_eff"], False),
            ("m_eff_h_armchair", gold_sheet["m_eff_h_armchair"], tolerances["m_eff"], False),
            ("C2D_zigzag", gold_sheet["C2D_zigzag"], tolerances["C2D"], False),
            ("C2D_armchair", gold_sheet["C2D_armchair"], tolerances["C2D"], False),
            ("E1_e_zigzag", gold_sheet["E1_e_zigzag"], tolerances["E1"], False),
            ("E1_h_zigzag", gold_sheet["E1_h_zigzag"], tolerances["E1"], False),
            ("E1_e_armchair", gold_sheet["E1_e_armchair"], tolerances["E1"], False),
            ("E1_h_armchair", gold_sheet["E1_h_armchair"], tolerances["E1"], False),
            ("mu_e_zigzag", gold_sheet["mu_e_zigzag"], tolerances["mu_rel"], True),
            ("mu_h_zigzag", gold_sheet["mu_h_zigzag"], tolerances["mu_rel"], True),
            ("mu_e_armchair", gold_sheet["mu_e_armchair"], tolerances["mu_rel"], True),
            ("mu_h_armchair", gold_sheet["mu_h_armchair"], tolerances["mu_rel"], True),
        ]
        total = 0.0
        count = 0
        for field, ref, tol, rel in checks:
            if field in sheet:
                count += 1
                try:
                    val = float(sheet[field])
                except:
                    val = None
                if val is None:
                    continue
                ok = check_field(val, ref, tol, rel)
                total += 1.0 if ok else 0.0
            else:
                total += 0.0
                count += 1
        return total / max(count, 1)

    # Nanoribbon 1D mobility formula (same as paper's Eq. 2)
    def mu_1D(C1D_eVcm, m_eff, E1):
        e = 1.602176634e-19
        hbar = 1.054571817e-34
        kB = 1.380649e-23
        T = 300.0
        m0 = 9.10938356e-31
        eV_to_J = 1.602176634e-19
        cm_to_m = 0.01
        C1D_SI = C1D_eVcm * eV_to_J / cm_to_m
        m_eff_kg = m_eff * m0
        E1_SI = E1 * eV_to_J
        numerator = e * hbar**3 * C1D_SI
        denominator = math.sqrt(2.0 * math.pi * kB * T) * (m_eff_kg**1.5) * (E1_SI**2)
        mu_SI = numerator / denominator
        return mu_SI * 1e4

    # Hidden gold for nanoribbons digitized from the paper's Figures 5 and 8.
    # These values are approximate but faithful to the reported trends.
    DIGITIZED_NANORIBBON_GOLD = [
        {
            "type": "zigzag", "N": 4,
            "bandgap_PBE": 0.78,
            "m_eff_e": 0.25, "m_eff_h": 0.95,
            "C1D": 0.45e10,
            "E1_e": -1.0, "E1_h": -2.5,
        },
        {
            "type": "zigzag", "N": 8,
            "bandgap_PBE": 0.57,
            "m_eff_e": 0.18, "m_eff_h": 0.78,
            "C1D": 1.5e10,
            "E1_e": -0.6, "E1_h": -2.2,
        },
        {
            "type": "armchair", "N": 4,
            "bandgap_PBE": 0.85,
            "m_eff_e": 0.30, "m_eff_h": 1.20,
            "C1D": 0.50e10,
            "E1_e": -1.1, "E1_h": -2.8,
        },
        {
            "type": "armchair", "N": 8,
            "bandgap_PBE": 0.62,
            "m_eff_e": 0.20, "m_eff_h": 0.85,
            "C1D": 1.6e10,
            "E1_e": -0.65, "E1_h": -2.3,
        },
    ]

    for nr in DIGITIZED_NANORIBBON_GOLD:
        nr["mu_e"] = mu_1D(nr["C1D"], nr["m_eff_e"], nr["E1_e"])
        nr["mu_h"] = mu_1D(nr["C1D"], nr["m_eff_h"], nr["E1_h"])

    def score_nr(nrs_list):
        gold_map = {}
        for gnr in DIGITIZED_NANORIBBON_GOLD:
            key = (gnr["type"], gnr["N"])
            gold_map[key] = gnr
        agent_map = {}
        for nr in nrs_list:
            if isinstance(nr, dict) and "type" in nr and "N" in nr:
                key = (nr["type"], nr["N"])
                agent_map[key] = nr
        total_field = 0.0
        num = len(DIGITIZED_NANORIBBON_GOLD)
        for key, gnr in gold_map.items():
            anr = agent_map.get(key)
            if anr is None:
                continue
            field_checks = [
                ("bandgap_PBE", gnr["bandgap_PBE"], tolerances["bandgap_PBE"], False),
                ("m_eff_e", gnr["m_eff_e"], tolerances["m_eff"], False),
                ("m_eff_h", gnr["m_eff_h"], tolerances["m_eff"], False),
                ("C1D", gnr["C1D"], tolerances["C1D_rel"], True),
                ("E1_e", gnr["E1_e"], tolerances["E1"], False),
                ("E1_h", gnr["E1_h"], tolerances["E1"], False),
                ("mu_e", gnr["mu_e"], tolerances["mu_rel"], True),
                ("mu_h", gnr["mu_h"], tolerances["mu_rel"], True),
            ]
            ribbon_score = 0.0
            cnt = 0
            for field, ref, tol, rel in field_checks:
                cnt += 1
                if field in anr:
                    try:
                        val = float(anr[field])
                    except:
                        val = None
                    if val is None:
                        ribbon_score += 0.0
                    else:
                        ok = check_field(val, ref, tol, rel)
                        ribbon_score += 1.0 if ok else 0.0
                else:
                    ribbon_score += 0.0
            if cnt > 0:
                total_field += ribbon_score / cnt
        avg_field = total_field / num if num > 0 else 0.0

        # structural trend: bandgap must decrease with increasing width N
        trend_score = 0.0
        for typ in ["zigzag", "armchair"]:
            nr4 = agent_map.get((typ, 4))
            nr8 = agent_map.get((typ, 8))
            if nr4 and nr8 and "bandgap_PBE" in nr4 and "bandgap_PBE" in nr8:
                try:
                    g4 = float(nr4["bandgap_PBE"])
                    g8 = float(nr8["bandgap_PBE"])
                    if g4 > g8:
                        trend_score += 1.0
                except:
                    pass
        trend_score = trend_score / 2.0 if 2 else 0.0
        nr_final = 0.8 * avg_field + 0.2 * trend_score
        return nr_final

    score_2d_val = score_2d(sheet, ctx["gold"]["sheet"]) if isinstance(sheet, dict) else 0.0
    score_nr_val = score_nr(nrs) if isinstance(nrs, list) else 0.0
    w_shape = 0.05
    w_2d = 0.5
    w_nr = 0.45
    overall = w_shape * shape_ok + w_2d * score_2d_val + w_nr * score_nr_val
    return round(overall, 6)


_SCORERS = {
    'results_check': score_0,
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
