import os
import json
import csv

# === author imports / helpers ===
import os
import json
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
        # Load the single scored artifact
        artifact_path = os.path.join(outputs_dir, 'dft_results.json')
        if not os.path.exists(artifact_path):
            return {'data': None}
        with open(artifact_path) as f:
            data = json.load(f)
        return {'data': data}


# === block: score_0 (check id='pristine_energy_diff') ===
def score_0(artifact, step, ctx):
        data = ctx.get('data')
        if data is None:
            return 0.0
        value = data.get('pristine_energy_diff_meV')
        if value is None:
            return 0.0
        target = step.get('target', 96.9)
        tol = step.get('tolerance', 5.0)
        diff = abs(value - target)
        if diff <= tol:
            return 1.0
        else:
            decay = (diff - tol) / tol
            return max(0.0, 1.0 - decay)


# === block: score_1 (check id='doped_energy_diff') ===
def score_1(artifact, step, ctx):
        data = ctx.get('data')
        if data is None:
            return 0.0
        value = data.get('doped_energy_diff_meV')
        if value is None:
            return 0.0
        target = step.get('target', 74.4)
        tol = step.get('tolerance', 5.0)
        diff = abs(value - target)
        if diff <= tol:
            return 1.0
        else:
            decay = (diff - tol) / tol
            return max(0.0, 1.0 - decay)


# === block: score_2 (check id='tc_estimation') ===
def score_2(artifact, step, ctx):
        data = ctx.get('data')
        if data is None:
            return 0.0
        pristine = data.get('pristine_energy_diff_meV')
        doped = data.get('doped_energy_diff_meV')
        reported_tc = data.get('estimated_Tc_K')
        if None in (pristine, doped, reported_tc) or pristine == 0:
            return 0.0
        expected_tc = 340.0 * doped / pristine
        internal_score = 1.0 if abs(reported_tc - expected_tc) <= 1.0 else 0.0
        target_tc = step.get('target_paper', 261.0)
        target_tol = step.get('target_tolerance', 10.0)
        tc_error = abs(reported_tc - target_tc)
        if tc_error <= target_tol:
            target_score = 1.0
        else:
            target_score = max(0.0, 1.0 - (tc_error - target_tol) / target_tol)
        # combine with 20% internal, 80% target closeness
        return 0.2 * internal_score + 0.8 * target_score


# === block: score_3 (check id='reduction') ===
def score_3(artifact, step, ctx):
        data = ctx.get('data')
        if data is None:
            return 0.0
        value = data.get('reduction_per_at_percent_K')
        if value is None:
            return 0.0
        target = step.get('target', 25.0)
        tol = step.get('tolerance', 3.0)
        diff = abs(value - target)
        if diff <= tol:
            return 1.0
        else:
            decay = (diff - tol) / tol
            return max(0.0, 1.0 - decay)


# === block: score_4 (check id='phonon_modes') ===
def score_4(artifact, step, ctx):
        data = ctx.get('data')
        if data is None:
            return 0.0
        phonon_modes = data.get('phonon_modes')
        if not isinstance(phonon_modes, list):
            return 0.0
        pristine_modes = []
        doped_modes = []
        for m in phonon_modes:
            freq = m.get('frequency_THz')
            desc = m.get('description', '').lower()
            if freq is None:
                continue
            if 'v-v' in desc or 'pristine' in desc:
                pristine_modes.append(freq)
            if 'w' in desc or 'doped' in desc:
                doped_modes.append(freq)
        pristine_ok = any(5.5 <= f <= 6.5 for f in pristine_modes)
        doped_ok = False
        if doped_modes:
            for f_doped in doped_modes:
                if 3.6 <= f_doped <= 4.8 and all(abs(f_doped - f_p) > 0.01 for f_p in pristine_modes):
                    doped_ok = True
                    break
        score = 0.0
        if pristine_ok:
            score += 0.5
        if doped_ok:
            score += 0.5
        return score


_SCORERS = {
    'pristine_energy_diff': score_0,
    'doped_energy_diff': score_1,
    'tc_estimation': score_2,
    'reduction': score_3,
    'phonon_modes': score_4,
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
