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
    ctx = {}
    for step in spec.get("steps", []):
        ref = step.get("reference")
        if ref:
            ctx[step["id"]] = ref
    return ctx


# === block: score_0 (check id='transitions_check') ===
def score_0(artifact, step, ctx):
    ref = ctx.get("transitions_check", {})
    expected = ref.get("transitions", [])
    wl_tol = ref.get("wavelength_tol_nm", 5.0)
    osc_tol_rel = ref.get("oscillator_tol_rel", 0.2)
    if not isinstance(artifact, list) or len(artifact) < 1:
        return 0.0
    if not expected:
        return 0.0
    matched = 0
    for exp in expected:
        t_wl = float(exp["wavelength_nm"])
        t_osc = float(exp["oscillator_strength"])
        found = False
        for entry in artifact:
            try:
                wl = float(entry.get("wavelength_nm"))
                osc = float(entry.get("oscillator_strength"))
            except (TypeError, ValueError):
                continue
            if abs(wl - t_wl) <= wl_tol:
                if abs(osc - t_osc) <= osc_tol_rel * abs(t_osc):
                    found = True
                    break
        if found:
            matched += 1
    return matched / float(len(expected))


# === block: score_1 (check id='raman_check') ===
def score_1(artifact, step, ctx):
    ref = ctx.get("raman_check", {})
    if not isinstance(artifact, list) or not artifact:
        return 0.0
    try:
        rows = []
        for row in artifact:
            wl = float(row["wavelength_nm"])
            freq = float(row["mode_freq_cm1"])
            act = float(row["relative_raman_activity"])
            dep = float(row["depolarization_ratio"])
            rows.append((freq, wl, act, dep))
    except (KeyError, ValueError):
        return 0.0
    modes = {}
    for freq, wl, act, dep in rows:
        modes.setdefault(round(freq, 1), {})[wl] = (act, dep)
    if len(modes) < 4:
        return 0.0
    checks = []
    ok900 = 0
    total = 0
    for f, d in modes.items():
        if 900 in d:
            act, _ = d[900]
            if abs(act - 1.0) < 1e-6:
                ok900 += 1
            total += 1
    if total > 0:
        checks.append(ok900 / total)
    else:
        checks.append(0.0)
    ok280 = 0
    cnt280 = 0
    for f, d in modes.items():
        if 280 in d:
            act, _ = d[280]
            if 10 <= act <= 50:
                ok280 += 1
            cnt280 += 1
    if cnt280 > 0:
        checks.append(ok280 / cnt280)
    else:
        checks.append(0.0)
    ok240 = 0
    cnt240 = 0
    for f, d in modes.items():
        if 240 in d:
            act, _ = d[240]
            if act >= 5000:
                ok240 += 1
            cnt240 += 1
    if cnt240 > 0:
        checks.append(ok240 / cnt240)
    else:
        checks.append(0.0)
    okdep = 0
    cntdep = 0
    for f, d in modes.items():
        if 240 in d:
            _, dep = d[240]
            if 0.28 <= dep <= 0.38:
                okdep += 1
            cntdep += 1
    if cntdep > 0:
        checks.append(okdep / cntdep)
    else:
        checks.append(0.0)
    bump_range = ref.get("bump_mode_freq_range", [1600, 1650])
    bump_ok = False
    for f, d in modes.items():
        if bump_range[0] <= f <= bump_range[1]:
            if 260 in d and 300 in d and 250 in d:
                _, dep260 = d[260]
                _, dep300 = d[300]
                _, dep250 = d[250]
                if dep260 > dep300 and dep260 > dep250:
                    bump_ok = True
                    break
    checks.append(1.0 if bump_ok else 0.0)
    return sum(checks) / len(checks) if checks else 0.0


_SCORERS = {
    'transitions_check': score_0,
    'raman_check': score_1,
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
