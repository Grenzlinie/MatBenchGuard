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
    ref = None
    for step in spec["steps"]:
        if step.get("id") == "step4":
            ref = step["reference"]
            break
    return {"ref": ref}


# === block: score_0 (check id='step4') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not isinstance(artifact, list) or len(artifact) < 2:
            return 0.0
        try:
            required = ["current_A", "voltage_nonuniform_V", "voltage_uniform_V", "power_nonuniform_W", "power_uniform_W"]
            for col in required:
                if col not in artifact[0]:
                    return 0.0
            ref = ctx["ref"]
            Voc = ref["Voc"]
            R = ref["R_int"]
            Pmax_target = ref["Pmax_target"]
            tol_rel = 0.10
            tol_cons = 0.03
            tol_pmax = 0.15

            points = []
            for row in artifact:
                try:
                    I = float(row["current_A"])
                    V_nu = float(row["voltage_nonuniform_V"])
                    V_u = float(row["voltage_uniform_V"])
                    P_nu = float(row["power_nonuniform_W"])
                    P_u = float(row["power_uniform_W"])
                    points.append((I, V_nu, V_u, P_nu, P_u))
                except (ValueError, KeyError):
                    continue
            if len(points) < 2:
                return 0.0

            max_rel_volt_err = 0.0
            max_rel_pow_err = 0.0
            max_cons_volt_diff = 0.0
            max_cons_pow_diff = 0.0
            pmax_nu = -1.0
            for I, Vnu, Vu, Pnu, Pu in points:
                if I == 0:
                    continue
                Vref = Voc - I * R
                if abs(Vref) > 1e-12:
                    err_v_nu = abs(Vnu - Vref) / abs(Vref)
                    err_v_u  = abs(Vu  - Vref) / abs(Vref)
                    err_v = max(err_v_nu, err_v_u)
                    if err_v > max_rel_volt_err:
                        max_rel_volt_err = err_v
                Pref = Vref * I if abs(Vref) > 1e-12 else 0.0
                if abs(Pref) > 1e-12:
                    err_p_nu = abs(Pnu - Pref) / abs(Pref)
                    err_p_u  = abs(Pu  - Pref) / abs(Pref)
                    err_p = max(err_p_nu, err_p_u)
                    if err_p > max_rel_pow_err:
                        max_rel_pow_err = err_p
                avg_v = (Vnu + Vu) / 2.0
                if abs(avg_v) > 1e-12:
                    diff_v = abs(Vnu - Vu) / abs(avg_v)
                    if diff_v > max_cons_volt_diff:
                        max_cons_volt_diff = diff_v
                avg_p = (Pnu + Pu) / 2.0
                if abs(avg_p) > 1e-12:
                    diff_p = abs(Pnu - Pu) / abs(avg_p)
                    if diff_p > max_cons_pow_diff:
                        max_cons_pow_diff = diff_p
                if Pnu > pmax_nu:
                    pmax_nu = Pnu
            max_rel_err = max(max_rel_volt_err, max_rel_pow_err)
            ref_score = 1.0 if max_rel_err <= tol_rel else max(0.0, 1.0 - (max_rel_err - tol_rel) / (0.5 - tol_rel))
            cons_v = 1.0 if max_cons_volt_diff <= tol_cons else max(0.0, 1.0 - (max_cons_volt_diff - tol_cons) / 0.1)
            cons_p = 1.0 if max_cons_pow_diff <= tol_cons else max(0.0, 1.0 - (max_cons_pow_diff - tol_cons) / 0.1)
            cons_score = min(cons_v, cons_p)
            if pmax_nu < 0:
                pmax_score = 0.0
            else:
                ratio = pmax_nu / Pmax_target
                if 1.0 - tol_pmax <= ratio <= 1.0 + tol_pmax:
                    pmax_score = 1.0
                else:
                    pmax_score = 0.0
            final = 0.4 * ref_score + 0.3 * cons_score + 0.3 * pmax_score
            return max(0.0, min(1.0, final))
        except Exception:
            return 0.0


_SCORERS = {
    'step4': score_0,
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
