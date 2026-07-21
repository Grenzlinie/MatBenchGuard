import os
import json
import csv

# === author imports / helpers ===
import csv, os, json


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


# === block: score_0 (check id='sim_and_gk_low_dipole') ===
def score_0(artifact, step, ctx):
    rows = artifact
    R = [float(r['R']) for r in rows]
    Gk = [float(r['G_k']) for r in rows]
    max_gk = 0.0
    for r, g in zip(R, Gk):
        if r >= 6.0 and g > max_gk:
            max_gk = g
    if max_gk < 50.0:
        return 1.0
    else:
        return 0.0


# === block: score_1 (check id='sim_and_gk_high_dipole') ===
def score_1(artifact, step, ctx):
    rows = artifact
    R = [float(r['R']) for r in rows]
    Gk = [float(r['G_k']) for r in rows]
    max_gk = -1e9
    best_R = 0.0
    for r, g in zip(R, Gk):
        if r >= 6.0 and g > max_gk:
            max_gk = g
            best_R = r
    if max_gk >= 100.0 and 20.0 <= best_R <= 40.0:
        return 1.0
    else:
        return 0.0


# === block: score_2 (check id='domain_summary') ===
def score_2(artifact, step, ctx):
    out_dir = '/app/outputs'
    def load_csv(path):
        with open(path) as f:
            return list(csv.DictReader(f))

    REF_RADIUS = 28.0
    TOL_RADIUS = 7.0
    MIN_GK = 100

    # weak coupling
    rows0 = load_csv(os.path.join(out_dir, 'gk_curves_mu0.635.csv'))
    max_gk0 = 0.0
    for r, g in [(float(r['R']), float(r['G_k'])) for r in rows0]:
        if r >= 6.0 and g > max_gk0:
            max_gk0 = g
    score_weak = 1.0 if max_gk0 < 50.0 else 0.0

    # strong coupling
    rows1 = load_csv(os.path.join(out_dir, 'gk_curves_mu1.651.csv'))
    best_R1 = None
    max_gk1 = -1e9
    for r, g in [(float(r['R']), float(r['G_k'])) for r in rows1]:
        if r >= 6.0 and g > max_gk1:
            max_gk1 = g
            best_R1 = r
    radius_ok = (best_R1 is not None and abs(best_R1 - REF_RADIUS) <= TOL_RADIUS)
    Gk_ok = (max_gk1 >= MIN_GK)
    score_strong = 1.0 if (radius_ok and Gk_ok) else 0.0

    return (score_weak + score_strong) / 2.0


_SCORERS = {
    'sim_and_gk_low_dipole': score_0,
    'sim_and_gk_high_dipole': score_1,
    'domain_summary': score_2,
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
