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


# === block: score_0 (check id='check_single_ni_moment') ===
def score_0(artifact, step, ctx):
    val = artifact.get('single_ni_magnetic_moment')
    if not isinstance(val, (int, float)):
        return 0.0
    target = step['target']
    tol = step.get('tolerance', 0.1)
    return 1.0 if abs(val - target) <= tol else 0.0


# === block: score_1 (check id='check_table1') ===
def score_1(artifact, step, ctx):
    rows = artifact.get('table1')
    if not isinstance(rows, list):
        return 0.0
    gold_rows = step['gold_rows']
    tols = step.get('tolerances', {})
    dist_tol = tols.get('ni_ni_distance', 0.1)
    delta_abs_tol = tols.get('delta_E_abs', 20)
    delta_rel_tol = tols.get('delta_E_rel', 0.5)
    m_tot_tol = tols.get('m_tot', 0.1)
    agent_by_config = {}
    for row in rows:
        cfg = row.get('config')
        if cfg is not None:
            agent_by_config[cfg] = row
    row_scores = []
    for gold in gold_rows:
        cfg = gold['config']
        agent_row = agent_by_config.get(cfg)
        if agent_row is None:
            row_scores.append(0.0)
            continue
        sub = []
        d_gold = gold['ni_ni_distance']
        d_agent = agent_row.get('ni_ni_distance')
        if isinstance(d_agent, (int, float)) and abs(d_agent - d_gold) <= dist_tol:
            sub.append(1.0)
        else:
            sub.append(0.0)
        de_gold = gold['delta_E']
        de_agent = agent_row.get('delta_E')
        if isinstance(de_agent, (int, float)):
            diff = abs(de_agent - de_gold)
            if diff <= delta_abs_tol:
                sub.append(1.0)
            elif abs(de_gold) > 1e-6 and diff <= delta_rel_tol * abs(de_gold):
                sub.append(1.0)
            else:
                sub.append(0.0)
        else:
            sub.append(0.0)
        mt_gold = gold['m_tot']
        mt_agent = agent_row.get('m_tot')
        if isinstance(mt_agent, (int, float)) and abs(mt_agent - mt_gold) <= m_tot_tol:
            sub.append(1.0)
        else:
            sub.append(0.0)
        cp_gold = gold['coupling']
        cp_agent = agent_row.get('coupling')
        if str(cp_agent).strip() == cp_gold:
            sub.append(1.0)
        else:
            sub.append(0.0)
        row_score = sum(sub) / len(sub) if sub else 0.0
        row_scores.append(row_score)
    if not row_scores:
        return 0.0
    return sum(row_scores) / len(row_scores)


# === block: score_2 (check id='check_table2') ===
def score_2(artifact, step, ctx):
    rows = artifact.get('table2')
    if not isinstance(rows, list):
        return 0.0
    gold_rows = step['gold_rows']
    tols = step.get('tolerances', {})
    dist_tol = tols.get('ni_ni_distance', 0.1)
    delta_abs_tol = tols.get('delta_E_abs', 20)
    delta_rel_tol = tols.get('delta_E_rel', 0.5)
    m_tot_tol = tols.get('m_tot', 0.1)
    agent_by_case = {}
    for row in rows:
        cs = row.get('case')
        if cs is not None:
            agent_by_case[cs] = row
    row_scores = []
    for gold in gold_rows:
        cs = gold['case']
        agent_row = agent_by_case.get(cs)
        if agent_row is None:
            row_scores.append(0.0)
            continue
        sub = []
        d_gold = gold['ni_ni_distance']
        d_agent = agent_row.get('ni_ni_distance')
        if isinstance(d_agent, (int, float)) and abs(d_agent - d_gold) <= dist_tol:
            sub.append(1.0)
        else:
            sub.append(0.0)
        de_gold = gold['delta_E']
        de_agent = agent_row.get('delta_E')
        if isinstance(de_agent, (int, float)):
            diff = abs(de_agent - de_gold)
            if diff <= delta_abs_tol:
                sub.append(1.0)
            elif abs(de_gold) > 1e-6 and diff <= delta_rel_tol * abs(de_gold):
                sub.append(1.0)
            else:
                sub.append(0.0)
        else:
            sub.append(0.0)
        mt_gold = gold['m_tot']
        mt_agent = agent_row.get('m_tot')
        if isinstance(mt_agent, (int, float)) and abs(mt_agent - mt_gold) <= m_tot_tol:
            sub.append(1.0)
        else:
            sub.append(0.0)
        cp_gold = gold['coupling']
        cp_agent = agent_row.get('coupling')
        if str(cp_agent).strip() == cp_gold:
            sub.append(1.0)
        else:
            sub.append(0.0)
        row_score = sum(sub) / len(sub) if sub else 0.0
        row_scores.append(row_score)
    if not row_scores:
        return 0.0
    return sum(row_scores) / len(row_scores)


# === block: score_3 (check id='check_trend') ===
def score_3(artifact, step, ctx):
    table1 = artifact.get('table1')
    table2 = artifact.get('table2')
    if not isinstance(table1, list) or not isinstance(table2, list):
        return 0.0
    if len(table1) != len(table2):
        return 0.0
    satisfied = 0
    min_required = step.get('min_satisfied_pairs', 4)
    for r1, r2 in zip(table1, table2):
        de1 = r1.get('delta_E')
        de2 = r2.get('delta_E')
        cp1 = r1.get('coupling')
        cp2 = r2.get('coupling')
        if not isinstance(de1, (int, float)) or not isinstance(de2, (int, float)):
            continue
        if de2 < de1 or (cp1 == 'FM' and cp2 == 'AFM'):
            satisfied += 1
    return 1.0 if satisfied >= min_required else 0.0


_SCORERS = {
    'check_single_ni_moment': score_0,
    'check_table1': score_1,
    'check_table2': score_2,
    'check_trend': score_3,
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
