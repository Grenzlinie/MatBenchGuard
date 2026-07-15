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
    def compute_gold_d0(params):
        c11 = params['c11']
        c12 = params['c12']
        gamma = params['gamma']
        bp = params['bp']
        M = (c11**2 - c12**2) / (8.0 * math.pi * c11)
        gold = {}
        for deg in params['theta_deg']:
            rad = math.radians(deg)
            x = math.sqrt(3) * gamma / (bp * M * 2.0 * rad)
            alpha = 0.5 - math.atan(x) / math.pi
            d = bp / (2.0 * math.sin(rad / 2.0))
            d0 = alpha * d
            gold[deg] = d0 / 1e-9
        return gold

    params = spec['steps'][2]['params']
    gold_d0 = compute_gold_d0(params)
    return {'gold_d0': gold_d0}


# === block: score_0 (check id='bulk_properties') ===
def score_0(artifact, step, ctx):
    # normalize artifact to list of dicts
    if isinstance(artifact, dict):
        entries = [artifact]
    elif isinstance(artifact, list):
        entries = artifact
    else:
        return 0.0

    gold = step.get('gold', {})
    # thresholds from the approved plan:
    # lattice (a, cos α, V0) < 30%, elastic constants < 20%
    lattice_threshold = 0.3
    elastic_threshold = 0.2
    lattice_decay = 0.3
    elastic_decay = 0.3

    lattice_keys = ['a_rhombohedral', 'cos_alpha', 'V0']
    elastic_keys = ['c11', 'c12', 'c13', 'c33', 'c14', 'c44']

    lattice_errors = []
    elastic_errors = []

    for entry in entries:
        method = entry.get('method')
        if method not in gold:
            continue
        g = gold[method]
        # lattice errors
        for key in lattice_keys:
            agent_val = entry.get(key)
            if agent_val is None:
                return 0.0
            ref = g.get(key)
            if ref is None:
                continue
            if ref == 0:
                if agent_val != 0:
                    lattice_errors.append(1.0)
                else:
                    lattice_errors.append(0.0)
            else:
                lattice_errors.append(abs(agent_val - ref) / abs(ref))
        # elastic errors
        for key in elastic_keys:
            agent_val = entry.get(key)
            if agent_val is None:
                return 0.0
            ref = g.get(key)
            if ref is None:
                continue
            if ref == 0:
                if agent_val != 0:
                    elastic_errors.append(1.0)
                else:
                    elastic_errors.append(0.0)
            else:
                elastic_errors.append(abs(agent_val - ref) / abs(ref))

    if not lattice_errors and not elastic_errors:
        return 0.0

    lattice_mape = sum(lattice_errors) / len(lattice_errors) if lattice_errors else 0.0
    elastic_mape = sum(elastic_errors) / len(elastic_errors) if elastic_errors else 0.0

    def part_score(mape, thresh, decay):
        if mape <= thresh:
            return 1.0
        else:
            return max(0.0, 1.0 - (mape - thresh) / decay)

    lattice_part = part_score(lattice_mape, lattice_threshold, lattice_decay)
    elastic_part = part_score(elastic_mape, elastic_threshold, elastic_decay)

    return 0.5 * lattice_part + 0.5 * elastic_part


# === block: score_1 (check id='sfe_values') ===
def score_1(artifact, step, ctx):
    def score_sfe(artifact, step, ctx):
        gold = step.get('gold', [])
        low = step.get('mape_threshold_low', 0.20)
        high = step.get('mape_threshold_high', 0.50)
        if not isinstance(artifact, list):
            return 0.0
        gold_lookup = {g['fault_id']: g for g in gold}
        errors = []
        for entry in artifact:
            fid = entry.get('fault_id')
            if fid not in gold_lookup:
                continue
            g = gold_lookup[fid]
            for field in ['LDA', 'GGA']:
                agent_val = entry.get(field)
                ref = g.get(field)
                if ref is None:
                    continue
                if agent_val is None:
                    errors.append(1.0)
                    continue
                errors.append(abs(agent_val - ref) / abs(ref) if ref != 0 else (0.0 if agent_val == 0 else 1.0))
            shell_fields = ['shell_Gale_Henson_0K', 'shell_Gale_Henson_1800K', 'shell_Minervini_0K', 'shell_Minervini_1800K']
            for field in shell_fields:
                ref = g.get(field)
                if ref is not None:
                    agent_val = entry.get(field)
                    if agent_val is None:
                        errors.append(1.0)
                    else:
                        errors.append(abs(agent_val - ref) / abs(ref))
        if not errors:
            return 0.0
        mape = sum(errors) / len(errors)
        if mape <= low:
            return 1.0
        elif mape >= high:
            return 0.0
        else:
            return 1.0 - (mape - low) / (high - low)

    return score_sfe(artifact, step, ctx)


# === block: score_2 (check id='dislocation_spacing') ===
def score_2(artifact, step, ctx):
    rows = artifact if isinstance(artifact, list) else []
    gold_d0 = ctx.get('gold_d0', {})
    rmse_full = step.get('rmse_full', 0.05)
    rmse_zero = step.get('rmse_zero', 0.20)
    sq = []
    for row in rows:
        try:
            deg = float(row['theta_deg'])
            d0 = float(row['d0_nm'])
        except (KeyError, ValueError, TypeError):
            return 0.0
        gold = gold_d0.get(deg)
        if gold is None:
            return 0.0
        sq.append((d0 - gold) ** 2)
    if not sq:
        return 0.0
    rmse = math.sqrt(sum(sq) / len(sq))
    if rmse <= rmse_full:
        return 1.0
    elif rmse >= rmse_zero:
        return 0.0
    else:
        return 1.0 - (rmse - rmse_full) / (rmse_zero - rmse_full)


# === block: score_3 (check id='sfe_order') ===
def score_3(artifact, step, ctx):
    def order_score(artifact, order_lda, order_gga):
        def check_order(vals, expected):
            if len(vals) < 2:
                return 0.0
            correct = 0
            for i in range(len(expected) - 1):
                a = vals.get(expected[i])
                b = vals.get(expected[i + 1])
                if a is None or b is None:
                    continue
                if a < b:
                    correct += 1
            return correct / max(1, len(expected) - 1)
    
        if not isinstance(artifact, list):
            return 0.0
        lda_vals = {}
        gga_vals = {}
        for entry in artifact:
            fid = entry.get('fault_id')
            if fid is None:
                continue
            lda_val = entry.get('LDA')
            gga_val = entry.get('GGA')
            if lda_val is not None:
                lda_vals[fid] = lda_val
            if gga_val is not None:
                gga_vals[fid] = gga_val
        score_lda = check_order(lda_vals, order_lda)
        score_gga = check_order(gga_vals, order_gga)
        return 0.5 * score_lda + 0.5 * score_gga

    return order_score(artifact, step.get('expected_order_lda', []), step.get('expected_order_gga', []))


_SCORERS = {
    'bulk_properties': score_0,
    'sfe_values': score_1,
    'dislocation_spacing': score_2,
    'sfe_order': score_3,
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
