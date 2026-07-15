import os
import json
import csv

# === author imports / helpers ===
import math
from statistics import mean


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


# === block: score_0 (check id='pdos_check') ===
def score_0(artifact, step, ctx):
    best = min(artifact, key=lambda r: abs(float(r['energy'])-0.0))
    total = float(best['total_DOS'])
    pz = float(best['B_pz'])
    fraction = pz/total if total != 0 else float('inf')
    pz_score = 1.0 if fraction < 0.5 else 0.0
    gold = step.get('gold_total_dos', 0.21)
    tol = step.get('tol_relative_dos', 0.10)
    rel_err = abs(total - gold) / gold if gold != 0 else 1.0
    if rel_err <= tol:
        dos_score = 1.0
    elif rel_err <= 2*tol:
        dos_score = 0.5
    else:
        dos_score = 0.0
    return pz_score * 0.2 + dos_score * 0.8


# === block: score_1 (check id='phonon_check') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    required_keys = ['E1u', 'A2u', 'E2g', 'B1g']
    if not all(k in artifact for k in required_keys):
        return 0.0
    structure_score = 1.0
    for key, expected_len in [('E1u',2), ('A2u',1), ('E2g',2), ('B1g',1)]:
        val = artifact.get(key)
        if not isinstance(val, list) or len(val) != expected_len:
            structure_score = 0.0
            break
    gold = step.get('gold_frequencies', {"E1u":328,"A2u":419,"E2g":665,"B1g":679})
    tol = step.get('tol_abs_cm', 25)
    mode_scores = []
    for key in required_keys:
        arr = artifact[key]
        avg = mean(float(v) for v in arr)
        g = gold[key]
        diff = abs(avg - g)
        if diff <= tol:
            mode_score = 1.0
        elif diff <= 2*tol:
            mode_score = 0.5
        else:
            mode_score = 0.0
        mode_scores.append(mode_score)
    avg_mode_score = sum(mode_scores)/len(mode_scores) if mode_scores else 0.0
    return structure_score * 0.1 + avg_mode_score * 0.9


_SCORERS = {
    'pdos_check': score_0,
    'phonon_check': score_1,
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
