import os
import json
import csv

# === author imports / helpers ===
import csv, json, math, os

def compute_band_gap(rows):
    """
    rows: list of dicts as returned by csv.DictReader.
    Assumes first column is 'k_coord' and rest are band energies.
    Returns band gap (eV) or None if data is degenerate.
    """
    if not rows:
        return None
    # separate key columns
    energy_cols = [k for k in rows[0].keys() if k != 'k_coord']
    if not energy_cols:
        return None
    # check for band crossing (metallic)
    for col in energy_cols:
        vals = []
        for r in rows:
            try:
                vals.append(float(r[col]))
            except (ValueError, KeyError):
                pass
        if not vals:
            continue
        vmin = min(vals)
        vmax = max(vals)
        if vmin <= 0.0 and vmax > 0.0:
            return 0.0   # crossing -> metallic
    # No crossing; compute minimum gap across k-points
    min_gap = float('inf')
    for r in rows:
        vals = []
        for col in energy_cols:
            try:
                vals.append(float(r[col]))
            except (ValueError, KeyError):
                pass
        if not vals:
            continue
        # occupied: energy <= 0; unoccupied: energy > 0
        occupied_max = max((v for v in vals if v <= 0.0), default=None)
        unoccupied_min = min((v for v in vals if v > 0.0), default=None)
        if occupied_max is not None and unoccupied_min is not None:
            gap_k = unoccupied_min - occupied_max
            if gap_k < min_gap:
                min_gap = gap_k
    if min_gap == float('inf'):
        return None
    return min_gap


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


# === block: score_0 (check id='feTP_gap') ===
def score_0(artifact, step, ctx):
    gap = compute_band_gap(artifact)
    if gap is None:
        return 0.0
    if gap <= 0.1:
        return 1.0
    elif gap >= 0.3:
        return 0.0
    else:
        # linear decay from 1.0 at 0.1 to 0.0 at 0.3
        return (0.3 - gap) / 0.2


# === block: score_1 (check id='feTPNO_gap') ===
def score_1(artifact, step, ctx):
    gap = compute_band_gap(artifact)
    if gap is None:
        return 0.0
    if gap >= 0.2:
        return 1.0
    elif gap <= 0.0:
        return 0.0
    else:
        # linear ramp from 0.0 at 0 eV to 1.0 at 0.2 eV
        return gap / 0.2


# === block: score_2 (check id='angle') ===
def score_2(artifact, step, ctx):
    angle = artifact.get('fe_NO_angle_deg') if isinstance(artifact, dict) else None
    if angle is None or not isinstance(angle, (int, float)):
        return 0.0
    return 1.0 if abs(angle - 148.0) <= 5.0 else 0.0


_SCORERS = {
    'feTP_gap': score_0,
    'feTPNO_gap': score_1,
    'angle': score_2,
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
