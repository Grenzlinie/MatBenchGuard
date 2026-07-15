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
    return {}


# === block: score_0 (check id='step_02_total_energies') ===
def score_0(artifact, step, ctx):
    energies = {}
    for row in artifact:
        cfg = row.get('spin_configuration', '').strip()
        val = float(row.get('total_energy_per_fu', 0))
        energies[cfg] = val
    gold = step.get('gold_energies', {})
    tol = step.get('energy_tol', 0.5)
    gold_afm_c2 = gold.get('AFM-C2')
    if 'AFM-C2' not in energies:
        return 0.0
    afm_c2 = energies['AFM-C2']
    score = 0.0
    # ordering check: AFM-C2 lowest
    others = {k:v for k,v in energies.items() if k != 'AFM-C2'}
    if others and afm_c2 <= min(others.values()):
        score += 0.5
    # full correct ordering: AFM-C2 < AFM-C1 < ferri < FM < NM
    order = ['AFM-C2','AFM-C1','ferri','FM','NM']
    sorted_configs = sorted(energies.items(), key=lambda x: x[1])
    if [cfg for cfg,_ in sorted_configs] == order:
        score += 0.3
    # numeric check on AFM-C2 energy
    if gold_afm_c2 is not None:
        num_score = max(0.0, 1.0 - abs(afm_c2 - gold_afm_c2) / tol)
        score += 0.2 * num_score
    return min(score, 1.0)


# === block: score_1 (check id='step_03_band_gap') ===
def score_1(artifact, step, ctx):
    gap = artifact.get('band_gap_GGA')
    type = artifact.get('gap_type', '').strip().lower()
    if gap is None:
        return 0.0
    gap_gold = step.get('band_gap_gold', 0.78)
    tol = step.get('gap_tol', 0.2)
    gap_score = max(0.0, 1.0 - abs(float(gap) - gap_gold) / tol)
    type_score = 1.0 if type == step.get('gap_type_gold', 'indirect') else 0.0
    return gap_score * 0.8 + type_score * 0.2


# === block: score_2 (check id='step_04_magnetic_moments') ===
def score_2(artifact, step, ctx):
    m1 = artifact.get('Mn1_moment')
    m2 = artifact.get('Mn2_moment')
    if m1 is None or m2 is None:
        return 0.0
    gold = step.get('moments_gold', {})
    g1 = gold.get('Mn1_moment', 3.3177)
    g2 = gold.get('Mn2_moment', 2.5403)
    tol = step.get('moment_tol', 0.1)
    s1 = max(0.0, 1.0 - abs(float(m1) - g1) / tol)
    s2 = max(0.0, 1.0 - abs(float(m2) - g2) / tol)
    return (s1 + s2) / 2.0


# === block: score_3 (check id='step_05_born_effective_charge') ===
def score_3(artifact, step, ctx):
    cols = ['Zxx','Zyy','Zzz','Zxy','Zxz','Zyz','Zyx','Zzx','Zzy']
    if not artifact or not isinstance(artifact, list):
        return 0.0
    gold = step.get('born_gold', {})
    tols = step.get('born_tolerances', {})
    default_tol = tols.get('default', 2.0)
    per_atom_scores = []
    for row in artifact:
        atom = row.get('atom', '').strip()
        if atom not in gold:
            continue
        gvec = gold[atom]
        atom_tols = tols.get(atom, [default_tol]*9)
        comp_scores = []
        for ci, col in enumerate(cols):
            agent_val = float(row.get(col, 0.0))
            gold_val = float(gvec[ci])
            t = atom_tols[ci] if ci < len(atom_tols) else default_tol
            comp_scores.append(max(0.0, 1.0 - abs(agent_val - gold_val) / t))
        if comp_scores:
            per_atom_scores.append(sum(comp_scores) / len(comp_scores))
    if not per_atom_scores:
        return 0.0
    return sum(per_atom_scores) / len(per_atom_scores)


# === block: score_4 (check id='step_06_polarization') ===
def score_4(artifact, step, ctx):
    P = artifact.get('spontaneous_polarization_P')
    if P is None:
        return 0.0
    gold_p = step.get('polarization_gold', 6.0)
    tol = step.get('polarization_tol', 1.0)
    return max(0.0, 1.0 - abs(float(P) - gold_p) / tol)


_SCORERS = {
    'step_02_total_energies': score_0,
    'step_03_band_gap': score_1,
    'step_04_magnetic_moments': score_2,
    'step_05_born_effective_charge': score_3,
    'step_06_polarization': score_4,
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
