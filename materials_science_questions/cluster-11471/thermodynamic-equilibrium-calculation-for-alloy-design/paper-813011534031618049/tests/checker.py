import os
import json
import csv

# === author imports / helpers ===
import json, csv, math
from itertools import groupby


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
    return {
        'phase_diagrams': next(s for s in spec['steps'] if s['id'] == 'phase_diagrams'),
        'solidification': next(s for s in spec['steps'] if s['id'] == 'solidification_paths'),
        'driving_force': next(s for s in spec['steps'] if s['id'] == 'driving_force')
    }


# === block: score_0 (check id='phase_diagrams') ===
def score_0(artifact, step, ctx):
    if artifact is None or not isinstance(artifact, list):
        return 0.0
    if len(artifact) < 8:
        return 0.0

    required_keys = {'Cr_wt', 'C_min_wt', 'C_max_wt', 'T_min_C', 'T_max_C'}
    ok = 0
    total = 0
    for entry in artifact:
        if not isinstance(entry, dict) or not required_keys.issubset(entry.keys()):
            continue
        try:
            cr = float(entry['Cr_wt'])
            c_min = float(entry['C_min_wt'])
            c_max = float(entry['C_max_wt'])
            t_min = float(entry['T_min_C'])
            t_max = float(entry['T_max_C'])
        except (ValueError, TypeError):
            continue
        if cr <= 0 or c_min <= 0 or c_max <= c_min or t_min <= 0 or t_max <= t_min:
            total += 1
            continue

        # Paper states C_min ≈ 0.06·Cr, C_max ≈ 0.1·Cr; allow generous relative tolerance
        good_c_min = (0.04 * cr) <= c_min <= (0.08 * cr)
        good_c_max = (0.08 * cr) <= c_max <= (0.12 * cr)
        # T_min near ferrite–austenite transition ~815 °C, T_max around eutectic ~1280 °C
        good_t_min = 750 <= t_min <= 900
        good_t_max = 1200 <= t_max <= 1350

        if good_c_min and good_c_max and good_t_min and good_t_max:
            ok += 1
        total += 1

    return ok / total if total > 0 else 0.0


# === block: score_1 (check id='solidification_paths') ===
def score_1(artifact, step, ctx):
    if artifact is None or not isinstance(artifact, list):
        return 0.0
    step = ctx['solidification']
    checks = step['checks']
    # structural_eutectic check
    cols = set(artifact[0].keys()) if artifact else set()
    required = {'composition', 'model', 'step_order', 'phases_sequence'}
    if not required.issubset(cols):
        return 0.0
    # group by composition and model
    groups = {}
    for row in artifact:
        key = (row['composition'], row['model'])
        groups.setdefault(key, []).append(row)
    # check 1: Scheil eutectic
    scheil_alloys = ['45Cr-4.0C','40Cr-3.5C','35Cr-3.0C','30Cr-2.3C','25Cr-2.0C','20Cr-1.5C','15Cr-1C','10Cr-0.75C','10Cr-5C']
    all_scheil_ok = True
    for alloy in scheil_alloys:
        key = (alloy, 'Scheil')
        steps_list = groups.get(key, [])
        # look for a step whose phases_sequence contains (Fcc or Bcc) and M7C3
        eutectic_found = False
        for s in steps_list:
            ps = s.get('phases_sequence', '')
            if ('M7C3' in ps) and (('Fcc' in ps) or ('Bcc' in ps)):
                eutectic_found = True
                break
        if not eutectic_found:
            all_scheil_ok = False
            break
    check1_score = 1.0 if all_scheil_ok else 0.0
    # check 2: Lever absence for 10Cr-0.75C
    lever_key = ('10Cr-0.75C', 'Lever')
    lever_steps = groups.get(lever_key, [])
    eutectic_in_lever = any(('M7C3' in s.get('phases_sequence','') and (('Fcc' in s.get('phases_sequence','')) or ('Bcc' in s.get('phases_sequence','')))) for s in lever_steps)
    check2_score = 0.0 if eutectic_in_lever else 1.0
    # check 3: reference_sequence (optional partial credit)
    ref_sequences = checks[2]['reference_sequences']
    tol_temp = checks[2]['tolerance_temp']
    seq_ok = 0.0
    seq_total = 0.0
    for key_spec, ref_steps in ref_sequences.items():
        alloy, model = key_spec.rsplit('_', 1)
        key = (alloy, model)
        agent_steps = sorted(groups.get(key, []), key=lambda r: int(r.get('step_order', 0)))
        if len(agent_steps) != len(ref_steps):
            continue
        correct = 0
        for agent_step, ref_step in zip(agent_steps, ref_steps):
            if agent_step.get('phases_sequence', '') == ref_step['phases']:
                # check temperature tolerance
                try:
                    start = float(agent_step.get('start_temp_C', 0))
                    end = float(agent_step.get('end_temp_C', 0))
                    # reference do not specify exact temps, so just skip temp check
                    correct += 1
                except:
                    pass
        seq_ok += correct / len(ref_steps) if ref_steps else 1.0
        seq_total += 1.0
    check3_score = seq_ok / seq_total if seq_total > 0 else 0.0
    # combine: 0.5 weight to eutectic structural checks, 0.5 to reference sequences
    score = 0.5 * ((check1_score + check2_score) / 2.0) + 0.5 * check3_score
    return score


# === block: score_2 (check id='driving_force') ===
def score_2(artifact, step, ctx):
    if artifact is None or not isinstance(artifact, list):
        return 0.0
    step = ctx['driving_force']
    checks = step['checks']
    ref_force = checks[1]['reference']
    ref_shell = checks[2]['reference']
    tol = checks[1]['tolerance']
    # build dict from artifact
    agent_data = {}
    for row in artifact:
        comp = row.get('composition')
        if comp:
            agent_data[comp] = row
    num_total = len(ref_force)
    if num_total == 0:
        return 0.0
    force_correct = 0
    shell_correct = 0
    for comp, target_force in ref_force.items():
        row = agent_data.get(comp)
        if row is None:
            continue
        try:
            agent_force = float(row.get('driving_force_J_per_mol', 0))
        except:
            agent_force = None
        if agent_force is not None and abs(agent_force - target_force) <= tol:
            force_correct += 1
        agent_shell = row.get('shell_possible')
        if agent_shell is not None:
            # normalize True/False string
            if isinstance(agent_shell, str):
                agent_shell = agent_shell.strip().lower() in ('true','1','yes')
            if agent_shell == ref_shell[comp]:
                shell_correct += 1
    score = 0.6 * (force_correct / num_total) + 0.4 * (shell_correct / num_total)
    return score


_SCORERS = {
    'phase_diagrams': score_0,
    'solidification_paths': score_1,
    'driving_force': score_2,
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
