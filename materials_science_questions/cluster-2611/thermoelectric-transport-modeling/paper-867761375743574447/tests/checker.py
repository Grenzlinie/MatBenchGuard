import os
import json
import csv

# === author imports / helpers ===
import os, csv, json, math
from collections import defaultdict


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
    ref_table = spec.get("reference_seebeck_xi", [])
    ref_by_mat = {r["material"]: r for r in ref_table}
    exp_series = spec.get("experimental_series", {})
    val_thr = spec.get("val_Al_Si_thresholds", {})
    return {"ref_by_mat": ref_by_mat, "exp_series": exp_series, "val_thr": val_thr}


# === block: score_0 (check id='check_seebeck') ===
def score_0(artifact, step, ctx):
    csv_path = os.path.join("/app/outputs", "seebeck_coefficients.csv")
    if not os.path.exists(csv_path):
        return 0.0
    with open(csv_path, newline='') as f:
        rows = list(csv.DictReader(f))
    if len(rows) < 14:
        return 0.0
    ref_by_mat = ctx["ref_by_mat"]
    scores = []
    for row in rows:
        mat = row["material"].strip()
        ref = ref_by_mat.get(mat)
        if ref is None:
            continue
        try:
            S = float(row["S_muV_per_K"])
            xi = float(row["xi_V_s0p5_per_J_cm2"])
        except (ValueError, KeyError):
            continue
        sign_score = 1.0 if (S > 0 and ref["S_gold"] > 0) or (S < 0 and ref["S_gold"] < 0) or (S == 0 and ref["S_gold"] == 0) else 0.0
        def mag_score(val, gold):
            if abs(gold) < 1e-9:
                return 1.0 if abs(val) < 1e-9 else 0.0
            ratio = abs(val - gold) / abs(gold)
            if ratio <= 0.5:
                return 1.0
            # decay: 0.5->0.0 linear
            return max(0.0, 1.0 - (ratio - 0.5) * 2.0)
        s_score = mag_score(S, ref["S_gold"])
        xi_score = mag_score(xi, ref["xi_gold"])
        row_score = sign_score * 0.5 + (s_score + xi_score) / 2.0 * 0.5
        scores.append(row_score)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_1 (check id='check_similarity') ===
def score_1(artifact, step, ctx):
    csv_path = os.path.join("/app/outputs", "seebeck_coefficients.csv")
    if not os.path.exists(csv_path):
        return 0.0
    with open(csv_path, newline='') as f:
        rows = list(csv.DictReader(f))
    if not rows:
        return 0.0
    # build material -> xi mapping
    xi_map = {}
    for row in rows:
        try:
            mat = row["material"].strip()
            xi = float(row["xi_V_s0p5_per_J_cm2"])
            xi_map[mat] = xi
        except (ValueError, KeyError):
            pass
    if not xi_map:
        return 0.0
    # sort descending xi to get agent ordering
    agent_order = sorted(xi_map.items(), key=lambda kv: kv[1], reverse=True)
    agent_rank = {mat: idx for idx, (mat, val) in enumerate(agent_order)}

    exp_series = ctx["exp_series"]
    def similarity_for_series(series):
        # filter materials present in both
        common = [m for m in series if m in agent_rank]
        if len(common) < 2:
            return 0.5  # neutral if insufficient
        pairs = []
        for i in range(len(common)):
            for j in range(i+1, len(common)):
                mat_a, mat_b = common[i], common[j]
                # in experimental series, common[i] comes before common[j]
                exp_order = (i < j)
                # agent order: higher xi first
                agent_hi_first = agent_rank[mat_a] < agent_rank[mat_b]
                pairs.append(1 if exp_order == agent_hi_first else 0)
        return sum(pairs) / len(pairs) if pairs else 0.5

    per_series = [similarity_for_series(exp_series[s]) for s in exp_series]
    if not per_series:
        return 0.0
    avg_sim = sum(per_series) / len(per_series)
    # threshold_or_better: if avg_sim >= 0.8, full credit; else linear decay from 0.8 down to 0.5
    if avg_sim >= 0.8:
        return 1.0
    elif avg_sim <= 0.5:
        return 0.0
    else:
        return (avg_sim - 0.5) / 0.3  # linearly from 0 at 0.5 to 1 at 0.8


# === block: score_2 (check id='check_validation_Al_Si') ===
def score_2(artifact, step, ctx):
    val_path = os.path.join("/app/outputs", "validation_Al_Si.txt")
    if not os.path.exists(val_path):
        return 0.0
    try:
        with open(val_path) as f:
            lines = f.read().strip().splitlines()
        err = {}
        for line in lines:
            if ':' in line:
                key, val = line.split(':', 1)
                key = key.strip()
                val = val.strip().rstrip('%')
                err[key] = float(val)
    except Exception:
        return 0.0
    thr = ctx["val_thr"]
    score = 0.0
    total = 0.0
    for mat_key, max_err_key in [("Al_rel_error", "Al_max_rel_error"), ("Si_rel_error", "Si_max_rel_error")]:
        if mat_key in err:
            total += 1.0
            val_abs = abs(err[mat_key])
            max_allowed = thr.get(max_err_key, 80.0)
            if val_abs <= max_allowed:
                score += 1.0
    if total == 0:
        return 0.0
    return score / total


_SCORERS = {
    'check_seebeck': score_0,
    'check_similarity': score_1,
    'check_validation_Al_Si': score_2,
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
