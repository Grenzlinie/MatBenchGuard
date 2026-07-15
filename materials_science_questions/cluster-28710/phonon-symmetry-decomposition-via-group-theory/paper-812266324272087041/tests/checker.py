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
    return {}


# === block: score_0 (check id='group_decomposition') ===
def score_0(artifact, step, ctx):
    import json
    import os

    artifact = json.load(open(os.path.join('/app/outputs', step['output_file']), 'r'))
    score = 0.0

    # irrep decomposition
    irr = artifact.get('irrep_decomposition', {})
    expected_irr = {'A1':7, 'A2':9, 'B1':7, 'B2':7, 'E':18}
    ok_irrep = all(irr.get(k) == v for k, v in expected_irr.items())
    score += 0.4 if ok_irrep else 0.0

    # total_modes
    total = artifact.get('total_modes', -1)
    # also verify sum
    sum_irr = sum(irr.values()) if isinstance(irr, dict) else -1
    if total == 66 and sum_irr == 66:
        score += 0.05

    # acoustic modes
    ac = artifact.get('acoustic_modes', {})
    if ac.get('A2') == 1 and ac.get('E') == 2:
        score += 0.1

    # optical modes
    opt = artifact.get('optical_modes', {})
    ir_opt = opt.get('IR_active', {})
    raman_opt = opt.get('Raman_active', {})
    if (ir_opt.get('A2') == 8 and
        raman_opt.get('A1') == 7 and raman_opt.get('B1') == 7 and
        raman_opt.get('B2') == 7 and raman_opt.get('E') == 17 and
        opt.get('E_also_IR_active') == True):
        score += 0.2

    # Raman tensor patterns
    tensors = artifact.get('raman_tensor_forms', {})
    def check_tensor(mat, pattern_type):
        if not isinstance(mat, list) or len(mat) != 3:
            return False
        for row in mat:
            if not isinstance(row, list) or len(row) != 3:
                return False
        try:
            if pattern_type == 'A1':
                # diagonal (a,a,b) non-zero, others zero
                return mat[0][0] != 0 and mat[1][1] != 0 and mat[2][2] != 0 and \
                       mat[0][1] == 0 and mat[0][2] == 0 and mat[1][0] == 0 and \
                       mat[1][2] == 0 and mat[2][0] == 0 and mat[2][1] == 0
            elif pattern_type == 'B1':
                # diagonal (c, -c, 0) with non-zero (c) and opposite sign on (1,1)
                # allow any non-zero values, but check zero pattern: (2,2) zero, others zero
                return mat[0][0] != 0 and mat[1][1] != 0 and mat[2][2] == 0 and \
                       mat[0][1] == 0 and mat[0][2] == 0 and mat[1][0] == 0 and \
                       mat[1][2] == 0 and mat[2][0] == 0 and mat[2][1] == 0
            elif pattern_type == 'B2':
                # symmetric off-diagonal (0,d,0; d,0,0; 0,0,0)
                return mat[0][1] != 0 and mat[1][0] != 0 and mat[2][2] == 0 and \
                       mat[0][0] == 0 and mat[0][2] == 0 and mat[1][1] == 0 and \
                       mat[1][2] == 0 and mat[2][0] == 0 and mat[2][1] == 0
            elif pattern_type == 'E':
                # list of two matrices
                if not isinstance(mat, list) or len(mat) != 2:
                    return False
                m1, m2 = mat[0], mat[1]
                # check both are 3x3
                for m in [m1, m2]:
                    if len(m) != 3 or any(len(row) != 3 for row in m):
                        return False
                # m1: non-zero at (0,2) and (2,0), rest zero
                ok1 = m1[0][2] != 0 and m1[2][0] != 0 and \
                      m1[0][0] == 0 and m1[0][1] == 0 and m1[1][0] == 0 and \
                      m1[1][1] == 0 and m1[1][2] == 0 and m1[2][1] == 0 and m1[2][2] == 0
                # m2: non-zero at (1,2) and (2,1), rest zero
                ok2 = m2[1][2] != 0 and m2[2][1] != 0 and \
                      m2[0][0] == 0 and m2[0][1] == 0 and m2[0][2] == 0 and \
                      m2[1][0] == 0 and m2[1][1] == 0 and m2[2][0] == 0 and m2[2][2] == 0
                return ok1 and ok2
            else:
                return False
        except (IndexError, TypeError):
            return False

    tensor_ok = True
    tensor_map = {'A1': tensors.get('A1'), 'B1': tensors.get('B1'), 'B2': tensors.get('B2'), 'E': tensors.get('E')}
    for sym, mat in tensor_map.items():
        if not check_tensor(mat, sym):
            tensor_ok = False
            break
    if tensor_ok:
        score += 0.25

    # cap at 1.0
    return min(score, 1.0)


_SCORERS = {
    'group_decomposition': score_0,
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
