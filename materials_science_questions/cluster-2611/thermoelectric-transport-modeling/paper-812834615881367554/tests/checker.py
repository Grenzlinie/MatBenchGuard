import os
import json
import csv

# === author imports / helpers ===
import re


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


# === block: score_0 (check id='check_band_gaps') ===
def score_0(artifact, step, ctx):
    targets = step['target']
    tol = step.get('tolerance_abs', 0.0)
    fields = step.get('fields', [])
    # The paper only reports band gaps for pristine, 2%, and 3%; the 1% gap is not traceable,
    # so we omit it from the exact-match check and rely on the separate trend check.
    fields_to_check = [f for f in fields if f != 'band_gap_1pct']
    if not isinstance(artifact, dict) or not fields_to_check:
        return 0.0
    sub_scores = []
    for f in fields_to_check:
        val = artifact.get(f)
        tgt = targets.get(f)
        if val is None or tgt is None:
            sub_scores.append(0.0)
            continue
        try:
            diff = abs(float(val) - float(tgt))
        except (ValueError, TypeError):
            sub_scores.append(0.0)
            continue
        sub_scores.append(1.0 if diff <= tol else 0.0)
    return sum(sub_scores) / len(sub_scores) if sub_scores else 0.0


# === block: score_1 (check id='check_effective_masses') ===
def score_1(artifact, step, ctx):
    targets = step['target']
    tols_rel = step.get('tolerance_relative', {})
    fields = step.get('fields', [])
    if not isinstance(artifact, dict) or not fields:
        return 0.0
    sub_scores = []
    for f in fields:
        val = artifact.get(f)
        tgt = targets.get(f)
        rtol = tols_rel.get(f, 0.2)
        if val is None or tgt is None:
            sub_scores.append(0.0)
            continue
        try:
            diff_rel = abs(float(val) - float(tgt)) / abs(float(tgt))
        except (ValueError, TypeError, ZeroDivisionError):
            sub_scores.append(0.0)
            continue
        sub_scores.append(1.0 if diff_rel <= rtol else 0.0)
    return sum(sub_scores) / len(sub_scores) if sub_scores else 0.0


# === block: score_2 (check id='check_phonon_softening') ===
def score_2(artifact, step, ctx):
    field = step.get('field', 'phonon_softening_description')
    keywords = step.get('keywords', [])
    desc = artifact.get(field, '')
    if not isinstance(desc, str) or not desc.strip():
        return 0.0
    desc_lower = desc.lower()
    all_found = True
    for kw in keywords:
        if not re.search(kw, desc_lower):
            all_found = False
            break
    return 1.0 if all_found else 0.0


# === block: score_3 (check id='check_bandgap_trend') ===
def score_3(artifact, step, ctx):
    trends = step.get('trend', [])
    if not isinstance(artifact, dict) or not trends:
        return 0.0
    all_ok = True
    for t in trends:
        from_val = artifact.get(t['from_field'])
        to_val = artifact.get(t['to_field'])
        if from_val is None or to_val is None:
            return 0.0
        try:
            if not (float(to_val) > float(from_val)):
                all_ok = False
                break
        except (ValueError, TypeError):
            return 0.0
    return 1.0 if all_ok else 0.0


# === block: score_4 (check id='check_effmass_trend') ===
def score_4(artifact, step, ctx):
    trends = step.get('trend', [])
    if not isinstance(artifact, dict) or not trends:
        return 0.0
    all_ok = True
    for t in trends:
        from_val = artifact.get(t['from_field'])
        to_val = artifact.get(t['to_field'])
        if from_val is None or to_val is None:
            return 0.0
        try:
            if not (float(to_val) > float(from_val)):
                all_ok = False
                break
        except (ValueError, TypeError):
            return 0.0
    return 1.0 if all_ok else 0.0


_SCORERS = {
    'check_band_gaps': score_0,
    'check_effective_masses': score_1,
    'check_phonon_softening': score_2,
    'check_bandgap_trend': score_3,
    'check_effmass_trend': score_4,
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
