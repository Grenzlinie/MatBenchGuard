import os
import json
import csv

# === author imports / helpers ===
import os, csv, math, json


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


# === block: score_0 (check id='dft_total_energy') ===
def score_0(artifact, step, ctx):
    data = artifact
    gold = step["config"]["gold"]
    # widened tolerance for cross-code reproduction (reviewer-requested)
    tol = 0.005
    def elem_score(val, ref, t):
        diff = abs(val - ref)
        if diff <= t:
            return 1.0
        elif diff <= 3*t:
            return 0.5
        else:
            return 0.0
    score_Co = elem_score(data["Co"], gold["Co"], tol)
    score_Cr = elem_score(data["Cr"], gold["Cr"], tol)
    return 0.5*score_Co + 0.5*score_Cr


# === block: score_1 (check id='new_phase_diagram_accuracy') ===
def score_1(artifact, step, ctx):
    rows = artifact
    cfg = step["config"]
    rng = cfg["composition_range"]
    gl = cfg["gold_left"]
    gm = cfg["gold_mid"]
    gr = cfg["gold_right"]
    max_dev = cfg["max_avg_deviation"]
    errors = []
    for row in rows:
        try:
            x = float(row["Mole_fraction_Cr"])
            T = float(row["Temperature_K"])
        except:
            continue
        if x < rng[0] or x > rng[1]:
            continue
        phase = row.get("Phase","")
        if "SIGMA" not in phase.upper():
            continue
        if gl["x0"] <= x <= gl["x1"]:
            goldT = gl["T0"] + (gl["T1"] - gl["T0"]) * (x - gl["x0"]) / (gl["x1"] - gl["x0"])
        elif gm["x0"] <= x <= gm["x1"]:
            goldT = gm["T0"]
        elif gr["x0"] <= x <= gr["x1"]:
            goldT = gr["T0"] + (gr["T1"] - gr["T0"]) * (x - gr["x0"]) / (gr["x1"] - gr["x0"])
        else:
            continue
        errors.append(abs(T - goldT))
    if not errors:
        return 1.0
    avg_dev = sum(errors) / len(errors)
    return max(0.0, min(1.0, 1.0 - (avg_dev - 20.0) / 20.0))


# === block: score_2 (check id='old_phase_diagram_accuracy') ===
def score_2(artifact, step, ctx):
    rows = artifact
    cfg = step["config"]
    rng = cfg["composition_range"]
    gl = cfg["gold_left"]
    gm = cfg["gold_mid"]
    gr = cfg["gold_right"]
    max_dev = cfg["max_avg_deviation"]
    errors = []
    for row in rows:
        try:
            x = float(row["Mole_fraction_Cr"])
            T = float(row["Temperature_K"])
        except:
            continue
        if x < rng[0] or x > rng[1]:
            continue
        phase = row.get("Phase","")
        if "SIGMA" not in phase.upper():
            continue
        if gl["x0"] <= x <= gl["x1"]:
            goldT = gl["T0"] + (gl["T1"] - gl["T0"]) * (x - gl["x0"]) / (gl["x1"] - gl["x0"])
        elif gm["x0"] <= x <= gm["x1"]:
            goldT = gm["T0"]
        elif gr["x0"] <= x <= gr["x1"]:
            goldT = gr["T0"] + (gr["T1"] - gr["T0"]) * (x - gr["x0"]) / (gr["x1"] - gr["x0"])
        else:
            continue
        errors.append(abs(T - goldT))
    if not errors:
        return 1.0
    avg_dev = sum(errors) / len(errors)
    return max(0.0, min(1.0, 1.0 - (avg_dev - 20.0) / 20.0))


# === block: score_3 (check id='trend_new_better_than_old') ===
def score_3(artifact, step, ctx):
    def _compute_avg_dev(rows, cfg):
        rng = cfg.get("composition_range", [0.5,0.8])
        gl = cfg.get("gold_left", {})
        gm = cfg.get("gold_mid", {})
        gr = cfg.get("gold_right", {})
        errs = []
        for row in rows:
            try:
                x = float(row["Mole_fraction_Cr"])
                T = float(row["Temperature_K"])
            except:
                continue
            if x < rng[0] or x > rng[1]:
                continue
            phase = row.get("Phase","")
            if "SIGMA" not in phase.upper():
                continue
            if gl and gl["x0"] <= x <= gl["x1"]:
                goldT = gl["T0"] + (gl["T1"] - gl["T0"]) * (x - gl["x0"]) / (gl["x1"] - gl["x0"])
            elif gm and gm["x0"] <= x <= gm["x1"]:
                goldT = gm["T0"]
            elif gr and gr["x0"] <= x <= gr["x1"]:
                goldT = gr["T0"] + (gr["T1"] - gr["T0"]) * (x - gr["x0"]) / (gr["x1"] - gr["x0"])
            else:
                continue
            errs.append(abs(T - goldT))
        if not errs:
            return 0.0
        return sum(errs) / len(errs)

    import csv
    new_rows = []
    old_rows = []
    try:
        with open("/app/outputs/new_model_phase_diagram.csv", newline="") as f:
            new_rows = list(csv.DictReader(f))
    except:
        pass
    try:
        with open("/app/outputs/old_model_phase_diagram.csv", newline="") as f:
            old_rows = list(csv.DictReader(f))
    except:
        pass

    new_cfg = {
        "composition_range": [0.5, 0.8],
        "gold_left": {"x0":0.45, "T0":610.0, "x1":0.55, "T1":1773.0},
        "gold_mid":  {"x0":0.55, "T0":1773.0, "x1":0.65, "T1":1773.0},
        "gold_right":{"x0":0.65, "T0":1773.0, "x1":0.75, "T1":800.0}
    }
    old_cfg = {
        "composition_range": [0.5, 0.8],
        "gold_left": {"x0":0.45, "T0":650.0, "x1":0.54, "T1":1800.0},
        "gold_mid":  {"x0":0.54, "T0":1800.0, "x1":0.64, "T1":1800.0},
        "gold_right":{"x0":0.64, "T0":1800.0, "x1":0.74, "T1":820.0}
    }
    new_avg = _compute_avg_dev(new_rows, new_cfg)
    old_avg = _compute_avg_dev(old_rows, old_cfg)
    return 1.0 if new_avg < old_avg else 0.0


# === block: score_4 (check id='thermo_structural') ===
def score_4(artifact, step, ctx):
    import csv
    from collections import defaultdict
    rows = artifact
    groups = defaultdict(list)
    for row in rows:
        groups[(row["Model"], row["Phase"])].append(row)

    full_range_ok = False
    old_sigma_truncated_ok = False
    no_discontinuity = True
    thresh = step["config"]["discontinuity_threshold"]

    for (model, phase), g in groups.items():
        g_sorted = sorted(g, key=lambda r: float(r["Mole_fraction_Cr"]))
        xs = [float(r["Mole_fraction_Cr"]) for r in g_sorted]
        gs = [float(r["Gibbs_energy_J_per_mol"]) for r in g_sorted]
        hs = [float(r["Enthalpy_J_per_mol"]) for r in g_sorted]
        if model == "new" and phase.lower() == "sigma":
            if min(xs) <= 0.02 and max(xs) >= 0.98:
                full_range_ok = True
        if model == "old" and phase.lower() == "sigma":
            if min(xs) > 0.4 and max(xs) < 0.8:
                old_sigma_truncated_ok = True
        for i in range(1, len(xs)):
            if abs(gs[i] - gs[i-1]) > thresh or abs(hs[i] - hs[i-1]) > thresh:
                no_discontinuity = False

    score = 0.0
    if full_range_ok:
        score += 0.6
    if no_discontinuity:
        score += 0.4
    return min(1.0, score)


_SCORERS = {
    'dft_total_energy': score_0,
    'new_phase_diagram_accuracy': score_1,
    'old_phase_diagram_accuracy': score_2,
    'trend_new_better_than_old': score_3,
    'thermo_structural': score_4,
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
