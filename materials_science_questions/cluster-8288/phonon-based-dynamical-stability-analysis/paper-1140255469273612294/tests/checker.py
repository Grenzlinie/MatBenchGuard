import os
import json
import csv

# === author imports / helpers ===
import csv, math
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
    ctx = {
        "eu_target": 24.42,
        "alpha_target": 0.026,
        "threshold_target": 14.0,
        "tol_eu": 2.0,
        "decay_eu": 6.0,
        "tol_alpha": 0.01,
        "decay_alpha": 0.05,
        "tol_threshold": 2.0,
        "decay_threshold": 6.0,
        "asymm_tol_dw": 0.2
    }
    return ctx


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not isinstance(rows, list):
        return 0.0
    eu_freq = None
    a2g_neg = False
    for r in rows:
        mode = r.get("mode","")
        freq = float(r.get("frequency_THz", 999))
        if "Eu(4)" in mode:
            eu_freq = freq
        if "A2g" in mode and freq < 0:
            a2g_neg = True
    eu_score = 0.0
    if eu_freq is not None:
        diff = abs(eu_freq - ctx["eu_target"])
        if diff <= ctx["tol_eu"]:
            eu_score = 1.0
        elif diff < ctx["decay_eu"]:
            eu_score = 1.0 - (diff - ctx["tol_eu"]) / (ctx["decay_eu"] - ctx["tol_eu"])
        else:
            eu_score = 0.0
    a2g_score = 1.0 if a2g_neg else 0.0
    return 0.6667 * eu_score + 0.3333 * a2g_score


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not isinstance(rows, list):
        return 0.0
    left_sel = [r for r in rows if float(r["displacement_Angstrom"]) < 0]
    right_sel = [r for r in rows if float(r["displacement_Angstrom"]) > 0]
    zero_candidates = [(abs(float(r["displacement_Angstrom"])), r) for r in rows]
    if not zero_candidates:
        return 0.0
    zero_row = min(zero_candidates, key=lambda x: x[0])[1]
    if not left_sel or not right_sel:
        return 0.0
    left_min = min(left_sel, key=lambda r: float(r["energy_eV"]))
    right_min = min(right_sel, key=lambda r: float(r["energy_eV"]))
    E0 = float(zero_row["energy_eV"])
    E_left = float(left_min["energy_eV"])
    E_right = float(right_min["energy_eV"])
    barrier_ok = E0 > E_left and E0 > E_right
    mean_min = (E_left + E_right) / 2.0
    if abs(E0 - mean_min) < 1e-9:
        asym = 1.0
    else:
        asym = abs(E_left - E_right) / abs(E0 - mean_min)
    sym_ok = asym < ctx["asymm_tol_dw"]
    if barrier_ok and sym_ok:
        return 1.0
    elif barrier_ok:
        return 0.5
    else:
        return 0.0


# === block: score_2 (check id='step_03') ===
def score_2(artifact, step, ctx):
    val = float(artifact.strip())
    diff = abs(val - ctx["alpha_target"])
    if diff <= ctx["tol_alpha"]:
        return 1.0
    elif diff < ctx["decay_alpha"]:
        return 1.0 - (diff - ctx["tol_alpha"]) / (ctx["decay_alpha"] - ctx["tol_alpha"])
    else:
        return 0.0


# === block: score_3 (check id='step_04') ===
def score_3(artifact, step, ctx):
    rows = artifact
    if not isinstance(rows, list):
        return 0.0
    groups = defaultdict(list)
    for r in rows:
        try:
            flu = float(r["fluence_mJcm2"])
            t = float(r["time_ps"])
            q = float(r["Q_A"])
            groups[flu].append((t, q))
        except (ValueError, KeyError):
            continue
    if not groups:
        return 0.0

    def find_closest_fluence(target, grps):
        best = None; best_diff = 1e6
        for f in grps:
            diff = abs(f - target)
            if diff < best_diff:
                best_diff = diff; best = f
        return best if best_diff < 1.0 else None

    req = [12.5, 14.0, 20.0]
    req_present = all(find_closest_fluence(r, groups) is not None for r in req)

    # below threshold: fluence 12.5 must yield final Q_A > 0
    below_ok = False
    f12 = find_closest_fluence(12.5, groups)
    if f12 is not None and groups[f12]:
        ts = sorted(groups[f12], key=lambda x: x[0])
        n = len(ts)
        start = max(int(0.8 * n), 0)
        avg = sum(q for _,q in ts[start:]) / (n - start)
        below_ok = avg > 0

    # above threshold: fluences 14 and 20 must yield final Q_A < 0
    above_ok = True
    for target_f in [14.0, 20.0]:
        f = find_closest_fluence(target_f, groups)
        if f is None or not groups[f]:
            above_ok = False; break
        ts = sorted(groups[f], key=lambda x: x[0])
        n = len(ts)
        start = max(int(0.8 * n), 0)
        avg = sum(q for _,q in ts[start:]) / (n - start)
        if avg >= 0:
            above_ok = False; break

    # recompute threshold: lowest fluence with negative final Q_A
    switched_fs = []
    for f, ts in groups.items():
        ts_sorted = sorted(ts, key=lambda x: x[0])
        n = len(ts_sorted)
        if n == 0: continue
        start = max(int(0.8 * n), 0)
        avg = sum(q for _,q in ts_sorted[start:]) / (n - start)
        if avg < 0:
            switched_fs.append(f)
    threshold = min(switched_fs) if switched_fs else None
    threshold_score = 0.0
    if threshold is not None:
        diff = abs(threshold - ctx["threshold_target"])
        if diff <= ctx["tol_threshold"]:
            threshold_score = 1.0
        elif diff < ctx["decay_threshold"]:
            threshold_score = 1.0 - (diff - ctx["tol_threshold"]) / (ctx["decay_threshold"] - ctx["tol_threshold"])
        else:
            threshold_score = 0.0

    s1 = 1.0 if req_present else 0.0
    s2 = 1.0 if below_ok else 0.0
    s3 = 1.0 if above_ok else 0.0
    s4 = threshold_score
    return 0.2 * s1 + 0.3 * s2 + 0.3 * s3 + 0.2 * s4


# === block: score_4 (check id='step_05') ===
def score_4(artifact, step, ctx):
    val = float(artifact.strip())
    diff = abs(val - ctx["threshold_target"])
    if diff <= ctx["tol_threshold"]:
        return 1.0
    elif diff < ctx["decay_threshold"]:
        return 1.0 - (diff - ctx["tol_threshold"]) / (ctx["decay_threshold"] - ctx["tol_threshold"])
    else:
        return 0.0


# === block: score_5 (check id='step_06') ===
def score_5(artifact, step, ctx):
    rows = artifact
    if not isinstance(rows, list):
        return 0.0
    left_max = None; right_min = None
    for r in rows:
        h = r.get("helicity", "").strip().lower()
        try:
            q = float(r["Q_A"])
        except (ValueError, KeyError):
            continue
        if h == "left":
            if left_max is None or q > left_max:
                left_max = q
        elif h == "right":
            if right_min is None or q < right_min:
                right_min = q
    if left_max is not None and left_max > 0 and right_min is not None and right_min < 0:
        return 1.0
    elif (left_max is not None and left_max > 0) or (right_min is not None and right_min < 0):
        return 0.5
    else:
        return 0.0


_SCORERS = {
    'step_01': score_0,
    'step_02': score_1,
    'step_03': score_2,
    'step_04': score_3,
    'step_05': score_4,
    'step_06': score_5,
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
