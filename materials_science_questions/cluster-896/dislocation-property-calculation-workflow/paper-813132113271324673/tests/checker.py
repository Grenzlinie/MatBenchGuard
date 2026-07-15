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


# === block: score_0 (check id='stress_strain_verification') ===
def score_0(artifact, step, ctx):
    cfg = step['config']
    gold = cfg['gold']
    tol = cfg['tolerance_rel']
    agent_rows = artifact
    # Build lookup by strain
    agent = {}
    for r in agent_rows:
        try:
            s = float(r['strain'])
            agent[s] = (float(r.get('stress_111',0.0)), float(r.get('stress_100',0.0)))
        except:
            continue
    passes = 0
    total = len(gold['strain'])
    for i, strain in enumerate(gold['strain']):
        if strain not in agent:
            continue
        a111, a100 = agent[strain]
        g111 = gold['stress_111'][i]
        g100 = gold['stress_100'][i]
        if abs(a111 - g111) <= tol * abs(g111) + 1e-9 and abs(a100 - g100) <= tol * abs(g100) + 1e-9:
            passes += 1
    return passes / total if total > 0 else 0.0


# === block: score_1 (check id='single_crystal_stored_energy') ===
def score_1(artifact, step, ctx):
    # Embed correct gold from paper's Figure 2b as reproduced by reference solve.
    correct_gold = {
        "strain": [0.0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.34],
        "stored_energy_111": [0.0, 0.45, 0.98, 1.62, 2.31, 3.08, 3.82, 4.25],
        "stored_energy_100": [0.0, 0.34, 0.75, 1.24, 1.82, 2.45, 3.12, 3.52],
    }
    tol = 0.15  # generous tolerance for re-implementation variability
    agent_rows = artifact
    agent = {}
    for r in agent_rows:
        try:
            s = float(r['strain'])
            agent[s] = (float(r.get('stored_energy_111',0.0)), float(r.get('stored_energy_100',0.0)))
        except:
            continue
    passes = 0
    total = len(correct_gold['strain'])
    ordering_ok = True
    for i, strain in enumerate(correct_gold['strain']):
        if strain not in agent:
            continue
        a111, a100 = agent[strain]
        g111 = correct_gold['stored_energy_111'][i]
        g100 = correct_gold['stored_energy_100'][i]
        if abs(a111 - g111) <= tol * abs(g111) + 1e-9 and abs(a100 - g100) <= tol * abs(g100) + 1e-9:
            passes += 1
        if a111 <= a100:
            ordering_ok = False
    score_val = passes / total if total > 0 else 0.0
    if not ordering_ok:
        score_val *= 0.5
    return max(0.0, min(1.0, score_val))


# === block: score_2 (check id='bicrystal_stored_energy') ===
def score_2(artifact, step, ctx):
    cfg = step['config']
    gold_entries = cfg['gold']
    tol = cfg['tolerance_rel']
    agent_rows = artifact
    # Build dict keyed by (bicrystal, grain)
    agent = {}
    for r in agent_rows:
        bc = r.get('bicrystal','').strip()
        gr = r.get('grain','').strip()
        try:
            v = float(r['stored_energy_avg'])
            agent[(bc, gr)] = v
        except:
            continue
    matches = 0
    total = len(gold_entries)
    ordering_ok = True
    for g in gold_entries:
        key = (g['bicrystal'], g['grain'])
        if key in agent:
            av = agent[key]
            gv = g['stored_energy_avg']
            if abs(av - gv) <= tol * abs(gv) + 1e-9:
                matches += 1
    # ordering check
    if cfg.get('check_ordering', False):
        if agent.get(('Bicrystal_001_111','111'), 0) <= agent.get(('Bicrystal_001_111','001'), 0):
            ordering_ok = False
        if agent.get(('Bicrystal_001_634','634'), 0) <= agent.get(('Bicrystal_001_634','001'), 0):
            ordering_ok = False
    score_val = matches / total if total > 0 else 0.0
    if cfg.get('check_ordering', False) and not ordering_ok:
        score_val *= 0.5
    return max(0.0, min(1.0, score_val))


_SCORERS = {
    'stress_strain_verification': score_0,
    'single_crystal_stored_energy': score_1,
    'bicrystal_stored_energy': score_2,
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
