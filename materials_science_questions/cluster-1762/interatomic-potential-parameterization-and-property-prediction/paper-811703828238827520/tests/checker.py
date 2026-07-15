import os
import json
import csv

# === author imports / helpers ===
import csv

def _score_ft(rows):
    if not rows or len(rows) < 10:
        return 0.0
    try:
        R_vals = [float(r['R']) for r in rows]
        mag_vals = [float(r['FT_magnitude']) for r in rows]
    except (KeyError, ValueError):
        return 0.0
    peak1 = max([m for r, m in zip(R_vals, mag_vals) if 1.0 <= r <= 2.2], default=0.0)
    peak2 = max([m for r, m in zip(R_vals, mag_vals) if 2.8 <= r <= 4.0], default=0.0)
    max_mag = max(mag_vals) if mag_vals else 1.0
    if max_mag == 0:
        return 0.0
    score = 0.0
    if peak1 > 0.01 * max_mag and peak2 > 0.01 * max_mag:
        score += 0.5
    if peak1 > peak2:
        score += 0.3
    if len(R_vals) >= 50:
        score += 0.2
    return min(1.0, score)


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
    return {"gold_struct": spec.get("gold_struct", [])}


# === block: score_0 (check id='struct_params') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    gold = ctx["gold_struct"]
    gold_lookup = {}
    for g in gold:
        key = (float(g["temperature"]), g["shell"].strip().lower())
        gold_lookup[key] = g
    total = len(gold)
    passed = 0
    tolerance_R = 0.01
    tolerance_sigma2 = 0.001
    for g in gold:
        key = (float(g["temperature"]), g["shell"].strip().lower())
        agent_row = None
        for r in rows:
            try:
                temp = float(r["temperature"])
                shell = r["shell"].strip().lower()
            except (ValueError, KeyError):
                continue
            if temp == key[0] and shell == key[1]:
                agent_row = r
                break
        if agent_row is None:
            continue
        try:
            N_agent = float(agent_row["N"])
            R_agent = float(agent_row["R"])
            sigma2_agent = float(agent_row["sigma2"])
        except (ValueError, KeyError):
            continue
        N_gold = float(g["N"])
        if abs(N_agent - N_gold) > 0.01:
            continue
        if abs(R_agent - float(g["R"])) > tolerance_R:
            continue
        if abs(sigma2_agent - float(g["sigma2"])) > tolerance_sigma2:
            continue
        passed += 1
    struct_score = passed / total if total > 0 else 0.0

    # Temperature trend check (stolen from removed ft_trend scorer, implemented with stdlib only)
    import os
    import csv


    def _load_peak(filename):
        path = os.path.join('/app/outputs', filename)
        with open(path, newline='') as f:
            reader = csv.DictReader(f)
            rows2 = list(reader)
        if not rows2:
            raise ValueError("Empty file")
        mags = []
        for r in rows2:
            R_val = float(r['R'])
            if 1.0 <= R_val <= 2.2:
                mags.append(float(r['FT_magnitude']))
        return max(mags) if mags else 0.0


    try:
        filename_180 = 'exafs_ft_180K.csv'
        filename_300 = 'exafs_ft_300K.csv'
        filename_400 = 'exafs_ft_400K.csv'
        a180 = _load_peak(filename_180)
        a300 = _load_peak(filename_300)
        a400 = _load_peak(filename_400)
        if a180 > a300 > a400:
            trend_score = 1.0
        elif a180 > a400 and a300 > a400:
            trend_score = 0.6
        elif a180 > a400:
            trend_score = 0.3
        else:
            trend_score = 0.0
    except Exception:
        trend_score = 0.0

    # Combine struct (weight 0.3) and trend (weight 0.1) into a single score, ratio 3:1
    combined = struct_score * 0.75 + trend_score * 0.25
    return combined


# === block: score_1 (check id='ft_180') ===
def score_1(artifact, step, ctx):
    return _score_ft(artifact)


# === block: score_2 (check id='ft_300') ===
def score_2(artifact, step, ctx):
    return _score_ft(artifact)


# === block: score_3 (check id='ft_400') ===
def score_3(artifact, step, ctx):
    return _score_ft(artifact)


# === block: score_4 (check id='ft_trend') ===
def score_4(artifact, step, ctx):
    import csv
    import numpy as np

    def _load_peak(filename):
        path = f'/app/outputs/{filename}'
        with open(path, newline='') as f:
            reader = csv.DictReader(f)
            rows2 = list(reader)
        if not rows2:
            raise ValueError("Empty file")
        R = np.array([float(r['R']) for r in rows2])
        mag = np.array([float(r['FT_magnitude']) for r in rows2])
        mask = (R >= 1.0) & (R <= 2.2)
        return np.max(mag[mask]) if np.any(mask) else 0.0

    amps = []
    for fname in ['exafs_ft_180K.csv', 'exafs_ft_300K.csv', 'exafs_ft_400K.csv']:
        try:
            amps.append(_load_peak(fname))
        except Exception:
            return 0.0
    a180, a300, a400 = amps
    if a180 > a300 > a400:
        return 1.0
    elif a180 > a400 and a300 > a400:
        return 0.6
    elif a180 > a400:
        return 0.3
    else:
        return 0.0


_SCORERS = {
    'struct_params': score_0,
    'ft_180': score_1,
    'ft_300': score_2,
    'ft_400': score_3,
    'ft_trend': score_4,
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
