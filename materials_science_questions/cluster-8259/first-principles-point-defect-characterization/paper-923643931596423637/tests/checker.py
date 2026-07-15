import os
import json
import csv

# === author imports / helpers ===
import json, math


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


# === block: score_0 (check id='results_systems') ===
def score_0(artifact, step, ctx):
    sys_list = artifact.get("systems", [])
    if not sys_list:
        return 0.0
    expected = step.get("expected_systems", [])
    if not expected:
        return 0.0
    tol_ads = step.get("tolerance_E_ads", 0.05)
    tol_f = step.get("tolerance_E_Fermi", 0.02)
    agent_by_key = {}
    for s in sys_list:
        key = (s.get("surface",""), s.get("adsorbate",""))
        agent_by_key[key] = s
    total_score = 0.0
    n = len(expected)
    if n == 0:
        return 1.0
    for exp in expected:
        key = (exp["surface"], exp["adsorbate"])
        agent_s = agent_by_key.get(key)
        if agent_s is None:
            continue
        s_val = 0.0
        try:
            if abs(float(agent_s.get("E_ads", 0.0)) - exp["E_ads"]) <= tol_ads:
                s_val += 0.5
            if abs(float(agent_s.get("E_Fermi", 0.0)) - exp["E_Fermi"]) <= tol_f:
                s_val += 0.5
        except (ValueError, KeyError, TypeError):
            s_val = 0.0
        total_score += s_val
    return total_score / n


# === block: score_1 (check id='results_reactions') ===
def score_1(artifact, step, ctx):
    rx_list = artifact.get("reaction_energies", [])
    expected = step.get("expected_reactions", [])
    if not expected:
        return 1.0
    agent_by_rx = {}
    for r in rx_list:
        key = str(r.get("reaction", "")).strip().lower().replace('→', '->')
        agent_by_rx[key] = r
    tol = step.get("tolerance", 0.05)
    total = 0.0
    for exp in expected:
        key = exp["reaction"].strip().lower().replace('→', '->')
        arx = agent_by_rx.get(key)
        if arx is None:
            continue
        try:
            if abs(float(arx.get("delta_E", 0.0)) - exp["delta_E"]) <= tol:
                total += 1.0
        except (ValueError, KeyError, TypeError):
            pass
    return total / len(expected) if expected else 1.0


# === block: score_2 (check id='band_structure_O_V') ===
def score_2(artifact, step, ctx):
    kpath = artifact.get("kpath", [])
    bands = artifact.get("bands", [])
    if not kpath or not bands:
        return 0.0
    # find Gamma point (minimum |k|)
    gamma_idx = None
    min_norm = float('inf')
    for i, k in enumerate(kpath):
        if len(k) >= 3:
            norm = math.sqrt(k[0]**2 + k[1]**2 + k[2]**2)
        elif len(k) >= 2:
            norm = math.sqrt(k[0]**2 + k[1]**2)
        elif len(k) == 1:
            norm = abs(k[0])
        else:
            norm = 0.0
        if norm < min_norm:
            min_norm = norm
            gamma_idx = i
    if gamma_idx is None:
        return 0.0
    vals = []
    for band in bands:
        if gamma_idx < len(band):
            vals.append(band[gamma_idx])
    if not vals:
        return 0.0
    min_abs = min(abs(v) for v in vals)
    tol = step.get("tolerance", 0.05)
    return 1.0 if min_abs <= tol else 0.0


_SCORERS = {
    'results_systems': score_0,
    'results_reactions': score_1,
    'band_structure_O_V': score_2,
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
