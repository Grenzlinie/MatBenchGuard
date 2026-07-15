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
    gs_path = os.path.join(outputs_dir, 'computed_percent_Cl3p.csv')
    xas_path = os.path.join(outputs_dir, 'simulated_XAS_features.csv')

    ground_totals = {}
    if os.path.exists(gs_path):
        with open(gs_path, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                compound = row.get('compound', '').strip()
                orbital = row.get('orbital', '').strip()
                pct_str = row.get('percent_Cl3p', '0')
                try:
                    pct = float(pct_str)
                except:
                    pct = 0.0
                if orbital == 'total':
                    ground_totals[compound] = pct

    xas_data = {}
    if os.path.exists(xas_path):
        with open(xas_path, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                compound = row.get('compound', '').strip()
                peak_label = row.get('peak_label', '').strip()
                try:
                    energy = float(row.get('peak_energy_eV', '0'))
                except:
                    energy = 0.0
                try:
                    osc = float(row.get('oscillator_strength', '0'))
                except:
                    osc = 0.0
                try:
                    pct = float(row.get('percent_Cl3p', '0'))
                except:
                    pct = 0.0
                if compound not in xas_data:
                    xas_data[compound] = []
                xas_data[compound].append({
                    'peak_label': peak_label,
                    'peak_energy_eV': energy,
                    'oscillator_strength': osc,
                    'percent_Cl3p': pct
                })

    xas_totals = {}
    for cpd, peaks in xas_data.items():
        xas_totals[cpd] = sum(p['percent_Cl3p'] for p in peaks)

    return {
        'ground_totals': ground_totals,
        'xas_data': xas_data,
        'xas_totals': xas_totals
    }


# === block: score_0 (check id='gs_total') ===
def score_0(artifact, step, ctx):
    params = step.get('parameters', {})
    compounds = params.get('compounds', {})
    gt = ctx['ground_totals']
    pass_count = 0
    for cpd, cfg in compounds.items():
        total = gt.get(cpd, None)
        if total is None:
            continue
        if abs(total - cfg['target_total']) <= cfg['tolerance']:
            pass_count += 1
    return pass_count / max(1, len(compounds)) if compounds else 0.0


# === block: score_1 (check id='gs_trend') ===
def score_1(artifact, step, ctx):
    gt = ctx['ground_totals']
    order = step.get('parameters', {}).get('order', [])
    if len(order) < 2:
        return 0.0
    vals = []
    for cpd in order:
        v = gt.get(cpd, None)
        if v is None:
            return 0.0
        vals.append(v)
    if all(vals[i] > vals[i+1] for i in range(len(vals)-1)):
        return 1.0
    return 0.0


# === block: score_2 (check id='xas_peaks') ===
def score_2(artifact, step, ctx):
    params = step.get('parameters', {})
    compounds = params.get('compounds', [])
    expected = params.get('expected_n_peaks', 2)
    xas_data = ctx['xas_data']
    if not compounds:
        return 0.0
    pass_count = 0
    for cpd in compounds:
        peaks = xas_data.get(cpd, [])
        if len(peaks) != expected:
            continue
        # ensure labels peak1 and peak2
        labels = [p.get('peak_label','') for p in peaks]
        if 'peak1' not in labels or 'peak2' not in labels:
            continue
        p1 = next((p for p in peaks if p['peak_label'] == 'peak1'), None)
        p2 = next((p for p in peaks if p['peak_label'] == 'peak2'), None)
        if p1 is None or p2 is None:
            continue
        if p2['oscillator_strength'] > p1['oscillator_strength']:
            pass_count += 1
    return pass_count / len(compounds)


# === block: score_3 (check id='xas_splitting') ===
def score_3(artifact, step, ctx):
    params = step.get('parameters', {})
    target_spl = params.get('target_splittings', {})
    tolerance = params.get('tolerance', 0.2)
    xas_data = ctx['xas_data']
    pass_count = 0
    total_cpds = len(target_spl)
    if total_cpds == 0:
        return 0.0
    for cpd, target in target_spl.items():
        peaks = xas_data.get(cpd, [])
        p1 = next((p for p in peaks if p['peak_label'] == 'peak1'), None)
        p2 = next((p for p in peaks if p['peak_label'] == 'peak2'), None)
        if p1 is None or p2 is None:
            continue
        split = p2['peak_energy_eV'] - p1['peak_energy_eV']
        if abs(split - target) <= tolerance:
            pass_count += 1
    return pass_count / total_cpds


# === block: score_4 (check id='xas_consistency') ===
def score_4(artifact, step, ctx):
    tolerance = step.get('parameters', {}).get('tolerance', 2.0)
    gt = ctx['ground_totals']
    xt = ctx['xas_totals']
    if not gt or not xt:
        return 0.0
    pass_count = 0
    for cpd in gt:
        g_val = gt[cpd]
        x_val = xt.get(cpd, None)
        if x_val is None:
            continue
        if abs(x_val - g_val) <= tolerance:
            pass_count += 1
    return pass_count / max(1, len(gt)) if gt else 0.0


_SCORERS = {
    'gs_total': score_0,
    'gs_trend': score_1,
    'xas_peaks': score_2,
    'xas_splitting': score_3,
    'xas_consistency': score_4,
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
