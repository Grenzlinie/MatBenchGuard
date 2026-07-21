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
    def compute_ref(l):
        hH = hS = 1.0
        EH = 100.0; ES = 1.0
        nuH = 0.2; nuS = 0.3
        alphaH = 1.0; alphaS = 10.0
        d = 1.0; DeltaT = 1.0
        cH = hH/(hH+hS)
        denom_s = EH*hH*(1-nuS) + ES*hS*(1-nuH)
        tilde_alpha_x = (EH*hH*(1-nuS)*alphaH + ES*hS*(1-nuH)*alphaS) / denom_s
        tilde_sigma_S = - (EH*ES*hH) / denom_s * (alphaS - alphaH) * DeltaT
        tilde_sigma_H = (EH*ES*hS) / denom_s * (alphaS - alphaH) * DeltaT
        A = EH*hH*(1+nuS) + ES*hS*(1+nuH)
        B = denom_s
        denom_beta = cH * l * A * B
        beta1 = (hH**2 * EH * ES * (EH*hH + ES*hS)) / denom_beta
        beta2 = (hH**2 * EH * ES * (nuS*EH*hH + nuH*ES*hS)) / denom_beta
        GS = ES / (2*(1+nuS))
        term_g = 1.0 + 4.0/3.0 * (( (hH+hS)*l ) / (hS*(l+d)))**2
        gamma = term_g * (l-d)/(l+d)
        num = (tilde_sigma_S/ES)*(2*beta1 - nuS*(beta1+beta2)) - (tilde_sigma_H/EH)*(2*beta1 - nuH*(beta1+beta2))
        den = (2.0/(EH*hH))*(beta1**2 - nuH*beta1*beta2) + (2.0/(ES*hS))*(beta1**2 - nuS*beta1*beta2) + gamma*GS/(2.0*hS)
        delta_d = num/den
        alpha_x = tilde_alpha_x + (l*( (1.0/(EH*hH))*(beta1 - nuH*beta2) ) + d*( - (1.0/(ES*hS))*(beta1 - nuS*beta2) )) / (l+d) * (delta_d/DeltaT)
        alpha_y = tilde_alpha_x + (1.0/(EH*hH))*(beta2 - nuH*beta1) * (delta_d/DeltaT)
        sigma_x_H = tilde_sigma_H + (1.0/hH)*beta1*delta_d
        sigma_y_H = tilde_sigma_H + (1.0/hH)*beta2*delta_d
        vol_avg_alpha = cH*alphaH + (1-cH)*alphaS
        norm_stress = (alphaS - alphaH)*DeltaT*ES
        return (alpha_x/vol_avg_alpha, alpha_y/vol_avg_alpha, sigma_x_H/norm_stress, sigma_y_H/norm_stress)

    l_values = [3.0, 10.0, 20.0, 35.0]
    ref = {}
    for l in l_values:
        ref[l] = compute_ref(l)
    return {"ref": ref, "tol": 1e-6}


# === block: score_0 (check id='check_staggered_csv') ===
def score_0(artifact, step, ctx):
    ref = ctx["ref"]
    tol_rel = float(step.get("tolerance", 1e-6))
    found = 0
    total = len(ref)
    for row in artifact:
        try:
            ar = float(row["aspect_ratio"])
        except:
            continue
        if ar not in ref:
            continue
        expected = ref[ar]
        try:
            v1 = float(row["normalized_alpha_x"])
            v2 = float(row["normalized_alpha_y"])
            v3 = float(row["normalized_sigma_x_H"])
            v4 = float(row["normalized_sigma_y_H"])
        except:
            continue
        def close(a, b):
            if b == 0:
                return abs(a) < tol_rel
            return abs(a - b) / abs(b) <= tol_rel
        if all(close(v, e) for v, e in zip([v1, v2, v3, v4], expected)):
            found += 1
    score = found / total if total > 0 else 0.0
    return min(1.0, score)


_SCORERS = {
    'check_staggered_csv': score_0,
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
