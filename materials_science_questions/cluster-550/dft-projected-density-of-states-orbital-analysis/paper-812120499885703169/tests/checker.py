import os
import json
import csv

# === author imports / helpers ===
import csv, math, os


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


# === block: score_0 (check id='band_gap') ===
def score_0(artifact, step, ctx):
    gamma_row = None
    d_row = None
    for row in artifact:
        lbl = row.get('kpoint_label', '')
        if lbl == 'Gamma' and gamma_row is None:
            gamma_row = row
        if lbl == 'D' and d_row is None:
            d_row = row
    if gamma_row is None or d_row is None:
        return 0.0

    def get_band_energies(row):
        energies = []
        for key in row:
            if key.startswith('band_'):
                try:
                    energies.append(float(row[key]))
                except ValueError:
                    pass
        return energies

    gamma_energies = get_band_energies(gamma_row)
    d_energies = get_band_energies(d_row)
    if not gamma_energies or not d_energies:
        return 0.0

    vbm_energies = [e for e in gamma_energies if e <= 0.0]
    if not vbm_energies:
        return 0.0
    vbm = max(vbm_energies)

    cbm_energies = [e for e in d_energies if e > 0.0]
    if not cbm_energies:
        return 0.0
    cbm = min(cbm_energies)

    gap = cbm - vbm
    target = float(step.get('target', 4.65))
    tolerance = float(step.get('tolerance', 0.2))
    if abs(gap - target) <= tolerance:
        return 1.0
    else:
        return 0.0


# === block: score_1 (check id='dielectric_peak') ===
def score_1(artifact, step, ctx):
    energies = []
    eps2 = []
    for row in artifact:
        try:
            e = float(row['energy'])
            x = float(row['epsilon2_xx'])
        except (ValueError, KeyError):
            continue
        if 5.0 <= e <= 10.0:
            energies.append(e)
            eps2.append(x)
    if not energies:
        return 0.0
    peak_idx = max(range(len(eps2)), key=lambda i: eps2[i])
    peak_energy = energies[peak_idx]
    target = float(step['target'])
    tol = float(step['tolerance'])
    if abs(peak_energy - target) <= tol:
        return 1.0
    else:
        return 0.0


# === block: score_2 (check id='total_dos_structure') ===
def score_2(artifact, step, ctx):
    threshold = 0.01
    gap_start = 0.0
    gap_end = 4.65
    count_total = 0
    count_zero = 0
    for row in artifact:
        try:
            e = float(row['energy'])
            dos = float(row['total_dos'])
        except (ValueError, KeyError):
            continue
        if gap_start <= e <= gap_end:
            count_total += 1
            if dos < threshold:
                count_zero += 1
    if count_total == 0:
        return 0.0
    fraction = count_zero / count_total
    return 1.0 if fraction >= 0.9 else 0.0


# === block: score_3 (check id='projected_dos_structure') ===
def score_3(artifact, step, ctx):
    region_start = -0.5
    region_end = 0.0
    p_sum = 0.0
    total_sum = 0.0
    O_sum = 0.0
    total_elem_sum = 0.0
    for row in artifact:
        try:
            e = float(row['energy'])
            s = float(row['s_dos'])
            p = float(row['p_dos'])
            O = float(row['O_dos'])
            C = float(row['C_dos'])
            N = float(row['N_dos'])
            H = float(row['H_dos'])
            S = float(row['S_dos'])
        except (ValueError, KeyError):
            continue
        if region_start <= e <= region_end:
            total = s + p
            if total > 0:
                p_sum += p
                total_sum += total
            total_elem = O + C + N + H + S
            if total_elem > 0:
                O_sum += O
                total_elem_sum += total_elem
    if total_sum == 0 or total_elem_sum == 0:
        return 0.0
    p_fraction = p_sum / total_sum
    O_fraction = O_sum / total_elem_sum
    score = 0.0
    if p_fraction > 0.8:
        score += 0.5
    if O_fraction > 0.7:
        score += 0.5
    return score


_SCORERS = {
    'band_gap': score_0,
    'dielectric_peak': score_1,
    'total_dos_structure': score_2,
    'projected_dos_structure': score_3,
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
