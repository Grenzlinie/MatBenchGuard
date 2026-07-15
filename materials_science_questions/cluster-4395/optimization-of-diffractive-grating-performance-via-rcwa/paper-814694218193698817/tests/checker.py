import os
import json
import csv

# === author imports / helpers ===
import math, cmath


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


# === block: score_0 (check id='compile_results') ===
def score_0(artifact, step, ctx):
    def to_float(val):
        try:
            return float(val) if val not in (None, '', ' ') else None
        except:
            return None

    def compute_z(amp, phase_deg):
        phase_rad = math.radians(phase_deg)
        re_s11 = amp * math.cos(phase_rad)
        im_s11 = amp * math.sin(phase_rad)
        numerator = complex(1 + re_s11, im_s11)
        denominator = complex(1 - re_s11, -im_s11)
        z = numerator / denominator
        return z.real, z.imag

    designs = {
        'Au nanodisk array': {
            'wl': 1480, 'wl_tol': 50,
            'z_real_tol': 0.1, 'z_imag_tol': 0.1, 'z_imag_dir': 'abs_less',
            'r0_max': 0.05, 'r20_max': 0.1, 'r36_max': 0.1, 'r20_dir': 'less', 'r36_dir': 'less'
        },
        'Pd wire array (p=450nm)': {
            'wl': 720, 'wl_tol': 50,
            'z_real_tol': 0.1, 'z_imag_tol': -0.15, 'z_imag_dir': 'leq',
            'r0_max': 0.05, 'r20_dir': 'greater', 'r20_min': 0.15, 'r36_dir': 'greater', 'r36_min': 0.3
        },
        'Pd wire array (p=300nm)': {
            'wl': 690, 'wl_tol': 50,
            'z_real_tol': 0.1, 'z_imag_tol': 0.1, 'z_imag_dir': 'abs_less',
            'r0_max': 0.05, 'r20_max': 0.1, 'r36_max': 0.1, 'r20_dir': 'less', 'r36_dir': 'less'
        },
        'Disordered Au nanodisk (single)': {
            'wl': 780, 'wl_tol': 50,
            'z_real_tol': 0.1, 'z_imag_tol': 0.1, 'z_imag_dir': 'abs_less',
            'skip_reflectance': True
        }
    }

    total = 0
    passed = 0
    for row in artifact:
        name = row.get('design_name', '').strip()
        if name not in designs:
            continue
        cfg = designs[name]
        # wavelength
        wl = to_float(row.get('resonance_wavelength_nm'))
        if wl is not None and abs(wl - cfg['wl']) <= cfg['wl_tol']:
            passed += 1
        total += 1
        # impedance recompute
        amp = to_float(row.get('S11_amplitude'))
        phase = to_float(row.get('S11_phase_deg'))
        if amp is None or phase is None:
            continue
        zr, zi = compute_z(amp, phase)
        # Z_real check
        if abs(zr - 1) < cfg['z_real_tol']:
            passed += 1
        total += 1
        # Z_imag check
        if cfg['z_imag_dir'] == 'abs_less':
            if abs(zi) < cfg['z_imag_tol']:
                passed += 1
        elif cfg['z_imag_dir'] == 'leq':
            if zi <= cfg['z_imag_tol']:
                passed += 1
        total += 1
        # reflectance checks
        if cfg.get('skip_reflectance'):
            continue
        r0 = to_float(row.get('reflectance_0deg'))
        r20 = to_float(row.get('reflectance_20deg'))
        r36 = to_float(row.get('reflectance_36deg'))
        if r0 is None or r20 is None or r36 is None:
            continue
        if r0 < cfg['r0_max']:
            passed += 1
        total += 1
        if cfg['r20_dir'] == 'less' and r20 < cfg['r20_max']:
            passed += 1
        elif cfg['r20_dir'] == 'greater' and r20 > cfg['r20_min']:
            passed += 1
        total += 1
        if cfg['r36_dir'] == 'less' and r36 < cfg['r36_max']:
            passed += 1
        elif cfg['r36_dir'] == 'greater' and r36 > cfg['r36_min']:
            passed += 1
        total += 1

    if total == 0:
        return 0.0
    return passed / total


_SCORERS = {
    'compile_results': score_0,
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
