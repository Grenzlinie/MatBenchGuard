import os
import json
import csv

# === author imports / helpers ===
import json, os, math, csv, sys
from collections import defaultdict
from itertools import permutations


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
    ctx = {}
    for step in spec.get("steps", []):
        ctx[step["id"]] = step
    return ctx


# === block: score_0 (check id='step_02') ===
def score_0(artifact, step, ctx):
    gold = step.get("hidden_gold", {})
    tols = step.get("tolerances", {})
    correct = 0
    total = 0
    for phase in ["ZB", "RS"]:
        if phase not in artifact:
            continue
        phase_data = artifact[phase]
        gold_phase = gold.get(phase, {})
        for field in ["a_Angstrom", "B0_GPa", "B0_prime"]:
            total += 1
            val = phase_data.get(field)
            gval = gold_phase.get(field)
            tol = tols.get(field, 0)
            if val is not None and gval is not None and abs(val - gval) <= tol:
                correct += 1
    return correct / total if total > 0 else 0.0


# === block: score_1 (check id='step_03') ===
def score_1(artifact, step, ctx):
    gold = step.get("hidden_gold", {})
    tols = step.get("tolerances", {})
    keys = [
        "transition_pressure_common_tangent_GPa",
        "transition_pressure_enthalpy_GPa",
        "volume_reduction_percent",
        "Vt_over_V0_ZB",
        "Vt_over_V0_RS",
        "V0_ZB_Bohr3"
    ]
    correct = 0
    total = len(keys)
    for key in keys:
        if key in artifact and key in gold:
            val = artifact[key]
            gval = gold[key]
            tol = tols.get(key, 0.0)
            if abs(val - gval) <= tol:
                correct += 1
    return correct / total


# === block: score_2 (check id='step_05') ===
def score_2(artifact, step, ctx):
    gold = step.get("hidden_gold", {})
    tols = step.get("tolerances", {})
    t_c11 = tols.get("C11_GPa", 20.0)
    t_c12 = tols.get("C12_GPa", 15.0)
    t_c44 = tols.get("C44_GPa", 20.0)

    static_correct = 0
    static_total = 0
    for keyword, gconst in [("ZB_at_0GPa", gold.get("ZB_at_0GPa")), ("RS_at_0GPa", gold.get("RS_at_0GPa"))]:
        if keyword not in artifact:
            continue
        art_const = artifact[keyword]
        for field, tol in [("C11_GPa", t_c11), ("C12_GPa", t_c12), ("C44_GPa", t_c44)]:
            static_total += 1
            v = art_const.get(field)
            gv = gconst.get(field) if gconst else None
            if v is not None and gv is not None and abs(v - gv) <= tol:
                static_correct += 1

    static_score = static_correct / static_total if static_total > 0 else 0.0

    pressure_data = artifact.get("ZB_pressure_dependence")
    if not isinstance(pressure_data, list):
        pressure_score = 0.0
    else:
        ref_points = gold.get("pressure_dependence", [])
        if not ref_points:
            pressure_score = 0.0
        else:
            correct_count = 0
            for rp in ref_points:
                p_ref = rp["pressure_GPa"]
                found = None
                for entry in pressure_data:
                    if abs(entry.get("pressure_GPa", 0) - p_ref) <= 0.5:
                        found = entry
                        break
                if found:
                    ok = True
                    for field in ["C11_GPa", "C12_GPa", "C44_GPa"]:
                        v = found.get(field)
                        gv = rp[field]
                        tol = tols.get(field, 20.0)
                        if v is None or abs(v - gv) > tol:
                            ok = False
                            break
                    if ok:
                        correct_count += 1
            pressure_score = correct_count / len(ref_points)

    return 0.6 * static_score + 0.4 * pressure_score


# === block: score_3 (check id='step_06') ===
def score_3(artifact, step, ctx):
    gold = step.get("hidden_gold", {})
    tols = step.get("tolerances", {})
    checks = [
        ("pressure_unstable_GPa", gold.get("pressure_unstable_GPa"), tols.get("pressure_unstable_GPa", 5.0)),
    ]
    fit_gold = gold.get("Delta_C11_12_fit", {})
    art_fit = artifact.get("Delta_C11_12_fit", {})
    for key in ["intercept", "linear_coeff", "quadratic_coeff"]:
        checks.append((key, fit_gold.get(key), tols.get(key, 0.0)))
    correct = 0
    total = len(checks)
    for key, gv, tol in checks:
        av = artifact.get(key) if key == "pressure_unstable_GPa" else art_fit.get(key) if art_fit else None
        if av is not None and gv is not None and abs(av - gv) <= tol:
            correct += 1
    return correct / total if total > 0 else 0.0


# === block: score_4 (check id='step_08') ===
def score_4(artifact, step, ctx):
    gold = step.get("hidden_gold", {})
    ref_points = gold.get("reference_points", [])
    if not ref_points:
        return 0.0
    tol_V = step.get("tolerance_V_over_V0", 0.03)

    try:
        rows = artifact  # list of dicts from csv.DictReader
    except:
        return 0.0

    by_temp = defaultdict(list)
    for row in rows:
        try:
            T = float(row.get("temperature_K"))
            P = float(row.get("pressure_GPa"))
            V = float(row.get("V_over_V0"))
            by_temp[T].append((P, V))
        except:
            continue

    # organise references into (T, (pressure, zb_v, rs_v))
    ref_by_temp = {}
    for rp in ref_points:
        T = rp["temperature_K"]
        P = rp["pressure_GPa"]
        phase = rp["phase"]
        v = rp["V_over_V0"]
        ref_by_temp.setdefault(T, {}).setdefault(P, {})[phase] = v

    total_pairs = 0
    correct_pairs = 0
    for T, pres_dict in ref_by_temp.items():
        agent_pts = by_temp.get(T, [])
        if not agent_pts:
            continue
        for P, phase_vals in pres_dict.items():
            if "ZB" not in phase_vals or "RS" not in phase_vals:
                continue
            v_zb = phase_vals["ZB"]
            v_rs = phase_vals["RS"]
            # collect agent V values within pressure window
            tol_P = 0.5
            candidate_vals = [v for (ap, v) in agent_pts if abs(ap - P) <= tol_P]
            if len(candidate_vals) < 2:
                total_pairs += 1
                continue
            best_ok = False
            for perm in permutations(candidate_vals, 2):
                err1 = abs(perm[0] - v_zb)
                err2 = abs(perm[1] - v_rs)
                if err1 <= tol_V and err2 <= tol_V:
                    best_ok = True
                    break
            if best_ok:
                correct_pairs += 1
            total_pairs += 1

    return correct_pairs / total_pairs if total_pairs > 0 else 0.0


_SCORERS = {
    'step_02': score_0,
    'step_03': score_1,
    'step_05': score_2,
    'step_06': score_3,
    'step_08': score_4,
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
