import os
import json
import csv

# === author imports / helpers ===
import json, math, cmath


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
        import math, cmath
        a = 1/math.sqrt(2)
        b = 1/math.sqrt(3)
        w = -0.5 + 1j * math.sqrt(3)/2
        wstar = w.conjugate()
        ia = 1j*a
        # Build reference matrix rows according to Table 1 ordering
        row0 = [[b,0.0],[b,0.0],[b,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0]]
        wc = -1j*w*b
        ws_c = -1j*wstar*b
        row1 = [[b,0.0],[wc.real,wc.imag],[ws_c.real,ws_c.imag],[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0]]
        row2 = [[b,0.0],[(wstar*b).real,(wstar*b).imag],[(w*b).real,(w*b).imag],[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0]]
        row3 = [[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,a],[0.0,0.0],[0.0,0.0],[0.0,-a],[0.0,0.0],[0.0,0.0]]
        row4 = [[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,-a],[0.0,0.0],[0.0,0.0],[0.0,a],[0.0,0.0],[0.0,0.0]]
        row5 = [[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,-a],[0.0,0.0],[0.0,0.0],[0.0,a],[0.0,0.0]]
        row6 = [[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,a],[0.0,0.0],[0.0,0.0],[0.0,-a],[0.0,0.0]]
        row7 = [[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,a],[0.0,0.0],[0.0,0.0],[0.0,-a]]
        row8 = [[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,-a],[0.0,0.0],[0.0,0.0],[0.0,a]]
        ref_matrix = [row0,row1,row2,row3,row4,row5,row6,row7,row8]
        for i in range(9):
            for j in range(9):
                ref_matrix[i][j] = [round(ref_matrix[i][j][0],6), round(ref_matrix[i][j][1],6)]
        expected_decomp = ["A1","A5","L1","L2"]
        expected_sizes = [1,2,3,3]
        return {"ref_matrix": ref_matrix, "expected_decomp": expected_decomp, "expected_sizes": expected_sizes}


# === block: score_0 (check id='step_1_cgc_matrix') ===
def score_0(artifact, step, ctx):
        agent_matrix = artifact.get("matrix", [])
        if len(agent_matrix) != 9 or any(len(row) != 9 for row in agent_matrix):
            return 0.0
        ref = ctx["ref_matrix"]
        max_abs_diff = 0.0
        for i in range(9):
            for j in range(9):
                ar, ai = agent_matrix[i][j]
                rr, ri = ref[i][j]
                diff = math.sqrt((ar-rr)**2 + (ai-ri)**2)
                if diff > max_abs_diff:
                    max_abs_diff = diff
        tol = float(step.get("tolerance", 1e-6))
        if max_abs_diff <= tol:
            return 1.0
        # partial credit: linearly decay to 0 when max_abs_diff reaches 0.1
        score = max(0.0, 1.0 - max_abs_diff / 0.1)
        return score


# === block: score_1 (check id='step_2_reduction') ===
def score_1(artifact, step, ctx):
        decomp = artifact.get("irreps_decomposition", [])
        sizes = artifact.get("block_sizes", [])
        norm = float(artifact.get("block_diagonal_norm", 999.0))
        expected_decomp = ctx["expected_decomp"]
        expected_sizes = ctx["expected_sizes"]
        decomp_ok = (decomp == expected_decomp)
        sizes_ok = (sizes == expected_sizes)
        norm_ok = (norm <= 1e-6)
        if decomp_ok and sizes_ok and norm_ok:
            return 1.0
        if decomp_ok and sizes_ok:
            return 0.5
        return 0.0


_SCORERS = {
    'step_1_cgc_matrix': score_0,
    'step_2_reduction': score_1,
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
