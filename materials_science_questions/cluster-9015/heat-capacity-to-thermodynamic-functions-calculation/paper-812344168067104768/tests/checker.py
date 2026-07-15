import os
import json
import csv

# === author imports / helpers ===
import csv
import json
import math
from collections import defaultdict


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
    steps = spec.get('steps', [])
    step = steps[0] if steps else {}
    ref = step.get('reference', [])
    tol_rel = float(step.get('tol_relative', 0.01))
    tol_abs = float(step.get('tol_absolute', 0.01))
    tol_match_T = float(step.get('temp_match_abs_tol', 0.01))

    # Build dict mapping temperature to expected values (Cp, S, H, G)
    expected = {}
    for row in ref:
        T, Cp, S, H, G = float(row[0]), float(row[1]), float(row[2]), float(row[3]), float(row[4])
        expected[T] = (Cp, S, H, G)

    return {
        'expected': expected,
        'total_points': len(expected),
        'tol_rel': tol_rel,
        'tol_abs': tol_abs,
        'tol_match_T': tol_match_T
    }


# === block: score_0 (check id='step_02_compute') ===
def score_0(artifact, step, ctx):
    if not artifact:
        return 0.0

    expected = ctx['expected']
    total = ctx['total_points']
    tol_rel = ctx['tol_rel']
    tol_abs = ctx['tol_abs']
    tol_match_T = ctx['tol_match_T']

    # Build index from agent data: list of dicts with float conversion
    agent_rows = []
    for row in artifact:
        try:
            T = float(row.get('T', row.get('T', 0)))
            Cp = float(row.get('Cp_over_R', 0))
            S = float(row.get('S_over_R', 0))
            H = float(row.get('H_over_RK', 0))
            G = float(row.get('G_over_RT', 0))
            agent_rows.append((T, Cp, S, H, G))
        except (ValueError, TypeError):
            continue

    passed = 0
    for ref_T, ref_vals in expected.items():
        # Find closest agent row
        best = None
        best_err = float('inf')
        for T, Cp, S, H, G in agent_rows:
            err = abs(T - ref_T)
            if err <= tol_match_T and err < best_err:
                best = (Cp, S, H, G)
                best_err = err
        if best is None:
            continue  # no matching temperature row
    
        Cp_ok = (abs(ref_vals[0]) < 1.0 and abs(best[0] - ref_vals[0]) <= tol_abs) or \
                (abs(ref_vals[0]) >= 1.0 and abs(best[0] - ref_vals[0]) <= tol_rel * abs(ref_vals[0]))
        S_ok  = (abs(ref_vals[1]) < 1.0 and abs(best[1] - ref_vals[1]) <= tol_abs) or \
                (abs(ref_vals[1]) >= 1.0 and abs(best[1] - ref_vals[1]) <= tol_rel * abs(ref_vals[1]))
        H_ok  = (abs(ref_vals[2]) < 1.0 and abs(best[2] - ref_vals[2]) <= tol_abs) or \
                (abs(ref_vals[2]) >= 1.0 and abs(best[2] - ref_vals[2]) <= tol_rel * abs(ref_vals[2]))
        G_ok  = (abs(ref_vals[3]) < 1.0 and abs(best[3] - ref_vals[3]) <= tol_abs) or \
                (abs(ref_vals[3]) >= 1.0 and abs(best[3] - ref_vals[3]) <= tol_rel * abs(ref_vals[3]))
        if Cp_ok and S_ok and H_ok and G_ok:
            passed += 1

    return passed / total if total > 0 else 0.0


_SCORERS = {
    'step_02_compute': score_0,
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
