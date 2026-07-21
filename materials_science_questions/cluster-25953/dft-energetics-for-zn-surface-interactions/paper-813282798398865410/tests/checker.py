import os
import json
import csv

# === author imports / helpers ===
import json


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
        tol = 15.0
        for step in spec.get('steps', []):
            if step['id'] == 'energy_values':
                gold = step.get('gold', {})
                tol = step.get('tolerance_kJmol', 15.0)
                break
        return {'gold': gold, 'tol': tol}


# === block: score_0 (check id='energy_values') ===
def score_0(artifact, step, ctx):
        # artifact is the parsed reaction_energies.json dict
        gold_ = ctx['gold']
        tol = ctx['tol']
        if not gold_ or not isinstance(artifact, dict):
            return 0.0
        n = len(gold_)
        matches = 0
        for key in gold_:
            if key not in artifact:
                continue
            sub = artifact[key]
            if not isinstance(sub, dict) or 'relative_energy_kJmol' not in sub:
                continue
            val = sub['relative_energy_kJmol']
            if not isinstance(val, (int, float)):
                continue
            if abs(val - gold_[key]) <= tol:
                matches += 1.0
        # H2S_a must be exactly 0; if it is present but far, that's caught by tolerance; but we can enforce exact zero separately?
        # We trust tolerance (0±15) is tight enough for reference point.
        return matches / n


# === block: score_1 (check id='trends') ===
def score_1(artifact, step, ctx):
        # artifact is parsed dict
        if not isinstance(artifact, dict):
            return 0.0
        def get_e(k):
            if k not in artifact: return None
            sub = artifact[k]
            if not isinstance(sub, dict) or 'relative_energy_kJmol' not in sub: return None
            v = sub['relative_energy_kJmol']
            return v if isinstance(v, (int,float)) else None
        SH_H_a = get_e('SH_H_a')
        TS3 = get_e('TS3')
        S_2H_b = get_e('S_2H_b')
        TS4 = get_e('TS4')
        S_2H_c = get_e('S_2H_c')
        TS6 = get_e('TS6')
        P1 = get_e('P1')
        P2 = get_e('P2')
        P3 = get_e('P3')
        if None in (SH_H_a, TS3, S_2H_b, TS4, S_2H_c, TS6, P1, P2, P3):
            return 0.0
        c1 = (TS3 - SH_H_a) > 300.0
        ts4_act = TS4 - S_2H_b
        c2 = 200.0 <= ts4_act <= 240.0
        c3 = (TS6 - S_2H_c) < 100.0
        c4 = (P3 < P1 and P3 < P2)
        conditions = [c1, c2, c3, c4]
        return sum(1.0 for c in conditions if c) / len(conditions)


_SCORERS = {
    'energy_values': score_0,
    'trends': score_1,
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
