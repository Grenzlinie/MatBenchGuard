import os
import json
import csv

# === author imports / helpers ===
import math
import csv
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
    import math
    f = 0.34
    E_f = 410e9
    E_m = 110e9
    D = 140e-6
    tau = 23e6
    I0 = 1.0
    I1 = 1.2
    c1 = 4 * I1**2 / math.pi
    c2 = (math.pi / (2 * I1)) ** 2 * I0
    ctx = {
        'c1': c1,
        'c2': c2,
    }
    return ctx


# === block: score_0 (check id='compute_analytical_crack_area') ===
def score_0(artifact, step, ctx):
    import math

    rtol = step.get('relative_tolerance', 0.001)
    atol = step.get('absolute_tolerance', 1e-5)
    ltol = step.get('limit_tolerance', 0.01)

    total_col = 0
    passed_col = 0
    total_limit = 0
    passed_limit = 0

    c1 = ctx['c1']
    c2 = ctx['c2']

    for row in artifact:
        try:
            sigma = float(row['Sigma_a'])
        except Exception:
            continue

        # Expected values
        if sigma > 1:
            A_short_exp = c1 * (math.sqrt(1 + c2 * sigma) - 1)**2
        else:
            A_short_exp = float('nan')
        A_long_exp = sigma**2 - 0.225 * sigma**3
        A_unbridged_exp = math.pi * sigma

        if sigma / 2 > 1:
            sig_half = sigma / 2
            DeltaA_short_exp = 2 * c1 * (math.sqrt(1 + c2 * sig_half) - 1)**2
        else:
            DeltaA_short_exp = float('nan')

        sig_half = sigma / 2
        DeltaA_long_exp = 2 * (sig_half**2 - 0.225 * sig_half**3)

        expected = {
            'A_short': A_short_exp,
            'A_long': A_long_exp,
            'A_unbridged': A_unbridged_exp,
            'DeltaA_short': DeltaA_short_exp,
            'DeltaA_long': DeltaA_long_exp,
        }

        # Column comparisons
        for col_name, exp_val in expected.items():
            if math.isnan(exp_val):
                continue
            if col_name not in row or row[col_name] == '':
                continue
            try:
                val = float(row[col_name])
            except Exception:
                continue
            total_col += 1
            if not math.isnan(val):
                if abs(val - exp_val) <= atol + rtol * max(abs(val), abs(exp_val)):
                    passed_col += 1

        # Limit check 1: Sigma_a > 10 => A_short ~ A_unbridged
        if sigma > 10 and not math.isnan(expected['A_short']):
            total_limit += 1
            try:
                agent_Ashort = float(row['A_short'])
                agent_Aunbr = float(row['A_unbridged'])
                if abs(agent_Ashort - agent_Aunbr) / agent_Aunbr <= ltol:
                    passed_limit += 1
            except Exception:
                pass

        # Limit check 2: Sigma_a < 0.1 => A_long ~ Sigma_a^2
        if sigma < 0.1:
            total_limit += 1
            try:
                agent_Along = float(row['A_long'])
                if agent_Along != 0 and abs(agent_Along - sigma**2) / (sigma**2) <= ltol:
                    passed_limit += 1
            except Exception:
                pass

    total = total_col + total_limit
    if total == 0:
        score = 0.0
    else:
        score = (passed_col + passed_limit) / total
    return score


_SCORERS = {
    'compute_analytical_crack_area': score_0,
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
