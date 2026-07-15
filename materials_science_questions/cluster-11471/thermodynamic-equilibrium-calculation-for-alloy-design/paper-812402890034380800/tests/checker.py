import os
import json
import csv

# === author imports / helpers ===
import os, json, re


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


# === block: score_0 (check id='step03_phase_fractions') ===
def score_0(artifact, step, ctx):
    data = artifact  # already parsed JSON dict
    step_target = step["target"]

    def in_range(val, low, high):
        return 1.0 if low <= val <= high else 0.0

    scores = []

    ferrite = data.get("alloy1_vol_frac_ferrite_850C")
    scores.append(in_range(ferrite, step_target["alloy1_vol_frac_ferrite_850C"]["min"], step_target["alloy1_vol_frac_ferrite_850C"]["max"]))

    m7c3 = data.get("alloy1_vol_frac_M7C3_850C")
    scores.append(in_range(m7c3, step_target["alloy1_vol_frac_M7C3_850C"]["min"], step_target["alloy1_vol_frac_M7C3_850C"]["max"]))

    stable = data.get("alloy2_stable_phase_at_800C", "").strip()
    expected_stable = step_target["alloy2_stable_phase_at_800C"]["expected"]
    scores.append(1.0 if stable == expected_stable else 0.0)

    aust = data.get("alloy1_vol_frac_austenite_1300C")
    scores.append(in_range(aust, step_target["alloy1_vol_frac_austenite_1300C"]["min"], step_target["alloy1_vol_frac_austenite_1300C"]["max"]))

    score = sum(scores) / len(scores)
    return score


# === block: score_1 (check id='step04_partition_coefficient') ===
def score_1(artifact, step, ctx):
    data = artifact
    step_target = step["target"]
    evid_file = os.path.join("/app/outputs", step.get("evidence_file", ""))

    # try recompute from process evidence (load-bearing path)
    if os.path.exists(evid_file):
        try:
            with open(evid_file) as f:
                metastable = json.load(f)
            # metastable format: list of {temperature, phases: {phase_name: {atomic_fraction: {element: value}}}}
            # find entry at 1300°C
            def find_t(entries, target_t, tol=5.0):
                for e in entries:
                    if abs(e.get("temperature", 0) - target_t) <= tol:
                        return e
                return None
            entry = find_t(metastable, 1300.0)
            if entry and "phases" in entry:
                phases = entry["phases"]
                aust_cr = phases.get("FCC_A1", {}).get("atomic_fraction", {}).get("Cr")
                m7c3_cr = phases.get("M7C3", {}).get("atomic_fraction", {}).get("Cr")
                if aust_cr is not None and m7c3_cr is not None and aust_cr > 0:
                    k = m7c3_cr / aust_cr
                    # compare recomputed k to paper acceptable range
                    vmin = step_target["Cr_partition_coefficient_1300C"]["min"]
                    vmax = step_target["Cr_partition_coefficient_1300C"]["max"]
                    return 1.0 if vmin <= k <= vmax else 0.0
        except Exception:
            pass  # fallback to reported value

    # fallback: compare reported value
    val = data.get("Cr_partition_coefficient_1300C")
    if val is None:
        return 0.0
    vmin = step_target["Cr_partition_coefficient_1300C"]["min"]
    vmax = step_target["Cr_partition_coefficient_1300C"]["max"]
    return 1.0 if vmin <= val <= vmax else 0.0


# === block: score_2 (check id='step06_silicon_effect') ===
def score_2(artifact, step, ctx):
    text = artifact.strip()
    expected = step["target"]["expected"]
    return 1.0 if text == expected else 0.0


_SCORERS = {
    'step03_phase_fractions': score_0,
    'step04_partition_coefficient': score_1,
    'step06_silicon_effect': score_2,
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
