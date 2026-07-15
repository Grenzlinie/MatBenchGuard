import os
import json
import csv

# === author imports / helpers ===
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
    return {}


# === block: score_0 (check id='structural_params') ===
def score_0(artifact, step, ctx):
    gold = step['gold']
    tol = step['tolerances']
    a = artifact.get('lattice_constant_A')
    B = artifact.get('bulk_modulus_Mbar')
    Bp = artifact.get('bulk_modulus_pressure_derivative')
    if a is None or B is None or Bp is None:
        return 0.0
    def check(val, target, tol_val):
        diff = abs(val - target)
        if diff <= tol_val:
            return 1.0
        return max(0.0, 1.0 - (diff - tol_val) / tol_val)
    s_a = check(a, gold['lattice_constant_A'], tol['lattice_constant_A_tol'])
    s_B = check(B, gold['bulk_modulus_Mbar'], tol['bulk_modulus_Mbar_tol'])
    s_Bp = check(Bp, gold['bulk_modulus_pressure_derivative'], tol['bulk_modulus_pressure_derivative_tol'])
    return (s_a + s_B + s_Bp) / 3.0


# === block: score_1 (check id='band_structure') ===
def score_1(artifact, step, ctx):
    gold = step['gold']
    tol = step['tolerances']['gap_tol_eV']
    def find_point(target):
        min_dist = float('inf')
        best = None
        for item in artifact:
            kp = item['kpoint']
            dist = math.sqrt(sum((a-b)**2 for a,b in zip(kp, target)))
            if dist < min_dist:
                min_dist = dist
                best = item
        return best
    gamma_pt = find_point([0.0, 0.0, 0.0])
    L_pt = find_point([0.5, 0.5, 0.5])
    if gamma_pt is None or L_pt is None:
        return 0.0
    def get_vbm_cbm(eigenvals):
        vbm = max([e for e in eigenvals if e <= 0], default=-float('inf'))
        cbm = min([e for e in eigenvals if e >= 0], default=float('inf'))
        return vbm, cbm
    vbm_G, cbm_G = get_vbm_cbm(gamma_pt['eigenvalues'])
    vbm_L, cbm_L = get_vbm_cbm(L_pt['eigenvalues'])
    dir_gap_G = cbm_G - vbm_G
    ind_gap = cbm_G - vbm_L
    gold_dir = gold['direct_gap_Gamma_eV']
    gold_ind = gold['indirect_gap_eV']
    def score_gap(comp, target):
        diff = abs(comp - target)
        if diff <= tol:
            return 1.0
        return max(0.0, 1.0 - (diff - tol) / tol)
    s_dir = score_gap(dir_gap_G, gold_dir)
    s_ind = score_gap(ind_gap, gold_ind)
    return (s_dir + s_ind) / 2.0


# === block: score_2 (check id='phonon_dispersion') ===
def score_2(artifact, step, ctx):
    gold = step['gold']
    tol = step['tolerances']['freq_tol_THz']
    targets = {
        'Gamma': (0.0, 0.0, 0.0),
        'X': (1.0, 0.0, 0.0),
        'W': (1.0, 0.5, 0.0),
        'L': (0.5, 0.5, 0.5)
    }
    cm1_to_THz = 1.0 / 33.356
    def find_closest(target):
        min_dist = float('inf')
        best = None
        for item in artifact:
            kp = item['kpoint']
            dist = math.sqrt(sum((a-b)**2 for a,b in zip(kp, target)))
            if dist < min_dist:
                min_dist = dist
                best = item
        return best
    scores = []
    for name, coord in targets.items():
        pt = find_closest(coord)
        if pt is None:
            return 0.0
        freqs_cm1 = pt['frequencies_cm1']
        freqs_THz = [f * cm1_to_THz for f in freqs_cm1]
        freqs_THz.sort()
        gold_freqs = gold[name]
        if len(gold_freqs) != len(freqs_THz):
            return 0.0
        for comp, g in zip(freqs_THz, gold_freqs):
            diff = abs(comp - g)
            if diff <= tol:
                s = 1.0
            else:
                s = max(0.0, 1.0 - (diff - tol) / tol)
            scores.append(s)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


_SCORERS = {
    'structural_params': score_0,
    'band_structure': score_1,
    'phonon_dispersion': score_2,
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
