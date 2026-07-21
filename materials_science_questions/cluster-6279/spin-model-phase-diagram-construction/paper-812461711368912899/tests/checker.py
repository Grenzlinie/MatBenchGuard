import os
import json
import csv

# === author imports / helpers ===
import math, itertools, json


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


# === block: score_0 (check id='step_01_ground_states') ===
def score_0(artifact, step, ctx):
    # Helper psi_value

    def psi_value(dAB, dAC, dBC, delta, perm, pair_idx):
        if pair_idx == 1:
            table = {
                'ABC': dAB + dAC,
                'ACB': dAB + dAC + 2*delta,
                'BAC': dAC + delta,
                'BCA': dAC + 2*delta,
                'CAB': dAB + 2*delta,
                'CBA': dAB + delta
            }
        elif pair_idx == 2:
            table = {
                'ABC': dAB + dBC,
                'ACB': dAB + delta,
                'BAC': dBC + delta,
                'BCA': dAB + 2*delta,
                'CAB': dBC + 2*delta,
                'CBA': dAB + dBC + 2*delta
            }
        else:  # pair_idx == 3
            table = {
                'ABC': dAC + dBC,
                'ACB': dAC + delta,
                'BAC': dAC + dBC + 2*delta,
                'BCA': dBC + 2*delta,
                'CAB': dAC + 2*delta,
                'CBA': dBC + delta
            }
        return table[perm]

    expected_cases = ['case_I', 'case_II', 'case_III', 'case_IV', 'case_V', 'case_VI']
    score = 0
    n = 0
    for case_key in expected_cases:
        if case_key not in artifact:
            continue
        case = artifact[case_key]
        if not isinstance(case, dict):
            continue
        try:
            dAB = float(case['delta_AB'])
            dAC = float(case['delta_AC'])
            dBC = float(case['delta_BC'])
            delta = float(case['delta'])
            min_phi = float(case['min_phi_T'])
            gt = str(case['ground_state_type']).strip()
        except Exception:
            continue
        perms = ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']
        best_phi = float('inf')
        for y1 in perms:
            for y2 in perms:
                for y3 in perms:
                    phi = psi_value(dAB, dAC, dBC, delta, y1, 1) + psi_value(dAB, dAC, dBC, delta, y2, 2) + psi_value(dAB, dAC, dBC, delta, y3, 3)
                    if phi < best_phi:
                        best_phi = phi
        if delta > 0:
            if dAB < delta:
                expected_type = 'homochiral'
            elif dAC < delta < dAB:
                expected_type = 'unusual_racemic'
            else:
                expected_type = 'none'
        else:
            if dAB < 0:
                expected_type = 'racemic'
            elif dAC < 0 < dAB:
                expected_type = 'none'
            else:
                expected_type = 'none'
        if abs(min_phi - best_phi) < 1e-6 and gt == expected_type:
            score += 1
        n += 1
    if n == 0:
        return 0.0
    return score / n


# === block: score_1 (check id='step_02_residual_entropy') ===
def score_1(artifact, step, ctx):
    try:
        val = float(artifact.strip())
    except Exception:
        return 0.0
    expected = math.sqrt(3) / (2 * math.pi) * (math.gamma(1/3)) ** 1.5
    if abs(val - expected) < 1e-6:
        return 1.0
    else:
        return 0.0


_SCORERS = {
    'step_01_ground_states': score_0,
    'step_02_residual_entropy': score_1,
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
