import os
import json
import csv

# === author imports / helpers ===
import json, math, re


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


# === block: score_0 (check id='cascade_lifetime') ===
def score_0(artifact, step, ctx):
    try:
        val = float(artifact.strip().splitlines()[0])
    except:
        return 0.0
    threshold = step.get("threshold_lifetime_ps", 1.0)
    ref = step.get("reference_lifetime_ps", 0.1)
    tol = step.get("reference_tolerance_ps", 0.05)
    partial_low = step.get("partial_threshold_ps", 0.5)
    if val > threshold:
        return 0.0
    score = 0.5
    if val <= ref + tol:
        score += 0.5
    elif val <= partial_low:
        score += 0.25
    return score


# === block: score_1 (check id='displacement_summary') ===
def score_1(artifact, step, ctx):
    energies = [("0.25", 0.25), ("0.5", 0.5), ("1", 1), ("5", 5), ("10", 10), ("30", 30)]
    required = [e[0] for e in energies]
    if not all(k in artifact for k in required):
        return 0.0
    effs = []
    for key, e_keV in energies:
        td = artifact[key]["total_displacements"]
        E = e_keV * 1000.0
        recomputed = td / (0.4 * E / 22.0)
        effs.append(recomputed)
    mono = 1.0
    for i in range(len(effs)-1):
        if effs[i] + 1e-9 < effs[i+1]:
            mono = 0.0
            break
    eff025 = effs[0]
    ref025 = step.get("ref_eff_025", 1.0)
    tol025 = step.get("tol_eff_025", 0.2)
    score025 = 1.0 if abs(eff025 - ref025) <= tol025 else 0.0
    eff30 = effs[-1]
    ref30 = step.get("ref_eff_30", 0.37)
    tol30 = step.get("tol_eff_30", 0.1)
    score30 = 1.0 if abs(eff30 - ref30) <= tol30 else 0.0
    ratio = artifact["10"].get("ratio_C_Si_interstitials", -1)
    ratio_min = step.get("ratio_min", 3.0)
    ratio_max = step.get("ratio_max", 7.0)
    score_ratio = 1.0 if ratio_min <= ratio <= ratio_max else 0.0
    consistency_tol = step.get("consistency_tol", 0.01)
    cons_passes = 0
    for idx, key in enumerate(required):
        reported = artifact[key]["efficiency"]
        if abs(reported - effs[idx]) / (abs(reported) + 1e-12) <= consistency_tol:
            cons_passes += 1
    score_cons = cons_passes / len(required)
    # anti-site fraction check (hidden range from paper: 10-20%)
    anti_min = step.get("anti_site_fraction_min", 0.1)
    anti_max = step.get("anti_site_fraction_max", 0.2)
    anti_passes = 0
    num_energies = len(required)
    for key in required:
        frac = artifact[key].get("anti_site_fraction", None)
        if frac is not None and anti_min <= frac <= anti_max:
            anti_passes += 1
    score_anti = anti_passes / num_energies if num_energies > 0 else 0.0
    total = 0.3 * mono + 0.2 * score025 + 0.2 * score30 + 0.15 * score_ratio + 0.05 * score_cons + 0.1 * score_anti
    return total


# === block: score_2 (check id='cluster_summary') ===
def score_2(artifact, step, ctx):
    try:
        num = int(re.findall(r'\d+', artifact)[0])
    except:
        return 0.0
    if num <= 3:
        return 1.0
    elif num <= 5:
        return 0.5
    else:
        return 0.0


_SCORERS = {
    'cascade_lifetime': score_0,
    'displacement_summary': score_1,
    'cluster_summary': score_2,
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
