import os
import json
import csv

# === author imports / helpers ===
import json
from pathlib import Path
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
    kM = 24.42
    muM = 13.27
    kK = 39.27
    muK = 14.07
    etaMs = 22.0e8
    etaMd = 7.75e8
    etaKs = 1.52e8
    etaKd = 0.254e8

    # bulk-side damage kernel coefficients
    Qo_o = (16./9.) * etaMs * (etaMs + 2*etaMd) / (etaMd * (2*etaMs + etaMd))
    Q1_o = (16./27.) * etaMs * (etaMs**2 + etaMd*etaMs + etaMd**2) / ((2*etaMs + etaMd)**2) * (
        3*(1./muM + 1./muK) - 2*(etaMs/etaMd)*(1./kM + 1./kK)
    )
    Qo_inf = (4./3.) * kM * (3*kM + 4*muM) / (muM * (3*kM + muM))
    Qm1_inf = - (4./3.) * kM * (9*kM**2 + 6*muM*kM + 4*muM**2) / ((3*kM + muM)**2) * (
        3*(kM/muM)*(1./etaMs + 1./etaKs) - 2*(1./etaMd + 1./etaKd)
    )

    # shear-side damage kernel coefficients
    M_o_o = (32./45.) * 3*etaMs * (3*etaMs + 2*etaMd) / ((etaMs + etaMd)*(2*etaMs + etaMd))
    M_1_o = (32./45.) * etaMs * etaMd * (7*etaMs**2 + 10*etaMs*etaMd + 4*etaMd**2) / ((etaMs + etaMd)**2 * (2*etaMs + etaMd)**2) * (
        etaMs/(3*kK) + etaMs/(3*kM) - etaMd/(2*muK) - etaMd/(2*muM)
    )
    M_o_inf = (16./45.) * (9*kM + 4*muM) * (3*kM + 4*muM) / ((3*kM + 2*muM)*(3*kM + muM))
    M_m1_inf = (16./15.) * kM * muM * (63*kM**2 + 60*kM*muM + 16*muM**2) / ((3*kM + muM)**2 * (3*kM + 2*muM)**2) * (
        3*kM/etaMs + 3*kM/etaKs - 2*muM/etaMd - 2*muM/etaKd
    )

    # solve linear systems
    kappa_M = Qo_inf
    v_M_s = Qo_o
    kappa_K = Qo_o + kK * ( 3*Q1_o/etaMs - (kappa_M - Qo_o)/kM )
    v_K_s = Qo_inf + etaKs * ( Qm1_inf/(3*kM) - (v_M_s - Qo_inf)/etaMs )

    m_M = M_o_inf
    v_M_d = M_o_o
    m_K = M_o_o + muK * ( 2*M_1_o/etaMd - (m_M - M_o_o)/muM )
    v_K_d = M_o_inf + etaKd * ( M_m1_inf/(2*muM) - (v_M_d - M_o_inf)/etaMd )

    gold = {
        "bulk": {"kappa_M": kappa_M, "kappa_K": kappa_K, "v_M_s": v_M_s, "v_K_s": v_K_s},
        "shear": {"m_M": m_M, "m_K": m_K, "v_M_d": v_M_d, "v_K_d": v_K_d}
    }
    return gold


# === block: score_0 (check id='step_compute_damage_constants') ===
def score_0(artifact, step, ctx):
    tol = 1e-6
    gold = ctx
    if not isinstance(artifact, dict):
        return 0.0
    if "bulk" not in artifact or "shear" not in artifact:
        return 0.0
    fields = [("bulk", "kappa_M"), ("bulk", "kappa_K"), ("bulk", "v_M_s"), ("bulk", "v_K_s"),
              ("shear", "m_M"), ("shear", "m_K"), ("shear", "v_M_d"), ("shear", "v_K_d")]
    scores = []
    for cat, key in fields:
        if cat not in gold or cat not in artifact or key not in gold[cat] or key not in artifact[cat]:
            scores.append(0.0)
            continue
        g = gold[cat][key]
        a = artifact[cat][key]
        if not isinstance(g, (int, float)) or not isinstance(a, (int, float)):
            scores.append(0.0)
            continue
        denom = max(abs(g), 1e-12)
        err = abs(a - g) / denom
        if err <= tol:
            scores.append(1.0)
        else:
            scores.append(max(0.0, 1.0 - err/tol))
    return sum(scores) / len(scores)


_SCORERS = {
    'step_compute_damage_constants': score_0,
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
