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
    ctx = {"gold": spec["steps"][0]["gold"]}
    return ctx


# === block: score_0 (check id='computed_results_main') ===
def score_0(artifact, step, ctx):
    gold = ctx["gold"]
    systems_dict = {s["name"]: s for s in artifact.get("systems", [])}

    HARTREE_TO_KJMOL = 2625.5
    etol = gold["energy_tolerance_kJmol"]
    dtol = gold["distance_tolerance_nm"]

    def score_val(val, target, tol):
        if target is None:
            return 1.0
        if abs(val - target) <= tol:
            return 1.0
        return max(0.0, 1.0 - (abs(val - target) - tol) / tol)

    # 1. cis-trans energy diff
    sc_cis_trans = 0.0
    if "trans N-ethylacetamide" in systems_dict and "cis N-ethylacetamide" in systems_dict:
        e_trans = systems_dict["trans N-ethylacetamide"]["total_energy_hartree"]
        e_cis = systems_dict["cis N-ethylacetamide"]["total_energy_hartree"]
        diff_kj = (e_cis - e_trans) * HARTREE_TO_KJMOL
        sc_cis_trans = score_val(diff_kj, gold["cis_trans_energy_diff_kJmol"], etol)

    # 2. activation energy
    sc_act = score_val(artifact.get("activation_energy_kJmol", None), gold["activation_energy_kJmol"], etol)

    def get_interaction(name):
        if name not in systems_dict:
            return None
        s = systems_dict[name]
        frag_names = gold["fragment_map"].get(name, [])
        e_complex = s["total_energy_hartree"]
        e_frags = sum(systems_dict[f]["total_energy_hartree"] for f in frag_names if f in systems_dict)
        return (e_complex - e_frags) * HARTREE_TO_KJMOL

    # 3. interaction energies
    sc_ints = []
    for name, gdata in gold["complexes"].items():
        ie = get_interaction(name)
        if ie is None:
            sc_ints.append(0.0)
        else:
            sc_ints.append(score_val(ie, gdata["interaction"], etol))
    sc_int_avg = sum(sc_ints) / len(sc_ints) if sc_ints else 0.0

    # 4. distances
    sc_distances = []
    for name, gdata in gold["complexes"].items():
        if gdata["distance"] is None:
            continue
        if name not in systems_dict:
            sc_distances.append(0.0)
            continue
        d = systems_dict[name].get("oh_distance_nm", None)
        if d is None:
            sc_distances.append(0.0)
        else:
            sc_distances.append(score_val(d, gdata["distance"], dtol))
    sc_dist_avg = sum(sc_distances) / len(sc_distances) if sc_distances else 1.0

    # 5. Relative trends
    sc_trends = []
    # a) cyclic and cis both-func interactions differ < 1 kJ
    ie_ring = get_interaction("2-pyrrolidinone + Al(OH)H2 (both functionalities)")
    ie_cis_both = get_interaction("cis N-ethylacetamide + Al(OH)H2 (both functionalities)")
    if ie_ring is not None and ie_cis_both is not None:
        sc_trends.append(1.0 if abs(ie_ring - ie_cis_both) < 1.0 else 0.0)
    else:
        sc_trends.append(0.0)

    # b) carbonyl-only interaction > 2 * amine-only interaction (in absolute values)
    ie_carb = get_interaction("trans N-ethylacetamide + Al(OH)H2 (carbonyl only)")
    ie_amine = get_interaction("trans N-ethylacetamide + Al(OH)H2 (amine only)")
    if ie_carb is not None and ie_amine is not None and ie_amine != 0:
        sc_trends.append(1.0 if (ie_carb / ie_amine) > 2.0 else 0.0)
    else:
        sc_trends.append(0.0)

    # c) two-site interaction increase ~7 kJ relative to carbonyl-only single-site
    ie_two = get_interaction("trans N-ethylacetamide + 2 Al(OH)H2 (both functionalities)")
    if ie_carb is not None and ie_two is not None:
        diff = ie_carb - ie_two  # positive expected ~7
        sc_trends.append(1.0 if 5.0 <= diff <= 9.0 else 0.0)
    else:
        sc_trends.append(0.0)
    sc_trend = sum(sc_trends) / len(sc_trends) if sc_trends else 0.0

    weights = {"cis_trans": 0.15, "activation": 0.15, "interaction": 0.30, "distance": 0.10, "trend": 0.30}
    total = (sc_cis_trans * weights["cis_trans"] +
             sc_act * weights["activation"] +
             sc_int_avg * weights["interaction"] +
             sc_dist_avg * weights["distance"] +
             sc_trend * weights["trend"])
    return total


_SCORERS = {
    'computed_results_main': score_0,
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
