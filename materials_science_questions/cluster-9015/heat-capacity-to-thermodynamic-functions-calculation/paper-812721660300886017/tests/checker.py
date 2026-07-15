import os
import json
import csv

# === author imports / helpers ===
import os, json, csv, math


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
    params = spec.get('integration_params', {})
    a = params['a']; b = params['b']; c = params['c']; d = params['d']
    H_f_298 = params['H_f_298']  # kJ/mol
    S_f_298 = params['S_f_298']  # J/mol/K
    T0 = 298.15

    def Cp(T):
        return a*T*T + b*T + c*T**(-0.5) + d

    def int_Cp_dT(T):
        # ∫_{T0}^{T} Cp dT
        return (a/3)*(T**3 - T0**3) + (b/2)*(T**2 - T0**2) + 2*c*(T**0.5 - T0**0.5) + d*(T - T0)

    def int_Cp_over_T(T):
        # ∫_{T0}^{T} (Cp/T) dT
        return (a/2)*(T**2 - T0**2) + b*(T - T0) - 2*c*(T**(-0.5) - T0**(-0.5)) + d*(math.log(T) - math.log(T0))

    def compute_gold(T):
        delta_H_J = int_Cp_dT(T)   # J/mol
        H = H_f_298 + delta_H_J/1000.0   # kJ/mol
        S = S_f_298 + int_Cp_over_T(T)   # J/mol/K
        G = H - T * S / 1000.0          # kJ/mol
        Cp_val = Cp(T)
        return {'Cp': Cp_val, 'S': S, 'H': H, 'G': G}

    return {'params': params, 'compute_gold': compute_gold}


# === block: score_0 (check id='step_02_export_csv') ===
def score_0(artifact, step, ctx):
    if not artifact:
        return 0.0
    tol = step['tolerance']
    S_abs = tol['S_abs_tol']
    H_rel = tol['H_rel_tol']; H_floor = tol['H_abs_floor']
    G_rel = tol['G_rel_tol']; G_floor = tol['G_abs_floor']
    Cp_rel = tol['Cp_rel_tol']; Cp_floor = tol['Cp_abs_floor']
    compute_gold = ctx['compute_gold']
    rows_scores = []
    for row in artifact:
        try:
            T = float(row['T(K)'])
            agent_Cp = float(row['Cp(J/mol/K)'])
            agent_S = float(row['S(J/mol/K)'])
            agent_G = float(row['G(kJ/mol)'])
            agent_H = float(row['H(kJ/mol)'])
        except (KeyError, ValueError):
            continue
        gold = compute_gold(T)
        # S: absolute tolerance
        S_ok = 1.0 if abs(gold['S'] - agent_S) <= S_abs else 0.0
        # H: relative with floor
        gH = abs(gold['H'])
        if gH < H_floor:
            H_ok = 1.0 if abs(gold['H'] - agent_H) <= H_floor else 0.0
        else:
            H_ok = 1.0 if abs(gold['H'] - agent_H) <= H_rel * gH else 0.0
        # G: relative with floor
        gG = abs(gold['G'])
        if gG < G_floor:
            G_ok = 1.0 if abs(gold['G'] - agent_G) <= G_floor else 0.0
        else:
            G_ok = 1.0 if abs(gold['G'] - agent_G) <= G_rel * gG else 0.0
        # Cp: relative with floor
        gCp = abs(gold['Cp'])
        if gCp < Cp_floor:
            Cp_ok = 1.0 if abs(gold['Cp'] - agent_Cp) <= Cp_floor else 0.0
        else:
            Cp_ok = 1.0 if abs(gold['Cp'] - agent_Cp) <= Cp_rel * gCp else 0.0
        row_score = (S_ok + H_ok + G_ok + Cp_ok) / 4.0
        rows_scores.append(row_score)
    if not rows_scores:
        return 0.0
    return sum(rows_scores) / len(rows_scores)


# === block: score_1 (check id='step_03_zero_crossing') ===
def score_1(artifact, step, ctx):
    if not artifact:
        return 0.0
    text = artifact.strip()
    try:
        val = int(text)
    except ValueError:
        return 0.0
    if abs(val - step['target']) <= step['tolerance_abs']:
        return 1.0
    else:
        return 0.0


_SCORERS = {
    'step_02_export_csv': score_0,
    'step_03_zero_crossing': score_1,
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
