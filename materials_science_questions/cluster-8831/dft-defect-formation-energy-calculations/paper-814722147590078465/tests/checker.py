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


# === block: score_0 (check id='step_04') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        targets = step.get("targets", {})
        tols = step.get("tolerances", {})
        tol_mag = tols.get("total_magnetic_moment_abs", 0.1)
        tol_cu = tols.get("Cu_partial_magnetic_moment_abs", 0.05)
        tol_bond = tols.get("Cu_O_bond_length_abs", 0.05)
        spin_threshold = tols.get("spin_polarization_threshold", 0.95)
        if not isinstance(artifact, dict):
            return 0.0
        sub_keys = ["10-0", "5-0"]
        if not all(k in artifact for k in sub_keys):
            return 0.0
        total = 0
        passed = 0
        for key in sub_keys:
            tgt = targets.get(key, {})
            if not isinstance(tgt, dict):
                continue
            val = artifact.get(key)
            if not isinstance(val, dict):
                continue
            # magnetic state
            total += 1
            if val.get("stable_magnetic_state") == tgt.get("stable_magnetic_state"):
                passed += 1
            # total magnetic moment
            total += 1
            if abs(float(val.get("total_magnetic_moment", 0)) - tgt.get("total_magnetic_moment", 0)) <= tol_mag:
                passed += 1
            # Cu partial magnetic moment
            total += 1
            if abs(float(val.get("Cu_partial_magnetic_moment", 0)) - tgt.get("Cu_partial_magnetic_moment", 0)) <= tol_cu:
                passed += 1
            # Cu-O bond length
            total += 1
            if abs(float(val.get("Cu_O_bond_length", 0)) - tgt.get("Cu_O_bond_length", 0)) <= tol_bond:
                passed += 1
            # spin polarization (threshold_or_better)
            total += 1
            sp = float(val.get("spin_polarization", 0))
            if sp >= spin_threshold:
                passed += 1
            # half-metallic: recompute from spin_polarization and magnetic state
            total += 1
            fm = (val.get("stable_magnetic_state") == "FM")
            hm = (sp >= spin_threshold) and fm
            if hm:
                passed += 1
        if total == 0:
            return 0.0
        return passed / total


# === block: score_1 (check id='step_05') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        targets = step.get("targets", {})
        tols = step.get("tolerances", {})
        tol_gap = tols.get("band_gap_abs", 0.05)
        tol_de = tols.get("deltaE_abs", 0.1)
        sub_keys = ["10-0", "5-0"]
        if not isinstance(artifact, dict) or not all(k in artifact for k in sub_keys):
            return 0.0
        total = 0
        passed = 0
        for key in sub_keys:
            tgt = targets.get(key, {})
            val = artifact.get(key)
            if not isinstance(val, dict):
                continue
            # magnetic state exact
            total += 1
            if val.get("stable_magnetic_state") == tgt.get("stable_magnetic_state"):
                passed += 1
            # band gap
            total += 1
            if abs(float(val.get("band_gap", 0)) - tgt.get("band_gap", 0)) <= tol_gap:
                passed += 1
            # deltaE: sign must match target (negative), magnitude within tolerance
            total += 1
            de_val = float(val.get("energy_difference_deltaE", 0))
            de_tgt = tgt.get("energy_difference_deltaE", 0)
            if (de_val * de_tgt > 0) and abs(de_val - de_tgt) <= tol_de:
                passed += 1
            # semiconducting: recompute from band_gap > 0.05 and AFM state
            total += 1
            gap = float(val.get("band_gap", 0))
            afm = (val.get("stable_magnetic_state") == "AFM")
            if (gap > 0.05) and afm:
                passed += 1
        if total == 0:
            return 0.0
        return passed / total


# === block: score_2 (check id='step_06') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        expected = step.get("expected_configs", ["a","b","c"])
        targets = step.get("targets", {})
        tols = step.get("tolerances", {})
        tol_mag = tols.get("total_magnetic_moment_abs", 0.1)
        tol_cu = tols.get("Cu_partial_magnetic_moment_abs", 0.05)
        spin_th = tols.get("spin_polarization_threshold", 0.95)
        if not isinstance(artifact, list):
            return 0.0
        config_map = {}
        for item in artifact:
            if isinstance(item, dict) and "configuration_id" in item:
                config_map[item["configuration_id"]] = item
        total = 0
        passed = 0
        for cfg_id in expected:
            tgt = targets.get(cfg_id, {})
            val = config_map.get(cfg_id)
            if not isinstance(val, dict):
                total += 4
                continue
            # state
            total += 1
            if val.get("stable_magnetic_state") == tgt.get("stable_magnetic_state"):
                passed += 1
            # total_mag
            total += 1
            if abs(float(val.get("total_magnetic_moment", 0)) - tgt.get("total_magnetic_moment", 0)) <= tol_mag:
                passed += 1
            # cu partial
            total += 1
            if abs(float(val.get("Cu_partial_magnetic_moment", 0)) - tgt.get("Cu_partial_magnetic_moment", 0)) <= tol_cu:
                passed += 1
            # spin polarization
            total += 1
            sp = float(val.get("spin_polarization", 0))
            if sp >= spin_th:
                passed += 1
        if total == 0:
            return 0.0
        return passed / total


_SCORERS = {
    'step_04': score_0,
    'step_05': score_1,
    'step_06': score_2,
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
