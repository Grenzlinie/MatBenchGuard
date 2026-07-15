import os
import json
import csv

# === author imports / helpers ===
import math, os, csv


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
    def prepare(outputs_dir, spec):
        gold_532 = {}
        for step in spec.get('steps', []):
            if step['id'] == 'step_532_intervals':
                gold_532 = step.get('gold_intervals', {})
        return {"gold_intervals_532": gold_532, "outputs_dir": outputs_dir}


# === block: score_0 (check id='step_532_data') ===
def score_0(artifact, step, ctx):
        if not artifact or len(artifact) < 2:
            return 0.0
        T = []
        Ne = []
        nm1 = []
        dndT = []
        e = []
        for row in artifact:
            try:
                T.append(float(row['T']))
                Ne.append(float(row['N_e']))
                nm1.append(float(row['n-1']))
                dndT.append(float(row['dn/dT']))
                e.append(float(row['e']))
            except (KeyError, TypeError, ValueError):
                return 0.0
        # Recompute e consistency
        for t, d, e_val in zip(T, dndT, e):
            if abs(d) < 1e-20:
                if not (math.isinf(e_val) or e_val > 1e6):
                    return 0.0
            else:
                expected = 1e-5 / (abs(d) * t)
                if abs(expected - e_val) / max(expected, 1e-9) > 1e-4:
                    return 0.0
        # Ne peak temperature
        max_idx = max(range(len(Ne)), key=lambda i: Ne[i])
        peak_T = T[max_idx]
        if abs(peak_T - 17000) > 1000:
            return 0.0
        # n-1 zero crossing
        zero_T = None
        for i in range(len(T)-1):
            if nm1[i] * nm1[i+1] <= 0:
                zero_T = T[i] + (T[i+1]-T[i]) * (-nm1[i])/(nm1[i+1]-nm1[i]) if nm1[i+1]!=nm1[i] else T[i]
                break
        if zero_T is None or abs(zero_T - 12000) > 1000:
            return 0.0
        # dn/dT zero crossing
        zdndT_T = None
        for i in range(len(T)-1):
            if dndT[i] * dndT[i+1] <= 0:
                zdndT_T = T[i] + (T[i+1]-T[i]) * (-dndT[i])/(dndT[i+1]-dndT[i]) if dndT[i+1]!=dndT[i] else T[i]
                break
        if zdndT_T is None or abs(zdndT_T - 17000) > 1000:
            return 0.0
        return 1.0


# === block: score_1 (check id='step_532_intervals') ===
def score_1(artifact, step, ctx):
    def score_532_intervals(artifact, step, ctx):
        data_path = os.path.join(ctx['outputs_dir'], 'thermo_optic_data_532nm.csv')
        if not os.path.exists(data_path):
            return 0.0
        with open(data_path, 'r') as f:
            reader = csv.DictReader(f)
            data_rows = list(reader)
        try:
            T = [float(row['T']) for row in data_rows]
            e = [float(row['e']) for row in data_rows]
        except Exception:
            return 0.0

        def find_interval(th):
            intervals = []
            start = None
            for i, val in enumerate(e):
                if val <= th:
                    if start is None:
                        start = T[i]
                else:
                    if start is not None:
                        intervals.append((start, T[i-1]))
                        start = None
            if start is not None:
                intervals.append((start, T[-1]))
            if not intervals:
                return None, None
            widest = max(intervals, key=lambda x: x[1]-x[0])
            return widest[0], widest[1]

        sub_intervals = {}
        for row in artifact:
            try:
                th = round(float(row.get('error_threshold', None)), 2)
                tl = float(row.get('T_lower', None))
                tu = float(row.get('T_upper', None))
                if tl is None or tu is None:
                    continue
                sub_intervals[th] = (tl, tu)
            except (TypeError, ValueError, KeyError):
                continue

        if not sub_intervals:
            return 0.0

        gold_532 = ctx.get('gold_intervals_532', {})
        tol = step.get('tolerance', 500)
        thresholds = [0.1, 0.12, 0.15, 0.2]
        total = 0.0
        cnt = 0
        for th in thresholds:
            th_str = str(th)
            if th_str not in gold_532:
                continue
            comp_l, comp_h = find_interval(th)
            if comp_l is None:
                continue
            sub_pair = sub_intervals.get(th)
            if sub_pair is None:
                continue
            sub_l, sub_h = sub_pair
            if abs(sub_l - comp_l) > 100 or abs(sub_h - comp_h) > 100:
                return 0.0
            g_low = gold_532[th_str]['lower']
            g_high = gold_532[th_str]['upper']
            score_th = max(0.0, 1.0 - (abs(sub_l - g_low) / tol) - (abs(sub_h - g_high) / tol))
            total += min(score_th, 1.0)
            cnt += 1
        if cnt == 0:
            return 0.0
        return total / cnt


# === block: score_2 (check id='step_808_data') ===
def score_2(artifact, step, ctx):
    def score_808_data(artifact, step, ctx):
        if not artifact or len(artifact) < 2:
            return 0.0
        try:
            T = [float(row['T']) for row in artifact]
            Ne = [float(row['N_e']) for row in artifact]
            dndT = [float(row['dn/dT']) for row in artifact]
            e = [float(row['e']) for row in artifact]
        except Exception:
            return 0.0
        # e consistency
        for t, d, e_val in zip(T, dndT, e):
            if abs(d) < 1e-20:
                if not (math.isinf(e_val) or e_val > 1e6):
                    return 0.0
            else:
                expected = 1e-5 / (abs(d) * t)
                if abs(expected - e_val) / max(expected, 1e-9) > 1e-4:
                    return 0.0
        # Ne peak
        max_idx = max(range(len(Ne)), key=lambda i: Ne[i])
        peak_T = T[max_idx]
        if abs(peak_T - 17000) > 1000:
            return 0.0
        # dn/dT zero crossing
        zdndT_T = None
        for i in range(len(T)-1):
            if dndT[i] * dndT[i+1] <= 0:
                zdndT_T = T[i] + (T[i+1]-T[i]) * (-dndT[i])/(dndT[i+1]-dndT[i]) if dndT[i+1]!=dndT[i] else T[i]
                break
        if zdndT_T is None or abs(zdndT_T - 17000) > 1000:
            return 0.0
        return 1.0


# === block: score_3 (check id='step_808_intervals') ===
def score_3(artifact, step, ctx):
    def score_808_intervals(artifact, step, ctx):
        data_path = os.path.join(ctx['outputs_dir'], 'thermo_optic_data_808nm.csv')
        if not os.path.exists(data_path):
            return 0.0
        with open(data_path, 'r') as f:
            reader = csv.DictReader(f)
            data_rows = list(reader)
        try:
            T = [float(row['T']) for row in data_rows]
            e = [float(row['e']) for row in data_rows]
        except Exception:
            return 0.0
        def find_interval(th):
            intervals = []
            start = None
            for i, val in enumerate(e):
                if val <= th:
                    if start is None:
                        start = T[i]
                else:
                    if start is not None:
                        intervals.append((start, T[i-1]))
                        start = None
            if start is not None:
                intervals.append((start, T[-1]))
            if not intervals:
                return None, None
            widest = max(intervals, key=lambda x: x[1]-x[0])
            return widest[0], widest[1]
        sub_808 = {}
        for row in artifact:
            th = round(float(row['error_threshold']), 2)
            sub_808[th] = (float(row['T_lower']), float(row['T_upper']))
        # consistency with raw data
        for th, (sub_l, sub_h) in sub_808.items():
            comp_l, comp_h = find_interval(th)
            if comp_l is None:
                if sub_l is not None:
                    return 0.0
                continue
            if abs(sub_l - comp_l) > 100 or abs(sub_h - comp_h) > 100:
                return 0.0
        # trend: width(808) > width(532)
        path_532 = os.path.join(ctx['outputs_dir'], 'error_intervals_532nm.csv')
        if not os.path.exists(path_532):
            return 0.0
        with open(path_532, 'r') as f:
            reader = csv.DictReader(f)
            sub_532 = {}
            for row in reader:
                th = round(float(row['error_threshold']), 2)
                sub_532[th] = (float(row['T_lower']), float(row['T_upper']))
        passed = 0
        total = 0
        for th, (l532, h532) in sub_532.items():
            if th in sub_808:
                l808, h808 = sub_808[th]
                if (h808 - l808) > (h532 - l532):
                    passed += 1
                total += 1
        if total == 0:
            return 0.0
        return passed / total


_SCORERS = {
    'step_532_data': score_0,
    'step_532_intervals': score_1,
    'step_808_data': score_2,
    'step_808_intervals': score_3,
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
