import os
import json
import csv

# === author imports / helpers ===
import numpy as np


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


# === block: score_0 (check id='s3_correlations') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        lines = artifact.strip().split('\n')
        if len(lines) < 200:
            return 0.0
        corr_map = {}
        for line in lines:
            parts = line.split()
            if len(parts) < 3:
                continue
            dx, dy, corr = int(parts[0]), int(parts[1]), float(parts[2])
            corr_map[(dx, dy)] = corr
        self_corr = corr_map.get((0, 0), None)
        nn_corr = corr_map.get((1, 0), None)
        checks = step.get('checks', {})
        valid_self = self_corr is not None and checks['self_corr_range'][0] <= self_corr <= checks['self_corr_range'][1]
        valid_nn = nn_corr is not None and nn_corr < -0.01 and checks.get('nn_corr_negative', False)
        if valid_self and valid_nn:
            return 1.0
        elif valid_self or valid_nn:
            return 0.5
        else:
            return 0.0


# === block: score_1 (check id='s4_dispersion') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        lines = artifact.strip().split('\n')
        if len(lines) < 8:
            return 0.0
        kx, ky, omega = [], [], []
        for line in lines:
            parts = line.split()
            if len(parts) < 3:
                continue
            kx.append(float(parts[0]))
            ky.append(float(parts[1]))
            omega.append(float(parts[2]))
        N = len(kx)
        if N == 0:
            return 0.0
        tol_rel = step.get('tol_rel', 0.1)
        tol_abs_gapless = step.get('tol_abs_gapless', 0.02)
        gapless = step.get('gapless_points', [])
        good = 0
        for i in range(N):
            kxi, kyi, om = kx[i], ky[i], omega[i]
            sw = 2.0 * np.sqrt(1.0 - ((np.cos(kxi) + np.cos(kyi)) / 2.0) ** 2)
            is_gapless = any(np.linalg.norm(np.array([kxi, kyi]) - np.array(gp)) < 1e-6 for gp in gapless)
            if is_gapless:
                if abs(om) <= tol_abs_gapless:
                    good += 1
            else:
                if sw > 1e-6:
                    err = abs(om - sw) / sw
                else:
                    err = abs(om)
                if err <= tol_rel:
                    good += 1
        return good / N


# === block: score_2 (check id='s5_gap_scaling') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        lines = artifact.strip().split('\n')
        rows = []
        for line in lines:
            parts = line.split()
            if len(parts) < 2:
                continue
            rows.append((int(parts[0]), float(parts[1])))
        if len(rows) != 3:
            return 0.0
        rows.sort(key=lambda x: x[0])
        Ls = [r[0] for r in rows]
        gaps = [r[1] for r in rows]
        if Ls != [16, 32, 64]:
            return 0.0
        monotonic = gaps[0] >= gaps[1] >= gaps[2]
        threshold_ok = gaps[2] <= step.get('max_gap_L64', 0.02)
        if monotonic and threshold_ok:
            return 1.0
        elif monotonic:
            return 0.5
        else:
            return 0.0


_SCORERS = {
    's3_correlations': score_0,
    's4_dispersion': score_1,
    's5_gap_scaling': score_2,
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
