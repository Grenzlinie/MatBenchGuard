import os
import json
import csv

# === author imports / helpers ===
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


# === block: score_0 (check id='band_gaps') ===
def score_0(artifact, step, ctx):
    def score_band_gaps(artifact, step, ctx):
        gold = step.get('gold', {})
        tol = step.get('tolerance_abs', 0.1)
        if not isinstance(artifact, dict) or not gold:
            return 0.0
        total = 0.0
        count = 0
        for key in ['GeS_ML', 'GeSe_ML', 'XX', 'XY']:
            val = artifact.get(key)
            gv = gold.get(key)
            if val is None or gv is None:
                continue
            try:
                val = float(val)
                gv = float(gv)
                err = abs(val - gv)
                if err <= tol:
                    total += 1.0
                else:
                    total += max(0.0, 1.0 - (err - tol) / (abs(gv) * 0.5))
                count += 1
            except (TypeError, ValueError):
                pass
        if count == 0:
            return 0.0
        return total / count


# === block: score_1 (check id='lattice_thermal_conductivity') ===
def score_1(artifact, step, ctx):
    def score_lattice(artifact, step, ctx):
        gold = step.get('gold', {})
        tol_rel = step.get('tolerance_rel', 0.20)
        if not isinstance(artifact, dict):
            return 0.0
        total = 0.0
        count = 0
        for key in ['GeS_ML', 'GeSe_ML', 'XX', 'XY']:
            if key in artifact and key in gold:
                val = artifact[key]
                try:
                    gv = float(gold[key])
                    rel_err = abs(val - gv) / abs(gv) if gv != 0 else abs(val)
                    if rel_err <= tol_rel:
                        total += 1.0
                    else:
                        total += max(0.0, 1.0 - (rel_err - tol_rel) / 0.3)
                    count += 1
                except (TypeError, ValueError, ZeroDivisionError):
                    pass
        if count == 0:
            return 0.0
        return total / count


# === block: score_2 (check id='zt_values') ===
def score_2(artifact, step, ctx):
    def score_zt(artifact, step, ctx):
        if not isinstance(artifact, dict):
            return 0.0
        gold_300 = step.get('gold_300K', {})
        gold_800 = step.get('gold_800K', {})
        materials = ['GeS_ML', 'GeSe_ML', 'XX', 'XY']
        temps = [('300K', gold_300), ('800K', gold_800)]
        # Threshold subscore
        sub_a = 0.0
        n_a = 0
        for mat in materials:
            for tkey, gold_t in temps:
                if mat in gold_t and mat in artifact and tkey in artifact[mat]:
                    val = artifact[mat][tkey]
                    gv = gold_t[mat]
                    if val >= gv:
                        sub_a += 1.0
                    else:
                        sub_a += max(0.0, val / abs(gv) if gv != 0 else 0.0)
                    n_a += 1
        score_a = sub_a / n_a if n_a > 0 else 0.0
        # Temperature monotonicity (ZT(800K) > ZT(300K))
        sub_b = 0.0
        n_b = 0
        for mat in materials:
            if mat in artifact and '300K' in artifact[mat] and '800K' in artifact[mat]:
                zt300 = artifact[mat]['300K']
                zt800 = artifact[mat]['800K']
                if zt800 > zt300:
                    sub_b += 1.0
                else:
                    sub_b += 0.0
                n_b += 1
        score_b = sub_b / n_b if n_b > 0 else 0.0
        # Ordering at 300K: monolayer ZT > heterostructure ZT
        mono = ['GeS_ML', 'GeSe_ML']
        hetero = ['XX', 'XY']
        sub_c = 0.0
        n_c = 0
        for m in mono:
            for h in hetero:
                if (m in artifact and h in artifact and '300K' in artifact[m] and '300K' in artifact[h]):
                    if artifact[m]['300K'] > artifact[h]['300K']:
                        sub_c += 1.0
                    else:
                        sub_c += 0.0
                    n_c += 1
        score_c = sub_c / n_c if n_c > 0 else 0.0
        total = 0.6 * score_a + 0.2 * score_b + 0.2 * score_c
        return total


_SCORERS = {
    'band_gaps': score_0,
    'lattice_thermal_conductivity': score_1,
    'zt_values': score_2,
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
