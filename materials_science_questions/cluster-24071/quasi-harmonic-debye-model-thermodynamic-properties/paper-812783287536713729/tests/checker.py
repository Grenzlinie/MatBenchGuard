import os
import json
import csv

# === author imports / helpers ===
import math
import os


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
    import os
    ctx = {"output_dir": "/app/outputs"}
    gold_coeffs = {}
    for step in spec["steps"]:
        if step.get("kind") == "coefficient_match":
            gold_coeffs[step["config"]["phase_key"]] = step["config"]["gold_coefficients"]
    ctx["gold_coeffs"] = gold_coeffs
    return ctx


# === block: score_0 (check id='gamma_csv_to_cs_consistency') ===
def score_0(artifact, step, ctx):
    import json

    temps = step["config"]["temperatures"]
    props = step["config"]["properties"]
    phase = step["config"]["phase_key"]
    tol_rel = step["config"]["tolerance_rel"]
    max_rel_err = step["config"].get("max_rel_error", 0.5)

    fits_path = os.path.join(ctx["output_dir"], "analytical_fits.json")
    if not os.path.exists(fits_path):
        return 0.0
    with open(fits_path) as f:
        fits = json.load(f)
    if phase not in fits:
        return 0.0
    coeffs_all = fits[phase]

    t_to_row = {}
    for row in artifact:
        try:
            t = float(row["T"])
        except (ValueError, KeyError):
            continue
        t_to_row[t] = row

    def eval_qha(coeff, T):
        a0 = coeff["a0"]
        a1, a2, a3, a4 = coeff["a1"], coeff["a2"], coeff["a3"], coeff["a4"]
        b1, b2, b3, b4 = coeff["b1"], coeff["b2"], coeff["b3"], coeff["b4"]
        c = coeff["c"]
        val = a0 + a1*T + a2*T*T + a3*T**3 + a4*T**4
        val += b1/T + b2/(T*T) + b3/(T**3) + b4/(T**4)
        val += c * math.log(T) if T > 0 else 0.0
        return val

    scores = []
    for T in temps:
        if T not in t_to_row:
            continue
        row = t_to_row[T]
        for prop in props:
            csv_col = f"{prop}_to_cs"
            csv_val_str = row.get(csv_col)
            if csv_val_str is None:
                continue
            try:
                csv_val = float(csv_val_str)
            except ValueError:
                continue
            if prop not in coeffs_all:
                continue
            calc_val = eval_qha(coeffs_all[prop], T)
            denom = max(abs(calc_val), 1e-9)
            rel_err = abs(calc_val - csv_val) / denom
            rel_err = min(rel_err, max_rel_err)
            s = max(0.0, 1.0 - rel_err / tol_rel)
            scores.append(s)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_1 (check id='alpha2_csv_to_cs_consistency') ===
def score_1(artifact, step, ctx):
    import json

    temps = step["config"]["temperatures"]
    props = step["config"]["properties"]
    phase = step["config"]["phase_key"]
    tol_rel = step["config"]["tolerance_rel"]
    max_rel_err = step["config"].get("max_rel_error", 0.5)

    fits_path = os.path.join(ctx["output_dir"], "analytical_fits.json")
    if not os.path.exists(fits_path):
        return 0.0
    with open(fits_path) as f:
        fits = json.load(f)
    if phase not in fits:
        return 0.0
    coeffs_all = fits[phase]

    t_to_row = {}
    for row in artifact:
        try:
            t = float(row["T"])
        except (ValueError, KeyError):
            continue
        t_to_row[t] = row

    def eval_qha(coeff, T):
        a0 = coeff["a0"]
        a1, a2, a3, a4 = coeff["a1"], coeff["a2"], coeff["a3"], coeff["a4"]
        b1, b2, b3, b4 = coeff["b1"], coeff["b2"], coeff["b3"], coeff["b4"]
        c = coeff["c"]
        val = a0 + a1*T + a2*T*T + a3*T**3 + a4*T**4
        val += b1/T + b2/(T*T) + b3/(T**3) + b4/(T**4)
        val += c * math.log(T) if T > 0 else 0.0
        return val

    scores = []
    for T in temps:
        if T not in t_to_row:
            continue
        row = t_to_row[T]
        for prop in props:
            csv_col = f"{prop}_to_cs"
            csv_val_str = row.get(csv_col)
            if csv_val_str is None:
                continue
            try:
                csv_val = float(csv_val_str)
            except ValueError:
                continue
            if prop not in coeffs_all:
                continue
            calc_val = eval_qha(coeffs_all[prop], T)
            denom = max(abs(calc_val), 1e-9)
            rel_err = abs(calc_val - csv_val) / denom
            rel_err = min(rel_err, max_rel_err)
            s = max(0.0, 1.0 - rel_err / tol_rel)
            scores.append(s)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_2 (check id='gamma_fits_accuracy') ===
def score_2(artifact, step, ctx):
    phase = step["config"]["phase_key"]
    gold_coeffs = step["config"]["gold_coefficients"]
    tol_rel = 0.30  # increased tolerance to accommodate different DFT codes
    temperatures = [100, 300, 500, 700, 900]

    agent_phase = artifact.get(phase)
    if not isinstance(agent_phase, dict):
        return 0.0

    def eval_qha(coeff, T):
        a0 = coeff["a0"]
        a1, a2, a3, a4 = coeff["a1"], coeff["a2"], coeff["a3"], coeff["a4"]
        b1, b2, b3, b4 = coeff["b1"], coeff["b2"], coeff["b3"], coeff["b4"]
        c = coeff["c"]
        val = a0 + a1*T + a2*T*T + a3*T**3 + a4*T**4
        val += b1/T + b2/(T*T) + b3/(T**3) + b4/(T**4)
        val += c * math.log(T) if T > 0 else 0.0
        return val

    scores = []
    for prop, gold_coeff in gold_coeffs.items():
        agent_coeff = agent_phase.get(prop)
        if not isinstance(agent_coeff, dict):
            scores.extend([0.0] * len(temperatures))
            continue
        try:
            for T in temperatures:
                gold_val = eval_qha(gold_coeff, T)
                agent_val = eval_qha(agent_coeff, T)
                denom = max(abs(gold_val), 1e-9)
                rel_err = min(abs(agent_val - gold_val) / denom, 1.0)
                s = max(0.0, 1.0 - rel_err / tol_rel)
                scores.append(s)
        except Exception:
            scores.extend([0.0] * len(temperatures))

    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_3 (check id='alpha2_fits_accuracy') ===
def score_3(artifact, step, ctx):
    phase = step["config"]["phase_key"]
    gold_coeffs = step["config"]["gold_coefficients"]
    tol_rel = 0.30
    temperatures = [100, 300, 500, 700, 900]

    agent_phase = artifact.get(phase)
    if not isinstance(agent_phase, dict):
        return 0.0

    def eval_qha(coeff, T):
        a0 = coeff["a0"]
        a1, a2, a3, a4 = coeff["a1"], coeff["a2"], coeff["a3"], coeff["a4"]
        b1, b2, b3, b4 = coeff["b1"], coeff["b2"], coeff["b3"], coeff["b4"]
        c = coeff["c"]
        val = a0 + a1*T + a2*T*T + a3*T**3 + a4*T**4
        val += b1/T + b2/(T*T) + b3/(T**3) + b4/(T**4)
        val += c * math.log(T) if T > 0 else 0.0
        return val

    scores = []
    for prop, gold_coeff in gold_coeffs.items():
        agent_coeff = agent_phase.get(prop)
        if not isinstance(agent_coeff, dict):
            scores.extend([0.0] * len(temperatures))
            continue
        try:
            for T in temperatures:
                gold_val = eval_qha(gold_coeff, T)
                agent_val = eval_qha(agent_coeff, T)
                denom = max(abs(gold_val), 1e-9)
                rel_err = min(abs(agent_val - gold_val) / denom, 1.0)
                s = max(0.0, 1.0 - rel_err / tol_rel)
                scores.append(s)
        except Exception:
            scores.extend([0.0] * len(temperatures))

    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_4 (check id='gs_cs_trends_gamma') ===
def score_4(artifact, step, ctx):
    checks = step["config"]["checks"]

    t_to_row = {}
    for row in artifact:
        try:
            t = float(row["T"])
        except (ValueError, KeyError):
            continue
        t_to_row[t] = row

    def _get(row, col):
        try:
            return float(row[col])
        except (ValueError, KeyError):
            return None

    scores = []
    for chk in checks:
        typ = chk["type"]
        if typ == "gt":
            col1, col2 = chk["col1"], chk["col2"]
            min_temp = chk.get("min_temp", 0)
            ok = 0
            cnt = 0
            for t, row in sorted(t_to_row.items()):
                if t < min_temp:
                    continue
                v1 = _get(row, col1)
                v2 = _get(row, col2)
                if v1 is not None and v2 is not None:
                    if v1 > v2:
                        ok += 1
                    cnt += 1
            scores.append(ok / cnt if cnt else 0.0)
        elif typ == "monotonic_increasing":
            col = chk["col"]
            vals = []
            for t in sorted(t_to_row):
                v = _get(t_to_row[t], col)
                if v is not None:
                    vals.append(v)
            if len(vals) < 2:
                scores.append(0.0)
            else:
                inc = all(vals[i] >= vals[i-1] - 1e-10 for i in range(1, len(vals)))
                scores.append(1.0 if inc else 0.0)
        elif typ == "positive":
            cols = chk["cols"]
            all_pos = True
            for row in t_to_row.values():
                for col in cols:
                    v = _get(row, col)
                    if v is not None and v <= 0:
                        all_pos = False
                        break
            scores.append(1.0 if all_pos else 0.0)
        else:
            scores.append(0.0)

    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_5 (check id='gs_cs_trends_alpha2') ===
def score_5(artifact, step, ctx):
    checks = step["config"]["checks"]

    t_to_row = {}
    for row in artifact:
        try:
            t = float(row["T"])
        except (ValueError, KeyError):
            continue
        t_to_row[t] = row

    def _get(row, col):
        try:
            return float(row[col])
        except (ValueError, KeyError):
            return None

    scores = []
    for chk in checks:
        typ = chk["type"]
        if typ == "close":
            col1, col2 = chk["col1"], chk["col2"]
            min_temp = chk.get("min_temp", 0)
            max_rel = chk.get("max_rel_diff", 0.02)
            ok = 0
            cnt = 0
            for t, row in sorted(t_to_row.items()):
                if t < min_temp:
                    continue
                v1 = _get(row, col1)
                v2 = _get(row, col2)
                if v1 is not None and v2 is not None:
                    denom = max(abs(v2), 1e-12)
                    if abs(v1 - v2) / denom <= max_rel:
                        ok += 1
                    cnt += 1
            scores.append(ok / cnt if cnt else 0.0)
        elif typ == "monotonic_increasing":
            col = chk["col"]
            vals = []
            for t in sorted(t_to_row):
                v = _get(t_to_row[t], col)
                if v is not None:
                    vals.append(v)
            if len(vals) < 2:
                scores.append(0.0)
            else:
                inc = all(vals[i] >= vals[i-1] - 1e-10 for i in range(1, len(vals)))
                scores.append(1.0 if inc else 0.0)
        elif typ == "positive":
            cols = chk["cols"]
            all_pos = True
            for row in t_to_row.values():
                for col in cols:
                    v = _get(row, col)
                    if v is not None and v <= 0:
                        all_pos = False
                        break
            scores.append(1.0 if all_pos else 0.0)
        else:
            scores.append(0.0)

    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_6 (check id='cp_dulong_petit_check') ===
def score_6(artifact, step, ctx):
    import os
    output_dir = ctx["output_dir"]
    dp = step["config"]["dulong_petit"]
    tol = step["config"]["tolerance"]
    min_temp = step["config"]["min_temp"]

    # load both CSVs
    gamma_path = os.path.join(output_dir, "gamma_TiAl_properties.csv")
    alpha2_path = os.path.join(output_dir, "alpha2_Ti3Al_properties.csv")
    if not os.path.exists(gamma_path) or not os.path.exists(alpha2_path):
        return 0.0

    gamma_csv = load_artifact(gamma_path)
    alpha2_csv = load_artifact(alpha2_path)
    if not gamma_csv or not alpha2_csv:
        return 0.0

    rows = gamma_csv + alpha2_csv

    checked = []
    for row in rows:
        try:
            t = float(row["T"])
        except (ValueError, KeyError):
            continue
        if t < min_temp:
            continue
        for col in ["Cp_gs_cs", "Cp_to_cs"]:
            val_str = row.get(col)
            if val_str is None:
                continue
            try:
                val = float(val_str)
            except ValueError:
                continue
            ok = abs(val - dp) <= tol
            checked.append(1.0 if ok else 0.0)

    if not checked:
        return 0.0
    return sum(checked) / len(checked)


# === block: score_7 (check id='alpha_anisotropy_gamma') ===
def score_7(artifact, step, ctx):
    min_temp = step["config"]["min_temp"]

    t_to_row = {}
    for row in artifact:
        try:
            t = float(row["T"])
        except (ValueError, KeyError):
            continue
        t_to_row[t] = row

    checked = 0
    passed = 0
    for t, row in sorted(t_to_row.items()):
        if t < min_temp:
            continue
        val_a = row.get("alpha_a_to_cs")
        val_c = row.get("alpha_c_to_cs")
        if val_a is None or val_c is None:
            continue
        try:
            a = float(val_a)
            c = float(val_c)
        except ValueError:
            continue
        if a > c:
            passed += 1
        checked += 1

    if checked == 0:
        return 0.0
    return passed / checked


_SCORERS = {
    'gamma_csv_to_cs_consistency': score_0,
    'alpha2_csv_to_cs_consistency': score_1,
    'gamma_fits_accuracy': score_2,
    'alpha2_fits_accuracy': score_3,
    'gs_cs_trends_gamma': score_4,
    'gs_cs_trends_alpha2': score_5,
    'cp_dulong_petit_check': score_6,
    'alpha_anisotropy_gamma': score_7,
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
