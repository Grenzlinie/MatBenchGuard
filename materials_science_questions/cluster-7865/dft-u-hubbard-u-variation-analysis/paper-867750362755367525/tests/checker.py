import os
import json
import csv

# === author imports / helpers ===
import json
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
    import os
    try:
        with open(os.path.join(outputs_dir, "phase_energies.json")) as f:
            phase_data = json.load(f)
    except Exception:
        phase_data = []
    return {"phase_data": phase_data}


# === block: score_0 (check id='phase_energies') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0
    required_keys = {"strain","E_upup_downdown","E_upup_upup","E_updown_updown"}
    for entry in artifact:
        if not isinstance(entry, dict) or not required_keys.issubset(entry.keys()):
            return 0.0
    entries = sorted(artifact, key=lambda x: x["strain"])
    strains = [e["strain"] for e in entries]
    if strains[0] > -0.055 or strains[-1] < 0.055 or len(entries) < 11:
        return 0.0
    gs = []
    for e in entries:
        vals = {0: e["E_upup_downdown"], 1: e["E_upup_upup"], 2: e["E_updown_updown"]}
        min_key = min(vals, key=vals.get)
        gs.append(min_key)
    idx0 = None
    for i, s in enumerate(strains):
        if abs(s) < 1e-6:
            idx0 = i
            break
    if idx0 is None:
        idx0 = min(range(len(strains)), key=lambda i: abs(strains[i]))
    score_gs0 = 1.0 if gs[idx0] == 0 else 0.0
    trans1_strain = None
    for i in range(idx0-1, -1, -1):
        if gs[i] == 1:
            trans1_strain = strains[i]
            break
    r1 = step.get("trans1_range", [-0.03, -0.005])
    score_trans1 = 1.0 if trans1_strain is not None and r1[0] <= trans1_strain <= r1[1] else 0.0
    trans2_strain = None
    for i in range(idx0-1, -1, -1):
        if gs[i] == 2:
            trans2_strain = strains[i]
            break
    r2 = step.get("trans2_range", [-0.065, -0.04])
    score_trans2 = 1.0 if trans2_strain is not None and r2[0] <= trans2_strain <= r2[1] else 0.0
    delta = entries[idx0]["E_upup_upup"] - entries[idx0]["E_upup_downdown"]
    target = step.get("delta_E_target", 0.5)
    tol = step.get("delta_E_tolerance_abs", 0.1)
    score_delta = 1.0 if abs(delta - target) <= tol else 0.0
    weights = {"gs0": 0.2, "trans1": 0.3, "trans2": 0.3, "delta": 0.2}
    total = score_gs0*weights["gs0"] + score_trans1*weights["trans1"] + score_trans2*weights["trans2"] + score_delta*weights["delta"]
    return max(0.0, min(1.0, total))


# === block: score_1 (check id='exchange_tc') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0
    for e in artifact:
        if not all(k in e for k in ("strain","J_intra","J_inter_first","J_inter_second","Tc")):
            return 0.0
    entries = sorted(artifact, key=lambda x: x["strain"])
    strains = [e["strain"] for e in entries]
    j_intra = [e["J_intra"] for e in entries]
    j_inter_first = [e["J_inter_first"] for e in entries]
    Tc = [e["Tc"] for e in entries]
    neg_max = step.get("J_intra_neg_strain_max", -0.04)
    pos_min = step.get("J_intra_pos_strain_min", -0.02)
    neg_indices = [i for i, s in enumerate(strains) if s <= neg_max]
    pos_indices = [i for i, s in enumerate(strains) if s >= pos_min]
    j_intra_negative = all(j_intra[i] < 0 for i in neg_indices) if neg_indices else False
    j_intra_positive = all(j_intra[i] > 0 for i in pos_indices) if pos_indices else False
    score_jintra = 1.0 if (j_intra_negative and j_intra_positive) else 0.0
    cross_range = step.get("J_inter_first_cross_range", [-0.015, -0.005])
    signs = []
    for i, s in enumerate(strains):
        if cross_range[0] <= s <= cross_range[1]:
            signs.append(j_inter_first[i])
    has_pos = any(x > 0 for x in signs)
    has_neg = any(x < 0 for x in signs)
    score_jinter = 1.0 if (has_pos and has_neg) else 0.0
    idx0 = min(range(len(strains)), key=lambda i: abs(strains[i]))
    tc0 = Tc[idx0]
    target0 = step.get("Tc_at_0_target", 44.0)
    tol0 = step.get("Tc_at_0_tol_ratio", 0.2)
    score_tc0 = 1.0 if abs(tc0 - target0) / target0 <= tol0 else 0.0
    idx_m3 = min(range(len(strains)), key=lambda i: abs(strains[i] + 0.03))
    tc_m3 = Tc[idx_m3]
    target_m3 = step.get("Tc_at_m3_target", 14.0)
    tol_m3 = step.get("Tc_at_m3_tol_ratio", 0.2)
    score_tcm3 = 1.0 if abs(tc_m3 - target_m3) / target_m3 <= tol_m3 else 0.0
    neg_entries = sorted([e for e in entries if e["strain"] <= 0.0], key=lambda x: x["strain"])
    Tc_neg = [e["Tc"] for e in neg_entries]
    if len(Tc_neg) > 1:
        mono = all(Tc_neg[i] <= Tc_neg[i+1] for i in range(len(Tc_neg)-1))
    else:
        mono = False
    score_mono = 1.0 if mono else 0.0
    scores = [score_jintra, score_jinter, score_tc0, score_tcm3, score_mono]
    return sum(scores) / len(scores)


# === block: score_2 (check id='lc_mae') ===
def score_2(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0
    strains_set = set()
    for e in artifact:
        if not all(k in e for k in ("strain","angle_deg","energy_meV")):
            return 0.0
        strains_set.add(e["strain"])
    if not strains_set.issubset({-0.05, 0.0, 0.05}):
        return 0.0
    strain_dict = defaultdict(list)
    for e in artifact:
        strain_dict[e["strain"]].append((e["angle_deg"], e["energy_meV"]))
    phase_data = ctx.get("phase_data", [])
    if not phase_data:
        return 0.0
    phase_dict = {}
    for p in phase_data:
        phase_dict[p["strain"]] = p["E_upup_downdown"] - p["E_upup_upup"]
    tol = step.get("delta_tol_meV", 0.1)
    consist_score = 0.0
    monot_score = 0.0
    for strain in [-0.05, 0.0, 0.05]:
        if strain not in strain_dict or strain not in phase_dict:
            continue
        points = strain_dict[strain]
        angle180_e = None
        for a, en in points:
            if abs(a - 180) < 1e-6:
                angle180_e = en
                break
        if angle180_e is None:
            max_angle = max(a for a, _ in points)
            angle180_e = next(en for a, en in points if a == max_angle)
        expected = phase_dict[strain]
        if abs(angle180_e - expected) <= tol:
            consist_score += 1.0
        sorted_pts = sorted(points, key=lambda x: x[0])
        energies = [v for _, v in sorted_pts]
        if len(energies) < 2:
            continue
        peak_idx = energies.index(max(energies))
        inc = all(energies[i] <= energies[i+1] for i in range(peak_idx))
        dec = all(energies[i] >= energies[i+1] for i in range(peak_idx, len(energies)-1))
        if inc and dec:
            monot_score += 1.0
    n = len(strains_set)
    if n == 0:
        return 0.0
    consist_score /= n
    monot_score /= n
    total = 0.5 * consist_score + 0.5 * monot_score
    return max(0.0, min(1.0, total))


_SCORERS = {
    'phase_energies': score_0,
    'exchange_tc': score_1,
    'lc_mae': score_2,
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
