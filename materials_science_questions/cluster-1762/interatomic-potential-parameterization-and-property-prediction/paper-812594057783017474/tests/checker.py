import os
import json
import csv

# === author imports / helpers ===
import csv
import json
import os


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


# === block: score_0 (check id='cohesive_scoring') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold_rows = step.get('gold_rows', [])
        if not gold_rows:
            return 0.0
        agent_map = {}
        for row in artifact:
            try:
                n = int(row['n'])
                m = int(row['m'])
                alpha = float(row['alpha'])
                val = float(row['Ea_E0'])
                key = (n, m, alpha)
                agent_map[key] = val
            except (ValueError, KeyError, TypeError):
                continue
        tol_abs = step.get('tolerance_abs', 0.02)
        tol_rel = step.get('tolerance_rel', 0.05)
        matched = 0
        for g in gold_rows:
            key = (g['n'], g['m'], g['alpha'])
            if key not in agent_map:
                continue
            agent_val = agent_map[key]
            gold_val = g['gold_Ea_E0']
            if abs(agent_val - gold_val) <= max(tol_abs, tol_rel * gold_val):
                matched += 1
        return matched / len(gold_rows) if gold_rows else 0.0


# === block: score_1 (check id='melting_scoring') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        params = step.get('params', {})
        if not artifact:
            return 0.0
        # Group by (m, alpha)
        groups = {}
        for row in artifact:
            try:
                m = int(row['m'])
                alpha = float(row['alpha'])
                n = int(row['n'])
                ratio = float(row['Tm_Tmbulk'])
            except (ValueError, KeyError, TypeError):
                continue
            key = (m, alpha)
            if key not in groups:
                groups[key] = []
            groups[key].append((n, ratio))
        # Sort each group by n
        for key in groups:
            groups[key].sort(key=lambda x: x[0])
        # 1. Monotonicity: ratio non-decreasing with n (allow small decrease)
        mono_tol = params.get('monotonicity_tolerance', 0.01)
        mono_pass = 0
        mono_total = 0
        for key, vals in groups.items():
            mono_total += 1
            if len(vals) < 2:
                mono_pass += 1
                continue
            increasing = True
            for i in range(len(vals)-1):
                if vals[i][1] - vals[i+1][1] > mono_tol:
                    increasing = False
                    break
            if increasing:
                mono_pass += 1
        mono_score = mono_pass / mono_total if mono_total > 0 else 0.0
        # 2. Ordering across alphas at each n: must decrease (higher alpha -> lower ratio)
        ordering_sets = params.get('ordering_sets', [])
        ord_tol = params.get('ordering_tolerance', 0.01)
        # collect all n values across all groups
        all_n = set()
        for vals in groups.values():
            for n, _ in vals:
                all_n.add(n)
        order_pass = 0
        order_total = 0
        for n in sorted(all_n):
            order_total += 1
            n_ok = True
            for rule in ordering_sets:
                m = rule['m']
                alphas = rule['alphas']
                # alphas are assumed in increasing order; we check for non-increasing ratio
                vals = []
                missing = False
                for a in alphas:
                    if (m, a) not in groups:
                        missing = True
                        break
                    found = None
                    for (nn, r) in groups[(m, a)]:
                        if nn == n:
                            found = r
                            break
                    if found is None:
                        missing = True
                        break
                    vals.append(found)
                if missing:
                    continue
                # Ensure values are non-increasing (later should not be significantly larger than earlier)
                for i in range(len(vals)-1):
                    if vals[i+1] - vals[i] > ord_tol:
                        n_ok = False
                        break
                if not n_ok:
                    break
            if n_ok:
                order_pass += 1
        order_score = order_pass / order_total if order_total > 0 else 0.0
        # 3. Range check [0,1]
        range_ok = True
        for row in artifact:
            try:
                r = float(row.get('Tm_Tmbulk', -1))
            except:
                continue
            if r < -0.01 or r > 1.01:
                range_ok = False
                break
        range_score = 1.0 if range_ok else 0.0
        # weighted combination
        w_mono = params.get('monotonicity_weight', 0.4)
        w_order = params.get('ordering_weight', 0.4)
        w_range = params.get('range_weight', 0.2)
        total = w_mono * mono_score + w_order * order_score + w_range * range_score
        return max(0.0, min(1.0, total))


_SCORERS = {
    'cohesive_scoring': score_0,
    'melting_scoring': score_1,
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
