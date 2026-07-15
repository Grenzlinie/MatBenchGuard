import os
import json
import csv

# === author imports / helpers ===
import json
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


# === block: score_0 (check id='vacancy_formation') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold = step['gold']
        tol_fe = step['tolerances']['formation_energy_ev']
        tol_mm = step['tolerances']['magnetic_moment_muB']
        trend_weight = step.get('trend_weight', 0.2)
        def check_entry(entry, gold_entry):
            fe_ok = abs(entry['formation_energy_ev'] - gold_entry['formation_energy_ev']) <= tol_fe
            mm_ok = abs(entry['magnetic_moment_muB'] - gold_entry['magnetic_moment_muB']) <= tol_mm
            if fe_ok and mm_ok:
                return 1.0
            elif fe_ok or mm_ok:
                return 0.5
            else:
                return 0.0
        zb_entries = sorted(artifact['zb'], key=lambda x: x['charge'])
        wz_entries = sorted(artifact['wz'], key=lambda x: x['charge'])
        zb_gold = gold['zb']
        wz_gold = gold['wz']
        scores = []
        for ae, ge in zip(zb_entries, zb_gold):
            scores.append(check_entry(ae, ge))
        for ae, ge in zip(wz_entries, wz_gold):
            scores.append(check_entry(ae, ge))
        numeric_score = sum(scores) / len(scores) if scores else 0.0
        def trend_ok(entries, key):
            vals = [e[key] for e in entries]
            for i in range(1, len(vals)):
                if vals[i] > vals[i-1] + 1e-9:
                    return False
            return True
        trend_fe_zb = trend_ok(zb_entries, 'formation_energy_ev')
        trend_fe_wz = trend_ok(wz_entries, 'formation_energy_ev')
        trend_mm_zb = trend_ok(zb_entries, 'magnetic_moment_muB')
        trend_mm_wz = trend_ok(wz_entries, 'magnetic_moment_muB')
        trend_score = 1.0 if all([trend_fe_zb, trend_fe_wz, trend_mm_zb, trend_mm_wz]) else 0.0
        final = numeric_score * (1.0 - trend_weight) + trend_score * trend_weight
        return min(1.0, max(0.0, final))


# === block: score_1 (check id='defect_complex') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold = step['gold']
        tol = step['tolerances']
        complex_data = artifact.get('Si_Ga+V_Ga', {})
        if not complex_data:
            return 0.0
        fe = abs(complex_data.get('formation_energy_ev', None) - gold['formation_energy_ev']) <= tol.get('formation_energy_ev', 0.5)
        be = abs(complex_data.get('binding_energy_ev', None) - gold['binding_energy_ev']) <= tol.get('binding_energy_ev', 0.5)
        mm = abs(complex_data.get('magnetic_moment_muB', None) - gold['magnetic_moment_muB']) <= tol.get('magnetic_moment_muB', 0.1)
        sub = [1.0 if f else 0.0 for f in [fe, be, mm]]
        return sum(sub) / len(sub) if sub else 0.0


# === block: score_2 (check id='slab_depth') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold_profile = step['gold']['depth_profile']
        tol_fe = step['tolerances']['formation_energy_ev']
        trend_weight = step.get('trend_weight', 0.2)
        prof = artifact.get('depth_profile', [])
        if not prof:
            return 0.0
        prof_sorted = sorted(prof, key=lambda x: x['layer'])
        scores = []
        for ae, ge in zip(prof_sorted, gold_profile):
            if abs(ae['formation_energy_ev'] - ge['formation_energy_ev']) <= tol_fe:
                scores.append(1.0)
            else:
                scores.append(0.0)
        numeric_score = sum(scores) / len(scores) if scores else 0.0
        fe_vals = [e['formation_energy_ev'] for e in prof_sorted]
        trend = True
        for i in range(1, len(fe_vals)):
            if fe_vals[i] < fe_vals[i-1] - 1e-9:
                trend = False
                break
        trend_score = 1.0 if trend else 0.0
        final = numeric_score * (1.0 - trend_weight) + trend_score * trend_weight
        return min(1.0, max(0.0, final))


_SCORERS = {
    'vacancy_formation': score_0,
    'defect_complex': score_1,
    'slab_depth': score_2,
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
