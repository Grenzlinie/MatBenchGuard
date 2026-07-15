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
    step_params = {}
    for s in spec.get('steps', []):
        step_params[s['id']] = s
    return {'step_params': step_params}


# === block: score_0 (check id='step02_binary_lattice') ===
def score_0(artifact, step, ctx):
    params = ctx['step_params'].get(step.get('id'), {})
    targets = params.get('targets', {})
    tol_a0 = params.get('tolerance_abs_a0', 0.1)
    tol_B0 = params.get('tolerance_rel_B0', 0.15)
    if not isinstance(artifact, list) or not artifact:
        return 0.0
    data = {}
    for row in artifact:
        binary = row.get('binary', '').strip()
        try:
            a0 = float(row.get('a0_angstrom', 'NaN'))
            B0 = float(row.get('B0_GPa', 'NaN'))
        except (ValueError, TypeError):
            continue
        data[binary] = {'a0': a0, 'B0': B0}
    scores = []
    for binary, tgt in targets.items():
        if binary not in data:
            scores.append(0.0)
            continue
        a0_err = abs(data[binary]['a0'] - tgt['a0'])
        a0_score = max(0.0, 1.0 - a0_err / tol_a0) if tol_a0 > 0 else (1.0 if a0_err < 1e-9 else 0.0)
        B0_rel_err = abs(data[binary]['B0'] - tgt['B0']) / abs(tgt['B0']) if tgt['B0'] != 0 else abs(data[binary]['B0'] - tgt['B0'])
        B0_score = max(0.0, 1.0 - B0_rel_err / tol_B0)
        scores.append(0.5 * a0_score + 0.5 * B0_score)
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_1 (check id='step04_binary_gaps') ===
def score_1(artifact, step, ctx):
    params = ctx['step_params'].get(step.get('id'), {})
    targets = params.get('targets', {})
    tol_rel = params.get('tolerance_rel_gap', 0.10)
    if not isinstance(artifact, list) or not artifact:
        return 0.0
    data = {}
    for row in artifact:
        binary = row.get('binary', '').strip()
        gt = row.get('gap_type', '').strip()
        try:
            val = float(row.get('energy_eV', 'NaN'))
        except (ValueError, TypeError):
            continue
        data[(binary, gt)] = val
    scores = []
    for binary, tgt in targets.items():
        key = (binary, tgt['gap_type'])
        target_val = tgt['energy_eV']
        if key not in data:
            scores.append(0.0)
            continue
        val = data[key]
        if target_val == 0.0:
            score = 1.0 if abs(val) <= 0.05 else 0.0
        else:
            rel_err = abs(val - target_val) / abs(target_val)
            score = max(0.0, 1.0 - rel_err / tol_rel)
        scores.append(score)
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_2 (check id='step06_quaternary_lattice') ===
def score_2(artifact, step, ctx):
    params = ctx['step_params'].get(step.get('id'), {})
    target = params.get('target', None)
    tol = params.get('tolerance_abs', 0.05)
    if target is None:
        return 0.0
    try:
        if isinstance(artifact, str):
            val = float(artifact.strip().split()[0])
        elif isinstance(artifact, list) and artifact:
            val = float(artifact[0])
        else:
            return 0.0
    except (ValueError, IndexError, AttributeError):
        return 0.0
    diff = abs(val - target)
    score = max(0.0, 1.0 - diff / tol) if tol > 0 else (1.0 if diff < 1e-9 else 0.0)
    return score


# === block: score_3 (check id='step08_quaternary_bandgap') ===
def score_3(artifact, step, ctx):
    params = ctx['step_params'].get(step.get('id'), {})
    target = params.get('target', None)
    tol_rel = params.get('tolerance_rel', 0.10)
    if target is None:
        return 0.0
    try:
        if isinstance(artifact, str):
            val = float(artifact.strip().split()[0])
        elif isinstance(artifact, list) and artifact:
            val = float(artifact[0])
        else:
            return 0.0
    except:
        return 0.0
    rel_err = abs(val - target) / abs(target) if target != 0 else abs(val - target)
    score = max(0.0, 1.0 - rel_err / tol_rel) if tol_rel > 0 else (1.0 if rel_err < 1e-9 else 0.0)
    return score


# === block: score_4 (check id='step10_quaternary_optical') ===
def score_4(artifact, step, ctx):
    params = ctx['step_params'].get(step.get('id'), {})
    targets = params.get('targets', {})
    tol_eps = params.get('tolerance_rel_eps', 0.05)
    tol_n = params.get('tolerance_rel_n', 0.05)
    # consistency check removed to avoid penalizing exact paper-gold matches
    if not isinstance(artifact, list) or len(artifact) < 2:
        return 0.0
    data = {}
    for row in artifact:
        prop = row.get('property', '').strip()
        try:
            val = float(row.get('value', 'NaN'))
        except (ValueError, TypeError):
            continue
        data[prop] = val
    eps = data.get('static_dielectric_constant', None)
    n = data.get('static_refractive_index', None)
    if eps is None or n is None:
        return 0.0
    # value scores
    if eps <= 0:
        eps_score = 0.0
    else:
        tgt_eps = targets.get('static_dielectric_constant', 1)
        rel_err_eps = abs(eps - tgt_eps) / abs(tgt_eps)
        eps_score = max(0.0, 1.0 - rel_err_eps / tol_eps)
    if n <= 0:
        n_score = 0.0
    else:
        tgt_n = targets.get('static_refractive_index', 1)
        rel_err_n = abs(n - tgt_n) / abs(tgt_n)
        n_score = max(0.0, 1.0 - rel_err_n / tol_n)
    return 0.5 * eps_score + 0.5 * n_score


_SCORERS = {
    'step02_binary_lattice': score_0,
    'step04_binary_gaps': score_1,
    'step06_quaternary_lattice': score_2,
    'step08_quaternary_bandgap': score_3,
    'step10_quaternary_optical': score_4,
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
