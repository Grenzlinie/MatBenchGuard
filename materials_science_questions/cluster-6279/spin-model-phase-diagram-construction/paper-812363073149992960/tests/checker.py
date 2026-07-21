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
    return {}


# === block: score_0 (check id='results_json') ===
def score_0(artifact, step, ctx):
    def compare_value(val, gold, tol_relative):
        if val is None: return 0.0
        if abs(gold) < 1e-12: return 1.0 if abs(val) < 1e-12 else 0.0
        rel_err = abs(val - gold) / abs(gold)
        if rel_err <= tol_relative:
            return 1.0
        elif rel_err <= 3 * tol_relative:
            return max(0.0, 1.0 - (rel_err - tol_relative) / (2 * tol_relative))
        else:
            return 0.0

    def compute_c(L0_N, L0_Np3, N):
        pi = math.pi
        inv = (1.0 / (N + 3) ** 2 - 1.0 / N ** 2)
        if abs(inv) < 1e-14: return None
        factor = math.log(L0_Np3) / (N + 3) - math.log(L0_N) / N
        c_val = (12.0 / (math.sqrt(3.0) * pi)) * factor / inv
        return c_val

    def compute_c_infty(c36, c69):
        f3 = (3 ** -4 + 6 ** -4) / (3 ** -2 + 6 ** -2)
        f6 = (6 ** -4 + 9 ** -4) / (6 ** -2 + 9 ** -2)
        denom = f6 - f3
        if abs(denom) < 1e-14: return None
        a = (c36 - c69) / denom
        c_inf = c36 + a * f3
        return c_inf

    artifact_dict = artifact
    if not isinstance(artifact_dict, dict) or 'critical_line' not in artifact_dict or 'multicritical_point' not in artifact_dict:
        return 0.0

    references_raw = step.get('reference', [])
    multi_gold = step.get('multicritical_gold', {})
    tols = step.get('tolerances', {})
    gold_by_delta = {}
    for r in references_raw:
        gold_by_delta[r['delta']] = r
    required_deltas = set(r['delta'] for r in references_raw)

    cl = artifact_dict['critical_line']
    mp = artifact_dict.get('multicritical_point')

    total_cl = 0.0
    present_deltas = set()
    for entry in cl:
        d = entry.get('delta')
        if d not in gold_by_delta:
            continue
        present_deltas.add(d)
        gold = gold_by_delta[d]
        # gap checking (N6,N9)
        eig6 = entry.get('eigenvalues_N6', {})
        eig9 = entry.get('eigenvalues_N9', {})
        gap_ok = 0.0
        if eig6 and eig9 and 'Lambda0' in eig6 and 'Lambda1' in eig6 and 'Lambda0' in eig9 and 'Lambda1' in eig9:
            try:
                G6 = math.log(eig6['Lambda0'] / eig6['Lambda1'])
                G9 = math.log(eig9['Lambda0'] / eig9['Lambda1'])
                if abs(G6 * 6 - G9 * 9) <= tols.get('gap_tol', 1e-6):
                    gap_ok = 1.0
            except:
                pass
        # t_c
        t_c = entry.get('t_c')
        t_c_score = compare_value(t_c, gold['t_c'], tols.get('t_c_relative', 0.01))
        # c (recompute if N3,N6,N9 available)
        gold_c = gold['c']
        eig3 = entry.get('eigenvalues_N3', {})
        c_score = 0.0
        if eig3 and 'Lambda0' in eig3 and eig6 and 'Lambda0' in eig6 and eig9 and 'Lambda0' in eig9:
            try:
                c36 = compute_c(eig3['Lambda0'], eig6['Lambda0'], 3)
                c69 = compute_c(eig6['Lambda0'], eig9['Lambda0'], 6)
                if c36 is not None and c69 is not None:
                    c_recomp = compute_c_infty(c36, c69)
                    if c_recomp is not None:
                        c_score = compare_value(c_recomp, gold_c, tols.get('c_relative', 0.05))
            except:
                pass
        if c_score == 0.0:
            c_score = compare_value(entry.get('c'), gold_c, tols.get('c_relative', 0.05))
        # x1_0
        x1_gold = gold['x1_0']
        x1_score = 0.0
        if eig9 and 'Lambda0' in eig9 and 'Lambda1' in eig9:
            try:
                G = math.log(eig9['Lambda0'] / eig9['Lambda1'])
                x1_recomp = (9.0 / (math.pi * math.sqrt(3.0))) * G
                x1_score = compare_value(x1_recomp, x1_gold, tols.get('x_relative', 0.05))
            except:
                x1_score = compare_value(entry.get('x1_0'), x1_gold, tols.get('x_relative', 0.05))
        else:
            x1_score = compare_value(entry.get('x1_0'), x1_gold, tols.get('x_relative', 0.05))
        # x2_0 (only self-reported)
        x2_gold = gold['x2_0']
        x2_score = compare_value(entry.get('x2_0'), x2_gold, tols.get('x_relative', 0.05))
        # weighted entry score
        entry_score = 0.2 * gap_ok + 0.25 * t_c_score + 0.2 * c_score + 0.15 * x1_score + 0.15 * x2_score + 0.05
        total_cl += entry_score

    missing = len(required_deltas - present_deltas)
    num_deltas = max(len(required_deltas), 1)
    critical_score = total_cl / num_deltas

    # multicritical point
    multi_score = 0.0
    if mp and isinstance(mp, dict):
        eig3_mp = mp.get('eigenvalues_N3', {})
        eig6_mp = mp.get('eigenvalues_N6', {})
        eig9_mp = mp.get('eigenvalues_N9', {})
        gap_ok_multi = 0.0
        if eig3_mp and eig6_mp and eig9_mp and 'Lambda0' in eig3_mp and 'Lambda1' in eig3_mp and 'Lambda0' in eig6_mp and 'Lambda1' in eig6_mp and 'Lambda0' in eig9_mp and 'Lambda1' in eig9_mp:
            try:
                G3 = math.log(eig3_mp['Lambda0'] / eig3_mp['Lambda1'])
                G6 = math.log(eig6_mp['Lambda0'] / eig6_mp['Lambda1'])
                G9 = math.log(eig9_mp['Lambda0'] / eig9_mp['Lambda1'])
                cond1 = abs(G3 * 3 - G6 * 6) <= tols.get('gap_tol', 1e-6)
                cond2 = abs(G6 * 6 - G9 * 9) <= tols.get('gap_tol', 1e-6)
                if cond1 and cond2:
                    gap_ok_multi = 1.0
            except:
                pass
        delta_t = mp.get('delta_t')
        t_t = mp.get('t_t')
        delta_score = compare_value(delta_t, multi_gold.get('delta_t'), tols.get('delta_t_relative', 0.02))
        t_t_score = compare_value(t_t, multi_gold.get('t_t'), tols.get('t_t_relative', 0.01))
        multi_score = 0.3 * gap_ok_multi + 0.3 * delta_score + 0.4 * t_t_score

    return min(max(0.7 * critical_score + 0.3 * multi_score, 0.0), 1.0)


_SCORERS = {
    'results_json': score_0,
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
