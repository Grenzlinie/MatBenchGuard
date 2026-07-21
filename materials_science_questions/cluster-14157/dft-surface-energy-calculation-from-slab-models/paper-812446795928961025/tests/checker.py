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


# === block: score_0 (check id='check_surface_energies') ===
def score_0(artifact, step, ctx):
    rows = artifact
    gold_table = step['gold_table']
    tols = step['tolerances']
    metals_expected = set(gold_table.keys())
    metal_rows = {row['metal']: row for row in rows}
    if not metals_expected.issubset(metal_rows.keys()):
        return 0.0
    scores = []
    for metal, gold in gold_table.items():
        row = metal_rows[metal]
        try:
            sigma0 = float(row['sigma0'])
            sigma1 = float(row['sigma1'])
            mu1 = float(row['mu1'])
        except (KeyError, ValueError):
            scores.append(0.0)
            continue
        ok = True
        if abs(sigma0 - gold['sigma0']) > tols['sigma0_relative'] * abs(gold['sigma0']):
            ok = False
        if abs(sigma1 - gold['sigma1']) > tols['sigma1_relative'] * abs(gold['sigma1']):
            ok = False
        if abs(mu1 - gold['mu1']) > tols['mu1_relative'] * abs(gold['mu1']):
            ok = False
        if sigma1 <= 0:
            ok = False
        scores.append(1.0 if ok else 0.0)
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_1 (check id='check_critical_charge_na') ===
def score_1(artifact, step, ctx):
    rows = artifact
    W_plus_eV = step['W_plus_eV']
    eV_to_au = step['eV_to_au']
    tol_abs = step['Z_star_tolerance_abs']
    W_plus_au = W_plus_eV * eV_to_au
    agent_rows = {}
    for r in rows:
        try:
            R = int(float(r['R']))
            Z_agent = float(r['Z_star'])
            agent_rows[R] = Z_agent
        except (KeyError, ValueError):
            continue
    expected_Rs = set(range(5, 31))
    if not expected_Rs.issubset(agent_rows.keys()):
        return 0.0
    correct = 0
    Z_vals = []
    for R in range(5, 31):
        Z_agent = agent_rows[R]
        Z_exp = W_plus_au * R + 0.5
        Z_vals.append(Z_agent)
        if abs(Z_agent - Z_exp) <= tol_abs:
            correct += 1
    if not all(Z_vals[i+1] >= Z_vals[i] - 1e-12 for i in range(len(Z_vals)-1)):
        return 0.0
    return correct / 26.0


_SCORERS = {
    'check_surface_energies': score_0,
    'check_critical_charge_na': score_1,
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
