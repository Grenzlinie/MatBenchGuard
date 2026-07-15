import os
import json
import csv

# === author imports / helpers ===
def _matrix_transpose(M):
    return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]

def tensor_to_array(tensor):
    return [[float(x) for x in row] for row in tensor]

def is_symmetric(C, tol=0.5):
    n = len(C)
    max_diff = 0.0
    for i in range(n):
        for j in range(n):
            diff = abs(C[i][j] - C[j][i])
            if diff > max_diff:
                max_diff = diff
    return max_diff <= tol

def is_positive_definite(C):
    n = len(C)
    L = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            s = sum(L[i][k] * L[j][k] for k in range(j))
            if i == j:
                val = C[i][i] - s
                if val <= 1e-12:
                    return False
                L[i][j] = val ** 0.5
            else:
                if L[j][j] == 0:
                    return False
                L[i][j] = (C[i][j] - s) / L[j][j]
    return True

def _invert_6x6(C):
    n = 6
    aug = [row[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(C)]
    for col in range(n):
        pivot_row = max(range(col, n), key=lambda i: abs(aug[i][col]))
        if abs(aug[pivot_row][col]) < 1e-12:
            raise ValueError("Matrix is singular")
        aug[col], aug[pivot_row] = aug[pivot_row], aug[col]
        pivot_val = aug[col][col]
        aug[col] = [v / pivot_val for v in aug[col]]
        for row in range(n):
            if row != col:
                factor = aug[row][col]
                aug[row] = [r - factor * p for r, p in zip(aug[row], aug[col])]
    inv = [row[n:] for row in aug]
    return inv

def compute_hill_moduli(C):
    S = _invert_6x6(C)
    c11, c22, c33 = C[0][0], C[1][1], C[2][2]
    c12, c23, c13 = C[0][1], C[1][2], C[0][2]
    c44, c55, c66 = C[3][3], C[4][4], C[5][5]
    BV = (c11 + c22 + c33 + 2 * (c12 + c23 + c13)) / 9.0
    s11, s22, s33 = S[0][0], S[1][1], S[2][2]
    s12, s23, s13 = S[0][1], S[1][2], S[0][2]
    BR = 1.0 / (s11 + s22 + s33 + 2 * (s12 + s23 + s13))
    B = (BV + BR) / 2.0
    GV = (c11 + c22 + c33 - (c12 + c23 + c13) + 3 * (c44 + c55 + c66)) / 15.0
    GR = 15.0 / (4 * (s11 + s22 + s33) - 4 * (s12 + s23 + s13) + 3 * (S[3][3] + S[4][4] + S[5][5]))
    G = (GV + GR) / 2.0
    denom = 3 * B + G
    E = 9 * B * G / denom if denom != 0 else 0.0
    nu = (3 * B - 2 * G) / (2 * denom) if denom != 0 else 0.0
    return B, G, E, nu

def directional_moduli_from_compliance(C, dir11_idx=0, dir33_idx=2, dirG44_idx=4):
    S = _invert_6x6(C)
    E11 = 1.0 / S[dir11_idx][dir11_idx] if abs(S[dir11_idx][dir11_idx]) > 1e-12 else 0.0
    E33 = 1.0 / S[dir33_idx][dir33_idx] if abs(S[dir33_idx][dir33_idx]) > 1e-12 else 0.0
    G44 = 1.0 / S[dirG44_idx][dirG44_idx] if abs(S[dirG44_idx][dirG44_idx]) > 1e-12 else 0.0
    return E11, E33, G44


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


# === block: score_0 (check id='pure_matrix_symmetry') ===
def score_0(artifact, step, ctx):
    C = tensor_to_array(artifact['stiffness_tensor'])
    tol = step.get('tolerance', 0.5)
    return 1.0 if is_symmetric(C, tol) else 0.0


# === block: score_1 (check id='pure_matrix_positive_definite') ===
def score_1(artifact, step, ctx):
    C = tensor_to_array(artifact['stiffness_tensor'])
    return 1.0 if is_positive_definite(C) else 0.0


# === block: score_2 (check id='pure_matrix_moduli') ===
def score_2(artifact, step, ctx):
    C = tensor_to_array(artifact['stiffness_tensor'])
    B, G, E, nu = compute_hill_moduli(C)
    gold = step.get('gold', {})
    tols = step.get('tolerances', {})
    subs = []
    for key in ['B', 'G', 'E', 'nu']:
        target = gold.get(key)
        tol = tols.get(key, 1.0)
        val = {'B':B, 'G':G, 'E':E, 'nu':nu}[key]
        subs.append(1.0 if abs(val - target) <= tol else 0.0)
    return sum(subs) / len(subs)


# === block: score_3 (check id='reinforced_symmetry') ===
def score_3(artifact, step, ctx):
    C = tensor_to_array(artifact['stiffness_tensor'])
    tol = step.get('tolerance', 0.5)
    return 1.0 if is_symmetric(C, tol) else 0.0


# === block: score_4 (check id='reinforced_positive_definite') ===
def score_4(artifact, step, ctx):
    C = tensor_to_array(artifact['stiffness_tensor'])
    return 1.0 if is_positive_definite(C) else 0.0


# === block: score_5 (check id='reinforced_E33_E11_trend') ===
def score_5(artifact, step, ctx):
    C = tensor_to_array(artifact['stiffness_tensor'])
    E11, E33, G44 = directional_moduli_from_compliance(C, 0, 2, 4)
    return 1.0 if E33 > E11 else 0.0


# === block: score_6 (check id='reinforced_E33_range') ===
def score_6(artifact, step, ctx):
    C = tensor_to_array(artifact['stiffness_tensor'])
    E11, E33, G44 = directional_moduli_from_compliance(C, 0, 2, 4)
    min_val = step.get('min', 4.0)
    max_val = step.get('max', 8.0)
    return 1.0 if min_val <= E33 <= max_val else 0.0


_SCORERS = {
    'pure_matrix_symmetry': score_0,
    'pure_matrix_positive_definite': score_1,
    'pure_matrix_moduli': score_2,
    'reinforced_symmetry': score_3,
    'reinforced_positive_definite': score_4,
    'reinforced_E33_E11_trend': score_5,
    'reinforced_E33_range': score_6,
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
