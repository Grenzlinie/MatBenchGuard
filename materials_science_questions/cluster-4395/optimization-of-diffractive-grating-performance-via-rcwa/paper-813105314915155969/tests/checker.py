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
    ctx = {}
    step_params = {}
    for s in spec.get('steps', spec.get('checks', [])):
        sid = s.get('id')
        if sid:
            step_params[sid] = s
    ctx['step_params'] = step_params
    return ctx


# === block: score_0 (check id='step_2') ===
def score_0(artifact, step, ctx):
    import traceback
    try:
        param = ctx['step_params'].get(step.get('id'), {})
        full_thresh = param.get('full_credit_threshold', 5.2)
        decay = param.get('decay_range', 5.0)
        peak_target = param.get('peak_angle_expected', 45.0)
        peak_tol = param.get('peak_angle_tolerance', 10.0)
        peak_w = param.get('peak_location_weight', 0.05)

        # artifact is list of dicts
        rows = artifact
        if not rows:
            return 0.0
        header = rows[0].keys()
        angle_cols = {}
        for k in header:
            if k.startswith('angle_'):
                ang_str = k[len('angle_'):]
                try:
                    ang = float(ang_str)
                    angle_cols[k] = ang
                except:
                    pass
        if not angle_cols:
            return 0.0
        sorted_ang = sorted(angle_cols.values())
        min_ang = min(sorted_ang)
        max_ang = max(sorted_ang)
        # check emissivity values
        valid = True
        for row in rows:
            for k, ang in angle_cols.items():
                v = row.get(k)
                if v == '' or v is None:
                    valid = False
                    break
                try:
                    vf = float(v)
                except:
                    valid = False
                    break
                if vf < -1e-9 or vf > 1.0 + 1e-9:
                    valid = False
                    break
            if not valid:
                break
        if not valid:
            dtheta = 999.0
        else:
            fwhms = []
            for row in rows:
                vals = {}
                for k, ang in angle_cols.items():
                    vals[ang] = float(row.get(k))
                peak_val = max(vals.values())
                if peak_val <= 0:
                    fwhms.append(0.0)
                    continue
                half = peak_val / 2.0
                angles_above = [ang for ang, v in vals.items() if v >= half]
                if not angles_above:
                    fwhms.append(0.0)
                else:
                    fwhm = max(angles_above) - min(angles_above)
                    fwhms.append(fwhm)
            dtheta = max(fwhms) if fwhms else 0.0
        # score angular dispersion
        if dtheta <= full_thresh:
            score_dtheta = 1.0
        else:
            score_dtheta = max(0.0, 1.0 - (dtheta - full_thresh) / decay)
        # peak location check
        peak_loc_score = 0.0
        if valid:
            # find global max emissivity and its angle
            best_angle = None
            best_value = -1.0
            for row in rows:
                for k, ang in angle_cols.items():
                    v = float(row.get(k))
                    if v > best_value:
                        best_value = v
                        best_angle = ang
            if best_angle is not None:
                abs_angle = abs(best_angle)
                if (peak_target - peak_tol) <= abs_angle <= (peak_target + peak_tol):
                    peak_loc_score = 1.0
        # combine
        score = (1.0 - peak_w) * score_dtheta + peak_w * peak_loc_score
        return score
    except Exception as e:
        traceback.print_exc()
        return 0.0


# === block: score_1 (check id='step_3') ===
def score_1(artifact, step, ctx):
    import traceback
    try:
        param = ctx['step_params'].get(step.get('id'), {})
        full_thresh = param.get('full_credit_threshold', 5.2)
        decay = param.get('decay_range', 5.0)
        txt = artifact.strip()
        reported = float(txt)
        if reported <= full_thresh:
            return 1.0
        else:
            return max(0.0, 1.0 - (reported - full_thresh) / decay)
    except Exception as e:
        traceback.print_exc()
        return 0.0


_SCORERS = {
    'step_2': score_0,
    'step_3': score_1,
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
