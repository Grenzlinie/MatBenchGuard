import os
import json
import csv

# === author imports / helpers ===
import csv, io, json, math, os


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
    cao2_set = {name.lower() for name in ["C2/c-I","C2/c-II","Pna2_1","I4/mcm","P2_1/c-L","P2_1/c-H","I4/mmm","Pa-3","Cmmm"]}
    cao_set = {"rocksalt","cscl"}
    o2_set = {"δ-o₂","delta-o2","cmcm","c2/m"}
    ctx = {"cao2_set":cao2_set, "cao_set":cao_set, "o2_set":o2_set}
    return ctx


# === block: score_0 (check id='static_decomp_enthalpy_65GPa') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    data = {}
    for r in rows:
        try:
            p = float(r["pressure(GPa)"])
            phase = r["phase"].strip().lower()
            h = float(r["enthalpy(eV/f.u.)"])
            if p not in data:
                data[p] = {}
            data[p][phase] = h
        except:
            continue
    target_p = 65.0
    found_p = None
    for p in sorted(data.keys()):
        if abs(p-target_p) < 0.5:
            found_p = p
            break
    if found_p is None:
        return 0.0
    d = data[found_p]
    cao2_set = ctx["cao2_set"]
    cao_set = ctx["cao_set"]
    o2_set = ctx["o2_set"]
    h_cao2 = min(h for ph,h in d.items() if ph in cao2_set)
    h_cao = min(h for ph,h in d.items() if ph in cao_set)
    h_o2 = min(h for ph,h in d.items() if ph in o2_set)
    delta_H = h_cao2 - (h_cao + 0.5*h_o2)
    target = float(step["target"])
    tol = float(step["tolerance_abs"])
    diff = abs(delta_H - target)
    if diff <= tol:
        return 1.0
    return max(0.0, 1.0 - (diff-tol)/tol)


# === block: score_1 (check id='static_phase_transitions') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    data = {}
    for r in rows:
        try:
            p = float(r["pressure(GPa)"])
            phase = r["phase"].strip().lower()
            h = float(r["enthalpy(eV/f.u.)"])
            if phase in ctx["cao2_set"]:
                if p not in data:
                    data[p] = {}
                data[p][phase] = h
        except:
            continue
    expected = step.get("expected_phases", {})
    if not expected:
        return 1.0
    score = 0.0
    count = 0
    for p_str, exp_phase in expected.items():
        try:
            p_target = float(p_str)
        except:
            continue
        best_p = None
        for p in data.keys():
            if abs(p - p_target) < 0.2:
                best_p = p
                break
        if best_p is None:
            continue
        phases = data[best_p]
        if not phases:
            continue
        lowest = min(phases, key=lambda ph: phases[ph])
        if lowest == exp_phase.lower():
            score += 1.0
        count += 1
    if count == 0:
        return 0.0
    return score / count


# === block: score_2 (check id='static_deltaH_positivity') ===
def score_2(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    data = {}
    for r in rows:
        try:
            p = float(r["pressure(GPa)"])
            phase = r["phase"].strip().lower()
            h = float(r["enthalpy(eV/f.u.)"])
            if p not in data:
                data[p] = {}
            data[p][phase] = h
        except:
            continue
    cao2_set = ctx["cao2_set"]
    cao_set = ctx["cao_set"]
    o2_set = ctx["o2_set"]
    positive = 0
    total = 0
    for p, phases in data.items():
        if not any(ph in cao_set for ph in phases) or not any(ph in o2_set for ph in phases):
            continue
        if not any(ph in cao2_set for ph in phases):
            continue
        h_cao2 = min(h for ph,h in phases.items() if ph in cao2_set)
        h_cao = min(h for ph,h in phases.items() if ph in cao_set)
        h_o2 = min(h for ph,h in phases.items() if ph in o2_set)
        delta = h_cao2 - (h_cao + 0.5*h_o2)
        total += 1
        if delta > 0:
            positive += 1
    if total == 0:
        return 0.0
    return positive / total


# === block: score_3 (check id='gibbs_decomp_65GPa_2500K') ===
def score_3(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    data = {}
    for r in rows:
        try:
            p = float(r["pressure(GPa)"])
            T = float(r["temperature(K)"])
            phase = r["phase"].strip().lower()
            G = float(r["gibbs_free_energy(eV/f.u.)"])
            key = (p, T)
            if key not in data:
                data[key] = {}
            data[key][phase] = G
        except:
            continue
    target_p = 65.0
    target_T = 2500.0
    target_key = None
    for (p,T), phases in data.items():
        if abs(p-target_p) < 0.5 and abs(T-target_T) < 10:
            target_key = (p,T)
            break
    if target_key is None:
        return 0.0
    phases_at = data[target_key]
    cao2_set = ctx["cao2_set"]
    cao_set = ctx["cao_set"]
    o2_set = ctx["o2_set"]
    h_cao2 = min(G for ph,G in phases_at.items() if ph in cao2_set)
    h_cao = min(G for ph,G in phases_at.items() if ph in cao_set)
    h_o2 = min(G for ph,G in phases_at.items() if ph in o2_set)
    delta_G = h_cao2 - (h_cao + 0.5*h_o2)
    target = float(step["target"])
    tol = float(step["tolerance_abs"])
    diff = abs(delta_G - target)
    if diff <= tol:
        return 1.0
    return max(0.0, 1.0 - (diff-tol)/tol)


# === block: score_4 (check id='gibbs_deltaG_positivity') ===
def score_4(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    data = {}
    for r in rows:
        try:
            p = float(r["pressure(GPa)"])
            T = float(r["temperature(K)"])
            phase = r["phase"].strip().lower()
            G = float(r["gibbs_free_energy(eV/f.u.)"])
            key = (p,T)
            if key not in data:
                data[key] = {}
            data[key][phase] = G
        except:
            continue
    target_p = 65.0
    target_T = 2500.0
    for (p,T), phases in data.items():
        if abs(p-target_p) < 0.5 and abs(T-target_T) < 10:
            phases_at = phases
            cao2_set = ctx["cao2_set"]
            cao_set = ctx["cao_set"]
            o2_set = ctx["o2_set"]
            h_cao2 = min(G for ph,G in phases_at.items() if ph in cao2_set)
            h_cao = min(G for ph,G in phases_at.items() if ph in cao_set)
            h_o2 = min(G for ph,G in phases_at.items() if ph in o2_set)
            delta_G = h_cao2 - (h_cao + 0.5*h_o2)
            return 1.0 if delta_G > 0 else 0.0
    return 0.0


# === block: score_5 (check id='bandgap_values') ===
def score_5(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    thermal = float(artifact.get("thermal_bandgap_eV", 0))
    optical = float(artifact.get("optical_bandgap_eV", 0))
    target_thermal = float(step["target_thermal"])
    target_optical = float(step["target_optical"])
    tol = float(step["tolerance"])
    def score_val(val, target):
        diff = abs(val - target)
        if diff <= tol:
            return 1.0
        return max(0.0, 1.0 - (diff - tol) / tol)
    return (score_val(thermal, target_thermal) + score_val(optical, target_optical)) / 2.0


_SCORERS = {
    'static_decomp_enthalpy_65GPa': score_0,
    'static_phase_transitions': score_1,
    'static_deltaH_positivity': score_2,
    'gibbs_decomp_65GPa_2500K': score_3,
    'gibbs_deltaG_positivity': score_4,
    'bandgap_values': score_5,
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
