import os
import json
import csv

# === author imports / helpers ===
import json, math, os


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
    gold = spec.get("gold", {}); return {"gold": gold}


# === block: score_0 (check id='step_04') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) != 6:
        return 0.0

    entries_by_n = {}
    for entry in artifact:
        if not isinstance(entry, dict):
            return 0.0
        if "n" not in entry or "trapping_energy" not in entry or "zpe_correction" not in entry:
            return 0.0
        n = entry["n"]
        if not isinstance(n, int) or n < 1 or n > 6:
            return 0.0
        entries_by_n[n] = entry

    if len(entries_by_n) != 6:
        return 0.0

    gold = ctx.get("gold", {})
    trapping_gold = gold.get("trapping_ZPE_corrected", {})
    trapping_tols = gold.get("trapping_tolerances", {})
    zpe_gold = gold.get("zpe_gold", {})
    zpe_tol = gold.get("zpe_tolerance", 0.02)
    # Apply relaxed minimum tolerance for ZPE to account for cross-code (VASP -> QE) reproducibility
    zpe_tol = max(zpe_tol, 0.05)

    points = 0.0
    max_points = 1.0

    for n in range(1, 6):
        tg = trapping_gold.get(str(n))
        if tg is None:
            continue
        tol = trapping_tols.get(str(n), 0.1)
        # Relax tolerance for n=1,2 to at least 0.10 eV for cross-code reproducibility
        if n in (1, 2):
            tol = max(tol, 0.10)
        try:
            reported = float(entries_by_n[n]["trapping_energy"])
        except (TypeError, ValueError):
            reported = None
        if reported is not None and abs(reported - tg) <= tol:
            points += 0.12

    # n=6 must be positive
    entry6 = entries_by_n[6]
    try:
        reported6 = float(entry6["trapping_energy"])
    except (TypeError, ValueError):
        reported6 = None
    if reported6 is not None and reported6 > 0:
        points += 0.1

    # ZPE checks
    for n in range(1, 7):
        zref = zpe_gold.get(str(n))
        if zref is None:
            continue
        try:
            reported_zpe = float(entries_by_n[n]["zpe_correction"])
        except (TypeError, ValueError):
            reported_zpe = None
        if reported_zpe is not None and abs(reported_zpe - zref) <= zpe_tol:
            points += 0.05

    return min(points / max_points, 1.0)


# === block: score_1 (check id='step_05') ===
def score_1(artifact, step, ctx):
    artifact = str(artifact).strip()
    gold = ctx.get("gold", {})
    barrier_gold = gold.get("diffusion_barrier_gold", 1.17)
    barrier_tol = gold.get("diffusion_barrier_tolerance", 0.1)
    try:
        val = float(artifact)
    except (ValueError, TypeError):
        return 0.0
    return 1.0 if abs(val - barrier_gold) <= barrier_tol else 0.0


_SCORERS = {
    'step_04': score_0,
    'step_05': score_1,
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
