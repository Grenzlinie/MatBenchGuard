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
    gold = spec.get('gold_data', {})
    step_02_gold = gold.get('step_02_gold', [])
    step_03_gold_set = set(gold.get('step_03_gold_set', []))
    return {
        'step_02_gold': step_02_gold,
        'step_02_gold_dict': {entry['SAC_id']: entry['DeltaG_Ostar'] for entry in step_02_gold},
        'step_03_gold_set': step_03_gold_set,
    }


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
        if not artifact or not isinstance(artifact, list) or len(artifact) == 0:
            return 0.0
        # Build case‑insensitive column map from first row
        first_row = artifact[0]
        col_map = {}
        for orig_key, _ in first_row.items():
            k = orig_key.strip().lower()
            if k == 'sac_id':  col_map['sac_id'] = orig_key
            elif k == 'metal': col_map['metal'] = orig_key
            elif k == 'substrate': col_map['substrate'] = orig_key
            elif k == 'ef':    col_map['ef'] = orig_key
            elif k == 'udiss': col_map['udiss'] = orig_key
            elif k == 'stable': col_map['stable'] = orig_key
        # Fail early if required columns missing
        for needed in ('sac_id', 'metal', 'substrate', 'ef', 'udiss'):
            if needed not in col_map:
                return 0.0
        target = step.get('target', {})
        expected_stable = target.get('stable_count', 149)
        expected_substrate = target.get('substrate_counts', {})
        stable_rows = []
        substrate_counts = {}
        for row in artifact:
            try:
                Ef = float(row.get(col_map['ef'], 0))
                Udiss = float(row.get(col_map['udiss'], 0))
                stable = Ef < 0 and Udiss > 0
                if stable:
                    substrate = row.get(col_map['substrate'], '').strip()
                    stable_rows.append(substrate)
                    substrate_counts[substrate] = substrate_counts.get(substrate, 0) + 1
            except (ValueError, TypeError):
                continue
        total_stable = len(stable_rows)
        # score total stable count: full credit within ±2, linear decay to 0 at ±12
        diff_total = abs(total_stable - expected_stable)
        if diff_total <= 2:
            total_score = 1.0
        else:
            total_score = max(0.0, 1.0 - (diff_total - 2) / 10.0)
        # score per‑substrate counts: average across expected substrates
        sub_score = 1.0
        if expected_substrate:
            scores = []
            for sub, exp_cnt in expected_substrate.items():
                act = substrate_counts.get(sub, 0)
                d = abs(act - exp_cnt)
                if d <= 2:
                    scores.append(1.0)
                else:
                    scores.append(max(0.0, 1.0 - (d - 2) / 10.0))
            sub_score = sum(scores) / len(scores)
        return total_score * sub_score


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    import math

    def score(artifact, step, ctx):
        if not artifact:
            return 0.0
        gold_dict = ctx.get('step_02_gold_dict', {})
        if not gold_dict:
            return 0.0
        target = step.get('target', {}).get('rmse', {})
        thresh = target.get('threshold', 0.2)
        decay = target.get('decay_factor', 0.5)
        # build agent dict
        agent_dict = {}
        for row in artifact:
            sid = row.get('SAC_id', '').strip()
            try:
                val = float(row.get('DeltaG_Ostar', 0))
                agent_dict[sid] = val
            except (ValueError, TypeError):
                continue
        # compute RMSE over all gold SACs
        err_sq = 0.0
        count = 0
        for sid, gval in gold_dict.items():
            if sid in agent_dict:
                diff = agent_dict[sid] - gval
                err_sq += diff * diff
                count += 1
            else:
                # missing – treat as large error
                err_sq += 5.0 ** 2
                count += 1
        if count == 0:
            return 0.0
        rmse = math.sqrt(err_sq / count)
        if rmse <= thresh:
            return 1.0
        else:
            score = max(0.0, 1.0 - (rmse - thresh) / (decay * thresh + 1e-9))
            return score


# === block: score_2 (check id='step_03') ===
def score_2(artifact, step, ctx):
    import math

    def score(artifact, step, ctx):
        gold_set = ctx.get('step_03_gold_set', set())
        if not gold_set:
            return 0.0
        if not artifact:
            return 0.0
        # recompute selective list from step_02 DeltaG_Ostar
        # We can read step_02 directly (it's available in the same run)
        # But to keep scorer independent, we'll just compare agent's step_03 list.
        # However to enforce consistency we could load step_02 inside, but not needed.
        agent_ids = set()
        for row in artifact:
            sid = row.get('SAC_id', '').strip()
            if sid:
                agent_ids.add(sid)
        if not agent_ids:
            return 0.0
        # compute F1
        tp = len(agent_ids & gold_set)
        if tp == 0:
            return 0.0
        precision = tp / len(agent_ids)
        recall = tp / len(gold_set)
        f1 = 2 * precision * recall / (precision + recall)
        return f1


# === block: score_3 (check id='step_04') ===
def score_3(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not artifact or len(artifact) == 0:
            return 0.0
        row = artifact[0]
        sid = row.get('SAC_id', '').strip()
        if sid != 'Zn@Pc-N4':
            return 0.0
        try:
            overpot = float(row.get('overpotential', 999))
        except (ValueError, TypeError):
            return 0.0
        return 1.0 if overpot <= 0.25 else 0.0


_SCORERS = {
    'step_01': score_0,
    'step_02': score_1,
    'step_03': score_2,
    'step_04': score_3,
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
