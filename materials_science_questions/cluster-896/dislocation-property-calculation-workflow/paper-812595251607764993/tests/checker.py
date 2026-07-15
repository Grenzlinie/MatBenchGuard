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
    def prepare(outputs_dir, spec):
        ctx = {}
        steps = spec.get('steps', [])
        for step in steps:
            if step.get('id') == 'mep_barrier_and_trend':
                ref = step.get('reference', {})
                ctx['barrier_target'] = {float(k): v for k, v in ref.get('barrier_meV_per_atom', {}).items()}
                ctx['tolerance'] = ref.get('tolerance', 0.20)
            elif step.get('id') == 'hysteresis':
                ranges = step.get('ranges', {})
                ctx['forward_transition_range'] = ranges.get('forward_onset_GPa', [80, 100])
                ctx['reverse_transition_range'] = ranges.get('reverse_onset_GPa', [110, 130])
                ctx['hysteresis_min'] = ranges.get('hysteresis_min_GPa', 10.0)
        return ctx


# === block: score_0 (check id='mep_barrier_and_trend') ===
def score_0(artifact, step, ctx):
    rows = artifact
    import math
    data = {}
    for r in rows:
        a0 = float(r['a0'])
        e = float(r['energy_meV_per_atom'])
        s = float(r['s'])
        if a0 not in data:
            data[a0] = []
        data[a0].append((s, e))
    barriers = {}
    for a0, pts in data.items():
        max_e = -float('inf')
        for s_val, e_val in pts:
            if e_val > max_e:
                max_e = e_val
        barriers[a0] = max_e
    target = ctx['barrier_target']
    tol = ctx['tolerance']
    scores_barrier = []
    for a0 in sorted(target.keys()):
        if a0 in barriers:
            e = barriers[a0]
            ref = target[a0]
            rel_err = abs(e - ref) / ref if ref != 0 else abs(e)
            if rel_err <= tol:
                scores_barrier.append(1.0)
            else:
                scores_barrier.append(max(0.0, 1.0 - (rel_err - tol) / 0.5))
        else:
            scores_barrier.append(0.0)
    barrier_score = sum(scores_barrier) / len(scores_barrier) if scores_barrier else 0.0
    sorted_a0 = sorted(target.keys())
    trend_ok = all(barriers.get(sorted_a0[i+1], float('inf')) < barriers.get(sorted_a0[i], float('-inf')) for i in range(len(sorted_a0)-1))
    trend_score = 1.0 if trend_ok else 0.0
    return 0.8 * barrier_score + 0.2 * trend_score


# === block: score_1 (check id='shear_nucleation') ===
def score_1(artifact, step, ctx):
    rows = artifact
    early_success = False
    max_hcp = 0.0
    limit = 0.30
    threshold = 0.1
    for r in rows:
        s = float(r['s'])
        h = float(r['hcp_fraction'])
        if s < limit and h > threshold:
            early_success = True
        if h > max_hcp:
            max_hcp = h
    score_early = 1.0 if early_success else 0.0
    score_complete = 1.0 if max_hcp >= 0.8 else max_hcp / 0.8
    return 0.6 * score_early + 0.4 * score_complete


# === block: score_2 (check id='hysteresis') ===
def score_2(artifact, step, ctx):
    rows = artifact
    vols = []
    press = []
    phase = []
    for r in rows:
        vols.append(float(r['volume_bohr3_per_atom']))
        press.append(float(r['pressure_GPa']))
        phase.append(r['phase_label'])
    forward_onset_idx = None
    for i, ph in enumerate(phase):
        if ph != 'bcc':
            forward_onset_idx = i
            break
    turn_idx = None
    for i in range(1, len(vols)):
        if vols[i] < vols[i-1]:
            turn_idx = i
            break
    if turn_idx is None:
        turn_idx = len(vols)
    reverse_onset_idx = None
    for i in range(turn_idx, len(vols)):
        if phase[i] != 'hcp':
            reverse_onset_idx = i
            break
    fr = ctx['forward_transition_range']
    rr = ctx['reverse_transition_range']
    hyst_min = ctx['hysteresis_min']
    score_f = 0.0
    if forward_onset_idx is not None:
        pf = press[forward_onset_idx]
        if fr[0] <= pf <= fr[1]:
            score_f = 1.0
        else:
            dist = max(fr[0] - pf, pf - fr[1], 0)
            score_f = max(0.0, 1.0 - dist / 20.0)
    score_r = 0.0
    if reverse_onset_idx is not None:
        pr = press[reverse_onset_idx]
        if rr[0] <= pr <= rr[1]:
            score_r = 1.0
        else:
            dist = max(rr[0] - pr, pr - rr[1], 0)
            score_r = max(0.0, 1.0 - dist / 20.0)
    score_h = 0.0
    if forward_onset_idx is not None and reverse_onset_idx is not None:
        hyst = press[reverse_onset_idx] - press[forward_onset_idx]
        if hyst > hyst_min:
            score_h = 1.0
        elif hyst > 0:
            score_h = hyst / hyst_min
        else:
            score_h = 0.0
    return 0.4 * score_f + 0.4 * score_r + 0.2 * score_h


_SCORERS = {
    'mep_barrier_and_trend': score_0,
    'shear_nucleation': score_1,
    'hysteresis': score_2,
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
