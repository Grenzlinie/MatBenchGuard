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
    return {}


# === block: score_0 (check id='two_vacancy_energy_check') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    val = artifact.get('two_vacancy_ripple_energy')
    if val is None:
        return 0.0
    try:
        val = float(val)
    except (TypeError, ValueError):
        return 0.0
    gold = float(step.get('gold_two_vacancy_energy', 4.73))
    tol = float(step.get('tolerance_abs', 0.2))
    return 1.0 if abs(val - gold) <= tol else 0.0


# === block: score_1 (check id='ripplocation_trends_check') ===
def score_1(artifact, step, ctx):
    def score_trends(artifact, step, ctx):
        models = artifact.get('models')
        if not models:
            return 0.0
        pristine = [m for m in models if m.get('type') == 'pristine']
        defective = [m for m in models if m.get('type') == 'defective']
        pts = sorted(pristine, key=lambda x: x.get('buckling_height', 0))
        dts = sorted(defective, key=lambda x: x.get('buckling_height', 0))
        inc_ok = all(
            pts[i].get('formation_energy_pristine') is not None and 
            pts[i+1].get('formation_energy_pristine') is not None and 
            pts[i]['formation_energy_pristine'] < pts[i+1]['formation_energy_pristine']
            for i in range(len(pts)-1)
        ) if len(pts) >= 2 else False
        dec_ok = all(
            dts[i].get('formation_energy_vacancy') is not None and
            dts[i+1].get('formation_energy_vacancy') is not None and
            dts[i]['formation_energy_vacancy'] > dts[i+1]['formation_energy_vacancy']
            for i in range(len(dts)-1)
        ) if len(dts) >= 2 else False
        if dts:
            max_def = max(dts, key=lambda x: x.get('buckling_height', 0))
            neg_at_max = (max_def.get('formation_energy_vacancy') is not None and
                          max_def['formation_energy_vacancy'] < 0)
        else:
            neg_at_max = False
        p_map = {m['buckling_height']: m for m in pts}
        d_map = {m['buckling_height']: m for m in dts}
        common = set(p_map.keys()) & set(d_map.keys())
        lower_total = False
        if common:
            max_h = max(common)
            if (p_map[max_h].get('total_energy') is not None and
                d_map[max_h].get('total_energy') is not None):
                lower_total = d_map[max_h]['total_energy'] < p_map[max_h]['total_energy']
        subs = [inc_ok, dec_ok, neg_at_max, lower_total]
        n_valid = 4 if common else 3
        score = sum(1 for s in subs if s) / n_valid if n_valid > 0 else 0.0
        return score


# === block: score_2 (check id='trend_text_check') ===
def score_2(artifact, step, ctx):
    def score_trend_text(artifact_text, step, ctx):
        import re
        ripp_path = '/app/outputs/ripplocation_energies.json'
        ripp = load_artifact(ripp_path)
        if ripp is None:
            return 0.0
        rv_two = ripp.get('two_vacancy_ripple_energy')
        models = ripp.get('models', [])
        txt = artifact_text
        score = 0.0
        if rv_two is not None and f'{rv_two:.2f}' in txt:
            score += 0.25
        pristine = [m for m in models if m.get('type') == 'pristine']
        defective = [m for m in models if m.get('type') == 'defective']
        all_p_ok = True
        for p in pristine:
            h = p.get('buckling_height')
            e = p.get('formation_energy_pristine')
            if h is None or e is None:
                all_p_ok = False; break
            if str(h) not in txt or f'{e:.1f}' not in txt:
                all_p_ok = False; break
        all_d_ok = True
        for d in defective:
            h = d.get('buckling_height')
            e = d.get('formation_energy_vacancy')
            if h is None or e is None:
                all_d_ok = False; break
            if str(h) not in txt or f'{e:.1f}' not in txt:
                all_d_ok = False; break
        if all_p_ok and all_d_ok:
            score += 0.35
        required_terms = ['increases monotonically', 'decreases monotonically', 'negative', 'thermodynamically']
        if all(term in txt.lower() for term in required_terms):
            score += 0.4
        return min(1.0, score)


_SCORERS = {
    'two_vacancy_energy_check': score_0,
    'ripplocation_trends_check': score_1,
    'trend_text_check': score_2,
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
