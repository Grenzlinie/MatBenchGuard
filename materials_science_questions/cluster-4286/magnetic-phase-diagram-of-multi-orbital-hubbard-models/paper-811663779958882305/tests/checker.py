import os
import json
import csv

# === author imports / helpers ===
import numpy as np
import json


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
    L = 6
    N = L*L
    a1 = np.array([1.0, 0.0])
    a2 = np.array([0.5, np.sqrt(3)/2])
    l1, l2 = np.mgrid[0:L, 0:L]
    l1 = l1.flatten()
    l2 = l2.flatten()
    pos = l1[:, None] * a1 + l2[:, None] * a2
    dist_sq = np.sum(pos**2, axis=1)
    min_dist = np.min(dist_sq[dist_sq > 1e-9])
    neighbor_indices = np.where(np.abs(dist_sq - min_dist) < 1e-6)[0].tolist()
    ctx = {
      "lattice_positions_int": np.column_stack([l1, l2]),
      "neighbor_indices": neighbor_indices
    }
    return ctx


# === block: score_0 (check id='half_filling_JAF0') ===
def score_0(artifact, step, ctx):
    params = step["params"]
    gold_positions = params["gold_peak_positions"]
    gold_vals = params["gold_peak_values"]
    tol_peak = params["tolerance_peak"]
    tol_nb = params.get("tolerance_neighbor", 0.05)
    peak_weight = params.get("peak_weight", 0.8)
    neighbor_weight = params.get("neighbor_weight", 0.2)
    neighbor_sign = params.get("neighbor_sign_check", False)
    gold_nb = params.get("gold_neighbor_corr", None)

    corr = np.array(artifact["spin_spin_correlations"])
    lattice_int = ctx["lattice_positions_int"]
    L = 6
    N = 36
    S_q = {}
    for m in range(L):
        for n in range(L):
            phase = np.exp(2j * np.pi * (m * lattice_int[:, 0] + n * lattice_int[:, 1]) / L)
            S_q[m, n] = np.sum(corr * phase) / N
    peak_scores = []
    for pos, gval in zip(gold_positions, gold_vals):
        m, n = pos
        Sq_val = np.abs(S_q[m, n])
        diff = abs(Sq_val - gval)
        score_i = max(0.0, 1.0 - diff / tol_peak)
        peak_scores.append(score_i)
    avg_peak = np.mean(peak_scores)
    neighbor_indices = ctx["neighbor_indices"]
    neighbor_corr = np.mean(corr[neighbor_indices])
    if gold_nb is not None:
        diff_nb = abs(neighbor_corr - gold_nb)
        nb_score = max(0.0, 1.0 - diff_nb / tol_nb)
    elif neighbor_sign:
        nb_score = 1.0 if neighbor_corr > 0 else 0.0
    else:
        nb_score = 1.0
    score = avg_peak * peak_weight + nb_score * neighbor_weight
    return float(score)


# === block: score_1 (check id='half_filling_JAF01') ===
def score_1(artifact, step, ctx):
    params = step["params"]
    gold_positions = params["gold_peak_positions"]
    gold_vals = params["gold_peak_values"]
    tol_peak = params["tolerance_peak"]
    peak_weight = params.get("peak_weight", 1.0)
    neighbor_weight = params.get("neighbor_weight", 0.0)
    neighbor_sign = params.get("neighbor_sign_check", False)
    gold_nb = params.get("gold_neighbor_corr", None)

    corr = np.array(artifact["spin_spin_correlations"])
    lattice_int = ctx["lattice_positions_int"]
    L = 6
    N = 36
    S_q = {}
    for m in range(L):
        for n in range(L):
            phase = np.exp(2j * np.pi * (m * lattice_int[:, 0] + n * lattice_int[:, 1]) / L)
            S_q[m, n] = np.sum(corr * phase) / N
    peak_scores = []
    for pos, gval in zip(gold_positions, gold_vals):
        m, n = pos
        Sq_val = np.abs(S_q[m, n])
        diff = abs(Sq_val - gval)
        score_i = max(0.0, 1.0 - diff / tol_peak)
        peak_scores.append(score_i)
    avg_peak = np.mean(peak_scores)
    neighbor_indices = ctx["neighbor_indices"]
    neighbor_corr = np.mean(corr[neighbor_indices])
    if gold_nb is not None:
        diff_nb = abs(neighbor_corr - gold_nb)
        nb_score = max(0.0, 1.0 - diff_nb / tol_peak)  # use same tol
    elif neighbor_sign:
        nb_score = 1.0 if neighbor_corr > 0 else 0.0
    else:
        nb_score = 1.0
    score = avg_peak * peak_weight + nb_score * neighbor_weight
    return float(score)


# === block: score_2 (check id='quarter_filling_JAF0') ===
def score_2(artifact, step, ctx):
    params = step["params"]
    gold_positions = params["gold_peak_positions"]
    gold_vals = params["gold_peak_values"]
    tol_peak = params["tolerance_peak"]
    peak_weight = params.get("peak_weight", 0.8)
    neighbor_weight = params.get("neighbor_weight", 0.2)
    neighbor_sign = params.get("neighbor_sign_check", False)
    gold_nb = params.get("gold_neighbor_corr", None)

    corr = np.array(artifact["spin_spin_correlations"])
    lattice_int = ctx["lattice_positions_int"]
    L = 6
    N = 36
    S_q = {}
    for m in range(L):
        for n in range(L):
            phase = np.exp(2j * np.pi * (m * lattice_int[:, 0] + n * lattice_int[:, 1]) / L)
            S_q[m, n] = np.sum(corr * phase) / N
    peak_scores = []
    for pos, gval in zip(gold_positions, gold_vals):
        m, n = pos
        Sq_val = np.abs(S_q[m, n])
        diff = abs(Sq_val - gval)
        score_i = max(0.0, 1.0 - diff / tol_peak)
        peak_scores.append(score_i)
    avg_peak = np.mean(peak_scores)
    neighbor_indices = ctx["neighbor_indices"]
    neighbor_corr = np.mean(corr[neighbor_indices])
    if gold_nb is not None:
        diff_nb = abs(neighbor_corr - gold_nb)
        nb_score = max(0.0, 1.0 - diff_nb / tol_peak)
    elif neighbor_sign:
        nb_score = 1.0 if neighbor_corr > 0 else 0.0
    else:
        nb_score = 1.0
    score = avg_peak * peak_weight + nb_score * neighbor_weight
    return float(score)


# === block: score_3 (check id='quarter_filling_JAF01') ===
def score_3(artifact, step, ctx):
    params = step["params"]
    gold_positions = params["gold_peak_positions"]
    gold_vals = params["gold_peak_values"]
    tol_peak = params["tolerance_peak"]
    tol_nb = params.get("tolerance_neighbor", 0.05)
    peak_weight = params.get("peak_weight", 0.8)
    neighbor_weight = params.get("neighbor_weight", 0.2)
    neighbor_sign = params.get("neighbor_sign_check", False)
    gold_nb = params.get("gold_neighbor_corr", None)

    corr = np.array(artifact["spin_spin_correlations"])
    lattice_int = ctx["lattice_positions_int"]
    L = 6
    N = 36
    S_q = {}
    for m in range(L):
        for n in range(L):
            phase = np.exp(2j * np.pi * (m * lattice_int[:, 0] + n * lattice_int[:, 1]) / L)
            S_q[m, n] = np.sum(corr * phase) / N
    peak_scores = []
    for pos, gval in zip(gold_positions, gold_vals):
        m, n = pos
        Sq_val = np.abs(S_q[m, n])
        diff = abs(Sq_val - gval)
        score_i = max(0.0, 1.0 - diff / tol_peak)
        peak_scores.append(score_i)
    avg_peak = np.mean(peak_scores)
    neighbor_indices = ctx["neighbor_indices"]
    neighbor_corr = np.mean(corr[neighbor_indices])
    if gold_nb is not None:
        diff_nb = abs(neighbor_corr - gold_nb)
        nb_score = max(0.0, 1.0 - diff_nb / tol_nb)
    elif neighbor_sign:
        nb_score = 1.0 if neighbor_corr > 0 else 0.0
    else:
        nb_score = 1.0
    score = avg_peak * peak_weight + nb_score * neighbor_weight
    return float(score)


_SCORERS = {
    'half_filling_JAF0': score_0,
    'half_filling_JAF01': score_1,
    'quarter_filling_JAF0': score_2,
    'quarter_filling_JAF01': score_3,
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
