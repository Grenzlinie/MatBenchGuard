import os
import json
import csv

# === author imports / helpers ===
import math


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
        # Precompute expected diameters based on a=0.246 nm
        a = 0.246
        expected_diameters = {}
        # armchair
        for n in range(4, 20):
            d_arm = a * n * math.sqrt(3) / math.pi
            expected_diameters[(n, n, 'armchair')] = d_arm
        # zigzag
        for n in range(5, 20):
            d_zz = a * n / math.pi
            expected_diameters[(n, 0, 'zigzag')] = d_zz
        ctx = {'expected_diameters': expected_diameters}
        return ctx
    


# === block: score_0 (check id='diameter_check') ===
def score_0(artifact, step, ctx):
            expected_diameters = ctx['expected_diameters']
            armchair = artifact.get('armchair', [])
            zigzag = artifact.get('zigzag', [])
            total = 0
            correct = 0
            for tube in armchair:
                try:
                    n = int(tube.get('n', -1))
                    m = int(tube.get('m', -1))
                    if n < 0 or m < 0:
                        continue
                    key = (n, m, 'armchair')
                    if key in expected_diameters:
                        total += 1
                        diam = tube.get('diameter_nm')
                        if diam is not None and isinstance(diam, (int, float)):
                            if abs(diam - expected_diameters[key]) < 1e-3:
                                correct += 1
                except (TypeError, ValueError, AttributeError):
                    continue
            for tube in zigzag:
                try:
                    n = int(tube.get('n', -1))
                    m = int(tube.get('m', -1))
                    if n < 0 or m < 0:
                        continue
                    key = (n, m, 'zigzag')
                    if key in expected_diameters:
                        total += 1
                        diam = tube.get('diameter_nm')
                        if diam is not None and isinstance(diam, (int, float)):
                            if abs(diam - expected_diameters[key]) < 1e-3:
                                correct += 1
                except (TypeError, ValueError, AttributeError):
                    continue
            return correct / max(total, 1)
        


# === block: score_1 (check id='omega_d_constancy') ===
def score_1(artifact, step, ctx):
            ref_product = step['parameters']['reference_product']
            tol = step['parameters']['tolerance_fraction']
            d_thresh = step['parameters']['d_threshold_nm']
            armchair = artifact.get('armchair', [])
            zigzag = artifact.get('zigzag', [])
            products = []
            for tube in armchair + zigzag:
                d = tube.get('diameter_nm')
                rbm = tube.get('rbm_frequency_cm-1')
                if d is not None and rbm is not None and d > d_thresh:
                    products.append(rbm * d)
            if not products:
                return 0.0
            mean_prod = sum(products) / len(products)
            if mean_prod <= 0:
                return 0.0
            rel_diff = abs(mean_prod - ref_product) / ref_product
            if rel_diff <= tol:
                return 1.0
            elif rel_diff <= 2 * tol:
                return 0.5
            else:
                return 0.0
        


# === block: score_2 (check id='specific_A1g_frequencies') ===
def score_2(artifact, step, ctx):
            params = step['parameters']
            # find armchair tube (12,12)
            armchair = artifact.get('armchair', [])
            zigzag = artifact.get('zigzag', [])
            tube_arm = None
            for t in armchair:
                if t['n'] == params['armchair_n'] and t['m'] == params['armchair_m']:
                    tube_arm = t
                    break
            tube_zig = None
            for t in zigzag:
                if t['n'] == params['zigzag_n'] and t['m'] == params['zigzag_m']:
                    tube_zig = t
                    break
            score_arm = 0.0
            score_zig = 0.0
            if tube_arm:
                a1g_freqs = [m['frequency_cm-1'] for m in tube_arm['gamma_modes'] if m['irrep'] == 'A1g']
                if a1g_freqs:
                    low = min(a1g_freqs)
                    high = max(a1g_freqs)
                    low_ok = abs(low - params['armchair_low_A1g']) <= params['armchair_low_tol']
                    high_ok = abs(high - params['armchair_high_A1g']) <= params['armchair_high_tol']
                    if low_ok and high_ok:
                        score_arm = 1.0
            if tube_zig:
                a1g_freqs = [m['frequency_cm-1'] for m in tube_zig['gamma_modes'] if m['irrep'] == 'A1g']
                if a1g_freqs:
                    low = min(a1g_freqs)
                    high = max(a1g_freqs)
                    low_ok = abs(low - params['zigzag_low_A1g']) <= params['zigzag_low_tol']
                    high_ok = abs(high - params['zigzag_high_A1g']) <= params['zigzag_high_tol']
                    if low_ok and high_ok:
                        score_zig = 1.0
            return (score_arm + score_zig) / 2.0
        


# === block: score_3 (check id='mode_activity_counts') ===
def score_3(artifact, step, ctx):
            exp_raman = step['parameters']['expected_raman']
            exp_ir = step['parameters']['expected_ir']
            tubes = artifact.get('armchair', []) + artifact.get('zigzag', [])
            if not tubes:
                return 0.0
            correct = 0
            for t in tubes:
                if t.get('raman_active_total') == exp_raman and t.get('ir_active_total') == exp_ir:
                    correct += 1
            return correct / len(tubes)
        


# === block: score_4 (check id='irrep_validity') ===
def score_4(artifact, step, ctx):
            allowed_basics = set(step['parameters']['allowed_basics'])
            E_prefix = step['parameters']['allowed_E_prefix']
            E_suffixes = set(step['parameters']['allowed_E_suffixes'])

            def is_valid_irrep(irr):
                if irr in allowed_basics:
                    return True
                if irr.startswith(E_prefix):
                    rest = irr[len(E_prefix):]
                    # expect rest to be digits + suffix
                    suffix = ''
                    digits = []
                    for ch in rest:
                        if ch.isdigit():
                            digits.append(ch)
                        else:
                            suffix = rest[len(digits):]
                            break
                    else:
                        return False  # no suffix
                    if digits and suffix in E_suffixes and len(digits) > 0:
                        return True
                return False

            tubes = artifact.get('armchair', []) + artifact.get('zigzag', [])
            total_modes = 0
            valid = 0
            for t in tubes:
                for m in t.get('gamma_modes', []):
                    total_modes += 1
                    if is_valid_irrep(m.get('irrep', '')):
                        valid += 1
            if total_modes == 0:
                return 0.0
            return valid / total_modes
        


_SCORERS = {
    'diameter_check': score_0,
    'omega_d_constancy': score_1,
    'specific_A1g_frequencies': score_2,
    'mode_activity_counts': score_3,
    'irrep_validity': score_4,
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
