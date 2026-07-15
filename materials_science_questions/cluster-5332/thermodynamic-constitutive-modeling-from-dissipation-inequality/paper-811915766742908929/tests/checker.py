import os
import json
import csv

# === author imports / helpers ===
import math, csv


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
    # constants from Tables I and II
    G = 51e9; nu = 0.3; rho = 9830; sigma0 = 200e6; rho_dm = 1e15; N = 4; lc = 1e-6; dtc = 2e-10; psi_inc_s = 1e-3; psi1 = psi2 = 3.3e-5
    c_s = math.sqrt(G / rho)
    v_cr_gold = math.sqrt(2) * c_s / N * math.sqrt((1 - nu) / (1 - 2 * nu))
    c_s_v_cr_sq = (c_s / v_cr_gold) ** 2

    def _ks_at(r, t):
        vd = r * v_cr_gold
        zeta_c = lc - N * vd * dtc
        if zeta_c <= 0:
            return 0.0
        zeta = -N * vd * t
        s = math.sqrt(24) * zeta / zeta_c
        psi_inc = psi_inc_s + psi1 * math.sin(s) + psi2 * math.cos(s)
        theta_psi = (G * rho_dm * zeta_c ** 2) / (3 * N ** 2) * c_s_v_cr_sq * (r ** 2) / (1 - r ** 2)
        U0f = lc ** 2 * rho_dm * sigma0 * psi_inc_s / 12.0
        D = (zeta_c ** 2 * rho_dm / 12.0) * (sigma0 * psi_inc + 0.5 * theta_psi * psi_inc ** 2)
        Uzeta_f = U0f - D
        return Uzeta_f / U0f

    gold_ks = {}
    for step in spec.get('steps', []):
        if step['id'] == 'ks_step':
            for cp in step.get('params', {}).get('checkpoints', []):
                r = cp['vd_over_vcr']
                t_ns = cp['t_ns']
                t = t_ns * 1e-9
                gold_ks[(r, t_ns)] = _ks_at(r, t)
    return {'v_cr_gold': v_cr_gold, 'gold_ks': gold_ks}


# === block: score_0 (check id='vcr_step') ===
def score_0(artifact, step, ctx):
    expected = ctx['v_cr_gold']
    tolerance = step.get('tolerance_abs', 50)
    raw = artifact.strip()
    if not raw:
        return 0.0
    try:
        val = float(raw)
    except (ValueError, TypeError):
        return 0.0
    return 1.0 if abs(val - expected) <= tolerance else 0.0


# === block: score_1 (check id='ks_step') ===
def score_1(artifact, step, ctx):
    agent_dict = {}
    for row in artifact:
        try:
            r = float(row['vd_over_vcr'])
            t_ns = float(row['t_ns'])
            ks = float(row['k_s'])
        except (ValueError, KeyError):
            continue
        agent_dict[(r, t_ns)] = ks
    checkpoints = step.get('params', {}).get('checkpoints', [])
    tolerance = step.get('params', {}).get('tolerance_abs', 0.05)
    errors = []
    for cp in checkpoints:
        key = (cp['vd_over_vcr'], cp['t_ns'])
        expected = ctx['gold_ks'].get(key)
        if expected is None or key not in agent_dict:
            return 0.0
        errors.append(abs(agent_dict[key] - expected))
    mae = sum(errors) / len(errors)
    score = max(0.0, 1.0 - mae / tolerance)
    return min(score, 1.0)


_SCORERS = {
    'vcr_step': score_0,
    'ks_step': score_1,
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
