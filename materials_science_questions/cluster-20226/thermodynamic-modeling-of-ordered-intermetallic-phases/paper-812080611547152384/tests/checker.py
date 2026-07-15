import os
import json
import csv

# === author imports / helpers ===
import math, os, csv


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
    import os, json
    fitted = None
    fp = os.path.join(outputs_dir, "fitted_parameters.json")
    if os.path.exists(fp):
        with open(fp) as f:
            fitted = json.load(f)
    return {"fitted": fitted}


# === block: score_0 (check id='fit_params') ===
def score_0(artifact, step, ctx):
    import math
    if not isinstance(artifact, dict):
        return 0.0
    gold = step.get("gold", {})
    tol_a = gold.get("tolerance_alpha", 1e-5)
    tol_e = gold.get("tolerance_eta", 0.1)
    tol_l = gold.get("tolerance_ln_a", 0.1)
    a_ok = 0
    eta_ok = 0
    ln_ok = 0
    if "alpha" in artifact:
        try:
            if abs(float(artifact["alpha"]) - gold["alpha"]) <= tol_a:
                a_ok = 1
        except:
            pass
    if "eta" in artifact:
        try:
            if abs(float(artifact["eta"]) - gold["eta"]) <= tol_e:
                eta_ok = 1
        except:
            pass
    if "ln_a_Zn_0" in artifact:
        try:
            if abs(float(artifact["ln_a_Zn_0"]) - gold["ln_a_Zn_0"]) <= tol_l:
                ln_ok = 1
        except:
            pass
    score = (a_ok + eta_ok + ln_ok) / 3.0
    return score


# === block: score_1 (check id='thermo_table') ===
def score_1(artifact, step, ctx):
    import math, csv
    if not isinstance(artifact, list) or not artifact:
        return 0.0
    gold_table = step.get("gold_table", [])
    tols = step.get("tolerances", {})
    cons = step.get("consistency", {})
    # Map agent rows by composition
    row_map = {}
    for r in artifact:
        try:
            comp = float(r["a/o_Zn"])
            row_map[comp] = r
        except:
            pass
    # Value check
    count = 0
    correct = 0
    for gt in gold_table:
        comp = gt["a/o_Zn"]
        r = row_map.get(comp)
        if r is None:
            continue
        for fname in ["ln_a_Zn", "ln_a_Pt", "Delta_G_kJ_per_g_atom", "Delta_H_kJ_per_g_atom", "T_Delta_S_kJ_per_g_atom"]:
            tv = tols.get(fname, 1e9)
            if fname in r and fname in gt:
                try:
                    v = float(r[fname])
                    if abs(v - gt[fname]) <= tv:
                        correct += 1
                except:
                    pass
            count += 1
    value_score = 0.0
    if count > 0:
        value_score = correct / count
    # Consistency check
    cons_score = 0.0
    fitted = ctx.get("fitted")
    if fitted and 50.0 in row_map:
        r50 = row_map[50.0]
        # ΔG at stoichiometry
        dg_exp = cons.get("DG_stoich_expected", -49.2)
        dg_tol = cons.get("DG_tolerance", 2.0)
        if "Delta_G_kJ_per_g_atom" in r50:
            try:
                if abs(float(r50["Delta_G_kJ_per_g_atom"]) - dg_exp) <= dg_tol:
                    cons_score += 0.5
            except:
                pass
        # ln_a_Zn vs fitted ln_a_Zn_0
        ln_tol = cons.get("ln_a_Zn_tolerance", 0.12)
        if "ln_a_Zn" in r50 and "ln_a_Zn_0" in fitted:
            try:
                if abs(float(r50["ln_a_Zn"]) - float(fitted["ln_a_Zn_0"])) <= ln_tol:
                    cons_score += 0.5
            except:
                pass
    # Combine: 70% value, 30% consistency
    return 0.7 * min(value_score, 1.0) + 0.3 * min(cons_score, 1.0)


# === block: score_2 (check id='dH_alpha') ===
def score_2(artifact, step, ctx):
    import math
    if not isinstance(artifact, list):
        return 0.0
    gold_alpha = step.get("gold_alpha", 0.0003)
    gold_DH = step.get("gold_Delta_H", -65.0)
    tol_DH = step.get("tolerance_Delta_H", 5.0)
    for r in artifact:
        if r.get("phase", "").strip().lower() == "ptzn":
            try:
                alpha = float(r["alpha"])
                DH = float(r["Delta_H_kJ_per_g_atom"])
                alpha_ok = abs(alpha - gold_alpha) <= 1e-5
                DH_ok = abs(DH - gold_DH) <= tol_DH
                if alpha_ok and DH_ok:
                    return 1.0
                elif DH_ok:
                    return 0.5
            except:
                pass
    return 0.0


_SCORERS = {
    'fit_params': score_0,
    'thermo_table': score_1,
    'dH_alpha': score_2,
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
