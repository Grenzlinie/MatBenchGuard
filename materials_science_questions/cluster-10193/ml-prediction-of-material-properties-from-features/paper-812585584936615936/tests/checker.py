import os
import json
import csv

# === author imports / helpers ===
import sys
import subprocess

def _ensure_deps():
    try:
        import numpy as np  # noqa: F811
        import scipy        # noqa: F401
    except ImportError:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "-q", "--no-cache-dir",
             "-i", "https://pypi.tuna.tsinghua.edu.cn/simple",
             "numpy", "scipy"]
        )
        import numpy as np  # noqa: F811
        import scipy        # noqa: F401

_ensure_deps()

import numpy as np
from scipy.stats import spearmanr


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
    step = None
    for s in spec['steps']:
        if s['id'] == 'step06':
            step = s
            break
    gold_table = {row['prototype']: row for row in step['gold_table']}
    gold_protos = list(gold_table.keys())
    ctx = {
        'gold_table': gold_table,
        'gold_protos': gold_protos,
        'abs_tol': step['abs_tol'],
        'rel_tol': step['rel_tol'],
        'total_stability_target': step['total_stability_target'],
        'total_stability_rel_tol': step['total_stability_rel_tol'],
        'zero_stability_prototypes': set(step['zero_stability_prototypes']),
        'spearman_threshold': step['spearman_threshold']
    }
    return ctx


# === block: score_0 (check id='step06') ===
def score_0(artifact, step, ctx):
    gold = ctx['gold_table']
    gold_protos = ctx['gold_protos']
    abs_tol = ctx['abs_tol']
    rel_tol = ctx['rel_tol']
    total_stab_target = ctx['total_stability_target']
    total_stab_rel = ctx['total_stability_rel_tol']
    zero_set = ctx['zero_stability_prototypes']
    spear_thr = ctx['spearman_threshold']

    agent_dict = {r['prototype']: r for r in artifact}

    # define columns to check
    count_cols = ['total_generated','after_symmetry','after_neutrality','after_stability']

    # Helper for tolerance
    def within_tol(agent_val, gold_val):
        if gold_val < 100:
            return abs(agent_val - gold_val) <= abs_tol
        else:
            return abs(agent_val - gold_val) <= rel_tol * gold_val

    total_cells = 0
    correct_cells = 0
    agent_stab_list = []
    gold_stab_list = []
    for proto in gold_protos:
        if proto not in agent_dict:
            # treat missing prototype as all zeros, which will likely be far off
            row_agent = {c:0 for c in count_cols}
        else:
            row_agent = agent_dict[proto]
        gold_row = gold[proto]
        for col in count_cols:
            a = int(row_agent.get(col,0))
            g = int(gold_row[col])
            if within_tol(a, g):
                correct_cells += 1
            total_cells += 1
        agent_stab_list.append(int(row_agent.get('after_stability',0)))
        gold_stab_list.append(int(gold_row['after_stability']))

    cell_acc = correct_cells / total_cells if total_cells > 0 else 0.0

    # total after_stability check
    agent_total_stab = sum(agent_stab_list)
    if agent_total_stab == 0:
        total_stab_score = 0.0
    else:
        rel_err = abs(agent_total_stab - total_stab_target) / total_stab_target
        total_stab_score = 1.0 if rel_err <= total_stab_rel else 0.0

    # zero prototypes check
    all_zero_ok = all(int(agent_dict.get(p,{}).get('after_stability',-1)) == 0 for p in zero_set)
    zero_score = 1.0 if all_zero_ok else 0.0

    # Spearman correlation
    if len(gold_stab_list) < 2:
        corr = 1.0
    else:
        corr, _ = spearmanr(agent_stab_list, gold_stab_list)
        if np.isnan(corr):
            corr = 0.0
    if corr >= spear_thr:
        spear_score = 1.0
    elif corr >= 0.5:
        spear_score = (corr - 0.5) / (spear_thr - 0.5) * 0.8 + 0.2  # partial credit
    else:
        spear_score = 0.0

    final = 0.5*cell_acc + 0.2*total_stab_score + 0.1*zero_score + 0.2*spear_score
    return min(1.0, max(0.0, final))


_SCORERS = {
    'step06': score_0,
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
