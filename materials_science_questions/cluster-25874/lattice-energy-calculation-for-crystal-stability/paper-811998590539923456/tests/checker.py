import os
import json
import csv

# === author imports / helpers ===
import math, json


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
    return spec.get('gold', {})


# === block: score_0 (check id='shape_check') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    required = ['anion_volume_nm3', 'cation_volumes_nm3', 'lattice_energies_kJmol']
    if not all(k in artifact for k in required):
        return 0.0
    try:
        cv = artifact['cation_volumes_nm3']
        le = artifact['lattice_energies_kJmol']
        for i in range(1,10):
            label = str(i)
            if label not in cv or not isinstance(cv[label], (int,float)):
                return 0.0
            entry = le.get(label)
            if not isinstance(entry, dict) or not all(k in entry for k in ('UL','dHL','dGL')):
                return 0.0
    except Exception:
        return 0.0
    return 1.0


# === block: score_1 (check id='lattice_energies_check') ===
def score_1(artifact, step, ctx):
    gold_energies = ctx.get('paper_lattice_energies', {})
    tolerance = step.get('tolerance_kJmol', 5.0)
    anion_vol = artifact.get('anion_volume_nm3')
    if not isinstance(anion_vol, (int,float)):
        return 0.0
    cation_volumes = artifact.get('cation_volumes_nm3', {})
    total = 0
    passed = 0
    for label in [str(i) for i in range(1,10)]:
        v_cat = cation_volumes.get(label)
        gold_entry = gold_energies.get(label)
        if not isinstance(v_cat, (int,float)) or not isinstance(gold_entry, dict):
            continue
        V = v_cat + anion_vol
        if V <= 0:
            continue
        UL_recomp = 2.0 * (117.3 * (V ** (-1.0/3.0)) + 51.9)
        dHL_recomp = UL_recomp + 5.0
        dGL_recomp = dHL_recomp - 298.0 * (1360.0 * V + 15.0) / 1000.0
        for key in ('UL','dHL','dGL'):
            total += 1
            try:
                if abs(locals()[key+'_recomp'] - gold_entry[key]) <= tolerance:
                    passed += 1
            except KeyError:
                pass
    return passed / total if total > 0 else 0.0


# === block: score_2 (check id='cation_volume_correlation_check') ===
def score_2(artifact, step, ctx):
    gold_volumes = ctx.get('experimental_cation_volumes_nm3', {})
    agent_volumes = artifact.get('cation_volumes_nm3', {})
    if not isinstance(agent_volumes, dict):
        return 0.0
    x = []
    y = []
    for label in sorted(gold_volumes.keys()):
        ax = gold_volumes[label]
        ay = agent_volumes.get(label)
        if isinstance(ax, (int,float)) and isinstance(ay, (int,float)):
            x.append(ax)
            y.append(ay)
    if len(x) < 2:
        return 0.0
    n = len(x)
    mean_x = sum(x)/n
    mean_y = sum(y)/n
    cov = sum((x[i]-mean_x)*(y[i]-mean_y) for i in range(n))
    var_x = sum((xi-mean_x)**2 for xi in x)
    var_y = sum((yi-mean_y)**2 for yi in y)
    if var_x == 0 or var_y == 0:
        return 0.0
    r = cov / math.sqrt(var_x * var_y)
    r2 = r**2
    return 1.0 if r2 >= 0.97 else 0.0


_SCORERS = {
    'shape_check': score_0,
    'lattice_energies_check': score_1,
    'cation_volume_correlation_check': score_2,
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
