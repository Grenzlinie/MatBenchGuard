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


# === block: score_0 (check id='step_03_mu2d_check') ===
def score_0(artifact, step, ctx):
    ref_T = step['reference_T']
    ref_mu = step['reference_mu']
    mape_thresh = step['mape_threshold']
    decay = step.get('decay_factor', 0.4)
    if not artifact:
        return 0.0
    T_map = {}
    for row in artifact:
        T = float(row['T'])
        mu = float(row['mu_2D'])
        T_map[T] = mu
    ts = sorted(T_map.keys())
    def get_mu_at(T):
        if T in T_map:
            return T_map[T]
        if not ts:
            return None
        idx = 0
        for i, t in enumerate(ts):
            if t >= T:
                idx = i
                break
        if idx == 0:
            return T_map[ts[0]] if abs(ts[0]-T) <= 0.015 else None
        if idx >= len(ts):
            return T_map[ts[-1]] if abs(ts[-1]-T) <= 0.015 else None
        t0, t1 = ts[idx-1], ts[idx]
        mu0, mu1 = T_map[t0], T_map[t1]
        if (t1 - t0) == 0:
            return None
        return mu0 + (mu1 - mu0) * (T - t0) / (t1 - t0)
    relative_errors = []
    for T_target, mu_target in zip(ref_T, ref_mu):
        mu_agent = get_mu_at(T_target)
        if mu_agent is None:
            relative_errors.append(1.0)
        else:
            rel_err = abs(mu_agent - mu_target) / mu_target if mu_target != 0 else 0.0
            relative_errors.append(rel_err)
    if not relative_errors:
        return 0.0
    mape = sum(relative_errors) / len(relative_errors)
    if mape <= mape_thresh:
        return 1.0
    else:
        return max(0.0, 1.0 - (mape - mape_thresh) / decay)


# === block: score_1 (check id='step_04a_ns_point') ===
def score_1(artifact, step, ctx):
    target_n_gas = step['target_n_gas']
    target_T = step['target_T']
    target_comp = step['target_component']
    ref_ns = step['reference_ns']
    tol_rel = step['tolerance_relative']
    decay = step.get('decay_factor', 0.5)
    if not artifact:
        return 0.0
    best_ns = None
    best_dT = None
    for row in artifact:
        ng = float(row['n_gas'])
        comp = row['component'].strip().lower()
        T2 = float(row['T'])
        ns = float(row['n_s'])
        if ng != target_n_gas or comp != target_comp:
            continue
        dT = abs(T2 - target_T)
        if best_ns is None or dT < best_dT:
            best_ns = ns
            best_dT = dT
    if best_ns is None:
        return 0.0
    rel_err = abs(best_ns - ref_ns) / ref_ns if ref_ns != 0 else 0.0
    if rel_err <= tol_rel:
        return 1.0
    else:
        return max(0.0, 1.0 - (rel_err - tol_rel) / decay)


# === block: score_2 (check id='step_04b_ns_structure') ===
def score_2(artifact, step, ctx):
    sat_targets = step['sat_targets']
    sat_tol = step['sat_tolerance_relative']
    if not artifact:
        return 0.0
    groups = {}
    for row in artifact:
        ng = row['n_gas']
        comp = row['component'].strip().lower()
        T = float(row['T'])
        ns = float(row['n_s'])
        key = (ng, comp)
        if key not in groups:
            groups[key] = []
        groups[key].append((T, ns))
    if not groups:
        return 0.0
    mono_ok = 0
    total = 0
    sat_ok = 0
    sat_total = 0
    for key, points in groups.items():
        points_sorted = sorted(points, key=lambda x: x[0])
        nss = [ns for _, ns in points_sorted]
        total += 1
        if all(nss[i] >= nss[i+1] - 1e-10 for i in range(len(nss)-1)):
            mono_ok += 1
        _, comp = key
        if comp in sat_targets:
            sat_total += 1
            ns_low = nss[0]
            target = sat_targets[comp]
            err = abs(ns_low - target) / (target if target != 0 else 1.0)
            if err <= sat_tol:
                sat_ok += 1
    mono_score = mono_ok / total if total > 0 else 1.0
    sat_score = sat_ok / sat_total if sat_total > 0 else 1.0
    return 0.5 * mono_score + 0.5 * sat_score


# === block: score_3 (check id='step_05_kt_check') ===
def score_3(artifact, step, ctx):
    targets = step['targets']
    tol_rel = step['tolerance_relative']
    decay = step.get('decay_factor', 0.4)
    if not artifact or not isinstance(artifact, dict):
        return 0.0
    scores = []
    for comp in ['mixture', 'single']:
        if comp not in artifact:
            scores.append(0.0)
            continue
        val = float(artifact[comp])
        tgt = targets[comp]
        rel_err = abs(val - tgt) / tgt if tgt != 0 else 0.0
        if rel_err <= tol_rel:
            scores.append(1.0)
        else:
            scores.append(max(0.0, 1.0 - (rel_err - tol_rel) / decay))
    return sum(scores) / len(scores)


_SCORERS = {
    'step_03_mu2d_check': score_0,
    'step_04a_ns_point': score_1,
    'step_04b_ns_structure': score_2,
    'step_05_kt_check': score_3,
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
