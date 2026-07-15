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


# === block: score_0 (check id='step2_isotope_shift') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        import math
        try:
            rows = list(artifact)
        except Exception:
            return 0.0
        if not rows:
            return 0.0
        p0 = step['params']['p0']
        Tc_max_ref = step['params']['Tc_max']
        tol_Tc = step['params']['tol_Tc_K']
        tol_alpha = step['params']['tol_alpha']
        alpha_slope = step['params']['alpha_slope']
        alpha_rise = step['params']['alpha_rise']
        max_Tc_min = step['params']['max_Tc_min']
        doping_max_Tc_tol = step['params']['doping_max_Tc_tol']
        alpha_at_max_Tc_max = step['params']['alpha_at_max_Tc_max']
        # parse rows
        dopings = []
        Tc_vals = []
        alpha_vals = []
        for row in rows:
            try:
                p = float(row['doping_p'])
                tc = float(row['Tc_K'])
                al = float(row['isotope_shift_alpha'])
            except (ValueError, KeyError):
                return 0.0
            if tc < 0 or al < 0 or al > 2.0:
                continue
            dopings.append(p)
            Tc_vals.append(tc)
            alpha_vals.append(al)
        if len(dopings) < 3:
            return 0.0
        # find max Tc
        max_idx = Tc_vals.index(max(Tc_vals))
        max_Tc = Tc_vals[max_idx]
        max_doping = dopings[max_idx]
        # get alpha at max Tc (closest to max doping)
        # use same row
        alpha_at_max = alpha_vals[max_idx]
        # shape checks
        shape_pass = 1.0 if (max_Tc >= max_Tc_min and abs(max_doping - p0) <= doping_max_Tc_tol and alpha_at_max < alpha_at_max_Tc_max) else 0.0
        # pointwise reference comparison
        n = len(dopings)
        n_good = 0
        for i in range(n):
            p = dopings[i]
            tc = Tc_vals[i]
            al = alpha_vals[i]
            Tc_ref = Tc_max_ref * max(0.0, 1.0 - 82.6*(p - p0)**2)
            delta_p = abs(p - p0)
            alpha_ref = min(alpha_slope, (alpha_slope/alpha_rise)*delta_p) if delta_p <= alpha_rise else alpha_slope
            if abs(tc - Tc_ref) <= tol_Tc and abs(al - alpha_ref) <= tol_alpha:
                n_good += 1
        pointwise_score = n_good / n
        final = 0.4 * shape_pass + 0.6 * pointwise_score
        return max(0.0, min(1.0, final))


# === block: score_1 (check id='step3_dcdw') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        text = artifact.strip() if isinstance(artifact, str) else ''
        if not text:
            return 0.0
        try:
            val = float(text.splitlines()[0])
        except Exception:
            return 0.0
        target = step['target']['value']
        tol = step['target']['tolerance']
        return 1.0 if abs(val - target) <= tol else 0.0


# === block: score_2 (check id='step3b_amplitude_ratio') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        text = artifact.strip() if isinstance(artifact, str) else ''
        if not text:
            return 0.0
        try:
            val = float(text.splitlines()[0])
        except Exception:
            return 0.0
        target = step['target']['value']
        tol = step['target']['tolerance']
        return 1.0 if abs(val - target) <= tol else 0.0


_SCORERS = {
    'step2_isotope_shift': score_0,
    'step3_dcdw': score_1,
    'step3b_amplitude_ratio': score_2,
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
