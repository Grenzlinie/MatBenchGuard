import os
import json
import csv

# === author imports / helpers ===
import os
import json


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
    def compute_bandgap(filepath):
        try:
            with open(filepath, 'r') as f:
                content = f.read()
        except:
            return None
        eigenvalues = []
        for line in content.splitlines():
            line = line.strip()
            if not line: continue
            parts = line.split()
            if len(parts) != 4: continue
            try:
                e = float(parts[3])
                eigenvalues.append(e)
            except: continue
        if not eigenvalues: return None
        vbm_candidates = [e for e in eigenvalues if e <= 0.0]
        if not vbm_candidates: return None
        vbm = max(vbm_candidates)
        cbm_candidates = [e for e in eigenvalues if e > 0.0]
        if not cbm_candidates: return None
        cbm = min(cbm_candidates)
        return cbm - vbm

    outputs_dir = '/app/outputs'
    pristine_gap = compute_bandgap(os.path.join(outputs_dir, 'bandstructure_pristine.dat'))
    cb_gap = compute_bandgap(os.path.join(outputs_dir, 'bandstructure_N_charge_balanced.dat'))
    ex_gap = compute_bandgap(os.path.join(outputs_dir, 'bandstructure_N_excess_Vac.dat'))

    dielectric = None
    try:
        with open(os.path.join(outputs_dir, 'dielectric_constants.json')) as f:
            dielectric = json.load(f)
    except: pass

    polaron = None
    try:
        with open(os.path.join(outputs_dir, 'polaron_properties.json')) as f:
            polaron = json.load(f)
    except: pass

    absorption = None
    try:
        with open(os.path.join(outputs_dir, 'absorption_edge.json')) as f:
            absorption = json.load(f)
    except: pass

    return {
        'pristine_gap': pristine_gap,
        'cb_gap': cb_gap,
        'ex_gap': ex_gap,
        'dielectric': dielectric,
        'polaron': polaron,
        'absorption': absorption
    }


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    gap = ctx.get('pristine_gap')
    if gap is None:
        return 0.0
    target = 2.25
    err = abs(gap - target)
    if err <= 0.2:
        return 1.0
    elif err >= 0.5:
        return 0.0
    else:
        return 1.0 - (err - 0.2) / 0.3


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    pristine = ctx.get('pristine_gap')
    cb = ctx.get('cb_gap')
    if pristine is None or cb is None:
        return 0.0
    reduction = pristine - cb
    if reduction >= 0.3:
        return 1.0
    elif reduction <= 0.0:
        return 0.0
    else:
        return reduction / 0.3


# === block: score_2 (check id='step_03') ===
def score_2(artifact, step, ctx):
    pristine = ctx.get('pristine_gap')
    ex = ctx.get('ex_gap')
    if pristine is None or ex is None:
        return 0.0
    reduction = pristine - ex
    if reduction >= 0.25:
        return 1.0
    elif reduction <= 0.05:
        return 0.0
    else:
        return (reduction - 0.05) / 0.2


# === block: score_3 (check id='step_04') ===
def score_3(artifact, step, ctx):
    die = ctx.get('dielectric')
    if die is None:
        return 0.0
    targets = {
        'pristine_epsilon_inf': (6.9, 1.38),
        'pristine_epsilon_0': (52.0, 10.4),
        'N_doped_epsilon_inf': (6.2, 1.24),
        'N_doped_epsilon_0': (27.0, 5.4)
    }
    scores = []
    for key, (tgt, tol) in targets.items():
        val = die.get(key)
        if val is None:
            scores.append(0.0)
        else:
            diff = abs(val - tgt)
            s = max(0.0, 1.0 - diff / tol) if tol > 0 else 1.0
            scores.append(s)
    return sum(scores) / len(scores)


# === block: score_4 (check id='step_05') ===
def score_4(artifact, step, ctx):
    pol = ctx.get('polaron')
    if pol is None:
        return 0.0
    mob = pol.get('mobility_enhancement_percent')
    if mob is None:
        return 0.0
    if mob >= 20.0:
        return 1.0
    else:
        return max(0.0, mob / 20.0)


# === block: score_5 (check id='step_06') ===
def score_5(artifact, step, ctx):
    absor = ctx.get('absorption')
    if absor is None:
        return 0.0
    redshift = absor.get('redshift_eV')
    if redshift is None:
        return 0.0
    if abs(redshift - 0.3) <= 0.1:
        return 1.0
    else:
        return 0.0


_SCORERS = {
    'step_01': score_0,
    'step_02': score_1,
    'step_03': score_2,
    'step_04': score_3,
    'step_05': score_4,
    'step_06': score_5,
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
