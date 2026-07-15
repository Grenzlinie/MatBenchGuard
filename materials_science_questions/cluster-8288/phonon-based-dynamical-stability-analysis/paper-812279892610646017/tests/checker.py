import os
import json
import csv

# === author imports / helpers ===
import math
import csv
import os


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
    ctx = {}
    for s in spec['steps']:
        ctx[s['id']] = s.get('params', {})
    return ctx


# === block: score_0 (check id='step_01_structural') ===
def score_0(artifact, step, ctx):
    rows = artifact  # list of dicts
    params = ctx[step['id']]
    required_cols = params['required_columns']
    # check columns
    if not rows or not all(col in rows[0] for col in required_cols):
        return 0.0
    # sort by pressure
    rows_sorted = sorted(rows, key=lambda r: float(r['pressure_GPa']))
    # monotonicity checks
    mono = params.get('monotonicity', {})
    field_mono_ok = {}
    for field, direction in mono.items():
        vals = [float(r[field]) for r in rows_sorted]
        if direction == 'non-increasing':
            ok = all(vals[i] >= vals[i+1] - 1e-6 for i in range(len(vals)-1))
        else:
            ok = all(vals[i] <= vals[i+1] + 1e-6 for i in range(len(vals)-1))
        field_mono_ok[field] = ok
    # closeness to references at selected pressures
    tolerances = params['tolerances']
    references = params['references']
    check_pressures = params['check_pressures']
    total_ref = len(check_pressures)
    pass_ref = 0
    for ptarget in check_pressures:
        if str(ptarget) not in references:
            continue
        ref = references[str(ptarget)]
        # find closest row
        best = min(rows_sorted, key=lambda r: abs(float(r['pressure_GPa']) - ptarget))
        # extra: ensure pressure difference is reasonable (<=1.0 GPa)
        if abs(float(best['pressure_GPa']) - ptarget) > 1.0:
            continue
        ok = True
        for field in ['c_over_a','u_ScN','u_GaN','volume_per4atoms_Bohr3']:
            if field not in tolerances or field not in ref:
                continue
            val = float(best[field])
            tol = tolerances[field]
            if abs(val - ref[field]) > tol:
                ok = False
                break
        if ok:
            pass_ref += 1
    # scoring weights
    col_ok = 1.0
    mono_ok = sum(field_mono_ok.values()) / max(len(field_mono_ok), 1)
    ref_match = pass_ref / total_ref if total_ref > 0 else 0.0
    return 0.1 * col_ok + 0.2 * mono_ok + 0.7 * ref_match


# === block: score_1 (check id='step_02_transition') ===
def score_1(artifact, step, ctx):
    txt = artifact  # string containing the number
    params = ctx[step['id']]
    ref_val = params['reference']
    tol = params['tolerance']
    try:
        val = float(txt.strip())
        if abs(val - ref_val) <= tol:
            return 1.0
        else:
            return 0.0
    except:
        return 0.0


# === block: score_2 (check id='step_03_piezoelectric') ===
def score_2(artifact, step, ctx):
    txt = artifact
    params = ctx[step['id']]
    ref_val = params['reference']
    tol = params['tolerance']
    try:
        val = float(txt.strip())
        if abs(val - ref_val) <= tol:
            return 1.0
        else:
            return 0.0
    except:
        return 0.0


# === block: score_3 (check id='step_04_phonon') ===
def score_3(artifact, step, ctx):
    rows = artifact
    params = ctx[step['id']]
    required_cols = params['required_columns']
    if not rows or not all(col in rows[0] for col in required_cols):
        return 0.0
    # sort by pressure
    rows_sorted = sorted(rows, key=lambda r: float(r['pressure_GPa']))
    # check softening: freq at low P > freq at high P near transition
    freq_map = {}
    for r in rows_sorted:
        p = float(r['pressure_GPa'])
        f = float(r['A1_TO_frequency_cm-1'])
        freq_map[p] = f
    # Find the minimum frequency and its pressure
    min_p = min(freq_map, key=lambda p: freq_map[p])
    min_f = freq_map[min_p]
    # Requirement: minimum frequency near 12 GPa (within 2 GPa) and less than 50 cm^-1
    if abs(min_p - 12.0) > 2.0 or min_f > 50.0:
        return 0.0
    # Also check that frequency at 8 GPa > 12 GPa and at 14 GPa > 12 GPa (if present)
    if 8.0 in freq_map and freq_map[8.0] <= min_f + 1e-6:
        return 0.5
    if 14.0 in freq_map and freq_map[14.0] <= min_f + 1e-6:
        return 0.5
    # additional check: reference values at given pressures
    refs = params.get('references', {})
    tol = params.get('tolerances', {}).get('A1_TO_frequency_cm-1', 50.0)
    total_ref = 0
    pass_ref = 0
    for p_str, ref_val in refs.items():
        ptarget = float(p_str)
        # find closest pressure
        best = min(rows_sorted, key=lambda r: abs(float(r['pressure_GPa']) - ptarget))
        if abs(float(best['pressure_GPa']) - ptarget) > 1.0:
            continue
        total_ref += 1
        if abs(float(best['A1_TO_frequency_cm-1']) - ref_val) <= tol:
            pass_ref += 1
    ref_frac = pass_ref / total_ref if total_ref > 0 else 0.0
    return 0.5 * max(0.0, min(1.0, (1.0 - abs(min_p-12.0)/2.0))) + 0.3 * (1.0 if min_f < 50.0 else 0.0) + 0.2 * ref_frac


_SCORERS = {
    'step_01_structural': score_0,
    'step_02_transition': score_1,
    'step_03_piezoelectric': score_2,
    'step_04_phonon': score_3,
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
