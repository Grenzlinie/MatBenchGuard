import os
import json
import csv

# === author imports / helpers ===
import os, json, csv, statistics


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


# === block: score_0 (check id='comp_check') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    config = step.get('config', {})
    posit_req = config.get('positivity_required', True)
    elem_config = config.get('elemental_conservation', {})
    atom_map = elem_config.get('atom_mapping', {})
    max_cv = elem_config.get('max_cv', 0.1)

    # Check positivity of all species columns (skip temperature)
    temp_col = 'Temperature (K)'
    if temp_col not in rows[0]:
        return 0.0
    species_cols = [c for c in rows[0].keys() if c != temp_col]

    pos_ok = True
    if posit_req:
        for row in rows:
            for col in species_cols:
                try:
                    val = float(row[col])
                except (ValueError, KeyError):
                    return 0.0
                if val < 0:
                    pos_ok = False
                    break
            if not pos_ok:
                break

    # Elemental conservation
    elem_totals = {'C': [], 'F': [], 'O': []}
    for row in rows:
        total = {'C': 0.0, 'F': 0.0, 'O': 0.0}
        for col in species_cols:
            if col in atom_map:
                try:
                    dens = float(row[col])
                except:
                    dens = 0.0
                for elem in ('C','F','O'):
                    total[elem] += dens * atom_map[col].get(elem, 0)
        for elem in ('C','F','O'):
            elem_totals[elem].append(total[elem])

    conserv_ok = True
    for elem in ('C','F','O'):
        vals = elem_totals[elem]
        if not vals or sum(vals) == 0:
            conserv_ok = False
        else:
            mean_val = statistics.mean(vals)
            if mean_val == 0:
                cv = 1e9
            else:
                cv = statistics.stdev(vals) / mean_val if len(vals) > 1 else 0.0
            if cv > max_cv:
                conserv_ok = False

    # Scoring: 0.5 for positivity, 0.5 for conservation
    score = 0.0
    if pos_ok:
        score += 0.5
    if conserv_ok:
        score += 0.5
    return score


# === block: score_1 (check id='thermo_check') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    config = step.get('config', {}).get('specific_heat_peaks', {})
    temp_col = config.get('temperature_column', 'Temperature (K)')
    cp_col = config.get('specific_heat_column', 'SpecificHeat')
    ranges = config.get('peak_ranges', [])

    if temp_col not in rows[0] or cp_col not in rows[0]:
        return 0.0
    temps = []
    cps = []
    for row in rows:
        try:
            t = float(row[temp_col])
            cp = float(row[cp_col])
            temps.append(t)
            cps.append(cp)
        except:
            continue

    # find local maxima
    peaks = []
    for i in range(1, len(cps)-1):
        if cps[i] > cps[i-1] and cps[i] > cps[i+1]:
            peaks.append(temps[i])

    if not peaks:
        return 0.0

    # check each range
    num_ranges = max(len(ranges),1)
    found = 0
    for r in ranges:
        lo, hi = r
        if any(lo <= p <= hi for p in peaks):
            found += 1

    return found / num_ranges


# === block: score_2 (check id='elec_cond_check') ===
def score_2(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    config = step.get('config', {}).get('low_temp_order', {})
    temp_col = config.get('temp_column', 'Temperature (K)')
    thresh = config.get('temp_threshold', 5000)
    cols = config.get('columns_order', [])
    if len(cols) < 3:
        return 0.0
    c1, c2, c3 = cols[0], cols[1], cols[2]

    violations = 0
    total = 0
    for row in rows:
        try:
            T = float(row[temp_col])
        except:
            continue
        if T < thresh:
            total += 1
            try:
                v1 = float(row[c1])
                v2 = float(row[c2])
                v3 = float(row[c3])
            except:
                violations += 1
                continue
            if not (v1 > v2 and v1 > v3):
                violations += 1

    if total == 0:
        return 1.0
    return max(0.0, 1.0 - violations / total)


# === block: score_3 (check id='therm_cond_check') ===
def score_3(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    config = step.get('config', {}).get('peak_check', {})
    temp_col = config.get('temp_column', 'Temperature (K)')
    val_col = config.get('value_column', 'ThermalConductivity_C6F12O')
    targets = config.get('target_peaks', [])

    if temp_col not in rows[0] or val_col not in rows[0]:
        return 0.0
    temps = []
    vals = []
    for row in rows:
        try:
            t = float(row[temp_col])
            v = float(row[val_col])
            temps.append(t)
            vals.append(v)
        except:
            continue

    if not temps:
        return 0.0

    # find local maxima
    peaks = []
    for i in range(1, len(vals)-1):
        if vals[i] > vals[i-1] and vals[i] > vals[i+1]:
            peaks.append(temps[i])

    if not peaks:
        return 0.0

    hits = 0
    for tgt in targets:
        center = tgt.get('center')
        tol = tgt.get('tol', 500)
        if center is None:
            continue
        if any(abs(p - center) <= tol for p in peaks):
            hits += 1

    num_targets = len(targets)
    if num_targets == 0:
        return 1.0
    return hits / num_targets


_SCORERS = {
    'comp_check': score_0,
    'thermo_check': score_1,
    'elec_cond_check': score_2,
    'therm_cond_check': score_3,
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
