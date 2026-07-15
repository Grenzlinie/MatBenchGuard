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


# === block: score_0 (check id='step4_analysis') ===
def score_0(artifact, step, ctx):
    def _safe_num(d, k):
        v = d.get(k)
        if isinstance(v, (int, float)):
            return v
        return None

    gold = step["gold"]
    tol = step["tolerances"]
    checks = []

    # As segregation within tolerance
    v = _safe_num(artifact, "as_segregation_energy_meV")
    if v is not None and abs(v - gold["as_segregation_energy_meV"]) <= tol["as_segregation_energy_meV_abs"]:
        checks.append(1)
    else:
        checks.append(0)

    # As+ segregation
    v = _safe_num(artifact, "asplus_segregation_energy_meV")
    if v is not None and abs(v - gold["asplus_segregation_energy_meV"]) <= tol["asplus_segregation_energy_meV_abs"]:
        checks.append(1)
    else:
        checks.append(0)

    # Ga segregation within tolerance
    v = _safe_num(artifact, "ga_segregation_energy_meV")
    if v is not None and abs(v) <= tol["ga_segregation_energy_meV_abs"]:
        checks.append(1)
    else:
        checks.append(0)

    # As relaxation energy gb
    v = _safe_num(artifact, "as_relaxation_energy_gb_meV")
    if v is not None and abs(v - gold["as_relaxation_energy_gb_meV"]) <= tol["relaxation_energy_abs_tolerance"]:
        checks.append(1)
    else:
        checks.append(0)

    # As relaxation energy bk
    v = _safe_num(artifact, "as_relaxation_energy_bk_meV")
    if v is not None and abs(v - gold["as_relaxation_energy_bk_meV"]) <= tol["relaxation_energy_abs_tolerance"]:
        checks.append(1)
    else:
        checks.append(0)

    # Similarity between As relaxation at gb and bk
    v_gb = _safe_num(artifact, "as_relaxation_energy_gb_meV")
    v_bk = _safe_num(artifact, "as_relaxation_energy_bk_meV")
    if v_gb is not None and v_bk is not None and abs(v_gb - v_bk) <= tol["relaxation_similarity_max_diff"]:
        checks.append(1)
    else:
        checks.append(0)

    # As+ relaxation gb
    v = _safe_num(artifact, "asplus_relaxation_energy_gb_meV")
    if v is not None and abs(v - gold["asplus_relaxation_energy_gb_meV"]) <= tol["relaxation_energy_abs_tolerance"]:
        checks.append(1)
    else:
        checks.append(0)

    # Ga relaxation gb
    v = _safe_num(artifact, "ga_relaxation_energy_gb_meV")
    if v is not None and abs(v - gold["ga_relaxation_energy_gb_meV"]) <= tol["relaxation_energy_abs_tolerance"]:
        checks.append(1)
    else:
        checks.append(0)

    # Ionization increase
    v = _safe_num(artifact, "as_ionization_increase_meV")
    if v is not None and abs(v - gold["as_ionization_increase_meV"]) <= tol["as_ionization_increase_meV_abs"]:
        checks.append(1)
    else:
        checks.append(0)

    # Bulk As binding
    v = _safe_num(artifact, "bulk_as_binding_energy_meV")
    if v is not None and abs(v - gold["bulk_as_binding_energy_meV"]) <= tol["bulk_as_binding_energy_meV_abs"]:
        checks.append(1)
    else:
        checks.append(0)

    # Interface band
    v = _safe_num(artifact, "interface_band_energy_meV")
    if v is not None and abs(v - gold["interface_band_energy_meV"]) <= tol["interface_band_energy_meV_abs"]:
        checks.append(1)
    else:
        checks.append(0)

    # Trend: As+ binding weaker than As (more negative -> stronger binding)
    v_as = _safe_num(artifact, "as_segregation_energy_meV")
    v_asplus = _safe_num(artifact, "asplus_segregation_energy_meV")
    if v_as is not None and v_asplus is not None and v_asplus > v_as:
        checks.append(1)
    else:
        checks.append(0)

    return sum(checks) / len(checks) if checks else 0.0


_SCORERS = {
    'step4_analysis': score_0,
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
