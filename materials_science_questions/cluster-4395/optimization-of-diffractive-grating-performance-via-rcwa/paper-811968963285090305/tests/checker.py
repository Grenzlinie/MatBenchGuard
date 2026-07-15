import os
import json
import csv

# === author imports / helpers ===
import csv, math


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
    return spec  # pass full spec for step-level access


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    gold = step.get('gold_table', [])
    if not gold:
        return 0.0
    # agent rows keyed by m as string
    agent_dict = {str(row.get('m', '')).strip(): row for row in artifact}
    correct = 0
    total = 0
    for gold_row in gold:
        m = str(gold_row['m'])
        agent_row = agent_dict.get(m)
        if agent_row is None:
            # no row for this order -> count all gold fields except m as missed
            total += sum(1 for k in gold_row if k != 'm')
            continue
        for field in ['eta_r', 'theta_r', 'eta_t', 'theta_t']:
            gold_val = gold_row.get(field)
            tol = step.get('tolerance', {}).get(field, {})
            rel_tol = tol.get('relative', 0.0)
            abs_tol = tol.get('absolute', 0.0)
            if gold_val is None:
                # evanescent transmitted order: agent must leave blank
                agent_val = agent_row.get(field, '').strip() if agent_row.get(field) is not None else ''
                total += 1
                if agent_val == '' or agent_val is None:
                    correct += 1
            else:
                agent_val = agent_row.get(field, '')
                total += 1
                try:
                    va = float(agent_val)
                    max_allowed = abs_tol + rel_tol * abs(gold_val)
                    if abs(va - gold_val) <= max_allowed:
                        correct += 1
                except (ValueError, TypeError):
                    pass
    return correct / total if total > 0 else 1.0


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    gold = step.get('gold_table', [])
    if not gold:
        return 0.0
    # agent rows keyed by f as string
    agent_dict = {}
    for row in artifact:
        try:
            f_val = float(row.get('f', ''))
            key = '{:.2f}'.format(f_val)
        except (ValueError, TypeError):
            key = row.get('f', '').strip()
        agent_dict[key] = row
    tol = step.get('tolerance', {}).get('power', {})
    rel_tol = tol.get('relative', 0.0)
    abs_tol = tol.get('absolute', 0.0)
    correct = 0
    total = 0
    for gold_row in gold:
        f_str = '{:.2f}'.format(gold_row['f'])
        agent_row = agent_dict.get(f_str)
        if agent_row is None:
            total += 3  # three power columns
            continue
        for col in ['power_60', 'power_70', 'power_80']:
            gold_val = gold_row[col]
            agent_val = agent_row.get(col, '')
            total += 1
            try:
                va = float(agent_val)
                max_allowed = abs_tol + rel_tol * abs(gold_val)
                if abs(va - gold_val) <= max_allowed:
                    correct += 1
            except (ValueError, TypeError):
                pass
    return correct / total if total > 0 else 1.0


_SCORERS = {
    'step_01': score_0,
    'step_02': score_1,
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
