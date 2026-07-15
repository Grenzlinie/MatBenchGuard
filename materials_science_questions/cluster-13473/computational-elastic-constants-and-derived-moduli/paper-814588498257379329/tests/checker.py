import os
import json
import csv


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


# === block: score_0 (check id='equilibrium_swelling') ===
def score_0(artifact, step, ctx):
    # Compare l0 for DC and SC against hidden gold with relative tolerance.
    gold = step.get('gold', {})
    tol_rel = step.get('tol_rel', 0.05)
    def score_l0(row, expected):
        try:
            val = float(row['l0'])
        except:
            return 0.0
        if expected == 0:
            return 1.0 if abs(val) < 1e-9 else 0.0
        err = abs(val - expected) / abs(expected)
        if err <= tol_rel:
            return 1.0
        return max(0.0, 1.0 - (err - tol_rel) / (2 * tol_rel))
    dc = next((r for r in artifact if r.get('topology') == 'DC'), None)
    sc = next((r for r in artifact if r.get('topology') == 'SC'), None)
    if dc is None or sc is None:
        return 0.0
    s1 = score_l0(dc, gold.get('DC_l0', 0.0))
    s2 = score_l0(sc, gold.get('SC_l0', 0.0))
    return (s1 + s2) / 2.0


# === block: score_1 (check id='deformation_data') ===
def score_1(artifact, step, ctx):
    # Quantitative comparison per (topology, alpha) + structural checks (monotonicity, sign, volume shrinkage).
    gold_points = step.get('gold', {})
    gold_l0 = step.get('gold_l0', {})
    tol_l = step.get('tol_rel_length', 0.05)
    tol_vs = step.get('tol_rel_vs', 0.10)

    def compare_val(val, exp, tol):
        if exp == 0:
            return 1.0 if abs(val) < 1e-6 else 0.0
        err = abs(val - exp) / abs(exp)
        if err <= tol:
            return 1.0
        return max(0.0, 1.0 - (err - tol) / (2 * tol))

    col_to_gold = {'l_parallel': 'lp', 'l_perpendicular': 'lt', 'volume_shrinkage': 'vs'}

    numeric_scores = []
    for topo in ['DC', 'SC']:
        topo_rows = [r for r in artifact if r.get('topology') == topo]
        if not topo_rows:
            return 0.0
        for row in topo_rows:
            alpha_key = "{:.1f}".format(float(row['alpha']))
            exp = gold_points.get(topo, {}).get(alpha_key)
            if exp is None:
                continue
            for key, tol in [('l_parallel', tol_l), ('l_perpendicular', tol_l), ('volume_shrinkage', tol_vs)]:
                gold_key = col_to_gold[key]
                try:
                    v = float(row[key])
                except:
                    numeric_scores.append(0.0)
                    continue
                numeric_scores.append(compare_val(v, exp[gold_key], tol))
    if not numeric_scores:
        return 0.0
    quant_score = sum(numeric_scores) / len(numeric_scores)

    # Structural checks
    structural = 1.0
    for topo in ['DC', 'SC']:
        rows = sorted([r for r in artifact if r.get('topology') == topo], key=lambda x: float(x['alpha']))
        lps = [float(r['l_parallel']) for r in rows]
        # monotonic non-increasing
        for i in range(len(lps)-1):
            if lps[i+1] > lps[i] + 1e-6:
                structural = 0.0
                break
        if structural == 0.0:
            break
        # sign of perpendicular deformation relative to l0
        if topo in gold_l0:
            l0_val = gold_l0[topo]
            for r in rows:
                if float(r['alpha']) > 0:
                    if topo == 'DC' and float(r['l_perpendicular']) <= l0_val + 1e-4:
                        structural = 0.0
                        break
                    if topo == 'SC' and float(r['l_perpendicular']) >= l0_val - 1e-4:
                        structural = 0.0
                        break
        # volume shrinkage non-negative and non-decreasing
        vss = [float(r['volume_shrinkage']) for r in rows]
        for v in vss:
            if v < -1e-6:
                structural = 0.0
                break
        for i in range(len(vss)-1):
            if vss[i+1] < vss[i] - 1e-6:
                structural = 0.0
                break

    return 0.7 * quant_score + 0.3 * structural


# === block: score_2 (check id='elastic_constants') ===
def score_2(artifact, step, ctx):
    # Compare a,b,c,d,e against gold per topology and field condition.
    expected = step['gold']
    tol_rel = step.get('tol_rel', 0.15)
    scores = []
    columns = ['a', 'b', 'c', 'd', 'e']
    for row in artifact:
        key = row['topology'] + '_' + row['field_condition']
        exp = expected.get(key)
        if exp is None:
            continue
        for idx, col in enumerate(columns):
            try:
                val = float(row[col])
            except:
                scores.append(0.0)
                continue
            exp_val = exp[idx]
            if exp_val == 0:
                s = 1.0 if abs(val) < 1e-6 else 0.0
            else:
                err = abs(val - exp_val) / abs(exp_val)
                if err <= tol_rel:
                    s = 1.0
                else:
                    s = max(0.0, 1.0 - (err - tol_rel) / (2 * tol_rel))
            scores.append(s)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_3 (check id='magnetization_curve') ===
def score_3(artifact, step, ctx):
    # Compare M per topology and alpha, plus monotonicity check.
    expected = step['gold']
    tol = step.get('tol_rel', 0.10)
    scores = []
    for topo in ['DC', 'SC']:
        topo_rows = [r for r in artifact if r.get('topology') == topo]
        if not topo_rows:
            return 0.0
        topo_rows.sort(key=lambda x: float(x['alpha']))
        prev_m = -1e9
        for row in topo_rows:
            alpha_key = "{:.1f}".format(float(row['alpha']))
            exp_val = expected.get(topo, {}).get(alpha_key)
            if exp_val is None:
                continue
            try:
                m = float(row['M'])
            except:
                scores.append(0.0)
                continue
            # quantitative
            if exp_val == 0:
                quant_s = 1.0 if abs(m) < 1e-6 else 0.0
            else:
                err = abs(m - exp_val) / abs(exp_val)
                if err <= tol:
                    quant_s = 1.0
                else:
                    quant_s = max(0.0, 1.0 - (err - tol) / (2 * tol))
            # monotonic increase
            mono_s = 1.0 if (prev_m <= m + 1e-6) else 0.0
            scores.append(0.8 * quant_s + 0.2 * mono_s)
            prev_m = m
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


_SCORERS = {
    'equilibrium_swelling': score_0,
    'deformation_data': score_1,
    'elastic_constants': score_2,
    'magnetization_curve': score_3,
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
