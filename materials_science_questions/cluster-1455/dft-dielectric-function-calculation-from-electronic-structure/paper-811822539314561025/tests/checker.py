import os
import json
import csv

# === author imports / helpers ===
import os, json, csv, math


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


# === block: score_0 (check id='undoped_check') ===
def score_0(artifact, step, ctx):
    energies = [float(r['energy_eV']) for r in artifact]
    eps1s = [float(r['epsilon1']) for r in artifact]
    eps2s = [float(r['epsilon2']) for r in artifact]
    max_eps2 = max(eps2s)
    idx = eps2s.index(max_eps2)
    peak_energy = energies[idx]
    min_energy = min(energies)
    idx_low = energies.index(min_energy)
    eps1_0 = eps1s[idx_low]

    results_path = '/app/outputs/results.json'
    consistency = 0.0
    if os.path.exists(results_path):
        with open(results_path) as f:
            res = json.load(f)
        und = res.get('undoped', {})
        try:
            r_eps2 = float(und.get('epsilon2_peak', max_eps2+9999))
            r_energy = float(und.get('peak_energy_eV', peak_energy+9999))
            r_eps1 = float(und.get('epsilon1_0', eps1_0+9999))
            if abs(max_eps2 - r_eps2) <= 0.01*abs(r_eps2)+1e-6:
                consistency += 1/3
            if abs(peak_energy - r_energy) <= 0.01:
                consistency += 1/3
            if abs(eps1_0 - r_eps1) <= 0.01*abs(r_eps1)+1e-6:
                consistency += 1/3
        except Exception:
            pass

    target = step.get('target', {})
    tol = step.get('tolerances', {})
    t_eps2 = float(target.get('epsilon2_peak', 0))
    tol_eps2 = float(tol.get('epsilon2_peak', 0.2))
    t_energy = float(target.get('peak_energy_eV', 0))
    tol_energy = float(tol.get('peak_energy_eV', 0.2))
    t_eps1 = float(target.get('epsilon1_0', 0))
    tol_eps1 = float(tol.get('epsilon1_0', 0.2))

    num = 0.0
    if t_eps2 > 0:
        if abs(max_eps2 - t_eps2) / t_eps2 <= tol_eps2:
            num += 1/3
    else:
        num += 1/3
    if abs(peak_energy - t_energy) <= tol_energy:
        num += 1/3
    if t_eps1 > 0:
        if abs(eps1_0 - t_eps1) / t_eps1 <= tol_eps1:
            num += 1/3
    else:
        num += 1/3

    final = 0.8*num + 0.2*consistency
    return min(1.0, final)


# === block: score_1 (check id='Ga_check') ===
def score_1(artifact, step, ctx):
    energies = [float(r['energy_eV']) for r in artifact]
    eps1s = [float(r['epsilon1']) for r in artifact]
    eps2s = [float(r['epsilon2']) for r in artifact]
    max_eps2 = max(eps2s)
    idx = eps2s.index(max_eps2)
    peak_energy = energies[idx]
    min_energy = min(energies)
    idx_low = energies.index(min_energy)
    eps1_0 = eps1s[idx_low]

    results_path = '/app/outputs/results.json'
    consistency = 0.0
    if os.path.exists(results_path):
        with open(results_path) as f:
            res = json.load(f)
        ga = res.get('Ga', {})
        try:
            r_eps2 = float(ga.get('epsilon2_peak', max_eps2+9999))
            r_energy = float(ga.get('peak_energy_eV', peak_energy+9999))
            r_eps1 = float(ga.get('epsilon1_0', eps1_0+9999))
            if abs(max_eps2 - r_eps2) <= 0.01*abs(r_eps2)+1e-6:
                consistency += 1/3
            if abs(peak_energy - r_energy) <= 0.01:
                consistency += 1/3
            if abs(eps1_0 - r_eps1) <= 0.01*abs(r_eps1)+1e-6:
                consistency += 1/3
        except Exception:
            pass

    target = step.get('target', {})
    tol = step.get('tolerances', {})
    t_eps2 = float(target.get('epsilon2_peak', 0))
    tol_eps2 = float(tol.get('epsilon2_peak', 0.2))
    t_energy = float(target.get('peak_energy_eV', 0))
    tol_energy = float(tol.get('peak_energy_eV', 0.2))
    t_eps1 = float(target.get('epsilon1_0', 0))
    tol_eps1 = float(tol.get('epsilon1_0', 0.2))

    num = 0.0
    if t_eps2 > 0:
        if abs(max_eps2 - t_eps2) / t_eps2 <= tol_eps2:
            num += 1/3
    else:
        num += 1/3
    if abs(peak_energy - t_energy) <= tol_energy:
        num += 1/3
    if t_eps1 > 0:
        if abs(eps1_0 - t_eps1) / t_eps1 <= tol_eps1:
            num += 1/3
    else:
        num += 1/3

    final = 0.8*num + 0.2*consistency
    return min(1.0, final)


# === block: score_2 (check id='As_check') ===
def score_2(artifact, step, ctx):
    energies = [float(r['energy_eV']) for r in artifact]
    eps1s = [float(r['epsilon1']) for r in artifact]
    eps2s = [float(r['epsilon2']) for r in artifact]
    max_eps2 = max(eps2s)
    idx = eps2s.index(max_eps2)
    peak_energy = energies[idx]
    min_energy = min(energies)
    idx_low = energies.index(min_energy)
    eps1_0 = eps1s[idx_low]

    results_path = '/app/outputs/results.json'
    consistency = 0.0
    if os.path.exists(results_path):
        with open(results_path) as f:
            res = json.load(f)
        as_ = res.get('As', {})
        try:
            r_eps2 = float(as_.get('epsilon2_peak', max_eps2+9999))
            r_energy = float(as_.get('peak_energy_eV', peak_energy+9999))
            r_eps1 = float(as_.get('epsilon1_0', eps1_0+9999))
            if abs(max_eps2 - r_eps2) <= 0.01*abs(r_eps2)+1e-6:
                consistency += 1/3
            if abs(peak_energy - r_energy) <= 0.01:
                consistency += 1/3
            if abs(eps1_0 - r_eps1) <= 0.01*abs(r_eps1)+1e-6:
                consistency += 1/3
        except Exception:
            pass

    target = step.get('target', {})
    tol = step.get('tolerances', {})
    t_eps2 = float(target.get('epsilon2_peak', 0))
    tol_eps2 = float(tol.get('epsilon2_peak', 0.2))
    t_energy = float(target.get('peak_energy_eV', 0))
    tol_energy = float(tol.get('peak_energy_eV', 0.2))
    t_eps1 = float(target.get('epsilon1_0', 0))
    tol_eps1 = float(tol.get('epsilon1_0', 0.2))

    num = 0.0
    if t_eps2 > 0:
        if abs(max_eps2 - t_eps2) / t_eps2 <= tol_eps2:
            num += 1/3
    else:
        num += 1/3
    if abs(peak_energy - t_energy) <= tol_energy:
        num += 1/3
    if t_eps1 > 0:
        if abs(eps1_0 - t_eps1) / t_eps1 <= tol_eps1:
            num += 1/3
    else:
        num += 1/3

    final = 0.8*num + 0.2*consistency
    return min(1.0, final)


# === block: score_3 (check id='ordering_metallicity') ===
def score_3(artifact, step, ctx):
    import csv

    def get_peak(path):
        if not os.path.exists(path):
            return None
        with open(path) as f:
            reader = csv.DictReader(f)
            best = None
            for row in reader:
                e2 = float(row['epsilon2'])
                if best is None or e2 > best:
                    best = e2
            return best

    undoped_peak = get_peak('/app/outputs/undoped_dielectric.csv')
    ga_peak = get_peak('/app/outputs/Ga_dielectric.csv')
    as_peak = get_peak('/app/outputs/As_dielectric.csv')

    order_score = 0.0
    if undoped_peak is not None and ga_peak is not None and as_peak is not None:
        if ga_peak > as_peak > undoped_peak:
            order_score = 1.0
    else:
        order_score = 0.0

    results_path = '/app/outputs/results.json'
    metal_score = 0.0
    if os.path.exists(results_path):
        with open(results_path) as f:
            res = json.load(f)
        ga = res.get('Ga', {})
        band_gap = float(ga.get('band_gap_eV', 999))
        if abs(band_gap) < 0.01:
            metal_score = 1.0
    else:
        metal_score = 0.0

    return 0.8 * order_score + 0.2 * metal_score


_SCORERS = {
    'undoped_check': score_0,
    'Ga_check': score_1,
    'As_check': score_2,
    'ordering_metallicity': score_3,
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
