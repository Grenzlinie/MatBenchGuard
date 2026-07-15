import os
import json
import csv

# === author imports / helpers ===
import sys
import subprocess

def _try_install_numpy():
    try:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "-q", "--no-cache-dir",
             "-i", "https://pypi.tuna.tsinghua.edu.cn/simple", "numpy"]
        )
    except Exception:
        pass

try:
    import numpy as np
except ImportError:
    _try_install_numpy()
    try:
        import numpy as np
    except ImportError:
        np = None

if np is None:
    class _NPFallback:
        def __getattr__(self, name):
            raise RuntimeError("numpy not available")
    np = _NPFallback()


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


# === block: score_0 (check id='tension_X_csv') ===
def score_0(artifact, step, ctx):
    strain = []
    stress = []
    for row in artifact:
        try:
            strain.append(float(row["strain"]))
            stress.append(float(row["stress"]))
        except:
            continue
    if len(strain) < 2:
        return 0.0
    strain = np.array(strain)
    stress = np.array(stress)
    cfg = step.get("config", {})
    mod_min = cfg.get("modulus_strain_min", 0.0)
    mod_max = cfg.get("modulus_strain_max", 0.005)
    mask = (strain >= mod_min) & (strain <= mod_max)
    if np.sum(mask) < 2:
        mod_score = 0.0
    else:
        coeffs = np.polyfit(strain[mask], stress[mask], 1)
        computed_mod = coeffs[0]
        gold_mod = cfg["gold_modulus_GPa"]
        tol = cfg["modulus_tolerance_fraction"]
        if abs(computed_mod - gold_mod) <= tol * gold_mod:
            mod_score = 1.0
        else:
            mod_score = 0.0

    ftype = cfg["failure_strain_type"]
    if ftype == "tension":
        idx_peak = np.argmax(stress)
        peak_stress = stress[idx_peak]
        fail_strain = None
        for i in range(idx_peak, len(stress)):
            if stress[i] <= 0.8 * peak_stress:
                fail_strain = strain[i]
                break
        if fail_strain is None:
            fail_score = 0.0
        else:
            gold_strain = cfg["gold_failure_strain"]
            tol_strain = cfg["strain_tolerance_abs"]
            if abs(fail_strain - gold_strain) <= tol_strain:
                fail_score = 1.0
            else:
                fail_score = 0.0
    else:
        idx_peak = np.argmax(stress)
        fail_strain = strain[idx_peak]
        gold_strain = cfg["gold_failure_strain_abs"]
        tol_strain = cfg["strain_tolerance_abs"]
        if abs(fail_strain - gold_strain) <= tol_strain:
            fail_score = 1.0
        else:
            fail_score = 0.0

    return 0.5 * mod_score + 0.5 * fail_score


# === block: score_1 (check id='tension_Y_csv') ===
def score_1(artifact, step, ctx):
    strain = []
    stress = []
    for row in artifact:
        try:
            strain.append(float(row["strain"]))
            stress.append(float(row["stress"]))
        except:
            continue
    if len(strain) < 2:
        return 0.0
    strain = np.array(strain)
    stress = np.array(stress)
    cfg = step.get("config", {})
    mod_min = cfg.get("modulus_strain_min", 0.0)
    mod_max = cfg.get("modulus_strain_max", 0.005)
    mask = (strain >= mod_min) & (strain <= mod_max)
    if np.sum(mask) < 2:
        mod_score = 0.0
    else:
        coeffs = np.polyfit(strain[mask], stress[mask], 1)
        computed_mod = coeffs[0]
        gold_mod = cfg["gold_modulus_GPa"]
        tol = cfg["modulus_tolerance_fraction"]
        if abs(computed_mod - gold_mod) <= tol * gold_mod:
            mod_score = 1.0
        else:
            mod_score = 0.0

    ftype = cfg["failure_strain_type"]
    if ftype == "tension":
        idx_peak = np.argmax(stress)
        peak_stress = stress[idx_peak]
        fail_strain = None
        for i in range(idx_peak, len(stress)):
            if stress[i] <= 0.8 * peak_stress:
                fail_strain = strain[i]
                break
        if fail_strain is None:
            fail_score = 0.0
        else:
            gold_strain = cfg["gold_failure_strain"]
            tol_strain = cfg["strain_tolerance_abs"]
            if abs(fail_strain - gold_strain) <= tol_strain:
                fail_score = 1.0
            else:
                fail_score = 0.0
    else:
        idx_peak = np.argmax(stress)
        fail_strain = strain[idx_peak]
        gold_strain = cfg["gold_failure_strain_abs"]
        tol_strain = cfg["strain_tolerance_abs"]
        if abs(fail_strain - gold_strain) <= tol_strain:
            fail_score = 1.0
        else:
            fail_score = 0.0

    return 0.5 * mod_score + 0.5 * fail_score


# === block: score_2 (check id='tension_Z_csv') ===
def score_2(artifact, step, ctx):
    strain = []
    stress = []
    for row in artifact:
        try:
            strain.append(float(row["strain"]))
            stress.append(float(row["stress"]))
        except:
            continue
    if len(strain) < 2:
        return 0.0
    strain = np.array(strain)
    stress = np.array(stress)
    cfg = step.get("config", {})
    mod_min = cfg.get("modulus_strain_min", 0.0)
    mod_max = cfg.get("modulus_strain_max", 0.005)
    mask = (strain >= mod_min) & (strain <= mod_max)
    if np.sum(mask) < 2:
        mod_score = 0.0
    else:
        coeffs = np.polyfit(strain[mask], stress[mask], 1)
        computed_mod = coeffs[0]
        gold_mod = cfg["gold_modulus_GPa"]
        tol = cfg["modulus_tolerance_fraction"]
        if abs(computed_mod - gold_mod) <= tol * gold_mod:
            mod_score = 1.0
        else:
            mod_score = 0.0

    ftype = cfg["failure_strain_type"]
    if ftype == "tension":
        idx_peak = np.argmax(stress)
        peak_stress = stress[idx_peak]
        fail_strain = None
        for i in range(idx_peak, len(stress)):
            if stress[i] <= 0.8 * peak_stress:
                fail_strain = strain[i]
                break
        if fail_strain is None:
            fail_score = 0.0
        else:
            gold_strain = cfg["gold_failure_strain"]
            tol_strain = cfg["strain_tolerance_abs"]
            if abs(fail_strain - gold_strain) <= tol_strain:
                fail_score = 1.0
            else:
                fail_score = 0.0
    else:
        idx_peak = np.argmax(stress)
        fail_strain = strain[idx_peak]
        gold_strain = cfg["gold_failure_strain_abs"]
        tol_strain = cfg["strain_tolerance_abs"]
        if abs(fail_strain - gold_strain) <= tol_strain:
            fail_score = 1.0
        else:
            fail_score = 0.0

    return 0.5 * mod_score + 0.5 * fail_score


# === block: score_3 (check id='compression_X_csv') ===
def score_3(artifact, step, ctx):
    strain = []
    stress = []
    for row in artifact:
        try:
            strain.append(float(row["strain"]))
            stress.append(float(row["stress"]))
        except:
            continue
    if len(strain) < 2:
        return 0.0
    strain = np.array(strain)
    stress = np.array(stress)
    cfg = step.get("config", {})
    mod_min = cfg.get("modulus_strain_min", 0.0)
    mod_max = cfg.get("modulus_strain_max", 0.005)
    mask = (strain >= mod_min) & (strain <= mod_max)
    if np.sum(mask) < 2:
        mod_score = 0.0
    else:
        coeffs = np.polyfit(strain[mask], stress[mask], 1)
        computed_mod = coeffs[0]
        gold_mod = cfg["gold_modulus_GPa"]
        tol = cfg["modulus_tolerance_fraction"]
        if abs(computed_mod - gold_mod) <= tol * gold_mod:
            mod_score = 1.0
        else:
            mod_score = 0.0

    ftype = cfg["failure_strain_type"]
    if ftype == "compression":
        idx_peak = np.argmax(stress)
        fail_strain = strain[idx_peak]
        gold_strain = cfg["gold_failure_strain_abs"]
        tol_strain = cfg["strain_tolerance_abs"]
        if abs(fail_strain - gold_strain) <= tol_strain:
            fail_score = 1.0
        else:
            fail_score = 0.0
    else:
        fail_score = 0.0

    return 0.5 * mod_score + 0.5 * fail_score


# === block: score_4 (check id='compression_Y_csv') ===
def score_4(artifact, step, ctx):
    strain = []
    stress = []
    for row in artifact:
        try:
            strain.append(float(row["strain"]))
            stress.append(float(row["stress"]))
        except:
            continue
    if len(strain) < 2:
        return 0.0
    strain = np.array(strain)
    stress = np.array(stress)
    cfg = step.get("config", {})
    mod_min = cfg.get("modulus_strain_min", 0.0)
    mod_max = cfg.get("modulus_strain_max", 0.005)
    mask = (strain >= mod_min) & (strain <= mod_max)
    if np.sum(mask) < 2:
        mod_score = 0.0
    else:
        coeffs = np.polyfit(strain[mask], stress[mask], 1)
        computed_mod = coeffs[0]
        gold_mod = cfg["gold_modulus_GPa"]
        tol = cfg["modulus_tolerance_fraction"]
        if abs(computed_mod - gold_mod) <= tol * gold_mod:
            mod_score = 1.0
        else:
            mod_score = 0.0

    ftype = cfg["failure_strain_type"]
    if ftype == "compression":
        idx_peak = np.argmax(stress)
        fail_strain = strain[idx_peak]
        gold_strain = cfg["gold_failure_strain_abs"]
        tol_strain = cfg["strain_tolerance_abs"]
        if abs(fail_strain - gold_strain) <= tol_strain:
            fail_score = 1.0
        else:
            fail_score = 0.0
    else:
        fail_score = 0.0

    return 0.5 * mod_score + 0.5 * fail_score


# === block: score_5 (check id='compression_Z_csv') ===
def score_5(artifact, step, ctx):
    strain = []
    stress = []
    for row in artifact:
        try:
            strain.append(float(row["strain"]))
            stress.append(float(row["stress"]))
        except:
            continue
    if len(strain) < 2:
        return 0.0
    strain = np.array(strain)
    stress = np.array(stress)
    cfg = step.get("config", {})
    mod_min = cfg.get("modulus_strain_min", 0.0)
    mod_max = cfg.get("modulus_strain_max", 0.005)
    mask = (strain >= mod_min) & (strain <= mod_max)
    if np.sum(mask) < 2:
        mod_score = 0.0
    else:
        coeffs = np.polyfit(strain[mask], stress[mask], 1)
        computed_mod = coeffs[0]
        gold_mod = cfg["gold_modulus_GPa"]
        tol = cfg["modulus_tolerance_fraction"]
        if abs(computed_mod - gold_mod) <= tol * gold_mod:
            mod_score = 1.0
        else:
            mod_score = 0.0

    ftype = cfg["failure_strain_type"]
    if ftype == "compression":
        idx_peak = np.argmax(stress)
        fail_strain = strain[idx_peak]
        gold_strain = cfg["gold_failure_strain_abs"]
        tol_strain = cfg["strain_tolerance_abs"]
        if abs(fail_strain - gold_strain) <= tol_strain:
            fail_score = 1.0
        else:
            fail_score = 0.0
    else:
        fail_score = 0.0

    return 0.5 * mod_score + 0.5 * fail_score


# === block: score_6 (check id='summary_ordering') ===
def score_6(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0

    offenses = 0
    total = 8

    try:
        tX = artifact["tension"]["X"]["E_modulus_GPa"]
        tY = artifact["tension"]["Y"]["E_modulus_GPa"]
        tZ = artifact["tension"]["Z"]["E_modulus_GPa"]
        if tZ > tX: offenses += 1
        if tZ > tY: offenses += 1

        tfX = artifact["tension"]["X"]["failure_strain"]
        tfY = artifact["tension"]["Y"]["failure_strain"]
        tfZ = artifact["tension"]["Z"]["failure_strain"]
        if tfZ < tfX: offenses += 1
        if tfZ < tfY: offenses += 1

        cX = artifact["compression"]["X"]["E_modulus_GPa"]
        cY = artifact["compression"]["Y"]["E_modulus_GPa"]
        cZ = artifact["compression"]["Z"]["E_modulus_GPa"]
        if cZ > cX: offenses += 1
        if cZ > cY: offenses += 1

        cfX = artifact["compression"]["X"]["failure_strain_abs"]
        cfY = artifact["compression"]["Y"]["failure_strain_abs"]
        cfZ = artifact["compression"]["Z"]["failure_strain_abs"]
        if cfZ > cfX: offenses += 1
        if cfZ > cfY: offenses += 1

    except:
        return 0.0

    return offenses / total


_SCORERS = {
    'tension_X_csv': score_0,
    'tension_Y_csv': score_1,
    'tension_Z_csv': score_2,
    'compression_X_csv': score_3,
    'compression_Y_csv': score_4,
    'compression_Z_csv': score_5,
    'summary_ordering': score_6,
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
