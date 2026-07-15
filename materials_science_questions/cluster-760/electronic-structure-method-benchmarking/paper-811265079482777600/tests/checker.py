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
    ctx = {}
    for step in spec.get('steps', []):
        if step['id'] == 'sigma_bde':
            ctx['bde_config'] = step.get('config', {})
    return ctx


# === block: score_0 (check id='nhc_homo_lumo') ===
def score_0(artifact, step, ctx):
    val = artifact.get('homo_lumo_gap_kcal_mol')
    if val is None:
        return 0.0
    return 1.0 if abs(val - step['target']) <= step['tolerance_abs'] else 0.0


# === block: score_1 (check id='nhc_casscf_3b1') ===
def score_1(artifact, step, ctx):
    val = artifact.get('casscf_b3b1_energy_kcal_mol')
    if val is None:
        return 0.0
    return 1.0 if abs(val - step['target']) <= step['tolerance_abs'] else 0.0


# === block: score_2 (check id='nhc_casscf_1b1') ===
def score_2(artifact, step, ctx):
    val = artifact.get('casscf_b1b1_energy_kcal_mol')
    if val is None:
        return 0.0
    return 1.0 if abs(val - step['target']) <= step['tolerance_abs'] else 0.0


# === block: score_3 (check id='sigma_bde') ===
def score_3(artifact, step, ctx):
    import csv
    bde_cfg = ctx.get('bde_config', {})
    gold_rows = bde_cfg.get('gold_rows', [])
    trend_cfg = bde_cfg.get('trend_check', {})
    if not isinstance(artifact, list):
        return 0.0
    data = {}
    for row in artifact:
        tm = row.get('TM', '').strip()
        try:
            b3 = float(row['BDE_B3LYP'])
            cc = float(row['BDE_CCSDT'])
            mult = int(row['multiplicity_gs'])
        except (ValueError, KeyError):
            continue
        data[tm] = {'B3LYP': b3, 'CCSDT': cc, 'mult': mult}
    if not data:
        return 0.0
    b3lyp_scores = []
    ccsdt_scores = []
    for gold in gold_rows:
        tm = gold['TM']
        if tm not in data:
            b3lyp_scores.append(0.0)
            ccsdt_scores.append(0.0)
            continue
        agent_b3 = data[tm]['B3LYP']
        agent_cc = data[tm]['CCSDT']
        b3lyp_scores.append(1.0 if abs(agent_b3 - gold['B3LYP']) <= gold['b3lyp_tol'] else 0.0)
        ccsdt_scores.append(1.0 if abs(agent_cc - gold['CCSDT']) <= gold['ccsdt_tol'] else 0.0)
    num = len(gold_rows) if gold_rows else 1
    b3lyp_avg = sum(b3lyp_scores) / num
    ccsdt_avg = sum(ccsdt_scores) / num
    trend_score = 1.0
    trend_tms = trend_cfg.get('B3LYP_max_TMs', [])
    if trend_tms:
        max_vals = {}
        for tm in data:
            max_vals[tm] = data[tm]['B3LYP']
        top_val = max(max_vals.values())
        for t in trend_tms:
            if t not in data or data[t]['B3LYP'] < top_val:
                trend_score = 0.0
                break
        if trend_score > 0.0:
            for t in trend_tms:
                if t not in data:
                    trend_score = 0.0
                    break
                if data[t]['B3LYP'] != top_val and max_vals[t] != top_val:
                    trend_score = 0.0
                    break
    return b3lyp_avg * 0.5 + ccsdt_avg * 0.3 + trend_score * 0.2


_SCORERS = {
    'nhc_homo_lumo': score_0,
    'nhc_casscf_3b1': score_1,
    'nhc_casscf_1b1': score_2,
    'sigma_bde': score_3,
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
