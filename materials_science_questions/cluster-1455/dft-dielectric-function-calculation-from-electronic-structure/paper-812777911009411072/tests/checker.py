import os
import json
import csv

# === author imports / helpers ===
import json
import csv
import sys
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
    return {}


# === block: score_0 (check id='check_results_Er') ===
def score_0(artifact, step, ctx):
    if artifact is None:
        return 0.0
    gold = step.get('target', {})
    tol = float(step.get('tolerance_abs', 0.1))
    # Reference ground state energy of polar_surface
    ps = artifact.get('polar_surface')
    if ps is None:
        return 0.0
    try:
        ref_e = min(ps['total_energy_FM'], ps['total_energy_AFM'])
    except (KeyError, TypeError):
        return 0.0
    configs = artifact
    pass_count = 0
    total = 0
    for cfg_name, target_er in gold.items():
        cfg = configs.get(cfg_name)
        if cfg is None:
            continue
        total += 1
        try:
            e_gs = min(cfg['total_energy_FM'], cfg['total_energy_AFM'])
            er = e_gs - ref_e
        except (KeyError, TypeError):
            continue
        if abs(er - target_er) <= tol:
            pass_count += 1
    if total == 0:
        return 0.0
    return pass_count / total


# === block: score_1 (check id='check_results_DeltaE') ===
def score_1(artifact, step, ctx):
    if artifact is None:
        return 0.0
    gold = step.get('target', {})
    tol = float(step.get('tolerance_abs', 10.0))  # meV
    configs = artifact
    pass_count = 0
    total = 0
    for cfg_name, target_de in gold.items():
        cfg = configs.get(cfg_name)
        if cfg is None:
            continue
        total += 1
        try:
            de = (cfg['total_energy_AFM'] - cfg['total_energy_FM']) * 1000.0  # eV -> meV
        except (KeyError, TypeError):
            continue
        if abs(de - target_de) <= tol:
            pass_count += 1
    if total == 0:
        return 0.0
    return pass_count / total


# === block: score_2 (check id='check_results_mag_total') ===
def score_2(artifact, step, ctx):
    if artifact is None:
        return 0.0
    gold = step.get('target', {})
    tol = float(step.get('tolerance_abs', 0.5))
    configs = artifact
    pass_count = 0
    total = 0
    for cfg_name, target_mag in gold.items():
        cfg = configs.get(cfg_name)
        if cfg is None:
            continue
        total += 1
        try:
            mag = cfg['total_magnetic_moment_muB']
        except (KeyError, TypeError):
            continue
        if abs(mag - target_mag) <= tol:
            pass_count += 1
    if total == 0:
        return 0.0
    return pass_count / total


# === block: score_3 (check id='check_results_mag_Ni') ===
def score_3(artifact, step, ctx):
    if artifact is None:
        return 0.0
    gold = step.get('target', {})
    tol = float(step.get('tolerance_abs', 0.5))
    configs = artifact
    pass_count = 0
    total = 0
    for cfg_name, target_moms in gold.items():
        cfg = configs.get(cfg_name)
        if cfg is None:
            continue
        try:
            ni1 = cfg['magnetic_moment_Ni1_muB']
            ni2 = cfg['magnetic_moment_Ni2_muB']
        except (KeyError, TypeError):
            continue
        if len(target_moms) != 2:
            continue
        for reported, target in [(ni1, target_moms[0]), (ni2, target_moms[1])]:
            total += 1
            if abs(reported - target) <= tol:
                pass_count += 1
    if total == 0:
        return 0.0
    return pass_count / total


# === block: score_4 (check id='check_results_ground_state') ===
def score_4(artifact, step, ctx):
    if artifact is None:
        return 0.0
    gold = step.get('target', {})
    configs = artifact
    pass_count = 0
    total = 0
    for cfg_name, expected_gs in gold.items():
        cfg = configs.get(cfg_name)
        if cfg is None:
            continue
        total += 1
        try:
            gs = cfg['ground_state']
        except (KeyError, TypeError):
            continue
        if gs == expected_gs:
            pass_count += 1
    if total == 0:
        return 0.0
    return pass_count / total


# === block: score_5 (check id='check_dos_bulk') ===
def score_5(artifact, step, ctx):
    path = '/app/outputs/dos_nonpolar_bulk.dat'
    try:
        with open(path, newline='') as f:
            reader = csv.DictReader(f, delimiter='\t')
            rows = list(reader)
    except Exception:
        return 0.0
    if not rows:
        return 0.0
    # Find row with energy closest to 0.0
    best_err = float('inf')
    best_row = None
    for row in rows:
        try:
            e = float(row['Energy(eV)'])
            err = abs(e)
            if err < best_err:
                best_err = err
                best_row = row
        except (ValueError, KeyError):
            continue
    if best_row is None or best_err > 0.05:  # must have a row within 0.05 eV of Fermi level
        return 0.0
    try:
        dos_up = float(best_row['DOS_up'])
        dos_down = float(best_row['DOS_down'])
    except (ValueError, KeyError):
        return 0.0
    half_metal = (dos_up < 0.1 and dos_down > 0.1) or (dos_up > 0.1 and dos_down < 0.1)
    return 1.0 if half_metal else 0.0


# === block: score_6 (check id='check_dos_surface') ===
def score_6(artifact, step, ctx):
    path = '/app/outputs/dos_nonpolar_surface.dat'
    try:
        with open(path, newline='') as f:
            reader = csv.DictReader(f, delimiter='\t')
            rows = list(reader)
    except Exception:
        return 0.0
    if not rows:
        return 0.0
    best_err = float('inf')
    best_row = None
    for row in rows:
        try:
            e = float(row['Energy(eV)'])
            err = abs(e)
            if err < best_err:
                best_err = err
                best_row = row
        except (ValueError, KeyError):
            continue
    if best_row is None or best_err > 0.05:
        return 0.0
    try:
        dos_up = float(best_row['DOS_up'])
        dos_down = float(best_row['DOS_down'])
    except (ValueError, KeyError):
        return 0.0
    half_metal = (dos_up < 0.1 and dos_down > 0.1) or (dos_up > 0.1 and dos_down < 0.1)
    return 1.0 if half_metal else 0.0


# === block: score_7 (check id='check_dos_mixed') ===
def score_7(artifact, step, ctx):
    path = '/app/outputs/dos_nonpolar_mixed.dat'
    try:
        with open(path, newline='') as f:
            reader = csv.DictReader(f, delimiter='\t')
            rows = list(reader)
    except Exception:
        return 0.0
    if not rows:
        return 0.0
    best_err = float('inf')
    best_row = None
    for row in rows:
        try:
            e = float(row['Energy(eV)'])
            err = abs(e)
            if err < best_err:
                best_err = err
                best_row = row
        except (ValueError, KeyError):
            continue
    if best_row is None or best_err > 0.05:
        return 0.0
    try:
        dos_up = float(best_row['DOS_up'])
        dos_down = float(best_row['DOS_down'])
    except (ValueError, KeyError):
        return 0.0
    half_metal = (dos_up < 0.1 and dos_down > 0.1) or (dos_up > 0.1 and dos_down < 0.1)
    return 1.0 if half_metal else 0.0


_SCORERS = {
    'check_results_Er': score_0,
    'check_results_DeltaE': score_1,
    'check_results_mag_total': score_2,
    'check_results_mag_Ni': score_3,
    'check_results_ground_state': score_4,
    'check_dos_bulk': score_5,
    'check_dos_surface': score_6,
    'check_dos_mixed': score_7,
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
