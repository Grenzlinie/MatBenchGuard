import os
import json
import csv

# === author imports / helpers ===
import csv
import json
from collections import defaultdict
import os


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
    gold = spec.get('gold_values', {})
    return {'gold_values': gold}


# === block: score_0 (check id='sif_check') ===
def score_0(artifact, step, ctx):
    gold = ctx['gold_values']
    rel_tol_peak = step.get('params', {}).get('rel_tol_peak', 0.05)
    rel_tol_static = step.get('params', {}).get('rel_tol_static', 0.05)
    rows = artifact
    if not rows:
        return 0.0
    # group rows
    from collections import defaultdict
    groups = defaultdict(list)
    for row in rows:
        try:
            mat = row['material'].strip()
            hcr = row['h_c_ratio'].strip()
            tn = float(row['time_normalized'])
            sif = float(row['sif_normalized'])
        except (KeyError, ValueError):
            continue
        groups[(mat, hcr)].append((tn, sif))
    total_score = 0.0
    count = 0
    for mat, hcrs in gold.items():
        for hcr, vals in hcrs.items():
            count += 1
            case_score = 0.0
            gold_peak = vals['peak']
            gold_static = vals['static']
            # find agent rows
            agent_peak = None
            agent_static = None
            ord_times = []
            ord_sifs = []
            for t, s in groups.get((mat, hcr), []):
                if abs(t - (-1)) < 1e-6:
                    agent_peak = s
                elif abs(t - (-2)) < 1e-6:
                    agent_static = s
                else:
                    ord_times.append(t)
                    ord_sifs.append(s)
            # peak comparison
            if agent_peak is not None:
                if gold_peak != 0:
                    err = abs(agent_peak - gold_peak) / abs(gold_peak)
                else:
                    err = abs(agent_peak)
                if err <= rel_tol_peak:
                    case_score += 0.5
                elif err <= 2 * rel_tol_peak:
                    case_score += 0.5 * (2.0 - err / rel_tol_peak)
            # static comparison
            if agent_static is not None:
                if gold_static != 0:
                    err = abs(agent_static - gold_static) / abs(gold_static)
                else:
                    err = abs(agent_static)
                if err <= rel_tol_static:
                    case_score += 0.5
                elif err <= 2 * rel_tol_static:
                    case_score += 0.5 * (2.0 - err / rel_tol_static)
            # internal consistency: max of ord points should be close to peak
            if agent_peak is not None and ord_sifs:
                max_ord = max(ord_sifs)
                if max_ord > 0 and abs(max_ord - agent_peak) / max_ord > rel_tol_peak:
                    case_score *= 0.9
                if agent_static is not None and agent_static > agent_peak + 0.1:
                    case_score *= 0.9
            total_score += case_score
    if count == 0:
        return 0.0
    return total_score / count


_SCORERS = {
    'sif_check': score_0,
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
