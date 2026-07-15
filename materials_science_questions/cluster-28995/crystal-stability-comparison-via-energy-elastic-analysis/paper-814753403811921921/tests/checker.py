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
    def Tm_fcc(P): return 2042.0 * (1.0 + P/44.3)**0.85
    def Tm_9R(P): return 1500.0 * (1.0 + P/20.0)**0.79
    pressures = [0.0, 50.0, 100.0]
    melting_expected = {}
    for P in pressures:
        melting_expected[(P, 'fcc')] = Tm_fcc(P)
        melting_expected[(P, '9R')] = Tm_9R(P)
    inverse_z_expected = {
        (20.0, 2500.0): 'fcc',
        (40.0, 2500.0): '9R',
        (100.0, 3000.0): '9R',
    }
    ctx = {
        'melting_expected': melting_expected,
        'inverse_z_expected': inverse_z_expected,
    }
    return ctx


# === block: score_0 (check id='check_melting') ===
def score_0(artifact, step, ctx):
    rows = artifact
    melting_expected = ctx['melting_expected']
    points = [
        (0.0, 'fcc'), (0.0, '9R'),
        (50.0, 'fcc'), (50.0, '9R'),
        (100.0, 'fcc'), (100.0, '9R')
    ]
    reported = {}
    for row in rows:
        try:
            P = float(row['pressure_GPa'])
            ph = row['phase'].strip()
            Tm = float(row['melting_temperature_K'])
            reported[(P, ph)] = Tm
        except (ValueError, KeyError):
            continue

    per_point_scores = []
    for pkey in points:
        if pkey not in reported:
            per_point_scores.append(0.0)
            continue
        rval = reported[pkey]
        expected = melting_expected.get(pkey)
        if expected is None or expected <= 0:
            per_point_scores.append(0.0)
            continue
        rel_err = abs(rval - expected) / expected
        score = max(0.0, 1.0 - rel_err / 0.15)  # linear decay from 1 at 0 to 0 at 0.15
        per_point_scores.append(score)
    avg_score = sum(per_point_scores) / len(per_point_scores) if per_point_scores else 0.0

    # trend check: 0 GPa: fcc > 9R; 50,100 GPa: 9R > fcc
    trend_ok = True
    try:
        fcc0 = reported.get((0.0, 'fcc'), None)
        f9r0 = reported.get((0.0, '9R'), None)
        if fcc0 is None or f9r0 is None or fcc0 <= f9r0:
            trend_ok = False
    except:
        trend_ok = False
    if trend_ok:
        for P in (50.0, 100.0):
            fccP = reported.get((P, 'fcc'), None)
            f9rP = reported.get((P, '9R'), None)
            if fccP is None or f9rP is None or fccP >= f9rP:
                trend_ok = False
                break
    trend_score = 1.0 if trend_ok else 0.0
    return 0.8 * avg_score + 0.2 * trend_score


# === block: score_1 (check id='check_inverse_z') ===
def score_1(artifact, step, ctx):
    rows = artifact
    expected = ctx['inverse_z_expected']
    epoints = [(20.0, 2500.0), (40.0, 2500.0), (100.0, 3000.0)]
    correct = 0
    for row in rows:
        try:
            P = float(row['pressure_GPa'])
            T = float(row['temperature_K'])
            ph = row['solid_phase'].strip().lower()
            key = (P, T)
            if key in expected:
                exp_ph = expected[key].lower()
                # Accept 'fcc' exactly; for 9R accept '9r', '9r', 'hexagonal', 'hex'
                if ph == exp_ph:
                    correct += 1
                elif exp_ph == '9r' and ph in ('9r', 'hexagonal', 'hex'):
                    correct += 1
        except (ValueError, KeyError):
            continue
    return correct / len(epoints)


_SCORERS = {
    'check_melting': score_0,
    'check_inverse_z': score_1,
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
