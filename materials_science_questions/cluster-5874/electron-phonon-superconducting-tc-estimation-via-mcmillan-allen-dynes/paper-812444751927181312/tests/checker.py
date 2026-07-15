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
    import csv, os

    # load element data
    element_path = os.path.join(outputs_dir, "element_electronegativity.csv")
    element_data = []
    if os.path.exists(element_path):
        with open(element_path, newline='') as f:
            reader = csv.DictReader(f)
            element_data = list(reader)

    # load alloy data
    alloy_path = os.path.join(outputs_dir, "alloy_equilibrium_electronegativity.csv")
    alloy_data = []
    if os.path.exists(alloy_path):
        with open(alloy_path, newline='') as f:
            reader = csv.DictReader(f)
            alloy_data = list(reader)

    return {
        "element_data": element_data,
        "alloy_data": alloy_data,
        "gold_data": spec.get("gold_data", {})
    }


# === block: score_0 (check id='check_element_electronegativity') ===
def score_0(artifact, step, ctx):
    import math

    gold_elements = ctx["gold_data"]["elements"]
    artifact_dict = {row.get("element", "").strip(): row for row in artifact}
    tolerances = step.get("tolerances", {})
    chi_tol = tolerances.get("chi_abs", 0.1)
    internal_tol = tolerances.get("internal_consistency", 1e-6)

    passed = 0
    total = len(gold_elements)
    if total == 0:
        return 0.0

    for gold in gold_elements:
        elem = gold["element"]
        row = artifact_dict.get(elem)
        if row is None:
            continue
        try:
            ip = float(row.get("IP", "nan"))
            ea = float(row.get("EA", "nan"))
            chi_agent = float(row.get("chi", "nan"))
        except (ValueError, TypeError):
            continue
        recomputed_chi = 0.5 * (ip + ea)
        if abs(recomputed_chi - chi_agent) > internal_tol:
            continue
        if abs(recomputed_chi - gold["chi"]) > chi_tol:
            continue
        passed += 1

    return passed / total


# === block: score_1 (check id='check_alloy_equilibrium_electronegativity') ===
def score_1(artifact, step, ctx):
    import math

    gold_alloys = ctx["gold_data"]["alloys"]
    element_data_map = {}
    for row in ctx["element_data"]:
        elem = row.get("element", "").strip()
        if not elem:
            continue
        try:
            ip = float(row.get("IP", "nan"))
            ea = float(row.get("EA", "nan"))
        except ValueError:
            continue
        element_data_map[elem] = (ip, ea)

    artifact_dict = {row.get("alloy", "").strip(): row for row in artifact}
    tolerances = step.get("tolerances", {})
    chi_tol = tolerances.get("chi_eq_abs", 0.1)
    internal_tol = tolerances.get("internal_consistency", 1e-6)

    passed = 0
    total = len(gold_alloys)
    if total == 0:
        return 0.0

    for gold in gold_alloys:
        alloy_name = gold["alloy"]
        row = artifact_dict.get(alloy_name)
        if row is None:
            continue
        try:
            chi_low = float(row.get("chi_eq_low", "nan"))
            chi_gen = float(row.get("chi_eq_general", "nan"))
        except ValueError:
            continue
        elem_a = gold["element_A"]
        elem_b = gold["element_B"]
        if elem_a not in element_data_map or elem_b not in element_data_map:
            continue
        ip_a, ea_a = element_data_map[elem_a]
        ip_b, ea_b = element_data_map[elem_b]
    
        ip_min = min(ip_a, ip_b)
        ea_max = max(ea_a, ea_b)
        recomputed_low = 0.5 * (ip_min + ea_max)
    
        chi_a = 0.5 * (ip_a + ea_a)
        chi_b = 0.5 * (ip_b + ea_b)
        eta_a = ip_a - ea_a
        eta_b = ip_b - ea_b
        if eta_a + eta_b == 0:
            continue
        recomputed_gen = (eta_b * chi_a + eta_a * chi_b) / (eta_a + eta_b)
    
        if abs(recomputed_low - chi_low) > internal_tol:
            continue
        if abs(recomputed_gen - chi_gen) > internal_tol:
            continue
        if abs(recomputed_low - gold["chi_eq_low"]) > chi_tol:
            continue
        passed += 1

    return passed / total


# === block: score_2 (check id='check_weighted_averages') ===
def score_2(artifact, step, ctx):
    import math

    element_rows = ctx["element_data"]
    alloy_rows = ctx["alloy_data"]
    tolerances = step.get("tolerances", {})
    metals_tol = tolerances.get("metals_avg_abs", 0.05)
    alloys_low_tol = tolerances.get("alloys_low_avg_abs", 0.05)
    alloys_gen_tol = tolerances.get("alloys_general_avg_abs", 0.1)
    internal_tol = 1e-6

    # recompute metals weighted average
    sum_tc_chi = 0.0
    sum_tc = 0.0
    for row in element_rows:
        try:
            tc = float(row.get("Tc", "nan") or "nan")
            chi = float(row.get("chi", "nan"))
        except ValueError:
            continue
        if not math.isnan(tc):
            sum_tc_chi += tc * chi
            sum_tc += tc
    recomputed_metals = (sum_tc_chi / sum_tc) if sum_tc > 0 else None

    # recompute alloy low average
    sum_tc_low = 0.0
    sum_tc_all = 0.0
    for row in alloy_rows:
        try:
            tc = float(row.get("Tc", "nan") or "nan")
            chi_low = float(row.get("chi_eq_low", "nan"))
        except ValueError:
            continue
        if not math.isnan(tc):
            sum_tc_low += tc * chi_low
            sum_tc_all += tc
    recomputed_low = (sum_tc_low / sum_tc_all) if sum_tc_all > 0 else None

    # recompute alloy general average (same sum_tc_all)
    sum_tc_gen = 0.0
    for row in alloy_rows:
        try:
            tc = float(row.get("Tc", "nan") or "nan")
            chi_gen = float(row.get("chi_eq_general", "nan"))
        except ValueError:
            continue
        if not math.isnan(tc):
            sum_tc_gen += tc * chi_gen
    recomputed_gen = (sum_tc_gen / sum_tc_all) if sum_tc_all > 0 else None

    # reported values from artifact
    reported = artifact if isinstance(artifact, dict) else {}
    rep_metals = reported.get("metals_weighted_avg")
    rep_low = reported.get("alloys_weighted_avg_low")
    rep_gen = reported.get("alloys_weighted_avg_general")

    gold = ctx["gold_data"]["target_averages"]
    gold_metals = gold["metals_weighted_avg"]
    gold_low = gold["alloys_weighted_avg_low"]
    gold_gen = gold["alloys_weighted_avg_general"]

    # scoring: each of three subchecks worth 1/3
    metal_pass = False
    if recomputed_metals is not None and rep_metals is not None:
        if abs(recomputed_metals - float(rep_metals)) <= internal_tol and abs(recomputed_metals - gold_metals) <= metals_tol:
            metal_pass = True

    low_pass = False
    if recomputed_low is not None and rep_low is not None:
        if abs(recomputed_low - float(rep_low)) <= internal_tol and abs(recomputed_low - gold_low) <= alloys_low_tol:
            low_pass = True

    gen_pass = False
    if recomputed_gen is not None and rep_gen is not None:
        if abs(recomputed_gen - float(rep_gen)) <= internal_tol and abs(recomputed_gen - gold_gen) <= alloys_gen_tol:
            gen_pass = True

    score = (1.0 if metal_pass else 0.0 + 1.0 if low_pass else 0.0 + 1.0 if gen_pass else 0.0) / 3.0
    return score


_SCORERS = {
    'check_element_electronegativity': score_0,
    'check_alloy_equilibrium_electronegativity': score_1,
    'check_weighted_averages': score_2,
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
