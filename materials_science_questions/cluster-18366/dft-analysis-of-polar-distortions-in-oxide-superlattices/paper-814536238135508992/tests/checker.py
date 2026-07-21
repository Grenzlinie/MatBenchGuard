import os
import json
import csv

# === author imports / helpers ===
import numpy as np
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
    def prepare(outputs_dir, spec):
        hbar = 1.054571817e-27
        m_e = 9.10938356e-28
        m1 = 1.8*m_e
        m2 = 3.5*m_e
        m3 = 6.0*m_e
        a_B = 5.8e-7
        const = 0.2
        gamma_euler = 0.5772156649
        k_B = 1.380649e-16
        n_c1 = 1.2e18
        n_c2 = 2.5e19
        kF_c1 = (3*np.pi**2 * n_c1)**(1.0/3.0)
        mu_c1 = hbar**2 * kF_c1**2 / (2*m1)
        def n_s12(mu):
            k1 = np.sqrt(2*m1*mu)/hbar if mu>0 else 0.0
            k2 = np.sqrt(2*m2*max(0.0, mu - mu_c1))/hbar
            return (k1**3 + k2**3) / (3*np.pi**2)
        lo = mu_c1
        hi = 1e-10
        for _ in range(100):
            mid = (lo+hi)/2
            if n_s12(mid) < n_c2:
                lo = mid
            else:
                hi = mid
            if hi-lo < 1e-16:
                break
        mu_c2 = (lo+hi)/2
        def n_s_total(mu):
            k1 = np.sqrt(2*m1*mu)/hbar if mu>0 else 0.0
            k2 = np.sqrt(2*m2*max(0.0, mu - mu_c1))/hbar
            k3 = np.sqrt(2*m3*max(0.0, mu - mu_c2))/hbar
            return (k1**3 + k2**3 + k3**3) / (3*np.pi**2)
        def find_mu(n_s):
            lo=0.0; hi=1e-10
            for _ in range(100):
                mid=(lo+hi)/2
                if n_s_total(mid) < n_s:
                    lo=mid
                else:
                    hi=mid
                if hi-lo < 1e-16:
                    break
            return (lo+hi)/2
        def calc_T_C(n_s):
            mu = find_mu(n_s)
            k1 = np.sqrt(2*m1*max(0,mu))/hbar
            k2 = np.sqrt(2*m2*max(0, mu - mu_c1))/hbar
            k3 = np.sqrt(2*m3*max(0, mu - mu_c2))/hbar
            eps=1e-20
            x1 = np.pi * a_B * k1
            lam1 = 0.0 if x1<eps else (1/x1)*np.log(1+x1)
            x2 = np.pi * a_B * k2
            lam2 = 0.0
            if k2>eps:
                num = np.pi * a_B * k2**2
                denom = k1 + (m2/m1)*k2
                lam2 = (m2/(np.pi*m1*a_B*k2)) * np.log(1 + num/denom)
            x3 = np.pi * a_B * k3
            lam3 = 0.0
            if k3>eps:
                num = np.pi * a_B * k3**2
                denom = k1 + (m2/m1)*k2 + (m3/m1)*k3
                lam3 = (m3/(np.pi*m1*a_B*k3)) * np.log(1 + num/denom)
            prefactor = const * (gamma_euler/np.pi**3)
            TC1 = prefactor * (hbar**2/(m1*a_B**2)) * x1**2 * np.exp(-1.0/lam1) / k_B if lam1>0 else 0.0
            TC2 = prefactor * (hbar**2/(m2*a_B**2)) * x2**2 * np.exp(-1.0/lam2) / k_B if lam2>0 else 0.0
            TC3 = prefactor * (hbar**2/(m3*a_B**2)) * x3**2 * np.exp(-1.0/lam3) / k_B if lam3>0 else 0.0
            return TC1, TC2, TC3
        grid_ns = np.logspace(np.log10(5e17), np.log10(1e20), 300)
        ref_TC = np.zeros((len(grid_ns), 3))
        for i, ns in enumerate(grid_ns):
            TC1,TC2,TC3 = calc_T_C(ns)
            ref_TC[i,0]=TC1; ref_TC[i,1]=TC2; ref_TC[i,2]=TC3
        dense_ns = np.logspace(np.log10(5e17), np.log10(1e20), 5000)
        tc_dense = np.zeros((len(dense_ns),3))
        for i,ns in enumerate(dense_ns):
            tc1,tc2,tc3 = calc_T_C(ns)
            tc_dense[i,0]=tc1; tc_dense[i,1]=tc2; tc_dense[i,2]=tc3
        maxima = {}
        for b in range(3):
            idx = np.argmax(tc_dense[:,b])
            maxima[b+1] = (float(dense_ns[idx]), float(tc_dense[idx,b]))
        return {"ref_ns": grid_ns, "ref_TC": ref_TC, "ref_maxima": maxima}


# === block: score_0 (check id='check_tc_vs_ns') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not artifact:
            return 0.0
        try:
            rows = sorted(artifact, key=lambda r: float(r.get("n_s",0)))
        except:
            return 0.0
        n_s_agent = np.array([float(r["n_s"]) for r in rows])
        tc1_agent = np.array([float(r["T_C_1"]) for r in rows])
        tc2_agent = np.array([float(r["T_C_2"]) for r in rows])
        tc3_agent = np.array([float(r["T_C_3"]) for r in rows])
        ref_ns = ctx["ref_ns"]
        ref_TC = ctx["ref_TC"]
        tc1_interp = np.interp(ref_ns, n_s_agent, tc1_agent, left=tc1_agent[0], right=tc1_agent[-1])
        tc2_interp = np.interp(ref_ns, n_s_agent, tc2_agent, left=tc2_agent[0], right=tc2_agent[-1])
        tc3_interp = np.interp(ref_ns, n_s_agent, tc3_agent, left=tc3_agent[0], right=tc3_agent[-1])
        threshold = 1e-6
        errors = []
        for agent_vals, ref_vals in zip([tc1_interp,tc2_interp,tc3_interp], ref_TC.T):
            valid = ref_vals > threshold
            if not np.any(valid):
                continue
            rel_err = np.abs(agent_vals[valid] - ref_vals[valid]) / ref_vals[valid]
            errors.extend(rel_err.tolist())
        if not errors:
            return 1.0
        mean_rel_err = np.mean(errors)
        max_allowed = step.get("params",{}).get("max_rel_err",0.5)
        return float(max(0.0, 1.0 - mean_rel_err / max_allowed))


# === block: score_1 (check id='check_maxima') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        ref_maxima = ctx["ref_maxima"]
        try:
            agent_max = {}
            for row in artifact:
                band = int(row["band"])
                n = float(row["n_s_max"])
                tc = float(row["T_C_max"])
                agent_max[band] = (n, tc)
        except:
            return 0.0
        scores = []
        for band in [1,2,3]:
            if band not in agent_max or band not in ref_maxima:
                scores.append(0.0)
                continue
            n_agent, tc_agent = agent_max[band]
            n_ref, tc_ref = ref_maxima[band]
            rel_n = abs(n_agent - n_ref) / n_ref
            rel_tc = abs(tc_agent - tc_ref) / tc_ref
            err = max(rel_n, rel_tc)
            max_allowed = step.get("params",{}).get("max_rel_err_maxima",0.5)
            scores.append(max(0.0, 1.0 - err / max_allowed))
        return float(np.mean(scores))


_SCORERS = {
    'check_tc_vs_ns': score_0,
    'check_maxima': score_1,
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
