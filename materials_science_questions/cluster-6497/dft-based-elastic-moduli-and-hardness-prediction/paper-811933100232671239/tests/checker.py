import os
import json
import csv

# === author imports / helpers ===
import os, json


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
    outputs_dir = spec.get('outputs_dir', '/app/outputs')
    return {'outputs_dir': outputs_dir}


# === block: score_0 (check id='step01_eos') ===
def score_0(artifact, step, ctx):
    fields_spec = step.get('fields', {})
    if not isinstance(artifact, dict):
        return 0.0
    ok = 0
    n = len(fields_spec)
    if n == 0:
        return 1.0
    for fname, spec_item in fields_spec.items():
        val = artifact.get(fname)
        if val is None:
            continue
        try:
            v = float(val)
            target = float(spec_item['target'])
            tol = float(spec_item['tolerance'])
            if abs(v - target) <= tol:
                ok += 1
        except (ValueError, TypeError):
            pass
    return ok / n


# === block: score_1 (check id='step02_elastic') ===
def score_1(artifact, step, ctx):
    fields_spec = step.get('fields', {})
    if not isinstance(artifact, dict):
        return 0.0
    ok = 0
    n = len(fields_spec)
    if n == 0:
        return 1.0
    for fname, spec_item in fields_spec.items():
        val = artifact.get(fname)
        if val is None:
            continue
        try:
            v = float(val)
            target = float(spec_item['target'])
            tol = float(spec_item['tolerance'])
            if abs(v - target) <= tol:
                ok += 1
        except (ValueError, TypeError):
            pass
    return ok / n


# === block: score_2 (check id='step03_bandgap') ===
def score_2(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    gap_ok = False
    type_ok = False
    gap_val = artifact.get('band_gap_eV')
    type_val = str(artifact.get('band_gap_type', '')).strip().lower()
    try:
        v = float(gap_val)
        if abs(v - step['gap_target']) <= step['gap_tolerance']:
            gap_ok = True
    except (ValueError, TypeError):
        gap_ok = False
    type_expected = step['type_target'].strip().lower()
    type_ok = (type_val == type_expected)
    return (0.5 if gap_ok else 0.0) + (0.5 if type_ok else 0.0)


# === block: score_3 (check id='consistency_bulk') ===
def score_3(artifact, step, ctx):
    outputs_dir = ctx['outputs_dir']
    path_eos = os.path.join(outputs_dir, 'step01_eos_properties.json')
    path_el = os.path.join(outputs_dir, 'step02_elastic_moduli.json')
    try:
        with open(path_eos) as f:
            eos = json.load(f)
        with open(path_el) as f:
            el = json.load(f)
        B_eos = float(eos.get('B_GPa', 0))
        B_el = float(el.get('B_el_GPa', 0))
        if B_eos <= 0.0:
            return 0.0
        delta = abs(B_eos - B_el) / B_eos
        max_r = step['max_ratio']
        return 1.0 if delta <= max_r else 0.0
    except Exception:
        return 0.0


_SCORERS = {
    'step01_eos': score_0,
    'step02_elastic': score_1,
    'step03_bandgap': score_2,
    'consistency_bulk': score_3,
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
