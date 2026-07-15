import os
import json
import csv

# === author imports / helpers ===
import csv, re, math


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
    gold_raw = spec.get('gold_table', [])
    gold = {}
    for row in gold_raw:
        key = (row['system'], row['hole_location'], row['spin_state'])
        gold[key] = float(row['energy'])
    return {'gold': gold}


# === block: score_0 (check id='value_match') ===
def score_0(artifact, step, ctx):
    tol = float(step.get('tolerance_abs', 0.3))
    max_pen = float(step.get('max_penalty_abs', 0.6))
    gold = ctx['gold']
    scores = []
    for (sys, hl, spin), ref in gold.items():
        found = None
        for r in artifact:
            if r.get('system') == sys and r.get('hole_location') == hl and r.get('spin_state') == spin:
                try:
                    val = float(r.get('excitation_energy_eV'))
                except:
                    continue
                found = val
                break
        if found is None:
            scores.append(0.0)
            continue
        err = abs(found - ref)
        if err <= tol:
            scores.append(1.0)
        elif err >= max_pen:
            scores.append(0.0)
        else:
            scores.append(1.0 - (err - tol) / (max_pen - tol))
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_1 (check id='monotonicity') ===
def score_1(artifact, step, ctx):
    tol_mono = 0.02  # allow tiny dips (0.02 eV) to match the paper's slight non-monotonicities
    groups = {}
    for r in artifact:
        sys = r.get('system', '')
        hl = r.get('hole_location', '')
        spin = r.get('spin_state', '')
        if hl in ('none', 'delocalized'):
            continue
        m = re.match(r'\(TiO2\)_?(\d+)', sys)
        if not m:
            continue
        n = int(m.group(1))
        try:
            v = float(r.get('excitation_energy_eV'))
        except:
            continue
        key = (hl, spin)
        groups.setdefault(key, []).append((n, v))
    total_pairs = 0
    correct = 0
    for entries in groups.values():
        entries.sort(key=lambda x: x[0])
        for i in range(len(entries)-1):
            total_pairs += 1
            # allow a decrease up to tol_mono to avoid penalizing the paper's own small dips
            if entries[i+1][1] + tol_mono >= entries[i][1]:
                correct += 1
    if total_pairs == 0:
        return 0.0
    return correct / total_pairs


# === block: score_2 (check id='singlet_gt_triplet') ===
def score_2(artifact, step, ctx):
    pairs = {}
    for r in artifact:
        sys = r.get('system', '')
        hl = r.get('hole_location', '')
        spin = r.get('spin_state', '')
        if hl not in ('out-of-plane', 'in-plane/outside', 'in-plane/inside'):
            continue
        m = re.match(r'\(TiO2\)_?(\d+)', sys)
        if not m:
            continue
        n = int(m.group(1))
        try:
            v = float(r.get('excitation_energy_eV'))
        except:
            continue
        key = (hl, n)
        if spin == 'triplet':
            if key not in pairs:
                pairs[key] = {}
            pairs[key]['triplet'] = v
        elif spin == 'singlet':
            if key not in pairs:
                pairs[key] = {}
            pairs[key]['singlet'] = v
    total = 0
    correct = 0
    for d in pairs.values():
        if 'triplet' in d and 'singlet' in d:
            total += 1
            if d['singlet'] > d['triplet']:
                correct += 1
    if total == 0:
        return 0.0
    return correct / total


# === block: score_3 (check id='energy_lowering') ===
def score_3(artifact, step, ctx):
    threshold = float(step.get('threshold_eV', 1.0))
    deloc = None
    localized = []
    for r in artifact:
        if r.get('system') != '(TiO2)_8':
            continue
        if r.get('hole_location') == 'delocalized' and r.get('spin_state') == 'triplet':
            try:
                deloc = float(r.get('excitation_energy_eV'))
            except:
                continue
        elif r.get('spin_state') == 'triplet' and r.get('hole_location') in ('out-of-plane', 'in-plane/outside', 'in-plane/inside'):
            try:
                localized.append(float(r.get('excitation_energy_eV')))
            except:
                continue
    if deloc is None or len(localized) < 3:
        return 0.0
    for loc in localized:
        if deloc - loc <= threshold:
            return 0.0
    return 1.0


_SCORERS = {
    'value_match': score_0,
    'monotonicity': score_1,
    'singlet_gt_triplet': score_2,
    'energy_lowering': score_3,
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
