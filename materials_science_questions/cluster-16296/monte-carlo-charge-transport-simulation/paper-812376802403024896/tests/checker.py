import os
import json
import csv

# === author imports / helpers ===
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
        path_2ps = os.path.join(outputs_dir, 'lo_phonon_spectrum_2ps.csv')
        ctx_data = {}
        if os.path.exists(path_2ps):
            with open(path_2ps, newline='') as f:
                reader = csv.DictReader(f)
                rows_2ps = list(reader)
            valleys = ['N_Gamma', 'N_L', 'N_X6', 'N_X7']
            peaks = {}
            max_vals = {}
            for v in valleys:
                q_vals = [float(r['q_inv_nm']) for r in rows_2ps]
                n_vals = [float(r[v]) for r in rows_2ps]
                if not n_vals:
                    continue
                idx_max = max(range(len(n_vals)), key=lambda i: n_vals[i])
                peaks[v] = q_vals[idx_max]
                max_vals[v] = n_vals[idx_max]
            q_vals_list = list(peaks.values())
            if q_vals_list:
                q_range_2ps = max(q_vals_list) - min(q_vals_list)
                max_peak = max(max_vals.values())
                min_peak = min(max_vals.values())
                ratio_2ps = max_peak / min_peak if min_peak > 0 else float('inf')
            else:
                q_range_2ps = None
                ratio_2ps = None
            ctx_data['q_range_2ps'] = q_range_2ps
            ctx_data['ratio_2ps'] = ratio_2ps
        return ctx_data


# === block: score_0 (check id='step_03_valley_populations') ===
def score_0(artifact, step, ctx):
        hot_rows = [r for r in artifact if r.get('hot_phonons','').strip().lower() in ('true','1')]
        nohot_rows = [r for r in artifact if r.get('hot_phonons','').strip().lower() in ('false','0')]
        if not hot_rows or not nohot_rows:
            return 0.0
        def mean_X6(rows, tmin=4.0, tmax=5.0):
            vals = []
            for r in rows:
                t = float(r.get('time_ps',0))
                if tmin <= t <= tmax:
                    vals.append(float(r.get('N_X6',0)))
            if not vals:
                return 0.0
            return sum(vals)/len(vals)
        mean_hot = mean_X6(hot_rows)
        mean_nohot = mean_X6(nohot_rows)
        if mean_hot >= mean_nohot - 1e-4:
            return 1.0
        else:
            return 0.0


# === block: score_1 (check id='step_04_lo_phonon_2ps') ===
def score_1(artifact, step, ctx):
        valleys = ['N_Gamma', 'N_L', 'N_X6', 'N_X7']
        q_vals = [float(r['q_inv_nm']) for r in artifact]
        if not q_vals:
            return 0.0
        peaks = {}
        max_vals = {}
        for v in valleys:
            n_vals = [float(r[v]) for r in artifact]
            if not n_vals:
                continue
            idx = max(range(len(n_vals)), key=lambda i: n_vals[i])
            peaks[v] = q_vals[idx]
            max_vals[v] = n_vals[idx]
        order = ['N_Gamma', 'N_L', 'N_X7', 'N_X6']
        order_ok = True
        for i in range(len(order)-1):
            if order[i] not in peaks or order[i+1] not in peaks:
                order_ok = False
                break
            if peaks[order[i]] >= peaks[order[i+1]]:
                order_ok = False
                break
        x7_ok = False
        if 'N_X7' in max_vals:
            max_list = [(v, max_vals[v]) for v in valleys if v in max_vals]
            sorted_vals = sorted(max_list, key=lambda x: x[1])
            if sorted_vals[0][0] == 'N_X7':
                if len(sorted_vals) >= 2:
                    if max_vals['N_X7'] < 0.5 * sorted_vals[1][1]:
                        x7_ok = True
                else:
                    x7_ok = True
            else:
                x7_ok = False
        else:
            x7_ok = False
        score = 0.0
        if order_ok:
            score += 0.5
        if x7_ok:
            score += 0.5
        return score


# === block: score_2 (check id='step_05_lo_phonon_2_5ps') ===
def score_2(artifact, step, ctx):
        valleys = ['N_Gamma', 'N_L', 'N_X6', 'N_X7']
        q_vals = [float(r['q_inv_nm']) for r in artifact]
        if not q_vals:
            return 0.0
        peaks = {}
        max_vals = {}
        for v in valleys:
            n_vals = [float(r[v]) for r in artifact]
            if not n_vals:
                continue
            idx = max(range(len(n_vals)), key=lambda i: n_vals[i])
            peaks[v] = q_vals[idx]
            max_vals[v] = n_vals[idx]
        if peaks:
            q_range_25 = max(peaks.values()) - min(peaks.values())
        else:
            q_range_25 = None
        if max_vals:
            max_peak = max(max_vals.values())
            min_peak = min(max_vals.values())
            ratio_25 = max_peak / min_peak if min_peak > 0 else float('inf')
        else:
            ratio_25 = None
        q_range_2ps = ctx.get('q_range_2ps')
        ratio_2ps = ctx.get('ratio_2ps')
        if q_range_2ps is None or ratio_2ps is None:
            return 0.0
        score = 0.0
        if q_range_25 is not None and q_range_25 < q_range_2ps - 1e-6:
            score += 0.5
        if ratio_25 is not None and ratio_2ps is not None and ratio_25 < ratio_2ps - 1e-6:
            score += 0.5
        return min(score, 1.0)


_SCORERS = {
    'step_03_valley_populations': score_0,
    'step_04_lo_phonon_2ps': score_1,
    'step_05_lo_phonon_2_5ps': score_2,
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
