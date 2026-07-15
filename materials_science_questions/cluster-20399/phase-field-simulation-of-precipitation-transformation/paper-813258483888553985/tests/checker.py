import os
import json
import csv

# === author imports / helpers ===
import math
import statistics
from collections import defaultdict

def spearman_r(x, y):
    n = len(x)
    if n < 2:
        return 0.0
    # rank x
    x_sorted = sorted((v, i) for i, v in enumerate(x))
    ranks_x = [0] * n
    for rank, (v, i) in enumerate(x_sorted):
        ranks_x[i] = rank + 1
    # rank y
    y_sorted = sorted((v, i) for i, v in enumerate(y))
    ranks_y = [0] * n
    for rank, (v, i) in enumerate(y_sorted):
        ranks_y[i] = rank + 1
    mean_rx = statistics.mean(ranks_x)
    mean_ry = statistics.mean(ranks_y)
    cov = sum((rx - mean_rx) * (ry - mean_ry) for rx, ry in zip(ranks_x, ranks_y))
    varx = sum((rx - mean_rx) ** 2 for rx in ranks_x)
    vary = sum((ry - mean_ry) ** 2 for ry in ranks_y)
    if varx == 0 or vary == 0:
        return 0.0
    return cov / (math.sqrt(varx) * math.sqrt(vary))


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


# === block: score_0 (check id='tension_power_law') ===
def score_0(artifact, step, ctx):
    artifact = artifact  # list of dicts from CSV
    step = step  # grading step dict

    if not artifact or not all(k in artifact[0] for k in ('l_d', 't_d', 'epsilon_u_bar', 'epsilon_u_0')):
        return 0.0

    try:
        l_d = [float(r['l_d']) for r in artifact]
        t_d = [float(r['t_d']) for r in artifact]
        eps_u = [float(r['epsilon_u_bar']) for r in artifact]
        eps_u_0_vals = [float(r['epsilon_u_0']) for r in artifact]
    except (ValueError, KeyError):
        return 0.0

    eps_u_0 = statistics.mean(eps_u_0_vals)
    if eps_u_0 <= 0:
        return 0.0

    beta_i = []
    for i in range(len(artifact)):
        l_ratio = l_d[i]
        t_ratio = t_d[i]
        eu_bar = eps_u[i]
        if l_ratio <= 1e-12 or t_ratio <= 0 or eu_bar <= 0:
            return 0.0
        if l_ratio == 1.0:
            continue
        num = math.log(eu_bar / eps_u_0)
        den = math.log(1.0 / l_ratio)
        bi = num / den * t_ratio
        beta_i.append(bi)

    if not beta_i:
        return 0.0

    beta = statistics.mean(beta_i)

    pred = []
    for i in range(len(artifact)):
        l_ratio = l_d[i]
        t_ratio = t_d[i]
        pred_val = eps_u_0 * (1.0 / l_ratio) ** (beta / t_ratio) if l_ratio > 0 else eps_u_0
        pred.append(pred_val)

    mean_y = statistics.mean(eps_u)
    ss_res = sum((y - f) ** 2 for y, f in zip(eps_u, pred))
    ss_tot = sum((y - mean_y) ** 2 for y in eps_u)
    if ss_tot == 0:
        r2 = 1.0
    else:
        r2 = 1.0 - ss_res / ss_tot

    target_beta = step.get('hidden', {}).get('target_beta', 0.37)
    beta_tol = step.get('hidden', {}).get('beta_tolerance', 0.15)
    beta_score = 1.0 if abs(beta - target_beta) <= beta_tol else 0.0

    r2_thresh = step.get('hidden', {}).get('r2_threshold', 0.85)
    if r2 >= r2_thresh:
        r2_score = 1.0
    elif r2 >= r2_thresh - 0.1:
        r2_score = (r2 - (r2_thresh - 0.1)) / 0.1
    else:
        r2_score = 0.0

    groups = defaultdict(list)
    for i in range(len(artifact)):
        groups[t_d[i]].append((l_d[i], eps_u[i]))

    monotonic_ok = True
    for td, pairs in groups.items():
        if len(pairs) < 2:
            continue
        ls = [p[0] for p in pairs]
        us = [p[1] for p in pairs]
        rho = spearman_r(ls, us)
        if rho > -0.5:
            monotonic_ok = False
            break

    monotonic_score = 1.0 if monotonic_ok else 0.0

    score = 0.4 * beta_score + 0.4 * r2_score + 0.2 * monotonic_score
    return max(0.0, min(1.0, score))


# === block: score_1 (check id='bending_trend') ===
def score_1(artifact, step, ctx):
    artifact = artifact
    step = step

    if not artifact or not all(k in artifact[0] for k in ('l_d', 't_d', 'epsilon_s')):
        return 0.0

    try:
        l_d = [float(r['l_d']) for r in artifact]
        t_d = [float(r['t_d']) for r in artifact]
        eps_s = [float(r['epsilon_s']) for r in artifact]
    except (ValueError, KeyError):
        return 0.0

    groups = defaultdict(list)
    for i in range(len(artifact)):
        groups[t_d[i]].append((l_d[i], eps_s[i]))

    ok = False
    for td, pairs in groups.items():
        if len(pairs) >= 2:
            ls = [p[0] for p in pairs]
            es = [p[1] for p in pairs]
            rho = spearman_r(ls, es)
            if rho <= -0.5:
                ok = True
                break

    return 1.0 if ok else 0.0


_SCORERS = {
    'tension_power_law': score_0,
    'bending_trend': score_1,
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
