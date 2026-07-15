import os
import json
import csv

# === author imports / helpers ===
import json
import os


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


# === block: score_0 (check id='results') ===
def score_0(artifact, step, ctx):
    gold = step.get('gold', {})
    tol = step.get('tolerances', {})
    required_keys = ['minimum_phonon_frequency', 'elastic_stability', 'magnetic_ground_state',
                     'energy_differences', 'spin_up_bandgap', 'spin_down_metallic', 'curie_temperature']
    if not all(k in artifact for k in required_keys):
        return 0.0
    scores = []
    phonon_val = artifact.get('minimum_phonon_frequency')
    if phonon_val is None:
        scores.append(0.0)
    else:
        threshold = tol.get('minimum_phonon_frequency_threshold', 0.0)
        if phonon_val > threshold:
            scores.append(1.0)
        else:
            scores.append(0.0)
    elastic = artifact.get('elastic_stability')
    if elastic is None:
        scores.append(0.0)
    elif bool(elastic) == gold['elastic_stability']:
        scores.append(1.0)
    else:
        scores.append(0.0)
    mgs = artifact.get('magnetic_ground_state')
    if mgs is None:
        scores.append(0.0)
    elif mgs == gold['magnetic_ground_state']:
        scores.append(1.0)
    else:
        scores.append(0.0)
    ed = artifact.get('energy_differences')
    if not isinstance(ed, dict):
        scores.append(0.0)
    else:
        diff_thresh = tol.get('energy_differences_threshold', 0.1)
        ed_keys = ['FM_vs_AFM1', 'FM_vs_AFM2', 'FM_vs_AFM3', 'FM_vs_NM']
        ed_scores = []
        for k in ed_keys:
            val = ed.get(k)
            if isinstance(val, (int, float)) and val > diff_thresh:
                ed_scores.append(1.0)
            else:
                ed_scores.append(0.0)
        scores.append(sum(ed_scores) / len(ed_scores) if ed_scores else 0.0)
    bandgap = artifact.get('spin_up_bandgap')
    if bandgap is None:
        scores.append(0.0)
    else:
        if bandgap > tol.get('spin_up_bandgap_threshold', 0.1):
            scores.append(1.0)
        else:
            scores.append(0.0)
    sdm = artifact.get('spin_down_metallic')
    if sdm is None:
        scores.append(0.0)
    elif bool(sdm) == gold['spin_down_metallic']:
        scores.append(1.0)
    else:
        scores.append(0.0)
    tc = artifact.get('curie_temperature')
    if isinstance(tc, (int, float)):
        target = gold.get('curie_temperature', 120)
        hr = tol.get('curie_temperature_half_range', 40)
        if abs(tc - target) <= hr:
            scores.append(1.0)
        else:
            scores.append(0.0)
    else:
        scores.append(0.0)
    return sum(scores) / len(scores) if scores else 0.0


_SCORERS = {
    'results': score_0,
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
