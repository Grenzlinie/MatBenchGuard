import os
import json
import csv

# === author imports / helpers ===
import csv, os

# Helper to safely get float from a row dict
def _safe_float(s):
    try:
        return float(s)
    except (ValueError, TypeError):
        return None


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
    def prepare(outputs_dir, spec):
        # No shared preprocessing needed; return empty context.
        return {}


# === block: score_0 (check id='adsorption_energies_check') ===
def score_0(artifact, step, ctx):
        rows = artifact
        config = step['config']
        # Only check the converged 9L slab to avoid penalising thin-slab anomalies
        slabs_to_check = [9]
        models = config['models']
        data = {}
        for row in rows:
            try:
                slab = int(row['slab'])
                model = row['model'].strip()
                E = _safe_float(row['E_ads'])
                if E is not None:
                    if slab not in data:
                        data[slab] = {}
                    data[slab][model] = E
            except Exception:
                continue
        # Check ordering: R > H1 and R > H2 for the converged slab
        ordering_ok = True
        for s in slabs_to_check:
            vals = data.get(s, {})
            if not all(m in vals for m in models):
                ordering_ok = False
                break
            if not (vals['R'] > vals['H1'] and vals['R'] > vals['H2']):
                ordering_ok = False
                break
        # Check closeness: |H1 - H2| < threshold for the converged slab
        closeness_ok = True
        thr = config['closeness_threshold_eV']
        for s in slabs_to_check:
            vals = data.get(s, {})
            if not ('H1' in vals and 'H2' in vals):
                closeness_ok = False
                break
            if abs(vals['H1'] - vals['H2']) >= thr:
                closeness_ok = False
                break
        score = (0.7 if ordering_ok else 0.0) + (0.3 if closeness_ok else 0.0)
        return score


# === block: score_1 (check id='spin_localization_check') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        rows = artifact
        config = step['config']
        slabs_needed = config['slabs']
        min_Ti = config['min_abs_Ti_spin']
        max_H = config['max_abs_H_spin']
        passed = 0
        total = len(slabs_needed)
        data = {}
        for row in rows:
            try:
                slab = int(row['slab'])
                spin_Ti = _safe_float(row['max_abs_spin_Ti'])
                spin_H = _safe_float(row['max_abs_spin_H'])
                if slab in slabs_needed and spin_Ti is not None and spin_H is not None:
                    data[slab] = (spin_Ti, spin_H)
            except Exception:
                continue
        for s in slabs_needed:
            if s in data:
                if data[s][0] > min_Ti and data[s][1] < max_H:
                    passed += 1
        return passed / total if total > 0 else 0.0


# === block: score_2 (check id='nh3_acidity_check') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        rows = artifact
        config = step['config']
        slabs_needed = config['slabs']
        min_diff = config['min_diff_eV']
        passed = 0
        total = len(slabs_needed)
        slab_diff = {}
        for row in rows:
            try:
                slab = int(row['slab'])
                system = row['system'].strip()
                E = _safe_float(row['E_ads_NH3'])
                if slab in slabs_needed and E is not None:
                    slab_diff.setdefault(slab, {})
                    if system in ('clean', 'H_covered'):
                        slab_diff[slab][system] = E
            except Exception:
                continue
        for s in slabs_needed:
            vals = slab_diff.get(s, {})
            if 'clean' in vals and 'H_covered' in vals:
                if vals['clean'] - vals['H_covered'] > min_diff:
                    passed += 1
        return passed / total if total > 0 else 0.0


_SCORERS = {
    'adsorption_energies_check': score_0,
    'spin_localization_check': score_1,
    'nh3_acidity_check': score_2,
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
