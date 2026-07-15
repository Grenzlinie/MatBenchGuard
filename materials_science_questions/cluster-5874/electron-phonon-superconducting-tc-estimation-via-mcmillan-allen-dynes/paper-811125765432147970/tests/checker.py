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
    return {}


# === block: score_0 (check id='step_02_alpha2F_recompute') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not isinstance(artifact, list) or len(artifact) < 200:
            return 0.0
        first = artifact[0]
        if 'frequency (meV)' not in first or 'alpha2F' not in first:
            return 0.0
        freq = []
        a2f = []
        for row in artifact:
            try:
                f = float(row['frequency (meV)'])
                a = float(row['alpha2F'])
                if f < 0 or a < 0:
                    return 0.0
                freq.append(f)
                a2f.append(a)
            except:
                return 0.0
        n = len(freq)
        if n < 200:
            return 0.0
        # sort by frequency
        pairs = sorted(zip(freq, a2f), key=lambda x: x[0])
        freq_sorted, a2f_sorted = zip(*pairs) if pairs else ([], [])
        # trapezoidal integration
        def integrate(x, y):
            s = 0.0
            for i in range(1, len(x)):
                s += 0.5 * (y[i] + y[i-1]) * (x[i] - x[i-1])
            return s
        # Compute λ
        integrand_lam = [a / max(w, 1e-12) for w, a in zip(freq_sorted, a2f_sorted)]
        lam = 2.0 * integrate(freq_sorted, integrand_lam)
        if lam <= 0:
            return 0.0
        # Compute ω_log
        integrand_log = [a * math.log(max(w, 1e-12)) / max(w, 1e-12) for w, a in zip(freq_sorted, a2f_sorted)]
        omega_log = math.exp(2.0 / lam * integrate(freq_sorted, integrand_log))
        # McMillan-Allen-Dynes with μ* = 0.1
        mu_star = 0.1
        omega_log_K = omega_log * 11.6045
        denom = lam - mu_star * (1.0 + 0.62 * lam)
        if denom <= 0:
            return 0.0
        exponent = -1.04 * (1.0 + lam) / denom
        tc = (omega_log_K / 1.2) * math.exp(exponent)
        # scoring
        shape_score = 0.2
        lam_score = 0.3
        tc_score = 0.5
        total = 0.0
        total += shape_score
        target_lam = 7.0
        if 0.5 * target_lam <= lam <= 2.0 * target_lam:
            total += lam_score
        if abs(tc - 600.0) <= 100.0:
            total += tc_score
        return total


# === block: score_1 (check id='step_03_Tc_direct') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        try:
            tc_val = float(artifact.strip())
        except:
            return 0.0
        if abs(tc_val - 600.0) <= 100.0:
            return 1.0
        return 0.0


_SCORERS = {
    'step_02_alpha2F_recompute': score_0,
    'step_03_Tc_direct': score_1,
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
