import os
import json
import csv

# === author imports / helpers ===
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
    gold_step = next(s for s in spec['steps'] if s['id'] == 'check_g0_k_values')
    gold_list = gold_step['target']['inline']['data']
    gold = {row[0]: {'G0': row[1], 'K': row[2]} for row in gold_list}
    return {'gold': gold}


# === block: score_0 (check id='check_g0_k_values') ===
def score_0(artifact, step, ctx):
    tol = step['tolerance_relative']
    passed = 0
    total = 0
    for row in artifact:
        name = row['crystal']
        if name not in ctx['gold']:
            continue
        total += 1
        g0 = float(row['G0'])
        k = float(row['K'])
        g0_gold = ctx['gold'][name]['G0']
        k_gold = ctx['gold'][name]['K']
        ok = True
        if abs(g0_gold) > 1e-12 and abs(g0 - g0_gold) / abs(g0_gold) > tol:
            ok = False
        if abs(k_gold) > 1e-12 and abs(k - k_gold) / abs(k_gold) > tol:
            ok = False
        if ok:
            passed += 1
    if total == 0:
        return 0.0
    return passed / total


# === block: score_1 (check id='check_g0_k_structural') ===
def score_1(artifact, step, ctx):
    constants = {
        'Au': (19.234, 16.314, 4.195),
        'Ag': (12.399, 9.367, 4.612),
        'V':  (22.8, 11.9, 4.26),
        'Nb': (24.6, 13.4, 2.87),
        'Ta': (26.7, 16.1, 8.25),
        'Pb': (4.953, 4.229, 1.490),
    }
    tol = step['tolerance_relative']
    passed = 0
    total = 0
    for row in artifact:
        name = row['crystal']
        if name not in constants:
            continue
        total += 1
        c11, c12, c44 = constants[name]
        G_V = (c11 - c12 + 3*c44) / 5.0
        G_R = (5 * c44 * (c11 - c12)) / (4*c44 + 3*(c11 - c12))
        G_H = (G_V + G_R) / 2.0
        g0 = float(row['G0'])
        if abs(G_H) > 1e-12 and abs(g0 - G_H) / abs(G_H) <= tol:
            passed += 1
    if total == 0:
        return 0.0
    return passed / total


_SCORERS = {
    'check_g0_k_values': score_0,
    'check_g0_k_structural': score_1,
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
