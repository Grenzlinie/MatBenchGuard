import os
import json
import csv

# === author imports / helpers ===
import csv
import os


def _lookup_frac(times, fracs, target_t):
    if not times:
        return None
    # assume times sorted
    n = len(times)
    if target_t <= times[0]:
        return fracs[0]
    if target_t >= times[-1]:
        return fracs[-1]
    for i in range(n - 1):
        t0, t1 = times[i], times[i + 1]
        if t0 <= target_t <= t1:
            if t1 == t0:
                return fracs[i]
            w = (target_t - t0) / (t1 - t0)
            return fracs[i] + w * (fracs[i + 1] - fracs[i])
    return None


def _is_monotonic(fracs, eps=1e-10):
    for i in range(1, len(fracs)):
        if fracs[i] < fracs[i - 1] - eps:
            return False
    return True


def _parse_two_col_csv(path):
    rows = []
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append(r)
    times = []
    fracs = []
    for r in rows:
        try:
            t = float(r['time_ps'])
            f = float(r['bcc_fraction'])
        except (ValueError, KeyError):
            continue
        times.append(t)
        fracs.append(f)
    # sort by time
    if times:
        paired = sorted(zip(times, fracs), key=lambda x: x[0])
        times, fracs = zip(*paired) if paired else ([], [])
        times = list(times)
        fracs = list(fracs)
    return times, fracs


def _parse_vol_csv(path):
    rows = []
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append(r)
    # group by volume
    vol_data = {}
    for r in rows:
        try:
            v = int(float(r['volume']))
            t = float(r['time_ps'])
            b = float(r['bcc_fraction'])
        except (ValueError, KeyError):
            continue
        vol_data.setdefault(v, []).append((t, b))
    for v in vol_data:
        vol_data[v].sort(key=lambda x: x[0])
    return vol_data


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
    oc_t, oc_f = (None, None)
    pp_t, pp_f = (None, None)
    vol_data = {}
    oc_frac30 = None
    pp_frac30 = None
    oc_monotonic = False
    pp_monotonic = False
    if os.path.exists('/app/outputs/olson_cohen_bcc_fraction.csv'):
        oc_t, oc_f = _parse_two_col_csv('/app/outputs/olson_cohen_bcc_fraction.csv')
        if oc_t:
            oc_frac30 = _lookup_frac(oc_t, oc_f, 30.0)
            oc_monotonic = _is_monotonic(oc_f)
    if os.path.exists('/app/outputs/perfect_perfect_bcc_fraction.csv'):
        pp_t, pp_f = _parse_two_col_csv('/app/outputs/perfect_perfect_bcc_fraction.csv')
        if pp_t:
            pp_frac30 = _lookup_frac(pp_t, pp_f, 30.0)
            pp_monotonic = _is_monotonic(pp_f)
    if os.path.exists('/app/outputs/volume_dependence_bcc_fraction.csv'):
        vol_data = _parse_vol_csv('/app/outputs/volume_dependence_bcc_fraction.csv')
    ctx = {
        'oc_frac30': oc_frac30,
        'oc_monotonic': oc_monotonic,
        'pp_frac30': pp_frac30,
        'pp_monotonic': pp_monotonic,
        'vol_data': vol_data
    }
    return ctx


# === block: score_0 (check id='oc_check') ===
def score_0(artifact, step, ctx):
    frac30 = ctx.get('oc_frac30')
    mono = ctx.get('oc_monotonic', False)
    score = 0.0
    if frac30 is not None:
        if frac30 > 0.01:
            score += 0.5
        if mono:
            score += 0.5
    return score


# === block: score_1 (check id='pp_check') ===
def score_1(artifact, step, ctx):
    pp_frac30 = ctx.get('pp_frac30')
    oc_frac30 = ctx.get('oc_frac30')
    mono = ctx.get('pp_monotonic', False)
    score = 0.0
    if pp_frac30 is not None:
        if pp_frac30 > 0.01:
            score += 0.4
        if oc_frac30 is not None and pp_frac30 > 0:
            ratio = oc_frac30 / pp_frac30
            if 0.5 <= ratio <= 2.0:
                score += 0.4
        elif oc_frac30 is None:
            # cannot check ratio, no credit
            pass
        if mono:
            score += 0.2
    return score


# === block: score_2 (check id='vol_check') ===
def score_2(artifact, step, ctx):
    vol_data = ctx.get('vol_data', {})
    target_volumes = [1, 2, 4, 8]
    frac30_by_vol = {}
    all_series_monotonic = True
    for v in target_volumes:
        if v not in vol_data:
            frac30_by_vol[v] = None
            all_series_monotonic = False
            continue
        pairs = vol_data[v]
        if not pairs:
            frac30_by_vol[v] = None
            all_series_monotonic = False
            continue
        ts = [p[0] for p in pairs]
        fs = [p[1] for p in pairs]
        frac30 = _lookup_frac(ts, fs, 30.0)
        frac30_by_vol[v] = frac30
        if not _is_monotonic(fs):
            all_series_monotonic = False

    frac30_values = [frac30_by_vol[v] for v in target_volumes if frac30_by_vol[v] is not None]
    vol8_frac = frac30_by_vol.get(8)
    vol_ordered = all(frac30_values[i] <= frac30_values[i + 1] + 1e-10 for i in range(len(frac30_values) - 1)) if len(frac30_values) >= 2 else False

    score = 0.0
    if vol8_frac is not None and vol8_frac > 0.1:
        score += 0.4
    if vol_ordered:
        score += 0.4
    if all_series_monotonic and any(frac30_by_vol[v] is not None for v in target_volumes):
        score += 0.2
    return score


_SCORERS = {
    'oc_check': score_0,
    'pp_check': score_1,
    'vol_check': score_2,
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
