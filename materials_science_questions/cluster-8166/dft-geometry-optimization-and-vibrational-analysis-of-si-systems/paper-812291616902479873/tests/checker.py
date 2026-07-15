import os
import json
import csv

# === author imports / helpers ===
import csv
import os
import json


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


# === block: score_0 (check id='step_01_bcp_analysis') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0

    # Normalize agent rows: cast n to int, strip/lower method
    agent_rows = []
    for row in artifact:
        try:
            n = int(row.get('n', ''))
            meth = (row.get('method', '')).strip().lower()
            rho = float(row.get('rho', 0))
            lap = float(row.get('laplacian', 0))
            d_si = float(row.get('d_Si', 0))
            agent_rows.append({'n': n, 'method': meth, 'rho': rho, 'laplacian': lap, 'd_si': d_si})
        except (ValueError, KeyError):
            continue

    gold_rows = step.get('gold_rows', [])
    tols = step.get('tolerances', {'rho': 0.005, 'laplacian': 0.02, 'd_si': 1.0})
    if not gold_rows:
        return 1.0

    scores = []
    for g_row in gold_rows:
        gn = g_row['n']
        gmeth = g_row['method'].strip().lower()
        # find matching agent row
        match = None
        for a_row in agent_rows:
            if a_row['n'] == gn and a_row['method'] == gmeth:
                match = a_row
                break
        if match is None:
            scores.append(0.0)
            continue
        # components
        rho_ok = 1.0 if abs(match['rho'] - g_row['rho']) <= tols['rho'] else 0.0
        lap_ok = 1.0 if abs(match['laplacian'] - g_row['laplacian']) <= tols['laplacian'] else 0.0
        dsi_ok = 1.0 if abs(match['d_si'] - g_row['d_si']) <= tols['d_si'] else 0.0
        row_score = (rho_ok + lap_ok + dsi_ok) / 3.0
        scores.append(row_score)

    return sum(scores) / len(scores)


# === block: score_1 (check id='step_02_energy_cost') ===
def score_1(artifact, step, ctx):
    try:
        val = float(artifact.strip())
    except (ValueError, AttributeError, TypeError):
        return 0.0
    min_val = float(step.get('threshold_min', 1e-6))
    max_val = float(step.get('threshold_max', 6.0))
    if val > min_val and val <= max_val:
        return 1.0
    else:
        return 0.0


_SCORERS = {
    'step_01_bcp_analysis': score_0,
    'step_02_energy_cost': score_1,
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
