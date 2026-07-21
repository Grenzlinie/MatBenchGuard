import os
import json
import csv

# === author imports / helpers ===
import math

# Partial CPUA parameters (meters)
R1p = 0.01; R2p = 0.008
hpp = 0.0002; hbp = 0.000025; hmp = 0.0001
s11p = 1.82e-11; sbp = 1.934e-10; smp = 1.01e-11
nup = 0.31; d31p = -270e-12

# Half CPUA parameters
R1h = 0.01; R2h = 0.005
hph = 0.00016; hbh = 0.00001; hmh = 0.0001
s11h = 1.82e-11; sbh = 1.934e-10; smh = 1.01e-11
nuh = 0.31; d31h = -270e-12

def compute_deflection(r_mm, V, model, cpu_type):
    r = r_mm * 0.001
    if cpu_type == 'partial':
        R1, R2 = R1p, R2p
        hp, hb, hm = hpp, hbp, hmp
        s11, sb, sm = s11p, sbp, smp
        nu, d31 = nup, d31p
    else:
        R1, R2 = R1h, R2h
        hp, hb, hm = hph, hbh, hmh
        s11, sb, sm = s11h, sbh, smh
        nu, d31 = nuh, d31h

    if model == 'without_bonding':
        hb = 0.0

    if model == 'with_bonding':
        C5 = sm * (1+nu) * (1 - (R2**2)/(R1**2)) * (hp*hb + hb**2)
        C6 = sb * (4*hm*hb + 2*hm**2 + hm*hp)
        C7 = 4 * (s11**2) * (sb**2) * (hm**4)
        C8 = (sb**2)*(sm**2)*(hp**4) + s11*sb*(sm**2)*(4*hp*hb**3 + 4*hp**3*hb + 6*hp**2*hb**2) + (s11**2)*(sm**2)*(hb**4)
        C9 = s11*(sb**2)*sm*(2*hp**3*hm + 2*hp*hm**3 + 6*hp**2*hb*hm + 6*hp*hb**2*hm + 6*hp*hb*hm**2 + 3*hp**2*hm**2) \
             + (s11**2)*sb*sm*(8*hb*hm**3 + 8*hb**3*hm + 12*hb**2*hm**2)
        numerator_const = 3*(1+nu)*d31*s11*sb*sm*(C5 + C6)
        denom = C7 + (1+nu)**2 * (1 - (R2**2)/(R1**2))**2 * C8 + 4*(1+nu)*(1 - (R2**2)/(R1**2))*C9
    else:
        C10 = 2*hm**2 + 2*hm*hp
        C11 = 4*s11*(hm**4)
        C12 = (sm**2)*(hp**4)
        C13 = s11*sm*(2*hp**3*hm + 2*hp*hm**3 + 3*hp**2*hm**2)
        numerator_const = 3*(1+nu)*d31*s11*sm*C10
        denom = C11 + (1+nu)**2 * (1 - (R2**2)/(R1**2))**2 * C12 + 4*(1+nu)*(1 - (R2**2)/(R1**2))*C13

    if r <= R2:
        w = numerator_const * ((1 - (R2**2)/(R1**2))*r**2 + 2*(R2**2)*math.log(R2/R1)) * V / denom
    else:
        w = numerator_const * (2*(R2**2)*math.log(r) - (R2**2)/(R1**2)*r**2 - 2*(R2**2)*math.log(R1) + R2**2) * V / denom

    return w * 1000.0


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
    import os, csv

    def load_csv(path):
        if not os.path.exists(path):
            return None
        with open(path, newline='') as f:
            return list(csv.DictReader(f))

    partial = load_csv(os.path.join(outputs_dir, 'step_01_deflections_partial.csv'))
    half = load_csv(os.path.join(outputs_dir, 'step_02_deflections_half.csv'))
    return {"partial_profile": partial, "half_profile": half}


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    tolerance = step.get('tolerance', 1e-6)
    if not artifact:
        return 0.0
    correct = 0
    for row in artifact:
        try:
            r_mm = float(row['r'])
            voltage = int(row['voltage'])
            model = row['model'].strip()
            agent_def = float(row['deflection'])
            expected = compute_deflection(r_mm, voltage, model, 'partial')
            if abs(agent_def - expected) <= tolerance:
                correct += 1
        except Exception:
            continue
    return correct / len(artifact) if len(artifact) > 0 else 0.0


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    tolerance = step.get('tolerance', 1e-6)
    if not artifact:
        return 0.0
    correct = 0
    for row in artifact:
        try:
            r_mm = float(row['r'])
            voltage = int(row['voltage'])
            model = row['model'].strip()
            agent_def = float(row['deflection'])
            expected = compute_deflection(r_mm, voltage, model, 'half')
            if abs(agent_def - expected) <= tolerance:
                correct += 1
        except Exception:
            continue
    return correct / len(artifact) if len(artifact) > 0 else 0.0


# === block: score_2 (check id='step_03') ===
def score_2(artifact, step, ctx):
    tolerance = step.get('tolerance', 1e-6)
    if not artifact or len(artifact) == 0:
        return 0.0
    correct = 0
    for row in artifact:
        try:
            cpu_type = row.get('cpu_type', '').strip()
            voltage = int(row['voltage'])
            model = row.get('model', '').strip()
            cd_agent = float(row['central_deflection'])
            cd_expected = compute_deflection(0.0, voltage, model, cpu_type)
            if abs(cd_agent - cd_expected) > tolerance:
                continue
            # cross-check with profile
            profile = ctx.get('partial_profile' if cpu_type == 'partial' else 'half_profile')
            if profile is not None:
                found = False
                for prow in profile:
                    if (abs(float(prow['r']) - 0.0) < 1e-12 and
                        int(prow['voltage']) == voltage and
                        prow['model'].strip() == model):
                        if abs(float(prow['deflection']) - cd_agent) <= tolerance:
                            found = True
                        break
                if not found:
                    continue
            correct += 1
        except Exception:
            continue
    return correct / len(artifact)


_SCORERS = {
    'step_01': score_0,
    'step_02': score_1,
    'step_03': score_2,
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
