import os
import json
import csv

# === author imports / helpers ===
import subprocess
import sys
import os
try:
    import sympy as sp
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "--no-cache-dir", "-i", "https://pypi.tuna.tsinghua.edu.cn/simple", "sympy"])
    import sympy as sp
import re


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


# === block: score_0 (check id='check_renorm_freq') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        lines = [line.strip() for line in artifact.split('\n') if line.strip()]
        if not lines:
            return 0.0
        line = lines[0]
        line = line.replace('ω', 'omega').replace('₀', '0').replace('²', '^2')
        if '=' not in line:
            return 0.0
        lhs, rhs = line.split('=', 1)
        rhs = rhs.strip()
        gold_parts = step['gold_expression'].split('=')
        gold_rhs = gold_parts[1].strip()
        omega0, f, g = sp.symbols('omega0 f g')
        local_dict = {'omega0': omega0, 'f': f, 'g': g}
        try:
            user_expr = sp.simplify(sp.sympify(rhs, locals=local_dict))
            gold_expr = sp.simplify(sp.sympify(gold_rhs, locals=local_dict))
        except Exception:
            return 0.0
        return 1.0 if sp.simplify(user_expr - gold_expr) == 0 else 0.0


# === block: score_1 (check id='check_gt_approx') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        lines = [line.strip() for line in artifact.split('\n') if line.strip()]
        if not lines:
            return 0.0
        line = lines[0]
        line = line.replace('ω', 'omega').replace('₀', '0').replace('²', '^2')
        if '=' not in line:
            return 0.0
        lhs, rhs = line.split('=', 1)
        rhs = rhs.strip()
        gold_parts = step['gold_expression'].split('=')
        gold_rhs = gold_parts[1].strip()
        G, hbar, k, T, omega_F_T1 = sp.symbols('G hbar k T omega_F_T1')
        local_dict = {'G': G, 'hbar': hbar, 'k': k, 'T': T, 'omega_F_T1': omega_F_T1}
        try:
            user_expr = sp.simplify(sp.sympify(rhs, locals=local_dict))
            gold_expr = sp.simplify(sp.sympify(gold_rhs, locals=local_dict))
        except Exception:
            return 0.0
        return 1.0 if sp.simplify(user_expr - gold_expr) == 0 else 0.0


# === block: score_2 (check id='check_barrett_constants') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        lines = artifact.split('\n')
        expected = step['gold_expressions']
        correct = 0
        total = 4
        omega0, hbar, f, k, G, g2, omega_F_T1 = sp.symbols('omega0 hbar f k G g2 omega_F_T1')
        local_dict = {'omega0': omega0, 'hbar': hbar, 'f': f, 'k': k, 'G': G, 'g2': g2, 'omega_F_T1': omega_F_T1, 'Abs': sp.Abs}
        name_map = {'a': 'A', 'b': 'B', 't1': 'T1', 't0': 'T0'}
        sub_trans = str.maketrans('₀₁₂₃₄₅₆₇₈₉', '0123456789')
        for line in lines:
            line = line.strip()
            if not line:
                continue
            line = line.translate(sub_trans)
            line = line.replace('ω', 'omega').replace('²', '^2')
            if '=' not in line:
                continue
            name_part, expr_part = line.split('=', 1)
            name = name_part.strip().replace('_', '').replace(' ', '').lower()
            canon = name_map.get(name)
            if not canon:
                continue
            gold_expr_str = expected[canon]
            try:
                user_expr = sp.simplify(sp.sympify(expr_part.strip(), locals=local_dict))
                gold_expr = sp.simplify(sp.sympify(gold_expr_str, locals=local_dict))
            except Exception:
                continue
            if sp.simplify(user_expr - gold_expr) == 0:
                correct += 1
        return min(1.0, correct / float(total))


_SCORERS = {
    'check_renorm_freq': score_0,
    'check_gt_approx': score_1,
    'check_barrett_constants': score_2,
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
