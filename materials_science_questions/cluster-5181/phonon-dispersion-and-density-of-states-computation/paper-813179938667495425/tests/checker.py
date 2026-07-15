import os
import json
import csv

# === author imports / helpers ===
import json
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


# === block: score_0 (check id='fitted_params') ===
def score_0(artifact, step, ctx):
        gold = step["config"]["gold"]
        tolerances = step["config"]["tolerances"]["relative"]
        default_tol = tolerances.get("default", 0.15)
        scores = []
        for key, target in gold.items():
            if key not in artifact:
                scores.append(0.0)
                continue
            val = artifact[key]
            if target == 0:
                if abs(val) < 1e-9:
                    scores.append(1.0)
                else:
                    scores.append(0.0)
                continue
            rel_err = abs(val - target) / abs(target)
            tol = tolerances.get(key, default_tol)
            s = max(0.0, 1.0 - rel_err / tol)
            scores.append(s)
        return sum(scores) / len(scores) if scores else 0.0


# === block: score_1 (check id='final_rms') ===
def score_1(artifact, step, ctx):
        target = step["target"]
        scores = []
        for key, t in target.items():
            if key not in artifact:
                scores.append(0.0)
                continue
            val = artifact[key]
            if val <= t + 1e-12:
                scores.append(1.0)
            else:
                penal = (val - t) / (0.5 * t) if t > 0 else 1.0
                scores.append(max(0.0, 1.0 - penal))
        return sum(scores) / len(scores) if scores else 0.0


# === block: score_2 (check id='crystal_energies') ===
def score_2(artifact, step, ctx):
        phases = {}
        for row in artifact:
            ph = row["phase"].strip().lower()
            phases[ph] = {
                "a": float(row["a_au"]),
                "b": float(row["b_au"]),
                "c": float(row["c_au"]),
                "beta": float(row.get("beta_deg", 90)),
                "energy": float(row["energy_per_fu_eV"])
            }
        required = ["alpha", "theta", "kappa", "bixbyite"]
        for ph in required:
            if ph not in phases:
                return 0.0
        gold_lat = step["config"]["gold_lattice"]
        lat_tol = step["config"]["lat_tol"]
        angle_tol = step["config"]["angle_tol"]
        lat_scores = []
        for ph in ["alpha", "theta"]:
            if ph not in gold_lat:
                continue
            gold = gold_lat[ph]
            ag = phases[ph]
            for field in ["a","b","c"]:
                err = abs(ag[field] - gold[field])
                s = max(0.0, 1.0 - err / lat_tol)
                lat_scores.append(s)
            if "beta" in gold:
                err_angle = abs(ag["beta"] - gold["beta"])
                if err_angle > 180:
                    err_angle = 360 - err_angle
                s_angle = max(0.0, 1.0 - err_angle / angle_tol)
                lat_scores.append(s_angle)
        lat_score = sum(lat_scores) / len(lat_scores) if lat_scores else 0.0
        e_alpha = phases["alpha"]["energy"]
        gold_diff = step["config"]["gold_energy_diff"]
        ediff_tol = step["config"]["ediff_tol"]
        diff_scores = []
        for ph in ["theta","kappa","bixbyite"]:
            agent_diff = phases[ph]["energy"] - e_alpha
            gd = gold_diff.get("alpha_"+ph, None)
            if gd is not None:
                err = abs(agent_diff - gd)
                s = max(0.0, 1.0 - err / ediff_tol)
                diff_scores.append(s)
        diff_score = sum(diff_scores) / len(diff_scores) if diff_scores else 0.0
        return 0.6 * lat_score + 0.4 * diff_score


# === block: score_3 (check id='phonon') ===
def score_3(artifact, step, ctx):
        if not artifact or len(artifact) != 30:
            return 0.0
        prev = -1.0
        for row in artifact:
            f = float(row["frequency_THz"])
            if f < 0 or f > 50:
                return 0.0
            if f <= prev:
                return 0.0
            prev = f
        return 1.0


# === block: score_4 (check id='elastic') ===
def score_4(artifact, step, ctx):
        gold = step["config"]["gold"]
        tol_rel = step["config"]["tolerance_relative"]
        scores = []
        for key, target in gold.items():
            if key not in artifact:
                scores.append(0.0)
                continue
            val = artifact[key]
            if target == 0:
                if abs(val) < 1e-9:
                    scores.append(1.0)
                else:
                    scores.append(0.0)
                continue
            rel_err = abs(val - target) / abs(target)
            s = max(0.0, 1.0 - rel_err / tol_rel)
            scores.append(s)
        return sum(scores) / len(scores) if scores else 0.0


# === block: score_5 (check id='thermal_expansion') ===
def score_5(artifact, step, ctx):
        gold_points = step["config"]["gold_points"]
        tol = step["config"]["tolerance_abs"]
        # Parse agent rows into sorted (T, V) list
        points = []
        for row in artifact:
            try:
                T = float(row["T_K"])
                V = float(row["V_over_V0"])
                points.append((T, V))
            except (ValueError, KeyError):
                continue
        if len(points) < 2:
            return 0.0
        points.sort(key=lambda x: x[0])
        Ts = [p[0] for p in points]
        Vs = [p[1] for p in points]
        scores = []
        for T_gold, V_gold in gold_points:
            T = float(T_gold)
            # linear search for the first index where Ts[idx] >= T
            idx = 0
            while idx < len(Ts) and Ts[idx] < T - 1e-9:
                idx += 1
            if idx == 0:
                if abs(Ts[0] - T) < 1e-9:
                    err = abs(Vs[0] - V_gold)
                    s = max(0.0, 1.0 - err / tol)
                else:
                    s = 0.0
            elif idx == len(Ts):
                if abs(Ts[-1] - T) < 1e-9:
                    err = abs(Vs[-1] - V_gold)
                    s = max(0.0, 1.0 - err / tol)
                else:
                    s = 0.0
            else:
                T1, T2 = Ts[idx-1], Ts[idx]
                V1, V2 = Vs[idx-1], Vs[idx]
                if T2 - T1 < 1e-12:
                    V_agent = (V1 + V2) / 2.0
                else:
                    V_agent = V1 + (V2 - V1) * (T - T1) / (T2 - T1)
                err = abs(V_agent - V_gold)
                s = max(0.0, 1.0 - err / tol)
            scores.append(s)
        return sum(scores) / len(scores) if scores else 0.0


# === block: score_6 (check id='defect') ===
def score_6(artifact, step, ctx):
        gold = step["config"]["gold"]
        tol = step["config"]["tolerance_abs"]
        scores = []
        for key, target in gold.items():
            if key not in artifact:
                scores.append(0.0)
                continue
            err = abs(artifact[key] - target)
            s = max(0.0, 1.0 - err / tol)
            scores.append(s)
        return sum(scores) / len(scores) if scores else 0.0


_SCORERS = {
    'fitted_params': score_0,
    'final_rms': score_1,
    'crystal_energies': score_2,
    'phonon': score_3,
    'elastic': score_4,
    'thermal_expansion': score_5,
    'defect': score_6,
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
