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
    import csv, os
    def prepare(outputs_dir, spec):
        curves_path = os.path.join(outputs_dir, 'step_02_magnetization_curves.csv')
        hysteresis_path = os.path.join(outputs_dir, 'step_03_hysteresis_summary.csv')
        curves = []
        if os.path.exists(curves_path):
            with open(curves_path, newline='') as f:
                curves = list(csv.DictReader(f))
        hysteresis = []
        if os.path.exists(hysteresis_path):
            with open(hysteresis_path, newline='') as f:
                hysteresis = list(csv.DictReader(f))
        return {'curves': curves, 'hysteresis': hysteresis}


# === block: score_0 (check id='exchange') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    required = ['separation_angstrom','substrate','ordering','E_ex_meV']
    if not all(col in rows[0] for col in required):
        return 0.0
    subs = set()
    cu_seps = {}
    pt_seps = {}
    for r in rows:
        sep_str = r.get('separation_angstrom')
        sub = r.get('substrate')
        e_str = r.get('E_ex_meV')
        if sep_str is None or sub is None or e_str is None:
            continue
        try:
            sep = float(sep_str)
            e = float(e_str)
        except (ValueError, TypeError):
            continue
        subs.add(sub)
        if sub == 'Cu':
            cu_seps.setdefault(sep, []).append(e)
        elif sub == 'Pt':
            pt_seps.setdefault(sep, []).append(e)
    if 'Cu' not in subs or 'Pt' not in subs:
        return 0.0
    score_val = 0.0
    if len(cu_seps) >= 5:
        score_val += 0.25
    if len(pt_seps) >= 5:
        score_val += 0.25
    cu_neg = any(any(v < 0 for v in vals) for sep, vals in cu_seps.items() if 5 <= sep <= 7)
    if cu_neg:
        score_val += 0.25
    consistent = True
    for sep, vals in cu_seps.items():
        if max(vals) - min(vals) > 1e-6:
            consistent = False
            break
    if consistent:
        for sep, vals in pt_seps.items():
            if max(vals) - min(vals) > 1e-6:
                consistent = False
                break
    if consistent:
        score_val += 0.25
    return min(score_val, 1.0)


# === block: score_1 (check id='anisotropy') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        rows = artifact
        if not rows:
            return 0.0
        required = ['separation_angstrom','substrate','ordering','E_MA_meV']
        if not all(col in rows[0] for col in required):
            return 0.0
        # Separate FM/AFM per substrate
        cu_fm = [float(r['E_MA_meV']) for r in rows if r['substrate']=='Cu' and r['ordering']=='FM']
        cu_afm = [float(r['E_MA_meV']) for r in rows if r['substrate']=='Cu' and r['ordering']=='AFM']
        pt = [float(r['E_MA_meV']) for r in rows if r['substrate']=='Pt']
        score = 0.0
        # Cu FM: at least one value above 1.5 meV
        if cu_fm and max(cu_fm) > 1.5:
            score += 0.2
        # Cu FM: most values between 0.1 and 1.0
        if cu_fm:
            in_range = sum(0.1 <= v <= 1.0 for v in cu_fm)
            if in_range >= len(cu_fm)*0.7:
                score += 0.2
        # Cu AFM variation less than FM
        if cu_fm and cu_afm:
            import statistics
            if statistics.stdev(cu_afm) < statistics.stdev(cu_fm):
                score += 0.2
        # Pt has sign changes (both positive and negative)
        if pt:
            pos = any(v > 0 for v in pt)
            neg = any(v < 0 for v in pt)
            if pos and neg:
                score += 0.2
            if max(pt) > 2.0:
                score += 0.2
        return min(score, 1.0)


# === block: score_2 (check id='magnetization_curves') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        rows = artifact
        gold_pairs = step.get('gold_pairs', [])
        if not rows or not gold_pairs:
            return 0.0
        # Group by substrate, separation
        from collections import defaultdict
        groups = defaultdict(list)
        for r in rows:
            key = (r['substrate'], float(r['separation_angstrom']))
            groups[key].append(r)
        def compute_hysteresis(rows_list):
            rows_list.sort(key=lambda r: float(r['field_T']))   # not ideal, use order
            fields = [float(r['field_T']) for r in rows_list]
            mags = [float(r['magnetization_norm']) for r in rows_list]
            n = len(fields)
            if n < 4:
                return None, None
            max_idx = fields.index(max(fields))
            asc_f = fields[:max_idx+1]
            asc_m = mags[:max_idx+1]
            desc_f = fields[max_idx+1:]
            desc_m = mags[max_idx+1:]
            def crossing(f, m):
                for i in range(len(f)-1):
                    if (m[i] <= 0 and m[i+1] >= 0) or (m[i] >= 0 and m[i+1] <= 0):
                        if abs(m[i+1]-m[i]) < 1e-12:
                            return f[i]
                        t = (0 - m[i]) / (m[i+1] - m[i])
                        return f[i] + t*(f[i+1]-f[i])
                return None
            asc_c = crossing(asc_f, asc_m)
            desc_c = crossing(desc_f, desc_m)
            coercive = 0.0
            if asc_c is not None and desc_c is not None:
                coercive = (abs(asc_c)+abs(desc_c))/2.0
            def value_at_zero(f, m):
                for i in range(len(f)-1):
                    if (f[i] <= 0 and f[i+1] >= 0) or (f[i] >= 0 and f[i+1] <= 0):
                        t = (0 - f[i]) / (f[i+1] - f[i])
                        return m[i] + t*(m[i+1]-m[i])
                idx = min(range(len(f)), key=lambda i: abs(f[i]))
                return m[idx]
            rem = value_at_zero(desc_f, desc_m) if desc_m else 0.0
            return coercive, rem
        total_matches = 0
        for gp in gold_pairs:
            key = (gp['substrate'], gp['separation_angstrom'])
            if key not in groups:
                continue
            curve = groups[key]
            coc, rem = compute_hysteresis(curve)
            if coc is None or rem is None:
                continue
            match = True
            if gp.get('expect_hysteresis', True):
                if abs(coc - gp['coercive_field_T']) > gp.get('tol_coercive_abs', 0.5):
                    match = False
                if abs(rem - gp['remanence_norm']) > gp.get('tol_remanence_abs', 0.3):
                    match = False
            else:
                # paramagnetic case: no hysteresis
                if coc > gp['tol_coercive_abs'] or abs(rem) > gp['tol_remanence_abs']:
                    match = False
            if match:
                total_matches += 1
        return total_matches / len(gold_pairs) if gold_pairs else 0.0


# === block: score_3 (check id='hysteresis_summary') ===
def score_3(artifact, step, ctx):
    def score(artifact, step, ctx):
        summary_rows = artifact
        curves = ctx.get('curves', [])
        gold_pairs = step.get('gold_pairs', [])
        if not summary_rows or not curves or not gold_pairs:
            return 0.0
        from collections import defaultdict
        curve_groups = defaultdict(list)
        for r in curves:
            key = (r['substrate'], float(r['separation_angstrom']))
            curve_groups[key].append(r)
        # Recompute hysteresis for each required pair
        def compute_hysteresis(rows_list):
            rows_list.sort(key=lambda r: float(r['field_T']))
            fields = [float(r['field_T']) for r in rows_list]
            mags = [float(r['magnetization_norm']) for r in rows_list]
            n = len(fields)
            if n < 4:
                return None, None
            max_idx = fields.index(max(fields))
            asc_f = fields[:max_idx+1]
            asc_m = mags[:max_idx+1]
            desc_f = fields[max_idx+1:]
            desc_m = mags[max_idx+1:]
            def crossing(f, m):
                for i in range(len(f)-1):
                    if (m[i] <= 0 and m[i+1] >= 0) or (m[i] >= 0 and m[i+1] <= 0):
                        if abs(m[i+1]-m[i]) < 1e-12:
                            return f[i]
                        t = (0 - m[i]) / (m[i+1] - m[i])
                        return f[i] + t*(f[i+1]-f[i])
                return None
            asc_c = crossing(asc_f, asc_m)
            desc_c = crossing(desc_f, desc_m)
            coercive = 0.0
            if asc_c is not None and desc_c is not None:
                coercive = (abs(asc_c)+abs(desc_c))/2.0
            def value_at_zero(f, m):
                for i in range(len(f)-1):
                    if (f[i] <= 0 and f[i+1] >= 0) or (f[i] >= 0 and f[i+1] <= 0):
                        t = (0 - f[i]) / (f[i+1] - f[i])
                        return m[i] + t*(m[i+1]-m[i])
                idx = min(range(len(f)), key=lambda i: abs(f[i]))
                return m[idx]
            rem = value_at_zero(desc_f, desc_m) if desc_m else 0.0
            return coercive, rem
        matches = 0
        for gp in gold_pairs:
            key = (gp['substrate'], gp['separation_angstrom'])
            if key not in curve_groups:
                continue
            coc_recomp, rem_recomp = compute_hysteresis(curve_groups[key])
            # Find corresponding summary row
            summary_match = False
            for sr in summary_rows:
                if sr['substrate'] == gp['substrate'] and abs(float(sr['separation_angstrom']) - gp['separation_angstrom']) < 0.01:
                    if abs(float(sr['coercive_field_T']) - coc_recomp) < 1e-6 and abs(float(sr['remanence_norm']) - rem_recomp) < 1e-6:
                        summary_match = True
                    break
            if summary_match:
                # Also check against gold (already done in curves, but still good)
                if gp.get('expect_hysteresis', True):
                    if abs(coc_recomp - gp['coercive_field_T']) <= gp.get('tol_coercive_abs', 0.5) and abs(rem_recomp - gp['remanence_norm']) <= gp.get('tol_remanence_abs', 0.3):
                        matches += 1
                else:
                    if coc_recomp <= gp['tol_coercive_abs'] and abs(rem_recomp) <= gp['tol_remanence_abs']:
                        matches += 1
            else:
                matches += 0
        return matches / len(gold_pairs) if gold_pairs else 0.0


_SCORERS = {
    'exchange': score_0,
    'anisotropy': score_1,
    'magnetization_curves': score_2,
    'hysteresis_summary': score_3,
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
