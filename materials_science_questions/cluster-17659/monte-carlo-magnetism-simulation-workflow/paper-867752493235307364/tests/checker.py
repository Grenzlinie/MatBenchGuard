import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.optimize import minimize_scalar
from scipy.special import i0, i1


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
        p=3
        beta=100.0
        beta0=2.0
        s_vals = np.arange(0.0, 1.01, 0.01).round(6)
        tau_vals = np.arange(0.0, 1.01, 0.01).round(6)
        ref_id = {}
        ref_ft = {}
        ref_sv = {}
        ref_sa = {}
        def global_min(f, bounds=(0,1), n_pts=100):
            ms = np.linspace(bounds[0], bounds[1], n_pts)
            fv = np.array([f(m) for m in ms])
            idx = np.argmin(fv)
            res = minimize_scalar(f, bounds=bounds, method='bounded', options={'maxiter':500,'xatol':1e-12})
            return res.x
        def f0(m,s,tau):
            t = s*p*m**(p-1)
            return s*(p-1)*m**p - (1-tau)*np.sqrt(t**2+1) - tau*t
        def fft(m,s,tau):
            t = s*p*m**(p-1)
            a1 = np.sqrt(t**2+1)
            a2 = t
            return s*(p-1)*m**p - (1/beta)*((1-tau)*np.log(2*np.cosh(beta*a1)) + tau*np.log(2*np.cosh(beta*a2)))
        def fsv(m,s,tau):
            t = s*p*m**(p-1)
            a1 = np.sqrt(t**2+1)
            a2 = t
            z1 = beta*a1; z2 = beta*a2
            return s*(p-1)*m**p - (1/beta)*((1-tau)*np.log(2*np.pi*i0(z1)) + tau*np.log(2*np.pi*i0(z2)))
        def fsa(m,s,tau):
            return (p-1)*m**p - tau*(1/beta0)*np.log(2*np.cosh(beta0*p*m**(p-1)))
        for s in s_vals:
            for tau in tau_vals:
                m0 = global_min(lambda m: f0(m,s,tau))
                ref_id[(s.item(),tau.item())] = m0
                mft = global_min(lambda m: fft(m,s,tau))
                ref_ft[(s.item(),tau.item())] = mft
                msv = global_min(lambda m: fsv(m,s,tau))
                ref_sv[(s.item(),tau.item())] = msv
                msa = global_min(lambda m: fsa(m,s,tau))
                ref_sa[(s.item(),tau.item())] = msa
        s_fine = np.arange(0.0, 1.0001, 0.005).round(6)
        ref_jump = []
        for tau in tau_vals:
            ms = []
            for sf in s_fine:
                m = global_min(lambda m: fft(m,sf,tau))
                ms.append(m)
            ms = np.array(ms)
            diff = np.abs(np.diff(ms))
            idx_jump = np.where(diff > 0.005)[0]
            for idx in idx_jump:
                low = ms[idx]; high = ms[idx+1]
                delta = abs(high - low)
                ref_jump.append({"tau": tau.item(), "delta_m": delta})
        ctx = {
            "ref_idealized": ref_id,
            "ref_finiteT": ref_ft,
            "ref_svmc": ref_sv,
            "ref_sa": ref_sa,
            "ref_jump": ref_jump,
            "tol_m": 0.001,
            "tol_tau": 0.005,
            "tol_dm": 0.001
        }
        return ctx


# === block: score_0 (check id='idealized') ===
def score_0(artifact, step, ctx):
    if ctx is None:
        return 0.0

    if not artifact:
        return 0.0

    ref = ctx["ref_idealized"]
    tol = ctx["tol_m"]
    correct = 0
    total = 0
    for row in artifact:
        s = round(float(row["s"]), 6)
        tau = round(float(row["tau"]), 6)
        m_agent = float(row["m"])
        key = (s, tau)
        if key in ref:
            m_ref = ref[key]
            if abs(m_agent - m_ref) <= tol:
                correct += 1
            total += 1
    if total == 0:
        return 0.0
    return correct / total


# === block: score_1 (check id='finiteT') ===
def score_1(artifact, step, ctx):
    ref = ctx["ref_finiteT"]
    tol = ctx["tol_m"]
    correct = 0
    total = 0
    for row in artifact:
        s = round(float(row["s"]), 6)
        tau = round(float(row["tau"]), 6)
        m_agent = float(row["m"])
        key = (s, tau)
        if key in ref:
            m_ref = ref[key]
            if abs(m_agent - m_ref) <= tol:
                correct += 1
            total += 1
    if total == 0:
        return 0.0
    return correct / total


# === block: score_2 (check id='jump') ===
def score_2(artifact, step, ctx):
    ref_jump = ctx["ref_jump"]
    tol_tau = ctx["tol_tau"]
    tol_dm = ctx["tol_dm"]
    n_ref = len(ref_jump)
    if n_ref == 0:
        return 0.0
    n_correct = 0
    for rj in ref_jump:
        tau_r = rj["tau"]
        dm_r = rj["delta_m"]
        matched = False
        for row in artifact:
            tau_a = float(row["tau"])
            dm_a = float(row["delta_m"])
            if abs(tau_a - tau_r) <= tol_tau and abs(dm_a - dm_r) <= tol_dm:
                matched = True
                break
        if matched:
            n_correct += 1
    return n_correct / n_ref


# === block: score_3 (check id='svmc') ===
def score_3(artifact, step, ctx):
    ref = ctx["ref_svmc"]
    tol = ctx["tol_m"]
    correct = 0
    total = 0
    for row in artifact:
        s = round(float(row["s"]), 6)
        tau = round(float(row["tau"]), 6)
        m_agent = float(row["m"])
        key = (s, tau)
        if key in ref:
            m_ref = ref[key]
            if abs(m_agent - m_ref) <= tol:
                correct += 1
            total += 1
    if total == 0:
        return 0.0
    return correct / total


# === block: score_4 (check id='sa') ===
def score_4(artifact, step, ctx):
    ref = ctx["ref_sa"]
    tol = ctx["tol_m"]
    correct = 0
    total = 0
    for row in artifact:
        s = round(float(row["s"]), 6)
        tau = round(float(row["tau"]), 6)
        m_agent = float(row["m"])
        key = (s, tau)
        if key in ref:
            m_ref = ref[key]
            if abs(m_agent - m_ref) <= tol:
                correct += 1
            total += 1
    if total == 0:
        return 0.0
    return correct / total


_SCORERS = {
    'idealized': score_0,
    'finiteT': score_1,
    'jump': score_2,
    'svmc': score_3,
    'sa': score_4,
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
