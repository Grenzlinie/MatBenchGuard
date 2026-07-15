import os
import json
import csv

# === author imports / helpers ===
import math, os, json


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
    return {"config": spec.get("config", {}), "tolerances": spec.get("steps", [])[0].get("tolerances", {})}


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    def compute_SN(aero, w, q2, cfg):
        A = cfg['A']
        B = cfg['B']
        A1 = cfg['A1']
        A2 = cfg['A2']
        F_ = cfg['F']
        rho_w = cfg['rho_w']
        rho_a = cfg['rho_a']
        pi = cfg['pi']
        table = cfg['S_star_table']
        aerosol = cfg['aerosols'].get(aero)
        if not aerosol:
            return None, None
        modes = []
        for m in aerosol['modes']:
            modes.append({
                'R_m': m['R_um'] * 1e-6,
                'ln_sigma': math.log(m['sigma']),
                'N_m3': m['N_cm3'] * 1e6
            })
        S = 0.01
        for i in range(1000):
            r_n_cr = (A / 3.0) * (4.0 / (B * S**2)) ** (1.0 / 3.0)
            N = 0.0
            for m in modes:
                xi = math.log(r_n_cr / m['R_m']) / (math.sqrt(2.0) * m['ln_sigma'])
                N += (m['N_m3'] / 2.0) * (1.0 - math.erf(xi))
            if N <= 0.0:
                return 0.0, 0.0
            R_val = (3.0 / (F_ * A1 * w)) * ((4.0 * pi * rho_w * A2 * N) / (3.0 * rho_a)) ** (2.0 / 3.0)
            r_star = math.sqrt(B / A) * (r_n_cr ** 1.5)
            sum_ter = 0.0
            for m in modes:
                alpha = 1.5 * m['ln_sigma']
                R_star = math.sqrt(B * (m['R_m'])**3 / A)
                term = R_star * math.exp(0.5 * alpha**2) * (1.0 + math.erf((math.log(R_star) + alpha**2 - math.log(r_star)) / (math.sqrt(2.0) * alpha)))
                sum_ter += (m['N_m3'] / 2.0) * term
            r0 = sum_ter / N
            q1 = (4.0 / 3.0) * pi * rho_w * N * r0**3 / rho_a
            Q0 = R_val**(3.0/4.0) * A2 * (q1 + q2)
            if Q0 <= table[0][0]:
                S_star = table[0][1]
            elif Q0 >= table[-1][0]:
                S_star = table[-1][1]
            else:
                for j in range(len(table)-1):
                    x0, y0 = table[j]
                    x1, y1 = table[j+1]
                    if x0 <= Q0 <= x1:
                        t = (Q0 - x0) / (x1 - x0)
                        S_star = y0 + t * (y1 - y0)
                        break
                else:
                    S_star = table[-1][1]
            S_new = R_val**(-3.0/4.0) * S_star
            if abs(S_new - S) < 1e-6 * max(1.0, S):
                S = S_new
                break
            S = S_new
        return S, N

    tol_s = ctx.get('tolerances', {}).get('S_max', {}).get('value', 0.05)
    tol_n = ctx.get('tolerances', {}).get('N', {}).get('value', 0.10)
    cfg = ctx['config']
    total = 0
    correct = 0
    for row in artifact:
        try:
            aero = row.get('aerosol_type', '').strip().lower()
            w = float(row['w'])
            q2 = float(row['q2'])
            s_agent = float(row['S_max'])
            n_agent = float(row['N'])
            s_ref, n_ref = compute_SN(aero, w, q2, cfg)
            if s_ref is None:
                total += 1
                continue
            if (abs(s_ref - s_agent) / (abs(s_ref) + 1e-12) <= tol_s and
                abs(n_ref - n_agent) / (abs(n_ref) + 1e-12) <= tol_n):
                correct += 1
            total += 1
        except Exception:
            total += 1
    return correct / total if total else 0.0


_SCORERS = {
    'step_01': score_0,
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
