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
    return {}


# === block: score_0 (check id='step1') ===
def score_0(artifact, step, ctx):
        # scoring logic for FCC and BCC structural trends
        config = step.get('scorer_config', {})
        fcc_gap_interval = config.get('fcc_gap_interval', [0.6, 0.75])
        fcc_gap_min, fcc_gap_max = fcc_gap_interval
        fcc_gap_tol = config.get('fcc_gap_tolerance', 1e-6)
        bcc_gap_tol = config.get('bcc_gap_tolerance', 1e-6)
        bcc_N_EF_frac = config.get('bcc_N_EF_fraction', 0.5)
        sub_weights = config.get('sub_weights', {'fcc_gap': 0.25, 'fcc_mono': 0.25, 'fcc_plasma': 0.15, 'bcc_gap': 0.15, 'bcc_metallic': 0.2})
        fcc_rows = []
        bcc_rows = []
        for row in artifact:
            phase = row.get('phase', '').strip().upper()
            try:
                v = float(row.get('V_over_V0'))
                n_ef = float(row.get('N_EF'))
                gap = float(row.get('band_gap'))
                plasma = float(row.get('plasma_frequency'))
            except (ValueError, TypeError):
                continue
            entry = {'V': v, 'N_EF': n_ef, 'band_gap': gap, 'plasma': plasma}
            if phase == 'FCC':
                fcc_rows.append(entry)
            elif phase == 'BCC':
                bcc_rows.append(entry)

        scores = {}

        # FCC band gap integrity
        fcc_gap_score = 1.0
        if fcc_rows:
            interval_rows = [r for r in fcc_rows if fcc_gap_min <= r['V'] <= fcc_gap_max]
            if interval_rows:
                neg_violations = sum(1 for r in interval_rows if r['band_gap'] < -fcc_gap_tol)
                fcc_gap_score = max(0.0, 1.0 - neg_violations / len(interval_rows))
                # must have at least one positive gap
                if all(r['band_gap'] <= fcc_gap_tol for r in interval_rows):
                    fcc_gap_score *= 0.5
            high_rows = [r for r in fcc_rows if r['V'] > fcc_gap_max]
            if high_rows:
                high_violations = sum(1 for r in high_rows if r['band_gap'] > fcc_gap_tol)
                if high_violations > 0:
                    fcc_gap_score = max(0.0, fcc_gap_score - 0.1 * high_violations / len(high_rows))
        else:
            fcc_gap_score = 0.0
        scores['fcc_gap'] = fcc_gap_score

        # FCC N_EF monotonic (should increase with V/V0, i.e. decrease with compression)
        fcc_mono_score = 1.0
        if fcc_rows:
            sorted_fcc = sorted(fcc_rows, key=lambda r: r['V'])
            n_vals = [r['N_EF'] for r in sorted_fcc]
            if len(n_vals) > 1:
                # adaptive tolerance: 2% of the N_EF range, minimum 1e-6
                n_range = max(n_vals) - min(n_vals)
                if n_range < 1e-6:
                    n_range = 1.0   # fallback so fraction makes sense
                adaptive_tol = max(1e-6, 0.02 * n_range)
                diffs = [n_vals[i+1] - n_vals[i] for i in range(len(n_vals)-1)]
                # violation if N_EF *decreases* beyond tolerance (d < -tol)
                violations = sum(1 for d in diffs if d < -adaptive_tol)
                fcc_mono_score = max(0.0, 1.0 - violations / len(diffs))
        else:
            fcc_mono_score = 0.0
        scores['fcc_mono'] = fcc_mono_score

        # FCC plasma frequency monotonic (should increase with V/V0, i.e. decrease with compression)
        fcc_plasma_score = 1.0
        if fcc_rows:
            sorted_fcc = sorted(fcc_rows, key=lambda r: r['V'])
            p_vals = [r['plasma'] for r in sorted_fcc]
            if len(p_vals) > 1:
                p_range = max(p_vals) - min(p_vals)
                if p_range < 1e-6:
                    p_range = 1.0
                adaptive_tol_p = max(1e-6, 0.02 * p_range)
                diffs_p = [p_vals[i+1] - p_vals[i] for i in range(len(p_vals)-1)]
                violations_p = sum(1 for d in diffs_p if d < -adaptive_tol_p)
                fcc_plasma_score = max(0.0, 1.0 - violations_p / len(diffs_p))
        else:
            fcc_plasma_score = 0.0
        scores['fcc_plasma'] = fcc_plasma_score

        # BCC gap zero
        bcc_gap_score = 1.0
        if bcc_rows:
            violations = sum(1 for r in bcc_rows if abs(r['band_gap']) > bcc_gap_tol)
            if len(bcc_rows) > 0:
                bcc_gap_score = max(0.0, 1.0 - violations / len(bcc_rows))
        else:
            bcc_gap_score = 0.0
        scores['bcc_gap'] = bcc_gap_score

        # BCC N_EF metallic threshold
        bcc_metal_score = 1.0
        if bcc_rows:
            max_n_ef = max(r['N_EF'] for r in bcc_rows)
            threshold = bcc_N_EF_frac * max_n_ef
            low_violations = sum(1 for r in bcc_rows if r['N_EF'] < threshold)
            if len(bcc_rows) > 0:
                bcc_metal_score = max(0.0, 1.0 - low_violations / len(bcc_rows))
        else:
            bcc_metal_score = 0.0
        scores['bcc_metallic'] = bcc_metal_score

        total = 0.0
        for k in sub_weights:
            total += scores.get(k, 0.0) * sub_weights[k]
        return min(1.0, max(0.0, total))


_SCORERS = {
    'step1': score_0,
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
