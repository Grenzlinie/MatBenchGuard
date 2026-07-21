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
    steps = spec.get("steps", [])
    step = None
    for s in steps:
        if s.get("id") == "step_01":
            step = s
            break
    if step is None:
        devices = {}
        d0_nm = 4000.0
        lambda_nm = 632.8
        tol = {}
    else:
        params = step.get("params", {})
        devices = params.get("devices", {})
        d0_nm = params.get("d0_nm", 4000.0)
        lambda_nm = params.get("lambda_nm", 632.8)
        tol = params.get("tolerances", {})
    return {
        "devices": devices,
        "d0_nm": d0_nm,
        "lambda_nm": lambda_nm,
        "tol": tol
    }


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    devices = ctx['devices']
    d0_nm = ctx['d0_nm']
    lambda_nm = ctx['lambda_nm']
    tol = ctx['tol']    # tolerances mapping, e.g. 'displacement', 'period_change', 'strain_percent', 'angular_urad'
    rows = artifact

    rows_by_device = {}
    for r in rows:
        did = str(r.get('device_id', '')).strip()
        if did in devices:
            rows_by_device[did] = r

    if len(rows_by_device) < 2:
        return 0.0

    scores = []
    for did, dev_params in devices.items():
        L_um = dev_params.get('L_um')
        if L_um is None:
            scores.append(0.0)
            continue
        row = rows_by_device.get(did)
        if not row:
            scores.append(0.0)
            continue
        try:
            agent_disp = float(row['membrane_displacement_nm'])
        except (ValueError, KeyError):
            scores.append(0.0)
            continue

        L_m = L_um * 1e-6
        agent_disp_m = agent_disp * 1e-9
        agent_strain = agent_disp_m / L_m
        agent_strain_pct = agent_strain * 100.0
        agent_pc = agent_strain * d0_nm
        agent_ang = (lambda_nm * agent_pc) / (d0_nm ** 2) * 1e6

        checks = []
        # displacement
        gold_disp = dev_params.get('gold_displacement_nm')
        if gold_disp is not None:
            td = tol.get('displacement', 0.05)
            if abs(gold_disp) < 1e-12:
                ok = abs(agent_disp - gold_disp) <= 0.1
            else:
                ok = abs(agent_disp - gold_disp) / abs(gold_disp) <= td
            checks.append(1.0 if ok else 0.0)

        # period change
        gold_pc = dev_params.get('gold_period_change_nm')
        if gold_pc is not None:
            tpc = tol.get('period_change', 0.05)
            if abs(gold_pc) < 1e-12:
                ok = abs(agent_pc - gold_pc) <= 0.01
            else:
                ok = abs(agent_pc - gold_pc) / abs(gold_pc) <= tpc
            checks.append(1.0 if ok else 0.0)

        # strain percent
        gold_strain = dev_params.get('gold_strain_percent')
        if gold_strain is not None:
            ts = tol.get('strain_percent', 0.05)
            if abs(gold_strain) < 1e-12:
                ok = abs(agent_strain_pct - gold_strain) <= 0.001
            else:
                ok = abs(agent_strain_pct - gold_strain) / abs(gold_strain) <= ts
            checks.append(1.0 if ok else 0.0)

        # angular change
        gold_ang = dev_params.get('gold_angular_urad')
        if gold_ang is not None:
            ta = tol.get('angular_urad', 0.10)
            if abs(gold_ang) < 1e-12:
                ok = abs(agent_ang - gold_ang) <= 0.1
            else:
                ok = abs(agent_ang - gold_ang) / abs(gold_ang) <= ta
            checks.append(1.0 if ok else 0.0)

        if checks:
            dev_score = sum(checks) / float(len(checks))
        else:
            dev_score = 0.0
        scores.append(dev_score)

    if not scores:
        return 0.0
    return sum(scores) / float(len(scores))


_SCORERS = {
    'step_01': score_0,
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
