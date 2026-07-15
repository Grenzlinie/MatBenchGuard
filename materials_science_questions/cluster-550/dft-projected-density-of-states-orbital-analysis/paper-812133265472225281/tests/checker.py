import os
import json
import csv


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


# === block: score_0 (check id='adsorption_energies_eval') ===
def score_0(artifact, step, ctx):
    def check(value, gold, tol):
        return 1.0 if abs(value - gold) <= tol else 0.0

    def check_list(values, golds, tol):
        if len(values) != len(golds):
            return 0.0
        n = len(golds)
        ok = sum(1 for v,g in zip(values,golds) if abs(v-g) <= tol)
        return ok / n if n>0 else 1.0

    golds = step["gold"]
    config_weights = step["config_weights"]
    energy_weight = step["energy_weight"]
    distance_weight = step["distance_weight"]
    energy_tol = step["tolerances"]["energy_eV"]
    dist_tol = step["tolerances"]["distance_Ang"]

    score = 0.0
    for ckey, cweight in config_weights.items():
        if ckey not in artifact:
            continue
        cdata = artifact[ckey]
        gdata = golds.get(ckey, {})
        # energy fields
        energy_fields = []
        for ef in ["PBE_Eads", "RPBE_Eads"]:
            if ef in gdata and ef in cdata:
                val = cdata[ef]
                if val is not None:
                    energy_fields.append(check(val, gdata[ef], energy_tol))
        e_score = sum(energy_fields) / len(energy_fields) if energy_fields else 0.0
        # distance fields
        dist_fields = []
        for df in ["Mo_O_distances", "O_O_distance", "C_O_distance", "Mo_C_distance", "C_C_distance"]:
            if df in gdata and df in cdata:
                gval = gdata[df]
                val = cdata[df]
                if isinstance(gval, list):
                    dist_fields.append(check_list(val, gval, dist_tol))
                else:
                    # gold expects a single scalar (float) – e.g., Mo_C_distance, C_C_distance
                    if isinstance(val, (list, tuple)):
                        # agent provided a list; extract the minimum to compare against gold
                        vals = [v for v in val if v is not None]
                        if not vals:
                            dist_fields.append(0.0)
                        else:
                            min_val = min(vals)
                            dist_fields.append(check(min_val, gval, dist_tol))
                    else:
                        dist_fields.append(check(val, gval, dist_tol) if val is not None else 0.0)
        d_score = sum(dist_fields) / len(dist_fields) if dist_fields else 0.0
        config_score = energy_weight * e_score + distance_weight * d_score
        score += cweight * config_score
    return max(0.0, min(1.0, score))


_SCORERS = {
    'adsorption_energies_eval': score_0,
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
