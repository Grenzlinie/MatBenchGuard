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
    steps = spec.get('steps', [])
    # Extract target values for lattice_kappa_check
    lat_targets = {}
    for s in steps:
        if s['id'] == 'lattice_kappa_check':
            lat_targets = s.get('targets', {})
            break
    return {
        'output_dir': outputs_dir,
        'lattice_targets': lat_targets
    }


# === block: score_0 (check id='lattice_kappa_check') ===
def score_0(artifact, step, ctx):
    kappa = artifact
    target_spec = ctx['lattice_targets']
    if not isinstance(kappa, dict):
        return 0.0
    # The paper reports only κ_l at 300 K for γ-Pb2SeTe (0.163 W/mK).
    # Exclude the 800 K field to avoid penalising the solver with an arbitrary target.
    FIELDS_TO_CHECK = {'kappa_l_300K'}
    scores = []
    for field, spec in target_spec.items():
        if field not in FIELDS_TO_CHECK:
            continue
        val = kappa.get(field)
        if val is None:
            scores.append(0.0)
            continue
        target = spec['target']
        tol = spec['tol_relative']
        if target == 0:
            scores.append(0.0)
            continue
        err_rel = abs(val - target) / target
        score = max(0.0, 1.0 - err_rel / tol) if tol > 0 else (1.0 if err_rel == 0 else 0.0)
        scores.append(score)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_1 (check id='transport_structure_check') ===
def score_1(artifact, step, ctx):
    data = artifact
    if not isinstance(data, list):
        return 0.0
    req_fields = step.get('expected_fields', [])
    for point in data:
        if not isinstance(point, dict):
            return 0.0
        if not all(f in point for f in req_fields):
            return 0.0
    if len(data) < step.get('min_points', 1):
        return 0.0
    return 1.0


# === block: score_2 (check id='zt_recompute_check') ===
def score_2(artifact, step, ctx):
    output_dir = ctx['output_dir']
    try:
        with open(os.path.join(output_dir, 'step_01_lattice_thermal_conductivity.json')) as f:
            kappa_data = json.load(f)
        with open(os.path.join(output_dir, 'step_02_electronic_transport.json')) as f:
            transport = json.load(f)
    except Exception:
        return 0.0

    kappa_l_800K = kappa_data.get('kappa_l_800K')
    if kappa_l_800K is None:
        return 0.0

    config = step.get('recompute_config', {})
    T = config['T']
    gold_max = config['gold_max_ZT']
    gold_n = config['gold_optimal_carrier_concentration']
    tol_n_rel = config.get('tol_carrier_conc_relative', 0.2)

    best_zt = -1
    best_n = None
    for point in transport:
        sigma = point.get('electrical_conductivity')
        S_uV = point.get('seebeck')
        kappa_e = point.get('electronic_thermal_conductivity')
        n = point.get('carrier_concentration')
        if None in (sigma, S_uV, kappa_e, n):
            continue
        S = S_uV * 1e-6
        pf = sigma * S * S
        zt = pf * T / (kappa_e + kappa_l_800K)
        if zt > best_zt:
            best_zt = zt
            best_n = n

    if best_zt < 0:
        return 0.0

    # Score ZT (threshold_or_better)
    if best_zt >= gold_max:
        score_zt = 1.0
    elif best_zt < 4.0:
        score_zt = 0.0
    else:
        score_zt = (best_zt - 4.0) / (gold_max - 4.0)

    # Score carrier concentration
    if best_n is None:
        score_n = 0.0
    else:
        dev = abs(best_n - gold_n) / gold_n
        score_n = max(0.0, 1.0 - dev / tol_n_rel) if tol_n_rel > 0 else 0.0

    weight_zt = 0.6
    weight_n = 0.4
    return weight_zt * score_zt + weight_n * score_n


_SCORERS = {
    'lattice_kappa_check': score_0,
    'transport_structure_check': score_1,
    'zt_recompute_check': score_2,
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
