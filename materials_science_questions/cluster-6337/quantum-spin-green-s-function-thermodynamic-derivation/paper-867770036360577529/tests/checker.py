import os
import json
import csv

# === author imports / helpers ===
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
    return {}


# === block: score_0 (check id='step_check_k2_02_t100') ===
def score_0(artifact, step, ctx):
        refs = step.get('reference_points', [])
        rot_tol = step.get('rotation_angle_tolerance', 0.01)
        data = []
        for row in artifact:
            try:
                bx = float(row['B_x'])
                sz = float(row['Sz_over_S'])
                sx = float(row['Sx_over_S'])
                tn = float(row['theta_norm'])
                data.append((bx, sz, sx, tn))
            except:
                continue
        if len(data) < 5:
            return 0.0

        # 1. rotation consistency: agent's (Sx, Sz) must imply the reported theta_norm
        rot_errs = []
        for bx, sz, sx, tn in data:
            if sz > 1e-9:
                a = math.atan2(sx, sz)
            elif sx > 0:
                a = math.pi/2
            else:
                a = 0.0
            imp_tn = a / (math.pi/2)
            rot_errs.append(abs(tn - imp_tn))
        avg_rot = sum(rot_errs) / len(rot_errs) if rot_errs else 0.0
        rot_score = max(0.0, 1.0 - avg_rot / rot_tol)

        # 2. structural sanity: reorientation curve shape must be correct
        sorted_data = sorted(data, key=lambda d: d[0])
        bx_min, sz_min, sx_min, tn_min = sorted_data[0]
        bx_max, sz_max, sx_max, tn_max = sorted_data[-1]
        struct_ok = True
        if not (0.7 <= sz_min <= 0.82 and sx_min <= 0.05):
            struct_ok = False
        if not (sz_max <= 0.05 and 0.7 <= sx_max <= 0.85):
            struct_ok = False
        for i in range(1, len(sorted_data)):
            if sorted_data[i][3] < sorted_data[i-1][3] - 1e-6:
                struct_ok = False
                break
        struct_score = 1.0 if struct_ok else 0.0

        # 3. soft reference proximity with generous tolerance (0.5) for correct re‑runs
        prox_tol = 0.5
        if refs:
            total_err = 0.0
            cnt = 0
            for ref in refs:
                ref_bx = ref['B_x']
                closest = min(sorted_data, key=lambda d: abs(d[0] - ref_bx))
                bx, sz, sx, tn = closest
                errs = [
                    abs(sz - ref['Sz_over_S']) / prox_tol,
                    abs(sx - ref['Sx_over_S']) / prox_tol,
                    abs(tn - ref['theta_norm']) / prox_tol
                ]
                total_err += sum(errs)
                cnt += 3
            avg_err = total_err / cnt if cnt > 0 else 0.0
            prox_score = max(0.0, 1.0 - avg_err)
        else:
            prox_score = 1.0

        return 0.2 * rot_score + 0.5 * struct_score + 0.3 * prox_score


# === block: score_1 (check id='step_check_k2_05_t4_9') ===
def score_1(artifact, step, ctx):
        refs = step.get('reference_points', [])
        tol = step.get('tolerance_abs', 0.1)
        rot_tol = step.get('rotation_angle_tolerance', 0.01)
        check_mono = step.get('check_monotonic_theta', False)
        data = []
        for row in artifact:
            try:
                bx = float(row['B_x'])
                sz = float(row['Sz_over_S'])
                sx = float(row['Sx_over_S'])
                tn = float(row['theta_norm'])
                data.append((bx, sz, sx, tn))
            except:
                continue
        if not data:
            return 0.0
        ref_score = 0.0
        if refs:
            hits = 0
            for ref in refs:
                ref_bx = ref['B_x']
                closest = min(data, key=lambda d: abs(d[0] - ref_bx))
                bx, sz, sx, tn = closest
                if abs(sz - ref['Sz_over_S']) <= tol and abs(sx - ref['Sx_over_S']) <= tol and abs(tn - ref['theta_norm']) <= tol:
                    hits += 1
            ref_score = hits / len(refs)
        else:
            ref_score = 1.0
        rot_errors = []
        for bx, sz, sx, tn in data:
            if sz > 0:
                angle_rad = math.atan2(sx, sz)
            elif sz == 0 and sx > 0:
                angle_rad = math.pi/2
            else:
                angle_rad = 0.0
            implied_tn = angle_rad / (math.pi/2)
            diff = abs(tn - implied_tn)
            rot_errors.append(diff)
        if rot_errors:
            avg_err = sum(rot_errors)/len(rot_errors)
            rot_score = max(0.0, 1.0 - avg_err / rot_tol)
        else:
            rot_score = 1.0
        mono_score = 1.0
        if check_mono:
            sorted_data = sorted(data, key=lambda d: d[0])
            for i in range(1, len(sorted_data)):
                if sorted_data[i][3] < sorted_data[i-1][3] - 1e-9:
                    mono_score = 0.0
                    break
        return 0.5 * ref_score + 0.3 * rot_score + 0.2 * mono_score


_SCORERS = {
    'step_check_k2_02_t100': score_0,
    'step_check_k2_05_t4_9': score_1,
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
