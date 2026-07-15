import os
import json
import csv

# === author imports / helpers ===
import json, csv


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
        step = spec["steps"][0]
        config = step.get("config", {})
        return {"config": config}


# === block: score_0 (check id='trends') ===
def score_0(artifact, step, ctx):
        config = ctx["config"]
        defect_mapping = config["defect_interior_mapping"]
        subst_pairs = config["substitutional_pairs"]
        eps = 1e-9

        # Build lookup: (system, defect, location, mu_N) -> E_f
        data = {}
        for row in artifact:
            if not isinstance(row, dict):
                continue
            try:
                sys_val = row.get("system")
                defect_val = row.get("defect")
                loc_val = row.get("location")
                mu_val = row.get("mu_N")
                ef_val = row.get("E_f")
                if any(v is None for v in [sys_val, defect_val, loc_val, mu_val, ef_val]):
                    continue
                sys = str(sys_val).strip()
                defect = str(defect_val).strip()
                loc = str(loc_val).strip()
                mu = round(float(mu_val), 10)
                ef = float(ef_val)
                key = (sys, defect, loc, mu)
                data[key] = ef
            except (ValueError, TypeError, AttributeError):
                continue

        # Get all distinct mu_N values present
        all_mu = sorted({key[3] for key in data.keys()})

        # Interfacial checks: interior vs each interface location for each defect
        interfacial_total = 0
        interfacial_passed = 0
        for defect, interior_info in defect_mapping.items():
            int_sys = interior_info["system"]
            int_loc = interior_info["location"]
            for mu in all_mu:
                int_key = (int_sys, defect, int_loc, mu)
                int_ef = data.get(int_key)
                if int_ef is None:
                    continue
                for hybrid_loc in ["interface_B", "interface_N"]:
                    hyb_key = ("hybrid", defect, hybrid_loc, mu)
                    hyb_ef = data.get(hyb_key)
                    if hyb_ef is not None:
                        interfacial_total += 1
                        if int_ef + eps >= hyb_ef:  # interior not higher than interface
                            interfacial_passed += 1

        # Substitutional vs vacancy checks
        substitution_total = 0
        substitution_passed = 0
        for pair in subst_pairs:
            sub = pair["sub"]
            vac = pair["vac"]
            for key_sub, ef_sub in data.items():
                sys, defect, loc, mu = key_sub
                if defect != sub:
                    continue
                key_vac = (sys, vac, loc, mu)
                ef_vac = data.get(key_vac)
                if ef_vac is not None:
                    substitution_total += 1
                    if ef_sub <= ef_vac + eps:
                        substitution_passed += 1

        int_score = interfacial_passed / interfacial_total if interfacial_total > 0 else 0.0
        sub_score = substitution_passed / substitution_total if substitution_total > 0 else 0.0
        combined = (int_score + sub_score) / 2.0
        return combined


_SCORERS = {
    'trends': score_0,
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
