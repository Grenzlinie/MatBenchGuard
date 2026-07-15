import os
import json
import csv

# === author imports / helpers ===
import json, math, csv, os
from collections import defaultdict

def compute_stats(depths):
    mpr = sum(depths) / len(depths)
    variance = sum((d - mpr)**2 for d in depths) / len(depths)
    sigma = math.sqrt(variance)
    return mpr, sigma

def score_traj(step, ctx):
    traj_data = ctx.get("traj_data", {})
    gold_conditions = step["gold"]
    tol_mpr = step.get("tol_mpr", 0.10)
    tol_sigma = step.get("tol_sigma", 0.20)
    scores = []
    for cond in gold_conditions:
        energy = cond["energy"]
        conc = cond.get("concentration", None)
        depths = traj_data.get((energy, conc), [])
        if not depths:
            scores.append(0.0)
            continue
        mpr_recomp, sigma_recomp = compute_stats(depths)
        mpr_gold = cond["mpr"]
        sigma_gold = cond["sigma"]
        mpr_rel_err = abs(mpr_recomp - mpr_gold) / max(mpr_gold, 1e-6)
        sigma_rel_err = abs(sigma_recomp - sigma_gold) / max(sigma_gold, 1e-6)
        mpr_score = max(0.0, 1.0 - mpr_rel_err / tol_mpr)
        sigma_score = max(0.0, 1.0 - sigma_rel_err / tol_sigma)
        scores.append((mpr_score + sigma_score) / 2.0)
    return sum(scores) / len(scores) if scores else 0.0

def score_crosscheck(step, ctx, artifact):
    traj_data = ctx.get("traj_data", {})
    if not traj_data or not artifact:
        return 0.0
    agent_lookup = {}
    for row in artifact:
        try:
            e = float(row.get("energy", float('nan')))
            c = float(row.get("concentration", float('nan')))
            mpr = float(row.get("mpr", float('nan')))
            sigma = float(row.get("sigma", float('nan')))
            if math.isnan(e) or math.isnan(c) or math.isnan(mpr) or math.isnan(sigma):
                continue
            agent_lookup[(e, c)] = (mpr, sigma)
        except (ValueError, KeyError):
            continue
    tol = step.get("tol_relative", 0.1)
    ok = 0
    total = 0
    for (energy, conc), depths in traj_data.items():
        if not depths:
            continue
        mpr_recomp, sigma_recomp = compute_stats(depths)
        key = (energy, conc)
        total += 1
        if key in agent_lookup:
            agent_mpr, agent_sigma = agent_lookup[key]
            mpr_ok = abs(agent_mpr - mpr_recomp) <= tol * max(abs(mpr_recomp), 1e-6)
            sigma_ok = abs(agent_sigma - sigma_recomp) <= tol * max(abs(sigma_recomp), 1e-6)
            if mpr_ok and sigma_ok:
                ok += 1
    return ok / total if total > 0 else 0.0

def score_ratio(step, ctx):
    traj_data = ctx.get("traj_data", {})
    energies = sorted([e for (e, c) in traj_data if c == 0.0 and traj_data[(e, c)]])
    if len(energies) < 2:
        return 0.0
    ratios = []
    for energy in energies:
        depths = traj_data[(energy, 0.0)]
        mpr_recomp, sigma_recomp = compute_stats(depths)
        ratio = sigma_recomp / mpr_recomp
        ratios.append(ratio)
    mean_ratio = sum(ratios) / len(ratios)
    tol_dev = step.get("tol_deviation", 0.2)
    ok = sum(1 for r in ratios if r >= mean_ratio * (1 - tol_dev) and r <= mean_ratio * (1 + tol_dev))
    return ok / len(ratios)


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
    traj_data = defaultdict(list)
    aSi_path = os.path.join(outputs_dir, "trajectories_aSi.jsonl")
    if os.path.isfile(aSi_path):
        with open(aSi_path) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                rec = json.loads(line)
                energy = float(rec["energy"])
                depth = float(rec["depth"])
                traj_data[(energy, 0.0)].append(depth)
    aSiH30_path = os.path.join(outputs_dir, "trajectories_aSiH30.jsonl")
    if os.path.isfile(aSiH30_path):
        with open(aSiH30_path) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                rec = json.loads(line)
                energy = float(rec["energy"])
                depth = float(rec["depth"])
                traj_data[(energy, 0.3)].append(depth)
    conc_path = os.path.join(outputs_dir, "trajectories_concsweep.jsonl")
    if os.path.isfile(conc_path):
        with open(conc_path) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                rec = json.loads(line)
                energy = float(rec["energy"])
                conc = float(rec["concentration"])
                depth = float(rec["depth"])
                traj_data[(energy, conc)].append(depth)
    return {"traj_data": dict(traj_data)}


# === block: score_0 (check id='step_trajectories_aSi') ===
def score_0(artifact, step, ctx):
    return score_traj(step, ctx)


# === block: score_1 (check id='step_trajectories_aSiH30') ===
def score_1(artifact, step, ctx):
    return score_traj(step, ctx)


# === block: score_2 (check id='step_concsweep') ===
def score_2(artifact, step, ctx):
    return score_traj(step, ctx)


# === block: score_3 (check id='step_summary_crosscheck') ===
def score_3(artifact, step, ctx):
    return score_crosscheck(step, ctx, artifact)


# === block: score_4 (check id='step_ratio_aSi') ===
def score_4(artifact, step, ctx):
    return score_ratio(step, ctx)


_SCORERS = {
    'step_trajectories_aSi': score_0,
    'step_trajectories_aSiH30': score_1,
    'step_concsweep': score_2,
    'step_summary_crosscheck': score_3,
    'step_ratio_aSi': score_4,
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
