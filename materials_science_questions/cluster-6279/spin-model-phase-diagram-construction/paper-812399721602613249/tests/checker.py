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
    def prepare(outputs_dir, spec):
        phi = (1 + math.sqrt(5)) / 2
        gold_sequence = 'E -> S3 -> S4 -> \\\\bar{S}_3 -> F'
        gold_transitions = {
            'E_to_S3': (-0.3, 1/6, (1/3)*math.log(1+math.sqrt(2))),
            'S3_to_S4': (2.0, (phi+3)/(3*(phi+2)), (1/3)*math.log(phi)),
            'S4_to_barS3': (5.0, (2*phi+3)/(3*(phi+2)), (1/3)*math.log(phi)),
            'barS3_to_F': (6.2, 5/6, (1/3)*math.log(1+math.sqrt(2)))
        }
        return {'gold_sequence': gold_sequence, 'gold_transitions': gold_transitions, 'mu_tol': 0.01, 'cov_tol': 0.05, 'ent_tol': 0.1}


# === block: score_0 (check id='sequence_check') ===
def score_0(artifact, step, ctx):
    if artifact is None:
        return 0.0
    content = artifact.strip()
    expected = ctx['gold_sequence']
    return 1.0 if content == expected else 0.0


# === block: score_1 (check id='transitions_check') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        import csv
        if artifact is None:
            return 0.0
        lines = artifact.strip().split('\n')
        if len(lines) < 2:
            return 0.0
        reader = csv.DictReader(lines)
        rows = list(reader)
        gold_dict = ctx['gold_transitions']
        mu_tol = ctx['mu_tol']
        cov_tol = ctx['cov_tol']
        ent_tol = ctx['ent_tol']
        reported = {}
        for row in rows:
            name = row.get('transition_name', '').strip()
            try:
                mu = float(row['mu'])
                cov = float(row['coverage'])
                ent = float(row['entropy'])
                reported[name] = (mu, cov, ent)
            except (ValueError, TypeError):
                pass
        n_gold = len(gold_dict)
        n_report = len(reported)
        if n_report == 0:
            return 0.0
        row_scores = []
        for name, (tgt_mu, tgt_cov, tgt_ent) in gold_dict.items():
            if name in reported:
                mu_val, cov_val, ent_val = reported[name]
                mu_ok = 1.0 if abs(mu_val - tgt_mu) <= mu_tol else 0.0
                cov_ok = 1.0 if abs(cov_val - tgt_cov) <= cov_tol else 0.0
                ent_ok = 1.0 if abs(ent_val - tgt_ent) <= ent_tol else 0.0
                row_score = (mu_ok + cov_ok + ent_ok) / 3.0
                row_scores.append(row_score)
            else:
                row_scores.append(0.0)
        match_ratio = n_gold / max(n_gold, n_report)
        mean_row_score = sum(row_scores) / len(row_scores) if row_scores else 0.0
        return mean_row_score * match_ratio


_SCORERS = {
    'sequence_check': score_0,
    'transitions_check': score_1,
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
