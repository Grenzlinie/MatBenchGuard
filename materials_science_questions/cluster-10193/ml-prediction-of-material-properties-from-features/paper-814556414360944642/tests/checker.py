import os
import json
import csv

# === author imports / helpers ===
import json, csv, math

def _score_r2(agent_val, ref_val, tol):
    if agent_val is None or ref_val is None:
        return 0.0
    if agent_val >= ref_val - tol:
        return 1.0
    # linear decay: at ref_val - 2*tol -> 0.0
    lower = ref_val - 2 * tol
    if agent_val <= lower:
        return 0.0
    return (agent_val - lower) / tol

def _score_mae(agent_val, ref_val, tol):
    if agent_val is None or ref_val is None:
        return 0.0
    if agent_val <= ref_val + tol:
        return 1.0
    upper = ref_val + 2 * tol
    if agent_val >= upper:
        return 0.0
    return (upper - agent_val) / tol

def _score_mse(agent_val, ref_val, tol):
    # MSE: lower is better, same structure as MAE
    return _score_mae(agent_val, ref_val, tol)

def _score_regression_metrics(artifact, ref):
    if not isinstance(artifact, dict):
        return 0.0
    atom_types = ref.get('atom_types', {})
    total_ref = ref.get('total', {})
    r2_tol = ref.get('R2_tolerance', 0.005)
    mae_tol = ref.get('mae_tolerance', 0.0005)
    mse_tol = ref.get('mse_tolerance', 0.00001)
    elements = ['H', 'C', 'N', 'O', 'F']
    agent_atom = artifact.get('atom_types', {})
    agent_total = artifact.get('total', {})
    sub_scores = []
    for elem in elements:
        ref_vals = atom_types.get(elem, {})
        agent_vals = agent_atom.get(elem, {})
        if not agent_vals:
            sub_scores.append(0.0)
            continue
        r2_s = _score_r2(agent_vals.get('R2'), ref_vals.get('R2'), r2_tol)
        mae_s = _score_mae(agent_vals.get('MAE'), ref_vals.get('MAE'), mae_tol)
        mse_s = _score_mse(agent_vals.get('MSE'), ref_vals.get('MSE'), mse_tol)
        sub_scores.append((r2_s + mae_s + mse_s) / 3.0)
    # total metrics
    if agent_total:
        r2_t = _score_r2(agent_total.get('R2'), total_ref.get('R2'), r2_tol)
        mae_t = _score_mae(agent_total.get('MAE'), total_ref.get('MAE'), mae_tol)
        mse_t = _score_mse(agent_total.get('MSE'), total_ref.get('MSE'), mse_tol)
        sub_scores.append((r2_t + mae_t + mse_t) / 3.0)
    # dipole moment R² (present in GAFF and DFT results)
    dipole_ref = ref.get('dipole_moment_R2')
    dipole_agent = artifact.get('dipole_moment_R2')
    if dipole_ref is not None and dipole_agent is not None:
        dipole_tol = ref.get('dipole_R2_tolerance', 0.005)
        dipole_s = _score_r2(dipole_agent, dipole_ref, dipole_tol)
        sub_scores.append(dipole_s)
    if not sub_scores:
        return 0.0
    return sum(sub_scores) / len(sub_scores)


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
    ctx = {}
    for step in steps:
        ref = step.get('reference')
        if ref:
            ctx[step['id']] = ref
    return ctx


# === block: score_0 (check id='fingerprints') ===
def score_0(artifact, step, ctx):
    ref = ctx.get('fingerprints')
    if not ref:
        return 0.0
    ref_rows = ref['rows']
    ref_set = set()
    for r in ref_rows:
        try:
            ref_set.add((int(r['l']), float(r['rc']), str(r['F_name'])))
        except (KeyError, ValueError, TypeError):
            continue
    if not ref_set:
        return 0.0
    if not isinstance(artifact, list):
        return 0.0
    agent_set = set()
    for row in artifact:
        try:
            l = int(row.get('l', ''))
            rc = float(row.get('rc', ''))
            fn = str(row.get('F_name', ''))
        except (ValueError, TypeError):
            continue
        agent_set.add((l, rc, fn))
    intersection = ref_set & agent_set
    score = len(intersection) / len(ref_set)
    return min(1.0, score)


# === block: score_1 (check id='gaff_metrics') ===
def score_1(artifact, step, ctx):
    return _score_regression_metrics(artifact, ctx.get('gaff_metrics'))


# === block: score_2 (check id='dft_metrics') ===
def score_2(artifact, step, ctx):
    return _score_regression_metrics(artifact, ctx.get('dft_metrics'))


# === block: score_3 (check id='transfer_metrics') ===
def score_3(artifact, step, ctx):
    ref = ctx.get('transfer_metrics')
    if not isinstance(artifact, dict):
        return 0.0
    atom_types = ref.get('atom_types', {})
    total_ref = ref.get('total', {})
    r2_tol = ref.get('R2_tolerance', 0.005)
    mae_tol = ref.get('mae_tolerance', 0.0005)
    mse_tol = ref.get('mse_tolerance', 0.00001)
    elements = ['H', 'C', 'N', 'O', 'F']
    agent_atom = artifact.get('atom_types', {})
    agent_total = artifact.get('total', {})
    sub_scores = []
    for elem in elements:
        ref_vals = atom_types.get(elem, {})
        agent_vals = agent_atom.get(elem, {})
        if not agent_vals:
            sub_scores.append(0.0)
            continue
        r2_s = _score_r2(agent_vals.get('R2'), ref_vals.get('R2'), r2_tol)
        mae_s = _score_mae(agent_vals.get('MAE'), ref_vals.get('MAE'), mae_tol)
        mse_s = _score_mse(agent_vals.get('MSE'), ref_vals.get('MSE'), mse_tol)
        sub_scores.append((r2_s + mae_s + mse_s) / 3.0)
    # total
    if agent_total:
        r2_t = _score_r2(agent_total.get('R2'), total_ref.get('R2'), r2_tol)
        mae_t = _score_mae(agent_total.get('MAE'), total_ref.get('MAE'), mae_tol)
        mse_t = _score_mse(agent_total.get('MSE'), total_ref.get('MSE'), mse_tol)
        sub_scores.append((r2_t + mae_t + mse_t) / 3.0)
    if not sub_scores:
        return 0.0
    return sum(sub_scores) / len(sub_scores)


_SCORERS = {
    'fingerprints': score_0,
    'gaff_metrics': score_1,
    'dft_metrics': score_2,
    'transfer_metrics': score_3,
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
