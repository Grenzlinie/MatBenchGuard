import os
import json
import csv

# === author imports / helpers ===
import subprocess, sys
try:
    import numpy as np
    from scipy.interpolate import interp1d
    from scipy.integrate import quad
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "--no-cache-dir", "-i", "https://pypi.tuna.tsinghua.edu.cn/simple", "numpy", "scipy"])
    import numpy as np
    from scipy.interpolate import interp1d
    from scipy.integrate import quad


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
    return {"debye_params": spec.get("debye_params", {})}


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    freqs = np.array([float(row["frequency"]) for row in artifact])
    alphas = np.array([float(row["alpha"]) for row in artifact])
    order = np.argsort(freqs)
    freqs = freqs[order]
    alphas = alphas[order]
    if len(freqs) < 100:
        return 0.0
    if freqs[0] > 1e-3 or freqs[-1] < 1.99:
        return 0.0
    f_interp = interp1d(freqs, alphas, kind='linear', fill_value=np.nan, bounds_error=False)
    checks = step.get("checks", [])
    sub_scores = []
    for c in checks:
        if "freq" in c:
            freq = c["freq"]
            val = f_interp(freq)
            if np.isnan(val):
                sub_scores.append(0.0)
                continue
            if "expected_min" in c:
                if val >= c["expected_min"]:
                    sub_scores.append(1.0)
                else:
                    sub_scores.append(0.0)
            elif "expected_max" in c:
                if val <= c["expected_max"]:
                    sub_scores.append(1.0)
                else:
                    sub_scores.append(0.0)
        elif "region" in c:
            r = c["region"]
            mask = (freqs >= r[0]) & (freqs <= r[1])
            if np.any(mask):
                min_alpha = np.min(alphas[mask])
            else:
                min_alpha = np.min(alphas)
            if min_alpha <= c["max_alpha"]:
                sub_scores.append(1.0)
            else:
                sub_scores.append(0.0)
    if not sub_scores:
        return 0.0
    return sum(sub_scores) / len(sub_scores)


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    csv_path = os.path.join("/app/outputs", "step_01_transmission.csv")
    csv_data = load_artifact(csv_path)
    if csv_data is None:
        return 0.0
    freqs = np.array([float(row["frequency"]) for row in csv_data])
    alphas_raw = np.array([float(row["alpha"]) for row in csv_data])
    order = np.argsort(freqs)
    freqs = freqs[order]
    alphas_raw = alphas_raw[order]
    alpha_func = interp1d(freqs, alphas_raw, kind='linear', fill_value=0.0, bounds_error=False)
    params = ctx.get("debye_params", {})
    v_s = params["v_s"]
    omega_max = params["omega_max"]
    T = params["T"]
    hbar = params["hbar"]
    kB = params["kB"]
    k_max = omega_max / v_s
    def total_integral(k_t):
        kz_max = np.sqrt(abs(k_max**2 - k_t**2))
        if kz_max == 0:
            return 0.0
        def inner(k_z):
            k = np.sqrt(k_t**2 + k_z**2)
            omega = v_s * k
            if omega > omega_max:
                return 0.0
            alpha = alpha_func(omega)
            if np.isnan(alpha):
                return 0.0
            x = hbar * omega / (kB * T)
            if x > 700:
                dn_dT = 0.0
            else:
                dn_dT = (x * np.exp(x)) / (T * (np.exp(x) - 1)**2)
            v_gz = v_s * k_z / k
            return hbar * omega * v_gz * alpha * dn_dT
        inner_val, _ = quad(inner, 0, kz_max, limit=200, epsabs=1e-12, epsrel=1e-8)
        return inner_val * k_t
    G_scored, _ = quad(total_integral, 0, k_max, limit=200, epsabs=1e-12, epsrel=1e-8)
    G_scored /= (2*np.pi)**2
    def total_integral_free(k_t):
        kz_max = np.sqrt(abs(k_max**2 - k_t**2))
        if kz_max == 0:
            return 0.0
        def inner_free(k_z):
            k = np.sqrt(k_t**2 + k_z**2)
            omega = v_s * k
            if omega > omega_max:
                return 0.0
            x = hbar * omega / (kB * T)
            if x > 700:
                dn_dT = 0.0
            else:
                dn_dT = (x * np.exp(x)) / (T * (np.exp(x) - 1)**2)
            v_gz = v_s * k_z / k
            return hbar * omega * v_gz * dn_dT
        inner_val, _ = quad(inner_free, 0, kz_max, limit=200, epsabs=1e-12, epsrel=1e-8)
        return inner_val * k_t
    G_free, _ = quad(total_integral_free, 0, k_max, limit=200, epsabs=1e-12, epsrel=1e-8)
    G_free /= (2*np.pi)**2
    if G_free == 0:
        return 0.0
    ratio = G_scored / G_free
    threshold_ratio = step.get("threshold_ratio", 0.72)
    max_ratio_for_partial = step.get("max_ratio_for_partial", 1.0)
    if ratio <= threshold_ratio:
        return 1.0
    else:
        score = (max_ratio_for_partial - ratio) / (max_ratio_for_partial - threshold_ratio)
        return max(0.0, score)


_SCORERS = {
    'step_01': score_0,
    'step_02': score_1,
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
