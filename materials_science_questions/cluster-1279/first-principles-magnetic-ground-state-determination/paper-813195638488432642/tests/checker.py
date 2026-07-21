import os
import json
import csv

# === author imports / helpers ===
import csv, os, math


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
    moments_path = os.path.join(outputs_dir, 'magnetic_moments.csv')
    total_moment = 0.0
    with open(moments_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            total_moment += float(row['spin_moment'])
    total_moment_fu = total_moment / 2.0
    return {'total_moment_fu': total_moment_fu}


# === block: score_0 (check id='total_energies') ===
def score_0(artifact, step, ctx):
    fim_energy = None
    min_energy = float('inf')
    for row in artifact:
        energy = float(row['total_energy'])
        if energy < min_energy:
            min_energy = energy
        config = row['magnetic_configuration'].strip().lower()
        if config == 'fim':
            fim_energy = energy
    if fim_energy is not None and abs(fim_energy - min_energy) < 1e-9:
        return 1.0
    else:
        return 0.0


# === block: score_1 (check id='magnetic_moments') ===
def score_1(artifact, step, ctx):
    total_moment = sum(float(row['spin_moment']) for row in artifact)
    total_moment_fu = total_moment / 2.0
    target = step.get('target', 1.667)
    tol = step.get('tolerance_abs', 0.2)
    if abs(total_moment_fu - target) <= tol:
        return 1.0
    else:
        return 0.0


# === block: score_2 (check id='total_dos') ===
def score_2(artifact, step, ctx):
    energies = []
    ups = []
    downs = []
    if isinstance(artifact, str):
        # parse plain-text .dat file
        lines = [ln.strip() for ln in artifact.strip().splitlines() if ln.strip() and not ln.strip().startswith('#')]
        for line in lines:
            parts = line.split()
            if len(parts) < 3:
                continue
            try:
                e, u, d = float(parts[0]), float(parts[1]), float(parts[2])
                energies.append(e)
                ups.append(u)
                downs.append(d)
            except ValueError:
                # skip header or comment lines
                continue
    else:
        for row in artifact:
            energies.append(float(row['energy']))
            ups.append(float(row['spin_up_dos']))
            downs.append(float(row['spin_down_dos']))
    if not energies:
        return 0.0
    sorted_idx = sorted(range(len(energies)), key=lambda i: energies[i])
    energies = [energies[i] for i in sorted_idx]
    ups = [ups[i] for i in sorted_idx]
    downs = [downs[i] for i in sorted_idx]
    net_moment = 0.0
    for i in range(len(energies)):
        if energies[i] > 0.0:
            break
        if i == 0:
            de = (energies[i+1] - energies[i]) if len(energies) > 1 else 1.0
        else:
            de = energies[i] - energies[i-1]
        net_moment += (ups[i] - downs[i]) * de
    tol = step.get('tolerance_abs', 0.3)
    total_moment_fu = ctx['total_moment_fu']
    if abs(net_moment - total_moment_fu) <= tol:
        return 1.0
    else:
        return 0.0


_SCORERS = {
    'total_energies': score_0,
    'magnetic_moments': score_1,
    'total_dos': score_2,
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
