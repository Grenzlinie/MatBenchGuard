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
    ref_freqs = spec.get('reference_frequencies', [])
    ref_ratios = spec.get('reference_ratios', [])
    return {'ref_freqs': ref_freqs, 'ref_ratios': ref_ratios}


# === block: score_0 (check id='freq_mape') ===
def score_0(artifact, step, ctx):
    ref_freqs = ctx.get('ref_freqs', [])
    ref_ratios = ctx.get('ref_ratios', [])

    # --- MAPE over reference frequencies (unchanged logic) ---
    errors = []
    for ref in ref_freqs:
        isom = ref['isomer']
        iso = ref['isotopologue']
        pat = ref['pattern']
        exp_freq = ref['experimental_freq']
        matches = [row for row in artifact if row.get('isomer','').strip().lower() == isom.lower() and row.get('isotopologue','').strip() == iso and pat.lower() in row.get('mode_description','').lower()]
        if len(matches) != 1:
            errors.append(100.0)
        else:
            freq = float(matches[0]['frequency_cm1'])
            ape = abs(freq - exp_freq) / exp_freq * 100
            errors.append(ape)

    if not errors:
        mape_score = 1.0
    else:
        mape = sum(errors) / len(errors)
        if mape <= 5.0:
            mape_score = 1.0
        elif mape >= 10.0:
            mape_score = 0.0
        else:
            mape_score = 1.0 - (mape - 5.0) / 5.0

    # --- Isotopic ratio check (fixed D‑row matching) ---
    iso_passed = 0
    iso_total = len(ref_ratios)
    for rr in ref_ratios:
        isom = rr['isomer']
        pat = rr['pattern']   # e.g. 'ce-h stretch'
        ratio_exp = rr['ratio_exp']
        # H row
        h_matches = [row for row in artifact if row.get('isomer','').strip().lower() == isom.lower()
                     and row.get('isotopologue','').strip() == 'H'
                     and pat.lower() in row.get('mode_description','').lower()]
        # D row – use pattern with 'h' replaced by 'd'
        d_pat = pat.lower().replace('-h', '-d').replace('h stretch', 'd stretch')
        d_matches = [row for row in artifact if row.get('isomer','').strip().lower() == isom.lower()
                     and row.get('isotopologue','').strip() == 'D'
                     and d_pat in row.get('mode_description','').lower()]
        if len(h_matches) != 1 or len(d_matches) != 1:
            continue
        freq_h = float(h_matches[0]['frequency_cm1'])
        freq_d = float(d_matches[0]['frequency_cm1'])
        if freq_d == 0:
            continue
        ratio_agent = freq_h / freq_d
        if abs(ratio_agent - ratio_exp) / ratio_exp < 0.05:
            iso_passed += 1

    iso_score = iso_passed / iso_total if iso_total > 0 else 1.0

    # Combined score (0.9 MAPE + 0.1 isotope) — the step weight is 0.9, so overall
    # weighted contribution remains consistent.
    return 0.9 * mape_score + 0.1 * iso_score


# === block: score_1 (check id='isotope_ratio') ===
def score_1(artifact, step, ctx):
    ref_ratios = ctx['ref_ratios']
    if not ref_ratios:
        return 1.0
    total = len(ref_ratios)
    passed = 0
    for rr in ref_ratios:
        isom = rr['isomer']
        pat = rr['pattern']
        ratio_exp = rr['ratio_exp']
        h_rows = [row for row in artifact if row['isomer'].strip().lower()==isom.lower() and row['isotopologue']=='H' and pat.lower() in row['mode_description'].lower()]
        d_rows = [row for row in artifact if row['isomer'].strip().lower()==isom.lower() and row['isotopologue']=='D' and pat.lower() in row['mode_description'].lower()]
        if len(h_rows)!=1 or len(d_rows)!=1:
            continue
        freq_h = float(h_rows[0]['frequency_cm1'])
        freq_d = float(d_rows[0]['frequency_cm1'])
        if freq_d == 0:
            continue
        ratio_agent = freq_h / freq_d
        if abs(ratio_agent - ratio_exp) / ratio_exp < 0.05:
            passed += 1
    if total == 0:
        return 1.0
    return passed / total


_SCORERS = {
    'freq_mape': score_0,
    'isotope_ratio': score_1,
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
