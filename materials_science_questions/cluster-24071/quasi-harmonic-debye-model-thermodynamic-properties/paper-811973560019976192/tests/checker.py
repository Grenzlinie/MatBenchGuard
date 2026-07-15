import os
import json
import csv

# === author imports / helpers ===
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


# === block: score_0 (check id='step_ir_peaks') ===
def score_0(artifact, step, ctx):
    def _canon_direction(d):
        d = d.strip().lower().replace(' ', '_')
        mapping = {'in_plane': 'in_plane', 'inplane': 'in_plane', 'in-plane': 'in_plane', 'out_of_plane': 'out_of_plane', 'outofplane': 'out_of_plane', 'out-of-plane': 'out_of_plane', 'mixed': 'mixed', 'in_and_out_of_plane': 'mixed'}
        return mapping.get(d, d)

    def _parse_species(s):
        return {sp.strip().lower() for sp in s.split(',') if sp.strip()}

    gold_peaks = step.get('gold_peaks', [])
    freq_tol = step.get('freq_tolerance', 8.0)
    agent = artifact  # list of dicts with 'frequency', 'direction', 'dominant_species'
    if not gold_peaks:
        return 0.0

    # Build list of agent peaks: list of (freq, direction_canon, species_set, index)
    agent_peaks = []
    for row in agent:
        try:
            freq = float(row.get('frequency', None))
            direction = _canon_direction(row.get('direction', ''))
            species = _parse_species(row.get('dominant_species', ''))
            # Only consider peaks below or at 200 cm-1 (task scope)
            if freq <= 200:
                agent_peaks.append((freq, direction, species))
        except (ValueError, TypeError):
            continue

    matched_gold = 0
    used = [False] * len(agent_peaks)
    for gp in gold_peaks:
        gf = float(gp['frequency'])
        gd = _canon_direction(gp['direction'])
        gs = _parse_species(gp['dominant_species'])
        for i, ap in enumerate(agent_peaks):
            if used[i]:
                continue
            if abs(ap[0] - gf) <= freq_tol and ap[1] == gd and ap[2] == gs:
                matched_gold += 1
                used[i] = True
                break

    return matched_gold / len(gold_peaks)


# === block: score_1 (check id='step_thermo') ===
def score_1(artifact, step, ctx):
    gold = step.get('gold', {})
    tolerances = step.get('tolerances_abs', {})
    artifact = artifact  # dict
    fields = ['Cv', 'S', 'U', 'F']
    if not gold or not tolerances:
        return 0.0
    matches = 0
    for field in fields:
        val = artifact.get(field)
        if val is None:
            continue
        try:
            diff = abs(float(val) - float(gold[field]))
            if diff <= float(tolerances[field]):
                matches += 1
        except (TypeError, KeyError, ValueError):
            continue
    return matches / len(fields)


_SCORERS = {
    'step_ir_peaks': score_0,
    'step_thermo': score_1,
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
