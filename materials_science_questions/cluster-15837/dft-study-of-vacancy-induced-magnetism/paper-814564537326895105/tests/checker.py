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


# === block: score_0 (check id='binary_check') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not isinstance(artifact, dict) or 'binary_compounds' not in artifact:
            return 0.0
        gold = step.get('hidden_gold', {})
        compounds_gold = gold.get('binary_compounds', [])
        tolerances = gold.get('tolerances', {})
        a0_rel_tol = tolerances.get('a0_rel', 0.01)
        E0_abs_tol = max(1.0, tolerances.get('E0_abs', 1.0))
        agent_binary = artifact.get('binary_compounds', [])
        agent_by_name = {e.get('name', '').strip(): e for e in agent_binary if isinstance(e, dict)}
        total_score = 0.0
        count = 0
        for c in compounds_gold:
            name = c.get('name', '')
            if name not in agent_by_name:
                continue
            entry = agent_by_name[name]
            gold_a0 = c.get('a0')
            if gold_a0 is not None:
                agent_a0 = entry.get('a0')
                if isinstance(agent_a0, (int, float)) and abs(gold_a0) > 1e-12:
                    rel_err = abs(agent_a0 - gold_a0) / abs(gold_a0)
                    score_a0 = max(0.0, 1.0 - rel_err / a0_rel_tol)
                else:
                    score_a0 = 1.0 if agent_a0 is not None else 0.0
                total_score += score_a0
                count += 1
            gold_E0 = c.get('E0')
            if gold_E0 is not None:
                agent_E0 = entry.get('E0')
                if isinstance(agent_E0, (int, float)):
                    diff = abs(agent_E0 - gold_E0)
                    score_E0 = max(0.0, 1.0 - diff / E0_abs_tol)
                    total_score += score_E0
                    count += 1
        return total_score / count if count > 0 else 0.0


# === block: score_1 (check id='ternary_numerical') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not isinstance(artifact, dict) or 'ternary_compounds' not in artifact:
            return 0.0
        gold = step.get('hidden_gold', {})
        compounds_gold = gold.get('ternary_compounds', [])
        tolerances = gold.get('tolerances', {})
        a0_rel_tol = tolerances.get('a0_rel', 0.01)
        E0_abs_tol = max(1.0, tolerances.get('E0_abs', 1.0))
        Ef_abs_tol = max(0.05, tolerances.get('Ef_abs', 0.05))
        moment_abs_tol = tolerances.get('moment_abs', 0.01)
        agent_ternary = artifact.get('ternary_compounds', [])
        agent_by_x = {}
        for entry in agent_ternary:
            if isinstance(entry, dict) and 'x' in entry:
                x_val = entry.get('x')
                if x_val is not None:
                    agent_by_x[str(x_val)] = entry
        total_score = 0.0
        count = 0
        for c in compounds_gold:
            x_key = str(c.get('x'))
            if x_key not in agent_by_x:
                continue
            entry = agent_by_x[x_key]
            # a0
            gold_a0 = c.get('a0')
            agent_a0 = entry.get('a0')
            if isinstance(agent_a0, (int, float)) and gold_a0 is not None and abs(gold_a0) > 1e-12:
                rel_err = abs(agent_a0 - gold_a0) / abs(gold_a0)
                score_a0 = max(0.0, 1.0 - rel_err / a0_rel_tol)
            else:
                score_a0 = 0.0
            total_score += score_a0
            count += 1
            # E0
            gold_E0 = c.get('E0')
            agent_E0 = entry.get('E0')
            if isinstance(agent_E0, (int, float)) and gold_E0 is not None:
                diff = abs(agent_E0 - gold_E0)
                score_E0 = max(0.0, 1.0 - diff / E0_abs_tol)
                total_score += score_E0
            count += 1
            # Ef
            gold_Ef = c.get('Ef')
            agent_Ef = entry.get('Ef')
            if isinstance(agent_Ef, (int, float)) and gold_Ef is not None:
                diff = abs(agent_Ef - gold_Ef)
                score_Ef = max(0.0, 1.0 - diff / Ef_abs_tol)
                total_score += score_Ef
            count += 1
            # magnetic_moment
            gold_moment = c.get('magnetic_moment')
            agent_moment = entry.get('magnetic_moment')
            if isinstance(agent_moment, (int, float)) and gold_moment is not None:
                diff = abs(agent_moment - gold_moment)
                score_moment = max(0.0, 1.0 - diff / moment_abs_tol)
                total_score += score_moment
            count += 1
        return total_score / count if count > 0 else 0.0


# === block: score_2 (check id='ternary_classification') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not isinstance(artifact, dict) or 'ternary_compounds' not in artifact:
            return 0.0
        gold_class_map = step.get('hidden_gold', {}).get('class_map', {})
        agent_ternary = artifact.get('ternary_compounds', [])
        agent_by_x = {}
        for entry in agent_ternary:
            if isinstance(entry, dict) and 'x' in entry:
                x_val = entry.get('x')
                if x_val is not None:
                    agent_by_x[str(x_val)] = entry
        total = 0.0
        n = 0
        for x_str, expected_class in gold_class_map.items():
            entry = agent_by_x.get(x_str)
            if entry and isinstance(entry, dict):
                agent_class = entry.get('class')
                if isinstance(agent_class, str) and agent_class.strip().lower() == expected_class:
                    total += 1.0
            n += 1
        return total / n if n > 0 else 0.0


# === block: score_3 (check id='ternary_trends') ===
def score_3(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not isinstance(artifact, dict) or 'ternary_compounds' not in artifact:
            return 0.0
        agent_ternary = artifact.get('ternary_compounds', [])
        entries = [e for e in agent_ternary if isinstance(e, dict) and 'x' in e]
        if len(entries) < 3:
            return 0.0
        entries.sort(key=lambda e: e.get('x', 0.0))
        a0s = [e.get('a0') for e in entries if isinstance(e.get('a0'), (int, float))]
        efs = [e.get('Ef') for e in entries if isinstance(e.get('Ef'), (int, float))]
        a0_increasing = len(a0s) == 3 and a0s[0] < a0s[1] < a0s[2]
        ef_positive = all(ef > 0 for ef in efs)
        score = (1.0 if a0_increasing else 0.0) + (1.0 if ef_positive else 0.0)
        return score / 2.0


_SCORERS = {
    'binary_check': score_0,
    'ternary_numerical': score_1,
    'ternary_classification': score_2,
    'ternary_trends': score_3,
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
