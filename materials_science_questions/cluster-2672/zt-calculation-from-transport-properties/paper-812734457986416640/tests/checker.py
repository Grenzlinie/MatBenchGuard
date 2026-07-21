import os
import json
import csv

# === author imports / helpers ===
import os
import json
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
        def max_zt_from_csv(path, zt_col='ZT'):
            if not os.path.exists(path):
                return None
            with open(path, newline='') as f:
                reader = csv.DictReader(f)
                zts = []
                for row in reader:
                    try:
                        zts.append(float(row[zt_col]))
                    except (KeyError, ValueError):
                        pass
                return max(zts) if zts else None

        ctx = {}
        output_dir = outputs_dir
        path400 = os.path.join(output_dir, 'zt_ordered_400K.csv')
        path_temps = os.path.join(output_dir, 'zt_ordered_temperatures.csv')

        ctx['max_zt_400k'] = max_zt_from_csv(path400, 'ZT')

        temps_max = {}
        if os.path.exists(path_temps):
            with open(path_temps, newline='') as f:
                reader = csv.DictReader(f)
                if 'ZT_200K' in reader.fieldnames and 'ZT_300K' in reader.fieldnames and 'ZT_400K' in reader.fieldnames:
                    max_vals = {'ZT_200K': 0.0, 'ZT_300K': 0.0, 'ZT_400K': 0.0}
                    for row in reader:
                        for col in max_vals:
                            try:
                                val = float(row[col])
                                max_vals[col] = max(max_vals[col], val)
                            except (KeyError, ValueError):
                                pass
                    temps_max = max_vals
        ctx['temps_max'] = temps_max
        return ctx


# === block: score_0 (check id='step2_zt_400k') ===
def score_0(artifact, step, ctx):
        if artifact is None or not artifact:
            return 0.0
        try:
            zt_values = [float(row['ZT']) for row in artifact]
        except (KeyError, ValueError):
            return 0.0
        max_zt = max(zt_values) if zt_values else 0.0
        if max_zt >= 20.0:
            zt_score = 1.0
        elif max_zt >= 10.0:
            zt_score = (max_zt - 10.0) / 10.0
        else:
            zt_score = 0.0

        shape_ok = True
        if len(artifact) < 300:
            shape_ok = False
        ef_in_range = True
        for row in artifact:
            try:
                ef = float(row['Ef (eV)'])
                if ef < -3.5 or ef > 3.5:
                    ef_in_range = False
                    break
            except (KeyError, ValueError):
                shape_ok = False
                break
        if not ef_in_range:
            shape_ok = False
        if any(v < 0 for v in zt_values):
            shape_ok = False
        if all(v < 0.1 for v in zt_values):
            shape_ok = False

        shape_score = 1.0 if shape_ok else 0.0
        return zt_score * 0.8 + shape_score * 0.2


# === block: score_1 (check id='step3_zt_temperatures') ===
def score_1(artifact, step, ctx):
        if artifact is None or not artifact:
            return 0.0
        cols = ['ZT_200K', 'ZT_300K', 'ZT_400K']
        max_t = {c: 0.0 for c in cols}
        try:
            for row in artifact:
                for c in cols:
                    val = float(row[c])
                    max_t[c] = max(max_t[c], val)
        except (KeyError, ValueError):
            return 0.0

        zt200 = max_t['ZT_200K']
        zt300 = max_t['ZT_300K']
        zt400 = max_t['ZT_400K']

        # ordering: 400 > 300 > 200 (small float slack)
        count = 0
        if zt400 > zt300 + 1e-6:
            count += 1
        if zt300 > zt200 + 1e-6:
            count += 1
        order_score = count / 2.0  # 0.0, 0.5, 1.0

        # consistency with zt_ordered_400K.csv
        cons_score = 0.0
        ref_max = ctx.get('max_zt_400k', None)
        if ref_max is not None and max(zt400, ref_max) > 0:
            diff_frac = abs(zt400 - ref_max) / max(zt400, ref_max)
            cons_score = 1.0 if diff_frac < 0.05 else 0.0
        else:
            cons_score = 0.0  # reference unavailable, skip consistency

        return order_score * 0.7 + cons_score * 0.3


_SCORERS = {
    'step2_zt_400k': score_0,
    'step3_zt_temperatures': score_1,
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
