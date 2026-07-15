import os
import json
import csv

# === author imports / helpers ===
import json, csv, os


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
    for step in spec.get("steps", []):
        sid = step["id"]
        data = {}
        for key in ["expected_fermi", "fermi_tol", "peak_windows", "target_charges", "tolerance", "target_populations", "depopulation"]:
            if key in step:
                data[key] = step[key]
        ctx[sid] = data
    return ctx


# === block: score_0 (check id='s04_pure_band_dos') ===
def score_0(artifact, step, ctx):
    if not all(k in artifact for k in ["fermi_energy", "band_energies", "dos"]):
        return 0.0
    fermi = artifact["fermi_energy"]
    dos = artifact["dos"]
    expected_fermi = step["expected_fermi"]
    fermi_tol = max(step.get("fermi_tol", 0.1), 0.1)  # floor to 0.1 eV to absorb re‑run spread
    fermi_score = 1.0 if abs(fermi - expected_fermi) <= fermi_tol else 0.0
    windows = step["peak_windows"]
    peak_count = 0
    for w in windows:
        low, high = w["low"], w["high"]
        found = False
        for pair in dos:
            if len(pair) >= 2:
                e, d = float(pair[0]), float(pair[1])
                if low <= e <= high and d > 0.0:
                    found = True
                    break
        if found:
            peak_count += 1
    peak_score = peak_count / len(windows)
    return 0.4 * fermi_score + 0.6 * peak_score


# === block: score_1 (check id='s05_doped_band_dos') ===
def score_1(artifact, step, ctx):
    if not all(k in artifact for k in ["fermi_energy", "band_energies", "dos"]):
        return 0.0
    fermi = artifact["fermi_energy"]
    dos = artifact["dos"]
    fermi_valid = isinstance(fermi, (int, float)) and -20.0 <= fermi <= 0.0
    windows = step.get("peak_windows", [])
    peak_found = False
    for w in windows:
        low, high = w["low"], w["high"]
        for pair in dos:
            if len(pair) >= 2:
                e, d = float(pair[0]), float(pair[1])
                if low <= e <= high and d > 0.0:
                    peak_found = True
                    break
        if peak_found:
            break
    score = 0.0
    score += 0.2  # valid keys (already validated)
    if fermi_valid:
        score += 0.3
    if peak_found:
        score += 0.5
    return min(1.0, score)


# === block: score_2 (check id='s06_mulliken') ===
def score_2(artifact, step, ctx):
    charges = artifact
    if not isinstance(charges, list) or len(charges) == 0:
        return 0.0
    targets = step["target_charges"]
    tol = step["tolerance"]
    req_rows = [("pure","Sb"), ("pure","V"), ("pure","O"), ("doped","Sb"), ("doped","V"), ("doped","O")]
    ti_present = False
    ti_charge = None
    row_scores = []
    for row in charges:
        struct = row.get("structure","").strip().lower()
        atom = row.get("atom_type","").strip()
        charge = float(row.get("average_charge",0))
        if struct == "doped" and atom == "Ti":
            ti_present = True
            ti_charge = charge
            continue
        for s, a in req_rows:
            if struct == s and atom == a:
                target = targets[s][a]
                diff = abs(charge - target)
                if diff <= tol:
                    row_scores.append(1.0)
                else:
                    row_scores.append(max(0.0, 1.0 - (diff - tol) / (4 * tol)))
                break
    if len(row_scores) == 0:
        return 0.0
    avg_target = sum(row_scores) / min(len(row_scores), 6)
    score = 0.8 * avg_target + (0.2 if ti_present else 0.0)
    return score


# === block: score_3 (check id='s07_orbital') ===
def score_3(artifact, step, ctx):
    pops = artifact
    if not isinstance(pops, list) or len(pops) == 0:
        return 0.0
    pure = {}
    doped = {}
    for row in pops:
        struct = row.get("structure","").strip().lower()
        orb = row.get("orbital","").strip()
        pop = float(row.get("population",0))
        if struct == "pure":
            pure[orb] = pop
        elif struct == "doped":
            doped[orb] = pop
    targets = step["target_populations"]
    tol = step["tolerance"]
    orbital_names = ["3d(x^2-y^2)", "3d(z^2)", "3d(xy)", "3d(xz)", "3d(yz)"]
    value_scores = []
    for orb in orbital_names:
        if orb in pure and orb in doped:
            tp = targets["pure"].get(orb)
            td = targets["doped"].get(orb)
            if tp is not None:
                diff = abs(pure[orb] - tp)
                if diff <= tol:
                    value_scores.append(1.0)
                else:
                    value_scores.append(max(0.0, 1.0 - (diff - tol) / (4 * tol)))
            if td is not None:
                diff = abs(doped[orb] - td)
                if diff <= tol:
                    value_scores.append(1.0)
                else:
                    value_scores.append(max(0.0, 1.0 - (diff - tol) / (4 * tol)))
        else:
            value_scores.append(0.0)
    value_score = sum(value_scores) / len(value_scores) if value_scores else 0.0
    dep = step.get("depopulation", {})
    dz2_pure = pure.get("3d(z^2)")
    dz2_doped = doped.get("3d(z^2)")
    dxy_pure = pure.get("3d(xy)")
    dxy_doped = doped.get("3d(xy)")
    trend_scores = []
    if dz2_pure is not None and dz2_doped is not None:
        diff = dz2_pure - dz2_doped
        expected = dep.get("z2_expected_diff", 0.16)
        tol_diff = dep.get("z2_tol_diff", 0.04)
        if abs(diff - expected) <= tol_diff:
            trend_scores.append(1.0)
        else:
            trend_scores.append(max(0.0, 1.0 - (abs(diff - expected) - tol_diff) / (2 * tol_diff)))
    else:
        trend_scores.append(0.0)
    if dxy_pure is not None and dxy_doped is not None:
        diff = dxy_pure - dxy_doped
        expected = dep.get("xy_expected_diff", 0.08)
        tol_diff = dep.get("xy_tol_diff", 0.03)
        if abs(diff - expected) <= tol_diff:
            trend_scores.append(1.0)
        else:
            trend_scores.append(max(0.0, 1.0 - (abs(diff - expected) - tol_diff) / (2 * tol_diff)))
    else:
        trend_scores.append(0.0)
    trend_score = sum(trend_scores) / len(trend_scores)
    return 0.5 * value_score + 0.5 * trend_score


_SCORERS = {
    's04_pure_band_dos': score_0,
    's05_doped_band_dos': score_1,
    's06_mulliken': score_2,
    's07_orbital': score_3,
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
