import os
import json
import csv

# === author imports / helpers ===
import csv, math


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
    gold_info = {}
    for step in spec.get('steps', []):
        sid = step.get('id', '')
        gold_info[sid] = step.get('gold_data', {})
    return gold_info


# === block: score_0 (check id='step_surface_energies') ===
def score_0(artifact, step, ctx):
    import os, csv

    artifact_parsed = {}
    if artifact is None or len(artifact) == 0:
        # fallback: read raw CSV with manual quoting to handle commas in the termination field
        path = '/app/outputs/surface_energies.csv'
        if os.path.exists(path):
            with open(path, 'r', newline='') as f:
                reader = csv.reader(f)
                headers = next(reader, None)
                if headers and len(headers) >= 3:
                    for row in reader:
                        if len(row) >= 3:
                            surf = row[0].strip()
                            term = ','.join(row[1:-1]).strip()
                            try:
                                energy = float(row[-1].strip())
                            except (ValueError, TypeError):
                                continue
                            artifact_parsed[surf] = energy
    else:
        for row in artifact:
            surf = row.get('surface', '').strip()
            try:
                energy = float(row.get('relaxed_surface_energy_J_m2', ''))
            except (ValueError, TypeError):
                continue
            artifact_parsed[surf] = energy

    data = artifact_parsed

    gold = ctx.get('step_surface_energies', {})
    scores = []
    for surf, info in gold.items():
        target = info['energy']
        tol = info['tolerance']
        if surf in data:
            val = data[surf]
            if val <= target:
                score = 1.0
            else:
                error = val - target
                score = max(0.0, 1.0 - error / tol) if tol > 0 else 0.0
        else:
            score = 0.0
        scores.append(score)

    avg_score = sum(scores) / len(scores) if scores else 0.0

    lowest_surface = step.get('ordering_rule', {}).get('lowest_surface', '')
    order_score = 0.0
    if data:
        min_surf = min(data, key=data.get)
        if min_surf == lowest_surface:
            order_score = 1.0

    final_score = 0.7 * avg_score + 0.3 * order_score
    return min(max(final_score, 0.0), 1.0)


# === block: score_1 (check id='step_attachment_energies') ===
def score_1(artifact, step, ctx):
    data = {}
    for row in artifact:
        surf = row.get('surface', '').strip()
        try:
            energy = float(row.get('relaxed_attachment_energy_eV', ''))
        except (ValueError, TypeError):
            continue
        data[surf] = energy

    gold = {k: v for k, v in ctx.get('step_attachment_energies', {}).items() if k != '122'}
    scores = []
    for surf, info in gold.items():
        target = info['energy']
        tol = info['tolerance']
        if surf in data:
            val = data[surf]
            if val <= target:
                score = 1.0
            else:
                error = val - target
                score = max(0.0, 1.0 - error / tol) if tol > 0 else 0.0
        else:
            score = 0.0
        scores.append(score)

    avg_score = sum(scores) / len(scores) if scores else 0.0

    lowest_surface = step.get('ordering_rule', {}).get('lowest_surface', '')
    order_score = 0.0
    if data:
        min_surf = min(data, key=data.get)
        if min_surf == lowest_surface:
            order_score = 1.0

    final_score = 0.7 * avg_score + 0.3 * order_score
    return min(max(final_score, 0.0), 1.0)


_SCORERS = {
    'step_surface_energies': score_0,
    'step_attachment_energies': score_1,
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
