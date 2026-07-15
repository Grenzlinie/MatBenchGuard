import os
import json
import csv

# === author imports / helpers ===
import csv, os

def recompute_gap_from_dos(rows, dos_thresh=0.001):
    """Recompute band gap (eV) from list of dicts with 'energy' and 'total_dos'.
    Fermi level is at energy=0."""
    vals = []
    for r in rows:
        try:
            e = float(r['energy'])
            d = float(r['total_dos'])
        except (KeyError, ValueError):
            continue
        vals.append((e, d))
    if not vals:
        return None
    vals.sort(key=lambda x: x[0])
    # VBM: highest occupied (energy < 0) with DOS > threshold
    vbm = None
    for e, d in vals:
        if e < 0 and d > dos_thresh:
            vbm = e
    # CBM: lowest unoccupied (energy > 0) with DOS > threshold
    cbm = None
    for e, d in vals:
        if e > 0 and d > dos_thresh:
            cbm = e
            break
    if vbm is not None and cbm is not None:
        return cbm - vbm
    return None


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
    dos_path = os.path.join(outputs_dir, 'pure_BTO_dos.csv')
    ctx = {'pure_gap': None}
    if os.path.exists(dos_path):
        with open(dos_path, newline='') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            if rows:
                ctx['pure_gap'] = recompute_gap_from_dos(rows)
    return ctx


# === block: score_0 (check id='pure_BTO_dos_check') ===
def score_0(artifact, step, ctx):
    import csv, os

    # 1. Band gap check (reuse from ctx computed in prepare)
    gap = ctx.get('pure_gap')
    target = step.get('target')
    tol = step.get('tolerance', 0.0)
    gap_score = 0.0
    if gap is not None and abs(gap - target) <= tol:
        gap_score = 1.0

    # 2. Optical absorption onset check (red shift + reference values)
    abs_path = os.path.join('/app/outputs', 'optical_absorption.csv')
    abs_score = 0.0
    if os.path.exists(abs_path):
        with open(abs_path, newline='') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        data = {}
        for row in rows:
            sys = row.get('system', '').strip()
            try:
                onset = float(row['onset_wavelength_nm'])
            except (ValueError, KeyError):
                continue
            data[sys] = onset
        # Hidden reference values from paper (BTO 495 nm, TiO2 anatase 425 nm)
        expected = {'BTO': 495.0, 'TiO2_anatase': 425.0}
        tol_nm = 30.0  # generous tolerance
        onset_ok = 0
        for sys, exp in expected.items():
            if sys in data and abs(data[sys] - exp) <= tol_nm:
                onset_ok += 1
        # Red shift condition
        red_shift = False
        if 'BTO' in data and 'TiO2_anatase' in data:
            if data['BTO'] > data['TiO2_anatase']:
                red_shift = True
        if onset_ok == 2 and red_shift:
            abs_score = 1.0
        elif onset_ok == 2:
            abs_score = 0.5
        else:
            abs_score = 0.0

    # Combine the two headline checks equally
    return 0.5 * gap_score + 0.5 * abs_score


# === block: score_1 (check id='substituted_bandgaps_check') ===
def score_1(artifact, step, ctx):
    pure_gap = ctx.get('pure_gap')
    rows = artifact  # list of dicts
    systems_expected = step.get('expected_systems', [])
    if not rows:
        return 0.0

    data = {}
    for row in rows:
        sys = row.get('system', '').strip()
        try:
            gap_val = float(row.get('band_gap'))
        except (ValueError, TypeError):
            gap_val = None
        flag_str = row.get('midgap_state_flag', '').strip().lower()
        flag = True if flag_str in ('true', '1', 'yes') else False
        data[sys] = {'gap': gap_val, 'flag': flag}

    checks = []
    for sys in systems_expected:
        if sys not in data:
            # Missing system: fail both gap-less and flag checks
            checks.append(False)
            checks.append(False)
            continue
        d = data[sys]
        # gap < pure_gap check
        if pure_gap is not None and d['gap'] is not None and d['gap'] < pure_gap:
            checks.append(True)
        else:
            checks.append(False)
        # midgap flag check
        if d['flag']:
            checks.append(True)
        else:
            checks.append(False)

    # Fe smallest gap check
    fe_gap = None
    for sys in systems_expected:
        if 'fe' in sys.lower() and sys in data:
            fe_gap = data[sys]['gap']
            break
    all_gaps = [data[s]['gap'] for s in systems_expected if s in data and data[s]['gap'] is not None]
    if all_gaps and fe_gap is not None:
        min_gap = min(all_gaps)
        if abs(fe_gap - min_gap) < 1e-9:
            checks.append(True)
        else:
            checks.append(False)
    else:
        checks.append(False)

    total_checks = len(checks)
    if total_checks == 0:
        return 0.0
    score = sum(1 for c in checks if c) / total_checks
    return score


_SCORERS = {
    'pure_BTO_dos_check': score_0,
    'substituted_bandgaps_check': score_1,
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
