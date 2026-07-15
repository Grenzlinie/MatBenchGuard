import os
import json
import csv

# === author imports / helpers ===
import math

def _rankdata(data):
    """Rank data, with average ranks for ties."""
    n = len(data)
    sorted_idx = sorted(range(n), key=lambda i: data[i])
    ranks = [0.0] * n
    i = 0
    while i < n:
        j = i
        while j < n and data[sorted_idx[j]] == data[sorted_idx[i]]:
            j += 1
        rank = (i + j - 1) / 2.0 + 1.0
        for k in range(i, j):
            ranks[sorted_idx[k]] = rank
        i = j
    return ranks

def _pearsonr(x, y):
    n = len(x)
    if n < 2:
        return 0.0, 1.0
    xm = sum(x) / n
    ym = sum(y) / n
    xd = [xi - xm for xi in x]
    yd = [yi - ym for yi in y]
    r_num = sum(xi * yi for xi, yi in zip(xd, yd))
    r_den = math.sqrt(sum(xi * xi for xi in xd) * sum(yi * yi for yi in yd))
    if r_den == 0:
        return 0.0, 1.0
    r = r_num / r_den
    return r, 0.0

def spearmanr(x, y):
    """Spearman rank correlation coefficient, returns (correlation, None)."""
    n = len(x)
    if n < 2:
        return 0.0, None
    rankx = _rankdata(x)
    ranky = _rankdata(y)
    r, _ = _pearsonr(rankx, ranky)
    return r, None


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
    outputs_dir = "/app/outputs"
    formation_path = os.path.join(outputs_dir, "oxygen_vacancy_formation_energies.csv")
    displacement_path = os.path.join(outputs_dir, "oxygen_vacancy_displacements.csv")

    with open(formation_path, newline='') as f:
        reader = csv.DictReader(f)
        ctx['formation'] = [row for row in reader]

    with open(displacement_path, newline='') as f:
        reader = csv.DictReader(f)
        ctx['displacement'] = [row for row in reader]

    return ctx


# === block: score_0 (check id='check_regional_formation_energies') ===
def score_0(artifact, step, ctx):
    artifact, step, ctx = artifact, step, ctx
    formation_data = ctx.get('formation', [])

    crystalline_sum = 0.0
    crystalline_count = 0
    amorphous_sum = 0.0
    amorphous_count = 0

    for row in formation_data:
        try:
            region = row['region'].strip().lower()
            dist = float(row['distance_from_interface_A'])
            energy = float(row['formation_energy_eV'])
        except (ValueError, KeyError):
            continue
        if region == 'crystalline' and dist < -5.0:
            crystalline_sum += energy
            crystalline_count += 1
        elif region == 'amorphous' and dist > 5.0:
            amorphous_sum += energy
            amorphous_count += 1

    if crystalline_count == 0 or amorphous_count == 0:
        return 0.0

    avg_crystalline = crystalline_sum / crystalline_count
    avg_amorphous = amorphous_sum / amorphous_count

    # Trend must hold
    if avg_crystalline <= avg_amorphous:
        return 0.0

    c_thresh = step.get('params', {}).get('crystalline_threshold', 2.0)
    a_thresh = step.get('params', {}).get('amorphous_threshold', 0.8)

    # Score crystalline (higher is better)
    if avg_crystalline >= c_thresh:
        s_cryst = 1.0
    else:
        s_cryst = max(0.0, 1.0 - (c_thresh - avg_crystalline) / c_thresh)

    # Score amorphous (lower is better)
    if avg_amorphous <= a_thresh:
        s_amor = 1.0
    else:
        s_amor = max(0.0, 1.0 - (avg_amorphous - a_thresh) / a_thresh)

    return 0.5 * s_cryst + 0.5 * s_amor


# === block: score_1 (check id='check_formation_displacement_correlation') ===
def score_1(artifact, step, ctx):
    artifact, step, ctx = artifact, step, ctx
    formation_data = ctx.get('formation', [])
    displacement_data = ctx.get('displacement', [])

    # Map site_id to formation energy
    e_map = {}
    for row in formation_data:
        try:
            sid = int(row['site_id'])
            energy = float(row['formation_energy_eV'])
        except (ValueError, KeyError):
            continue
        e_map[sid] = energy

    e_values = []
    d_values = []
    for row in displacement_data:
        try:
            sid = int(row['site_id'])
            disp = float(row['root_sum_square_displacement_angstrom'])
        except (ValueError, KeyError):
            continue
        if sid in e_map:
            e_values.append(e_map[sid])
            d_values.append(disp)

    if len(e_values) < 5:
        return 0.0

    r, _ = spearmanr(e_values, d_values)
    thresh = step.get('params', {}).get('correlation_threshold', -0.5)

    if r <= thresh:
        return 1.0
    else:
        # r > thresh => worse, linear decay
        # penalty from distance above thresh relative to gap from 1
        # safer: score = max(0.0, 1.0 - (r - thresh) / abs(thresh))
        penalty = (r - thresh) / abs(thresh)
        return max(0.0, 1.0 - penalty)


_SCORERS = {
    'check_regional_formation_energies': score_0,
    'check_formation_displacement_correlation': score_1,
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
