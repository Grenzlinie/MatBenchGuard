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


# === block: score_0 (check id='coupling_energies_struct') ===
def score_0(artifact, step, ctx):
    systems_data = {}
    for row in artifact:
        sys = row.get('system', '').strip()
        try:
            n = int(row['n'])
            de = float(row['delta_E'])
        except (ValueError, KeyError):
            continue
        if sys:
            systems_data.setdefault(sys, []).append((n, de))
    required = {'Fe-V', 'Co-Pd', 'Co-Ru', 'Fe-Cr'}
    if not required.issubset(systems_data.keys()):
        return 0.0
    def sorted_deltas(records):
        records.sort(key=lambda x: x[0])
        return [v for _, v in records]
    def passes_friedel(deltas):
        if len(deltas) < 3:
            return False
        signs = [1 if v > 0 else -1 if v < 0 else 0 for v in deltas]
        if any(s == 0 for s in signs):
            return False
        alternates = all(signs[i] * signs[i+1] < 0 for i in range(len(signs)-1))
        decreasing = all(abs(deltas[i+1]) <= abs(deltas[i]) + 1e-9 for i in range(len(deltas)-1))
        return alternates and decreasing
    def passes_exp_decay(deltas):
        if len(deltas) < 2:
            return False
        first_sign = 1 if deltas[0] > 0 else -1 if deltas[0] < 0 else 0
        if first_sign == 0:
            return False
        same_sign = all((1 if v > 0 else -1 if v < 0 else 0) == first_sign for v in deltas)
        decreasing = all(abs(deltas[i+1]) <= abs(deltas[i]) + 1e-9 for i in range(len(deltas)-1))
        return same_sign and decreasing
    def passes_parity_oscill(deltas, originals):
        if len(originals) < 3:
            return False
        odd_signs = [de for n, de in originals if n % 2 == 1]
        even_signs = [de for n, de in originals if n % 2 == 0]
        if not odd_signs or not even_signs:
            return False
        odd_sign = 1 if all(v > 0 for v in odd_signs) else -1 if all(v < 0 for v in odd_signs) else 0
        even_sign = 1 if all(v > 0 for v in even_signs) else -1 if all(v < 0 for v in even_signs) else 0
        if odd_sign == 0 or even_sign == 0:
            return False
        if odd_sign == even_sign:
            return False
        odd_mean_abs = sum(abs(v) for v in odd_signs) / len(odd_signs)
        even_mean_abs = sum(abs(v) for v in even_signs) / len(even_signs)
        if odd_mean_abs <= even_mean_abs:
            return False
        return True
    passed = 0
    for sys in ['Fe-V', 'Co-Ru']:
        if sys in systems_data:
            deltas = sorted_deltas(systems_data[sys][:])
            if passes_friedel(deltas):
                passed += 1
    if 'Co-Pd' in systems_data:
        deltas = sorted_deltas(systems_data['Co-Pd'][:])
        if passes_exp_decay(deltas):
            passed += 1
    if 'Fe-Cr' in systems_data:
        originals = systems_data['Fe-Cr'][:]
        deltas = [v for _, v in originals]
        if passes_parity_oscill(deltas, originals):
            passed += 1
    return passed / 4.0


_SCORERS = {
    'coupling_energies_struct': score_0,
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
