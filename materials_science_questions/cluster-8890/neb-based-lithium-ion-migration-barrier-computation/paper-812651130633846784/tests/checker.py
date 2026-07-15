import os
import json
import csv


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
    gold = None
    for step in spec.get("steps", []):
        if "gold" in step:
            gold = step["gold"]
    return {"gold": gold}


# === block: score_0 (check id='adsorption_diffusion_check') ===
def score_0(artifact, step, ctx):
    artifact_json = artifact
    if not isinstance(artifact_json, dict) or 'adsorption_energies' not in artifact_json or 'diffusion_barrier' not in artifact_json:
        return 0.0
    ads_list = artifact_json['adsorption_energies']
    barrier = artifact_json['diffusion_barrier']
    gold = ctx['gold']
    gold_ads = gold['adsorption_entries']
    gold_dict = {}
    for g in gold_ads:
        gold_dict[(g['species'], g['condition'], g['with_vdw'])] = g
    correct_ads = 0
    total_ads = len(gold_ads)
    sign_ok = True
    ordering_groups = {}
    for entry in ads_list:
        species = entry.get('species')
        condition = entry.get('condition')
        with_vdw = entry.get('with_vdw')
        energy = entry.get('energy_eV')
        if energy is None or not isinstance(energy, (int, float)):
            continue
        key = (species, condition, with_vdw)
        g = gold_dict.get(key)
        if g is not None and abs(energy - g['energy_eV']) <= g.get('tolerance', 0.2):
            correct_ads += 1
        if energy > -1e-6:
            sign_ok = False
        group_key = (condition, with_vdw)
        ordering_groups.setdefault(group_key, []).append((species, energy))
    ordering_ok = True
    for gk, items in ordering_groups.items():
        emap = {s: e for s, e in items}
        if 'Li2S' not in emap or 'S8' not in emap:
            ordering_ok = False
            continue
        min_spec = min(emap, key=emap.get)
        max_spec = max(emap, key=emap.get)
        if min_spec != 'Li2S' or max_spec != 'S8':
            ordering_ok = False
    barrier_ok = False
    if isinstance(barrier, dict) and barrier.get('species') == 'Li2S' and 'barrier_eV' in barrier:
        bval = barrier['barrier_eV']
        gb = gold['diffusion_barrier']
        if bval > 0 and abs(bval - gb['barrier_eV']) <= gb['tolerance']:
            barrier_ok = True
        if bval <= 0:
            sign_ok = False
    ads_score = correct_ads / total_ads if total_ads > 0 else 0.0
    barrier_score = 1.0 if barrier_ok else 0.0
    sign_score = 1.0 if sign_ok else 0.0
    ordering_score = 1.0 if ordering_ok else 0.0
    return 0.6 * ads_score + 0.2 * barrier_score + 0.1 * sign_score + 0.1 * ordering_score


_SCORERS = {
    'adsorption_diffusion_check': score_0,
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
