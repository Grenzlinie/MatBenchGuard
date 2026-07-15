import os
import json
import csv

# === author imports / helpers ===
import os, csv, statistics, math


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
    step = spec['steps'][0]
    gold_medians = step['gold_medians']
    disp_pairs = step.get('dispersion_pairs', [])
    batty_pair = step.get('batty_pair', [])
    median_weight = step.get('median_metric_weight', 0.85)
    disp_weight = step.get('dispersion_weight', 0.10)
    batty_weight = step.get('batty_weight', 0.05)
    return {
        'gold_medians': gold_medians,
        'disp_pairs': disp_pairs,
        'batty_pair': batty_pair,
        'median_weight': median_weight,
        'disp_weight': disp_weight,
        'batty_weight': batty_weight
    }


# === block: score_0 (check id='step_7_per_molecule_metrics') ===
def score_0(artifact, step, ctx):
    artifact_path = '/app/outputs/per_molecule_metrics.csv'
    if not os.path.exists(artifact_path):
        return 0.0
    try:
        with open(artifact_path, newline='') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
    except Exception:
        return 0.0
    if not rows:
        return 0.0
    method_values = {}
    for row in rows:
        method = row.get('method', '').strip()
        try:
            mare = float(row.get('MARE', 0))
            r2 = float(row.get('R2', 0))
            sp = float(row.get('Spearman_rho', 0))
        except (ValueError, TypeError):
            continue
        method_values.setdefault(method, {'MARE': [], 'R2': [], 'Spearman_rho': []})
        method_values[method]['MARE'].append(mare)
        method_values[method]['R2'].append(r2)
        method_values[method]['Spearman_rho'].append(sp)
    medians = {}
    for method, vals in method_values.items():
        medians[method] = {
            'MARE': statistics.median(vals['MARE']) if vals['MARE'] else None,
            'R2': statistics.median(vals['R2']) if vals['R2'] else None,
            'Spearman_rho': statistics.median(vals['Spearman_rho']) if vals['Spearman_rho'] else None
        }
    gold = ctx['gold_medians']
    # --- metric scoring ---
    mare_factor = 1.0   # zero at gold * (1 + mare_factor)
    r2_tol = 0.2        # absolute drop tolerance for R2
    spearman_tol = 0.2   # absolute drop tolerance for Spearman
    method_scores = []
    for method, gold_vals in gold.items():
        agent_vals = medians.get(method, {})
        if agent_vals is None:
            continue
        scores = []
        for metric, ref in [('MARE', gold_vals.get('MARE')), ('R2', gold_vals.get('R2')), ('Spearman_rho', gold_vals.get('Spearman_rho'))]:
            if ref is None or agent_vals.get(metric) is None:
                scores.append(1.0)  # no check if missing
                continue
            agent_val = agent_vals[metric]
            if metric == 'MARE':
                if agent_val <= ref:
                    scores.append(1.0)
                else:
                    excess = agent_val - ref
                    max_excess = ref * mare_factor
                    score = max(0.0, 1.0 - excess / max_excess) if max_excess > 0 else 0.0
                    scores.append(score)
            elif metric == 'R2':
                if agent_val >= ref:
                    scores.append(1.0)
                else:
                    deficit = ref - agent_val
                    score = max(0.0, 1.0 - deficit / r2_tol) if r2_tol > 0 else 0.0
                    scores.append(score)
            else:  # Spearman_rho
                if agent_val >= ref:
                    scores.append(1.0)
                else:
                    deficit = ref - agent_val
                    score = max(0.0, 1.0 - deficit / spearman_tol) if spearman_tol > 0 else 0.0
                    scores.append(score)
        method_scores.append(sum(scores)/len(scores) if scores else 1.0)
    if method_scores:
        main_score = sum(method_scores)/len(method_scores)
    else:
        main_score = 0.0
    # --- dispersion check ---
    disp_score = 1.0
    disp_pairs = ctx.get('disp_pairs', [])
    for pair in disp_pairs:
        r2_disp = medians.get(pair[0], {}).get('R2')
        r2_nodisp = medians.get(pair[1], {}).get('R2')
        if r2_disp is None or r2_nodisp is None:
            disp_score *= 0.0
            break
        if r2_disp > r2_nodisp:
            continue
        else:
            disp_score *= 0.0
            break
    # --- BATTY/n check ---
    batty_pair = ctx.get('batty_pair', [])
    batty_score = 1.0
    if len(batty_pair) == 2:
        r2_battyn = medians.get(batty_pair[0], {}).get('R2')
        r2_batty = medians.get(batty_pair[1], {}).get('R2')
        if r2_battyn is not None and r2_batty is not None:
            if r2_battyn > r2_batty:
                batty_score = 1.0
            else:
                batty_score = 0.0
        else:
            batty_score = 0.0
    w_median = ctx['median_weight']
    w_disp = ctx['disp_weight']
    w_batty = ctx['batty_weight']
    total = w_median * main_score + w_disp * disp_score + w_batty * batty_score
    return float(total)


_SCORERS = {
    'step_7_per_molecule_metrics': score_0,
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
