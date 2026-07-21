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
    def prepare(outputs_dir, spec):
        return {}  # gold is embedded in each step


# === block: score_0 (check id='phase_boundary') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold = step['gold']
        tol = step['tolerance_Uc']
        entries = artifact.get('metallic_phase_boundary', [])
        agent = {}
        for e in entries:
            key = (e.get('N'), e.get('epsilon_f_over_V'))
            agent[key] = e.get('U_c_over_V')
        hits = 0
        for g in gold:
            key = (g['N'], g['epsilon_f_over_V'])
            val = agent.get(key)
            if val is not None and abs(val - g['U_c_over_V']) <= tol:
                hits += 1
        return hits / len(gold) if gold else 0.0


# === block: score_1 (check id='magnetization') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold = step['gold']
        tol = step['tolerance_m']
        entries = artifact.get('metallic_magnetization', [])
        agent = {}
        for e in entries:
            key = (e.get('N'), e.get('epsilon_f_over_V'), e.get('B_over_V'))
            agent[key] = e.get('magnetization')
        hits = 0
        for g in gold:
            key = (g['N'], g['epsilon_f_over_V'], g['B_over_V'])
            val = agent.get(key)
            if val is not None and abs(val - g['magnetization']) <= tol:
                hits += 1
        return hits / len(gold) if gold else 0.0


# === block: score_2 (check id='occupations') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold = step['gold']
        tol = step['tolerance_prob']
        entries = artifact.get('metallic_occupations', [])
        agent = {}
        for e in entries:
            key = (e.get('N'), e.get('epsilon_f_over_V'))
            agent[key] = e
        hits = 0
        fields = ['e2','p2','d2','n_f']
        for g in gold:
            key = (g['N'], g['epsilon_f_over_V'])
            e = agent.get(key)
            if e is not None:
                ok = True
                for f in fields:
                    if abs(e.get(f, 0.0) - g[f]) > tol:
                        ok = False
                        break
                if ok:
                    hits += 1
        return hits / len(gold) if gold else 0.0


# === block: score_3 (check id='kondo_insulator') ===
def score_3(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold = step['gold']
        tol_prob = step['tolerance_prob']
        tol_abs = step['tol_gap_abs']
        tol_rel = step['tol_gap_rel']
        entries = artifact.get('kondo_insulator', [])
        agent = {}
        for e in entries:
            key = e.get('U_over_V')
            agent[key] = e
        hits = 0
        for g in gold:
            key = g['U_over_V']
            e = agent.get(key)
            if e is not None:
                if (abs(e.get('e2',0.0)-g['e2']) <= tol_prob and
                    abs(e.get('p2',0.0)-g['p2']) <= tol_prob and
                    abs(e.get('d2',0.0)-g['d2']) <= tol_prob and
                    abs(e.get('gap_over_V',0.0)-g['gap_over_V']) <= max(tol_abs, tol_rel*abs(g['gap_over_V']))):
                    hits += 1
        return hits / len(gold) if gold else 0.0


_SCORERS = {
    'phase_boundary': score_0,
    'magnetization': score_1,
    'occupations': score_2,
    'kondo_insulator': score_3,
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
