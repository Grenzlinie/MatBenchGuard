import os
import json
import csv

# === author imports / helpers ===
import json, os, re


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
    gold_strings = {
        'rutile': 'A1g(R)+A2g(-)+B1g(R)+B2g(R)+Eg(R)+A2u(IR,E||c)+2B1u(-)+3Eu(IR,E⊥c)',
        'anatase': 'A1g(R)+2B1g(R)+3Eg(R)+A2u(IR,E||c)+B2u(-)+2Eu(IR,E⊥c)',
        'brookite': '9Ag(R)+9B1g(R)+9B2g(R)+9B3g(R)+9Au(-)+8B1u(IR,E||c)+8B2u(IR,E||b)+8B3u(IR,E||a)',
        'corundum_alpha_Ga2O3': '2A1g(R)+3A2g(-)+5Eg(R)+2A1u(-)+2A2u(IR,E||c)+4Eu(IR,E⊥c)',
        'beta_Ga2O3': '20Ag(R)+10Bg(R)+9Au(IR,E||b)+18Bu(IR,E⊥b)',
        'cubic_ZrO2': 'T1u(IR)+T2g(R)',
        'monoclinic_ZrO2': '9Ag(R)+9Bg(R)+8Au(IR,E||b)+7Bu(IR,E⊥b)',
        'Li3NbO4': '8A1(R)+8E(R)+23T(IR+R)',
        'ilmenite_MnTiO3': '6Ag(R)+5Eg(R)+4Au(IR,E||c)+4Eu(IR,E⊥c)',
        'ordered_LiAl5O8': '6A1(R)+8A2(-)+14E(R)+20T2(R)+21T1(IR)',
        'trirutile_ZnSb2O6': '3A1g(R)+3A2g(-)+3B1g(R)+3B2g(R)+3Eg(R)+5A2u(IR,E||c)+6B1u(-)+11Eu(IR,E⊥c)',
        'trirutile_MgSb2O6': '3A1g(R)+3A2g(-)+3B1g(R)+3B2g(R)+3Eg(R)+5A2u(IR,E||c)+6B1u(-)+11Eu(IR,E⊥c)'
    }
    # Sort terms for each gold string (already sorted above, but to be safe we sort)
    def _sort_terms(norm):
        terms = [t.strip() for t in norm.split('+')]
        terms.sort()
        return '+'.join(terms)
    for k in gold_strings:
        gold_strings[k] = _sort_terms(gold_strings[k])
    return {'gold': gold_strings}


# === block: score_0 (check id='step_factor_group') ===
def score_0(artifact, step, ctx):
    import re
    artifact = load_artifact(os.path.join('/app/outputs', 'factor_group_decompositions.json'))
    gold = ctx['gold']
    keys = list(gold.keys())
    def normalize(s):
        # remove all whitespace
        s = re.sub(r'\s+', '', s)
        # unify various dash/minus
        s = s.replace('−', '-').replace('–', '-').replace('—', '-')
        # unify common string differences (E || c -> E||c)
        s = s.replace('|', '|')
        # remove leading/trailing spaces from terms later
        terms = [t.strip() for t in s.split('+') if t.strip()]
        # sort terms
        terms.sort()
        return '+'.join(terms)
    match = 0
    total = len(keys)
    for k in keys:
        try:
            agent_decomp = artifact[k].get('decomposition', '')
        except (KeyError, TypeError):
            continue
        if normalize(agent_decomp) == gold[k]:
            match += 1
    return match / total if total > 0 else 0.0


_SCORERS = {
    'step_factor_group': score_0,
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
