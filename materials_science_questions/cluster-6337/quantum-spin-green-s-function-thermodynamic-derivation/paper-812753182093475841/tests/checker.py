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
    return {}


# === block: score_0 (check id='step_02_low_temperature_solution') ===
def score_0(artifact, step, ctx):
    import math

    artifact_str = artifact
    try:
        namespace = {}
        exec(artifact_str, namespace)
    except Exception:
        return 0.0

    required_funcs = ['omega', 'Gamma', 'magnetization', 'correlation']
    for f in required_funcs:
        if f not in namespace:
            return 0.0

    omega = namespace['omega']
    Gamma = namespace['Gamma']
    magnetization = namespace['magnetization']
    correlation = namespace['correlation']

    hidden_params = step.get('hidden_params', [])
    tol_rel = step.get('tolerance_rel', 1e-6)

    def ref_omega(k, I, h, S, T):
        four_I_S = 4.0 * I * S
        term = 1.0 - 0.5 * T / (I * S * S) * (1.0 - h / (h + four_I_S))
        if term < 0.0:
            term = 0.0
        return h + four_I_S * (math.sin(k / 2.0) ** 2) * math.sqrt(term)

    def ref_Gamma(k, I, h, S, T):
        return (8.0 * I * I / (h * (h + 4.0 * I * S))) * T * T * ((1.0 - math.cos(k)) ** 2)

    def ref_magnetization(I, h, S, T):
        return S - T / math.sqrt(h * (h + 4.0 * I * S))

    def ref_correlation(k, I, h, S, T):
        return (2.0 / S) * T / (h + 2.0 * I * S * (1.0 - math.cos(k)))

    success = 0
    total = 0
    for params in hidden_params:
        try:
            k = float(params['k'])
            I = float(params['I'])
            h = float(params['h'])
            S = float(params['S'])
            T = float(params['T'])
            ref_vals = {
                'omega': ref_omega(k, I, h, S, T),
                'Gamma': ref_Gamma(k, I, h, S, T),
                'magnetization': ref_magnetization(I, h, S, T),
                'correlation': ref_correlation(k, I, h, S, T),
            }
            agent_vals = {
                'omega': omega(k, I, h, S, T),
                'Gamma': Gamma(k, I, h, S, T),
                'magnetization': magnetization(I, h, S, T),
                'correlation': correlation(k, I, h, S, T),
            }
        except Exception:
            continue
        for fname in required_funcs:
            expected = ref_vals[fname]
            agent_val = agent_vals[fname]
            if abs(expected) < 1e-12:
                diff = abs(agent_val - expected)
                if diff <= tol_rel:
                    success += 1
            else:
                rel_err = abs(agent_val - expected) / abs(expected)
                if rel_err <= tol_rel:
                    success += 1
            total += 1

    if total == 0:
        return 0.0
    return success / total


_SCORERS = {
    'step_02_low_temperature_solution': score_0,
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
