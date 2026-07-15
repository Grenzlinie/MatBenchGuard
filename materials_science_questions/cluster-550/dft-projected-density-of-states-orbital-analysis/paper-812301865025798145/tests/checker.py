import os
import json
import csv

# === author imports / helpers ===
import csv
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


# === block: score_0 (check id='check_dHvA_entries') ===
def score_0(artifact, step, ctx):
    try:
        # artifact is list of dicts from CSV
        rows = artifact
        if not isinstance(rows, list) or len(rows) == 0:
            return 0.0
        # validate required columns
        required = {'branch', 'direction', 'frequency_calc', 'mass_calc'}
        if not required.issubset(rows[0].keys()):
            return 0.0
        # build lookup by (branch, direction)
        row_map = {}
        for r in rows:
            br = r.get('branch', '').strip()
            dr = r.get('direction', '').strip()
            row_map[(br, dr)] = r

        gold = step.get('gold', [])
        freq_tol = step.get('frequency_tolerance', 0.10)
        # ensure mass tolerance is at least 100% to accommodate DFT mass accuracy
        mass_tol = max(step.get('mass_tolerance', 1.0), 1.0)

        freq_pass = 0
        mass_pass = 0
        total = len(gold)

        for exp in gold:
            key = (exp['branch'], exp['direction'])
            if key not in row_map:
                continue  # missing counts as fail for both
            r = row_map[key]
            try:
                freq = float(r['frequency_calc'])
                mass = float(r['mass_calc'])
            except (ValueError, TypeError):
                continue
            exp_freq = exp['frequency_exp']
            exp_mass = exp['mass_exp']
            if abs(freq - exp_freq) / max(exp_freq, 1e-12) <= freq_tol:
                freq_pass += 1
            if abs(mass - exp_mass) / max(exp_mass, 1e-12) <= mass_tol:
                mass_pass += 1

        # ordering check
        ordering_ok = True
        dirs = step.get('ordering_directions', [])
        for d in dirs:
            # gather rows for this direction in CSV order
            dir_rows = [r for r in rows if r.get('direction', '').strip() == d]
            vals = []
            for r in dir_rows:
                try:
                    vals.append(float(r['frequency_calc']))
                except (ValueError, TypeError):
                    ordering_ok = False
                    break
            if ordering_ok and len(vals) > 1:
                if not all(vals[i] < vals[i+1] for i in range(len(vals)-1)):
                    ordering_ok = False
                    break

        freq_score = freq_pass / total if total > 0 else 0.0
        mass_score = mass_pass / total if total > 0 else 0.0
        factor = 1.0 if ordering_ok else 0.8
        final = (0.8 * freq_score + 0.2 * mass_score) * factor
        return max(0.0, min(1.0, final))
    except Exception:
        return 0.0


_SCORERS = {
    'check_dHvA_entries': score_0,
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
