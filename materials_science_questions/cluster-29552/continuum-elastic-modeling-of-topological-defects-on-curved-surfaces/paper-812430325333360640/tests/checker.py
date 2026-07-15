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


# === block: score_0 (check id='check_shape_type') ===
def score_0(artifact, step, ctx):
    def score_shape_type(artifact, step, ctx):
        simulations = artifact.get("simulations", [])
        required = step.get("parameters", {}).get("required_combos", [])
        if not simulations or not required:
            return 0.0
        lookup = {}
        for sim in simulations:
            v = sim.get("v")
            mu = sim.get("mu")
            shape = sim.get("shape_type", "").strip().lower()
            lookup[(v, mu)] = shape
        correct = 0
        for req in required:
            key = (req["v"], req["mu"])
            if key in lookup and lookup[key] == req["expected_shape"].strip().lower():
                correct += 1
        return correct / len(required) if required else 0.0


# === block: score_1 (check id='check_defect_wt_alignment') ===
def score_1(artifact, step, ctx):
    def score_defect_wt_alignment(artifact, step, ctx):
        simulations = artifact.get("simulations", [])
        tol = step.get("parameters", {}).get("tolerance_fraction", 0.01)
        if not simulations:
            return 0.0
        scores = []
        for sim in simulations:
            w_t_profile = sim.get("w_t_profile", [])
            defects = sim.get("defects", [])
            L_s = sim.get("L_s", None)
            if L_s is None or L_s <= 0 or not w_t_profile or not defects:
                scores.append(0.0)
                continue
            points = sorted(w_t_profile, key=lambda x: x.get("s", 0))
            s_vals = [p["s"] for p in points]
            w_vals = [p["w_t"] for p in points]
            if len(w_vals) < 2:
                scores.append(0.0)
                continue
            maxima_s = []
            for i in range(1, len(w_vals)-1):
                if w_vals[i] > w_vals[i-1] and w_vals[i] > w_vals[i+1]:
                    maxima_s.append(s_vals[i])
            if w_vals[0] > w_vals[1]:
                maxima_s.append(s_vals[0])
            if w_vals[-1] > w_vals[-2]:
                maxima_s.append(s_vals[-1])
            if not maxima_s:
                scores.append(0.0)
                continue
            aligned = 0
            for d in defects:
                ds = d.get("s")
                if ds is None:
                    continue
                ok = False
                for ms in maxima_s:
                    if abs(ds - ms) <= tol * L_s:
                        ok = True
                        break
                if ok:
                    aligned += 1
            frac = aligned / len(defects) if defects else 0.0
            total_q = sum(d.get("topological_charge", 0) for d in defects)
            charges_ok = all(
                abs(d.get("topological_charge", 0) - 0.5) < 1e-6 or
                abs(d.get("topological_charge", 0) + 0.5) < 1e-6
                for d in defects
            )
            if abs(total_q - 2.0) < 1e-6 and charges_ok:
                sim_score = frac
            else:
                sim_score = frac * 0.5
            scores.append(sim_score)
        return sum(scores) / len(scores) if scores else 0.0


_SCORERS = {
    'check_shape_type': score_0,
    'check_defect_wt_alignment': score_1,
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
