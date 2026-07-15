import os
import json
import csv

# === author imports / helpers ===
import math, os, csv


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


# === block: score_0 (check id='numeric_values') ===
def score_0(artifact, step, ctx):
    import csv, math

    def safe_float(v):
        try:
            return float(v)
        except:
            return None

    def safe_int(v):
        try:
            i = int(float(v))
            if float(i) == float(v):
                return i
            return None
        except:
            return None

    gold_list = step.get('gold', [])
    tols = step.get('tolerances', {})
    if not gold_list or not artifact:
        return 0.0

    rows = {r.get('compound','').strip().lower(): r for r in artifact}
    expected = ['be2b', 'albeb', 'mgbeb', 'nabeb']
    scores = []

    for g in gold_list:
        cp = g['compound'].strip().lower()
        row = rows.get(cp)
        if row is None:
            scores.append(0.0)
            continue
        prop_scores = []
        for key in ['a_Ang','B_GPa','Bprime','VB_eV','Eg_Gamma_X_eV','Nv','N_EF_total_states_per_eV','B_p_contribution_states_per_eV']:
            gold_val = g[key]
            agent_str = row.get(key, '')
            tol = tols.get(key)
            if tol is None:
                continue
            tol_type = tol['type']
            tol_val = tol.get('value')
            if tol_type == 'special':
                # B_p_contribution: gold null means agent must have '-'
                if gold_val is None:
                    if str(agent_str).strip() == '-':
                        prop_scores.append(1.0)
                    else:
                        prop_scores.append(0.0)
                else:
                    gv = float(gold_val)
                    if gv == 0.0:
                        av = safe_float(agent_str)
                        if av is not None and abs(av) <= 1e-6:
                            prop_scores.append(1.0)
                        else:
                            prop_scores.append(0.0)
                    else:
                        av = safe_float(agent_str)
                        if av is None:
                            prop_scores.append(0.0)
                        else:
                            rel_err = abs(av - gv) / abs(gv)
                            if rel_err <= 0.10:
                                prop_scores.append(1.0)
                            else:
                                prop_scores.append(0.0)
            elif tol_type == 'exact':
                gi = int(gold_val)
                ai = safe_int(agent_str)
                if ai is not None and ai == gi:
                    prop_scores.append(1.0)
                else:
                    prop_scores.append(0.0)
            elif tol_type == 'absolute':
                gv = float(gold_val)
                av = safe_float(agent_str)
                if av is None:
                    prop_scores.append(0.0)
                else:
                    if abs(av - gv) <= tol_val:
                        prop_scores.append(1.0)
                    else:
                        prop_scores.append(0.0)
            elif tol_type == 'relative':
                gv = float(gold_val)
                if gv == 0.0:
                    av = safe_float(agent_str)
                    if av is not None and abs(av) <= 1e-6:
                        prop_scores.append(1.0)
                    else:
                        prop_scores.append(0.0)
                else:
                    av = safe_float(agent_str)
                    if av is None:
                        prop_scores.append(0.0)
                    else:
                        rel_err = abs(av - gv) / abs(gv)
                        if rel_err <= tol_val:
                            prop_scores.append(1.0)
                        else:
                            prop_scores.append(0.0)
            else:
                prop_scores.append(0.0)
        if prop_scores:
            scores.append(sum(prop_scores) / len(prop_scores))
        else:
            scores.append(0.0)

    if scores:
        return sum(scores) / len(scores)
    return 0.0


# === block: score_1 (check id='lattice_ordering') ===
def score_1(artifact, step, ctx):
    if not artifact:
        return 0.0
    order = step.get('expected_order', [])
    if len(order) < 2:
        return 1.0
    rows = {r.get('compound','').strip().lower(): r for r in artifact}
    vals = []
    for comp in order:
        row = rows.get(comp.lower())
        if row is None:
            return 0.0
        try:
            v = float(row.get('a_Ang', 0))
        except:
            return 0.0
        vals.append(v)

    for i in range(len(vals)-1):
        if vals[i] <= vals[i+1]:
            return 0.0
    return 1.0


_SCORERS = {
    'numeric_values': score_0,
    'lattice_ordering': score_1,
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
