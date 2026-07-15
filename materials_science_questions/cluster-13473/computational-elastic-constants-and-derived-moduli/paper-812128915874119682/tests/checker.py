import os
import json
import csv

# === author imports / helpers ===
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
    return {}


# === block: score_0 (check id='step_02') ===
def score_0(artifact, step, ctx):
    fields = step.get("config", {}).get("fields", [])
    tol_factor = step.get("config", {}).get("tolerance_factor", 2.0)
    if not fields:
        return 0.0
    match = 0
    for f in fields:
        path = f["path"]
        ref = f["ref"]
        sigma = f["sigma"]
        parts = path.split(".")
        val = artifact
        for p in parts:
            if isinstance(val, dict) and p in val:
                val = val[p]
            else:
                val = None
                break
        if val is None:
            continue
        if abs(val - ref) <= tol_factor * sigma:
            match += 1
    return match / len(fields)


# === block: score_1 (check id='step_03') ===
def score_1(artifact, step, ctx):
    decay = step.get("config", {}).get("decay_scale_log_error", 0.2)
    if not artifact:
        return 0.0

    try:
        with open("/app/outputs/fitted_KT_params.json") as f:
            kt_params = json.load(f)
    except Exception:
        return 0.0

    errors = []
    for row in artifact:
        try:
            beta = int(row["beta_lambda"])
            L = float(row["L"])
            l0 = float(row["l0"])
            chi6 = float(row["chi6"])
        except (KeyError, ValueError):
            continue
        if chi6 <= 0 or L <= 0 or l0 <= 0:
            continue

        key = f"beta_lambda_{beta}"
        if key not in kt_params:
            continue
        a = float(kt_params[key]["a_chi"])
        b = float(kt_params[key]["b_chi"])
        l0_star = float(kt_params[key]["l0_star"])

        # KT form valid only for l0 > l0_star
        if l0 <= l0_star:
            continue
        delta = l0 - l0_star
        if delta <= 0:
            continue

        # recompute ξ₆_fit from fitted KT parameters
        xi6_fit = (a * math.exp(b / math.sqrt(delta))) ** (4.0 / 7.0)
        if xi6_fit <= 0:
            continue

        chi6_scaled = chi6 / (L ** 1.75)
        expected = (xi6_fit / L) ** 1.75
        if expected <= 0 or chi6_scaled <= 0:
            continue

        ratio = chi6_scaled / expected
        if ratio <= 0:
            continue
        errors.append(abs(math.log(ratio)))

    if not errors:
        return 0.0
    mean_err = sum(errors) / len(errors)
    score = max(0.0, 1.0 - mean_err / decay)
    return score


# === block: score_2 (check id='step_04') ===
def score_2(artifact, step, ctx):
    sep_min = step.get("config", {}).get("peak_separation_min", 0.3)
    near_zero = step.get("config", {}).get("near_zero_max", 0.15)
    near_55 = step.get("config", {}).get("near_55_min", 0.45)
    valley_ratio = step.get("config", {}).get("valley_ratio_max", 0.5)
    required_N = step.get("config", {}).get("required_N", [196, 400, 784])
    if not artifact:
        return 0.0
    histograms = defaultdict(list)
    for row in artifact:
        try:
            N = int(row["N"])
            low = float(row["psi6_bin_low"])
            high = float(row["psi6_bin_high"])
            cnt = int(row["count"])
            histograms[N].append((low, high, cnt))
        except (KeyError, ValueError):
            continue
    pass_count = 0
    for N in required_N:
        if N not in histograms:
            continue
        bins = histograms[N]
        bins.sort(key=lambda x: x[0])
        mids = [(lo+hi)/2 for lo,hi,_ in bins]
        counts = [c for _,_,c in bins]
        n = len(counts)
        peaks = []
        for i in range(1, n-1):
            if counts[i] > counts[i-1] and counts[i] > counts[i+1]:
                peaks.append((mids[i], counts[i], i))
        if len(peaks) < 2:
            continue
        peaks.sort(key=lambda x: x[1], reverse=True)
        p1 = peaks[0]; p2 = peaks[1]
        pos1, cnt1, idx1 = p1
        pos2, cnt2, idx2 = p2
        if abs(pos1-pos2) < sep_min:
            continue
        if not ((pos1 <= near_zero and pos2 >= near_55) or (pos2 <= near_zero and pos1 >= near_55)):
            continue
        lo = min(idx1, idx2)
        hi = max(idx1, idx2)
        if hi - lo <= 1:
            continue
        valley_counts = [counts[i] for i in range(lo+1, hi)]
        min_valley = min(valley_counts)
        min_peak = min(cnt1, cnt2)
        if min_valley / min_peak <= valley_ratio:
            pass_count += 1
    score = pass_count / len(required_N)
    return score


_SCORERS = {
    'step_02': score_0,
    'step_03': score_1,
    'step_04': score_2,
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
