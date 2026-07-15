import os
import json
import csv

# === author imports / helpers ===
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
    return {}  # gold is accessed directly from step dict inside each scorer


# === block: score_0 (check id='step_compute_uniform') ===
def score_0(artifact, step, ctx):
    gold_rows = step['gold']
    abs_tol = step.get('tolerance_energy_abs', 0.01)
    rel_tol = step.get('tolerance_energy_rel', 0.01)
    expected = {float(r['rs']): r for r in gold_rows}
    artifacts = {float(row['rs']): row for row in artifact}
    total = len(expected)
    ok = 0
    for rs, ge in expected.items():
        ae = artifacts.get(rs)
        if ae is None:
            continue
        # check nonmagnetic and ferromagnetic
        nm_ok = False
        fm_ok = False
        try:
            val_nm = float(ae['nonmagnetic_energy'])
            val_fm = float(ae['ferromagnetic_energy'])
            tol_nm = max(abs_tol, rel_tol * abs(float(ge['nonmagnetic_energy'])))
            tol_fm = max(abs_tol, rel_tol * abs(float(ge['ferromagnetic_energy'])))
            if abs(val_nm - float(ge['nonmagnetic_energy'])) <= tol_nm:
                nm_ok = True
            if abs(val_fm - float(ge['ferromagnetic_energy'])) <= tol_fm:
                fm_ok = True
        except (ValueError, KeyError):
            pass
        # electron gas: just must be negative
        eg_ok = False
        try:
            val_eg = float(ae['electron_gas_energy'])
            if val_eg < 0:
                eg_ok = True
        except (ValueError, KeyError):
            pass
        if nm_ok and fm_ok and eg_ok:
            ok += 1
    return ok / total if total else 0.0


# === block: score_1 (check id='step_compute_yukawa') ===
def score_1(artifact, step, ctx):
    gold_rows = step['gold']
    abs_tol = step.get('tolerance_energy_abs', 0.01)
    rel_tol = step.get('tolerance_energy_rel', 0.01)
    expected = {float(r['rs']): r for r in gold_rows}
    artifacts = {float(row['rs']): row for row in artifact}
    total = len(expected)
    ok = 0
    for rs, ge in expected.items():
        ae = artifacts.get(rs)
        if ae is None:
            continue
        nm_ok = False
        fm_ok = False
        try:
            val_nm = float(ae['nonmagnetic_energy'])
            val_fm = float(ae['ferromagnetic_energy'])
            tol_nm = max(abs_tol, rel_tol * abs(float(ge['nonmagnetic_energy'])))
            tol_fm = max(abs_tol, rel_tol * abs(float(ge['ferromagnetic_energy'])))
            if abs(val_nm - float(ge['nonmagnetic_energy'])) <= tol_nm:
                nm_ok = True
            if abs(val_fm - float(ge['ferromagnetic_energy'])) <= tol_fm:
                fm_ok = True
        except (ValueError, KeyError):
            pass
        eg_ok = False
        try:
            val_eg = float(ae['electron_gas_energy'])
            if val_eg < 0:
                eg_ok = True
        except (ValueError, KeyError):
            pass
        if nm_ok and fm_ok and eg_ok:
            ok += 1
    return ok / total if total else 0.0


# === block: score_2 (check id='step_critical_densities') ===
def score_2(artifact, step, ctx):
    try:
        gold = step['gold']
        nr = float(artifact.get('nonmagnetic_critical_r_s'))
        nd = float(artifact.get('nonmagnetic_critical_density_cm2'))
        fr = float(artifact.get('ferromagnetic_critical_r_s'))
        fd = float(artifact.get('ferromagnetic_critical_density_cm2'))
    except (TypeError, KeyError, ValueError):
        return 0.0

    tol_rs = step.get('tolerance_r_s', 2)
    tol_density = step.get('tolerance_density_rel', 0.15)

    score = 0.0
    if abs(nr - gold['nonmagnetic_critical_r_s']) <= tol_rs:
        score += 0.25
    if abs(nd - gold['nonmagnetic_critical_density_cm2']) <= tol_density * gold['nonmagnetic_critical_density_cm2']:
        score += 0.25
    if abs(fr - gold['ferromagnetic_critical_r_s']) <= tol_rs:
        score += 0.25
    if abs(fd - gold['ferromagnetic_critical_density_cm2']) <= tol_density * gold['ferromagnetic_critical_density_cm2']:
        score += 0.25
    return score


_SCORERS = {
    'step_compute_uniform': score_0,
    'step_compute_yukawa': score_1,
    'step_critical_densities': score_2,
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
