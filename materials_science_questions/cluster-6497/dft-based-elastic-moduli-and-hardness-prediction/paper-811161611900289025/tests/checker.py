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
        # Hidden gold is already inline in step config; nothing to prepare here.
        return {}


# === block: score_0 (check id='fitted_parameters') ===
def score_0(artifact, step, ctx):
        rows = [r for r in artifact if all(k in r for k in ['Group','m','C'])]
        gold = step['gold']
        groups = ['sp3','spd','3d','4d','5d4f']
        score_per_group = 0.0
        for g in groups:
            match = [r for r in rows if r['Group'].strip() == g]
            if not match:
                continue
            try:
                m = float(match[0]['m'])
                c = float(match[0]['C'])
            except:
                continue
            gd = gold.get(g)
            if gd is None:
                continue
            m_ok = abs(m - gd['m']) <= 0.01
            c_ok = abs(c - gd['C']) <= 0.001
            if m_ok and c_ok:
                score_per_group += 1.0
            elif m_ok or c_ok:
                score_per_group += 0.5
        # max possible 5.0
        score = min(1.0, score_per_group / 5.0)
        return score


# === block: score_1 (check id='predicted_B') ===
def score_1(artifact, step, ctx):
        # Load the agent's predicted bulk moduli from the output file
        import csv
        pred_path = '/app/outputs/step_02_predicted_B.csv'
        agent_preds = {}
        try:
            with open(pred_path, newline='') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    comp = (row.get('Compound') or '').strip()
                    if not comp:
                        continue
                    try:
                        pred_b = float(row.get('Predicted_B_GPa') or '')
                    except:
                        continue
                    agent_preds[comp] = pred_b
        except:
            return 0.0

        if not agent_preds:
            return 0.0

        compounds = step.get('compounds', []) or []
        if not compounds:
            return 0.0

        scores = []
        for comp in compounds:
            comp_name = (comp.get('Compound') or '').strip()
            if comp_name not in agent_preds:
                scores.append(0.0)
                continue
            b_pred = agent_preds[comp_name]
            b_exp = comp.get('B_exp_GPa')
            if b_exp is None or b_exp == 0:
                rel_err = 1.0
            else:
                rel_err = abs(b_pred - b_exp) / b_exp
            # full credit if relative error <= 20%; linear decay to 0 at 40%
            if rel_err <= 0.20:
                sc = 1.0
            elif rel_err >= 0.40:
                sc = 0.0
            else:
                sc = (0.40 - rel_err) / 0.20
            scores.append(sc)
        avg = sum(scores) / len(scores) if scores else 0.0
        return avg


_SCORERS = {
    'fitted_parameters': score_0,
    'predicted_B': score_1,
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
