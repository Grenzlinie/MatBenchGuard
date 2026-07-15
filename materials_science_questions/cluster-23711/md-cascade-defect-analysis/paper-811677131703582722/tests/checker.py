import os
import json
import csv

# === author imports / helpers ===
import json, math


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


# === block: score_0 (check id='mixing_densification_results.json_check') ===
def score_0(artifact, step, ctx):
    gold = step.get('gold', {})
    tolerances = step.get('tolerances', {})
    trend_checks = step.get('trend_checks', [])
    rho_late_times = step.get('rho_late_times', [2.0, 6.0, 12.0])

    if not isinstance(artifact, dict):
        return 0.0

    unreg = artifact.get('unregistered_low_barrier')
    reg = artifact.get('registered_low_barrier')
    if not isinstance(unreg, list) or not isinstance(reg, list):
        return 0.0

    # index entries by time_ps (rounded to nearest 0.1)
    def build_index(entries):
        idx = {}
        for e in entries:
            try:
                t = float(e['time_ps'])
                # round to 1 decimal to match 0.1,2.0 etc.
                key = round(t, 1)
                idx[key] = e
            except (ValueError, TypeError, KeyError):
                continue
        return idx

    unreg_idx = build_index(unreg)
    reg_idx = build_index(reg)

    times = [0.1, 2.0, 6.0, 12.0]
    tol_m_abs = tolerances.get('m', {}).get('abs_min', 1.0)
    tol_m_rel = tolerances.get('m', {}).get('rel_frac', 0.2)
    tol_rho = tolerances.get('rho', {}).get('abs_tol', 0.2)

    sub_checks_passed = 0
    total_sub_checks = 0

    for interface_name, idx, gold_dict in [
        ('unregistered', unreg_idx, gold.get('unregistered_low_barrier', {})),
        ('registered', reg_idx, gold.get('registered_low_barrier', {}))
    ]:
        for t in times:
            key = round(t, 1)
            gold_entry = gold_dict.get(str(key))  # gold keys are strings '0.1' etc.
            if gold_entry is None:
                continue
            actual = idx.get(key)
            if actual is None:
                # missing entry -> fail both m and rho checks
                total_sub_checks += 2
                continue
            for field in ['m', 'rho']:
                gold_val = gold_entry.get(field)
                try:
                    actual_val = float(actual.get('m_percent' if field == 'm' else 'rho'))
                except (TypeError, ValueError):
                    total_sub_checks += 1
                    continue
                total_sub_checks += 1
                if field == 'm':
                    allowed = max(tol_m_abs, tol_m_rel * abs(gold_val))
                    if abs(actual_val - gold_val) <= allowed:
                        sub_checks_passed += 1
                else:  # rho
                    if abs(actual_val - gold_val) <= tol_rho:
                        sub_checks_passed += 1

    # trend checks
    for tc in trend_checks:
        t = tc['time']
        field = tc.get('field', 'm')
        key = round(t, 1)
        unreg_e = unreg_idx.get(key)
        reg_e = reg_idx.get(key)
        total_sub_checks += 1
        if unreg_e is None or reg_e is None:
            continue
        try:
            unreg_val = float(unreg_e.get('m_percent' if field == 'm' else 'rho'))
            reg_val = float(reg_e.get('m_percent' if field == 'm' else 'rho'))
            if reg_val > unreg_val:
                sub_checks_passed += 1
        except (ValueError, TypeError):
            continue

    # rho >= 1 at late times: 2.0, 6.0, 12.0
    for t in rho_late_times:
        key = round(t, 1)
        unreg_e = unreg_idx.get(key)
        reg_e = reg_idx.get(key)
        for e in [unreg_e, reg_e]:
            if e is None:
                total_sub_checks += 1
                continue
            total_sub_checks += 1
            try:
                val = float(e.get('rho'))
                if val >= 1.0:
                    sub_checks_passed += 1
            except (ValueError, TypeError):
                continue

    if total_sub_checks == 0:
        return 0.0
    return min(1.0, sub_checks_passed / total_sub_checks)


_SCORERS = {
    'mixing_densification_results.json_check': score_0,
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
