import os
import json
import csv

# === author imports / helpers ===
import csv, math

k_B = 0.0861733034  # meV/K

def compute_expected_ratio(T, freq_params):
    omega_H = freq_params['omega_H_meV']
    omega_D = freq_params['omega_D_meV']
    scale_D = freq_params['scale_D_act']
    perp_ratio = freq_params['omega_perp_H_ratio']
    par_ratio = freq_params['omega_par_H_ratio']
    omega_perp_H = perp_ratio * omega_H
    omega_par_H = par_ratio * omega_H
    omega_perp_D = omega_perp_H * scale_D
    omega_par_D = omega_par_H * scale_D
    beta = 1.0 / (k_B * T)
    # O-site factor
    sh_H = math.sinh(omega_H * beta / 2.0)
    sh_D = math.sinh(omega_D * beta / 2.0)
    O_term = (sh_D / sh_H) ** 3
    sh_perp_H = math.sinh(omega_perp_H * beta / 2.0)
    sh_perp_D = math.sinh(omega_perp_D * beta / 2.0)
    perp_term = (sh_perp_H / sh_perp_D) ** 2
    sh_par_H = math.sinh(omega_par_H * beta / 2.0)
    sh_par_D = math.sinh(omega_par_D * beta / 2.0)
    par_term = sh_par_H / sh_par_D
    return O_term * perp_term * par_term


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
    def prepare(outputs_dir, spec):
        steps = spec.get('steps', [])
        freq_params = None
        for step in steps:
            if step.get('id') == 'step_ratio_accuracy':
                freq_params = step.get('frequencies', {})
                break
        return {'freq_params': freq_params}


# === block: score_0 (check id='step_ratio_accuracy') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        freq_params = ctx.get('freq_params')
        if not freq_params:
            return 0.0
        tolerance = step.get('tolerance_abs', 0.02)
        if not artifact:
            return 0.0
        total = 0
        within = 0
        for row in artifact:
            try:
                T = float(row['temperature_K'])
                ratio = float(row['ratio_DD_DH'])
            except (KeyError, ValueError, TypeError):
                continue
            expected = compute_expected_ratio(T, freq_params)
            if abs(ratio - expected) <= tolerance:
                within += 1
            total += 1
        if total == 0:
            return 0.0
        return within / total


# === block: score_1 (check id='step_ratio_structure') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not artifact:
            return 0.0
        classical = step.get('classical_ratio', 0.70710678)
        check_monotonic = step.get('check_monotonic_decreasing_T', True)
        check_classical = step.get('check_above_classical', True)
        min_points = step.get('min_points', 50)
        data = []
        for row in artifact:
            try:
                T = float(row['temperature_K'])
                r = float(row['ratio_DD_DH'])
                data.append((T, r))
            except (KeyError, ValueError):
                continue
        if len(data) < min_points:
            return 0.0
        data.sort(key=lambda x: x[0])
        Ts = [d[0] for d in data]
        ratios = [d[1] for d in data]
        if check_classical:
            if not all(r > classical for r in ratios):
                return 0.0
        if check_monotonic:
            for i in range(1, len(ratios)):
                if ratios[i] > ratios[i-1]:
                    return 0.0
        return 1.0


_SCORERS = {
    'step_ratio_accuracy': score_0,
    'step_ratio_structure': score_1,
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
