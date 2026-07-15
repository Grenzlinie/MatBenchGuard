import os
import json
import csv

# === author imports / helpers ===
import os, json, re


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
        grueneisen_path = os.path.join(outputs_dir, 'grueneisen_results.json')
        if os.path.exists(grueneisen_path):
            with open(grueneisen_path) as f:
                grueneisen_data = json.load(f)
        else:
            grueneisen_data = None
        return {'grueneisen_data': grueneisen_data}


# === block: score_0 (check id='step_compute_parameters') ===
def score_0(artifact, step, ctx):
        gold_data = step.get('gold_data', {})
        tol_rel = step['tolerance']['relative']
        tol_abs = step['tolerance']['absolute']
        def within_tol(val, gold_list):
            if val is None:
                return False
            for g in gold_list:
                if abs(val - g) <= tol_abs + tol_rel * abs(g):
                    return True
            return False
        total_pairs = 0
        correct_pairs = 0
        for mineral in ('barite', 'celestine'):
            gold_modes = gold_data.get(mineral, [])
            agent_modes = artifact.get(mineral, [])
            agent_by_wn = {m['wavenumber(cm)']: m for m in agent_modes}
            for gm in gold_modes:
                wn = gm['wavenumber']
                agent_mode = agent_by_wn.get(wn)
                if agent_mode is None:
                    for key, gold_vals in [('gamma_iP',gm.get('gamma_iP',[])), ('gamma_iT',gm.get('gamma_iT',[])), ('a_i(x10^5_K^-1)',gm.get('a_i',[]))]:
                        if gold_vals:
                            total_pairs += 1
                    continue
                for key, gold_vals in [('gamma_iP',gm.get('gamma_iP',[])), ('gamma_iT',gm.get('gamma_iT',[])), ('a_i(x10^5_K^-1)',gm.get('a_i',[]))]:
                    if not gold_vals:
                        continue
                    total_pairs += 1
                    agent_val = agent_mode.get(key)
                    if agent_val is not None and within_tol(agent_val, gold_vals):
                        correct_pairs += 1
        if total_pairs == 0:
            return 1.0
        return correct_pairs / total_pairs


# === block: score_1 (check id='step_trend_check') ===
def score_1(artifact, step, ctx):
        m_o_threshold = step.get('m_o_threshold', 250)
        grueneisen_data = ctx.get('grueneisen_data')
        if grueneisen_data is None:
            return 0.0
        def compute_trend(params):
            mo_modes = [m for m in params if m['wavenumber(cm)'] < m_o_threshold]
            so4_modes = [m for m in params if m['wavenumber(cm)'] >= m_o_threshold]
            if not mo_modes or not so4_modes:
                return False
            def group_has_values(key, modes):
                return any(m.get(key) is not None for m in modes)
            def avg_non_null(key, modes):
                vals = [m[key] for m in modes if m.get(key) is not None]
                return sum(vals) / len(vals) if vals else 0.0
            # only check parameters that are present in both groups
            if group_has_values('gamma_iP', mo_modes) and group_has_values('gamma_iP', so4_modes):
                if avg_non_null('gamma_iP', mo_modes) <= avg_non_null('gamma_iP', so4_modes):
                    return False
            if group_has_values('gamma_iT', mo_modes) and group_has_values('gamma_iT', so4_modes):
                if avg_non_null('gamma_iT', mo_modes) <= avg_non_null('gamma_iT', so4_modes):
                    return False
            if group_has_values('a_i(x10^5_K^-1)', mo_modes) and group_has_values('a_i(x10^5_K^-1)', so4_modes):
                mo_abs = sum(abs(m['a_i(x10^5_K^-1)']) for m in mo_modes if m.get('a_i(x10^5_K^-1)') is not None) / max(1, len([m for m in mo_modes if m.get('a_i(x10^5_K^-1)') is not None]))
                so4_abs = sum(abs(m['a_i(x10^5_K^-1)']) for m in so4_modes if m.get('a_i(x10^5_K^-1)') is not None) / max(1, len([m for m in so4_modes if m.get('a_i(x10^5_K^-1)') is not None]))
                if mo_abs <= so4_abs:
                    return False
            return True
        text = artifact
        lines = text.strip().split('\n')
        if len(lines) != 2:
            return 0.0
        pattern = r'\(\s*(True|False)\s*\)'
        match1 = re.search(pattern, lines[0])
        match2 = re.search(pattern, lines[1])
        if not match1 or not match2:
            return 0.0
        agent_barite = (match1.group(1) == 'True')
        agent_celestine = (match2.group(1) == 'True')
        trend_barite = compute_trend(grueneisen_data.get('barite', []))
        trend_celestine = compute_trend(grueneisen_data.get('celestine', []))
        score = 0.0
        if agent_barite == trend_barite:
            score += 0.5
        if agent_celestine == trend_celestine:
            score += 0.5
        return score


_SCORERS = {
    'step_compute_parameters': score_0,
    'step_trend_check': score_1,
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
