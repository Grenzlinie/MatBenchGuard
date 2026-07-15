import os
import json
import csv

# === author imports / helpers ===
import csv, os, math, json


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
    return {'spec': spec}


# === block: score_0 (check id='eos') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold = step.get('gold', {})
        tol = step.get('tolerances', {})
        if not artifact or not isinstance(artifact, list):
            return 0.0
        # build dict from agent rows
        agent = {}
        for row in artifact:
            lattice = row.get('lattice','')
            if lattice:
                agent[lattice] = row
        # score each expected lattice
        total = 0
        count = 0
        for lat, gvals in gold.items():
            if lat not in agent:
                count += 1
                continue
            ag = agent[lat]
            ok = True
            try:
                v0 = float(ag.get('V0_ang3', math.nan))
                if abs(v0 - gvals['V0_ang3']) > tol.get('V0_ang3_abs', 1.0):
                    ok = False
                b0 = float(ag.get('B0_GPa', math.nan))
                if gvals['B0_GPa'] != 0:
                    if abs(b0 - gvals['B0_GPa']) / abs(gvals['B0_GPa']) > tol.get('B0_GPa_rel', 0.05):
                        ok = False
                bp = float(ag.get('B0_prime', math.nan))
                if abs(bp - gvals['B0_prime']) > tol.get('B0_prime_abs', 0.5):
                    ok = False
                vsp = float(ag.get('Vsp_ang3', math.nan))
                if abs(vsp - gvals['Vsp_ang3']) > tol.get('Vsp_ang3_abs', 1.0):
                    ok = False
                psp = float(ag.get('psp_GPa', math.nan))
                if abs(psp - gvals['psp_GPa']) > tol.get('psp_GPa_abs', 0.5):
                    ok = False
            except (ValueError, TypeError):
                ok = False
            if ok:
                total += 1
            count += 1
        if count == 0:
            return 0.0
        return total / count


# === block: score_1 (check id='elastic_sc') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        criteria = step.get('criteria', [])
        zero_tol = float(step.get('zero_pressure_tol', 0.1))
        if not artifact or not isinstance(artifact, list):
            return 0.0
        # find row with pressure closest to 0
        best = None
        best_dist = None
        for row in artifact:
            try:
                p = float(row.get('pressure_GPa', math.nan))
            except (ValueError, TypeError):
                continue
            dist = abs(p)
            if best is None or dist < best_dist:
                best = row
                best_dist = dist
        if best is None or best_dist > zero_tol:
            return 0.0
        # evaluate criteria
        passed = 0
        total = len(criteria)
        for crit in criteria:
            fname = crit['field']
            op = crit['op']
            gold_val = float(crit['value'])
            try:
                val = float(best.get(fname, math.nan))
            except (ValueError, TypeError):
                continue
            if op == '>':
                if val > gold_val:
                    passed += 1
            elif op == '<':
                if val < gold_val:
                    passed += 1
        if total == 0:
            return 1.0
        return passed / total


# === block: score_2 (check id='elastic_grae1') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold_pts = step.get('gold_points', [])
        comp_tol = float(step.get('component_tol', 10.0))
        press_tol = float(step.get('pressure_tol', 0.2))
        if not artifact or not isinstance(artifact, list):
            return 0.0
        # match each gold point to nearest volume
        matched = 0
        total = len(gold_pts)
        used = [False] * len(artifact)
        for gp in gold_pts:
            gp_vol = gp['volume_A3']
            # find closest row
            best_idx = -1
            best_dv = None
            for i, row in enumerate(artifact):
                if used[i]:
                    continue
                try:
                    v = float(row.get('volume_A3', math.nan))
                except (ValueError, TypeError):
                    continue
                dv = abs(v - gp_vol)
                if best_idx == -1 or dv < best_dv:
                    best_idx = i
                    best_dv = dv
            if best_idx == -1:
                continue
            row = artifact[best_idx]
            used[best_idx] = True
            ok = True
            for key in ['C11_GPa','C12_GPa','C33_GPa','C44_GPa','C13_GPa']:
                try:
                    val = float(row.get(key, math.nan))
                    gold_val = gp[key]
                except (ValueError, TypeError):
                    ok = False
                    break
                if abs(val - gold_val) > comp_tol:
                    ok = False
                    break
            # optionally check pressure
            try:
                p = float(row.get('pressure_GPa', math.nan))
            except (ValueError, TypeError):
                p = math.nan
            if not math.isnan(p) and not math.isnan(gp['pressure_GPa']):
                if abs(p - gp['pressure_GPa']) > press_tol:
                    ok = False
            if ok:
                matched += 1
        if total == 0:
            return 1.0
        return matched / total


# === block: score_3 (check id='critical_pts') ===
def score_3(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold_rows = step.get('gold_rows', [])
        pos_tol = float(step.get('pos_tol', 0.05))
        rho_rel_tol = float(step.get('rho_rel_tol', 0.10))
        lap_rel_tol = float(step.get('laplacian_rel_tol', 0.20))
        if not artifact or not isinstance(artifact, list):
            return 0.0
        # build list of agent rows
        agent_rows = []
        for row in artifact:
            try:
                x = float(row.get('x', math.nan))
                y = float(row.get('y', math.nan))
                z = float(row.get('z', math.nan))
                rho = float(row.get('rho_e_per_bohr3', math.nan))
                lap_str = row.get('laplacian_e_per_bohr5', None)
                if lap_str is None or lap_str == '' or str(lap_str).strip().upper() == 'NAN':
                    lap = None
                else:
                    lap = float(lap_str)
            except (ValueError, TypeError):
                continue
            agent_rows.append({
                'lattice': row.get('lattice',''),
                'cp_type': row.get('cp_type',''),
                'x': x, 'y': y, 'z': z,
                'rho': rho, 'lap': lap
            })
        matched = 0
        gold_used = [False] * len(gold_rows)
        agent_used = [False] * len(agent_rows)
        for gi, g in enumerate(gold_rows):
            glat = g['lattice']
            gtype = g['cp_type']
            gx, gy, gz = g['x'], g['y'], g['z']
            grho = g['rho_e_per_bohr3']
            glap = g.get('laplacian_e_per_bohr5')
            glap_is_nan = glap is None or (isinstance(glap, float) and math.isnan(glap))
            best_idx = -1
            best_dist = None
            for ai, arow in enumerate(agent_rows):
                if agent_used[ai]:
                    continue
                if arow['lattice'] != glat or arow['cp_type'] != gtype:
                    continue
                dist = math.sqrt((arow['x']-gx)**2 + (arow['y']-gy)**2 + (arow['z']-gz)**2)
                if dist > pos_tol:
                    continue
                if best_idx == -1 or dist < best_dist:
                    best_idx = ai
                    best_dist = dist
            if best_idx == -1:
                continue
            aw = agent_rows[best_idx]
            # check rho
            if grho != 0:
                if abs(aw['rho'] - grho) / abs(grho) > rho_rel_tol:
                    continue
            else:
                if aw['rho'] != 0:
                    continue
            # check laplacian
            if not glap_is_nan:
                if aw['lap'] is None:
                    continue
                if glap != 0:
                    if abs(aw['lap'] - glap) / abs(glap) > lap_rel_tol:
                        continue
            gold_used[gi] = True
            agent_used[best_idx] = True
            matched += 1
        if len(gold_rows) == 0:
            return 1.0
        return matched / len(gold_rows)


_SCORERS = {
    'eos': score_0,
    'elastic_sc': score_1,
    'elastic_grae1': score_2,
    'critical_pts': score_3,
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
