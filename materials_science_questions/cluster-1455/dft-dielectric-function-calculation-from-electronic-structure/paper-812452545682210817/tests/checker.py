import os
import json
import csv

# === author imports / helpers ===
import csv
import os
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
    return {}


# === block: score_0 (check id='step_bandgap') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not artifact or len(artifact) == 0:
            return 0.0
        cases = step.get('parameters', {}).get('cases', ['u0_25_25', 'u0_30_0'])
        required_t = [i * 0.01 for i in range(26)]
        t0_bounds = step.get('parameters', {}).get('t0_ratio_bounds', [0.12, 0.20])
        out_scores = []
        for case in cases:
            rows = [r for r in artifact if r.get('displacement_case', '') == case]
            if len(rows) < 26:
                out_scores.append(0.0)
                continue
            rows.sort(key=lambda r: float(r.get('time_fraction', 0)))
            ts = [float(r['time_fraction']) for r in rows]
            ratios = [float(r['bandgap_to_midgap_ratio']) for r in rows]
            t_ok = all(abs(ts[i] - required_t[i]) < 1e-6 for i in range(26))
            if not t_ok:
                out_scores.append(0.0)
                continue
            # monotonic decreasing
            mono = all(ratios[i] >= ratios[i+1] - 1e-9 for i in range(25))
            t0_ok = t0_bounds[0] <= ratios[0] <= t0_bounds[1]
            case_score = (0.5 if mono else 0.0) + (0.5 if t0_ok else 0.0)
            out_scores.append(case_score)
        return sum(out_scores) / len(out_scores) if out_scores else 0.0


# === block: score_1 (check id='step_guided') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not artifact or len(artifact) == 0:
            return 0.0
        params = step.get('parameters', {})
        expected_len = params.get('num_points', 51)
        start = params.get('wavevector_start', 0.0)
        end = params.get('wavevector_end', 0.5)
        step_val = params.get('wavevector_step', 0.01)
        freq_lo = params.get('freq_lower', 0.28)
        freq_hi = params.get('freq_upper', 0.33)
        rows = artifact
        len_score = 1.0 if len(rows) == expected_len else 0.0
        if len_score == 0.0:
            return 0.0
        rows.sort(key=lambda r: float(r.get('wavevector', 0)))
        wv = [float(r['wavevector']) for r in rows]
        expected_wv = [start + i * step_val for i in range(expected_len)]
        wv_match = all(abs(wv[i] - expected_wv[i]) < 1e-6 for i in range(expected_len))
        freqs = [float(r['frequency']) for r in rows]
        freq_ok = [1.0 if freq_lo <= f <= freq_hi else 0.0 for f in freqs]
        freq_score = sum(freq_ok) / len(freq_ok) if freq_ok else 0.0
        return 0.2 * len_score + 0.2 * (1.0 if wv_match else 0.0) + 0.6 * freq_score


_SCORERS = {
    'step_bandgap': score_0,
    'step_guided': score_1,
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
