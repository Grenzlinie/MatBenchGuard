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
    import json, os
    struct_path = os.path.join(outputs_dir, "structural_properties.json")
    sanity_ok = False
    try:
        with open(struct_path) as f:
            struct = json.load(f)
        if all(k in struct for k in ["a0","C11","C12","C44","B","G","Y","V","θ_D","ν","A"]):
            if (struct["C11"] > 0 and struct["C12"] > 0 and struct["C44"] > 0 and
                struct["B"] > 0 and struct["G"] > 0 and struct["Y"] > 0 and
                struct["V"] > 0 and struct["θ_D"] > 0 and
                0 < struct.get("ν", 0) < 0.5 and struct["A"] > 0 and
                struct["C11"] > struct["C12"]):
                    sanity_ok = True
    except:
        pass
    ctx = {"sanity_ok": sanity_ok}
    for step in spec.get("steps", []):
        sid = step["id"]
        if sid == "structural_properties":
            ctx["gold_structural"] = step["gold"]
            ctx["tol_structural"] = step["tolerance"]
        elif sid == "bandgap":
            ctx["gold_bandgap"] = step["gold"]
            ctx["tol_bandgap"] = step["tolerance"]
        elif sid == "seebeck_curve":
            ctx["gold_seebeck"] = step["gold"]
        elif sid == "zt_300k":
            ctx["gold_zt"] = step["gold"]
            ctx["tol_zt"] = step["tolerance"]
    return ctx


# === block: score_0 (check id='structural_properties') ===
def score_0(artifact, step, ctx):
    if not ctx.get("sanity_ok", False): return 0.0
    artifact_dict = artifact
    gold = ctx["gold_structural"]
    tol_rel = ctx["tol_structural"]
    scores = []
    for field, gval in gold.items():
        aval = artifact_dict.get(field)
        if aval is None or not isinstance(aval, (int, float)):
            scores.append(0.0)
            continue
        rel_err = abs(aval - gval) / gval if gval != 0 else (0 if aval == 0 else 1)
        tol = tol_rel[field]
        if rel_err <= tol:
            scores.append(1.0)
        else:
            scores.append(max(0.0, 2 - rel_err / tol))
    return sum(scores) / len(scores)


# === block: score_1 (check id='bandgap') ===
def score_1(artifact, step, ctx):
    if not ctx.get("sanity_ok", False): return 0.0
    val = float(artifact.strip())
    gold = ctx["gold_bandgap"]
    tol = ctx["tol_bandgap"]
    delta = abs(val - gold)
    if delta <= tol:
        return 1.0
    else:
        return max(0.0, 1.0 - (delta - tol) / tol)


# === block: score_2 (check id='seebeck_curve') ===
def score_2(artifact, step, ctx):
    if not ctx.get("sanity_ok", False): return 0.0
    try:
        temps = [float(r['T(K)']) for r in artifact]
        seebeck = [float(r['S(µV/K)']) for r in artifact]
    except:
        return 0.0
    if len(temps) < 2:
        return 0.0
    # linear interpolation
    def get_S(t):
        if t <= temps[0]: return seebeck[0]
        if t >= temps[-1]: return seebeck[-1]
        for i in range(len(temps)-1):
            if temps[i] <= t <= temps[i+1]:
                t0, t1 = temps[i], temps[i+1]
                s0, s1 = seebeck[i], seebeck[i+1]
                return s0 + (s1-s0)*(t-t0)/(t1-t0) if t1 != t0 else s0
        return 0.0
    S80 = get_S(80)
    S300 = get_S(300)
    peak_S = max(seebeck)
    peak_T = temps[seebeck.index(peak_S)]
    gold = ctx["gold_seebeck"]
    tol_S = gold["tolerance_S"]
    tol_peak_temp = gold["tolerance_peak_temp"]
    # peak temperature
    if abs(peak_T - gold["peak_temp"]) <= tol_peak_temp:
        score_peak_T = 1.0
    else:
        score_peak_T = max(0.0, 1.0 - (abs(peak_T - gold["peak_temp"]) - tol_peak_temp)/tol_peak_temp)
    # peak S
    delta_S = abs(peak_S - gold["peak_S"])
    if delta_S <= tol_S * gold["peak_S"]:
        score_peak_S = 1.0
    else:
        score_peak_S = max(0.0, 1.0 - (delta_S/gold["peak_S"] - tol_S)/tol_S)
    # S at 300
    delta_S30 = abs(S300 - gold["S_300"])
    if delta_S30 <= tol_S * gold["S_300"]:
        score_S30 = 1.0
    else:
        score_S30 = max(0.0, 1.0 - (delta_S30/gold["S_300"] - tol_S)/tol_S)
    return (score_peak_T + score_peak_S + score_S30) / 3.0


# === block: score_3 (check id='zt_300k') ===
def score_3(artifact, step, ctx):
    if not ctx.get("sanity_ok", False): return 0.0
    val = float(artifact.strip())
    gold = ctx["gold_zt"]
    tol = ctx["tol_zt"]
    delta = abs(val - gold)
    if delta <= tol:
        return 1.0
    else:
        return max(0.0, 1.0 - (delta - tol) / tol)


_SCORERS = {
    'structural_properties': score_0,
    'bandgap': score_1,
    'seebeck_curve': score_2,
    'zt_300k': score_3,
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
