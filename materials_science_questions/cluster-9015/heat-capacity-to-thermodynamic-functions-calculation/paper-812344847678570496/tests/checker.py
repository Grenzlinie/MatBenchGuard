import os
import json
import csv

# === author imports / helpers ===
import csv, os, math
from typing import Dict, Any, List


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
    def prepare(outputs_dir, spec):
        step = spec['steps'][0]
        gold_table = step['gold_table']
        return {'gold': gold_table}


# === block: score_0 (check id='thermo_functions') ===
def score_0(artifact, step, ctx):
    if not ctx or not isinstance(ctx, dict) or 'gold' not in ctx:
        return 0.0
    gold = ctx['gold']
    if not isinstance(gold, dict):
        return 0.0
    if not artifact or not isinstance(artifact, list):
        return 0.0

    def _safe_float(val, default=0.0):
        try:
            return float(val)
        except (TypeError, ValueError):
            return default

    rows_by_t = {}
    for row in artifact:
        t_str = row.get('T', '').strip()
        if not t_str:
            continue
        try:
            t = float(t_str)
        except (ValueError, TypeError):
            continue
        rows_by_t[t] = row

    def cp_tol(T):
        if T <= 50.0:
            return 0.02
        elif T >= 200.0:
            return 0.005
        else:
            return 0.02 + (T - 50.0) / 150.0 * (0.005 - 0.02)

    TOL_S = 0.01
    TOL_G = 0.01
    TOL_H = 0.01
    special_T = {298.15: 3.0}
    total_weight = 0.0
    weighted_score_sum = 0.0

    for t_str, gold_vals in gold.items():
        t = float(t_str)
        w = special_T.get(t, 1.0)
        if t not in rows_by_t:
            total_weight += w
            weighted_score_sum += 0.0 * w
            continue
        row = rows_by_t[t]
        cell_scores = []

        # Cp
        cp_agent = _safe_float(row.get('Cp'))
        cp_gold = gold_vals['Cp']
        if cp_gold == 0:
            cp_rel_err = abs(cp_agent)
            cp_tol_val = 0.02
        else:
            cp_rel_err = abs(cp_agent - cp_gold) / abs(cp_gold)
            cp_tol_val = cp_tol(t)
        cp_score = 1.0 if cp_rel_err <= cp_tol_val else max(0.0, 1.0 - (cp_rel_err - cp_tol_val) / 0.5)
        cell_scores.append(cp_score)

        # S
        s_agent = _safe_float(row.get('S'))
        s_gold = gold_vals['S']
        if s_gold == 0:
            s_rel_err = abs(s_agent)
        else:
            s_rel_err = abs(s_agent - s_gold) / abs(s_gold)
        s_score = 1.0 if s_rel_err <= TOL_S else max(0.0, 1.0 - (s_rel_err - TOL_S) / 0.5)
        cell_scores.append(s_score)

        # neg_G_over_T
        g_agent = _safe_float(row.get('neg_G_over_T'))
        g_gold = gold_vals['neg_G_over_T']
        if g_gold == 0:
            g_rel_err = abs(g_agent)
        else:
            g_rel_err = abs(g_agent - g_gold) / abs(g_gold)
        g_score = 1.0 if g_rel_err <= TOL_G else max(0.0, 1.0 - (g_rel_err - TOL_G) / 0.5)
        cell_scores.append(g_score)

        # H
        h_agent = _safe_float(row.get('H'))
        h_gold = gold_vals['H']
        if h_gold == 0:
            h_rel_err = abs(h_agent)
        else:
            h_rel_err = abs(h_agent - h_gold) / abs(h_gold)
        h_score = 1.0 if h_rel_err <= TOL_H else max(0.0, 1.0 - (h_rel_err - TOL_H) / 0.5)
        cell_scores.append(h_score)

        row_score = sum(cell_scores) / len(cell_scores)
        total_weight += w
        weighted_score_sum += row_score * w

    if total_weight > 0:
        final_score = weighted_score_sum / total_weight
    else:
        final_score = 0.0
    return final_score


_SCORERS = {
    'thermo_functions': score_0,
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
