import os
import json
import csv

# === author imports / helpers ===
import math, csv
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
    def phi(u, v, J, K, Delta):
        eD = math.exp(Delta)
        eK = math.exp(K)
        eJ = math.exp(J)
        emJ = math.exp(-J)
        uz = u ** (z - 1)
        vz = v ** (z - 1)
        num = eD + eK * (eJ * uz + emJ * vz)
        denom = eD + uz + vz
        return num / denom

    def iterate(x0, y0, J, K, Delta, max_iter=5000, tol=1e-8):
        x, y = x0, y0
        hist_x, hist_y = [], []
        for i in range(max_iter):
            xn = phi(x, y, J, K, Delta)
            yn = phi(y, x, J, K, Delta)
            if i > 200 and abs(xn - x) < tol and abs(yn - y) < tol:
                return ('fixed', xn, yn)
            x, y = xn, yn
            if i >= max_iter - 50:
                hist_x.append(x)
                hist_y.append(y)
        if len(hist_x) < 4:
            return ('none', None, None)
        diffs = [abs(hist_x[-i] - hist_x[-i-2]) + abs(hist_y[-i] - hist_y[-i-2]) for i in range(1, min(20, len(hist_x)), 2) if i+1 < len(hist_x)]
        if diffs and max(diffs) < tol * 10:
            return ('cycle2', (hist_x[-2], hist_y[-2]), (hist_x[-1], hist_y[-1]))
        return ('none', None, None)

    def free_energy(x, y, Delta):
        eD = math.exp(Delta)
        xz = x ** z
        yz = y ** z
        xz1 = x ** (z - 1)
        yz1 = y ** (z - 1)
        term1 = 0.0
        if (xz + yz) > 1e-300:
            term1 = math.log(1.0 + math.exp(-Delta) * (xz + yz))
        term2 = 0.0
        if (xz1 + yz1) > 1e-300:
            term2 = (z / (2 - z)) * math.log(1.0 + math.exp(-Delta) * (xz1 + yz1))
        return -(term1 + term2)

    def order_params(x, y, Delta):
        eD = math.exp(Delta)
        xz = x ** z
        yz = y ** z
        denom = eD + xz + yz
        m = (xz - yz) / denom if denom != 0 else 0.0
        q = (xz + yz) / denom if denom != 0 else 0.0
        return m, q

    def classify_attractor(att, Delta):
        typ = att[0]
        if typ == 'fixed':
            x, y = att[1], att[2]
            m, q = order_params(x, y, Delta)
            if abs(x - y) < 1e-6:
                phase = 'd'
            else:
                phase = 'f'
            return phase, m, q, None, None
        elif typ == 'cycle2':
            (xA, yA), (xB, yB) = att[1], att[2]
            mA, qA = order_params(xA, yA, Delta)
            mB, qB = order_params(xB, yB, Delta)
            if abs(mA) < 1e-6 and abs(mB) < 1e-6:
                if abs(qA - qB) < 1e-6:
                    phase = 'd'
                else:
                    phase = 'a'
            else:
                if abs(mA - mB) < 5e-3:
                    phase = 'f'
                else:
                    phase = 'i'
            return phase, mA, qA, mB, qB
        else:
            return 'unknown', 0, 0, None, None

    z = 4
    KoverJs = [5, 3, -0.1, -0.8, -1, -2.5, -3, -3.5]
    T_min, T_max, nT = 0.01, 3.0, 100
    D_min, D_max, nD = -5.0, 5.0, 100
    T_vals = [T_min + (T_max - T_min) * i / (nT - 1) for i in range(nT)]
    D_vals = [D_min + (D_max - D_min) * i / (nD - 1) for i in range(nD)]

    points = []
    for KoverJ in KoverJs:
        for iT, T in enumerate(T_vals):
            for iD, D in enumerate(D_vals):
                if T < 1e-4:
                    continue
                J = 1.0 / (z * T)
                Delta = D / T
                K = KoverJ * J
                initial_guesses = [
                    (0.1, 0.1),
                    (1.0, 1.0),
                    (0.5, 2.0),
                    (2.0, 0.5),
                    (0.3, 0.8),
                    (1.5, 0.2)
                ]
                attractors = []
                seen = set()
                for x0, y0 in initial_guesses:
                    att = iterate(x0, y0, J, K, Delta)
                    if att[0] == 'none':
                        continue
                    if att[0] == 'fixed':
                        key = (round(att[1], 6), round(att[2], 6))
                    else:
                        key = (round(att[1][0],6), round(att[1][1],6), round(att[2][0],6), round(att[2][1],6))
                    if key not in seen:
                        seen.add(key)
                        attractors.append(att)
                if not attractors:
                    continue
                best_phase = None
                best_fe = float('inf')
                best_att = None
                for att in attractors:
                    if att[0] == 'fixed':
                        fe = free_energy(att[1], att[2], Delta)
                    elif att[0] == 'cycle2':
                        fe1 = free_energy(att[1][0], att[1][1], Delta)
                        fe2 = free_energy(att[2][0], att[2][1], Delta)
                        fe = (fe1 + fe2) / 2.0
                    else:
                        continue
                    if fe < best_fe:
                        best_fe = fe
                        best_att = att
                if best_att:
                    ph, _, _, _, _ = classify_attractor(best_att, Delta)
                    points.append((KoverJ, T, D, ph))

    phase_grid = {KoverJ: {(iT,iD): None for iT in range(nT) for iD in range(nD)} for KoverJ in KoverJs}
    for rec in points:
        k, T, D, ph = rec
        iT = int(round((T - T_min) / (T_max - T_min) * (nT - 1)))
        iD = int(round((D - D_min) / (D_max - D_min) * (nD - 1)))
        if 0 <= iT < nT and 0 <= iD < nD:
            phase_grid[k][(iT,iD)] = ph

    transitions = []
    for KoverJ in KoverJs:
        for iT in range(nT - 1):
            for iD in range(nD - 1):
                for (diT, diD) in [(1,0), (0,1)]:
                    iT2 = iT + diT
                    iD2 = iD + diD
                    p1 = phase_grid[KoverJ].get((iT,iD))
                    p2 = phase_grid[KoverJ].get((iT2,iD2))
                    if p1 is None or p2 is None or p1 == p2:
                        continue
                    T_mid = (T_vals[iT] + T_vals[iT2]) / 2.0
                    D_mid = (D_vals[iD] + D_vals[iD2]) / 2.0
                    if p1 == 'd' and p2 == 'f':
                        trans_type = 'second_order'
                    else:
                        trans_type = 'first_order'
                    transitions.append({
                        'K_over_J': KoverJ,
                        'delta_over_zJ': D_mid,
                        'temperature_over_zJ': T_mid,
                        'transition_type': trans_type,
                        'phase_from': p1,
                        'phase_to': p2
                    })
    ctx = {'gold': transitions}


# === block: score_0 (check id='step_01_phase_boundaries') ===
def score_0(artifact, step, ctx):
    gold = ctx['gold']
    if not artifact or not isinstance(artifact, list):
        return 0.0
    agent_points = []
    for row in artifact:
        try:
            K = float(row['K_over_J'])
            delta = float(row['delta_over_zJ'])
            T = float(row['temperature_over_zJ'])
            p_from = row['phase_from'].strip()
            p_to = row['phase_to'].strip()
            agent_points.append({
                'K': K, 'delta': delta, 'T': T,
                'phases': frozenset([p_from, p_to])
            })
        except (KeyError, ValueError):
            continue
    if not agent_points:
        return 0.0
    delta_tol = 0.2
    T_tol = 0.05
    matched_count = 0
    total_gold = len(gold)
    if total_gold == 0:
        return 1.0
    for g in gold:
        gK = g['K_over_J']
        gdelta = g['delta_over_zJ']
        gT = g['temperature_over_zJ']
        gphases = frozenset([g['phase_from'], g['phase_to']])
        matched = False
        for ap in agent_points:
            if ap['K'] == gK and ap['phases'] == gphases:
                if abs(ap['delta'] - gdelta) <= delta_tol and abs(ap['T'] - gT) <= T_tol:
                    matched = True
                    break
        if matched:
            matched_count += 1
    return matched_count / total_gold


_SCORERS = {
    'step_01_phase_boundaries': score_0,
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
