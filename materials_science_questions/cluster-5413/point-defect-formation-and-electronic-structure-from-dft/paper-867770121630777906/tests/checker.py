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


# === block: score_0 (check id='formation_energies') ===
def score_0(artifact, step, ctx):
    import json
    artifact = json.loads(artifact) if isinstance(artifact, str) else artifact
    fe = artifact.get('formation_energies', {})
    # Group by charge state; keys like 'ic_0', 'ib_0'
    ic_energies = {}
    ib_energies = {}
    for key, val in fe.items():
        if key.startswith('ic_') and isinstance(val, dict):
            try:
                chg = key.split('_', 1)[1]
                ic_energies[chg] = float(val.get('energy_eV'))
            except:
                pass
        elif key.startswith('ib_') and isinstance(val, dict):
            try:
                chg = key.split('_', 1)[1]
                ib_energies[chg] = float(val.get('energy_eV'))
            except:
                pass
    common_charges = set(ic_energies.keys()) & set(ib_energies.keys())
    if not common_charges:
        return 0.0
    n_total = len(common_charges)
    n_ok = sum(1 for chg in common_charges if ic_energies[chg] < ib_energies[chg])
    return n_ok / n_total


# === block: score_1 (check id='transition_levels') ===
def score_1(artifact, step, ctx):
    import json
    data = artifact if isinstance(artifact, (dict, list)) else json.loads(artifact)
    lower = float(step.get('lower', 2.3))
    upper = float(step.get('upper', 2.9))
    if isinstance(data, list):
        for item in data:
            level = float(item.get('level_eV', 1000))
            if lower <= level <= upper:
                return 1.0
        return 0.0
    else:
        level = float(data.get('level_eV', 1000))
        if lower <= level <= upper:
            return 1.0
        return 0.0


# === block: score_2 (check id='simulated_intensity_profiles') ===
def score_2(artifact, step, ctx):
    import csv
    threshold = float(step.get('threshold', 0.85))
    if not isinstance(artifact, list) or len(artifact) < 2:
        return 0.0
    # find index of maximum intensity_defect_free
    max_intensity = -1.0
    max_idx = -1
    for i, row in enumerate(artifact):
        df_val = float(row.get('intensity_defect_free', -1))
        if df_val > max_intensity:
            max_intensity = df_val
            max_idx = i
    if max_idx < 0:
        return 0.0
    defect_val = float(artifact[max_idx]['intensity_with_defect'])
    ratio = defect_val / max_intensity
    if ratio <= threshold:
        return 1.0
    else:
        # monotonic partial credit: full at ratio <= threshold, decays to 0 at ratio = 1.0
        score = max(0.0, 1.0 - (ratio - threshold) / (1.0 - threshold))
        return score


_SCORERS = {
    'formation_energies': score_0,
    'transition_levels': score_1,
    'simulated_intensity_profiles': score_2,
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
