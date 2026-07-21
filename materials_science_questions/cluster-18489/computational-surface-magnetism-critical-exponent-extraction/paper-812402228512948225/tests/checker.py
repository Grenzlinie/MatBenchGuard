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


# === block: score_0 (check id='step_03') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not rows or len(rows) < 2:
        return 0.0
    try:
        T = [float(r['temperature']) for r in rows]
        core = [float(r['core_mag']) for r in rows]
        surf = [float(r['surf_mag']) for r in rows]
        spec = [float(r['specific_heat']) for r in rows]
    except (KeyError, ValueError):
        return 0.0
    params = step.get('params', {})
    w1 = params.get('core_gt_surf_weight', 0.3)
    w2 = params.get('surface_low_weight', 0.3)
    w3 = params.get('peak_weight', 0.2)
    w4 = params.get('core_low_weight', 0.2)
    s1 = 1.0 if all(c > s for c, s in zip(core, surf)) else 0.0
    surf_low_max = params.get('surf_low_max', 0.2)
    core_drop_min = params.get('core_drop_min', 0.6)
    surf_low_idx = next((i for i, s in enumerate(surf) if s < surf_low_max), None)
    if surf_low_idx is not None:
        T_surf_low = T[surf_low_idx]
        core_drop_idx = next((i for i, c in enumerate(core) if c < core_drop_min), None)
        if core_drop_idx is None:
            s2 = 1.0
        else:
            s2 = 1.0 if T_surf_low < T[core_drop_idx] else 0.0
    else:
        s2 = 0.0
    s3 = 1.0 if max(spec) > 0 else 0.0
    core_high_min = params.get('core_high_min', 0.8)
    s4 = 1.0 if max(core) > core_high_min else 0.0
    return min(1.0, max(0.0, w1*s1 + w2*s2 + w3*s3 + w4*s4))


# === block: score_1 (check id='step_04') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not rows or len(rows) < 2:
        return 0.0
    try:
        bin_vals = [float(r['radial_bin']) for r in rows]
        mag = [float(r['local_mag']) for r in rows]
    except (KeyError, ValueError):
        return 0.0
    params = step.get('params', {})
    mono_weight = params.get('mono_weight', 0.7)
    last_weight = params.get('last_weight', 0.3)
    mono = all(mag[i] >= mag[i+1] - 1e-9 for i in range(len(mag)-1))
    s_mono = 1.0 if mono else 0.0
    s_last = 1.0 if mag[-1] < 0.9 else 0.0
    return mono_weight * s_mono + last_weight * s_last


_SCORERS = {
    'step_03': score_0,
    'step_04': score_1,
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
