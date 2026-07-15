import os
import json
import csv

# === author imports / helpers ===
import math
import json

AUTOKCAL = 627.509

def _find_key(energies, patterns):
    """Return the first energy dict whose key contains all pattern substrings (case-insensitive), or None."""
    for key in energies:
        key_lower = key.lower()
        if all(p.lower() in key_lower for p in patterns):
            return energies[key]
    return None


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


# === block: score_0 (check id='reaction1_hf') ===
def score_0(artifact, step, ctx):
    try:
        energies = artifact["total_energies"]
        e_d3h = _find_key(energies, ["SiH5", "D3h"])
        e_super = _find_key(energies, ["SiH4", "H-", "200 au"])
        if e_d3h is None or e_super is None:
            return 0.0
        val_kcal = (e_d3h["hf"] - e_super["hf"]) * AUTOKCAL
        target = step.get("target", None)
        tol = step.get("tolerance_abs", 1.0)
        if target is None:
            return 0.0
        diff = abs(val_kcal - target)
        score = max(0.0, 1.0 - diff / tol) if tol > 0 else (1.0 if diff == 0 else 0.0)
        return float(score)
    except Exception:
        return 0.0


# === block: score_1 (check id='reaction1_corr') ===
def score_1(artifact, step, ctx):
    try:
        energies = artifact["total_energies"]
        e_d3h = _find_key(energies, ["SiH5", "D3h"])
        e_super = _find_key(energies, ["SiH4", "H-", "200 au"])
        if e_d3h is None or e_super is None:
            return 0.0
        val_kcal = (e_d3h["correlated"] - e_super["correlated"]) * AUTOKCAL
        target = step.get("target", None)
        tol = step.get("tolerance_abs", 1.0)
        if target is None:
            return 0.0
        diff = abs(val_kcal - target)
        score = max(0.0, 1.0 - diff / tol) if tol > 0 else (1.0 if diff == 0 else 0.0)
        return float(score)
    except Exception:
        return 0.0


# === block: score_2 (check id='pseudorotation_hf') ===
def score_2(artifact, step, ctx):
    try:
        energies = artifact["total_energies"]
        e_c4v = _find_key(energies, ["SiH5", "C4v"])
        e_d3h = _find_key(energies, ["SiH5", "D3h"])
        if e_c4v is None or e_d3h is None:
            return 0.0
        val_kcal = (e_c4v["hf"] - e_d3h["hf"]) * AUTOKCAL
        target = step.get("target", None)
        tol = step.get("tolerance_abs", 1.0)
        if target is None:
            return 0.0
        diff = abs(val_kcal - target)
        score = max(0.0, 1.0 - diff / tol) if tol > 0 else (1.0 if diff == 0 else 0.0)
        return float(score)
    except Exception:
        return 0.0


# === block: score_3 (check id='pseudorotation_corr') ===
def score_3(artifact, step, ctx):
    try:
        energies = artifact["total_energies"]
        e_c4v = _find_key(energies, ["SiH5", "C4v"])
        e_d3h = _find_key(energies, ["SiH5", "D3h"])
        if e_c4v is None or e_d3h is None:
            return 0.0
        val_kcal = (e_c4v["correlated"] - e_d3h["correlated"]) * AUTOKCAL
        target = step.get("target", None)
        tol = step.get("tolerance_abs", 1.0)
        if target is None:
            return 0.0
        diff = abs(val_kcal - target)
        score = max(0.0, 1.0 - diff / tol) if tol > 0 else (1.0 if diff == 0 else 0.0)
        return float(score)
    except Exception:
        return 0.0


# === block: score_4 (check id='inversion_hf') ===
def score_4(artifact, step, ctx):
    try:
        energies = artifact["total_energies"]
        e_d3h = _find_key(energies, ["SiH3", "D3h"])
        e_c3v = _find_key(energies, ["SiH3", "C3v"])
        if e_d3h is None or e_c3v is None:
            return 0.0
        val_kcal = (e_d3h["hf"] - e_c3v["hf"]) * AUTOKCAL
        target = step.get("target", None)
        tol = step.get("tolerance_abs", 1.0)
        if target is None:
            return 0.0
        diff = abs(val_kcal - target)
        score = max(0.0, 1.0 - diff / tol) if tol > 0 else (1.0 if diff == 0 else 0.0)
        return float(score)
    except Exception:
        return 0.0


# === block: score_5 (check id='inversion_corr') ===
def score_5(artifact, step, ctx):
    try:
        energies = artifact["total_energies"]
        e_d3h = _find_key(energies, ["SiH3", "D3h"])
        e_c3v = _find_key(energies, ["SiH3", "C3v"])
        if e_d3h is None or e_c3v is None:
            return 0.0
        val_kcal = (e_d3h["correlated"] - e_c3v["correlated"]) * AUTOKCAL
        target = step.get("target", None)
        tol = step.get("tolerance_abs", 1.0)
        if target is None:
            return 0.0
        diff = abs(val_kcal - target)
        score = max(0.0, 1.0 - diff / tol) if tol > 0 else (1.0 if diff == 0 else 0.0)
        return float(score)
    except Exception:
        return 0.0


# === block: score_6 (check id='reaction3_hf') ===
def score_6(artifact, step, ctx):
    try:
        energies = artifact["total_energies"]
        e_sih5 = _find_key(energies, ["SiH5", "D3h"])
        e_sih3 = _find_key(energies, ["SiH3", "C3v"])
        e_h2 = _find_key(energies, ["H2"])
        if e_sih5 is None or e_sih3 is None or e_h2 is None:
            return 0.0
        val_kcal = (e_sih5["hf"] - (e_sih3["hf"] + e_h2["hf"])) * AUTOKCAL
        target = step.get("target", None)
        tol = step.get("tolerance_abs", 1.0)
        if target is None:
            return 0.0
        diff = abs(val_kcal - target)
        score = max(0.0, 1.0 - diff / tol) if tol > 0 else (1.0 if diff == 0 else 0.0)
        return float(score)
    except Exception:
        return 0.0


# === block: score_7 (check id='reaction3_corr') ===
def score_7(artifact, step, ctx):
    try:
        energies = artifact["total_energies"]
        e_sih5 = _find_key(energies, ["SiH5", "D3h"])
        e_sih3 = _find_key(energies, ["SiH3", "C3v"])
        e_h2 = _find_key(energies, ["H2"])
        if e_sih5 is None or e_sih3 is None or e_h2 is None:
            return 0.0
        val_kcal = (e_sih5["correlated"] - (e_sih3["correlated"] + e_h2["correlated"])) * AUTOKCAL
        target = step.get("target", None)
        tol = step.get("tolerance_abs", 1.0)
        if target is None:
            return 0.0
        diff = abs(val_kcal - target)
        score = max(0.0, 1.0 - diff / tol) if tol > 0 else (1.0 if diff == 0 else 0.0)
        return float(score)
    except Exception:
        return 0.0


# === block: score_8 (check id='consistency_correlation_formation') ===
def score_8(artifact, step, ctx):
    try:
        energies = artifact["total_energies"]
        e_d3h = _find_key(energies, ["SiH5", "D3h"])
        e_super = _find_key(energies, ["SiH4", "H-", "200 au"])
        if e_d3h is None or e_super is None:
            return 0.0
        delta_hf = (e_d3h["hf"] - e_super["hf"]) * AUTOKCAL
        delta_corr = (e_d3h["correlated"] - e_super["correlated"]) * AUTOKCAL
        return 1.0 if delta_corr < delta_hf else 0.0
    except Exception:
        return 0.0


_SCORERS = {
    'reaction1_hf': score_0,
    'reaction1_corr': score_1,
    'pseudorotation_hf': score_2,
    'pseudorotation_corr': score_3,
    'inversion_hf': score_4,
    'inversion_corr': score_5,
    'reaction3_hf': score_6,
    'reaction3_corr': score_7,
    'consistency_correlation_formation': score_8,
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
