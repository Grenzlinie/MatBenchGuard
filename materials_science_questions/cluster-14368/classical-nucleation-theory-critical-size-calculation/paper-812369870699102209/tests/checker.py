import os
import json
import csv

# === author imports / helpers ===
import os, json, csv


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


# === block: score_0 (check id='step_m_upper') ===
def score_0(artifact, step, ctx):
    targets = step.get('targets', {})
    if not isinstance(artifact, dict):
        return 0.0
    total = 0
    count = 0
    for field, tspec in targets.items():
        val = artifact.get(field)
        if val is None:
            continue
        try:
            val_num = float(val)
            target_num = float(tspec['value'])
            tol_num = float(tspec.get('tolerance', 0.0))
        except (TypeError, KeyError, ValueError):
            continue
        if abs(val_num - target_num) <= tol_num:
            total += 1
        count += 1
    return total / count if count > 0 else 0.0


# === block: score_1 (check id='step_nat_thresh') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        rows = artifact
        if not rows:
            return 0.0
        config = step.get('config', {})
        pcol100 = config.get('probability_column_100mbar', 'P_100mbar')
        pcol50 = config.get('probability_column_50mbar', 'P_50mbar')
        mcol = config.get('m_column', 'm')
        thresh_prob = config.get('threshold_probability', 0.9999)
        gold = config.get('gold_thresholds', {})

        def find_threshold(pcol):
            # assume rows sorted by m increasing
            for row in rows:
                try:
                    p = float(row[pcol])
                    if p >= thresh_prob:
                        return float(row[mcol])
                except (ValueError, KeyError):
                    continue
            return float('inf')

        th100 = find_threshold(pcol100)
        th50 = find_threshold(pcol50)

        def score_one(th, gkey):
            g = gold.get(gkey)
            if g is None:
                return 0.0
            target = g['value']
            tol = g.get('tolerance', 0.0)
            if th == float('inf'):
                return 0.0
            return 1.0 if abs(th - target) <= tol else 0.0

        s1 = score_one(th100, '100mbar')
        s2 = score_one(th50, '50mbar')
        return 0.5 * s1 + 0.5 * s2


# === block: score_2 (check id='step_sbs_thresh') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        rows = artifact
        if not rows:
            return 0.0
        config = step.get('config', {})
        pcol100 = config.get('probability_column_100mbar', 'P_100mbar')
        pcol50 = config.get('probability_column_50mbar', 'P_50mbar')
        mcol = config.get('m_column', 'm')
        thresh_prob = config.get('threshold_probability', 0.9999)
        gold = config.get('gold_thresholds', {})

        def find_threshold(pcol):
            for row in rows:
                try:
                    p = float(row[pcol])
                    if p >= thresh_prob:
                        return float(row[mcol])
                except (ValueError, KeyError):
                    continue
            return float('inf')

        th100 = find_threshold(pcol100)
        th50 = find_threshold(pcol50)

        def score_one(th, gkey):
            g = gold.get(gkey)
            if g is None:
                return 0.0
            target = g['value']
            tol = g.get('tolerance', 0.0)
            if th == float('inf'):
                return 0.0
            return 1.0 if abs(th - target) <= tol else 0.0

        s1 = score_one(th100, '100mbar')
        s2 = score_one(th50, '50mbar')
        return 0.5 * s1 + 0.5 * s2


# === block: score_3 (check id='step_structural') ===
def score_3(artifact, step, ctx):
    import os, json, csv

    def score(artifact, step, ctx):
        outputs_dir = '/app/outputs'
        # load m_upper_limits
        limits_path = os.path.join(outputs_dir, 'm_upper_limits.json')
        try:
            with open(limits_path) as f:
                limits = json.load(f)
            m_NAT_SAT = limits['m_NAT_SAT']
            m_SBS_SAT = limits['m_SBS_SAT']
        except Exception:
            return 0.0

        # load NAT CSV and find thresholds
        nat_path = os.path.join(outputs_dir, 'nucleation_probability_NAT.csv')
        sbs_path = os.path.join(outputs_dir, 'nucleation_probability_SBS.csv')
        def find_threshold(path, pcol, mcol='m', thresh_prob=0.9999):
            try:
                with open(path, newline='') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        if float(row[pcol]) >= thresh_prob:
                            return float(row[mcol])
            except Exception:
                return None
            return None

        nat_100 = find_threshold(nat_path, 'P_100mbar')
        nat_50 = find_threshold(nat_path, 'P_50mbar')
        sbs_100 = find_threshold(sbs_path, 'P_100mbar')
        sbs_50 = find_threshold(sbs_path, 'P_50mbar')

        score = 0.0
        count = 0
        if nat_100 is not None:
            if nat_100 >= m_NAT_SAT:
                score += 0.25
            count += 1
        if nat_50 is not None:
            if nat_50 >= m_NAT_SAT:
                score += 0.25
            count += 1
        if sbs_100 is not None:
            if sbs_100 >= m_SBS_SAT:
                score += 0.25
            count += 1
        if sbs_50 is not None:
            if sbs_50 >= m_SBS_SAT:
                score += 0.25
            count += 1
        # If some thresholds missing, we give 0 for those sub-checks.
        # If count=0, score stays 0.
        return score


_SCORERS = {
    'step_m_upper': score_0,
    'step_nat_thresh': score_1,
    'step_sbs_thresh': score_2,
    'step_structural': score_3,
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
