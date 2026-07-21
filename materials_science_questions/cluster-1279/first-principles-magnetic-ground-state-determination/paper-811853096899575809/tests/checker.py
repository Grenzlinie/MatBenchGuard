import os
import json
import csv

# === author imports / helpers ===
import csv, os, json


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


# === block: score_0 (check id='shape_gate') ===
def score_0(artifact, step, ctx):
    required = step.get('required_columns', [])
    if not artifact:
        return 0.0
    cols = set(artifact[0].keys())
    if not all(c in cols for c in required):
        return 0.0
    # Numeric tolerance support: if the step declares tol, target and optionally column, verify them.
    tol = step.get('tol')
    target_val = step.get('target')
    if tol is not None and target_val is not None:
        col = step.get('column', 'delta_EFM_meV')
        if isinstance(target_val, dict):
            # per‑system targets (e.g. {'b-IFO': 84.8, ...})
            for row in artifact:
                sys = row.get('system', '').strip()
                if sys in target_val:
                    try:
                        if abs(float(row[col]) - target_val[sys]) > tol:
                            return 0.0
                    except (ValueError, KeyError):
                        return 0.0
        else:
            # scalar target
            for row in artifact:
                try:
                    if abs(float(row[col]) - target_val) > tol:
                        return 0.0
                except (ValueError, KeyError):
                    return 0.0
    return 1.0


# === block: score_1 (check id='delta_EFM') ===
def score_1(artifact, step, ctx):
    targets = step.get('targets', {})
    gold_map = {}
    tol_map = {}
    for sys, t in targets.items():
        gold_map[sys] = t['delta_EFM_meV']
        tol_map[sys] = t.get('tol', 15)
    ordering_rule = step.get('ordering_rule', '')
    expected_order = [s.strip() for s in ordering_rule.split('<') if s.strip()] if ordering_rule else []
    agent_values = {}
    for row in artifact:
        sys = row.get('system', '').strip()
        val_str = row.get('delta_EFM_meV', '')
        if not val_str:
            continue
        try:
            val = float(val_str)
        except:
            return 0.0
        agent_values[sys] = val
    passed_tol = 0
    for sys, gold in gold_map.items():
        if sys in agent_values and abs(agent_values[sys] - gold) <= tol_map.get(sys, 15):
            passed_tol += 1
    # ordering check
    if expected_order:
        filtered = {s: agent_values[s] for s in expected_order if s in agent_values}
        if len(filtered) == len(expected_order):
            sorted_filtered = sorted(filtered, key=lambda s: filtered[s])
            ordering_correct = (sorted_filtered == expected_order)
        else:
            ordering_correct = False
    else:
        ordering_correct = True  # no ordering rule
    tol_score = (passed_tol / max(len(gold_map), 1)) * 0.8
    order_score = 0.2 if ordering_correct else 0.0
    return tol_score + order_score


# === block: score_2 (check id='magnetic_moments') ===
def score_2(artifact, step, ctx):
    targets = step.get('targets', {})
    tol = step.get('tol', 0.3)
    total_checks = 0
    passed = 0
    for row in artifact:
        sys = row.get('system', '').strip()
        if sys not in targets:
            continue
        sys_targets = targets[sys]
        for field, gold in sys_targets.items():
            total_checks += 1
            try:
                val = float(row.get(field, ''))
            except:
                continue
            if abs(val - gold) <= tol:
                passed += 1
    if total_checks == 0:
        return 0.0
    return passed / total_checks


_SCORERS = {
    'shape_gate': score_0,
    'delta_EFM': score_1,
    'magnetic_moments': score_2,
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