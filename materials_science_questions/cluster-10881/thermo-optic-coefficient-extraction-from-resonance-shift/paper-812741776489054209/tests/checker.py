import os
import json
import csv

# === author imports / helpers ===
try:
    import numpy as np
except ImportError:
    class np:
        @staticmethod
        def array(x):
            return list(x)


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
    spec_steps = spec['steps']
    step1 = spec_steps[0] if spec_steps else {}
    step2 = spec_steps[1] if len(spec_steps) > 1 else {}

    gold_toc = {}
    for mat, pts in step1.get('gold_points', {}).items():
        pts_arr = np.array(pts)  # T, n, k
        dndT_list = []
        dkdT_list = []
        for i in range(len(pts_arr)-1):
            t1, n1, k1 = pts_arr[i]
            t2, n2, k2 = pts_arr[i+1]
            dt = t2 - t1
            dndT_list.append((n2 - n1) / dt)
            dkdT_list.append((k2 - k1) / dt)
        gold_toc[mat] = {
            'dn_dT_min': min(dndT_list),
            'dn_dT_max': max(dndT_list),
            'dk_dT_min': min(dkdT_list),
            'dk_dT_max': max(dkdT_list)
        }

    gold_rows = step2.get('gold_rows', [])
    # precompute gold density and alpha for each row
    gold_density_alpha = []
    for row in gold_rows:
        mat, T, n = row
        r = (n*n - 1.0) / (n*n + 2.0)
        rho = 6.96 * r
        alpha = 5.711e-23 / 6.96
        gold_density_alpha.append((mat, T, rho, alpha))

    ctx = {
        'gold_toc': gold_toc,
        'tol_abs': step1.get('tolerance_abs', 1e-8),
        'tol_rel': step1.get('tolerance_rel', 0.005),
        'gold_density_alpha': gold_density_alpha,
        'tol_rel_row': step2.get('tol_rel', 0.005)
    }
    return ctx


# === block: score_0 (check id='step_01_toc') ===
def score_0(artifact, step, ctx):
    data = artifact  # list of dicts
    if not isinstance(data, list):
        return 0.0
    gold_dict = ctx['gold_toc']
    required_mats = list(gold_dict.keys())
    # map agent data by material
    agent_by_mat = {}
    for entry in data:
        mat = entry.get('material', '').strip()
        if mat:
            agent_by_mat[mat] = entry

    mat_scores = []
    for mat in required_mats:
        if mat not in agent_by_mat:
            mat_scores.append(0.0)
            continue
        agent_entry = agent_by_mat[mat]
        gold = gold_dict[mat]
        fields_ok = 0
        total_fields = 4
        for key in ['dn_dT_min', 'dn_dT_max', 'dk_dT_min', 'dk_dT_max']:
            ag = agent_entry.get(key)
            go = gold[key]
            if ag is None or not isinstance(ag, (int, float)):
                continue
            tol = ctx['tol_abs'] + ctx['tol_rel'] * abs(go)
            if abs(ag - go) <= tol:
                fields_ok += 1
        mat_scores.append(fields_ok / total_fields)

    # also penalize extra materials slightly? ignore.
    score = sum(mat_scores) / len(mat_scores) if mat_scores else 0.0
    return max(0.0, min(1.0, score))


# === block: score_1 (check id='step_02_density_polarizability') ===
def score_1(artifact, step, ctx):
    data = artifact
    if not isinstance(data, list):
        return 0.0
    gold_rows = ctx['gold_density_alpha']
    tol_rel = ctx['tol_rel_row']
    agent_rows = []
    for row in data:
        try:
            mat = str(row['material']).strip()
            T = float(row['temperature_K'])
            dens = float(row['density_g_per_cm3'])
            pol = float(row['polarizability_cm3'])
            agent_rows.append((mat, T, dens, pol))
        except Exception:
            continue

    matched = 0
    for mat, T, gold_rho, gold_alpha in gold_rows:
        found = False
        for amat, aT, adens, apol in agent_rows:
            if amat != mat:
                continue
            if abs(aT - T) > 1e-3:  # allow tiny temperature drift
                continue
            # check density
            if abs(adens - gold_rho) > tol_rel * abs(gold_rho) + 1e-8:
                continue
            # check polarizability
            if abs(apol - gold_alpha) > tol_rel * abs(gold_alpha) + 1e-24:
                continue
            found = True
            break
        if found:
            matched += 1

    score = matched / len(gold_rows) if gold_rows else 1.0
    return max(0.0, min(1.0, score))


_SCORERS = {
    'step_01_toc': score_0,
    'step_02_density_polarizability': score_1,
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
