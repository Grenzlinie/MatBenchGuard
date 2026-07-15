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


# === block: score_0 (check id='step_ziman_results') ===
def score_0(artifact, step, ctx):
    import math

    def _rel_error(val, gold):
        if gold == 0:
            return 0.0 if val == 0 else 1.0
        return abs(val - gold) / abs(gold)

    def _piecewise_score(rel_err, tol, decay_factor):
        if rel_err <= tol:
            return 1.0
        if rel_err >= decay_factor * tol:
            return 0.0
        # linear decay from 1 at tol to 0 at decay_factor*tol
        return 1.0 - (rel_err - tol) / ((decay_factor - 1) * tol)

    artifact_dict = artifact
    if not isinstance(artifact_dict, dict):
        return 0.0

    gold = step.get('gold', {})
    tolerances = step.get('rel_tolerances', {})
    weights_within = step.get('score_weights_within', {})
    decay = float(step.get('decay_factor', 2.0))

    volumes = ['164.5', '155', '147', '140']
    score = 0.0

    # resistivities
    gold_res = gold.get('resistivities', {})
    w_res = weights_within.get('resistivities', [0.0]*4)
    if isinstance(w_res, list) and len(w_res) == 4:
        for i, v in enumerate(volumes):
            gv = gold_res.get(v)
            av = artifact_dict.get('resistivities', {}).get(v)
            if gv is not None and av is not None:
                rel = _rel_error(av, gv)
                score += w_res[i] * _piecewise_score(rel, tolerances.get('resistivities', 0.1), decay)

    # thermopowers
    gold_thermo = gold.get('thermopowers', {})
    w_thermo = weights_within.get('thermopowers', [0.0]*4)
    if isinstance(w_thermo, list) and len(w_thermo) == 4:
        for i, v in enumerate(volumes):
            gv = gold_thermo.get(v)
            av = artifact_dict.get('thermopowers', {}).get(v)
            if gv is not None and av is not None:
                rel = _rel_error(av, gv)
                score += w_thermo[i] * _piecewise_score(rel, tolerances.get('thermopowers', 0.15), decay)

    # g2_ambient
    g_g2 = gold.get('g2_ambient')
    a_g2 = artifact_dict.get('g2_ambient')
    if g_g2 is not None and a_g2 is not None:
        w_g2 = weights_within.get('g2_ambient', 0.0)
        rel = _rel_error(a_g2, g_g2)
        score += w_g2 * _piecewise_score(rel, tolerances.get('g2_ambient', 0.2), decay)

    # dln_g2_dln_a
    g_deriv = gold.get('dln_g2_dln_a')
    a_deriv = artifact_dict.get('dln_g2_dln_a')
    if g_deriv is not None and a_deriv is not None:
        w_deriv = weights_within.get('dln_g2_dln_a', 0.0)
        rel = _rel_error(a_deriv, g_deriv)
        score += w_deriv * _piecewise_score(rel, tolerances.get('dln_g2_dln_a', 0.25), decay)

    return min(1.0, max(0.0, score))


_SCORERS = {
    'step_ziman_results': score_0,
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
