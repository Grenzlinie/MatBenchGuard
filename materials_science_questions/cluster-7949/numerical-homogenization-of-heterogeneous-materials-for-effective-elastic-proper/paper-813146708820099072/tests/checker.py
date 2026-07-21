import os
import json
import csv

# === author imports / helpers ===
import csv
import math
import numpy as np


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


# === block: score_0 (check id='compute_energies') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0

    params = step.get('params', {})
    coherent_dirs = params.get('coherent_directions', [])
    eps_close = params.get('epsilon_close', 1e-6)
    ord_eps = params.get('ordering_epsilon', 1e-9)
    var_std_min = params.get('variation_std_min', 1e-9)
    w = params.get('sub_weights', {'ordering': 0.3, 'constancy': 0.3, 'partial_rank_one_variation_minima': 0.4})
    # Use a realistic constancy tolerance (1e-4) to not penalize correct numerical minimisation.
    const_std_tol = 1e-4

    # parse values
    thetas = []
    phis = []
    e_vt = []
    e_rs = []
    e_pr = []
    for r in rows:
        try:
            th = float(r['theta'])
            ph = float(r['phi'])
            vt = float(r['energy_VoigtTaylor'])
            rs = float(r['energy_ReussSachs'])
            pr = float(r['energy_PartialRankOne'])
            thetas.append(th)
            phis.append(ph)
            e_vt.append(vt)
            e_rs.append(rs)
            e_pr.append(pr)
        except:
            return 0.0

    n = len(e_vt)
    if n < 2:
        return 0.0

    # 1. ordering
    ord_ok = True
    for vt, rs, pr in zip(e_vt, e_rs, e_pr):
        if vt + ord_eps < pr or pr + ord_eps < rs:
            ord_ok = False
            break
    score_ord = 1.0 if ord_ok else 0.0

    # 2. constancy (relaxed tolerance)
    arr_vt = np.array(e_vt)
    arr_rs = np.array(e_rs)
    std_vt = np.std(arr_vt)
    std_rs = np.std(arr_rs)
    const_ok = (std_vt <= const_std_tol) and (std_rs <= const_std_tol)
    score_const = 1.0 if const_ok else 0.0

    # 3. partial rank-one variation + minima at coherent orientations
    arr_pr = np.array(e_pr)
    std_pr = np.std(arr_pr)
    if std_pr <= var_std_min:
        score_pr = 0.0
    else:
        # find rows whose N is near a coherent direction
        coherent_idxs = []
        for i in range(n):
            th = thetas[i]
            ph = phis[i]
            N = [math.sin(th)*math.cos(ph), math.sin(th)*math.sin(ph), math.cos(th)]
            for cd in coherent_dirs:
                if all(abs(a-b) < eps_close for a,b in zip(N, cd)):
                    coherent_idxs.append(i)
                    break
        if not coherent_idxs:
            score_pr = 0.0
        else:
            min_coherent = min(arr_pr[j] for j in coherent_idxs)
            non_coherent_mask = np.ones(n, dtype=bool)
            non_coherent_mask[coherent_idxs] = False
            if np.any(arr_pr[non_coherent_mask] < min_coherent - 1e-9):
                score_pr = 0.0
            else:
                score_pr = 1.0

    total = w['ordering']*score_ord + w['constancy']*score_const + w['partial_rank_one_variation_minima']*score_pr
    return min(1.0, max(0.0, total))


_SCORERS = {
    'compute_energies': score_0,
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
