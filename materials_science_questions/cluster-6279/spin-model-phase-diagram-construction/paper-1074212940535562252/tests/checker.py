import os
import json
import csv

# === author imports / helpers ===
try:
    import numpy as np
    from numpy.linalg import eigh
except ImportError:
    np = None
    eigh = None
import math
import csv


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


# === block: score_0 (check id='step_bounded') ===
def score_0(artifact, step, ctx):
        import math
        if np is None or eigh is None:
            return 0.0
        data = {}
        try:
            for row in artifact:
                lam = float(row["lambda"])
                nu = float(row["winding_number"])
                ln_gap = float(row["ln_gap"])
                gam = float(row["lyapunov_exponent"])
                data[lam] = (nu, ln_gap, gam)
        except (ValueError, TypeError, KeyError):
            pass
        params = step["recompute"]["params"]
        lambda_points = step["recompute"]["lambda_points"]
        tol_nu = step["recompute"]["winding_tolerance"]
        tol_gam = step["recompute"]["lyapunov_tolerance"]
        alpha = params["alpha"]
        t1 = params["t1"]
        t2 = params["t2"]
        b = params["b"]
        N = params["N"]

        def lyapunov(lam):
            n = np.arange(1, N+1)
            cos = np.cos(2*math.pi*alpha*n)
            t1p = t1 + lam*cos/(1.0 - b*cos)
            log_ratio = np.log(np.abs(t2)) - np.log(np.abs(t1p))
            return abs(np.mean(log_ratio))

        def winding_number(lam):
            n = np.arange(1, N+1)
            cos = np.cos(2*math.pi*alpha*n)
            t1p = t1 + lam*cos/(1.0 - b*cos)
            L = 2*N
            H = np.zeros((L, L))
            for i in range(N):
                idxA = 2*i
                idxB = 2*i+1
                H[idxA, idxB] = t1p[i]
                H[idxB, idxA] = t1p[i]
                if i < N-1:
                    nxtA = 2*(i+1)
                    H[idxB, nxtA] = t2
                    H[nxtA, idxB] = t2
            eigvals, eigvecs = eigh(H)
            occupied = eigvecs[:, :N]
            Q = np.zeros((L, L))
            Gamma = np.diag(np.tile([1, -1], N))
            for j in range(N):
                v_j = occupied[:, j].reshape(-1,1)
                Q += v_j @ v_j.T
                v_tilde = Gamma @ v_j
                Q -= v_tilde @ v_tilde.T
            X = np.diag(np.repeat(np.arange(1, N+1), 2))
            comm = Q @ X - X @ Q
            M = Gamma @ Q @ comm
            Lp = N
            start = (L - Lp)//2
            end = start + Lp
            sub = M[start:end, start:end]
            return np.trace(sub) / Lp

        nu_match = 0
        gam_match = 0
        total = len(lambda_points)
        for lam in lambda_points:
            if lam not in data:
                continue
            agent_nu, _, agent_gam = data[lam]
            comp_gam = lyapunov(lam)
            comp_nu = winding_number(lam)
            if abs(agent_gam - comp_gam) <= tol_gam:
                gam_match += 1
            if abs(agent_nu - comp_nu) <= tol_nu:
                nu_match += 1
        pt_score = (gam_match/total + nu_match/total) / 2.0 if total > 0 else 0.0

        all_lam = sorted(data.keys())
        nus_int = [round(data[l][0]) for l in all_lam]
        exp_seq = step["structural_checks"]["expected_nu_sequence"]
        distinct = []
        last = None
        for v in nus_int:
            if v != last:
                distinct.append(v)
                last = v
        seq_ok = distinct == exp_seq
        struct = 0.0
        if seq_ok:
            struct += 0.2
        transitions_lam = []
        for i in range(1, len(nus_int)):
            if nus_int[i] != nus_int[i-1]:
                transitions_lam.append(all_lam[i])
        if transitions_lam:
            gaps = {l: data[l][1] for l in all_lam}
            min_correct = 0
            for t in transitions_lam:
                idx = all_lam.index(t)
                left = gaps[all_lam[idx-1]] if idx > 0 else float('inf')
                right = gaps[all_lam[idx+1]] if idx+1 < len(all_lam) else float('inf')
                own = gaps[t]
                if own < left and own < right:
                    min_correct += 1
            struct += (min_correct / len(transitions_lam)) * 0.15
            small_gam = 0
            thr = step["structural_checks"]["lyapunov_small_threshold"]
            for t in transitions_lam:
                if abs(data[t][2]) < thr:
                    small_gam += 1
            struct += (small_gam / len(transitions_lam)) * 0.15
        return pt_score * 0.6 + struct * 0.4


# === block: score_1 (check id='step_unbounded') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        import math
        data = {}
        for row in artifact:
            lam = float(row["lambda"])
            nu = float(row["winding_number"])
            ln_gap = float(row["ln_gap"])
            gam = float(row["lyapunov_exponent"])
            data[lam] = (nu, ln_gap, gam)
        params = step["recompute"]["params"]
        lambda_points = step["recompute"]["lambda_points"]
        tol_nu = step["recompute"]["winding_tolerance"]
        tol_gam = step["recompute"]["lyapunov_tolerance"]
        alpha = params["alpha"]
        t1 = params["t1"]
        t2 = params["t2"]
        b = params["b"]
        N = params["N"]

        def lyapunov(lam):
            n = np.arange(1, N+1)
            cos = np.cos(2*math.pi*alpha*n)
            t1p = t1 + lam*cos/(1.0 - b*cos)
            log_ratio = np.log(np.abs(t2)) - np.log(np.abs(t1p))
            return abs(np.mean(log_ratio))

        def winding_number(lam):
            n = np.arange(1, N+1)
            cos = np.cos(2*math.pi*alpha*n)
            t1p = t1 + lam*cos/(1.0 - b*cos)
            L = 2*N
            H = np.zeros((L, L))
            for i in range(N):
                idxA = 2*i
                idxB = 2*i+1
                H[idxA, idxB] = t1p[i]
                H[idxB, idxA] = t1p[i]
                if i < N-1:
                    nxtA = 2*(i+1)
                    H[idxB, nxtA] = t2
                    H[nxtA, idxB] = t2
            eigvals, eigvecs = eigh(H)
            occupied = eigvecs[:, :N]
            Q = np.zeros((L, L))
            Gamma = np.diag(np.tile([1, -1], N))
            for j in range(N):
                v_j = occupied[:, j].reshape(-1,1)
                Q += v_j @ v_j.T
                v_tilde = Gamma @ v_j
                Q -= v_tilde @ v_tilde.T
            X = np.diag(np.repeat(np.arange(1, N+1), 2))
            comm = Q @ X - X @ Q
            M = Gamma @ Q @ comm
            Lp = N
            start = (L - Lp)//2
            end = start + Lp
            sub = M[start:end, start:end]
            return np.trace(sub) / Lp

        nu_match = 0
        gam_match = 0
        total = len(lambda_points)
        for lam in lambda_points:
            if lam not in data:
                continue
            agent_nu, _, agent_gam = data[lam]
            comp_gam = lyapunov(lam)
            comp_nu = winding_number(lam)
            if abs(agent_gam - comp_gam) <= tol_gam:
                gam_match += 1
            if abs(agent_nu - comp_nu) <= tol_nu:
                nu_match += 1
        pt_score = (gam_match/total + nu_match/total) / 2.0 if total > 0 else 0.0

        all_lam = sorted(data.keys())
        nus_int = [round(data[l][0]) for l in all_lam]
        exp_seq = step["structural_checks"]["expected_nu_sequence"]
        distinct = []
        last = None
        for v in nus_int:
            if v != last:
                distinct.append(v)
                last = v
        seq_ok = distinct == exp_seq
        struct = 0.0
        if seq_ok:
            struct += 0.2
        transitions_lam = []
        for i in range(1, len(nus_int)):
            if nus_int[i] != nus_int[i-1]:
                transitions_lam.append(all_lam[i])
        if transitions_lam:
            gaps = {l: data[l][1] for l in all_lam}
            min_correct = 0
            for t in transitions_lam:
                idx = all_lam.index(t)
                left = gaps[all_lam[idx-1]] if idx > 0 else float('inf')
                right = gaps[all_lam[idx+1]] if idx+1 < len(all_lam) else float('inf')
                own = gaps[t]
                if own < left and own < right:
                    min_correct += 1
            struct += (min_correct / len(transitions_lam)) * 0.15
            small_gam = 0
            thr = step["structural_checks"]["lyapunov_small_threshold"]
            for t in transitions_lam:
                if abs(data[t][2]) < thr:
                    small_gam += 1
            struct += (small_gam / len(transitions_lam)) * 0.15
        return pt_score * 0.6 + struct * 0.4


_SCORERS = {
    'step_bounded': score_0,
    'step_unbounded': score_1,
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
