import os
import json
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


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        import csv, math
        # model parameters (SI)
        L_g = 40e-9
        A_g = L_g * L_g
        B = 2.38e-19
        E_val = 1e12
        t = 3.4e-10
        P_t = 10 * 101325.0  # 10 atm -> Pa
        Gamma_b = -0.232
        # helper
        def compute_energies(kappa_nm):
            if kappa_nm <= 0.0:
                return 0.0
            kappa_m = kappa_nm * 1e9  # m^-1
            Rd = 1.0 / kappa_m
            # A_pr
            A_pr = (B * Rd / P_t) ** 0.25 * math.pi * L_g / 2.0
            # A_s
            arg = L_g / (2.0 * Rd)
            if abs(arg) > 1.0:
                A_s = 0.0
            else:
                A_s = 2.0 * math.pi * Rd * Rd * (1.0 - math.cos(arg))
            # A_def
            A_def = A_pr + (math.pi / 4.0) * A_g - A_s
            if A_def <= 0.0:
                # fallback: avoid zero
                A_def = A_pr
            # strain and angle
            eps_s = (A_pr - A_def) / A_def
            theta_t = math.pi * (1.0 + eps_s)
            # spring constant
            ks = 2.0 * B * (A_g / (t * t)) * math.sqrt(P_t / E_val)
            E_s_spring = 0.5 * ks * (theta_t - math.pi) ** 2
            # critical angle
            theta_t_c = math.pi / (1.0 + ((E_val / (P_t * A_pr * A_pr)) ** (1.0/9.0)) * (t ** (4.0/9.0)))
            # slider
            if theta_t < theta_t_c:
                E_b_slider = (Gamma_b / 2.0) * A_def * (math.sin(theta_t_c / 2.0) - math.sin(theta_t / 2.0))
            else:
                E_b_slider = 0.0
            # potential energy
            Ep = P_t * (A_def * (Rd + math.sqrt(A_def) * math.cos(theta_t / 2.0) / 2.0) + A_s * Rd)
            return E_s_spring + E_b_slider + Ep

        rows = artifact
        if len(rows) < 20:
            return 0.0
        kappas = []
        agent_energies = []
        for r in rows:
            try:
                k = float(r.get('curvature_1_per_nm', 0))
                e = float(r.get('total_energy_J', 0))
                kappas.append(k)
                agent_energies.append(e)
            except:
                continue
        n = len(kappas)
        if n < 20:
            return 0.0
        gold_energies = [compute_energies(k) for k in kappas]
        # compute MAPE over points where gold energy magnitude > 1e-25
        sum_abs_pct = 0.0
        count = 0
        for g, a in zip(gold_energies, agent_energies):
            if abs(g) < 1e-25:
                if abs(a) < 1e-25:
                    continue
                else:
                    sum_abs_pct += 1.0  # large error
                    count += 1
            else:
                pct = abs(a - g) / abs(g)
                sum_abs_pct += pct
                count += 1
        if count == 0:
            return 1.0
        mape = sum_abs_pct / count
        threshold = 0.10
        if mape <= threshold:
            return 1.0
        else:
            # linear decay to 0 at 0.20
            score = max(0.0, 1.0 - (mape - threshold) / 0.10)
            return min(score, 1.0)


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        lines = artifact.strip().split('\n')
        if len(lines) < 2:
            return 0.0
        # parse line 1: A_g_c = <value> nm²
        line1 = lines[0].strip()
        import re
        area = None
        m = re.search(r'A_g_c\s*=\s*([\d.]+)\s*nm', line1, re.IGNORECASE)
        if m:
            try:
                area = float(m.group(1))
            except:
                pass
        # parse line 2: kappa_d_E = <value> nm⁻¹ or 'No root'
        line2 = lines[1].strip().lower()
        is_no_root = 'no root' in line2
        # sub-weights
        w_area = 0.6
        w_root = 0.4
        score = 0.0
        target_area = 3765
        rel_tol = 0.02
        if area is not None:
            if target_area == 0.0:
                area_ok = abs(area) < 1e-12
            else:
                area_ok = abs(area - target_area) / target_area <= rel_tol
            if area_ok:
                score += w_area
        if is_no_root:
            score += w_root
        return score


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
