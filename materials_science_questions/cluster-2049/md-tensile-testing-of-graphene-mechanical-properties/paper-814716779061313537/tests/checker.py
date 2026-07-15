import os
import json
import csv

# === author imports / helpers ===
import sys
import subprocess
import importlib

try:
    import numpy as np
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', 'numpy', '-i', 'https://pypi.tuna.tsinghua.edu.cn/simple'])
    import numpy as np

def bz_expected(f_nN, x_A):
    """Compute expected B_z in Tesla for given force (nN) and x (Angstrom)."""
    hbar = 1.054571817e-34
    e = 1.602176634e-19
    hbar_over_e = hbar / e
    E = 340.0      # N/m
    nu = 0.165
    beta = 3.0
    a = 2.46e-10   # m
    Lz = 3.5e-10    # m
    F0 = f_nN * 1e-9
    x_m = x_A * 1e-10
    x_dim = x_m / Lz
    if abs(x_dim) < 1e-12:
        return 0.0
    abs_x = abs(x_dim)
    term = (2.0 * np.log(1.0 + abs_x) / abs_x
            - (2.0 + 3.0 * abs_x) / (1.0 + abs_x)**2)
    prefactor = -hbar_over_e * (F0 / (E * Lz**2)) * (np.sqrt(3.0) * beta / (2.0 * a)) * ((2.0 + nu) / x_dim)
    return prefactor * term


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


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    if artifact is None:
        return 0.0
    return 1.0 if artifact.strip() == "Σ vanishes: True" else 0.0


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    import numpy as np

    if not artifact:
        return 0.0

    grid = step['grid']
    forces = grid['forces_nN']
    x_start = grid['x_range_A']['start']
    x_end = grid['x_range_A']['end']
    x_step = grid['x_range_A']['step']
    x_vals = list(range(x_start, x_end + 1, x_step))
    expected_combos = set()
    for f in forces:
        for x in x_vals:
            expected_combos.add((round(f, 9), round(x, 9)))

    rows_dict = {}
    for row in artifact:
        try:
            f_val = float(row['F_nN'])
            x_val = float(row['x_A'])
        except (ValueError, KeyError):
            continue
        key = (round(f_val, 9), round(x_val, 9))
        if key in rows_dict:
            return 0.0
        rows_dict[key] = float(row['B_z_T'])

    if set(rows_dict.keys()) != expected_combos:
        return 0.0

    tol_rel = step.get('tolerance_rel', 0.05)
    tol_abs = step.get('tolerance_abs_small', 1e-6)

    scores = []
    for (f, x), bz_agent in rows_dict.items():
        bz_exp = bz_expected(f, x)
        err = abs(bz_agent - bz_exp)
        max_allowed = max(tol_rel * max(abs(bz_exp), tol_abs), 1e-10)
        scores.append(1.0 if err <= max_allowed else 0.0)

    return float(np.mean(scores))


_SCORERS = {
    'step_01': score_0,
    'step_02': score_1,
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
