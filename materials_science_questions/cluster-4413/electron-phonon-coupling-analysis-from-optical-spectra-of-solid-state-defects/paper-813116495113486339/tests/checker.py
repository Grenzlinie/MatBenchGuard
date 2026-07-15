import os
import json
import csv

# === author imports / helpers ===
import sys
import subprocess
try:
    import numpy as np
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', '--no-cache-dir', 'numpy'])
    import numpy as np
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
    ref_defs = spec['steps'][1]['check_config']['reference_vector_defs']
    sqrt2 = math.sqrt(2)
    U_cols = []
    for block_name in ["M1","M2","M3","M4"]:
        for pairs in ref_defs[block_name]:
            vec = np.zeros(24)
            for i1, s1, i2, s2 in pairs:
                vec[i1] = s1 / sqrt2
                vec[i2] = s2 / sqrt2
            U_cols.append(vec)
    U = np.column_stack(U_cols)
    irrep_chars = spec['steps'][1]['check_config']['irrep_characters']
    block_sizes = [8,4,4,8]
    block_chars = [irrep_chars["M1"], irrep_chars["M2"], irrep_chars["M3"], irrep_chars["M4"]]
    Gamma_matrices = {}
    for op_idx in range(4):
        diag = np.concatenate([np.full(size, block_chars[b][op_idx]) for b, size in enumerate(block_sizes)])
        Gamma_matrices[op_idx] = U @ np.diag(diag) @ U.T
    ctx = {
        "Gamma_matrices": Gamma_matrices,
        "irrep_chars": irrep_chars,
        "tolerance_symmetry": spec['steps'][1]['check_config']['tolerance_symmetry_eigen'],
        "tolerance_ortho": spec['steps'][1]['check_config']['tolerance_orthonormality']
    }
    return ctx


# === block: score_0 (check id='check_01_multiplicities') ===
def score_0(artifact, step, ctx):
    gold = step["gold_values"]
    if artifact.get("n1") != gold["n1"] or artifact.get("n2") != gold["n2"] or artifact.get("n3") != gold["n3"] or artifact.get("n4") != gold["n4"]:
        return 0.0
    return 1.0


# === block: score_1 (check id='check_02_symmetry_modes') ===
def score_1(artifact, step, ctx):
    M1_vecs = np.array(artifact["M1"])
    M2_vecs = np.array(artifact["M2"])
    M3_vecs = np.array(artifact["M3"])
    M4_vecs = np.array(artifact["M4"])
    if M1_vecs.shape != (8,24) or M2_vecs.shape != (4,24) or M3_vecs.shape != (4,24) or M4_vecs.shape != (8,24):
        return 0.0
    all_vecs = np.concatenate([M1_vecs, M2_vecs, M3_vecs, M4_vecs], axis=0)
    gram = all_vecs @ all_vecs.T
    if np.max(np.abs(gram - np.eye(24))) > ctx["tolerance_ortho"]:
        return 0.0
    char_map = {"M1": [1,1,1,1], "M2": [1,-1,1,-1], "M3": [1,1,-1,-1], "M4": [1,-1,-1,1]}
    for block_name, chars in char_map.items():
        vecs = {"M1": M1_vecs, "M2": M2_vecs, "M3": M3_vecs, "M4": M4_vecs}[block_name]
        for v in vecs:
            for op_idx in range(4):
                expected = chars[op_idx] * v
                actual = ctx["Gamma_matrices"][op_idx] @ v
                if np.max(np.abs(actual - expected)) > ctx["tolerance_symmetry"]:
                    return 0.0
    return 1.0


_SCORERS = {
    'check_01_multiplicities': score_0,
    'check_02_symmetry_modes': score_1,
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
