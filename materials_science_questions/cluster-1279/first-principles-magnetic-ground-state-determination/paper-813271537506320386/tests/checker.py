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
# ...
    return violations


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


# === block: score_0 (check id='binding_energies') ===
def score_0(artifact, step, ctx):
    clusters = artifact.get('clusters', [])
    gold_list = step.get('gold', [])
    tol = step.get('tolerance', 0.1)
    total_score = 0.0
    count = 0
    for g in gold_list:
        n = g['n']
        target = g['value']
        cluster = next((c for c in clusters if c.get('n') == n), None)
        if cluster is None or 'ground_state' not in cluster:
            continue
        val = cluster['ground_state'].get('binding_energy_eV_per_atom')
        if val is None:
            continue
        diff = max(0.0, target - val)
        if diff <= tol:
            total_score += 1.0
        else:
            total_score += max(0.0, 1.0 - (diff - tol) / (5.0 * tol))
        count += 1
    return total_score / count if count > 0 else 0.0


# === block: score_1 (check id='homo_lumo_gaps') ===
def score_1(artifact, step, ctx):
    clusters = artifact.get('clusters', [])
    if not clusters:
        return 0.0
    gaps = {}
    for c in clusters:
        n = c.get('n')
        if n is not None and c.get('ground_state', {}).get('homo_lumo_gap_eV') is not None:
            gaps[n] = c['ground_state']['homo_lumo_gap_eV']
    # require all n=1..5 present to evaluate trends
    if set(range(1, 6)) - set(gaps.keys()):
        return 0.0
    score = 0.0
    # global maximum at n=2 (the most chemically stable)
    if max(gaps, key=gaps.get) == 2:
        score += 0.6
    # local peak at n=4 (second local maximum in even-odd oscillation)
    if gaps.get(4, 0) > gaps.get(3, 0) and gaps.get(4, 0) > gaps.get(5, 0):
        score += 0.4
    return min(1.0, score)


# === block: score_2 (check id='total_magnetic_moments') ===
def score_2(artifact, step, ctx):
    clusters = artifact.get('clusters', [])
    if not clusters:
        return 0.0

    total_moments = {}
    avg_gd = {}
    avg_o = {}
    for c in clusters:
        n = c.get('n')
        gs = c.get('ground_state', {})
        if n is not None and gs:
            tm = gs.get('total_magnetic_moment_muB')
            gd = gs.get('avg_Gd_moment_muB')
            o = gs.get('avg_O_moment_muB')
            if tm is not None and gd is not None and o is not None:
                total_moments[n] = tm
                avg_gd[n] = gd
                avg_o[n] = o

    required = {1,2,3,4,5}
    if not required.issubset(total_moments.keys()):
        return 0.0

    # 1. Monotonic increase
    tm_sorted = [total_moments[i] for i in sorted(required)]
    monotonic = all(tm_sorted[i] <= tm_sorted[i+1] + 0.1 for i in range(len(tm_sorted)-1))
    score_mono = 1.0 if monotonic else 0.0

    # 2. Self-consistency with local moments (Gd–O antiferromagnetic)
    tolerance = 1.0  # μB
    consistent_count = 0
    for n in required:
        expected = n * avg_gd[n] - 3 * avg_o[n]
        diff = abs(total_moments[n] - expected)
        if diff <= tolerance:
            consistent_count += 1
    score_consist = consistent_count / len(required)

    return 0.5 * score_mono + 0.5 * score_consist


# === block: score_3 (check id='local_moments') ===
def score_3(artifact, step, ctx):
    import math
    clusters = artifact.get('clusters', [])
    gold_list = step.get('gold', [])
    tol_gd = step.get('tolerance_gd', 0.5)
    tol_o = step.get('tolerance_o', 0.2)
    total_score = 0.0
    count = 0
    for g in gold_list:
        n = g['n']
        tgt_gd = g['avg_Gd']
        tgt_o = g['avg_O']
        cluster = next((c for c in clusters if c.get('n') == n), None)
        if cluster is None or 'ground_state' not in cluster:
            continue
        v_gd = cluster['ground_state'].get('avg_Gd_moment_muB')
        v_o = cluster['ground_state'].get('avg_O_moment_muB')
        if v_gd is None or v_o is None:
            continue
        diff_gd = abs(v_gd - tgt_gd)
        diff_o = abs(v_o - tgt_o)
        score_gd = 1.0 if diff_gd <= tol_gd else max(0.0, 1.0 - (diff_gd - tol_gd) / (5.0 * tol_gd))
        score_o = 1.0 if diff_o <= tol_o else max(0.0, 1.0 - (diff_o - tol_o) / (5.0 * tol_o))
        total_score += 0.5 * score_gd + 0.5 * score_o
        count += 1
    return total_score / count if count > 0 else 0.0


# === block: score_4 (check id='bond_lengths') ===
def score_4(artifact, step, ctx):
    import math
    clusters = artifact.get('clusters', [])
    gold_list = step.get('gold', [])
    tol = step.get('tolerance', 0.01)
    total_score = 0.0
    count = 0
    for g in gold_list:
        n = g['n']
        target = g['value']
        cluster = next((c for c in clusters if c.get('n') == n), None)
        if cluster is None or 'ground_state' not in cluster:
            continue
        val = cluster['ground_state'].get('avg_bond_length_nm')
        if val is None:
            continue
        diff = abs(val - target)
        if diff <= tol:
            total_score += 1.0
        else:
            total_score += max(0.0, 1.0 - (diff - tol) / (5.0 * tol))
        count += 1
    return total_score / count if count > 0 else 0.0


# === block: score_5 (check id='symmetries') ===
def score_5(artifact, step, ctx):
    clusters = artifact.get('clusters', [])
    gold_list = step.get('gold', [])
    total_score = 0.0
    count = 0
    for g in gold_list:
        n = g['n']
        target_sym = g['value']
        cluster = next((c for c in clusters if c.get('n') == n), None)
        if cluster is None or 'ground_state' not in cluster:
            continue
        sym = cluster['ground_state'].get('symmetry', '').strip()
        total_score += 1.0 if sym == target_sym else 0.0
        count += 1
    return total_score / count if count > 0 else 0.0


# === block: score_6 (check id='isomer_energies') ===
def score_6(artifact, step, ctx):
    import math
    clusters = artifact.get('clusters', [])
    gold_list = step.get('gold', [])
    tol = step.get('tolerance', 0.05)
    total_score = 0.0
    count_pairs = 0
    for g in gold_list:
        n = g['n']
        cluster = next((c for c in clusters if c.get('n') == n), None)
        if cluster is None:
            continue
        isomers = cluster.get('low_lying_isomers', [])
        if len(isomers) < 2:
            continue
        iso1 = isomers[0]
        iso2 = isomers[1]
        expected = [
            (g['iso1_sym'], g['iso1_energy']),
            (g['iso2_sym'], g['iso2_energy'])
        ]
        pair_scores = []
        for exp_sym, exp_energy in expected:
            best_score = 0.0
            for iso in [iso1, iso2]:
                sym = iso.get('symmetry', '').strip()
                energy = iso.get('relative_energy_eV')
                if sym == exp_sym and energy is not None:
                    diff = abs(energy - exp_energy)
                    if diff <= tol:
                        best_score = max(best_score, 1.0)
                    else:
                        best_score = max(best_score, max(0.0, 1.0 - (diff - tol) / (5.0 * tol)))
            pair_scores.append(best_score)
        total_score += sum(pair_scores) / 2.0
        count_pairs += 1
    return total_score / count_pairs if count_pairs > 0 else 0.0


# === block: score_7 (check id='structural_consistency') ===
def score_7(artifact, step, ctx):
    clusters = artifact.get('clusters', [])
    if not clusters:
        return 0.0
    score = 0.0

    # monotonic increase of total magnetic moments
    moments = []
    for n in range(1, 6):
        cluster = next((c for c in clusters if c.get('n') == n), None)
        if cluster and cluster.get('ground_state', {}).get('total_magnetic_moment_muB') is not None:
            moments.append(cluster['ground_state']['total_magnetic_moment_muB'])
        else:
            moments.append(None)
    if all(m is not None for m in moments):
        inc = all(moments[i] <= moments[i+1] + 0.1 for i in range(len(moments)-1))
        score += 0.2 if inc else 0.0

    # Gd2O3 (n=2) has highest binding energy
    binding_energies = {}
    for c in clusters:
        n = c.get('n')
        if n and c.get('ground_state', {}).get('binding_energy_eV_per_atom') is not None:
            binding_energies[n] = c['ground_state']['binding_energy_eV_per_atom']
    if binding_energies:
        max_n = max(binding_energies, key=binding_energies.get)
        score += 0.2 if max_n == 2 else 0.0

    # HOMO-LUMO gap structural trends: global max at n=2, and even-odd oscillation with local peak at n=4
    gaps = {}
    for c in clusters:
        n = c.get('n')
        if n is not None and c.get('ground_state', {}).get('homo_lumo_gap_eV') is not None:
            gaps[n] = c['ground_state']['homo_lumo_gap_eV']
    if set(range(1, 6)).issubset(set(gaps.keys())):
        global_max_correct = (max(gaps, key=gaps.get) == 2)
        local_peak_correct = (gaps.get(4, 0) > gaps.get(3, 0) and gaps.get(4, 0) > gaps.get(5, 0))
        score += 0.2 if (global_max_correct and local_peak_correct) else 0.0

    # local Gd moments in [6.5, 8.5] muB
    gd_moments = []
    for c in clusters:
        if c.get('ground_state', {}).get('avg_Gd_moment_muB') is not None:
            gd_moments.append(c['ground_state']['avg_Gd_moment_muB'])
    if gd_moments:
        all_in_range = all(6.5 <= m <= 8.5 for m in gd_moments)
        score += 0.2 if all_in_range else 0.0

    # O moments small (<= 1.0 muB)
    o_moments = []
    for c in clusters:
        if c.get('ground_state', {}).get('avg_O_moment_muB') is not None:
            o_moments.append(c['ground_state']['avg_O_moment_muB'])
    if o_moments:
        all_small = all(m <= 1.0 for m in o_moments)
        score += 0.2 if all_small else 0.0

    return min(1.0, score)


_SCORERS = {
    'binding_energies': score_0,
    'homo_lumo_gaps': score_1,
    'total_magnetic_moments': score_2,
    'local_moments': score_3,
    'bond_lengths': score_4,
    'symmetries': score_5,
    'isomer_energies': score_6,
    'structural_consistency': score_7,
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
    # Validate output contract first; log violations but do not block scoring
    violations = _ff_validate_output_contract()
    os.makedirs("/logs/verifier", exist_ok=True)
    if violations:
        with open("/logs/verifier/contract_violations.json", "w") as f:
            json.dump(violations, f, indent=2)

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