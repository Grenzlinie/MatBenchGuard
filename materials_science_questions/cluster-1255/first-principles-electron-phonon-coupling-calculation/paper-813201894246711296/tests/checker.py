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


# === block: score_0 (check id='step04_hg_freq') ===
def score_0(artifact, step, ctx):
    gold_freq = step['gold_frequencies']
    tol = step['tolerance_cm1']
    rows = artifact
    freq_map = {}
    for row in rows:
        comp = row.get('compound','').strip()
        mode = row.get('mode','').strip()
        if comp and mode:
            freq_map[(comp, mode)] = row.get('frequency_cm1')
    total = 0
    ok = 0
    for comp, modes in gold_freq.items():
        for mode, ref_freq in modes.items():
            total += 1
            agent_val = freq_map.get((comp, mode))
            if agent_val is not None:
                try:
                    if abs(float(agent_val) - ref_freq) <= tol:
                        ok += 1
                except:
                    pass
    return ok / total if total > 0 else 0.0


# === block: score_1 (check id='step06_coupling_tc') ===
def score_1(artifact, step, ctx):
    gold_coupling = step['gold_coupling']
    rel_tol = step['tolerance_rel']
    rows = artifact
    data = {}
    for row in rows:
        comp = row.get('compound','').strip()
        if comp:
            data[comp] = row
    params = ['lambda_N0','lambda_Nxi','omega_ln_N0','omega_ln_Nxi']
    param_ok = 0
    param_total = 0
    tc_values = []
    scdft_tc = step['scdft_tc']
    tc_factor_low = step['tc_factor_low']
    tc_factor_high = step['tc_factor_high']
    for comp in ['K3C60','Rb3C60','Cs3C60']:
        gold = gold_coupling[comp]
        agent = data.get(comp)
        if agent is None:
            continue
        for p in params:
            param_total += 1
            g = gold[p]
            a_str = agent.get(p)
            if a_str is None:
                continue
            try:
                a = float(a_str)
            except:
                continue
            if abs(a - g) <= rel_tol * abs(g):
                param_ok += 1
        tc_str = agent.get('Tc_MAD_K')
        if tc_str is not None:
            try:
                tc = float(tc_str)
                tc_values.append(tc)
            except:
                pass
    tc_ok = 0
    tc_total = 0
    if len(tc_values) == 3 and tc_values[0] < tc_values[1] < tc_values[2]:
        tc_ok += 1
    tc_total += 1
    for i, comp in enumerate(['K3C60','Rb3C60','Cs3C60']):
        if i < len(tc_values):
            targ = scdft_tc[comp]
            tc = tc_values[i]
            if tc_factor_low * targ <= tc <= tc_factor_high * targ:
                tc_ok += 1
        tc_total += 1
    param_score = param_ok / param_total if param_total > 0 else 0.0
    tc_score = tc_ok / tc_total if tc_total > 0 else 0.0
    combined = 0.6 * param_score + 0.4 * tc_score
    return combined


_SCORERS = {
    'step04_hg_freq': score_0,
    'step06_coupling_tc': score_1,
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
