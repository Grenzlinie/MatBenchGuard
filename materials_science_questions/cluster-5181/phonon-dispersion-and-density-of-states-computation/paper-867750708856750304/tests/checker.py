import os
import json
import csv

# === author imports / helpers ===
import csv, json, math, os


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
    def _parse_targets(step):
        return step.get('targets', {})  # whole dict

    def _parse_tolerances(step):
        return step.get('tolerances', step.get('tolerance_abs', 0.0))

    def prepare(outputs_dir, spec):
        ctx = {}
        for step in spec.get('steps', []):
            sid = step['id']
            ctx[sid] = {
                'targets': _parse_targets(step),
                'tolerances': _parse_tolerances(step),
                'kind': step.get('kind', 'numeric'),
            }
            if sid == 'step_03':
                ctx[sid]['search_label_prefix'] = step.get('search_label_prefix', 'Γ→')
                ctx[sid]['q_index'] = step.get('q_index', 0)
                ctx[sid]['targets'] = step.get('targets', {})
                ctx[sid]['tolerance_meV'] = step.get('tolerance_meV', 5.0)
            if sid == 'step_03_dos':
                ctx[sid]['mode_energies'] = step.get('targets', {}).get('mode_energies_meV', [])
                ctx[sid]['tolerance_peak_meV'] = step.get('tolerance_peak_meV', 5.0)
        return ctx


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    if not artifact or len(artifact) == 0:
        return 0.0
    row = artifact[0]
    ctx_step = ctx.get('step_01', {})
    targets = ctx_step.get('targets', {})
    tolerances = ctx_step.get('tolerances', {})
    keys = [('a(Å)', 'a'), ('c(Å)', 'c'), ('z', 'z')]
    scores = []
    for col, name in keys:
        try:
            val = float(row.get(col, None))
        except (TypeError, ValueError):
            scores.append(0.0)
            continue
        target = targets.get(name)
        tol = tolerances.get(name, 0.0)
        if target is None or tol <= 0.0:
            scores.append(1.0)
            continue
        diff = abs(val - target)
        if diff <= tol:
            scores.append(1.0)
        else:
            # linear decay to 0 at 2*tol
            score = max(0.0, 1.0 - (diff - tol) / tol)
            scores.append(score)
    return sum(scores) / len(scores)


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    if not artifact or len(artifact) == 0:
        return 0.0
    row = artifact[0]
    ctx_step = ctx.get('step_02', {})
    targets = ctx_step.get('targets', {})
    tol = ctx_step.get('tolerances', 20.0) if isinstance(ctx_step.get('tolerances'), (int, float)) else 20.0
    keys = [('c11(GPa)', 'c11'), ('c12', 'c12'), ('c13', 'c13'), ('c33', 'c33'), ('c44', 'c44')]
    scores = []
    for col, name in keys:
        try:
            val = float(row.get(col, None))
        except (TypeError, ValueError):
            scores.append(0.0)
            continue
        target = targets.get(name)
        if target is None or tol <= 0.0:
            scores.append(1.0)
            continue
        diff = abs(val - target)
        if diff <= tol:
            scores.append(1.0)
        else:
            score = max(0.0, 1.0 - (diff - tol) / tol)
            scores.append(score)
    return sum(scores) / len(scores)


# === block: score_2 (check id='step_03') ===
def score_2(artifact, step, ctx):
    if not artifact or len(artifact) == 0:
        return 0.0
    ctx_step = ctx.get('step_03', {})
    targets = ctx_step.get('targets', {})
    gamma_meV = targets.get('gamma_freq_meV')
    if not gamma_meV or len(gamma_meV) == 0:
        return 0.0
    tol_meV = ctx_step.get('tolerance_meV', 5.0)
    tol_cm1 = tol_meV * 8.065544
    prefix = ctx_step.get('search_label_prefix', 'Γ→')
    q_idx_target = ctx_step.get('q_index', 0)
    # Extract rows at the start of the first segment
    matching_rows = []
    for row in artifact:
        label = row.get('q_path_label', '')
        try:
            q_idx = int(row.get('q_index', -1))
        except (TypeError, ValueError):
            continue
        if label.startswith(prefix) and q_idx == q_idx_target:
            try:
                freq = float(row.get('frequency_cm-1', None))
            except (TypeError, ValueError):
                continue
            matching_rows.append(freq)
    if len(matching_rows) != len(gamma_meV):
        return 0.0
    total_err = 0.0
    for i, f_cm1 in enumerate(matching_rows):
        expected_cm1 = gamma_meV[i] * 8.065544
        total_err += abs(f_cm1 - expected_cm1)
    avg_err = total_err / len(gamma_meV)
    if avg_err <= tol_cm1:
        return 1.0
    return max(0.0, 1.0 - (avg_err - tol_cm1) / tol_cm1)


# === block: score_3 (check id='step_03_dos') ===
def score_3(artifact, step, ctx):
    if not artifact or len(artifact) == 0:
        return 0.0
    ctx_step = ctx.get('step_03_dos', {})
    mode_energies = ctx_step.get('mode_energies', [])
    tol_meV = ctx_step.get('tolerance_peak_meV', 5.0)
    if not mode_energies:
        return 0.0
    energies = []
    dos = []
    for row in artifact:
        try:
            e = float(row.get('energy_meV', None))
            d = float(row.get('dos_arb_units', None))
        except (TypeError, ValueError):
            continue
        energies.append(e)
        dos.append(d)
    if len(energies) < 2:
        return 0.0
    found = 0
    for target_e in mode_energies:
        low = target_e - tol_meV
        high = target_e + tol_meV
        max_dos = -1.0
        for e, d in zip(energies, dos):
            if low <= e <= high and d > max_dos:
                max_dos = d
        if max_dos > 0.01:  # any non-negligible peak
            found += 1
    return found / len(mode_energies)


# === block: score_4 (check id='step_04') ===
def score_4(artifact, step, ctx):
    if not artifact or len(artifact) < 2:
        return 0.0
    ctx_step = ctx.get('step_04', {})
    targets = ctx_step.get('targets', {})
    tols = ctx_step.get('tolerances', {})
    a0_target = targets.get('a0', 2.905)
    c0_target = targets.get('c0', 7.483)
    alpha_target = targets.get('alpha', 6.5e-6)
    tol_a0 = tols.get('a0', 0.01)
    tol_c0 = tols.get('c0', 0.01)
    tol_alpha = tols.get('alpha_abs', 1e-6)
    # parse rows
    T_list = []
    a_list = []
    c_list = []
    for row in artifact:
        try:
            T = float(row.get('T_K', None))
            a = float(row.get('a_AA', None))
            c = float(row.get('c_AA', None))
        except (TypeError, ValueError):
            continue
        T_list.append(T)
        a_list.append(a)
        c_list.append(c)
    if len(T_list) < 2:
        return 0.0
    # extract 0 K and 1000 K
    zipped = list(zip(T_list, a_list, c_list))
    zipped.sort(key=lambda x: x[0])
    # find closest to 0 and 1000
    def find_closest(zipped, target_T):
        best = None
        best_dist = float('inf')
        for T, a, c in zipped:
            dist = abs(T - target_T)
            if dist < best_dist:
                best_dist = dist
                best = (T, a, c)
        return best

    row0 = find_closest(zipped, 0.0)
    row1000 = find_closest(zipped, 1000.0)
    if row0 is None or row1000 is None:
        return 0.0
    T0, a0, c0 = row0
    T1000, a1000, c1000 = row1000
    if T1000 - T0 <= 0:
        return 0.0
    # a0/c0 check
    def val_score(val, target, tol):
        diff = abs(val - target)
        if diff <= tol:
            return 1.0
        return max(0.0, 1.0 - (diff - tol) / tol)
    score_a0 = val_score(a0, a0_target, tol_a0)
    score_c0 = val_score(c0, c0_target, tol_c0)
    # alpha check
    alpha_a = (a1000 - a0) / (a0 * (T1000 - T0))
    alpha_c = (c1000 - c0) / (c0 * (T1000 - T0))
    alpha_avg = (alpha_a + alpha_c) / 2.0
    diff_alpha = abs(alpha_avg - alpha_target)
    if diff_alpha <= tol_alpha:
        score_alpha = 1.0
    else:
        score_alpha = max(0.0, 1.0 - (diff_alpha - tol_alpha) / tol_alpha)
    # monotonic: a and c must be non-decreasing
    mono_ok = 1.0
    for i in range(1, len(a_list)):
        if a_list[i] < a_list[i-1] - 1e-12:
            mono_ok = 0.0
            break
    if mono_ok:
        for i in range(1, len(c_list)):
            if c_list[i] < c_list[i-1] - 1e-12:
                mono_ok = 0.0
                break
    # combine (0.2 a0/c0, 0.6 alpha, 0.2 monotonic)
    final = 0.2 * (score_a0 + score_c0) / 2.0 + 0.6 * score_alpha + 0.2 * mono_ok
    return min(1.0, max(0.0, final))


_SCORERS = {
    'step_01': score_0,
    'step_02': score_1,
    'step_03': score_2,
    'step_03_dos': score_3,
    'step_04': score_4,
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
