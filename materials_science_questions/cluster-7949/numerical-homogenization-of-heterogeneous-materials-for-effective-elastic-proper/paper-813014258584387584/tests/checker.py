import os
import json
import csv

# === author imports / helpers ===
import json, math


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
    E0 = 3.3
    nu0 = 0.34
    E1 = 70.0
    nu1 = 0.27
    E2 = 101.0
    nu2 = 0.06
    f0 = 0.7254
    f1 = 0.1433
    f2 = 0.1313

    def bulk_shear(E, nu):
        K = E / (3.0 * (1.0 - 2.0*nu))
        G = E / (2.0 * (1.0 + nu))
        return K, G

    def young_poisson(K, G):
        E = 9.0*K*G / (3.0*K + G)
        nu = (3.0*K - 2.0*G) / (2.0*(3.0*K + G))
        return E, nu

    K0, G0 = bulk_shear(E0, nu0)
    K1, G1 = bulk_shear(E1, nu1)
    K2, G2 = bulk_shear(E2, nu2)

    K_dil = K0
    G_dil = G0
    for f, K, G in [(f1,K1,G1),(f2,K2,G2)]:
        K_dil += f * (K - K0) * (3.0*K0 + 4.0*G0) / (3.0*K + 4.0*G0)
        denom_G = G0*(9.0*K0 + 8.0*G0) + 6.0*G*(K0 + 2.0*G0)
        G_dil += f * 5.0*G0*(G - G0)*(3.0*K0 + 4.0*G0) / denom_G

    E_dil, nu_dil = young_poisson(K_dil, G_dil)

    sum_num_K = 0.0
    sum_den_K = 0.0
    sum_num_G = 0.0
    sum_den_G = 0.0
    for f,K,G in [(f0,K0,G0),(f1,K1,G1),(f2,K2,G2)]:
        sum_num_K += f * K / (3.0*K + 4.0*G0)
        sum_den_K += f / (3.0*K + 4.0*G0)
        denom_G = G0*(9.0*K0 + 8.0*G0) + 6.0*G*(K0 + 2.0*G0)
        sum_num_G += f * G / denom_G
        sum_den_G += f / denom_G

    K_mt = sum_num_K / sum_den_K
    G_mt = sum_num_G / sum_den_G

    E_mt_val, nu_mt_val = young_poisson(K_mt, G_mt)

    return {
        "ref": {
            "E_dil": E_dil,
            "v_dil": nu_dil,
            "E_mt": E_mt_val,
            "v_mt": nu_mt_val
        }
    }


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    import math

    step = step  # provided by harness
    artifact = artifact  # provided by harness
    ctx = ctx

    ref = ctx["ref"]
    tol = 1e-8
    score_per_field = []
    for field_info in step.get("fields", []):
        key = field_info["name"]
        if key not in artifact:
            score_per_field.append(0.0)
            continue
        val = artifact[key]
        ref_val = ref[key]
        if ref_val != 0.0:
            rel_err = abs(val - ref_val) / max(1e-12, abs(ref_val))
        else:
            rel_err = abs(val - ref_val)
        if rel_err <= tol:
            score_per_field.append(1.0)
        else:
            score_per_field.append(0.0)
    return sum(score_per_field) / len(score_per_field) if score_per_field else 0.0


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
