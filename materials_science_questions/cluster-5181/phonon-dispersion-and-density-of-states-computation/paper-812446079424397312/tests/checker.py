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


# === block: score_0 (check id='step_form_factor') ===
def score_0(artifact, step, ctx):
    import csv, math
    gold_points = step.get('config',{}).get('gold_points', [])
    tol_rel = step.get('config',{}).get('tolerance_rel', 0.05)
    if not artifact or len(artifact)==0:
        return 0.0
    qs, vs = [], []
    for row in artifact:
        try:
            q = float(row['q'])
            v = float(row['v_screened'])
            qs.append(q)
            vs.append(v)
        except:
            pass
    if not qs:
        return 0.0
    def find_v(q_target):
        best_q = min(qs, key=lambda x: abs(x-q_target))
        idx = qs.index(best_q)
        return vs[idx]
    max_rel_err = 0.0
    typical_scale = max(abs(v) for v in vs) if vs else 1.0
    for (qg, vg) in gold_points:
        v_agent = find_v(qg)
        if abs(vg) < 1e-6:
            err = abs(v_agent - vg) / max(0.01, typical_scale)
        else:
            err = abs(v_agent - vg) / abs(vg)
        max_rel_err = max(max_rel_err, err)
    if max_rel_err <= tol_rel:
        score = 1.0
    else:
        score = max(0.0, 1.0 - (max_rel_err - tol_rel) / tol_rel)
    return score


# === block: score_1 (check id='step_resistivity') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold_value = step.get('config',{}).get('gold_value', 31.256)
        tol_rel = step.get('config',{}).get('tolerance_rel', 0.05)
        try:
            text = artifact.strip() if isinstance(artifact, str) else str(artifact)
            # take the first floating point number
            import re
            fl_str = re.findall(r'[-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?', text)
            if not fl_str:
                return 0.0
            val = float(fl_str[0])
        except:
            return 0.0
        if gold_value == 0.0:
            return 1.0 if val == 0.0 else 0.0
        rel_err = abs(val - gold_value) / abs(gold_value)
        if rel_err <= tol_rel:
            score = 1.0
        else:
            score = max(0.0, 1.0 - (rel_err - tol_rel) / tol_rel)
        return score


# === block: score_2 (check id='step_phonon') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold_points = step.get('config',{}).get('gold_points', [])
        mape_threshold = step.get('config',{}).get('mape_threshold', 0.10)
        if not artifact or not gold_points:
            return 0.0
        # Build lookup: (direction, zeta, branch) -> frequency
        agent_map = {}
        for row in artifact:
            try:
                direction = str(row.get('direction','')).strip()
                zeta = float(row.get('zeta', -1))
                branch = str(row.get('branch','')).strip()
                freq = float(row.get('frequency', 0))
                agent_map[(direction, zeta, branch)] = freq
            except:
                pass
        total_ape = 0.0
        count = 0
        for gp in gold_points:
            d = str(gp.get('direction','')).strip()
            z = float(gp.get('zeta', -1))
            b = str(gp.get('branch','')).strip()
            key = (d, z, b)
            if key not in agent_map:
                return 0.0  # missing required point
            f_agent = agent_map[key]
            f_gold = gp.get('frequency', 1.0)
            if f_gold == 0.0:
                if f_agent == 0.0:
                    ape = 0.0
                else:
                    ape = 1.0  # completely wrong
            else:
                ape = abs(f_agent - f_gold) / abs(f_gold)
            total_ape += ape
            count += 1
        mape = total_ape / count if count > 0 else 1.0
        if mape <= mape_threshold:
            score = 1.0
        else:
            score = max(0.0, 1.0 - (mape - mape_threshold) / mape_threshold)
        return score


_SCORERS = {
    'step_form_factor': score_0,
    'step_resistivity': score_1,
    'step_phonon': score_2,
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
