import os
import json
import csv

# === author imports / helpers ===
import csv
import os
import math


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
    ctx = {}
    barrier_mev = None
    csv_path = os.path.join(outputs_dir, 'energy_vs_angle.csv')
    if os.path.exists(csv_path):
        with open(csv_path, newline='') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            if rows and 'angle_deg' in rows[0] and 'energy_eV' in rows[0]:
                energies = [float(r['energy_eV']) for r in rows if r['energy_eV'].strip()]
                if energies:
                    barrier_ev = max(energies) - min(energies)
                    barrier_mev = barrier_ev * 1000.0
    ctx['recomputed_barrier_mev'] = barrier_mev
    ctx['equilibrium_distance'] = None
    dist_path = os.path.join(outputs_dir, 'equilibrium_distance.txt')
    if os.path.exists(dist_path):
        with open(dist_path) as f:
            text = f.read().strip()
        try:
            ctx['equilibrium_distance'] = float(text)
        except ValueError:
            pass
    return ctx


# === block: score_0 (check id='optimize_geometry') ===
def score_0(artifact, step, ctx):
    d = ctx.get('equilibrium_distance')
    if d is None or not isinstance(d, (int, float)) or d <= 0:
        return 0.0
    target = step.get('target')
    if target is None:
        return 0.0
    tol = step.get('tolerance')
    if tol is None:
        return 0.0
    diff = abs(d - target)
    if diff <= tol:
        return 1.0
    return max(0.0, 1.0 - (diff - tol) / tol)


# === block: score_1 (check id='rotation_scan') ===
def score_1(artifact, step, ctx):
    barrier_mev = ctx.get('recomputed_barrier_mev')
    if barrier_mev is None:
        return 0.0
    threshold = 100.0
    decay = 200.0
    if barrier_mev <= threshold:
        return 1.0
    else:
        return max(0.0, 1.0 - (barrier_mev - threshold) / decay)


# === block: score_2 (check id='compute_barrier') ===
def score_2(artifact, step, ctx):
    barrier_mev = ctx.get('recomputed_barrier_mev')
    if barrier_mev is None:
        return 0.0
    artifact_text = artifact  # artifact is the loaded text from rotational_barrier.txt
    try:
        reported = float(artifact_text.strip())
    except (ValueError, TypeError):
        return 0.0
    diff = abs(reported - barrier_mev)
    tol = 1.0
    decay = 5.0
    if diff <= tol:
        return 1.0
    else:
        return max(0.0, 1.0 - (diff - tol) / decay)


_SCORERS = {
    'optimize_geometry': score_0,
    'rotation_scan': score_1,
    'compute_barrier': score_2,
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
