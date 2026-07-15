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
    import csv, os
    ctx = {}
    am_path = os.path.join(outputs_dir, 'atomic_moments.csv')
    ctx['total_moment'] = None
    if os.path.exists(am_path):
        with open(am_path, newline='') as f:
            reader = csv.DictReader(f)
            total = 0.0
            for row in reader:
                total += float(row['magnetic_moment'])
            ctx['total_moment'] = total / 32.0
    dos_path = os.path.join(outputs_dir, 'dos_data.csv')
    ctx['band_gap'] = None
    if os.path.exists(dos_path):
        energies = []
        spin_up = []
        spin_down = []
        with open(dos_path, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                energies.append(float(row['energy']))
                spin_up.append(float(row['spin_up_dos']))
                spin_down.append(float(row['spin_down_dos']))
        total_dos = [u + d for u, d in zip(spin_up, spin_down)]
        max_tdos = max(total_dos) if total_dos else 0.0
        if max_tdos > 0:
            threshold = 0.001 * max_tdos
            below_fermi = [(e, t) for e, t in zip(energies, total_dos) if e < 0]
            above_fermi = [(e, t) for e, t in zip(energies, total_dos) if e > 0]
            vbm = max([e for e, t in below_fermi if t > threshold], default=None)
            cbm = min([e for e, t in above_fermi if t > threshold], default=None)
            if vbm is not None and cbm is not None:
                ctx['band_gap'] = cbm - vbm
    return ctx


# === block: score_0 (check id='step4') ===
def score_0(artifact, step, ctx):
    total_moment = sum(float(row['magnetic_moment']) for row in artifact) / 32.0
    target = step['target_moment_per_fu']
    tol = step['tolerance_moment']
    diff = abs(total_moment - target)
    moment_score = 1.0 if diff <= tol else max(0.0, 1.0 - (diff - tol) / tol)
    max_moment = step['max_moment_per_atom']
    total_atoms = len(artifact)
    if total_atoms == 0:
        deloc_score = 0.0
    else:
        exceed_count = sum(1 for row in artifact if float(row['magnetic_moment']) > max_moment)
        deloc_score = 1.0 - exceed_count / total_atoms
    return 0.7 * moment_score + 0.3 * deloc_score


# === block: score_1 (check id='step5') ===
def score_1(artifact, step, ctx):
    if artifact is None or ctx.get('total_moment') is None:
        return 0.0
    try:
        val = float(artifact.strip())
    except:
        return 0.0
    return 1.0 if abs(val - ctx['total_moment']) <= step['tolerance'] else 0.0


# === block: score_2 (check id='step6') ===
def score_2(artifact, step, ctx):
    energies = [float(row['energy']) for row in artifact]
    spin_up = [float(row['spin_up_dos']) for row in artifact]
    spin_down = [float(row['spin_down_dos']) for row in artifact]
    total_dos = [u + d for u, d in zip(spin_up, spin_down)]
    max_tdos = max(total_dos) if total_dos else 0.0
    gap_score = 0.0
    if max_tdos > 0:
        threshold = 0.001 * max_tdos
        below_fermi = [(e, t) for e, t in zip(energies, total_dos) if e < 0]
        above_fermi = [(e, t) for e, t in zip(energies, total_dos) if e > 0]
        vbm = max([e for e, t in below_fermi if t > threshold], default=None)
        cbm = min([e for e, t in above_fermi if t > threshold], default=None)
        if vbm is not None and cbm is not None:
            gap = cbm - vbm
            target_gap = step['target_band_gap']
            tol = step['tolerance_band_gap']
            diff = abs(gap - target_gap)
            if diff <= tol:
                gap_score = 1.0
            else:
                gap_score = max(0.0, 1.0 - (diff - tol) / tol)
    nonneg_score = 1.0 if (all(u >= 0 for u in spin_up) and all(d >= 0 for d in spin_down)) else 0.0
    min_e = min(energies)
    max_e = max(energies)
    range_score = 1.0 if (min_e <= -5.0 and max_e >= 5.0) else 0.0
    return 0.8 * gap_score + 0.1 * nonneg_score + 0.1 * range_score


# === block: score_3 (check id='step7') ===
def score_3(artifact, step, ctx):
    if artifact is None or ctx.get('band_gap') is None:
        return 0.0
    try:
        val = float(artifact.strip())
    except:
        return 0.0
    return 1.0 if abs(val - ctx['band_gap']) <= step['tolerance'] else 0.0


_SCORERS = {
    'step4': score_0,
    'step5': score_1,
    'step6': score_2,
    'step7': score_3,
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
