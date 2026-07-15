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
    return {}  # no shared state


# === block: score_0 (check id='step_cooling') ===
def score_0(artifact, step, ctx):
    import math

    def score(artifact, step, ctx):
        gold = step.get('gold', [])
        tol = step.get('tolerance', 10.0)
        if not gold:
            return 1.0
        agent = {}
        for row in artifact:
            try:
                t = float(row['time'])
                ts = float(row['temperature_surface'])
                tc = float(row['temperature_center'])
                agent[t] = (ts, tc)
            except (KeyError, ValueError):
                continue
        if not agent:
            return 0.0
        agent_times = sorted(agent.keys())
        def get_agent(tgt):
            # find closest
            idx = min(range(len(agent_times)), key=lambda i: abs(agent_times[i]-tgt))
            return agent[agent_times[idx]]
        ok = 0
        for g in gold:
            try:
                tgt_time = float(g['time'])
                ref_surf = float(g['temperature_surface'])
                ref_cent = float(g['temperature_center'])
            except (KeyError, ValueError):
                continue
            agt_surf, agt_cent = get_agent(tgt_time)
            if abs(agt_surf - ref_surf) <= tol and abs(agt_cent - ref_cent) <= tol:
                ok += 1
        return ok / len(gold) if gold else 1.0


# === block: score_1 (check id='step_phase_fractions') ===
def score_1(artifact, step, ctx):
    import math

    def score(artifact, step, ctx):
        gold = step.get('gold', [])
        tol = step.get('tolerance', 0.05)
        sum_tol = step.get('sum_tolerance', 0.02)
        if not gold:
            return 1.0
        # index agent by (radius, time) using closest match
        agent_points = []
        for row in artifact:
            try:
                r = float(row['radius'])
                t = float(row['time'])
                fr = float(row['ferrite'])
                pe = float(row['pearlite'])
                ba = float(row['bainite'])
                ma = float(row['martensite'])
                agent_points.append((r, t, fr, pe, ba, ma))
            except (KeyError, ValueError):
                continue
        if not agent_points:
            return 0.0
        # helper to find closest agent point by (radius, time) distance in L2
        def get_closest(r_tgt, t_tgt):
            best = None
            best_dist = float('inf')
            for (rr, tt, fr, pe, ba, ma) in agent_points:
                dist = (rr - r_tgt)**2 + (tt - t_tgt)**2
                if dist < best_dist:
                    best_dist = dist
                    best = (fr, pe, ba, ma)
            return best
        ok = 0
        for g in gold:
            try:
                r_tgt = float(g['radius'])
                t_tgt = float(g['time'])
                ref_fr = float(g['ferrite'])
                ref_pe = float(g['pearlite'])
                ref_ba = float(g['bainite'])
                ref_ma = float(g['martensite'])
            except (KeyError, ValueError):
                continue
            agt = get_closest(r_tgt, t_tgt)
            if agt is None:
                continue
            afr, ape, aba, ama = agt
            if (abs(afr - ref_fr) <= tol and abs(ape - ref_pe) <= tol and
                abs(aba - ref_ba) <= tol and abs(ama - ref_ma) <= tol):
                ok += 1
        # sum check on all agent rows
        sum_violations = 0
        for (r, t, fr, pe, ba, ma) in agent_points:
            s = fr + pe + ba + ma
            if s > 1.0 + sum_tol:
                sum_violations += 1
        # combine: 90% weight on point match, 10% on sum compliance
        point_score = ok / len(gold) if gold else 1.0
        sum_score = max(0.0, 1.0 - sum_violations / max(1, len(agent_points)))
        return 0.9 * point_score + 0.1 * sum_score


# === block: score_2 (check id='step_hardness') ===
def score_2(artifact, step, ctx):
    import math

    def score(artifact, step, ctx):
        gold = step.get('gold', [])
        tol = step.get('tolerance', 20.0)
        if not gold:
            return 1.0
        agent = {}
        for row in artifact:
            try:
                r = float(row['radius'])
                hv = float(row['Vickers hardness'])
                agent[r] = hv
            except (KeyError, ValueError):
                continue
        if not agent:
            return 0.0
        radii = sorted(agent.keys())
        if not radii:
            return 0.0
        def get_agent(r_tgt):
            idx = min(range(len(radii)), key=lambda i: abs(radii[i]-r_tgt))
            return agent[radii[idx]]
        ok = 0
        for g in gold:
            try:
                r = float(g['radius'])
                ref_hv = float(g['Vickers hardness'])
            except (KeyError, ValueError):
                continue
            agt_hv = get_agent(r)
            if abs(agt_hv - ref_hv) <= tol:
                ok += 1
        return ok / len(gold) if gold else 1.0


# === block: score_3 (check id='step_von_mises') ===
def score_3(artifact, step, ctx):
    import math

    def score(artifact, step, ctx):
        gold = step.get('gold', [])
        tol = step.get('tolerance', 50.0)
        if not gold:
            return 1.0
        agent = {}
        for row in artifact:
            try:
                r = float(row['radius'])
                vm = float(row['von_Mises_stress'])
                agent[r] = vm
            except (KeyError, ValueError):
                continue
        if not agent:
            return 0.0
        radii = sorted(agent.keys())
        if not radii:
            return 0.0
        def get_agent(r_tgt):
            idx = min(range(len(radii)), key=lambda i: abs(radii[i]-r_tgt))
            return agent[radii[idx]]
        ok = 0
        for g in gold:
            try:
                r = float(g['radius'])
                ref_vm = float(g['von_Mises_stress'])
            except (KeyError, ValueError):
                continue
            agt_vm = get_agent(r)
            if abs(agt_vm - ref_vm) <= tol:
                ok += 1
        return ok / len(gold) if gold else 1.0


# === block: score_4 (check id='step_volume') ===
def score_4(artifact, step, ctx):
    import math

    def score(artifact, step, ctx):
        gold = step.get('gold', [])
        tol = step.get('tolerance', 200.0)
        if not gold:
            return 1.0
        agent = {}
        for row in artifact:
            try:
                t = float(row['time'])
                vol = float(row['volume'])
                agent[t] = vol
            except (KeyError, ValueError):
                continue
        if not agent:
            return 0.0
        times = sorted(agent.keys())
        if not times:
            return 0.0
        def get_agent(t_tgt):
            idx = min(range(len(times)), key=lambda i: abs(times[i]-t_tgt))
            return agent[times[idx]]
        ok = 0
        for g in gold:
            try:
                t = float(g['time'])
                ref_vol = float(g['volume'])
            except (KeyError, ValueError):
                continue
            agt_vol = get_agent(t)
            if abs(agt_vol - ref_vol) <= tol:
                ok += 1
        return ok / len(gold) if gold else 1.0


# === block: score_5 (check id='step_dimensional') ===
def score_5(artifact, step, ctx):
    import math

    def score(artifact, step, ctx):
        gold = step.get('gold', [])
        tol = step.get('tolerance', 0.05)
        if not artifact or not gold:
            return 1.0
        # agent rows
        agent_map = {}
        for row in artifact:
            dim = row.get('dimension', '').strip().lower()
            try:
                change = float(row['change_mm'])
                agent_map[dim] = change
            except (KeyError, ValueError):
                continue
        ok = 0
        total = 0
        for g in gold:
            try:
                dim = str(g['dimension']).strip().lower()
                ref_change = float(g['change_mm'])
            except (KeyError, ValueError):
                continue
            total += 1
            agt_change = agent_map.get(dim)
            if agt_change is not None and abs(agt_change - ref_change) <= tol:
                ok += 1
        return ok / total if total > 0 else 1.0


_SCORERS = {
    'step_cooling': score_0,
    'step_phase_fractions': score_1,
    'step_hardness': score_2,
    'step_von_mises': score_3,
    'step_volume': score_4,
    'step_dimensional': score_5,
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
