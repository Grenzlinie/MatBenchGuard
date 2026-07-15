import os
import json
import csv

# === author imports / helpers ===
import os
import json
import csv
import math


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
    def load_json(path):
        with open(path) as f:
            return json.load(f)

    def load_csv(path):
        with open(path, newline='') as f:
            return list(csv.DictReader(f))

    outputs_dir = outputs_dir  # provided by scaffold
    ctx = {}
    try:
        ctx['critical'] = load_json(os.path.join(outputs_dir, 'critical_radius.json'))
    except:
        ctx['critical'] = None
    try:
        ctx['burst_csv'] = load_csv(os.path.join(outputs_dir, 'burst_energy_vs_molecules.csv'))
    except:
        ctx['burst_csv'] = None
    try:
        ctx['fitted_slope'] = load_json(os.path.join(outputs_dir, 'fitted_slope.json'))
    except:
        ctx['fitted_slope'] = None
    try:
        ctx['nucleation'] = load_csv(os.path.join(outputs_dir, 'nucleation_outcomes.csv'))
    except:
        ctx['nucleation'] = None
    return ctx


# === block: score_0 (check id='critical_radius') ===
def score_0(artifact, step, ctx):
    artifact = ctx.get('critical')
    if artifact is None:
        return 0.0
    R_c = artifact.get('R_c_nm')
    if R_c is None:
        return 0.0
    target = step.get('target', 3.8)
    tolerance = step.get('tolerance', 0.5)
    if abs(R_c - target) <= tolerance:
        return 1.0
    else:
        return 0.0


# === block: score_1 (check id='burst_csv') ===
def score_1(artifact, step, ctx):
    rows = ctx.get('burst_csv')
    if not rows:
        return 0.0
    sum_xy = 0.0
    sum_x2 = 0.0
    energy_col = step.get('columns', {}).get('energy', 'burst_total_energy_kJ_per_mol')
    mol_col = step.get('columns', {}).get('molecules', 'burst_molecules_count')
    for r in rows:
        try:
            e = float(r.get(energy_col, 0))
            m = float(r.get(mol_col, 0))
            sum_xy += e * m
            sum_x2 += m * m
        except:
            continue
    if sum_x2 == 0:
        return 0.0
    slope = sum_xy / sum_x2
    target = step.get('target', 53.5)
    tol = step.get('tolerance_relative', 0.30)
    rel_err = abs(slope - target) / target if target != 0 else float('inf')
    if rel_err <= tol:
        return 1.0
    else:
        # linearly decay to 0 at twice the tolerance
        score = max(0.0, 1.0 - (rel_err - tol) / tol)
        return score


# === block: score_2 (check id='fitted_slope') ===
def score_2(artifact, step, ctx):
    artifact = ctx.get('fitted_slope')
    if artifact is None:
        return 0.0
    reported = artifact.get('E_mol0_kJ_per_mol')
    if reported is None:
        return 0.0
    # recompute slope from burst CSV
    rows = ctx.get('burst_csv')
    if not rows:
        return 0.0
    sum_xy = 0.0
    sum_x2 = 0.0
    energy_col = 'burst_total_energy_kJ_per_mol'
    mol_col = 'burst_molecules_count'
    for r in rows:
        try:
            e = float(r.get(energy_col, 0))
            m = float(r.get(mol_col, 0))
            sum_xy += e * m
            sum_x2 += m * m
        except:
            continue
    if sum_x2 == 0:
        recomputed = 0.0
    else:
        recomputed = sum_xy / sum_x2
    if abs(reported - recomputed) < 1e-6:
        return 1.0
    return 0.0


# === block: score_3 (check id='nucleation') ===
def score_3(artifact, step, ctx):
    rows = ctx.get('nucleation')
    if not rows:
        return 0.0
    expect = step.get('expected_conditions', [])
    if not expect:
        return 1.0
    # normalize rows: convert to dict with string keys and lowercased values for nucleation_occurred
    norm_rows = []
    for r in rows:
        nr = {}
        for k, v in r.items():
            if k == 'nucleation_occurred':
                val = str(v).strip().lower()
                nr[k] = val
            else:
                try:
                    nr[k] = float(v)
                except:
                    nr[k] = v
        norm_rows.append(nr)
    ok = 0
    for exp in expect:
        match = False
        for nr in norm_rows:
            if (abs(nr.get('pressure_GPa', 0) - exp.get('pressure_GPa', 0)) < 1e-6 and
                abs(nr.get('velocity_m_per_s', 0) - exp.get('velocity_m_per_s', 0)) < 1e-6 and
                nr.get('nucleation_occurred') == str(exp.get('nucleation_occurred')).lower()):
                match = True
                break
        if match:
            ok += 1
    return ok / len(expect)


_SCORERS = {
    'critical_radius': score_0,
    'burst_csv': score_1,
    'fitted_slope': score_2,
    'nucleation': score_3,
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
