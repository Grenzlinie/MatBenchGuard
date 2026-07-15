import os
import json
import csv

# === author imports / helpers ===
import csv, math, os, json, sys


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
    T0_map = {3:0.340, 4:0.350, 5:0.380, 7:0.417}
    gold_chain_prob = {3:1.0, 4:1.0, 5:0.8, 6:0.6, 7:0.3, 8:0.0, 9:0.0}
    return {"T0_map": T0_map, "gold_chain_prob": gold_chain_prob}


# === block: score_0 (check id='energy_ratio') ===
def score_0(artifact, step, ctx):
    import math


    def virtual_chains_ratio(g, T_star, T0):
        eta = math.sqrt(T0 / T_star) * math.exp(1.0 / T0 - 1.0 / T_star)
        k_max = 2 * g - 5
        if k_max < 0:
            return 1.0
        num = 0.0
        den = 0.0
        eta_pow = 1.0
        max_bonds = 3 * g - 6
        for k in range(k_max + 1):
            coeff = max_bonds - k
            num += coeff * eta_pow
            den += eta_pow
            eta_pow *= eta
        if den == 0:
            return 1.0
        return num / ((g - 1) * den)


    T0_map = ctx["T0_map"]
    expected_g = [3, 4, 5, 7]
    counts = {g: 0 for g in expected_g}
    pass_rows = 0
    valid_rows = 0
    for row in artifact:
        try:
            g = int(row["g"])
            t = float(row["T_star"])
            ratio = float(row["ratio"])
        except (ValueError, KeyError):
            continue
        if g not in T0_map:
            continue
        if 0.42 <= t <= 0.71:
            counts[g] += 1
            expected = virtual_chains_ratio(g, t, T0_map[g])
            if abs(ratio - expected) <= 0.1:
                pass_rows += 1
            valid_rows += 1
    for g in expected_g:
        if counts.get(g, 0) < 5:
            return 0.0
    return pass_rows / max(1, valid_rows)


# === block: score_1 (check id='transition_temp') ===
def score_1(artifact, step, ctx):
    T0_map = ctx["T0_map"]
    correct = set()
    for row in artifact:
        try:
            g = int(row["g"])
            t0 = float(row["T0_star"])
        except (ValueError, KeyError):
            continue
        if g in T0_map and abs(t0 - T0_map[g]) <= 0.02:
            correct.add(g)
    return len(correct) / len(T0_map)


# === block: score_2 (check id='chain_prob') ===
def score_2(artifact, step, ctx):
    gold = ctx["gold_chain_prob"]
    seen = set()
    correct = 0
    total = 7  # g=3..9
    for row in artifact:
        try:
            g = int(row["g"])
            p1 = float(row["P1"])
        except (ValueError, KeyError):
            continue
        if g in gold and g not in seen:
            seen.add(g)
            if abs(p1 - gold[g]) <= 0.1:
                correct += 1
    return correct / total


# === block: score_3 (check id='rdf_g6') ===
def score_3(artifact, step, ctx):
    r_star = []
    G = []
    for row in artifact:
        try:
            rs = float(row["r_star"])
            gv = float(row["G"])
            r_star.append(rs)
            G.append(gv)
        except (ValueError, KeyError):
            continue
    if not r_star:
        return 0.0
    best_rs = None
    best_g = -1
    for rs, gv in zip(r_star, G):
        if 0.5 <= rs <= 1.5 and gv > best_g:
            best_g = gv
            best_rs = rs
    peak_score = 0.0
    height_score = 0.0
    if best_rs is not None:
        if abs(best_rs - 1.0) <= 0.05:
            peak_score = 1.0
        if abs(best_g - 1.5) <= 0.3:
            height_score = 1.0
    plateau_vals = [gv for rs, gv in zip(r_star, G) if 2.0 <= rs <= 3.0]
    plateau_score = 0.0
    if plateau_vals:
        mean_g = sum(plateau_vals) / len(plateau_vals)
        if 0.1 <= mean_g <= 0.4:
            plateau_score = 1.0
    return 0.4 * peak_score + 0.4 * height_score + 0.2 * plateau_score


_SCORERS = {
    'energy_ratio': score_0,
    'transition_temp': score_1,
    'chain_prob': score_2,
    'rdf_g6': score_3,
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
