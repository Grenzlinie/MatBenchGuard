import os
import json
import csv

# === author imports / helpers ===
import csv, json, os

class _NP:
    @staticmethod
    def polyfit(x, y, deg):
        # Pure-Python linear fit (degree 1 only)
        if deg != 1:
            raise NotImplementedError("only degree 1 supported")
        n = len(x)
        if n < 2:
            return [0.0, 0.0]
        sum_x = sum(x)
        sum_y = sum(y)
        sum_xy = sum(xi * yi for xi, yi in zip(x, y))
        sum_xx = sum(xi * xi for xi in x)
        denom = n * sum_xx - sum_x * sum_x
        if denom == 0:
            slope = 0.0
        else:
            slope = (n * sum_xy - sum_x * sum_y) / denom
        intercept = (sum_y - slope * sum_x) / n
        return [slope, intercept]

np = _NP()


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
    def load_csv(path):
        with open(path, newline='') as f:
            return list(csv.DictReader(f))
    s1 = load_csv(os.path.join(outputs_dir, 'step_01_resonance_angles.csv'))
    s2 = load_csv(os.path.join(outputs_dir, 'step_02_sensitivity_data.csv'))

    # extract slant FWHM
    slant_fwhm = None
    for row in s1:
        if row['configuration'].strip() == 'slant_60deg':
            slant_fwhm = float(row['FWHM_deg'])
            break
    if slant_fwhm is None:
        raise ValueError('slant_60deg FWHM not found')

    # compute slopes for each configuration from step_02
    def calc_slope(rows, config_name):
        x = []
        y = []
        for row in rows:
            if row['configuration'].strip() == config_name:
                x.append(float(row['refractive_index']))
                y.append(float(row['resonance_angle_deg']))
        if len(x) < 2:
            return None
        coeffs = np.polyfit(x, y, 1)
        slope = -coeffs[0]  # angle decreases with index, slope positive magnitude
        return slope

    slant_slope = calc_slope(s2, 'slant_60deg')
    unslant_slope = calc_slope(s2, 'unslant_90deg')

    return {'slant_fwhm': slant_fwhm, 'slant_slope': slant_slope, 'unslant_slope': unslant_slope}


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    gold = step['gold_table']
    correct = 0
    angle_tol = step['tolerance_angle_deg']
    fwhm_tol = step['tolerance_fwhm_deg']
    for g in gold:
        found = False
        for row in artifact:
            if row['configuration'].strip() == g['configuration']:
                found = True
                a = float(row['resonance_angle_deg'])
                f = float(row['FWHM_deg'])
                if abs(a - g['resonance_angle_deg']) <= angle_tol and abs(f - g['fwhm_deg']) <= fwhm_tol:
                    correct += 1
                break
        if not found:
            continue
    return correct / len(gold)


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    expected = step['expected_slope']
    tol_rel = step['tolerance_relative']

    def slope_score(config_name):
        rows = [r for r in artifact if r['configuration'].strip() == config_name]
        if len(rows) < 2:
            return 0.0
        x = [float(r['refractive_index']) for r in rows]
        y = [float(r['resonance_angle_deg']) for r in rows]
        # check monotonic decreasing
        if any(y[i] < y[i+1] for i in range(len(y)-1)):
            return 0.0
        coeffs = np.polyfit(x, y, 1)
        slope = -coeffs[0]  # positive magnitude
        exp = expected.get(config_name)
        if exp is None:
            return 0.0
        err_rel = abs(slope - exp) / exp
        score = max(0.0, 1.0 - err_rel / tol_rel)
        return score

    s1 = slope_score('slant_60deg')
    s2 = slope_score('unslant_90deg')
    return 0.5 * s1 + 0.5 * s2


# === block: score_2 (check id='step_03') ===
def score_2(artifact, step, ctx):
    slant_slope = ctx.get('slant_slope')
    unslant_slope = ctx.get('unslant_slope')
    slant_fwhm = ctx.get('slant_fwhm')
    if slant_slope is None or unslant_slope is None or slant_fwhm is None or slant_fwhm == 0:
        return 0.0

    fom = slant_slope / slant_fwhm

    def linear_score(val, low, high):
        if low >= high:
            return 0.0
        ratio = (val - low) / (high - low)
        return max(0.0, min(1.0, ratio))

    sens_low = step['slant_sens_low']
    sens_high = step['slant_sens_high']
    usens_low = step['unslant_sens_low']
    usens_high = step['unslant_sens_high']
    fom_low = step['fom_low']
    fom_high = step['fom_high']

    slant_sens_score = linear_score(slant_slope, sens_low, sens_high)
    unslant_sens_score = linear_score(unslant_slope, usens_low, usens_high)
    fom_score = linear_score(fom, fom_low, fom_high)

    return 0.3 * slant_sens_score + 0.2 * unslant_sens_score + 0.5 * fom_score


_SCORERS = {
    'step_01': score_0,
    'step_02': score_1,
    'step_03': score_2,
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
