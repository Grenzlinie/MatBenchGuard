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


# === block: score_0 (check id='qm_mm_results') ===
def score_0(artifact, step, ctx):
    # Read agent artifact (already loaded as list of dicts)
    step = step  # from grading_spec
    probes_ref = step["probes"]
    clean_ref = {"v_st": step["clean_v_ref_st"], "v_el": step["clean_v_ref_el"], "v_ch": step["clean_v_ref_ch"]}
    tol_freq_rel = step["tolerances"]["frequency_rel"]
    tol_freq_abs_min = step["tolerances"]["frequency_abs_min"]
    tol_enthalpy_abs = step["tolerances"]["enthalpy_abs"]
    struct_eps = step["tolerances"]["structural_epsilon"]

    # 1. Basic shape
    if not isinstance(artifact, list) or len(artifact) != 8:
        return 0.0
    clean_agent = None
    probe_map = {}
    for entry in artifact:
        if entry.get("probe") == "clean":
            clean_agent = entry
        else:
            probe_map[entry["probe"]] = entry
    if clean_agent is None:
        return 0.0
    expected_names = set(p["name"] for p in probes_ref)
    if set(probe_map.keys()) != expected_names:
        return 0.0

    required_fields = ["v_st", "v_el", "v_ch", "delta_v_st", "delta_v_el", "delta_v_ch",
                       "delta_H_st", "delta_H_el", "delta_H_ch"]
    for e in [clean_agent] + list(probe_map.values()):
        for f in required_fields:
            if f not in e or not isinstance(e[f], (int, float)):
                return 0.0

    # 2. Self-consistency (delta_v = clean_v - v) within 10 cm^-1
    consistency_ok = True
    for trt in ["st", "el", "ch"]:
        cv = clean_agent["v_" + trt]
        for name, ae in probe_map.items():
            expected = cv - ae["v_" + trt]
            if abs(expected - ae["delta_v_" + trt]) > 10:
                consistency_ok = False
                break
        if not consistency_ok:
            break
    shape_score = 1.0 if consistency_ok else 0.0

    # 3. Numeric accuracy (frequencies and enthalpies)
    v_scores = []
    dh_scores = []
    for p in probes_ref:
        name = p["name"]
        ae = probe_map[name]
        for trt in ["st", "el", "ch"]:
            v_agent = ae["v_" + trt]
            v_ref = p["v_" + trt]
            # frequency: accept if within tolerance
            abs_tol = max(tol_freq_abs_min, tol_freq_rel * abs(v_ref))
            if abs(v_agent - v_ref) <= abs_tol:
                v_scores.append(1.0)
            else:
                v_scores.append(0.0)
            # enthalpy
            if abs(ae["delta_H_" + trt] - p["delta_H_" + trt]) <= tol_enthalpy_abs:
                dh_scores.append(1.0)
            else:
                dh_scores.append(0.0)
    v_score = sum(v_scores) / len(v_scores) if v_scores else 0.0
    dh_score = sum(dh_scores) / len(dh_scores) if dh_scores else 0.0

    # 4. Structural ordering (core claim)
    struct_score = 0.0
    n_checks = 0
    for p in probes_ref:
        name = p["name"]
        ae = probe_map[name]
        # experimental reference midpoint
        if "v_exp_range" in p:
            v_exp = (p["v_exp_range"][0] + p["v_exp_range"][1]) / 2.0
        else:
            v_exp = p["v_exp"]
        v_st = ae["v_st"]
        v_el = ae["v_el"]
        v_ch = ae["v_ch"]
        d_st = abs(v_st - v_exp)
        d_el = abs(v_el - v_exp)
        d_ch = abs(v_ch - v_exp)

        # strong vs weak regime (based on paper ΔH_st)
        dH_st_ref = p["delta_H_st"]
        if dH_st_ref >= 9:
            n_checks += 1
            if d_st <= d_el + struct_eps:
                struct_score += 1.0
        elif dH_st_ref <= 6:
            n_checks += 1
            if d_el <= d_st + struct_eps:
                struct_score += 1.0
        # all probes: ch is best
        n_checks += 1
        if d_ch <= min(d_st, d_el) + struct_eps:
            struct_score += 1.0

    struct_score = struct_score / n_checks if n_checks > 0 else 1.0

    # 5. Composite score
    score = 0.1 * shape_score + 0.3 * (0.5 * v_score + 0.5 * dh_score) + 0.6 * struct_score
    return max(0.0, min(1.0, round(score, 6)))


_SCORERS = {
    'qm_mm_results': score_0,
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
