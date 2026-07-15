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


# === block: score_0 (check id='step_01_results_check') ===
def score_0(artifact, step, ctx):
    config = step.get('config', {})
    eq_tol = config.get('eq_tol', 1e-6)
    rel_tol = config.get('rel_tol', 1e-5)
    asym_tol = config.get('asym_tol', 0.01)
    large_alpha_thresh = config.get('large_alpha_threshold', 50.0)

    rows = artifact
    if not isinstance(rows, list):
        return 0.0

    alphas, ps, E0s, ms = [], [], [], []
    for row in rows:
        try:
            a = float(row.get('alpha', None))
            p = float(row.get('p', None))
            e = float(row.get('E0', None))
            m = float(row.get('m_star_over_m', None))
        except (TypeError, ValueError):
            continue
        alphas.append(a)
        ps.append(p)
        E0s.append(e)
        ms.append(m)

    num_rows = len(alphas)
    if num_rows == 0:
        return 0.0

    # Consistency check: p satisfies equation, E0 and m*/m computed correctly from p
    consistency_scores = []
    for i in range(num_rows):
        a = alphas[i]
        p = ps[i]
        e = E0s[i]
        m = ms[i]
        if p == 0:
            eq_ok = False
        else:
            residual = abs(p**4 * (1 - 2*a/(3*p)) - 1)
            eq_ok = residual < eq_tol
        try:
            e_exp = -3*(p**2 - 1)*(p**2 + 3)/(4*p**2)
            e_rel_err = abs(e - e_exp) / max(abs(e_exp), 1e-12)
            m_exp = ((p**2 - 1)*(p**4 + 2*p**2 - 2))/(p**2 + 1) + 1
            m_rel_err = abs(m - m_exp) / max(abs(m_exp), 1e-12)
        except ZeroDivisionError:
            eq_ok = False
            e_rel_err = 1.0
            m_rel_err = 1.0
        row_ok = eq_ok and (e_rel_err < rel_tol) and (m_rel_err < rel_tol)
        consistency_scores.append(1.0 if row_ok else 0.0)

    consistency_score = sum(consistency_scores) / num_rows

    # Asymptotic check for large alpha
    asymp_scores = []
    for i in range(num_rows):
        a = alphas[i]
        if a >= large_alpha_thresh:
            e = E0s[i]
            m = ms[i]
            re = e * 3 / (a**2)
            rm = m * 81 / (16 * a**4)
            if abs(re + 1) < asym_tol and abs(rm - 1) < asym_tol:
                asymp_scores.append(1.0)
            else:
                asymp_scores.append(0.0)

    if asymp_scores:
        asymp_score = sum(asymp_scores) / len(asymp_scores)
    else:
        asymp_score = 0.0

    total_score = 0.7 * consistency_score + 0.3 * asymp_score
    return total_score


_SCORERS = {
    'step_01_results_check': score_0,
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
