import os
import json
import csv

# === author imports / helpers ===
import math

def _score_field(val, gold, rel_tol, abs_tol=None):
    if gold == 0:
        return 1.0 if val == 0 else 0.0
    rel_err = abs(val - gold) / gold
    if abs_tol is not None and abs(val - gold) <= abs_tol:
        return 1.0
    if rel_err <= rel_tol:
        return 1.0
    return max(0.0, 1.0 - (rel_err - rel_tol) / rel_tol)


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
    return {"spec": spec}


# === block: score_0 (check id='transition_data') ===
def score_0(artifact, step, ctx):
    gold_rows = step.get("gold", [])
    if not gold_rows:
        return 0.0
    gold_by_x = {row["composition_x"]: row for row in gold_rows}
    tol = step.get("tolerance", {})
    agent_by_x = {}
    for row in artifact:
        try:
            x = float(row["composition_x"])
            agent_by_x[x] = row
        except:
            continue
    pt_tol = tol.get("transition_pressure_GPa", {})
    rel_pt = pt_tol.get("relative", 0.15)
    abs_pt = pt_tol.get("absolute", None)
    v_tol = tol.get("volume_collapse_percent", {})
    rel_v = v_tol.get("relative", 0.20)
    total_score = 0.0
    count = 0
    for x, g_row in gold_by_x.items():
        count += 1
        a_row = agent_by_x.get(x)
        if a_row is None:
            continue
        try:
            pt = float(a_row["transition_pressure_GPa"])
            vc = float(a_row["volume_collapse_percent"])
        except:
            continue
        s_pt = _score_field(pt, g_row["transition_pressure_GPa"], rel_pt, abs_pt)
        s_vc = _score_field(vc, g_row["volume_collapse_percent"], rel_v)
        total_score += (s_pt + s_vc) / 2.0
    if count == 0:
        return 0.0
    return total_score / count


# === block: score_1 (check id='elastic_constants_B3') ===
def score_1(artifact, step, ctx):
    gold_rows = step.get("gold", [])
    if not gold_rows:
        return 0.0
    gold_by_x = {row["composition_x"]: row for row in gold_rows}
    tol = step.get("tolerance", {})
    agent_by_x = {}
    for row in artifact:
        try:
            x = float(row["composition_x"])
            agent_by_x[x] = row
        except:
            continue
    tol_bt = tol.get("B_T_GPa", {}).get("relative", 0.15)
    tol_c44 = tol.get("C44_GPa", {}).get("relative", 0.15)
    tol_cs = tol.get("C_s_GPa", {}).get("relative", 0.20)
    total_score = 0.0
    count = 0
    for x, g_row in gold_by_x.items():
        count += 1
        a_row = agent_by_x.get(x)
        if a_row is None:
            continue
        try:
            bt = float(a_row["B_T_GPa"])
            c44 = float(a_row["C44_GPa"])
            cs = float(a_row["C_s_GPa"])
        except:
            continue
        s_bt = _score_field(bt, g_row["B_T_GPa"], tol_bt)
        s_c44 = _score_field(c44, g_row["C44_GPa"], tol_c44)
        s_cs = _score_field(cs, g_row["C_s_GPa"], tol_cs)
        total_score += (s_bt + s_c44 + s_cs) / 3.0
    if count == 0:
        return 0.0
    return total_score / count


# === block: score_2 (check id='soec_vs_pressure') ===
def score_2(artifact, step, ctx):
    if not artifact:
        return 0.0
    rows = []
    for r in artifact:
        try:
            p = float(r["pressure_GPa"])
            c11 = float(r["C11_GPa"])
            c12 = float(r["C12_GPa"])
            c44 = float(r["C44_GPa"])
            rows.append((p, c11, c12, c44))
        except:
            continue
    if len(rows) < 2:
        return 0.0
    rows.sort(key=lambda x: x[0])
    ps, c11s, c12s, c44s = zip(*rows)
    # Check monotonic (non-decreasing, allow tiny noise)
    eps = 1e-6
    mono_ok = True
    for arr in (c11s, c12s, c44s):
        for i in range(1, len(arr)):
            if arr[i] < arr[i-1] - eps:
                mono_ok = False
                break
    # Check jump: at least one series shows a step > threshold
    jump_thresh = step.get("jump_threshold", 10.0)
    has_jump = False
    for arr in (c11s, c12s, c44s):
        diffs = [arr[i] - arr[i-1] for i in range(1, len(arr))]
        if diffs and max(diffs) >= jump_thresh:
            has_jump = True
            break
    if mono_ok and has_jump:
        return 1.0
    elif mono_ok:
        return 0.5
    else:
        return 0.0


_SCORERS = {
    'transition_data': score_0,
    'elastic_constants_B3': score_1,
    'soec_vs_pressure': score_2,
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
