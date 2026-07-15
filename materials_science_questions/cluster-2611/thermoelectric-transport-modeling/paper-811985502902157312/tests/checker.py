import os
import json
import csv

# === author imports / helpers ===
import csv, os, json, collections


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


# === block: score_0 (check id='value_match') ===
def score_0(artifact, step, ctx):
    ref_vals = step.get('reference_values', [])
    if not ref_vals:
        return 1.0
    rel_tol = step.get('tolerance_relative', 0.15)
    abs_tol = step.get('tolerance_abs', 10.0)
    ref_dict = {}
    for ref in ref_vals:
        key = (str(ref['compound']).strip(), str(ref['doping_level']).strip(), float(ref['temperature_K']))
        ref_dict[key] = float(ref['Seebeck_uV_K'])
    total_expected = len(ref_vals)
    matched = 0
    for row in artifact:
        try:
            comp = str(row.get('compound','')).strip()
            doping = str(row.get('doping_level','')).strip()
            temp = float(row.get('temperature_K', None))
            seebeck = float(row.get('Seebeck_uV_K', None))
        except (ValueError, TypeError):
            continue
        key = (comp, doping, temp)
        if key in ref_dict:
            ref_S = ref_dict[key]
            diff = abs(seebeck - ref_S)
            if diff <= max(rel_tol * ref_S, abs_tol):
                matched += 1
    if total_expected == 0:
        return 1.0
    return min(1.0, matched / total_expected)


# === block: score_1 (check id='monotonicity') ===
def score_1(artifact, step, ctx):
    from collections import defaultdict
    doping_order = {
        'h=0.5': 0, 'h=0.6': 1, 'h=0.7': 2, 'h=0.8': 3,
        'p=0.5': 0, 'p=1.0': 1, 'p=2.0': 2
    }
    groups = defaultdict(list)
    for row in artifact:
        comp = str(row.get('compound','')).strip()
        doping = str(row.get('doping_level','')).strip()
        try:
            T = float(row.get('temperature_K', None))
            S = float(row.get('Seebeck_uV_K', None))
        except (ValueError, TypeError):
            continue
        groups[(comp, T)].append((doping, S))
    all_monotonic = True
    for (comp, T), entries in groups.items():
        sorted_entries = sorted(entries, key=lambda x: doping_order.get(x[0], 9999))
        sorted_entries = [e for e in sorted_entries if e[0] in doping_order]
        if len(sorted_entries) < 2:
            continue
        prev_S = sorted_entries[0][1]
        for doping, S in sorted_entries[1:]:
            if S > prev_S:
                all_monotonic = False
                break
            prev_S = S
        if not all_monotonic:
            break
    return 1.0 if all_monotonic else 0.0


_SCORERS = {
    'value_match': score_0,
    'monotonicity': score_1,
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
