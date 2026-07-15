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
    return {
        'gap_noSOC': spec.get('gold', {}).get('gap_noSOC', 0.570),
        'gap_SOC': spec.get('gold', {}).get('gap_SOC', 0.123),
        'parity_base': spec.get('gold', {}).get('parity_base', {'Γ': -1, 'X': 1, 'Y': -1, 'M': -1}),
        'z2_base': spec.get('gold', {}).get('z2_base', 1),
        'gap_tol': spec.get('gold', {}).get('gap_tolerance_abs', 0.05),
        'tunable_delta': 0.1
    }


# === block: score_0 (check id='phonon_base') ===
def score_0(artifact, step, ctx):
    data = artifact.get('max_imaginary_frequency', None)
    if data is None:
        return 0.0
    return 1.0 if data <= 0.0 else 0.0


# === block: score_1 (check id='bands_nosoc_base') ===
def score_1(artifact, step, ctx):
    try:
        value = float(artifact.strip())
    except (ValueError, AttributeError):
        return 0.0
    gold = ctx['gap_noSOC']
    tol = ctx['gap_tol']
    diff = abs(value - gold)
    if diff <= tol:
        return 1.0
    else:
        return max(0.0, 1.0 - (diff - tol) / tol)


# === block: score_2 (check id='bands_soc_base') ===
def score_2(artifact, step, ctx):
    try:
        value = float(artifact.strip())
    except (ValueError, AttributeError):
        return 0.0
    gold = ctx['gap_SOC']
    tol = ctx['gap_tol']
    diff = abs(value - gold)
    if diff <= tol:
        return 1.0
    else:
        return max(0.0, 1.0 - (diff - tol) / tol)


# === block: score_3 (check id='parity_base') ===
def score_3(artifact, step, ctx):
    expected = ctx['parity_base']
    for key in ['Γ', 'X', 'Y', 'M']:
        if artifact.get(key) != expected.get(key):
            return 0.0
    return 1.0


# === block: score_4 (check id='z2_base') ===
def score_4(artifact, step, ctx):
    try:
        value = int(artifact.strip())
    except (ValueError, AttributeError):
        return 0.0
    return 1.0 if value == ctx['z2_base'] else 0.0


# === block: score_5 (check id='parity_tunable') ===
def score_5(artifact, step, ctx):
    gamma = artifact.get('Γ')
    if gamma != -1:
        return 0.0
    prod = 1
    for key in ['Γ', 'X', 'Y', 'M']:
        v = artifact.get(key)
        if v is None:
            return 0.0
        prod *= v
    return 1.0 if prod == -1 else 0.0


# === block: score_6 (check id='gap_tunable') ===
def score_6(artifact, step, ctx):
    try:
        tunable_gap = float(artifact.strip())
    except (ValueError, AttributeError):
        return 0.0
    # read base SOC gap from step_03_band_gap_SOC.txt
    import os
    base_path = os.path.join('/app/outputs', 'step_03_band_gap_SOC.txt')
    try:
        with open(base_path, 'r') as f:
            base_gap_str = f.read()
        base_gap = float(base_gap_str.strip())
    except Exception:
        # if base gap missing, treat as fail
        return 0.0
    return 1.0 if tunable_gap >= base_gap + ctx['tunable_delta'] else 0.0


_SCORERS = {
    'phonon_base': score_0,
    'bands_nosoc_base': score_1,
    'bands_soc_base': score_2,
    'parity_base': score_3,
    'z2_base': score_4,
    'parity_tunable': score_5,
    'gap_tunable': score_6,
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
