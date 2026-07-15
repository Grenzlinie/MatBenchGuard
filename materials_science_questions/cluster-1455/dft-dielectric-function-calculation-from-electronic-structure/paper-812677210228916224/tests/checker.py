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


# === block: score_0 (check id='mech_values') ===
def score_0(artifact, step, ctx):
    def score_mech_values(artifact, step, ctx):
        gold = step['gold']
        tolerances = step['tolerances']
        cols = ['B_H', 'G_H', 'B_H_G_H', 'v', 'C12_C44']
        total = 0
        within = 0
        for row in artifact:
            p = str(row.get('pressure', '')).strip()
            if p not in gold:
                continue
            expected = gold[p]
            for col in cols:
                try:
                    val = float(row.get(col, 0))
                except (ValueError, TypeError):
                    continue
                exp = expected[col]
                tol_info = tolerances[col]
                if tol_info['type'] == 'relative':
                    tol = tol_info['value'] * abs(exp) + 1e-9
                else:
                    tol = tol_info['value'] + 1e-9
                total += 1
                if abs(val - exp) <= tol:
                    within += 1
        if total == 0:
            return 0.0
        return within / total


# === block: score_1 (check id='mech_trend') ===
def score_1(artifact, step, ctx):
    def score_mech_trend(artifact, step, ctx):
        rows = []
        for row in artifact:
            try:
                p = int(row.get('pressure', -1))
                b = float(row.get('B_H', 0))
                g = float(row.get('G_H', 0))
                bhg = float(row.get('B_H_G_H', 0))
                v = float(row.get('v', 0))
                c12 = float(row.get('C12_C44', 0))
                rows.append((p, b, g, bhg, v, c12))
            except (ValueError, TypeError):
                continue
        if not rows:
            return 0.0
        rows.sort(key=lambda x: x[0])
        bh_ok = all(rows[i][1] >= rows[i-1][1] for i in range(1, len(rows)))
        gh_ok = all(rows[i][2] >= rows[i-1][2] for i in range(1, len(rows)))
        row_dict = {r[0]: r for r in rows}
        bhg_anomaly = 0
        v_anomaly = 0
        if 10 in row_dict and 15 in row_dict:
            bhg_anomaly = 1 if row_dict[15][3] < row_dict[10][3] else 0
            v_anomaly = 1 if row_dict[15][4] < row_dict[10][4] else 0
        c12_sign = 0
        if 0 in row_dict and 5 in row_dict:
            c12_0 = row_dict[0][5]
            c12_5 = row_dict[5][5]
            if c12_0 < 0 and c12_5 > 0:
                c12_sign = 1
        subs = [bh_ok, gh_ok, bhg_anomaly, v_anomaly, c12_sign]
        return sum(subs) / float(len(subs))


# === block: score_2 (check id='bandgap_values') ===
def score_2(artifact, step, ctx):
    def score_bandgap_values(artifact, step, ctx):
        gold = step.get('gold', {})
        tol = step.get('tolerance', {}).get('value', 0.2)
        gaps = []
        # 0) extract all pressure/gap pairs from artifact
        for row in artifact:
            p_str = str(row.get('pressure', '')).strip()
            try:
                p = int(p_str)
                gap = float(row.get('band_gap', 0))
                gaps.append((p, gap))
            except (ValueError, TypeError):
                continue
        if not gaps:
            return 0.0
        gaps.sort(key=lambda x: x[0])
        # 1) value checks at P=0 and P=40
        value_checks = 0
        value_passed = 0
        for p, gap in gaps:
            if p in (0, 40):
                exp = gold.get(str(p))
                if exp is not None:
                    value_checks += 1
                    if abs(gap - exp) <= tol:
                        value_passed += 1
        # 2) trend check: non‑increasing (decreasing or equal)
        trend_ok = 1 if all(gaps[i][1] >= gaps[i+1][1] for i in range(len(gaps)-1)) else 0
        total_checks = value_checks + 1  # add the trend check
        passed_checks = value_passed + trend_ok
        return passed_checks / total_checks if total_checks else 0.0


# === block: score_3 (check id='refractive_values') ===
def score_3(artifact, step, ctx):
    def score_refractive_values(artifact, step, ctx):
        gold = step['gold']
        tol = step['tolerance']['value']
        total = 0
        within = 0
        for row in artifact:
            d = str(row.get('direction', '')).strip()
            if d not in gold:
                continue
            try:
                n0 = float(row.get('static_refractive_index_n0', 0))
            except (ValueError, TypeError):
                continue
            total += 1
            if abs(n0 - gold[d]) <= tol:
                within += 1
        if total == 0:
            return 0.0
        return within / total


_SCORERS = {
    'mech_values': score_0,
    'mech_trend': score_1,
    'bandgap_values': score_2,
    'refractive_values': score_3,
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
