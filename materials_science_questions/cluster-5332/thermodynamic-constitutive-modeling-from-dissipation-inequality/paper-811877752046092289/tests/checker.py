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
    K1 = 1e9
    K2 = 5e9
    sigma_y2 = 30e6
    V = 2.0
    K_eq = (K1 + K2) / 2.0
    N = 20
    Ei_step = 0.1 / (N - 1)
    expected_Ei = [i * Ei_step for i in range(N)]

    # pre-compute expected values for each E_i
    expected = []
    for e_iexp in expected_Ei:
        W_i_exp = 0.5 * V * (K1 / K2) * K_eq * (e_iexp ** 2)
        Sigma_exp = (K_eq / K2) * (sigma_y2 + K1 * e_iexp)
        E_total_exp = Sigma_exp / K_eq + e_iexp
        Psi_exp = 0.5 * V * K_eq * (E_total_exp - e_iexp) ** 2 + W_i_exp
        D_exp = V * (K_eq / K2) * sigma_y2 * 1.0  # Ġ^i = 1 s^{-1}
        beta_d_exp = 1.0 / (1.0 + (K1 / sigma_y2) * e_iexp)
        beta_int_exp = 1.0 / (1.0 + (K1 / (2.0 * sigma_y2)) * e_iexp)
        expected.append((W_i_exp, Psi_exp, D_exp, beta_d_exp, beta_int_exp))

    return {
        'expected_Ei': expected_Ei,
        'expected_data': expected
    }


# === block: score_0 (check id='step_01_energetics') ===
def score_0(artifact, step, ctx):
    tol = step['params']['tolerances']
    ei_list = ctx['expected_Ei']
    expected = ctx['expected_data']

    if len(artifact) != len(ei_list):
        return 0.0

    all_ok = True
    for i, row in enumerate(artifact):
        try:
            e_i = float(row['E_i'])
            if abs(e_i - ei_list[i]) > tol['E_i']['abs']:
                all_ok = False
                break
            w_i = float(row['W_i'])
            psi = float(row['Psi'])
            d_val = float(row['D'])
            beta_d_val = float(row['beta_d'])
            beta_int_val = float(row['beta_int'])

            w_i_exp, psi_exp, d_exp, bd_exp, bi_exp = expected[i]

            # W_i: relative tolerance, but handle zero
            if abs(w_i_exp) < 1e-12:
                if abs(w_i - w_i_exp) > 1e-12:
                    all_ok = False
                    break
            else:
                if abs((w_i - w_i_exp) / w_i_exp) > tol['W_i']['rel']:
                    all_ok = False
                    break

            # Psi: relative tolerance
            if abs(psi_exp) < 1e-12:
                if abs(psi - psi_exp) > 1e-12:
                    all_ok = False
                    break
            else:
                if abs((psi - psi_exp) / psi_exp) > tol['Psi']['rel']:
                    all_ok = False
                    break

            # D: relative tolerance
            if abs(d_exp) < 1e-12:
                if abs(d_val - d_exp) > 1e-12:
                    all_ok = False
                    break
            else:
                if abs((d_val - d_exp) / d_exp) > tol['D']['rel']:
                    all_ok = False
                    break

            # beta_d: absolute tolerance
            if abs(beta_d_val - bd_exp) > tol['beta_d']['abs']:
                all_ok = False
                break

            # beta_int: absolute tolerance
            if abs(beta_int_val - bi_exp) > tol['beta_int']['abs']:
                all_ok = False
                break

        except (KeyError, ValueError):
            all_ok = False
            break

    return 1.0 if all_ok else 0.0


_SCORERS = {
    'step_01_energetics': score_0,
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
