import os
import json
import csv

# === author imports / helpers ===
import os
import json
import csv
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
    spec = {}  # injected; loading handled by framework
    return {"spec": spec}


# === block: score_0 (check id='trap_levels') ===
def score_0(artifact, step, ctx):
    import json
    from pathlib import Path
    artifact_path = Path('/app/outputs/bandstructure_trap_levels.json')
    if not artifact_path.exists():
        return 0.0
    with open(artifact_path) as f:
        artifact = json.load(f)
    defects = artifact.get('defects')
    if not isinstance(defects, list) or not defects:
        return 0.0
    gold_defects = step.get('gold', {}).get('defects', [])
    tol = step.get('gold', {}).get('tolerance_trap_energy_eV', 0.1)
    band_gap_tol = step.get('gold', {}).get('tolerance_band_gap_eV', 0.1)
    score_total = 0.0
    n_defects = len(gold_defects)
    if n_defects == 0:
        return 0.0
    for gd in gold_defects:
        gname = gd['name']
        gtraps = sorted(gd.get('trap_energies', []))
        gband = gd.get('band_gap', None)
        adef = None
        for d in defects:
            if d.get('name', '') == gname:
                adef = d
                break
        if adef is None:
            continue
        atrap = sorted(adef.get('trap_energies', []))
        aband = adef.get('band_gap', None)
        # trap score
        if len(gtraps) == 0 and len(atrap) == 0:
            trap_score = 1.0
        elif len(gtraps) == 0 or len(atrap) == 0:
            trap_score = 0.0
        else:
            max_len = max(len(gtraps), len(atrap))
            matches = 0
            for gval in gtraps:
                for aval in atrap:
                    if abs(gval - aval) <= tol:
                        matches += 1
                        break
            trap_score = matches / max_len
        # band gap score
        if gband is not None and aband is not None:
            band_score = 1.0 if abs(aband - gband) <= band_gap_tol else 0.0
        else:
            band_score = 1.0
        defect_score = 0.8 * trap_score + 0.2 * band_score
        score_total += defect_score
    return score_total / n_defects


# === block: score_1 (check id='neb_barriers') ===
def score_1(artifact, step, ctx):
    import json
    from pathlib import Path
    import re

    artifact_path = Path('/app/outputs/neb_barriers.json')
    if not artifact_path.exists():
        return 0.0
    with open(artifact_path) as f:
        artifact = json.load(f)
    reactions = artifact.get('reactions')
    if not isinstance(reactions, list) or not reactions:
        return 0.0
    gold_reactions = step.get('gold', {}).get('reactions', [])
    if not gold_reactions:
        return 0.0

    def normalize_pathway(s):
        s = s.lower()
        s = re.sub(r'[^a-z0-9\s]', ' ', s)
        return set(s.split())

    score_total = 0.0
    for gr in gold_reactions:
        gpath = gr['pathway']
        gbar = gr['barrier_height_gold']
        tol = gr.get('tolerance_eV', 0.05)
        g_tokens = normalize_pathway(gpath)
        areact = None
        for r in reactions:
            a_tokens = normalize_pathway(r.get('pathway', ''))
            # require all gold tokens appear in agent's string, or all agent tokens appear in gold
            if g_tokens.issubset(a_tokens) or g_tokens.issuperset(a_tokens):
                areact = r
                break
        if areact is None:
            continue
        abar = areact.get('barrier_height')
        if abar is None:
            react_score = 0.0
        else:
            react_score = max(0.0, 1.0 - abs(abar - gbar) / tol) if tol > 0 else (1.0 if abs(abar - gbar) < 1e-9 else 0.0)
        score_total += react_score
    return score_total / len(gold_reactions)


# === block: score_2 (check id='iv_curve') ===
def score_2(artifact, step, ctx):
    import csv
    from pathlib import Path
    artifact_path = Path('/app/outputs/iv_characteristics.csv')
    if not artifact_path.exists():
        return 0.0
    with open(artifact_path, newline='') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    if not rows:
        return 0.0
    try:
        vg_list = []
        id_list = []
        for r in rows:
            vg_list.append(float(r['Vg']))
            id_list.append(float(r['Id']))
    except (KeyError, ValueError):
        return 0.0
    if len(vg_list) < 50:
        return 0.0
    # find leakage at Vg=0 (closest)
    leakage = None
    for vg, id_val in zip(vg_list, id_list):
        if abs(vg) < 1e-9:
            leakage = id_val
            break
    if leakage is None:
        # interpolate
        leakage = 0.0  # fallback but low score
    leakage_gold = step.get('gold', {}).get('leakage_A_per_um', 1e-13)
    leakage_tol = step.get('gold', {}).get('leakage_relative_tol', 0.20)
    vth_target = step.get('gold', {}).get('vth_id_target_A_per_um', 1e-8)
    vth_gold = step.get('gold', {}).get('vth_gold_V', 2.12)
    vth_tol = step.get('gold', {}).get('vth_tolerance_abs_V', 0.5)
    # compute Vth: Vg where Id closest to target
    def find_vth(vgs, ids, target):
        best_vg = None
        best_diff = float('inf')
        for vg, id_val in zip(vgs, ids):
            diff = abs(id_val - target)
            if diff < best_diff:
                best_diff = diff
                best_vg = vg
        return best_vg
    vth_agent = find_vth(vg_list, id_list, vth_target)
    leakage_score = 0.0
    if leakage > 0:
        rel_error = abs(leakage - leakage_gold) / leakage_gold
        leakage_score = max(0.0, 1.0 - rel_error / leakage_tol) if leakage_tol > 0 else (1.0 if rel_error < 1e-9 else 0.0)
    else:
        leakage_score = 0.0
    vth_score = 0.0
    if vth_agent is not None:
        vth_score = max(0.0, 1.0 - abs(vth_agent - vth_gold) / vth_tol)
    return (leakage_score + vth_score) / 2.0


_SCORERS = {
    'trap_levels': score_0,
    'neb_barriers': score_1,
    'iv_curve': score_2,
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
