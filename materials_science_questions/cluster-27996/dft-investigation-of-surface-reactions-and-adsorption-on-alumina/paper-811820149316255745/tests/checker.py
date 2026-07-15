import os
import json
import csv

# === author imports / helpers ===
import os
import json
import csv
import math


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


# === block: score_0 (check id='ads_des_check') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    ref = step.get('reference', {})
    tol = float(step.get('tolerance', 0.15))
    keys = ['E_ads_AlCl', 'E_des_AlCl', 'E_des_AlCl3']
    scores = []
    for k in keys:
        if k not in artifact:
            scores.append(0.0)
            continue
        try:
            val = float(artifact[k])
        except (TypeError, ValueError):
            scores.append(0.0)
            continue
        ref_val = ref.get(k)
        if ref_val is None:
            scores.append(1.0)
            continue
        diff = abs(val - ref_val)
        if diff <= tol:
            scores.append(1.0)
        else:
            scores.append(max(0.0, 1.0 - (diff - tol) / tol))
    avg = sum(scores) / len(scores) if scores else 0.0
    return avg


# === block: score_1 (check id='reaction_steps_check') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, list) or not artifact:
        return 0.0
    ref = step.get('reference', {})
    tol = float(step.get('tolerance', 0.2))
    scores = []
    for row in artifact:
        sid = row.get('step_id', '').strip()
        if sid not in ref:
            continue
        try:
            val = float(row.get('reaction_energy', 0.0))
        except (TypeError, ValueError):
            scores.append(0.0)
            continue
        ref_val = ref[sid]
        diff = abs(val - ref_val)
        if diff <= tol:
            scores.append(1.0)
        else:
            scores.append(max(0.0, 1.0 - (diff - tol) / tol))
    # ensure all expected steps are present
    for sid in ref:
        present = any(r.get('step_id', '').strip() == sid for r in artifact)
        if not present:
            scores.append(0.0)
    avg = sum(scores) / len(scores) if scores else 0.0
    return avg


# === block: score_2 (check id='general_energies_check') ===
def score_2(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    ref = step.get('reference', {})
    tol = float(step.get('tolerance', 0.2))
    mechanisms = ['mechanism_A', 'mechanism_B', 'mechanism_C']
    energy_scores = []
    for m in mechanisms:
        mech = artifact.get(m)
        if not isinstance(mech, dict):
            energy_scores.append(0.0)
            continue
        ref_mech = ref.get(m, {})
        for key in ['surface_only_energy', 'general_energy']:
            try:
                val = float(mech.get(key, 0.0))
            except (TypeError, ValueError):
                energy_scores.append(0.0)
                continue
            ref_val = ref_mech.get(key, 0.0)
            diff = abs(val - ref_val)
            if diff <= tol:
                energy_scores.append(1.0)
            else:
                energy_scores.append(max(0.0, 1.0 - (diff - tol) / tol))
    energy_avg = sum(energy_scores) / len(energy_scores) if energy_scores else 0.0
    # ordering check: general_energy(C) < general_energy(B) < general_energy(A)
    ordering_ok = False
    try:
        ge_a = float(artifact.get('mechanism_A', {}).get('general_energy', 0.0))
        ge_b = float(artifact.get('mechanism_B', {}).get('general_energy', 0.0))
        ge_c = float(artifact.get('mechanism_C', {}).get('general_energy', 0.0))
        if ge_c < ge_b < ge_a:
            ordering_ok = True
    except (TypeError, ValueError):
        pass
    ordering_score = 1.0 if ordering_ok else 0.0
    # combine: 90% energies, 10% ordering
    return 0.9 * energy_avg + 0.1 * ordering_score


_SCORERS = {
    'ads_des_check': score_0,
    'reaction_steps_check': score_1,
    'general_energies_check': score_2,
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
