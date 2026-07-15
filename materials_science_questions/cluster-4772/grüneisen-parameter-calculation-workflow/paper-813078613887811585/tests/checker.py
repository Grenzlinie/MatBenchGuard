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


# === block: score_0 (check id='step04_compute_gruneisen') ===
def score_0(artifact, step, ctx):
    import csv, io, collections

    def score(artifact, step, ctx):
        if not artifact:
            return 0.0
        # build lookup from artifact
        data = {}
        for row in artifact:
            try:
                mode = row['mode'].strip()
                p = float(row['pressure_GPa'])
                g = float(row['gamma_T'])
                data.setdefault(mode, {})[p] = g
            except (KeyError, ValueError):
                continue
        check_pressures = step.get('check_pressures', [])
        signs = step.get('expected_gamma_signs', {})
        dirs = step.get('expected_gamma_direction', {})
        # sign check at first pressure
        sign_ok = 0
        sign_total = len(signs)
        for mode, exp_sign in signs.items():
            if mode not in data or check_pressures[0] not in data[mode]:
                continue
            val = data[mode][check_pressures[0]]
            if (exp_sign == 1 and val > 0) or (exp_sign == -1 and val < 0):
                sign_ok += 1
        sign_score = sign_ok / max(1, sign_total)
        # trend (monotonic direction)
        trend_ok = 0
        trend_total = len(dirs)
        for mode, dir_flag in dirs.items():
            if mode not in data:
                continue
            vals = []
            for p in check_pressures:
                if p in data[mode]:
                    vals.append(data[mode][p])
            if len(vals) < 2:
                continue
            correct = True
            for i in range(len(vals)-1):
                diff = vals[i+1] - vals[i]
                if dir_flag == 1:  # should increase
                    if diff < 0:
                        correct = False
                        break
                else:  # should decrease
                    if diff > 0:
                        correct = False
                        break
            if correct:
                trend_ok += 1
        trend_score = trend_ok / max(1, trend_total)
        return 0.5 * sign_score + 0.5 * trend_score


# === block: score_1 (check id='step07_final_frequencies') ===
def score_1(artifact, step, ctx):
    import csv

    def score(artifact, step, ctx):
        if not artifact:
            return 0.0
        # build lookup from artifact
        data = {}
        for row in artifact:
            try:
                mode = row['mode'].strip()
                p = float(row['pressure_GPa'])
                f = float(row['frequency_cm1'])
                data.setdefault(mode, {})[p] = f
            except (KeyError, ValueError):
                continue
        check_pressures = step.get('check_pressures', [])
        tol = step.get('tolerance', 5.0)
        ref_list = step.get('reference_frequencies', [])
        # build reference lookup
        ref = {}
        for item in ref_list:
            m = item['mode']
            p = item['pressure']
            f = item['frequency']
            ref.setdefault(m, {})[p] = f
        # tolerance pass rate
        total = 0
        passed = 0
        for mode, press_dict in ref.items():
            for p, gold in press_dict.items():
                total += 1
                if mode in data and p in data[mode]:
                    if abs(data[mode][p] - gold) <= tol:
                        passed += 1
        tol_score = passed / max(1, total)
        # trend check
        expected_trend = step.get('expected_freq_trend', {})
        trend_ok = 0
        trend_modes = 0
        for mode, trend in expected_trend.items():
            if mode not in data:
                continue
            vals = []
            for p in check_pressures:
                if p in data[mode]:
                    vals.append(data[mode][p])
            if len(vals) < 2:
                continue
            trend_modes += 1
            correct = True
            for i in range(len(vals)-1):
                diff = vals[i+1] - vals[i]
                if trend == 'increase':
                    if diff < 0:
                        correct = False
                        break
                else:  # decrease
                    if diff > 0:
                        correct = False
                        break
            if correct:
                trend_ok += 1
        trend_score = trend_ok / max(1, trend_modes)
        return 0.8 * tol_score + 0.2 * trend_score


_SCORERS = {
    'step04_compute_gruneisen': score_0,
    'step07_final_frequencies': score_1,
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
