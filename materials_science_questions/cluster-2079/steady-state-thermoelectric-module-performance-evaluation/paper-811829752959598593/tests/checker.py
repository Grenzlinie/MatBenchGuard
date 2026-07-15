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
    ref = spec.get('reference_power_curve')
    if not ref:
        return {'required_loads': [], 'ref_values': {}}
    required_loads = ref['required_loads']
    ref_values = {float(k): v for k, v in ref['values'].items()}
    return {'required_loads': required_loads, 'ref_values': ref_values}


# === block: score_0 (check id='step_03_scored') ===
def score_0(artifact, step, ctx):
    req_loads = ctx.get('required_loads', [])
    ref_vals = ctx.get('ref_values', {})

    agent_data = {}
    for row in artifact:
        try:
            r = float(row['load_resistance_ohm'])
            p = float(row['output_power_W'])
            agent_data[r] = p
        except Exception:
            continue

    # Collect paired data points at required loads
    pairs = []
    for rl in req_loads:
        ap = agent_data.get(rl)
        ep = ref_vals.get(rl)
        if ap is not None and ep is not None and ep != 0.0:
            pairs.append((ap, ep))

    if len(pairs) < 3:
        return 0.0

    # MAPE
    mape_sum = 0.0
    for ap, ep in pairs:
        mape_sum += abs(ap - ep) / ep
    mape = mape_sum / len(pairs)

    if mape <= 0.03:
        map_score = 1.0
    elif mape <= 0.05:
        map_score = 0.9
    elif mape <= 0.10:
        map_score = 0.7
    else:
        map_score = max(0.0, 0.7 - 2.0 * (mape - 0.10))

    # R² (coefficient of determination)
    ep_vals = [ep for _, ep in pairs]
    mean_ep = sum(ep_vals) / len(ep_vals)
    tss = sum((ep - mean_ep) ** 2 for ep in ep_vals)
    if tss == 0.0:
        r2 = 0.0
    else:
        rss = sum((ap - ep) ** 2 for ap, ep in pairs)
        r2 = 1.0 - rss / tss

    if r2 >= 0.98:
        r2_score = 1.0
    elif r2 >= 0.95:
        r2_score = 0.9
    elif r2 >= 0.90:
        r2_score = 0.7
    else:
        r2_score = max(0.0, (r2 - 0.85) / 0.15)

    return 0.5 * map_score + 0.5 * r2_score


_SCORERS = {
    'step_03_scored': score_0,
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
