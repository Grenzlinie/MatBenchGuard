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
    steps = spec['steps']
    step = None
    for s in steps:
        if s['id'] == 'band_gaps_scorer':
            step = s
            break
    if step is None:
        raise ValueError('Missing band_gaps_scorer step')
    ref = step['reference_values']
    tol = step['tolerance_abs']
    return {'ref': ref, 'tol': tol}


# === block: score_0 (check id='band_gaps_scorer') ===
def score_0(artifact, step, ctx):
    artifact = artifact
    ref = ctx['ref']
    tol = ctx['tol']
    order = ['5a','5b','5c','5f','5h','5j','5k','5l']
    agent_map = {}
    for row in artifact:
        comp = row.get('compound','').strip()
        try:
            val = float(row.get('band_gap_eV'))
            agent_map[comp] = val
        except:
            pass

    hits = 0
    agent_vals = []
    ref_vals = []
    for comp in order:
        gold_val = ref.get(comp)
        if gold_val is None:
            continue
        if comp in agent_map:
            v = agent_map[comp]
            if abs(v - gold_val) <= tol:
                hits += 1
            agent_vals.append(v)
            ref_vals.append(gold_val)

    tolerance_score = hits / len(order)

    # Spearman rank correlation to replace scipy.stats.kendalltau
    n = len(agent_vals)
    if n < 2:
        ordering_score = 0.5
    else:
        # rank data (average ranks for ties)
        def rankdata(a):
            n = len(a)
            idx = sorted(range(n), key=lambda i: a[i])
            ranks = [0]*n
            i = 0
            while i < n:
                j = i
                while j < n and a[idx[j]] == a[idx[i]]:
                    j += 1
                r = 1 + (i + j - 1) / 2.0  # 1-indexed average rank
                for k in range(i, j):
                    ranks[idx[k]] = r
                i = j
            return ranks
        rank_a = rankdata(agent_vals)
        rank_r = rankdata(ref_vals)
        mean_ra = sum(rank_a) / n
        mean_rr = sum(rank_r) / n
        num = sum((ra - mean_ra)*(rr - mean_rr) for ra, rr in zip(rank_a, rank_r))
        denom_a = math.sqrt(sum((ra - mean_ra)**2 for ra in rank_a))
        denom_b = math.sqrt(sum((rr - mean_rr)**2 for rr in rank_r))
        if denom_a == 0 or denom_b == 0:
            rho = 0.0
        else:
            rho = num / (n * denom_a * denom_b)
        ordering_score = (rho + 1.0) / 2.0

    return 0.5 * tolerance_score + 0.5 * ordering_score


_SCORERS = {
    'band_gaps_scorer': score_0,
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
