import os
import json
import csv

# === author imports / helpers ===
import json
import os
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
        gold = spec['gold']
        artifact_path = os.path.join(outputs_dir, 'theoretical_data.json')
        with open(artifact_path) as f:
            data = json.load(f)

        derived = {}
        for mol in ['CH4', 'CF4']:
            mg = gold[mol]
            d = data[mol]
            u_prime = float(d['u_prime'])
            E = u_prime + mg['q_kcal']
            f_plus = float(d['f_plus'])
            f_trans = float(d['f_trans_prime'])
            f_rot = float(d['f_rot'])
            C = mg['C_factor']
            d_star_rot = C * f_plus / f_trans
            d_star_nrot = C * f_plus / (f_trans * f_rot)
            derived[mol] = {
                'E': E,
                'D_star_rot': d_star_rot,
                'D_star_nrot': d_star_nrot
            }
        return {'gold': gold, 'derived': derived, 'artifact': data}


# === block: score_0 (check id='E_CH4') ===
def score_0(artifact, step, ctx):
        derived = ctx['derived']['CH4']
        target = ctx['gold']['CH4']['E_theoretical']
        tol = 0.5
        e = derived['E']
        diff = abs(e - target)
        if diff <= tol:
            return 1.0
        return max(0.0, 1.0 - (diff - tol) / tol)


# === block: score_1 (check id='E_CF4') ===
def score_1(artifact, step, ctx):
        derived = ctx['derived']['CF4']
        target = ctx['gold']['CF4']['E_theoretical']
        tol = 0.5
        e = derived['E']
        diff = abs(e - target)
        if diff <= tol:
            return 1.0
        return max(0.0, 1.0 - (diff - tol) / tol)


# === block: score_2 (check id='D_star_rot_CH4') ===
def score_2(artifact, step, ctx):
        derived = ctx['derived']['CH4']
        target = ctx['gold']['CH4']['D_star_rot_theoretical']
        rel_tol = 0.5
        d = derived['D_star_rot']
        if target == 0:
            return 1.0 if d == 0 else 0.0
        err = abs(d - target) / abs(target)
        if err <= rel_tol:
            return 1.0
        return max(0.0, 1.0 - (err - rel_tol) / rel_tol)


# === block: score_3 (check id='D_star_nrot_CH4') ===
def score_3(artifact, step, ctx):
        derived = ctx['derived']['CH4']
        target = ctx['gold']['CH4']['D_star_nrot_theoretical']
        rel_tol = 0.5
        d = derived['D_star_nrot']
        if target == 0:
            return 1.0 if d == 0 else 0.0
        err = abs(d - target) / abs(target)
        if err <= rel_tol:
            return 1.0
        return max(0.0, 1.0 - (err - rel_tol) / rel_tol)


# === block: score_4 (check id='D_star_rot_CF4') ===
def score_4(artifact, step, ctx):
        derived = ctx['derived']['CF4']
        target = ctx['gold']['CF4']['D_star_rot_theoretical']
        rel_tol = 0.5
        d = derived['D_star_rot']
        if target == 0:
            return 1.0 if d == 0 else 0.0
        err = abs(d - target) / abs(target)
        if err <= rel_tol:
            return 1.0
        return max(0.0, 1.0 - (err - rel_tol) / rel_tol)


# === block: score_5 (check id='D_star_nrot_CF4') ===
def score_5(artifact, step, ctx):
        derived = ctx['derived']['CF4']
        target = ctx['gold']['CF4']['D_star_nrot_theoretical']
        rel_tol = 0.5
        d = derived['D_star_nrot']
        if target == 0:
            return 1.0 if d == 0 else 0.0
        err = abs(d - target) / abs(target)
        if err <= rel_tol:
            return 1.0
        return max(0.0, 1.0 - (err - rel_tol) / rel_tol)


# === block: score_6 (check id='rotation_CH4') ===
def score_6(artifact, step, ctx):
        derived = ctx['derived']['CH4']
        gold = ctx['gold']['CH4']
        d_rot = derived['D_star_rot']
        d_nrot = derived['D_star_nrot']
        d_exp = gold['D_star_expt']
        return 1.0 if abs(d_nrot - d_exp) < abs(d_rot - d_exp) else 0.0


# === block: score_7 (check id='rotation_CF4') ===
def score_7(artifact, step, ctx):
        derived = ctx['derived']['CF4']
        gold = ctx['gold']['CF4']
        d_rot = derived['D_star_rot']
        d_nrot = derived['D_star_nrot']
        d_exp = gold['D_star_expt']
        return 1.0 if abs(d_rot - d_exp) < abs(d_nrot - d_exp) else 0.0


_SCORERS = {
    'E_CH4': score_0,
    'E_CF4': score_1,
    'D_star_rot_CH4': score_2,
    'D_star_nrot_CH4': score_3,
    'D_star_rot_CF4': score_4,
    'D_star_nrot_CF4': score_5,
    'rotation_CH4': score_6,
    'rotation_CF4': score_7,
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
