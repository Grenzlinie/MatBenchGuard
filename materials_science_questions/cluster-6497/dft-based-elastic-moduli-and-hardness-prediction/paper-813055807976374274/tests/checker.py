import os
import json
import csv

# === author imports / helpers ===
import json, csv, os, math


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


# === block: score_0 (check id='candidate_energies') ===
def score_0(artifact, step, ctx):
        energies = artifact
        comparisons = step.get("comparisons", [])
        tol = step.get("tolerance_eV", 0.2)
        if not isinstance(energies, dict) or len(comparisons) == 0:
            return 0.0
        scores = []
        for comp in comparisons:
            s1 = comp["struct1"]
            s2 = comp["struct2"]
            gold_diff = comp["gold_diff_eV"]
            expected_lower = comp.get("expected_lower")
            if s1 not in energies or s2 not in energies:
                scores.append(0.0)
                continue
            diff = energies[s1] - energies[s2]
            # sign check
            if expected_lower == s1:
                if diff > 0:
                    scores.append(0.0)
                    continue
            elif expected_lower == s2:
                if diff < 0:
                    scores.append(0.0)
                    continue
            if abs(abs(diff) - gold_diff) <= tol:
                scores.append(1.0)
            else:
                scores.append(0.0)
        return sum(scores) / len(scores)


# === block: score_1 (check id='phonon_summary') ===
def score_1(artifact, step, ctx):
        expected = step.get("expected", {})
        if not isinstance(artifact, dict):
            return 0.0
        total = len(expected)
        if total == 0:
            return 0.0
        correct = 0.0
        for key, exp_val in expected.items():
            if key not in artifact:
                continue
            art_val = artifact[key]
            if isinstance(exp_val, dict) and 'stable' in exp_val:
                if isinstance(art_val, dict) and art_val.get('stable') == exp_val['stable']:
                    correct += 1.0
            else:
                if art_val == exp_val:
                    correct += 1.0
        return correct / total


# === block: score_2 (check id='stable_structures') ===
def score_2(artifact, step, ctx):
        expected = set(step.get("expected_lines", []))
        if not isinstance(artifact, str):
            return 0.0
        lines = [line.strip() for line in artifact.split('\n') if line.strip()]
        found = set(lines)
        if found == expected:
            return 1.0
        # stricter: no extra structures
        return 0.0


# === block: score_3 (check id='mechanical_properties') ===
def score_3(artifact, step, ctx):
        gold = step.get("gold", {})
        tolerances = step.get("tolerances", {})
        if not isinstance(artifact, dict):
            return 0.0
        total_fields = 0
        pass_score = 0.0
        for struct in ["B2N4-I", "B3N3-I"]:
            for direction in ["biaxial", "X-axial", "Y-axial"]:
                for field in ["E_GPa", "Y_N_m", "tau_c_GPa", "epsilon_c"]:
                    total_fields += 1
                    gv = gold.get(struct, {}).get(direction, {}).get(field)
                    if gv is None:
                        continue
                    av = artifact.get(struct, {}).get(direction, {}).get(field)
                    if av is None:
                        continue
                    tol_cfg = tolerances.get(field, {})
                    if "relative" in tol_cfg:
                        rel = tol_cfg["relative"]
                        if abs(av - gv) <= rel * abs(gv):
                            pass_score += 1.0
                        elif abs(av - gv) <= 2 * rel * abs(gv):
                            pass_score += 0.5
                    elif "absolute" in tol_cfg:
                        abs_tol = tol_cfg["absolute"]
                        if abs(av - gv) <= abs_tol:
                            pass_score += 1.0
                        elif abs(av - gv) <= 2 * abs_tol:
                            pass_score += 0.5
                    else:
                        pass_score += 1.0
        if total_fields == 0:
            return 0.0
        return min(1.0, pass_score / total_fields)


# === block: score_4 (check id='band_gap_strain') ===
def score_4(artifact, step, ctx):
        rows = artifact
        required_strains = step.get("required_strains", list(range(0,9)))
        tol_gap = step.get("tolerance_gap_eV", 0.1)
        gap_0_target = step.get("gap_at_0_ev", 0.06)
        gap_8_target = step.get("gap_at_8_ev", 0.57)
        transition_range = step.get("direct_to_indirect_strain_range", [4,6])
        if not isinstance(rows, list):
            return 0.0
        strain_map = {}
        for row in rows:
            try:
                strain = int(row["strain_percent"])
                gap = float(row["band_gap_eV"])
                btype = row["band_type"].strip().lower()
                strain_map[strain] = {"gap": gap, "type": btype}
            except:
                pass
        if len(strain_map) == 0:
            return 0.0
        score = 0.0
        checks = 0
        # presence of required strains
        for s in required_strains:
            checks += 1
            if s in strain_map:
                score += 1.0
        # monotonic increase
        sorted_strains = sorted(strain_map.keys())
        monotonic = True
        for i in range(1, len(sorted_strains)):
            if strain_map[sorted_strains[i]]["gap"] < strain_map[sorted_strains[i-1]]["gap"] - 0.001:
                monotonic = False
                break
        checks += 1
        if monotonic:
            score += 1.0
        # endpoint gaps
        def check_gap(strain, target):
            if strain in strain_map:
                gap = strain_map[strain]["gap"]
                return abs(gap - target) <= tol_gap
            return False
        checks += 2
        if check_gap(0, gap_0_target):
            score += 1.0
        if check_gap(8, gap_8_target):
            score += 1.0
        # transition strain within [4,6]
        transition_strain = None
        for s in sorted_strains:
            btype = strain_map[s]["type"]
            if btype == "direct":
                continue
            else:
                transition_strain = s
                break
        checks += 1
        if transition_strain is not None and transition_range[0] <= transition_strain <= transition_range[1]:
            score += 1.0
        # consistency: all strains before transition are direct, after are indirect
        consistent = True
        trans_found = None
        for s in sorted_strains:
            btype = strain_map[s]["type"]
            if btype == "indirect":
                if trans_found is None:
                    trans_found = s
                else:
                    if trans_found > s:
                        consistent = False
            else:  # direct
                if trans_found is not None and s > trans_found:
                    consistent = False
        checks += 1
        if consistent:
            score += 1.0
        # presence of both direct and indirect
        has_direct = any(strain_map[s]["type"] == "direct" for s in strain_map)
        has_indirect = any(strain_map[s]["type"] == "indirect" for s in strain_map)
        checks += 1
        if has_direct and has_indirect:
            score += 1.0
        if checks == 0:
            return 0.0
        return min(1.0, score / checks)


_SCORERS = {
    'candidate_energies': score_0,
    'phonon_summary': score_1,
    'stable_structures': score_2,
    'mechanical_properties': score_3,
    'band_gap_strain': score_4,
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
