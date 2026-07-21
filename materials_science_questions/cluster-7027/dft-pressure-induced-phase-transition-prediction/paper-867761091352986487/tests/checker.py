import os
import json
import csv

# === author imports / helpers ===
import csv
import os
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
    return {}


# === block: score_0 (check id='structural_ordering') ===
def score_0(artifact, step, ctx):
    EPS = 1e-9
    rows = artifact
    if not rows or not all(col in rows[0] for col in ['pressure_GPa','structure','relative_enthalpy_meV_per_H2O']):
        return 0.0
    data = {}
    for r in rows:
        try:
            p = float(r['pressure_GPa'])
            s = r['structure'].strip().lower()
            v = float(r['relative_enthalpy_meV_per_H2O'])
            data.setdefault(p, {})[s] = v
        except (ValueError, KeyError):
            return 0.0
    conditions = []

    # 0 GPa: hexagonal must exist, be negative, and be the structural minimum
    if 0.0 in data and 'hexagonal' in data[0.0]:
        hval = data[0.0]['hexagonal']
        cond = (hval < -EPS) and all(v >= hval - EPS for v in data[0.0].values())
    else:
        cond = False
    conditions.append(cond)

    # 1 GPa: all relative enthalpies must be >= -EPS (square-tube is the stable phase)
    if 1.0 in data:
        cond = all(v >= -EPS for v in data[1.0].values())
    else:
        cond = False
    conditions.append(cond)

    # 2, 3, 4 GPa: HCP must exist, be negative, and be the structural minimum
    for p in [2.0, 3.0, 4.0]:
        if p in data and 'hcp' in data[p]:
            hcp_v = data[p]['hcp']
            cond = (hcp_v < -EPS) and all(v >= hcp_v - EPS for v in data[p].values())
        else:
            cond = False
        conditions.append(cond)

    # 5 GPa: buckled-rhombic must exist, be negative, and be the structural minimum
    if 5.0 in data and 'buckled-rhombic' in data[5.0]:
        brv = data[5.0]['buckled-rhombic']
        cond = (brv < -EPS) and all(v >= brv - EPS for v in data[5.0].values())
    else:
        cond = False
    conditions.append(cond)

    return sum(conditions) / len(conditions) if conditions else 0.0


# === block: score_1 (check id='square_vs_squaretube_threshold_1GPa') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not rows or not all(col in rows[0] for col in ['pressure_GPa','structure','relative_enthalpy_meV_per_H2O']):
        return 0.0
    square_val = None
    for r in rows:
        try:
            p = float(r['pressure_GPa'])
            s = r['structure'].strip().lower()
            v = float(r['relative_enthalpy_meV_per_H2O'])
        except (ValueError, KeyError):
            continue
        if abs(p - 1.0) < 1e-6 and s == 'square':
            square_val = v
            break
    if square_val is None:
        return 0.0
    # monotonic scoring: threshold 15 meV/H2O, higher is better
    if square_val >= 15.0:
        return 1.0
    elif square_val <= 0.0:
        return 0.0
    else:
        return square_val / 15.0


_SCORERS = {
    'structural_ordering': score_0,
    'square_vs_squaretube_threshold_1GPa': score_1,
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
