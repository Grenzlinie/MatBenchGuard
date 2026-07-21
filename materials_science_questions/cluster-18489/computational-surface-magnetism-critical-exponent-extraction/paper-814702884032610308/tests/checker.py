import os
import json
import csv

# === author imports / helpers ===
import re


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
        '''Prepare gold reference from grading_spec_json.'''
        gold = spec.get("gold_table", {})
        if not gold:
            gold = {"finite": [], "extrap": {}}
        return {"gold": gold}


# === block: score_0 (check id='table_step') ===
def score_0(artifact, step, ctx):
        rows = artifact  # list of dicts
        gold = ctx["gold"]
        finite_gold = gold.get("finite", [])
        extrap_gold = gold.get("extrap", {})

        if len(rows) != 10:
            return 0.0

        fields = ["K_star", "y_t", "y_h", "y_h_over_y_t", "y_hs"]
        n_finite_correct = 0
        n_finite_total = 0

        for idx, fg in enumerate(finite_gold):
            if idx >= len(rows) - 1:  # last row is extrapolated
                break
            row = rows[idx]
            L = fg["L"]
            rtol = 1e-6 if L <= 5 else 1e-5
            for f in fields:
                try:
                    agent_val = float(row.get(f, ""))
                except (ValueError, TypeError):
                    agent_val = None
                if agent_val is not None:
                    gold_val = fg[f]
                    if abs(gold_val) > 1e-12:
                        if abs(agent_val - gold_val) <= rtol * abs(gold_val):
                            n_finite_correct += 1
                    else:
                        # fallback absolute tolerance for zero-valued fields (none expected)
                        if abs(agent_val - gold_val) <= 1e-12:
                            n_finite_correct += 1
                n_finite_total += 1

        # Extrapolated row (10th row, index 9)
        extrap_row = rows[9] if len(rows) > 9 else {}
        extrap_correct = 0
        extrap_total = 5
        for f in fields:
            val_str = str(extrap_row.get(f, ""))
            match = re.match(r'^\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)\s*\(\s*\d+\s*\)\s*$', val_str)
            if match:
                try:
                    agent_center = float(match.group(1))
                    gold_center = extrap_gold.get(f + "_c")
                    gold_err = extrap_gold.get(f + "_err", 0.0)
                    if gold_center is not None and abs(agent_center - gold_center) <= 2 * gold_err:
                        extrap_correct += 1
                except (ValueError, TypeError):
                    pass

        total_fields = n_finite_total + extrap_total
        if total_fields == 0:
            return 0.0
        return max(0.0, min(1.0, (n_finite_correct + extrap_correct) / total_fields))


_SCORERS = {
    'table_step': score_0,
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
