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
    def prepare(outputs_dir, spec):
        # no shared preparation needed; scorer uses step's inline gold
        return {}


# === block: score_0 (check id='check_ul_values_and_trend') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        import csv
        # artifact is expected to be a list of dicts (from csv.DictReader)
        if not isinstance(artifact, list) or len(artifact) == 0:
            return 0.0
        # required columns
        if 'System' not in artifact[0] or 'UL_V' not in artifact[0] or '\u0394Gmax_eV' not in artifact[0]:
            return 0.0
        gold = step.get('gold_values', {})
        tol = step.get('tolerance_abs', 0.15)
        systems_found = set()
        ul_map = {}
        dg_map = {}
        consistency_ok = 0
        for row in artifact:
            sys = row.get('System', '').strip()
            if not sys:
                continue
            try:
                ul = float(row['UL_V'])
                dg = float(row['\u0394Gmax_eV'])
            except (ValueError, TypeError):
                continue
            if abs(ul + dg) <= 0.01:  # UL = -ΔGmax / e, e in eV/V is 1
                consistency_ok += 1
            ul_map[sys] = ul
            dg_map[sys] = dg
            systems_found.add(sys)
        n_rows = len(artifact)
        if n_rows == 0:
            return 0.0
        consistency_score = consistency_ok / n_rows if n_rows > 0 else 0.0
        # value agreement
        matches = 0
        for sys, gold_ul in gold.items():
            if sys in ul_map:
                if abs(ul_map[sys] - gold_ul) <= tol:
                    matches += 1
            else:
                # missing system counts as mismatch
                pass
        value_score = matches / len(gold) if gold else 0.0
        # trend: F-Fe@F-G must have the highest (least negative) UL
        required_sys = step.get('trend_check', {}).get('required_highest_system', '')
        trend_score = 0.0
        if required_sys and required_sys in ul_map:
            max_ul = max(ul_map.values()) if ul_map else None
            # check that not all ULs are equal (degenerate)
            if max_ul is not None and max_ul > min(ul_map.values()):
                if ul_map[required_sys] == max_ul:
                    trend_score = 1.0
        # combine with weights: 0.2 consistency, 0.5 value agreement, 0.3 trend
        total = 0.2 * consistency_score + 0.5 * value_score + 0.3 * trend_score
        # clamp to [0,1]
        return min(1.0, max(0.0, total))


_SCORERS = {
    'check_ul_values_and_trend': score_0,
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
