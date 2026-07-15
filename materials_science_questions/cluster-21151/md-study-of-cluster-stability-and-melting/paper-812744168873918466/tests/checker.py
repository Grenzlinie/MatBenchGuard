import os
import json
import csv

# === author imports / helpers ===
import csv
import os
import math
from collections import defaultdict


def _find_nearest_temp(data, target_temp, key='temperature_K'):
    """Return row with temperature closest to target_temp, or None."""
    best = None
    best_diff = float('inf')
    for row in data:
        try:
            diff = abs(float(row[key]) - target_temp)
            if diff < best_diff:
                best_diff = diff
                best = row
        except (ValueError, KeyError):
            continue
    return best


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
    spec = grading_spec = globals().get('grading_spec', {})
    steps = spec.get('steps', [])
    ctx = {}
    for step in steps:
        sid = step.get('id')
        if sid:
            ctx[sid] = step.get('params', {})
    return ctx


# === block: score_0 (check id='step_03') ===
def score_0(artifact, step, ctx):
    def score_step_03(artifact, step, ctx):
        try:
            params = ctx.get('step_03', {})
            T_min = float(params.get('T_min', 970.0))
            T_max = float(params.get('T_max', 1170.0))
            rel_thresh = float(params.get('relative_peak_threshold', 0.05))
            temps = []
            cps = []
            for row in artifact:
                try:
                    t = float(row['temperature_K'])
                    cp = float(row['heat_capacity_J_per_mol_K'])
                    temps.append(t)
                    cps.append(cp)
                except (ValueError, KeyError):
                    return 0.0
            if not temps:
                return 0.0
            # compute global max Cp (ignoring possibly extreme outliers)
            global_max = max(cps)
            if global_max <= 0:
                return 0.0
            # find local maxima within window
            found_peak = False
            for i in range(1, len(temps)-1):
                t = temps[i]
                if T_min <= t <= T_max:
                    if cps[i] > cps[i-1] and cps[i] > cps[i+1]:
                        if cps[i] >= rel_thresh * global_max:
                            found_peak = True
                            break
            # also accept a strong singleton peak if only one point in window (edge case)
            if not found_peak:
                window_cps = [(t, cp) for t, cp in zip(temps, cps) if T_min <= t <= T_max]
                if window_cps:
                    max_cp_in_window = max(cp for _, cp in window_cps)
                    if max_cp_in_window >= rel_thresh * global_max:
                        found_peak = True
            return 1.0 if found_peak else 0.0
        except Exception:
            return 0.0


# === block: score_1 (check id='step_04') ===
def score_1(artifact, step, ctx):
    def score_step_04(artifact, step, ctx):
        try:
            params = ctx.get('step_04', {})
            T_low = float(params.get('T_low', 1000.0))
            T_high = float(params.get('T_high', 1100.0))
            drop_threshold = float(params.get('drop_threshold', 0.20))
            row_low = _find_nearest_temp(artifact, T_low)
            row_high = _find_nearest_temp(artifact, T_high)
            if row_low is None or row_high is None:
                return 0.0
            fcc_low = float(row_low['fcc_fraction'])
            fcc_high = float(row_high['fcc_fraction'])
            drop = fcc_low - fcc_high
            if drop <= 0:
                return 0.0
            # full credit if drop >= threshold
            if drop >= drop_threshold:
                return 1.0
            # partial credit proportional
            return max(0.0, min(1.0, drop / drop_threshold))
        except Exception:
            return 0.0


# === block: score_2 (check id='step_06') ===
def score_2(artifact, step, ctx):
    def score_step_06(artifact, step, ctx):
        try:
            params = ctx.get('step_06', {})
            T_min = float(params.get('T_min', 970.0))
            T_max = float(params.get('T_max', 1170.0))
            temps = []
            se = []
            for row in artifact:
                try:
                    t = float(row['temperature_K'])
                    val = float(row['surface_energy_mJ_per_m2'])
                    temps.append(t)
                    se.append(val)
                except (ValueError, KeyError):
                    return 0.0
            if len(temps) < 3:
                return 0.0
            for i in range(1, len(temps)-1):
                t = temps[i]
                if T_min <= t <= T_max:
                    if se[i] < se[i-1] and se[i] < se[i+1]:
                        return 1.0
            # also check if a single point in window is a minimum among its immediate neighbors (if window size 1)
            window_indices = [i for i, t in enumerate(temps) if T_min <= t <= T_max]
            if len(window_indices) == 1:
                idx = window_indices[0]
                if idx > 0 and idx < len(temps)-1:
                    if se[idx] < se[idx-1] and se[idx] < se[idx+1]:
                        return 1.0
            return 0.0
        except Exception:
            return 0.0


# === block: score_3 (check id='step_07') ===
def score_3(artifact, step, ctx):
    def score_step_07(artifact, step, ctx):
        try:
            expected = ctx.get('step_07', {}).get('expected', {})
            if not expected:
                return 0.0
            correct = 0
            total = len(expected)
            seen = set()
            for row in artifact:
                try:
                    shell = int(row['shell_number'])
                    ptype = row['transition_type'].strip()
                    if shell in expected and expected[str(shell)] == ptype:
                        correct += 1
                    seen.add(shell)
                except (ValueError, KeyError):
                    continue
            if total == 0:
                return 0.0
            return correct / total
        except Exception:
            return 0.0


_SCORERS = {
    'step_03': score_0,
    'step_04': score_1,
    'step_06': score_2,
    'step_07': score_3,
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
