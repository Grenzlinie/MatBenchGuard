import os
import json
import csv

# === author imports / helpers ===
import tarfile, io


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
    return {"output_dir": "/app/outputs"}


# === block: score_0 (check id='step_computed_results') ===
def score_0(artifact, step, ctx):
    import json, os, tarfile

    # original scoring for this step
    gold = step.get("gold", {})
    tolerances = step.get("tolerances", {})
    tol_sd = tolerances.get("spin_density", 0.02)
    tol_exc = tolerances.get("excitation_energy", 500)
    tol_osc = tolerances.get("oscillator_strength", 0.15)
    complexes = ["PH3-7d+", "6d+", "CH3O-6e+"]
    fields = ["spin_density_Fe1", "spin_density_Fe2", "excitation_energy_cm-1", "oscillator_strength"]
    score_numerical = 0.0
    count = 0
    for com in complexes:
        g = gold.get(com, {})
        a = artifact.get(com, {})
        for f in fields:
            if f in g and f in a:
                diff = abs(a[f] - g[f])
                if "spin_density" in f:
                    tol = tol_sd
                elif "excitation" in f:
                    tol = tol_exc
                elif "oscillator" in f:
                    tol = tol_osc
                if diff <= tol:
                    s = 1.0
                else:
                    s = max(0.0, 1.0 - (diff - tol) / tol)
                score_numerical += s
            count += 1
    if count > 0:
        score_numerical /= count
    else:
        score_numerical = 0.0
    trend_score = 0.0
    try:
        sd_ph3 = artifact["PH3-7d+"]["spin_density_Fe1"]
        sd_6d = artifact["6d+"]["spin_density_Fe1"]
        sd_ch3o = artifact["CH3O-6e+"]["spin_density_Fe1"]
        exc_ph3 = artifact["PH3-7d+"]["excitation_energy_cm-1"]
        exc_6d = artifact["6d+"]["excitation_energy_cm-1"]
        exc_ch3o = artifact["CH3O-6e+"]["excitation_energy_cm-1"]
        trend_correct = 1.0
        if not (sd_ph3 > sd_6d and sd_6d > sd_ch3o):
            trend_correct -= 0.3
        if not (exc_ph3 < exc_6d and exc_ph3 < exc_ch3o):
            trend_correct -= 0.3
        if artifact["PH3-7d+"]["oscillator_strength"] <= 0 or artifact["6d+"]["oscillator_strength"] <= 0 or artifact["CH3O-6e+"]["oscillator_strength"] <= 0:
            trend_correct -= 0.1
        trend_score = max(0.0, trend_correct)
    except (KeyError, TypeError):
        trend_score = 0.0
    score_json = 0.6 * score_numerical + 0.4 * trend_score

    # geometry archive score (replicate scorer to avoid main-loop crash on binary file)
    geom_path = os.path.join(ctx.get("output_dir", "/app/outputs"), "optimized_geometries.tar.gz")
    expected_geom = [
        "neutral/PH3-7d_neutral.xyz",
        "neutral/6d_neutral.xyz",
        "neutral/CH3O-6e_neutral.xyz",
        "cation/PH3-7d_cation.xyz",
        "cation/6d_cation.xyz",
        "cation/CH3O-6e_cation.xyz"
    ]
    score_geom = 0.0
    try:
        with tarfile.open(geom_path, "r:gz") as tar:
            names = set(tar.getnames())
        found = sum(1 for f in expected_geom if f in names)
        if len(expected_geom) > 0:
            score_geom = found / float(len(expected_geom))
    except Exception:
        score_geom = 0.0

    total = 0.9 * score_json + 0.1 * score_geom
    breakdown = {
        "step_computed_results": {"score": score_json, "weight": 0.9},
        "step_geometry_archive": {"score": score_geom, "weight": 0.1}
    }

    os.makedirs("/logs/verifier", exist_ok=True)
    with open("/logs/verifier/reward.txt", "w") as f:
        f.write(str(round(total, 6)))
    with open("/logs/verifier/breakdown.json", "w") as f:
        json.dump(breakdown, f, indent=2)

    # exit cleanly to avoid the main loop crashing on the binary artifact
    os._exit(0)


# === block: score_1 (check id='step_geometry_archive') ===
def score_1(artifact, step, ctx):
    import os, tarfile
    expected = step.get("expected_files", [])
    path = os.path.join(ctx.get("output_dir", "/app/outputs"), step["output_file"])
    try:
        with tarfile.open(path, "r:gz") as tar:
            names = set(tar.getnames())
        found = sum(1 for f in expected if f in names)
        if len(expected) == 0:
            return 0.0
        return found / float(len(expected))
    except Exception:
        return 0.0


_SCORERS = {
    'step_computed_results': score_0,
    'step_geometry_archive': score_1,
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
