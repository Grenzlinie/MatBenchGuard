import os
import json
import csv


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
    import csv
    import os

    def prepare(outputs_dir, spec):
        path = os.path.join(outputs_dir, 'shift_current_tensors.csv')
        data = []
        with open(path, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
        data_dict = {}
        for row in data:
            thick = row['thickness'].strip()
            comp = row['component'].strip()
            energy = float(row['energy_eV'])
            sigma = float(row['sigma_muA_per_V2'])
            key = (thick, comp)
            if key not in data_dict:
                data_dict[key] = []
            data_dict[key].append((energy, sigma))
        for k in data_dict:
            data_dict[k].sort(key=lambda x: x[0])
        return {'data': data, 'data_dict': data_dict}


# === block: score_0 (check id='shape_gate') ===
def score_0(artifact, step, ctx):
    data = ctx['data']
    if not data:
        return 0.0
    required_cols = {'thickness', 'component', 'energy_eV', 'sigma_muA_per_V2'}
    if not required_cols.issubset(data[0].keys()):
        return 0.0
    thicknesses = {'monolayer', 'bilayer', 'four-layer', 'bulk'}
    components = {'xxx', 'xyy', 'xzz', 'yxx', 'yyy', 'yzz', 'zxx', 'zyy', 'zzz'}
    found = set()
    for row in data:
        found.add((row['thickness'].strip(), row['component'].strip()))
    expected = set()
    for t in thicknesses:
        for c in components:
            expected.add((t, c))
    if not expected.issubset(found):
        return 0.0
    return 1.0


# === block: score_1 (check id='trend_izz_small') ===
def score_1(artifact, step, ctx):
    dd = ctx['data_dict']
    thicknesses = ['monolayer', 'bilayer']
    comps = ['xzz', 'yzz', 'zzz']
    max_abs_vals = []
    for t in thicknesses:
        for c in comps:
            key = (t, c)
            if key not in dd:
                return 0.0
            curve = dd[key]
            if not curve:
                return 0.0
            maxv = max(abs(s) for _, s in curve)
            max_abs_vals.append(maxv)
    if all(v < 0.1 for v in max_abs_vals):
        return 1.0
    return 0.0


# === block: score_2 (check id='trend_zii_layer_enhancement') ===
def score_2(artifact, step, ctx):
    dd = ctx['data_dict']
    comps = ['zxx', 'zyy']
    thicknesses = ['bilayer', 'four-layer']
    ref_key = ('bulk', None)
    peak_bulk = {}
    for c in comps:
        key = ('bulk', c)
        if key not in dd or not dd[key]:
            return 0.0
        peak_bulk[c] = max(s for _, s in dd[key])
    for t in thicknesses:
        for c in comps:
            key = (t, c)
            if key not in dd or not dd[key]:
                return 0.0
            peak = max(s for _, s in dd[key])
            if peak_bulk[c] == 0:
                if peak == 0:
                    continue
                return 0.0
            if peak < 2.0 * peak_bulk[c]:
                return 0.0
    return 1.0


# === block: score_3 (check id='trend_ykk_oscillatory') ===
def score_3(artifact, step, ctx):
    dd = ctx['data_dict']
    thicknesses = ['monolayer', 'bilayer']
    comps = ['yxx', 'yyy', 'yzz']
    for t in thicknesses:
        for c in comps:
            key = (t, c)
            if key not in dd or not dd[key]:
                return 0.0
            curve = dd[key]
            sigs = [s for _, s in curve]
            # require at least two sign changes (zero crossings) and some amplitude
            if max(sigs) - min(sigs) < 0.1:
                continue
            sign_changes = sum(1 for i in range(len(sigs)-1) if sigs[i]*sigs[i+1] < 0)
            if sign_changes >= 2:
                return 1.0
    return 0.0


# === block: score_4 (check id='trend_xxx_xyy_opposite_sign') ===
def score_4(artifact, step, ctx):
    dd = ctx['data_dict']
    thicknesses = ['monolayer', 'bilayer', 'four-layer', 'bulk']
    for t in thicknesses:
        key1 = (t, 'xxx')
        key2 = (t, 'xyy')
        if key1 not in dd or key2 not in dd or not dd[key1] or not dd[key2]:
            return 0.0
        curve1 = dd[key1]
        curve2 = dd[key2]
        for (_, s1), (_, s2) in zip(curve1, curve2):
            if s1 * s2 >= 0:
                return 0.0
    return 1.0


_SCORERS = {
    'shape_gate': score_0,
    'trend_izz_small': score_1,
    'trend_zii_layer_enhancement': score_2,
    'trend_ykk_oscillatory': score_3,
    'trend_xxx_xyy_opposite_sign': score_4,
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
