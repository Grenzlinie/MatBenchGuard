import os
import json
import csv

# === author imports / helpers ===
import os
import csv
import numpy as np


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
    gold_data = {
        'AlN_GammaA_Gamma0.03': (
            np.array([10, 20, 30, 40, 50, 75, 100, 125, 150, 200, 250, 300, 350, 400, 500]),
            np.array([12.5, 55.3, 128.6, 222.1, 315.0, 408.2, 415.7, 387.1, 348.3, 284.6, 238.5, 204.7, 179.2, 158.6, 127.8])
        ),
        'AlN_GammaA_Gamma0.13': (
            np.array([10, 20, 30, 40, 50, 75, 100, 125, 150, 200, 250, 300, 350, 400, 500]),
            np.array([8.1, 32.9, 75.4, 131.2, 190.7, 294.3, 331.5, 326.0, 306.2, 261.8, 224.1, 195.2, 172.4, 153.9, 125.3])
        ),
        'AlN_GammaA_Gamma0.42': (
            np.array([10, 20, 30, 40, 50, 75, 100, 125, 150, 200, 250, 300, 350, 400, 500]),
            np.array([4.7, 17.2, 38.1, 66.3, 100.5, 178.4, 222.9, 238.1, 238.7, 217.6, 192.4, 170.5, 152.3, 137.0, 112.9])
        ),
        'AlN_GammaK_Gamma0.03': (
            np.array([10, 20, 30, 40, 50, 75, 100, 125, 150, 200, 250, 300, 350, 400, 500]),
            np.array([9.2, 40.8, 97.5, 173.4, 254.1, 356.9, 382.2, 370.1, 341.7, 283.5, 239.3, 206.2, 180.9, 160.3, 129.2])
        ),
        'AlN_GammaK_Gamma0.13': (
            np.array([10, 20, 30, 40, 50, 75, 100, 125, 150, 200, 250, 300, 350, 400, 500]),
            np.array([5.9, 23.7, 54.6, 96.4, 145.2, 240.7, 283.4, 288.3, 276.1, 239.8, 207.0, 180.9, 160.2, 143.1, 116.7])
        ),
        'AlN_GammaK_Gamma0.42': (
            np.array([10, 20, 30, 40, 50, 75, 100, 125, 150, 200, 250, 300, 350, 400, 500]),
            np.array([3.4, 12.1, 27.1, 47.4, 72.4, 134.6, 174.9, 193.2, 198.5, 184.2, 164.8, 146.9, 131.5, 118.3, 97.4])
        ),
        'Ge_isotropic': (
            np.array([5, 10, 15, 20, 30, 40, 50, 75, 100, 150, 200, 250, 300, 350, 400, 500]),
            np.array([35.2, 92.7, 148.5, 195.3, 233.1, 245.8, 247.6, 231.4, 214.7, 185.2, 161.9, 142.8, 127.1, 114.2, 103.5, 86.3])
        ),
    }
    return {'exp_data': gold_data}


# === block: score_0 (check id='thermal_conductivity_mae') ===
def score_0(artifact, step, ctx):
    tolerance_rel = float(step.get('tolerance_relative', 0.05))
    if not isinstance(artifact, dict):
        return 0.0
    required_keys = [
        'AlN_GammaA_Gamma0.03',
        'AlN_GammaA_Gamma0.13',
        'AlN_GammaA_Gamma0.42',
        'AlN_GammaK_Gamma0.03',
        'AlN_GammaK_Gamma0.13',
        'AlN_GammaK_Gamma0.42',
        'Ge_isotropic'
    ]
    rel_errors = []
    for key in required_keys:
        if key not in artifact:
            return 0.0
        agent_list = artifact[key]
        if not isinstance(agent_list, list):
            return 0.0
        agent_T_list = []
        agent_k_list = []
        for d in agent_list:
            agent_T_list.append(float(d['T']))
            agent_k_list.append(float(d['k']))
        agent_T = np.array(agent_T_list)
        agent_k = np.array(agent_k_list)
        sort_idx = np.argsort(agent_T)
        agent_T = agent_T[sort_idx]
        agent_k = agent_k[sort_idx]
        exp_data = ctx.get('exp_data', {})
        if key not in exp_data:
            return 0.0
        exp_T, exp_k = exp_data[key]
        interp_k = np.interp(exp_T, agent_T, agent_k)
        points_rel_err = np.abs(interp_k - exp_k) / (np.abs(exp_k) + 1e-8)
        avg_rel_err = np.mean(points_rel_err)
        rel_errors.append(avg_rel_err)
    avg_rel_error = np.mean(rel_errors)
    if avg_rel_error <= tolerance_rel:
        score = 1.0
    else:
        score = max(0.0, 1.0 - (avg_rel_error - tolerance_rel) / tolerance_rel)
    return float(score)


_SCORERS = {
    'thermal_conductivity_mae': score_0,
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
