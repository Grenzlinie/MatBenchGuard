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


# === block: score_0 (check id='results') ===
def score_0(artifact, step, ctx):
        # validate structure and numeric types, rejecting None explicitly
        required_keys = ["grain_boundary_thickness", "grain_boundary", "triple_junction", "ice_vapor_interface"]
        for k in required_keys:
            if k not in artifact:
                return 0.0
        if not isinstance(artifact.get("grain_boundary_thickness"), (int, float)) or artifact.get("grain_boundary_thickness") is None:
            return 0.0
        for region in ["grain_boundary", "triple_junction", "ice_vapor_interface"]:
            reg = artifact.get(region)
            if not isinstance(reg, dict):
                return 0.0
            for f in ["f_liq_bond", "f_liq_mol", "f_NHBneq4", "D"]:
                val = reg.get(f)
                if not isinstance(val, (int, float)) or val is None:
                    return 0.0

        # paper gold
        gold = {
            "thickness": 1.0,
            "grain_boundary": {"f_liq_bond": 0.332, "f_liq_mol": 0.305, "f_NHBneq4": 0.013, "D": 5.0e-13},
            "triple_junction": {"f_liq_bond": 0.638, "f_liq_mol": 0.527, "f_NHBneq4": 0.032, "D": 1.7e-12},
            "ice_vapor_interface": {"f_liq_bond": 0.406, "f_liq_mol": 0.393, "f_NHBneq4": 0.111, "D": 3.4e-11}
        }

        # thickness score (linear decay within 0.5 nm)
        t = artifact["grain_boundary_thickness"]
        thickness_score = max(0.0, 1.0 - abs(t - gold["thickness"]) / 0.5)

        # fraction scores (tolerance 0.1 absolute)
        fraction_scores = []
        for region in ["grain_boundary", "triple_junction", "ice_vapor_interface"]:
            for field in ["f_liq_bond", "f_liq_mol", "f_NHBneq4"]:
                val = artifact[region][field]
                ref = gold[region][field]
                diff = abs(val - ref)
                score = max(0.0, 1.0 - diff / 0.1)
                fraction_scores.append(score)
        mean_fraction_score = sum(fraction_scores) / len(fraction_scores)

        # diffusion coefficient scores (within factor 2)
        d_scores = []
        for region in ["grain_boundary", "triple_junction", "ice_vapor_interface"]:
            val = artifact[region]["D"]
            if val <= 0:
                d_scores.append(0.0)
                continue
            ref = gold[region]["D"]
            if ref / 2.0 <= val <= ref * 2.0:
                d_scores.append(1.0)
            else:
                d_scores.append(0.0)
        mean_d_score = sum(d_scores) / len(d_scores)

        # structural ordering: D_surf > D_tj > D_gb
        d_gb = artifact["grain_boundary"]["D"]
        d_tj = artifact["triple_junction"]["D"]
        d_surf = artifact["ice_vapor_interface"]["D"]
        order_ok = (d_surf > d_tj > d_gb)
        order_score = 1.0 if order_ok else 0.0

        total = 0.1 * thickness_score + 0.5 * mean_fraction_score + 0.3 * mean_d_score + 0.1 * order_score
        return min(max(total, 0.0), 1.0)


_SCORERS = {
    'results': score_0,
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
