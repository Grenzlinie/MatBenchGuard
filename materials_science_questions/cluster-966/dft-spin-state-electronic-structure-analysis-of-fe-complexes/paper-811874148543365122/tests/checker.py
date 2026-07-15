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


# === block: score_0 (check id='results_scoring') ===
def score_0(artifact, step, ctx):
        required_keys = ["high_spin_energy", "intermediate_spin_energy", "energy_difference",
                         "high_spin_Fe_moment", "intermediate_spin_Fe_moment",
                         "high_spin_Co_moment", "intermediate_spin_Co_moment",
                         "Fe_O_bond_length", "Co_O_bond_length", "coupling_sign"]
        if not all(k in artifact for k in required_keys):
            return 0.0
        params = step.get("params", {})
        tol_bond = params.get("tol_bond", 0.05)
        tol_moment = params.get("tol_moment", 0.5)
        fe_o_len = params.get("fe_o_length", 1.92)
        co_o_len = params.get("co_o_length", 1.74)
        fe_moment_hs = params.get("fe_moment_hs", 4.4)
        fe_moment_is = params.get("fe_moment_is", 2.9)
        expected_coupling = params.get("coupling_sign_expected", "antiferromagnetic")
        hs = artifact["high_spin_energy"]
        is_ = artifact["intermediate_spin_energy"]
        # energy ordering: high-spin is ground state -> hs < is_
        score_energy = 1.0 if hs < is_ else 0.0
        # bond lengths
        score_fe_bond = 1.0 if abs(artifact["Fe_O_bond_length"] - fe_o_len) <= tol_bond else 0.0
        score_co_bond = 1.0 if abs(artifact["Co_O_bond_length"] - co_o_len) <= tol_bond else 0.0
        # Fe moment magnitudes and antiparallel sign (any orientation)
        fe_hs_mag = abs(artifact["high_spin_Fe_moment"])
        fe_is_mag = abs(artifact["intermediate_spin_Fe_moment"])
        fe_hs_ok = 1.0 if (abs(fe_hs_mag - fe_moment_hs) <= tol_moment) and (artifact["high_spin_Fe_moment"] * artifact["high_spin_Co_moment"] < 0) else 0.0
        fe_is_ok = 1.0 if (abs(fe_is_mag - fe_moment_is) <= tol_moment) and (artifact["intermediate_spin_Fe_moment"] * artifact["intermediate_spin_Co_moment"] < 0) else 0.0
        # coupling sign consistency (orientation-blind)
        coupling_ok = 1.0 if (artifact["coupling_sign"] == expected_coupling) and (artifact["high_spin_Fe_moment"] * artifact["high_spin_Co_moment"] < 0) and (artifact["intermediate_spin_Fe_moment"] * artifact["intermediate_spin_Co_moment"] < 0) else 0.0
        w_energy = 0.15
        w_fe_bond = 0.15
        w_co_bond = 0.15
        w_fe_hs = 0.15
        w_fe_is = 0.15
        w_coupling = 0.25
        total = (w_energy * score_energy +
                 w_fe_bond * score_fe_bond +
                 w_co_bond * score_co_bond +
                 w_fe_hs * fe_hs_ok +
                 w_fe_is * fe_is_ok +
                 w_coupling * coupling_ok)
        return max(0.0, min(1.0, total))


_SCORERS = {
    'results_scoring': score_0,
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
