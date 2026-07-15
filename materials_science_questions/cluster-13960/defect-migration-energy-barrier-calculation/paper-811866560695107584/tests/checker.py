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
    ctx = {}
    steps = spec.get('steps', [])
    for step in steps:
        sid = step.get('id')
        if 'gold' in step:
            ctx[f'{sid}_gold'] = step['gold']
        if 'tolerance_abs' in step:
            ctx[f'{sid}_tol'] = step['tolerance_abs']
    return ctx


# === block: score_0 (check id='step_01_formation_energies') ===
def score_0(artifact, step, ctx):
    import os, json
    tol = ctx.get('step_01_formation_energies_tol', 0.05)
    gold = ctx.get('step_01_formation_energies_gold')
    if not gold:
        return 0.0
    if not isinstance(artifact, dict):
        return 0.0
    fields = ['bulk_formation_energy', ('layer1','site1'), ('layer1','site2'), ('layer1','site3'),
              ('layer2','site1'), ('layer2','site2'), ('layer2','site3'),
              ('layer3','site1'), ('layer3','site2'), ('layer3','site3'),
              ('layer4','site1'), ('layer4','site2'), ('layer4','site3')]
    ok = 0
    total = 0
    for f in fields:
        if isinstance(f, tuple):
            try:
                v = artifact.get(f[0], {}).get(f[1], None)
                g = gold.get(f[0], {}).get(f[1], None)
            except:
                v = None
                g = None
        else:
            v = artifact.get(f)
            g = gold.get(f)
        total += 1
        if v is None or g is None:
            continue
        if abs(v - g) <= tol:
            ok += 1
        else:
            # partial linear score: 0.5 if within 3*tol
            if abs(v - g) <= 3*tol:
                ok += 0.5
    if total == 0:
        return 0.0
    return ok / total


# === block: score_1 (check id='step_02_activation_energies') ===
def score_1(artifact, step, ctx):
    tol = ctx.get('step_02_activation_energies_tol', 0.1)
    gold = ctx.get('step_02_activation_energies_gold')
    if not gold:
        return 0.0
    if not isinstance(artifact, dict):
        return 0.0
    ok = 0.0
    total = 0.0
    for path_key, gold_pairs in gold.items():
        agent_pairs = artifact.get(path_key)
        if not isinstance(agent_pairs, dict):
            continue
        for pair_key, gval in gold_pairs.items():
            aval = agent_pairs.get(pair_key)
            total += 1
            if aval is None:
                continue
            if abs(aval - gval) <= tol:
                ok += 1.0
            elif abs(aval - gval) <= 3*tol:
                ok += 0.5
    if total == 0:
        return 0.0
    return ok / total


# === block: score_2 (check id='trends') ===
def score_2(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    try:
        layer1 = artifact.get('layer1', {})
        layer2 = artifact.get('layer2', {})
        layer3 = artifact.get('layer3', {})
        layer4 = artifact.get('layer4', {})
        # trend 1: site2 and site3 in layer1 are negative
        neg_ok = (layer1.get('site2', 0) < 0) and (layer1.get('site3', 0) < 0)
        # trend 2: site1 energies increasing: l1 <= l2 <= l3 <= l4
        s1 = layer1.get('site1', None)
        s2 = layer2.get('site1', None)
        s3 = layer3.get('site1', None)
        s4 = layer4.get('site1', None)
        inc_ok = (s1 is not None and s2 is not None and s3 is not None and s4 is not None and
                  s1 <= s2 <= s3 <= s4)
        return (0.5 if neg_ok else 0.0) + (0.5 if inc_ok else 0.0)
    except:
        return 0.0


_SCORERS = {
    'step_01_formation_energies': score_0,
    'step_02_activation_energies': score_1,
    'trends': score_2,
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
