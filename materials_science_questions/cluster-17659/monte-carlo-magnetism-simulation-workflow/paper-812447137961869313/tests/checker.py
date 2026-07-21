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
    def prepare(outputs_dir, spec):
        refs = {}
        for step in spec.get("steps", []):
            sid = step.get("id")
            if sid == "coercive_field_vs_temperature":
                refs[sid] = {float(t): float(hc) for t, hc in step["reference_values"]}
            elif sid == "magnetization_quench":
                refs[sid] = {float(t): float(m) for t, m in step["reference_values"]}
        return {"refs": refs, "spec": spec}


# === block: score_0 (check id='hysteresis_loop') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) < 100:
        return 0.0
    try:
        H = [float(r["H"]) for r in artifact]
        M = [float(r["M"]) for r in artifact]
    except (KeyError, ValueError):
        return 0.0
    max_h = max(H)
    peak_idx = H.index(max_h)
    forward = list(zip(H[:peak_idx+1], M[:peak_idx+1]))
    reverse = list(zip(H[peak_idx:], M[peak_idx:]))
    def area_trap(s):
        a = 0.0
        for i in range(len(s)-1):
            dh = s[i+1][0] - s[i][0]
            avg = (s[i+1][1] + s[i][1]) / 2.0
            a += dh * avg
        return a
    area_fwd = area_trap(forward)
    area_rev = area_trap(reverse)
    loop_area = abs(area_fwd - area_rev)
    if loop_area > 0.1:
        return 1.0
    else:
        return 0.0


# === block: score_1 (check id='coercive_field_vs_temperature') ===
def score_1(artifact, step, ctx):
    refs = ctx["refs"].get("coercive_field_vs_temperature", {})
    tol = step["tolerance"]
    temp_to_hc = {}
    for row in artifact:
        try:
            t = float(row["temperature"])
            hc = float(row["coercive_field"])
            temp_to_hc[t] = hc
        except (KeyError, ValueError):
            continue
    required_temps = [0.1,0.3,0.5,0.7,0.9,1.0,1.1,1.2]
    point_scores = []
    for t in required_temps:
        if t not in refs:
            continue
        hc_agent = temp_to_hc.get(t)
        if hc_agent is None:
            point_scores.append(0.0)
            continue
        diff = abs(hc_agent - refs[t])
        score = max(0.0, 1.0 - diff / tol)
        point_scores.append(score)
    avg_pt = sum(point_scores) / len(point_scores) if point_scores else 0.0
    sorted_temps = sorted(temp_to_hc.keys())
    violations = 0
    for i in range(len(sorted_temps)-1):
        if sorted_temps[i] < sorted_temps[i+1]:
            if temp_to_hc[sorted_temps[i]] < temp_to_hc[sorted_temps[i+1]]:
                violations += 1
    mono_score = max(0.0, 1.0 - 0.1 * violations)
    final = 0.7 * avg_pt + 0.3 * mono_score
    return min(1.0, final)


# === block: score_2 (check id='magnetization_quench') ===
def score_2(artifact, step, ctx):
    refs = ctx["refs"].get("magnetization_quench", {})
    tol = step.get("tolerance", 0.05)
    agent_data = {}
    for row in artifact:
        try:
            t = float(row["temperature"])
            m = float(row["magnetization"])
            agent_data[t] = m
        except (KeyError, ValueError):
            continue
    point_scores = []
    for t, m_ref in refs.items():
        if t in agent_data:
            m_agent = agent_data[t]
            diff = abs(m_agent - m_ref)
            score = max(0.0, 1.0 - diff / tol)
            point_scores.append(score)
        else:
            point_scores.append(0.0)
    avg_pt = sum(point_scores) / len(point_scores) if point_scores else 0.0
    temps = sorted(agent_data.keys())
    if temps:
        max_m = max(agent_data.values())
        peak_ts = [t for t, m in agent_data.items() if m == max_m]
        peak_t = sum(peak_ts) / len(peak_ts)
        peak_check = step.get("peak_check", [0.5, 0.7])
        if peak_check[0] <= peak_t <= peak_check[1]:
            peak_score = 1.0
        else:
            peak_score = 0.0
    else:
        peak_score = 0.0
    final = 0.6 * avg_pt + 0.4 * peak_score
    return min(1.0, final)


_SCORERS = {
    'hysteresis_loop': score_0,
    'coercive_field_vs_temperature': score_1,
    'magnetization_quench': score_2,
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
