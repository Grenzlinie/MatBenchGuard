import os
import json
import csv

# === author imports / helpers ===
import subprocess
import sys
try:
    import numpy as np
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "--no-cache-dir", "-i", "https://pypi.tuna.tsinghua.edu.cn/simple", "numpy"])
    import numpy as np
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
    ctx = {}
    ctx['steps'] = spec.get('steps', [])
    ctx['output_contract'] = spec.get('output_contract', {})
    return ctx


# === block: score_0 (check id='step_04_buckling') ===
def score_0(artifact, step, ctx):
    if artifact is None: return 0.0
    expected_rows = step.get('expected_rows', [])
    if not expected_rows: return 1.0
    agent_rows = {}
    for row in artifact:
        key = (row.get('system','').strip(), row.get('boundary_condition','').strip(), row.get('compression_direction','').strip())
        try:
            val = float(row.get('buckling_strain_percent', ''))
        except:
            val = None
        agent_rows[key] = val
    correct = 0
    total = len(expected_rows)
    for exp in expected_rows:
        key = (exp['system'], exp['boundary_condition'], exp['compression_direction'])
        agent_val = agent_rows.get(key)
        if agent_val is None:
            continue
        tol = exp.get('tolerance', 0.1)
        expected_val = exp['buckling_strain_percent']
        if abs(agent_val - expected_val) <= tol:
            correct += 1
        else:
            # partial credit: linear decay beyond tolerance up to 2*tolerance
            rel_err = abs(agent_val - expected_val) / max(0.001, abs(expected_val))
            if rel_err <= 0.5:  # allow up to 50% relative error for partial
                correct += max(0.0, 1.0 - rel_err)
    return correct / total if total > 0 else 0.0


# === block: score_1 (check id='step_05_free_energy') ===
def score_1(artifact, step, ctx):
    if artifact is None: return 0.0
    expected_rows = step.get('expected_rows', [])
    if not expected_rows: return 1.0
    agent_rows = {}
    for row in artifact:
        key = (row.get('system','').strip(), row.get('boundary_condition','').strip(), row.get('compression_direction','').strip())
        try:
            fe = float(row.get('free_energy_min_eV', ''))
        except:
            fe = None
        try:
            eps = float(row.get('equilibrium_strain_percent', ''))
        except:
            eps = None
        agent_rows[key] = (fe, eps)
    correct = 0
    total = len(expected_rows)
    for exp in expected_rows:
        key = (exp['system'], exp['boundary_condition'], exp['compression_direction'])
        agent = agent_rows.get(key)
        if agent is None:
            continue
        fe_agent, eps_agent = agent
        if fe_agent is None or eps_agent is None:
            continue
        tol_fe = exp.get('tolerance', 0.5)
        tol_eps = exp.get('strain_tolerance', 0.1)
        fe_ok = abs(fe_agent - exp['free_energy_min_eV']) <= tol_fe
        eps_ok = abs(eps_agent - exp['equilibrium_strain_percent']) <= tol_eps
        if fe_ok and eps_ok:
            correct += 1
        else:
            # partial: average of fe and eps scores
            fe_score = max(0.0, 1.0 - abs(fe_agent - exp['free_energy_min_eV']) / max(0.001, abs(exp['free_energy_min_eV'])))
            eps_score = max(0.0, 1.0 - abs(eps_agent - exp['equilibrium_strain_percent']) / max(0.001, abs(exp['equilibrium_strain_percent'])))
            correct += 0.5 * (fe_score + eps_score)
    return correct / total if total > 0 else 0.0


# === block: score_2 (check id='step_06_shape') ===
def score_2(artifact, step, ctx):
    if artifact is None: return 0.0
    ribbon_length = step.get('ribbon_length_nm', 20.0)
    threshold_r2_pg = step.get('pg_r2_threshold', 0.9)
    gb_r2_max = step.get('gb_r2_max', 0.7)
    residual_threshold = step.get('residual_threshold_nm', 0.05)
    center_x = step.get('center_x_nm', 10.0)
    systems = {}
    for row in artifact:
        sys = row.get('system','').strip()
        if sys not in systems:
            systems[sys] = {'x': [], 'z': []}
        try:
            x = float(row['x_position_nm'])
            z = float(row['average_z_deviation_nm'])
        except:
            continue
        systems[sys]['x'].append(x)
        systems[sys]['z'].append(z)
    def sine_model(x, A):
        return A * np.sin(np.pi * x / ribbon_length)
    results = {}
    for sys, data in systems.items():
        x = np.array(data['x'])
        z = np.array(data['z'])
        if len(x) < 2:
            results[sys] = {'r2': None, 'residual_center': None}
            continue
        sin_vals = np.sin(np.pi * x / ribbon_length)
        A, _, _, _ = np.linalg.lstsq(sin_vals[:, None], z, rcond=None)
        pred = A * sin_vals
        ss_res = np.sum((z - pred)**2)
        ss_tot = np.sum((z - np.mean(z))**2)
        r2 = 1 - ss_res / ss_tot if ss_tot > 0 else 0.0
        idx = np.argmin(np.abs(x - center_x))
        residual_center = abs(z[idx] - pred[idx])
        results[sys] = {'r2': r2, 'residual_center': residual_center}
    pg_score = 0.0
    gb_scores = []
    for sys, r in results.items():
        if sys == 'PG':
            if r['r2'] is not None and r['r2'] > threshold_r2_pg:
                pg_score = 1.0
            else:
                pg_score = max(0.0, r['r2'] if r['r2'] is not None else 0.0)  # partial based on r2
        else:
            if r['r2'] is not None:
                cond_r2 = r['r2'] < gb_r2_max
                cond_res = r['residual_center'] is not None and r['residual_center'] > residual_threshold
                if cond_r2 and cond_res:
                    gb_scores.append(1.0)
                else:
                    # partial: average of r2 complement and residual ratio
                    r2_score = max(0.0, 1.0 - r['r2']/gb_r2_max) if gb_r2_max > 0 else 1.0
                    res_score = min(1.0, r['residual_center']/residual_threshold) if residual_threshold > 0 else 1.0
                    gb_scores.append(0.5*(r2_score + res_score))
    if 'PG' not in results:
        pg_score = 0.0
    # weights: PG 0.4, each grain boundary 0.3; handle missing systems
    if len(gb_scores) >= 2:
        total = pg_score * 0.4 + (gb_scores[0] + gb_scores[1]) * 0.3
    elif len(gb_scores) == 1:
        total = pg_score * 0.4 + gb_scores[0] * 0.6
    else:
        total = pg_score * 1.0
    return min(1.0, total)


_SCORERS = {
    'step_04_buckling': score_0,
    'step_05_free_energy': score_1,
    'step_06_shape': score_2,
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
