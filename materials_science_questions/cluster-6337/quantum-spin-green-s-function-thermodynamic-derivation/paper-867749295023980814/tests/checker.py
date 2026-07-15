import os
import json
import csv

# === author imports / helpers ===
import numpy as np, json, math


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
    def prepare(outputs_dir, spec):
        # Extract any needed pre‑computed gold from spec if desired; here we pass the whole spec.
        return {"spec": spec}


# === block: score_0 (check id='dispersion') ===
def score_0(artifact, step, ctx):
    def score_dispersion(artifact, step, ctx):
        import numpy as np
        params = step["params"]
        sigma, J, Gx, Gy, Jz = float(params["sigma"]), float(params["J"]), float(params["Gamma_x"]), float(params["Gamma_y"]), float(params["Jz"])
        tol = float(params["tolerance_meV"])
        min_pts = int(params["min_points"])
        disp = artifact.get("dispersion")
        if not disp or len(disp) < min_pts:
            return 0.0
        def omega_nu(q, nu):
            qx, qy, qz = q[0], q[1], q[2]
            J0 = 2*J*(1+1) + 2*Jz
            Jq = 2*J*(np.cos(qx)+np.cos(qy)) + 2*Jz*np.cos(qz)
            A = sigma * (J0 + 2*Gx)
            B = sigma * Gy * np.cos(qy)
            C = sigma * (Jq + Gy * np.cos(qy))
            v = A*A + B*B - C*C + 2*nu*A*B
            if v < 0:
                v = 0.0
            return np.sqrt(v)
        ok = 0
        for p in disp:
            try:
                q, om, op = p["q_point"], float(p["omega_minus"]), float(p["omega_plus"])
            except (KeyError, ValueError, TypeError):
                continue
            em = omega_nu(q, -1)
            ep = omega_nu(q, 1)
            if abs(om - em) <= tol and abs(op - ep) <= tol:
                ok += 1
        n = len(disp)
        if n == 0:
            return 0.0
        return min(1.0, ok / n)


# === block: score_1 (check id='magnetization') ===
def score_1(artifact, step, ctx):
    def score_magnetization(artifact, step, ctx):
        import numpy as np
        params = step["params"]
        gold = params["gold_points"]
        Tg = gold["T"]
        sg = gold["sigma"]
        tol = float(gold["tolerance_sigma"])
        curve = artifact.get("magnetization_curve")
        if not curve or len(curve) < 2:
            return 0.0
        Tvals = np.array([p["T"] for p in curve])
        Svals = np.array([p["sigma"] for p in curve])
        mono = all(Svals[i] >= Svals[i+1] - 1e-12 for i in range(len(Svals)-1))
        matches = 0
        for t, s in zip(Tg, sg):
            idx = np.argmin(np.abs(Tvals - t))
            if abs(Svals[idx] - s) <= tol:
                matches += 1
        point_score = matches / len(Tg) if Tg else 1.0
        mono_score = 1.0 if mono else 0.0
        return 0.9 * point_score + 0.1 * mono_score


# === block: score_2 (check id='neel_temperature') ===
def score_2(artifact, step, ctx):
    def score_neel_temperature(artifact, step, ctx):
        params = step["params"]
        gold_cases = params["gold_Tc_meV"]
        tol_rel = float(params["tolerance_relative"])
        neel = artifact.get("neel_temperatures")
        if not neel or not isinstance(neel, dict):
            return 0.0
        scores = []
        for case, gold_val in gold_cases.items():
            if case not in neel:
                scores.append(0.0)
                continue
            try:
                rep = float(neel[case]["Tc_meV"])
            except (KeyError, ValueError, TypeError):
                scores.append(0.0)
                continue
            rel_err = abs(rep - gold_val) / gold_val
            if rel_err <= tol_rel:
                sc = 1.0
            elif rel_err <= 2 * tol_rel:
                sc = 0.5
            else:
                sc = 0.0
            scores.append(sc)
        if not scores:
            return 0.0
        return sum(scores) / len(scores)


_SCORERS = {
    'dispersion': score_0,
    'magnetization': score_1,
    'neel_temperature': score_2,
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
