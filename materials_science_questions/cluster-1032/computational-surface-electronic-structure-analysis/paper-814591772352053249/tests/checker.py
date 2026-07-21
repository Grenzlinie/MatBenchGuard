import os
import json
import csv

# === author imports / helpers ===
import csv, os, json, math


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


# === block: score_0 (check id='quasiparticle_bethe') ===
def score_0(artifact, step, ctx):
    data = artifact
    if not data:
        return 0.0
    gold = step.get('gold', {})
    gvals = gold.get('gvals', [0.5,1.0,1.5])
    fillings = gold.get('fillings', [0.0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0])
    tol = gold.get('tolerance_abs', 0.05)
    lookup = {}
    for row in data:
        try:
            g = float(row.get('g', row.get('g', None)))
            fill = float(row.get('filling', row.get('filling', None)))
            z = float(row.get('Z', row.get('Z', None)))
            lookup[(g, fill)] = z
        except Exception:
            pass
    total = 0
    ok = 0
    for g in gvals:
        S = 1.0 / math.sqrt(1 + g**2)
        for n in fillings:
            total += 1
            gold_z = (1 + (S - 1) * n / 2.0) ** 2
            agent_z = lookup.get((g, n))
            if agent_z is not None and abs(agent_z - gold_z) <= tol:
                ok += 1
    if total == 0:
        return 0.0
    return ok / total


# === block: score_1 (check id='layer_densities') ===
def score_1(artifact, step, ctx):
    data = artifact
    if not data:
        return 0.0
    gold = step.get('gold', {})
    tol = gold.get('tolerance_abs', 0.02)
    gold_rows = gold.get('rows', [])
    if not gold_rows:
        return 0.0
    lookup = {}
    for row in data:
        try:
            layer = int(row.get('layer', -1))
            U = float(row.get('U', -1))
            n = float(row.get('n', -100))
            lookup[(layer, U)] = n
        except Exception:
            pass
    total = len(gold_rows)
    ok = 0
    for gr in gold_rows:
        key = (gr['layer'], gr['U'])
        agent_n = lookup.get(key)
        if agent_n is not None and abs(agent_n - gr['n']) <= tol:
            ok += 1
    num_score = ok / total if total > 0 else 0.0
    # structural trends: n1>n2>n3>n4>n5 and n1>1.8
    trend_ok = True
    U_vals = sorted(set(gr['U'] for gr in gold_rows))
    for U in U_vals:
        vals = [lookup.get((l, U)) for l in range(1,6)]
        if any(v is None for v in vals):
            trend_ok = False
            break
        if not (vals[0] > 1.8):
            trend_ok = False
            break
        for i in range(len(vals)-1):
            if not (vals[i] > vals[i+1]):
                trend_ok = False
                break
        if not trend_ok:
            break
    trend_score = 1.0 if trend_ok else 0.0
    return 0.9 * num_score + 0.1 * trend_score


_SCORERS = {
    'quasiparticle_bethe': score_0,
    'layer_densities': score_1,
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
