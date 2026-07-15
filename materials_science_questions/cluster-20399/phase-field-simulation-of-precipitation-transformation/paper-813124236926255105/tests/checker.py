import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.interpolate import interp1d
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
    ref_curves = spec['steps'][0]['params']['reference_curves']
    temp_config = spec['steps'][1]['params']
    band_config = spec['steps'][2]['params']
    ctx = {
        'ref_curves': ref_curves,
        'temp_config': temp_config,
        'band_config': band_config
    }
    return ctx


# === block: score_0 (check id='stress_strain_curves') ===
def score_0(artifact, step, ctx):
    # stress_strain_curves scorer
    import numpy as np
    from scipy.interpolate import interp1d

    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0

    params = step['params']
    tol_mape = params['tolerance_mape']
    decay = params['decay_scale']
    ref_curves = ctx['ref_curves']

    # separate agent points by strain_rate
    agent_by_rate = {}
    for row in artifact:
        try:
            sr = float(row['strain_rate'])
            strain = float(row['strain'])
            stress = float(row['stress'])
        except (ValueError, KeyError):
            continue
        agent_by_rate.setdefault(sr, []).append((strain, stress))

    mapes = []
    for sr_key, ref_data in ref_curves.items():
        ref_sr = float(sr_key)
        # find matching agent points (allow small numerical diff)
        best_sr = None
        for sr in agent_by_rate:
            if abs(sr - ref_sr) < 1e-6:
                best_sr = sr
                break
        if best_sr is None:
            mapes.append(1.0)  # missing rate, penalty
            continue
        agent_pts = sorted(agent_by_rate[best_sr], key=lambda x: x[0])
        if len(agent_pts) < 2:
            mapes.append(1.0)
            continue
        agent_strains = np.array([p[0] for p in agent_pts])
        agent_stresses = np.array([p[1] for p in agent_pts])
        ref_strains = np.array(ref_data['strain'])
        ref_stresses = np.array(ref_data['stress'])
        # interpolate reference at agent strains
        try:
            interp = interp1d(ref_strains, ref_stresses, kind='linear', bounds_error=False, fill_value=0.0)
        except ValueError:
            mapes.append(1.0)
            continue
        ref_interp = interp(agent_strains)
        # compute MAPE, skip points where ref stress near zero
        mask = np.abs(ref_interp) > 1e-6
        if np.sum(mask) == 0:
            mapes.append(0.0)
            continue
        ape = np.abs(agent_stresses[mask] - ref_interp[mask]) / np.abs(ref_interp[mask])
        mape = np.mean(ape)
        mapes.append(mape)

    if len(mapes) == 0:
        return 0.0
    overall_mape = np.mean(mapes)
    if overall_mape <= tol_mape:
        return 1.0
    score = max(0.0, 1.0 - (overall_mape - tol_mape) / decay)
    return float(score)


# === block: score_1 (check id='temperature_evolution') ===
def score_1(artifact, step, ctx):
    # temperature_evolution scorer
    import numpy as np

    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0

    config = ctx['temp_config']
    tol_temp = config['tolerance_temp_k']
    T0 = config['ambient_T0']
    expected = config['expected']

    # separate by strain rate
    agent_by_rate = {}
    for row in artifact:
        try:
            sr = float(row['strain_rate'])
            temp = float(row['temperature'])
        except (ValueError, KeyError):
            continue
        agent_by_rate.setdefault(sr, []).append(temp)

    scores = []
    for sr_key, exp in expected.items():
        ref_sr = float(sr_key)
        best_sr = None
        for sr in agent_by_rate:
            if abs(sr - ref_sr) < 1e-6:
                best_sr = sr
                break
        if best_sr is None:
            scores.append(0.0)
            continue
        temps = np.array(agent_by_rate[best_sr])
        if len(temps) < 2:
            scores.append(0.0)
            continue
        T_max = np.max(temps)
        T_min = np.min(temps)
        rise = T_max - T0
        drop = T0 - T_min
        delta_rise = abs(rise - exp['rise'])
        delta_drop = abs(drop - exp['drop'])
        # score per rate: 1 - max(delta)/tol, clip to [0,1]
        rate_score = max(0.0, 1.0 - max(delta_rise, delta_drop) / tol_temp)
        scores.append(rate_score)

    if len(scores) == 0:
        return 0.0
    return float(np.mean(scores))


# === block: score_2 (check id='band_angle') ===
def score_2(artifact, step, ctx):
    # band_angle scorer
    if not isinstance(artifact, dict):
        return 0.0
    config = ctx['band_config']
    angle = artifact.get(config['field'], None)
    if angle is None:
        return 0.0
    try:
        angle = float(angle)
    except (ValueError, TypeError):
        return 0.0
    if config['min_angle'] <= angle <= config['max_angle']:
        return 1.0
    return 0.0


_SCORERS = {
    'stress_strain_curves': score_0,
    'temperature_evolution': score_1,
    'band_angle': score_2,
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
