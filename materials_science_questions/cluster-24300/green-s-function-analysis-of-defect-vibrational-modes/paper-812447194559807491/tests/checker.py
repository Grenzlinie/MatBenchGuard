import os
import json
import csv

# === author imports / helpers ===
import math

def _frac_score(agent_val, gold_val, rel_tol, abs_tol):
    if gold_val == 0:
        max_err = abs_tol
    else:
        max_err = max(rel_tol * abs(gold_val), abs_tol)
    err = abs(agent_val - gold_val)
    if err <= max_err:
        return 1.0
    else:
        excess = err - max_err
        penalty = excess / (abs(gold_val) + 1e-12)
        return max(0.0, 1.0 - penalty)

IMPURITY_MAP = {
    "vacancy": "vac.", "Vacancy": "vac.", "VAC.": "vac.", "vac": "vac.",
    "ag": "Ag", "AG": "Ag", "silver": "Ag",
    "mg": "Mg", "MG": "Mg",
    "zn": "Zn", "ZN": "Zn",
    "cd": "Cd", "CD": "Cd",
    "hg": "Hg", "HG": "Hg",
    "ga": "Ga", "GA": "Ga",
    "tl": "Tl", "TL": "Tl",
    "sn": "Sn", "SN": "Sn",
    "pb": "Pb", "PB": "Pb",
    "sb": "Sb", "SB": "Sb",
    "bi": "Bi", "BI": "Bi",
}


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
    ctx = {}
    for step in spec['steps']:
        step_id = step['id']
        gold_rows = step.get('gold_table', [])
        rel_tol = step.get('relative_tolerance', 0.1)
        abs_tol = step.get('absolute_tolerance', 0.05)
    
        if step_id == 'scattering_rates':
            lookup = {}
            for r in gold_rows:
                imp = IMPURITY_MAP.get(r['impurity'], r['impurity'])
                key = (imp, r['zone'])
                lookup[key] = (r['tau0_inv'], r['tau_inv'])
            ctx[step_id] = {'lookup': lookup, 'rel_tol': rel_tol, 'abs_tol': abs_tol}
        elif step_id == 'resistivities':
            lookup = {}
            for r in gold_rows:
                imp = IMPURITY_MAP.get(r['impurity'], r['impurity'])
                lookup[imp] = r['resistivity_6psiPW']
            ctx[step_id] = {'lookup': lookup, 'rel_tol': rel_tol, 'abs_tol': abs_tol}
        elif step_id == 'dingle_temperatures':
            lookup = {}
            for r in gold_rows:
                imp = IMPURITY_MAP.get(r['impurity'], r['impurity'])
                key = (imp, r['orbit'])
                lookup[key] = r['T_D']
            ctx[step_id] = {'lookup': lookup, 'rel_tol': rel_tol, 'abs_tol': abs_tol}
        else:
            ctx[step_id] = {}
    return ctx


# === block: score_0 (check id='scattering_rates') ===
def score_0(artifact, step, ctx):
    ctx_step = ctx['scattering_rates']
    lookup = ctx_step['lookup']
    rel_tol = ctx_step['rel_tol']
    abs_tol = ctx_step['abs_tol']
    scores = []
    for row in artifact:
        imp_raw = row.get('impurity', '')
        imp = IMPURITY_MAP.get(imp_raw, imp_raw)
        zone = row.get('zone', '')
        key = (imp, zone)
        if key not in lookup:
            scores.append(0.0)
            continue
        gold_tau0, gold_tau_inv = lookup[key]
        try:
            tau0 = float(row['tau0_inv'])
            tau_inv = float(row['tau_inv'])
        except (ValueError, KeyError):
            scores.append(0.0)
            continue
        s0 = _frac_score(tau0, gold_tau0, rel_tol, abs_tol)
        s1 = _frac_score(tau_inv, gold_tau_inv, rel_tol, abs_tol)
        scores.append((s0 + s1) / 2.0)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_1 (check id='resistivities') ===
def score_1(artifact, step, ctx):
    ctx_step = ctx['resistivities']
    lookup = ctx_step['lookup']
    rel_tol = ctx_step['rel_tol']
    abs_tol = ctx_step['abs_tol']
    scores = []
    for row in artifact:
        imp_raw = row.get('impurity', '')
        imp = IMPURITY_MAP.get(imp_raw, imp_raw)
        if imp not in lookup:
            scores.append(0.0)
            continue
        gold_val = lookup[imp]
        try:
            agent_val = float(row['resistivity_6psiPW'])
        except (ValueError, KeyError):
            scores.append(0.0)
            continue
        scores.append(_frac_score(agent_val, gold_val, rel_tol, abs_tol))
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_2 (check id='dingle_temperatures') ===
def score_2(artifact, step, ctx):
    ctx_step = ctx['dingle_temperatures']
    lookup = ctx_step['lookup']
    rel_tol = ctx_step['rel_tol']
    abs_tol = ctx_step['abs_tol']
    scores = []
    for row in artifact:
        imp_raw = row.get('impurity', '')
        imp = IMPURITY_MAP.get(imp_raw, imp_raw)
        orbit = row.get('orbit', '')
        key = (imp, orbit)
        if key not in lookup:
            scores.append(0.0)
            continue
        gold_val = lookup[key]
        try:
            agent_val = float(row['T_D'])
        except (ValueError, KeyError):
            scores.append(0.0)
            continue
        scores.append(_frac_score(agent_val, gold_val, rel_tol, abs_tol))
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


_SCORERS = {
    'scattering_rates': score_0,
    'resistivities': score_1,
    'dingle_temperatures': score_2,
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
