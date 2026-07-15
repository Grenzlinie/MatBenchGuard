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
    import math
    steps = spec.get('steps', [])
    hidden = []
    for step in steps:
        if step.get('id') == 'accuracy_hidden_points':
            hidden = step.get('params', {}).get('hidden_points', [])
            break
    xi_values = [0.01 + i*(0.99-0.01)/99 for i in range(100)]
    expected = []
    for hp in hidden:
        N = hp['N']
        xi = xi_values[hp['xi_index']]
        s = 0.0
        for m in range(1, N):
            U = 4 * xi**2 * math.sin(math.pi * m / N)**2 / (1 - xi**2)**2
            s += U * math.log(1 + 1/U)
        deltaW = xi**4 - 4 * xi**2 * math.log(xi) - 1 - (1 - xi**2)**2 * (1.0 / N) * s
        expected.append({'N': N, 'xi': xi, 'expected': deltaW})
    ctx = {'expected': expected, 'xi_values': xi_values}


# === block: score_0 (check id='accuracy_hidden_points') ===
def score_0(artifact, step, ctx):
    if artifact is None or not isinstance(artifact, list):
        return 0.0

    # Retrieve hidden points from the scorer's own step params (bypass broken ctx)
    hidden_points = []
    if 'params' in step and isinstance(step['params'], dict):
        hidden_points = step['params'].get('hidden_points', [])
    if not hidden_points:
        return 0.0

    # Reconstruct per‑N sorted unique xi values from the submitted artifact
    n_to_xi_list = {}
    for row in artifact:
        try:
            N_val = int(row['N'])
            xi_val = float(row['xi'])
            if N_val not in n_to_xi_list:
                n_to_xi_list[N_val] = []
            n_to_xi_list[N_val].append(xi_val)
        except:
            pass
    for N_val in n_to_xi_list:
        n_to_xi_list[N_val] = sorted(set(n_to_xi_list[N_val]))

    pass_count = 0
    total = len(hidden_points)
    for hp in hidden_points:
        N_target = hp['N']
        xi_idx = hp['xi_index']
        if N_target not in n_to_xi_list:
            continue
        xi_list = n_to_xi_list[N_target]
        if xi_idx >= len(xi_list):
            continue
        xi = xi_list[xi_idx]

        # Recomute expected deltaW from the paper's formula (Eq. 16)
        s = 0.0
        for m in range(1, N_target):
            U = 4 * xi**2 * math.sin(math.pi * m / N_target)**2 / (1 - xi**2)**2
            s += U * math.log(1 + 1 / U)
        exp_dw = xi**4 - 4 * xi**2 * math.log(xi) - 1 - (1 - xi**2)**2 * (1.0 / N_target) * s

        # Find the agent's reported deltaW for this exact (N, xi)
        found = None
        for row in artifact:
            try:
                if int(row['N']) == N_target and abs(float(row['xi']) - xi) < 1e-12:
                    found = float(row['deltaW'])
                    break
            except:
                pass
        if found is None:
            continue

        rel_err = abs(found - exp_dw) / max(abs(exp_dw), 1e-12)
        if rel_err <= 1e-6:
            pass_count += 1

    return pass_count / total


# === block: score_1 (check id='all_negative') ===
def score_1(artifact, step, ctx):
    for row in artifact:
        try:
            dw = float(row['deltaW'])
            if dw >= 0.0:
                return 0.0
        except:
            pass
    return 1.0


_SCORERS = {
    'accuracy_hidden_points': score_0,
    'all_negative': score_1,
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
