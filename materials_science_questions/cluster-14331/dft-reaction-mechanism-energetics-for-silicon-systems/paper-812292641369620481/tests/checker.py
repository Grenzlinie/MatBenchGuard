import os
import json
import csv

# === author imports / helpers ===
import json, os


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


# === block: score_0 (check id='sic2h4_energies') ===
def score_0(artifact, step, ctx):
        entries = step['config']['entries']
        agent_data = artifact  # already validated list of dicts from output_contract
        energy_scores = []
        for expected in entries:
            match = None
            for d in agent_data:
                if (d.get('isomer') == expected['isomer'] and
                    d.get('symmetry') == expected['symmetry'] and
                    d.get('basis') == expected['basis']):
                    match = d
                    break
            if match is None:
                energy_scores.append(0.0)
                continue
            err = abs(match['total_energy_hartree'] - expected['gold_total'])
            # full credit for err <= 0.001, zero for err >= 0.01
            score = max(0.0, 1.0 - (err - 0.001) / 0.009) if err > 0.001 else 1.0
            energy_scores.append(score)
        energy_score = sum(energy_scores) / len(energy_scores) if energy_scores else 0.0

        # check ordering per basis
        ordering_conf = step['config'].get('ordering', {})
        ordering_scores = []
        for basis, order_list in ordering_conf.items():
            rel_map = {}
            for d in agent_data:
                if d.get('basis') == basis and d.get('isomer') in order_list:
                    rel_map[d['isomer']] = d.get('relative_energy_kcal_per_mol')
            if len(rel_map) < 2:
                ordering_scores.append(1.0)
                continue
            viol = 0
            pairs = len(order_list) - 1
            for i in range(pairs):
                iso_a, iso_b = order_list[i], order_list[i+1]
                if iso_a not in rel_map or iso_b not in rel_map:
                    continue
                rel_a, rel_b = rel_map[iso_a], rel_map[iso_b]
                # require rel_a <= rel_b (more negative first); if rel_b - rel_a < -0.5 kcal => violation
                if rel_b - rel_a < -0.5:
                    viol += 1
            if pairs > 0:
                ordering_scores.append(max(0.0, 1.0 - viol / pairs))
            else:
                ordering_scores.append(1.0)
        ordering_score = sum(ordering_scores) / len(ordering_scores) if ordering_scores else 1.0

        final_score = 0.9 * energy_score + 0.1 * ordering_score
        return final_score


# === block: score_1 (check id='sic2h2_energies') ===
def score_1(artifact, step, ctx):
        entries = step['config']['entries']
        agent_data = artifact
        energy_scores = []
        for expected in entries:
            match = None
            for d in agent_data:
                if (d.get('isomer') == expected['isomer'] and
                    d.get('symmetry') == expected['symmetry'] and
                    d.get('basis') == expected['basis']):
                    match = d
                    break
            if match is None:
                energy_scores.append(0.0)
                continue
            err = abs(match['total_energy_hartree'] - expected['gold_total'])
            score = max(0.0, 1.0 - (err - 0.001) / 0.009) if err > 0.001 else 1.0
            energy_scores.append(score)
        energy_score = sum(energy_scores) / len(energy_scores) if energy_scores else 0.0

        ordering_conf = step['config'].get('ordering', {})
        ordering_scores = []
        for basis, order_list in ordering_conf.items():
            rel_map = {}
            for d in agent_data:
                if d.get('basis') == basis and d.get('isomer') in order_list:
                    rel_map[d['isomer']] = d.get('relative_energy_kcal_per_mol')
            if len(rel_map) < 2:
                ordering_scores.append(1.0)
                continue
            viol = 0
            pairs = len(order_list) - 1
            for i in range(pairs):
                iso_a, iso_b = order_list[i], order_list[i+1]
                if iso_a not in rel_map or iso_b not in rel_map:
                    continue
                rel_a, rel_b = rel_map[iso_a], rel_map[iso_b]
                if rel_b - rel_a < -0.5:
                    viol += 1
            if pairs > 0:
                ordering_scores.append(max(0.0, 1.0 - viol / pairs))
            else:
                ordering_scores.append(1.0)
        ordering_score = sum(ordering_scores) / len(ordering_scores) if ordering_scores else 1.0

        final_score = 0.9 * energy_score + 0.1 * ordering_score
        return final_score


_SCORERS = {
    'sic2h4_energies': score_0,
    'sic2h2_energies': score_1,
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
