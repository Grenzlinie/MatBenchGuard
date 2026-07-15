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
    return {}


# === block: score_0 (check id='mod_scores') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    gold = step["gold"]
    tols = step["tolerances"]
    expected_models = ["M1","M2","M3","M4","M5"]
    if not all(m in artifact for m in expected_models):
        return 0.0
    total_fields = 0
    correct_fields = 0
    for model in expected_models:
        gmod = gold[model]
        amod = artifact[model]
        if not isinstance(amod, dict):
            continue
        # E_mod
        total_fields += 1
        if abs(amod.get("E_mod_eV", 0.0) - gmod["E_mod_eV"]) <= tols["E_mod_eV"]:
            correct_fields += 1
        # charge
        total_fields += 1
        if abs(amod.get("charge_Ag_e", 0.0) - gmod["charge_Ag_e"]) <= tols["charge"]:
            correct_fields += 1
        # bonds
        gbonds = gmod["bonds"]
        abonds = amod.get("bonds", [])
        g_types = {}
        for b in gbonds:
            t = b["type"]
            if t not in g_types:
                g_types[t] = []
            g_types[t].append(b["length_Ang"])
        a_types = {}
        for b in abonds:
            t = b.get("type")
            if t is None:
                continue
            if t not in a_types:
                a_types[t] = []
            a_types[t].append(b.get("length_Ang", 0.0))
        for t, g_lens in g_types.items():
            a_lens = sorted(a_types.get(t, []))
            if len(a_lens) != len(g_lens):
                continue
            g_lens_sorted = sorted(g_lens)
            ok = all(abs(a_lens[i] - g_lens_sorted[i]) <= tols["length_Ang"] for i in range(len(g_lens)))
            total_fields += len(g_lens)
            if ok:
                correct_fields += len(g_lens)
    numeric_score = correct_fields / total_fields if total_fields > 0 else 0.0
    # trend: M5 highest E_mod
    emods = {}
    for m in expected_models:
        if "E_mod_eV" in artifact[m]:
            emods[m] = artifact[m]["E_mod_eV"]
    if emods:
        max_model = max(emods, key=emods.get)
        trend_ok = (max_model == "M5")
    else:
        trend_ok = False
    return numeric_score * 0.8 + (0.2 if trend_ok else 0.0)


# === block: score_1 (check id='ads_scores') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    gold = step["gold"]
    tols = step["tolerances"]
    expected_models = ["M01","M51","M52","M53","M54","M55","M56","M57","M58","M59"]
    if not all(m in artifact for m in expected_models):
        return 0.0
    total_fields = 0
    correct_fields = 0
    for model in expected_models:
        gmod = gold[model]
        amod = artifact[model]
        if not isinstance(amod, dict):
            continue
        # E_ads
        total_fields += 1
        if abs(amod.get("E_ads_eV", 0.0) - gmod["E_ads_eV"]) <= tols["E_ads_eV"]:
            correct_fields += 1
        # bonds
        gbonds = gmod["bonds"]
        abonds = amod.get("bonds", [])
        g_types = {}
        for b in gbonds:
            t = b["type"]
            if t not in g_types:
                g_types[t] = []
            g_types[t].append(b["length_Ang"])
        a_types = {}
        for b in abonds:
            t = b.get("type")
            if t is None:
                continue
            if t not in a_types:
                a_types[t] = []
            a_types[t].append(b.get("length_Ang", 0.0))
        for t, g_lens in g_types.items():
            a_lens = sorted(a_types.get(t, []))
            if len(a_lens) != len(g_lens):
                continue
            g_lens_sorted = sorted(g_lens)
            ok = all(abs(a_lens[i] - g_lens_sorted[i]) <= tols["length_Ang"] for i in range(len(g_lens)))
            total_fields += len(g_lens)
            if ok:
                correct_fields += len(g_lens)
    numeric_score = correct_fields / total_fields if total_fields > 0 else 0.0
    # trend: M51 highest E_ads among M5x
    emods = {}
    for m in ["M51","M52","M53","M54","M55","M56","M57","M58","M59"]:
        if "E_ads_eV" in artifact.get(m, {}):
            emods[m] = artifact[m]["E_ads_eV"]
    if emods:
        max_model = max(emods, key=emods.get)
        trend_ok = (max_model == "M51")
    else:
        trend_ok = False
    return numeric_score * 0.8 + (0.2 if trend_ok else 0.0)


# === block: score_2 (check id='chg_scores') ===
def score_2(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    gold = step["gold"]
    tol = step["tolerances"]["charge"]
    expected_models = ["M01","M51","M59"]
    if not all(m in artifact for m in expected_models):
        return 0.0
    total_fields = 0
    correct_fields = 0
    # M01
    g01 = gold["M01"]
    a01 = artifact["M01"]
    if isinstance(a01, dict):
        total_fields += 1
        if abs(a01.get("NO2_charge_e", 0.0) - g01["NO2_charge_e"]) <= tol:
            correct_fields += 1
        dq = a01.get("delta_q_per_atom")
        if isinstance(dq, dict):
            for atom in ["N","O_a","O_b"]:
                total_fields += 1
                if abs(dq.get(atom, 0.0) - g01["delta_q_per_atom"][atom]) <= tol:
                    correct_fields += 1
    # M51
    g51 = gold["M51"]
    a51 = artifact["M51"]
    if isinstance(a51, dict):
        for key in ["NO2_charge_e","Ag_charge_e","Si1_charge_e"]:
            total_fields += 1
            if abs(a51.get(key, 0.0) - g51[key]) <= tol:
                correct_fields += 1
    # M59
    g59 = gold["M59"]
    a59 = artifact["M59"]
    if isinstance(a59, dict):
        for key in ["NO2_charge_e","Ag_charge_e","Si1_charge_e"]:
            total_fields += 1
            if abs(a59.get(key, 0.0) - g59[key]) <= tol:
                correct_fields += 1
    return correct_fields / total_fields if total_fields > 0 else 0.0


_SCORERS = {
    'mod_scores': score_0,
    'ads_scores': score_1,
    'chg_scores': score_2,
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
