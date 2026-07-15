import os
import json
import csv

# === author imports / helpers ===
import re


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


# === block: score_0 (check id='step_02_tddft_uvvis') ===
def score_0(artifact, step, ctx):
    gold_peaks = [(194.5, 0.574, [('HOMO-4','LUMO'),('40','45'),('42','55'),('43','54')]),
                     (224.7, 0.047, [('HOMO','LUMO+16'),('42','61')])]
    if not artifact or len(artifact) < 2:
        return 0.0

    # find the two rows with highest oscillator strength
    sorted_rows = sorted(artifact, key=lambda r: float(r.get('oscillator_strength', 0)), reverse=True)
    # we check the top two
    peak_score = 0.0
    label_score = 0.0
    checked_peaks = set()
    for row in sorted_rows[:2]:
        wl = float(row.get('wavelength_nm', 0))
        f = float(row.get('oscillator_strength', 0))
        label = row.get('transition_label', '')
        for gw, gf, patterns in gold_peaks:
            if gw in checked_peaks:
                continue
            if abs(wl - gw) <= 5.0:
                # wavelength match
                if abs(f - gf) / gf <= 0.20:
                    peak_score += 0.5
                else:
                    peak_score += 0.25  # wavelength ok but f off
                # label check: at least one pattern matches
                found = False
                for (a,b) in patterns:
                    if a in label and b in label:
                        found = True
                        break
                if found:
                    label_score += 0.5
                else:
                    label_score += 0.0
                checked_peaks.add(gw)
                break
        else:
            # no wavelength match within 5 nm
            peak_score += 0.0

    # scale to [0,1]
    peak_score = min(1.0, peak_score)
    label_score = min(1.0, label_score)
    return 0.1 + 0.6 * peak_score + 0.3 * label_score


# === block: score_1 (check id='step_03_nbo_e2') ===
def score_1(artifact, step, ctx):
    if not artifact:
        return 0.0

    donation_ok = False
    back_donation_ok = False
    for row in artifact:
        donor = row.get('donor', '')
        acceptor = row.get('acceptor', '')
        e2 = float(row.get('E2_kcal_mol', 0))
        if 'Fe' in donor and 'd' in donor and 'LP*' in acceptor:
            if e2 > 100.0:
                donation_ok = True
        if 'C' in donor and 'Fe' in acceptor and e2 > 0:
            back_donation_ok = True

    score = 0.0
    if donation_ok:
        score += 0.6
    if back_donation_ok:
        score += 0.4
    return score


# === block: score_2 (check id='step_04_nbo_charges') ===
def score_2(artifact, step, ctx):
    if not artifact:
        return 0.0

    # expected charges and tolerances
    ref = {
        'fe': (0.212, 0.05),
        'c': (-0.247, 0.05),
        'h': (0.226, 0.05),
        'cp_ring': (-0.10, 0.03)
    }
    matched = {k: False for k in ref}
    for row in artifact:
        motif = row.get('atom_or_moiety', '').strip().lower()
        charge = float(row.get('natural_charge', 0))
        for key, (ref_val, tol) in ref.items():
            if matched[key]:
                continue
            if key == 'cp_ring':
                if 'cp' in motif and 'ring' in motif:
                    if abs(charge - ref_val) <= tol:
                        matched[key] = True
            else:
                if motif == key:
                    if abs(charge - ref_val) <= tol:
                        matched[key] = True

    return sum(0.25 for v in matched.values() if v)


_SCORERS = {
    'step_02_tddft_uvvis': score_0,
    'step_03_nbo_e2': score_1,
    'step_04_nbo_charges': score_2,
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
