import os
import json
import csv

# === author imports / helpers ===
import os, json, math

def cubic_vrh(C11, C12, C44):
    B_v = (C11 + 2*C12) / 3.0
    G_v = (C11 - C12 + 3*C44) / 5.0
    B_r = B_v
    G_r = 5.0 * (C11 - C12) * C44 / (4.0*C44 + 3.0*(C11 - C12))
    B = (B_v + B_r) / 2.0
    G = (G_v + G_r) / 2.0
    return B, G

def orthorhombic_vrh(C11, C22, C33, C44, C55, C66, C12, C13, C23):
    B_v = (C11 + C22 + C33 + 2.0*(C12 + C13 + C23)) / 9.0
    G_v = (C11 + C22 + C33 + 3.0*(C44 + C55 + C66) - (C12 + C13 + C23)) / 15.0
    # Reuss compliance matrix inversion
    M = [[C11, C12, C13, 0, 0, 0],
         [C12, C22, C23, 0, 0, 0],
         [C13, C23, C33, 0, 0, 0],
         [0, 0, 0, C44, 0, 0],
         [0, 0, 0, 0, C55, 0],
         [0, 0, 0, 0, 0, C66]]
    # compute S by inverting M (only upper left 3x3 + diag)
    det = C11*C22*C33 + 2*C12*C13*C23 - C11*C23**2 - C22*C13**2 - C33*C12**2
    if det == 0:
        return B_v, G_v
    S11 = (C22*C33 - C23**2) / det
    S22 = (C11*C33 - C13**2) / det
    S33 = (C11*C22 - C12**2) / det
    S12 = (C13*C23 - C12*C33) / det
    S13 = (C12*C23 - C13*C22) / det
    S23 = (C12*C13 - C23*C11) / det
    S44 = 1.0/C44 if C44!=0 else 0
    S55 = 1.0/C55 if C55!=0 else 0
    S66 = 1.0/C66 if C66!=0 else 0
    B_r = 1.0 / (S11 + S22 + S33 + 2.0*(S12 + S13 + S23))
    G_r = 15.0 / (4.0*(S11+S22+S33) - 4.0*(S12+S13+S23) + 3.0*(S44+S55+S66))
    B = (B_v + B_r) / 2.0
    G = (G_v + G_r) / 2.0
    return B, G

def trigonal_vrh(C11, C12, C13, C14, C33, C44):
    C66 = (C11 - C12) / 2.0
    B_v = (2.0*(C11 + C12) + 4.0*C13 + C33) / 9.0
    G_v = (C11 + C12 + 2.0*C33 - 4.0*C13 + 12.0*C44 + 12.0*C66) / 30.0
    # Reuss
    M = [[C11, C12, C13, C14, 0, 0],
         [C12, C11, C13, -C14, 0, 0],
         [C13, C13, C33, 0, 0, 0],
         [C14, -C14, 0, C44, 0, 0],
         [0, 0, 0, 0, C44, C14],
         [0, 0, 0, 0, C14, C66]]
    # invert using numpy not allowed, we use formulas
    det_a = (C11 - C12)*((C11 + C12)*C33 - 2*C13**2) - 2*C14**2*C33
    if det_a == 0:
        return B_v, G_v
    # compliance matrix elements
    S11 = 0.5*((C11*C33 - C13**2)/(C11 - C12) + C33*C14**2/det_a)
    S12 = 0.5*((C12*C33 - C13**2)/(C11 - C12) - C33*C14**2/det_a)
    S13 = -C13*C33/det_a
    S14 = -C14*C33/det_a
    S33 = ((C11 + C12)*C33 - 2*C13**2) / det_a
    S44 = C66 / (C44*C66 - C14**2)
    S66 = C44 / (C44*C66 - C14**2)
    S15 = 0  # not needed
    B_r = 1.0 / (2.0*S11 + 2.0*S12 + 4.0*S13 + S33)
    G_r = 15.0 / (4.0*(2.0*S11 - S12 + S33 - 2.0*S13) + 3.0*(2.0*S44 + S66))
    B = (B_v + B_r) / 2.0
    G = (G_v + G_r) / 2.0
    return B, G


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
    gold = next(step['params']['gold'] for step in spec['steps'] if step['id'] == 'phase_accuracy')
    tolerances = next(step['params']['tolerances'] for step in spec['steps'] if step['id'] == 'phase_accuracy')
    return {'gold': gold, 'tolerances': tolerances}


# === block: score_0 (check id='phase_accuracy') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold = ctx['gold']
        tolerances = ctx['tolerances']
        phases_data = artifact.get('phases', [])
        if not phases_data:
            return 0.0

        # phase to cij mapping based on known paper ordering
        phase_cij_map = {
            'V': {'names': ['C11', 'C12', 'C44'], 'system': 'cubic'},
            'V2C': {'names': ['C11','C22','C33','C44','C55','C66','C12','C13','C23'], 'system': 'orthorhombic'},
            'V4C3': {'names': ['C11','C33','C44','C12','C23'], 'system': 'trigonal'},
            'P31-V6C5': {'names': ['C11','C33','C44','C12','C13'], 'system': 'trigonal'},
            'V8C7': {'names': ['C11', 'C12', 'C44'], 'system': 'cubic'},
            'VC': {'names': ['C11', 'C12', 'C44'], 'system': 'cubic'}
        }

        def calc_properties(phase_name, cij):
            info = phase_cij_map.get(phase_name)
            if info is None:
                return None
            names = info['names']
            sys = info['system']
            if len(cij) < len(names):
                return None
            vals = {name: cij[i] for i, name in enumerate(names)}
            try:
                if sys == 'cubic':
                    B, G = cubic_vrh(vals['C11'], vals.get('C12', 0), vals.get('C44', 0))
                elif sys == 'orthorhombic':
                    B, G = orthorhombic_vrh(
                        vals['C11'], vals['C22'], vals['C33'],
                        vals['C44'], vals['C55'], vals['C66'],
                        vals['C12'], vals['C13'], vals['C23'])
                elif sys == 'trigonal':
                    C11 = vals['C11']
                    C33 = vals['C33']
                    C44 = vals['C44']
                    C12 = vals.get('C12', 0)
                    C13 = vals.get('C13', vals.get('C23', 0))  # fallback
                    C14 = vals.get('C14', 0)
                    B, G = trigonal_vrh(C11, C12, C13, C14, C33, C44)
                else:
                    return None
                if B <= 0 or G <= 0:
                    return None
                E = 9.0 * B * G / (3.0 * B + G)
                v = (3.0 * B - 2.0 * G) / (2.0 * (3.0 * B + G))
                Hv = 2.0 * ((G/B)**2 * G)**0.583 - 3.0
                return {'B': B, 'G': G, 'E': E, 'v': v, 'Hv': Hv}
            except Exception:
                return None

        phase_scores = []
        for phase in phases_data:
            name = phase.get('phase_name', '')
            cij = phase.get('Cij', [])
            props = calc_properties(name, cij)
            if props is None:
                phase_scores.append(0.0)
                continue
            gold_phase = gold.get(name)
            if gold_phase is None:
                phase_scores.append(0.0)
                continue
            prop_scores = []
            for prop, tol in tolerances.items():
                g = gold_phase.get(prop)
                if g is None:
                    continue
                pval = props.get(prop)
                if pval is None:
                    prop_scores.append(0.0)
                    continue
                if prop == 'v':
                    err = abs(pval - g)
                    if err <= tol:
                        prop_scores.append(1.0)
                    else:
                        prop_scores.append(max(0.0, 1.0 - err / (tol*2)))
                else:
                    base = max(abs(g), 1e-6)
                    err_ratio = abs(pval - g) / base
                    if err_ratio <= tol:
                        prop_scores.append(1.0)
                    else:
                        prop_scores.append(max(0.0, 1.0 - err_ratio / (tol*2)))
            if prop_scores:
                phase_scores.append(sum(prop_scores)/len(prop_scores))
            else:
                phase_scores.append(0.0)

        if not phase_scores:
            return 0.0
        return sum(phase_scores) / len(phase_scores)


# === block: score_1 (check id='monotonic_trend') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        order = step['params']['order']
        prop_keys = step['params']['properties']
        phases_data = artifact.get('phases', [])
        if not phases_data:
            return 0.0
        name_to_data = {p.get('phase_name', ''): p for p in phases_data}
        trend_ok = True
        for prop in prop_keys:
            vals = []
            for pname in order:
                p = name_to_data.get(pname)
                if p is None or prop not in p:
                    trend_ok = False
                    vals.clear()
                    break
                vals.append(float(p[prop]))
            if len(vals) != len(order):
                trend_ok = False
                break
            # check strictly increasing
            for i in range(1, len(vals)):
                if vals[i] <= vals[i-1]:
                    trend_ok = False
                    break
            if not trend_ok:
                break
        if trend_ok:
            return 1.0
        # partial: check if at least one property monotonic
        for prop in prop_keys:
            vals = []
            for pname in order:
                p = name_to_data.get(pname)
                if p is None or prop not in p:
                    vals.clear()
                    break
                vals.append(float(p[prop]))
            if len(vals) != len(order):
                continue
            if all(vals[i] > vals[i-1] for i in range(1, len(vals))):
                return 0.5
        return 0.0


_SCORERS = {
    'phase_accuracy': score_0,
    'monotonic_trend': score_1,
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
