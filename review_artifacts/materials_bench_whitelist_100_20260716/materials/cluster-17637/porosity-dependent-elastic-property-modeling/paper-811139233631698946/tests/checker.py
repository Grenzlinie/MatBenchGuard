import os
import json
import csv

# === author imports / helpers ===
import csv
import math
import os


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


# === block: score_0 (check id='step01_surfC_const') ===
def score_0(artifact, step, ctx):
        # artifact: list of dicts
        total = 0
        passed = 0
        for row in artifact:
            if row['surface'] != 'C':
                continue
            for mod in ['k_norm','m_norm','n_norm','l_norm','G_norm','Gp_norm']:
                total += 1
                if abs(float(row[mod]) - 1.0) <= 0.002:
                    passed += 1
        return passed / total if total > 0 else 0.0


# === block: score_1 (check id='step01_surf_ord') ===
def score_1(artifact, step, ctx):
        # Group by (radius, distribution) for surfaces A,B
        radii_wanted = [1,2,5]
        moduli = ['k_norm','m_norm','n_norm','l_norm','G_norm','Gp_norm']
        total = 0
        passed = 0
        def get_rows(radius, dist):
            A_rows = [r for r in artifact if float(r['radius'])==radius and r['distribution']==dist and r['surface']=='A']
            B_rows = [r for r in artifact if float(r['radius'])==radius and r['distribution']==dist and r['surface']=='B']
            return A_rows, B_rows
        for radius in radii_wanted:
            for dist in ['square','hexagonal']:
                A_list, B_list = get_rows(radius, dist)
                if not A_list or not B_list:
                    continue
                A = A_list[0]
                B = B_list[0]
                for mod in moduli:
                    a = float(A[mod])
                    b = float(B[mod])
                    da = abs(a - 1.0)
                    db = abs(b - 1.0)
                    total += 1
                    if da >= db:
                        passed += 1
        return passed / total if total > 0 else 0.0


# === block: score_2 (check id='step01_monotonic') ===
def score_2(artifact, step, ctx):
        radii_available = sorted(set(float(r['radius']) for r in artifact))
        moduli = ['k_norm','m_norm','n_norm','l_norm','G_norm','Gp_norm']
        total = 0
        passed = 0
        for surf in ['A','B']:
            for dist in ['square','hexagonal']:
                subset = [r for r in artifact if r['surface']==surf and r['distribution']==dist]
                subset.sort(key=lambda x: float(x['radius']))
                for mod in moduli:
                    vals = [abs(float(row[mod])-1.0) for row in subset]
                    if len(vals) < 2:
                        continue
                    total += 1
                    # check monotonically decreasing (allowing tiny increase)
                    non_monotonic = 0
                    for i in range(len(vals)-1):
                        if vals[i+1] > vals[i] * 1.01:  # allow 1% fluctuation
                            non_monotonic += 1
                    if non_monotonic <= 1:  # allow at most one violation
                        passed += 1
        return passed / total if total > 0 else 0.0


# === block: score_3 (check id='step02_trend') ===
def score_3(artifact, step, ctx):
        shapes = ['4_oscillations','8_oscillations']
        total = 0
        passed = 0
        for shape in shapes:
            rows = [r for r in artifact if r['shape']==shape]
            rows.sort(key=lambda x: float(x['R0']))
            kvals = [float(r['k_norm']) for r in rows]
            if len(kvals) < 2:
                continue
            total += 1
            # check monotonic decreasing
            decreasing = all(kvals[i] >= kvals[i+1] for i in range(len(kvals)-1))
            total += 1
            if decreasing:
                passed += 1
            # check that R0=1 value larger than R0=50
            first = next((float(r['k_norm']) for r in rows if float(r['R0'])==1.0), None)
            last = next((float(r['k_norm']) for r in rows if float(r['R0'])==50.0), None)
            if first and last:
                total += 1
                if first > last:
                    passed += 1
        return passed / total if total > 0 else 0.0


# === block: score_4 (check id='step03_monotonic') ===
def score_4(artifact, step, ctx):
        radii_available = sorted(set(float(r['radius']) for r in artifact))
        moduli = ['k_norm','m_norm','n_norm','l_norm','G_norm','Gp_norm']
        total = 0
        passed = 0
        for dist in ['square','hexagonal']:
            subset = [r for r in artifact if r['distribution']==dist]
            subset.sort(key=lambda x: float(x['radius']))
            for mod in moduli:
                vals = [float(row[mod]) for row in subset]
                if len(vals) < 2:
                    continue
                total += 1
                # non-increasing
                mono = all(vals[i] >= vals[i+1] - 1e-6 for i in range(len(vals)-1))
                if mono:
                    passed += 1
        # for random, just check direction from 1 to 50
        random_rows = [r for r in artifact if r['distribution']=='random']
        if random_rows:
            random_rows.sort(key=lambda x: float(x['radius']))
            r1_rows = [r for r in random_rows if float(r['radius'])==1.0]
            r50_rows = [r for r in random_rows if float(r['radius'])==50.0]
            if r1_rows and r50_rows:
                for mod in moduli:
                    avg1 = sum(float(r[mod]) for r in r1_rows)/len(r1_rows)
                    avg50 = sum(float(r[mod]) for r in r50_rows)/len(r50_rows)
                    total += 1
                    if avg1 >= avg50:
                        passed += 1
        return passed / total if total > 0 else 0.0


_SCORERS = {
    'step01_surfC_const': score_0,
    'step01_surf_ord': score_1,
    'step01_monotonic': score_2,
    'step02_trend': score_3,
    'step03_monotonic': score_4,
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
