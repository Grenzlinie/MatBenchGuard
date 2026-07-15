import os
import json
import csv

# === author imports / helpers ===
import numpy as np
import csv
import io

def compute_alpha(epsilon, delta):
    r = np.sqrt(epsilon**2 + delta**2)
    term1 = np.sqrt(r + delta)
    term2 = np.sqrt(r - delta)
    alpha = 0.5 * (term1 * (1 + 1j) - term2 * (1 - 1j))
    return alpha

def compute_W(epsilon, delta, z):
    alpha = compute_alpha(epsilon, delta)
    denom = 1j * delta + epsilon
    sinh_a = np.sinh(alpha)
    C1 = (1 - np.exp(-alpha)) / (2 * sinh_a * denom)
    C2 = (np.exp(alpha) - 1) / (2 * sinh_a * denom)
    W = C1 * np.exp(alpha * z) + C2 * np.exp(-alpha * z) - 1 / denom
    return W

def compute_U_V_A(epsilon, delta, z):
    W = compute_W(epsilon, delta, z)
    U = np.real(W)
    V = np.imag(W)
    A = np.sqrt(U**2 + V**2)
    return U, V, A


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


# === block: score_0 (check id='step_shape_nominal') ===
def score_0(artifact, step, ctx):
    epsilon = 1e-6
    delta = 0.2
    expected_z = np.linspace(0.0, 1.0, 1000)
    U_exp, V_exp, A_exp = compute_U_V_A(epsilon, delta, expected_z)

    if not artifact or not isinstance(artifact, list) or len(artifact) != 1000:
        return 0.0
    try:
        agent_z = np.array([float(row['z']) for row in artifact])
        agent_U = np.array([float(row['U']) for row in artifact])
        agent_V = np.array([float(row['V']) for row in artifact])
        agent_A = np.array([float(row['amplitude']) for row in artifact])
    except (KeyError, ValueError, TypeError):
        return 0.0

    if not np.allclose(agent_z, expected_z, atol=1e-12):
        return 0.0
    if not np.allclose(agent_U, U_exp, atol=1e-12):
        return 0.0
    if not np.allclose(agent_V, V_exp, atol=1e-12):
        return 0.0
    if not np.allclose(agent_A, A_exp, atol=1e-12):
        return 0.0
    return 1.0


# === block: score_1 (check id='step_max_amplitude_vs_delta') ===
def score_1(artifact, step, ctx):
    epsilon = 1e-6
    delta_list = [0.1, 0.5, 1, 2, 5, 10, 20, 50, 100]
    z_center = np.array([0.5])
    agent_rows = list(csv.DictReader(io.StringIO('\n'.join(artifact))))
    if len(agent_rows) != len(delta_list):
        return 0.0
    agent_delta = np.array([float(row['delta']) for row in agent_rows])
    agent_amp = np.array([float(row['max_amplitude']) for row in agent_rows])
    # sort by delta for component-wise comparison
    order = np.argsort(agent_delta)
    agent_delta = agent_delta[order]
    agent_amp = agent_amp[order]
    expected_delta = np.array(delta_list)
    expected_amp = np.array([compute_U_V_A(epsilon, d, z_center)[2][0] for d in delta_list])
    if not np.allclose(agent_delta, expected_delta, atol=1e-12):
        return 0.0
    if not np.allclose(agent_amp, expected_amp, atol=1e-12):
        return 0.0
    return 1.0


# === block: score_2 (check id='step_max_amplitude_vs_epsilon') ===
def score_2(artifact, step, ctx):
    delta = 0.2
    epsilon_list = [0.1, 1, 5, 10, 20, 50, 100]
    z_center = np.array([0.5])
    agent_rows = list(csv.DictReader(io.StringIO('\n'.join(artifact))))
    if len(agent_rows) != len(epsilon_list):
        return 0.0
    agent_epsilon = np.array([float(row['epsilon']) for row in agent_rows])
    agent_amp = np.array([float(row['max_amplitude']) for row in agent_rows])
    order = np.argsort(agent_epsilon)
    agent_epsilon = agent_epsilon[order]
    agent_amp = agent_amp[order]
    expected_epsilon = np.array(epsilon_list)
    expected_amp = np.array([compute_U_V_A(e, delta, z_center)[2][0] for e in epsilon_list])
    if not np.allclose(agent_epsilon, expected_epsilon, atol=1e-12):
        return 0.0
    if not np.allclose(agent_amp, expected_amp, atol=1e-12):
        return 0.0
    return 1.0


_SCORERS = {
    'step_shape_nominal': score_0,
    'step_max_amplitude_vs_delta': score_1,
    'step_max_amplitude_vs_epsilon': score_2,
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
