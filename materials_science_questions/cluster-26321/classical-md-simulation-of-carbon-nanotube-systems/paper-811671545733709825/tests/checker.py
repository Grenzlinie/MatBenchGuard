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
        # Extract hidden gold from step parameters
        ctx = {}
        for step in spec.get("steps", []):
            sid = step["id"]
            params = step.get("parameters", {})
            ctx[sid] = params
        return ctx


# === block: score_0 (check id='check_mw_curves') ===
def score_0(artifact, step, ctx):
        from collections import defaultdict
        params = ctx.get('check_mw_curves', {})
        monotonic_tol = params.get('monotonic_tolerance_relative_change', 0.01)
        plateau_rel_thresh = params.get('plateau_relative_change_threshold', 0.05)
        plateau_frac = params.get('plateau_fraction', 0.2)
        data = defaultdict(list)
        for row in artifact:
            system = row['system'].strip()
            temp = int(row['temperature_K'])
            time_ns = float(row['time_ns'])
            mw = float(row['Mw_g_per_mol'])
            data[(system, temp)].append((time_ns, mw))
        total_traj = len(data)
        if total_traj == 0:
            return 0.0
        monotonic_score = 0.0
        plateau_score = 0.0
        ordering_score = 0.0
        temps = set()
        for (sys, temp), points in data.items():
            temps.add(temp)
            points_sorted = sorted(points, key=lambda x: x[0])
            mws = [p[1] for p in points_sorted]
            times = [p[0] for p in points_sorted]
            # monotonic: no decrease beyond relative tolerance
            monotonic = True
            for i in range(1, len(mws)):
                if mws[i] < mws[i-1] - monotonic_tol * mws[i-1]:
                    monotonic = False
                    break
            monotonic_score += 1.0 if monotonic else 0.0
            # plateau for tube systems only
            if sys in ('10_10', '7_7'):
                last_idx = max(0, int((1 - plateau_frac) * len(mws)))
                if last_idx < len(mws) - 1:
                    mw_start = mws[last_idx]
                    mw_end = mws[-1]
                    if mw_start > 0:
                        rel_change = abs(mw_end - mw_start) / mw_start
                        if rel_change <= plateau_rel_thresh:
                            plateau_score += 1.0
                        else:
                            plateau_score += 0.0
                    else:
                        plateau_score += 0.0
                else:
                    plateau_score += 1.0  # too few points, assume plateau
        mono_avg = monotonic_score / total_traj if total_traj > 0 else 0.0
        tube_trajs = sum(1 for (s,_) in data if s in ('10_10','7_7'))
        plat_avg = plateau_score / tube_trajs if tube_trajs > 0 else 1.0
        # ordering at each temperature: bulk > 10_10 > 7_7 using final Mw
        ord_pass = 0
        for temp in temps:
            final_mws = {}
            for sys in ('bulk', '10_10', '7_7'):
                key = (sys, temp)
                if key in data:
                    pts = sorted(data[key], key=lambda x: x[0])
                    final_mws[sys] = pts[-1][1]
            if 'bulk' in final_mws and '10_10' in final_mws and '7_7' in final_mws:
                if final_mws['bulk'] > final_mws['10_10'] * 0.99 and final_mws['10_10'] > final_mws['7_7'] * 0.99:
                    ord_pass += 1.0
                elif final_mws['bulk'] > final_mws['10_10'] * 0.99 or final_mws['10_10'] > final_mws['7_7'] * 0.99:
                    ord_pass += 0.5
        ord_avg = ord_pass / len(temps) if len(temps) > 0 else 0.0
        final_score = 0.4 * mono_avg + 0.3 * plat_avg + 0.3 * ord_avg
        return min(1.0, max(0.0, final_score))


# === block: score_1 (check id='check_rate_constants') ===
def score_1(artifact, step, ctx):
        from collections import defaultdict
        params = ctx.get('check_rate_constants', {})
        windows = params.get('ratio_windows', {})
        rates = defaultdict(dict)
        for row in artifact:
            sys = row['system'].strip()
            temp = int(row['temperature_K'])
            rate = float(row['rate_constant_s_per_mol'])
            rates[temp][sys] = rate
        total_checks = 0
        passed = 0
        for temp, sys_rates in rates.items():
            if not {'bulk','10_10','7_7'}.issubset(sys_rates):
                continue
            bulk = sys_rates['bulk']
            t10 = sys_rates['10_10']
            t7 = sys_rates['7_7']
            # ordering bonus
            if bulk > t10 * 0.99 and t10 > t7 * 0.99:
                passed += 0.3
            elif bulk > t10 * 0.99 or t10 > t7 * 0.99:
                passed += 0.1
            total_checks += 0.3
            # ratio window for 10_10
            if t10 > 0:
                r_b10 = bulk / t10
                low, high = windows.get('bulk_10_10', [9,27])
                if low <= r_b10 <= high:
                    passed += 0.35
                else:
                    dist = min(abs(r_b10-low), abs(r_b10-high))
                    passed += max(0, 0.35 - 0.35 * dist / 10.0)
            total_checks += 0.35
            # ratio window for 7_7
            if t7 > 0:
                r_b7 = bulk / t7
                low, high = windows.get('bulk_7_7', [25,75])
                if low <= r_b7 <= high:
                    passed += 0.35
                else:
                    dist = min(abs(r_b7-low), abs(r_b7-high))
                    passed += max(0, 0.35 - 0.35 * dist / 25.0)
            total_checks += 0.35
        score = passed / total_checks if total_checks > 0 else 0.0
        return min(1.0, max(0.0, score))


# === block: score_2 (check id='check_activation_energies') ===
def score_2(artifact, step, ctx):
        params = ctx.get('check_activation_energies', {})
        ranges = params.get('acceptable_ranges', {})
        bandwidth = params.get('out_of_range_decay_bandwidth', 20.0)
        eads = {}
        for row in artifact:
            sys = row['system'].strip()
            ea = float(row['activation_energy_kcal_per_mol'])
            eads[sys] = ea
        total_sys = 0
        cum_score = 0.0
        for sys, (low, high) in ranges.items():
            ea = eads.get(sys, None)
            if ea is None:
                continue
            total_sys += 1
            if low <= ea <= high:
                cum_score += 1.0
            else:
                dist = 0
                if ea < low:
                    dist = low - ea
                elif ea > high:
                    dist = ea - high
                cum_score += max(0.0, 1.0 - dist / bandwidth)
        score = cum_score / total_sys if total_sys > 0 else 0.0
        return min(1.0, max(0.0, score))


_SCORERS = {
    'check_mw_curves': score_0,
    'check_rate_constants': score_1,
    'check_activation_energies': score_2,
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
