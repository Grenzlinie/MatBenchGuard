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
    c0 = 1.0
    c1_afm = 0.05
    c1_ba = -0.05
    coeff_full_afm = (3 * c0 + c1_afm) / (c0 + c1_afm)
    coeff_trunc_afm = (c0 + 3 * c1_afm) / (2 * c1_afm)
    abs_c1_ba = abs(c1_ba)
    coeff_full_ba = 4 * (3 * c0 - 5 * abs_c1_ba) / (c0 - abs_c1_ba)
    coeff_trunc_ba = (c0 + abs_c1_ba) / abs_c1_ba
    tol = 1e-5
    return {
        'coeff_full_afm': coeff_full_afm,
        'coeff_trunc_afm': coeff_trunc_afm,
        'coeff_full_ba': coeff_full_ba,
        'coeff_trunc_ba': coeff_trunc_ba,
        'tol_abs': tol
    }


# === block: score_0 (check id='afm_boundary_consistency') ===
def score_0(artifact, step, ctx):
    if not artifact:
        return 0.0
    total = len(artifact)
    if total == 0:
        return 0.0
    ok_rows = 0
    for row in artifact:
        try:
            nc = float(row['n_c_over_n'])
            fz = float(row['Fz_nc_over_n'])
            pb = float(row['p_b_over_c1n'])
            nc_t = float(row['n_c_over_n_truncated'])
            fz_t = float(row['Fz_nc_over_n_truncated'])
            pb_t = float(row['p_b_over_c1n_truncated'])
            expected = nc + ctx['coeff_full_afm'] * fz
            expected_t = nc_t + ctx['coeff_trunc_afm'] * fz_t
            def check(val, exp):
                ae = abs(val - exp)
                max_val = max(abs(exp), 1e-12)
                return ae < 0.001 or ae / max_val < 0.05
            if check(pb, expected) and check(pb_t, expected_t):
                ok_rows += 1
        except (KeyError, ValueError, TypeError):
            pass
    return ok_rows / total


# === block: score_1 (check id='ba_boundary_consistency') ===
def score_1(artifact, step, ctx):
    if not artifact:
        return 0.0
    total = len(artifact)
    if total == 0:
        return 0.0
    ok_rows = 0
    for row in artifact:
        try:
            nc = float(row['n_c_over_n'])
            d_nc = float(row['d_nc_over_n'])
            qb = float(row['q_b_over_abs_c1n'])
            nc_t = float(row['n_c_over_n_truncated'])
            d_nc_t = float(row['d_nc_over_n_truncated'])
            qb_t = float(row['q_b_over_abs_c1n_truncated'])
            expected = 2 * nc - ctx['coeff_full_ba'] * d_nc
            expected_t = 2 * nc_t - ctx['coeff_trunc_ba'] * d_nc_t
            if abs(qb - expected) <= ctx['tol_abs'] and abs(qb_t - expected_t) <= ctx['tol_abs']:
                ok_rows += 1
        except (KeyError, ValueError, TypeError):
            pass
    return ok_rows / total


_SCORERS = {
    'afm_boundary_consistency': score_0,
    'ba_boundary_consistency': score_1,
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
