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
            except Exception as exc:
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
                # only check that the file is readable and header matches
                with open(path, newline="") as _f:
                    reader = _ff_csv.DictReader(_f, delimiter=delim)
                    headers = reader.fieldnames or []
                required_cols = schema.get("required_columns", [])
                for col in required_cols:
                    if col not in headers:
                        violations.append(base + ": missing column '" + col + "' in header")
            except Exception as exc:
                violations.append(base + ": CSV/TSV read error (" + str(exc) + ")")
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
        except Exception:
            return None
    if path.endswith(".csv") or path.endswith(".tsv"):
        delim = "\t" if path.endswith(".tsv") else ","
        with open(path, newline="") as f:
            return list(csv.DictReader(f, delimiter=delim))
    with open(path) as f:
        return f.read()


def prepare(outputs_dir, spec):
    return {}


# === block: score_0 (check id='step_01a') ===
def score_0(artifact, step, ctx):
    # Hard-coded reference and tolerances for [Fe(phen)2(NCS)2] transition quantities
    ref = {"Tc_K": 176.29, "Delta_H_kJ_mol": 8.6, "Delta_S_J_K_mol": 48.78}
    tol = {"Tc_K": 0.02, "Delta_H_kJ_mol": 0.14, "Delta_S_J_K_mol": 0.71}
    artifact = artifact if isinstance(artifact, dict) else {}
    fields = [("Tc_K", "Tc_K"), ("Delta_H_kJ_mol", "Delta_H_kJ_mol"), ("Delta_S_J_K_mol", "Delta_S_J_K_mol")]
    scores = []
    for field_key, tol_key in fields:
        if field_key not in artifact:
            scores.append(0.0)
            continue
        val = artifact[field_key]
        r = ref.get(field_key)
        t = tol.get(tol_key, 0.0)
        if not isinstance(r, (int, float)) or t <= 0:
            scores.append(1.0 if abs(val - r) < 1e-9 else 0.0)
            continue
        err = abs(val - r)
        if err <= t:
            scores.append(1.0)
        else:
            # linear decay to zero at 3*tol
            s = max(0.0, 1.0 - (err - t) / (2.0 * t))
            scores.append(s)
    return sum(scores) / max(len(scores), 1)


# === block: score_1 (check id='step_01b') ===
def score_1(artifact, step, ctx):
    # Hard-coded reference and tolerances for [Fe(phen)2(NCSe)2] transition quantities
    ref = {"Tc_K": 231.26, "Delta_H_kJ_mol": 11.6, "Delta_S_J_K_mol": 51.22}
    tol = {"Tc_K": 0.02, "Delta_H_kJ_mol": 0.44, "Delta_S_J_K_mol": 2.33}
    artifact = artifact if isinstance(artifact, dict) else {}
    fields = [("Tc_K", "Tc_K"), ("Delta_H_kJ_mol", "Delta_H_kJ_mol"), ("Delta_S_J_K_mol", "Delta_S_J_K_mol")]
    scores = []
    for field_key, tol_key in fields:
        if field_key not in artifact:
            scores.append(0.0)
            continue
        val = artifact[field_key]
        r = ref.get(field_key)
        t = tol.get(tol_key, 0.0)
        if not isinstance(r, (int, float)) or t <= 0:
            scores.append(1.0 if abs(val - r) < 1e-9 else 0.0)
            continue
        err = abs(val - r)
        if err <= t:
            scores.append(1.0)
        else:
            s = max(0.0, 1.0 - (err - t) / (2.0 * t))
            scores.append(s)
    return sum(scores) / max(len(scores), 1)


# === block: score_2 (check id='step_02a') ===
def score_2(artifact, step, ctx):
    # Hard-coded reference and tolerances for NCS model parameters
    ref = {"N_mol-1": 6.34e21, "n": 95}
    tol = {"N_mol-1": 0.1, "n": 5}   # N: relative, n: absolute
    artifact = artifact if isinstance(artifact, dict) else {}
    def field_score(key, t_val, rel=False):
        if key not in artifact:
            return 0.0
        val = artifact[key]
        r = ref.get(key)
        if r is None:
            return 0.0
        if rel:
            if r == 0:
                return 1.0 if abs(val) < 1e-9 else 0.0
            err_ratio = abs(val - r) / abs(r)
            if err_ratio <= t_val:
                return 1.0
            else:
                return max(0.0, 1.0 - (err_ratio - t_val) / (2.0 * t_val))
        else:
            err = abs(val - r)
            if err <= t_val:
                return 1.0
            else:
                return max(0.0, 1.0 - (err - t_val) / (2.0 * t_val))
    s1 = field_score("N_mol-1", tol["N_mol-1"], rel=True)
    s2 = field_score("n", tol["n"], rel=False)
    return 0.5 * s1 + 0.5 * s2


# === block: score_3 (check id='step_02b') ===
def score_3(artifact, step, ctx):
    # Hard-coded reference and tolerances for NCSe model parameters
    ref = {"N_mol-1": 7.83e21, "n": 77}
    tol = {"N_mol-1": 0.1, "n": 5}
    artifact = artifact if isinstance(artifact, dict) else {}
    def field_score(key, t_val, rel=False):
        if key not in artifact:
            return 0.0
        val = artifact[key]
        r = ref.get(key)
        if r is None:
            return 0.0
        if rel:
            if r == 0:
                return 1.0 if abs(val) < 1e-9 else 0.0
            err_ratio = abs(val - r) / abs(r)
            if err_ratio <= t_val:
                return 1.0
            else:
                return max(0.0, 1.0 - (err_ratio - t_val) / (2.0 * t_val))
        else:
            err = abs(val - r)
            if err <= t_val:
                return 1.0
            else:
                return max(0.0, 1.0 - (err - t_val) / (2.0 * t_val))
    s1 = field_score("N_mol-1", tol["N_mol-1"], rel=True)
    s2 = field_score("n", tol["n"], rel=False)
    return 0.5 * s1 + 0.5 * s2


# === block: score_4 (check id='step_03a') ===
def score_4(artifact, step, ctx):
    # Hard-coded reference for NCS model Cp curve
    ref_Tc = 176.29
    ref_Cp_max = 7164.7
    tol_Cp_frac = 0.10
    tol_Tc_abs = 1.0
    rows = artifact if isinstance(artifact, list) else []
    cp_vals = []
    T_vals = []
    for row in rows:
        if row is None:
            continue
        try:
            T = float(row.get("T(K)", row.get("T", None)))
            Cp = float(row.get("Cp_model(J/K/mol)", row.get("Cp", None)))
            cp_vals.append(Cp)
            T_vals.append(T)
        except (ValueError, TypeError):
            continue
    if not cp_vals:
        return 0.0
    max_idx = cp_vals.index(max(cp_vals))
    max_Cp = cp_vals[max_idx]
    max_T = T_vals[max_idx]
    if ref_Cp_max <= 0:
        score_Cp = 1.0 if max_Cp <= 1e-6 else 0.0
    else:
        rel_err = abs(max_Cp - ref_Cp_max) / ref_Cp_max
        if rel_err <= tol_Cp_frac:
            score_Cp = 1.0
        else:
            score_Cp = max(0.0, 1.0 - (rel_err - tol_Cp_frac) / (2.0 * tol_Cp_frac))
    if tol_Tc_abs <= 0:
        score_Tc = 1.0 if abs(max_T - ref_Tc) < 1e-9 else 0.0
    else:
        err_Tc = abs(max_T - ref_Tc)
        if err_Tc <= tol_Tc_abs:
            score_Tc = 1.0
        else:
            score_Tc = max(0.0, 1.0 - (err_Tc - tol_Tc_abs) / (2.0 * tol_Tc_abs))
    return 0.7 * score_Cp + 0.3 * score_Tc


# === block: score_5 (check id='step_03b') ===
def score_5(artifact, step, ctx):
    # Hard-coded reference for NCSe model Cp curve
    ref_Tc = 231.26
    ref_Cp_max = 8010.9
    tol_Cp_frac = 0.10
    tol_Tc_abs = 1.0
    rows = artifact if isinstance(artifact, list) else []
    cp_vals = []
    T_vals = []
    for row in rows:
        if row is None:
            continue
        try:
            T = float(row.get("T(K)", row.get("T", None)))
            Cp = float(row.get("Cp_model(J/K/mol)", row.get("Cp", None)))
            cp_vals.append(Cp)
            T_vals.append(T)
        except (ValueError, TypeError):
            continue
    if not cp_vals:
        return 0.0
    max_idx = cp_vals.index(max(cp_vals))
    max_Cp = cp_vals[max_idx]
    max_T = T_vals[max_idx]
    if ref_Cp_max <= 0:
        score_Cp = 1.0 if max_Cp <= 1e-6 else 0.0
    else:
        rel_err = abs(max_Cp - ref_Cp_max) / ref_Cp_max
        if rel_err <= tol_Cp_frac:
            score_Cp = 1.0
        else:
            score_Cp = max(0.0, 1.0 - (rel_err - tol_Cp_frac) / (2.0 * tol_Cp_frac))
    if tol_Tc_abs <= 0:
        score_Tc = 1.0 if abs(max_T - ref_Tc) < 1e-9 else 0.0
    else:
        err_Tc = abs(max_T - ref_Tc)
        if err_Tc <= tol_Tc_abs:
            score_Tc = 1.0
        else:
            score_Tc = max(0.0, 1.0 - (err_Tc - tol_Tc_abs) / (2.0 * tol_Tc_abs))
    return 0.7 * score_Cp + 0.3 * score_Tc


_SCORERS = {
    "step_01a": score_0,
    "step_01b": score_1,
    "step_02a": score_2,
    "step_02b": score_3,
    "step_03a": score_4,
    "step_03b": score_5,
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
            except Exception as exc:
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