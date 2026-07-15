import os
import json
import csv

# === author imports / helpers ===
import math
import json


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
        phi_m_deg = {45: 16.0, 60: 13.0, 75: 12.0}
        d_mm = {}
        for gamma in [45, 60, 75]:
            d_mm[gamma] = 5.0 / math.cos(math.radians(gamma))
        rotation_gold = {
            45: math.tan(math.radians(16.0)) / d_mm[45],
            60: math.tan(math.radians(13.0)) / d_mm[60],
            75: math.tan(math.radians(12.0)) / d_mm[75],
        }
        ctx = {
            'phi_m_deg': phi_m_deg,
            'd_mm': d_mm,
            'rotation_gold': rotation_gold
        }
        return ctx


# === block: score_0 (check id='kink_score') ===
def score_0(artifact, step, ctx):
        if not artifact:
            return 0.0
        phi_m_deg = ctx['phi_m_deg']
        d_mm = ctx['d_mm']
        threshold_mvk = step['params']['threshold_mvk']
        threshold_mts = step['params']['threshold_mts']
        wmvk = step['params']['sub_weights']['mvk']
        wmts = step['params']['sub_weights']['mts']
        se_mts = 0.0
        se_mvk = 0.0
        n_mts = 0
        n_mvk = 0
        for row in artifact:
            try:
                gamma = int(float(row['gamma']))
                if gamma not in phi_m_deg:
                    continue
                x3 = float(row['x3'])
                # exclude points too close to the edge (SIF unreliable)
                d = d_mm[gamma]
                if x3 > 0.98 * d or x3 <= 0.0:
                    continue
                phi_gold = math.degrees(math.atan( (x3 / d) * math.tan(math.radians(phi_m_deg[gamma])) ))
                phi_mts = float(row['phi_MTS'])
                phi_mvk = float(row['phi_MVK'])
                se_mts += (phi_mts - phi_gold) ** 2
                n_mts += 1
                se_mvk += (phi_mvk - phi_gold) ** 2
                n_mvk += 1
            except (KeyError, ValueError):
                continue
        if n_mts == 0 or n_mvk == 0:
            return 0.0
        rmse_mts = math.sqrt(se_mts / n_mts)
        rmse_mvk = math.sqrt(se_mvk / n_mvk)
        if rmse_mvk <= threshold_mvk:
            score_mvk = 1.0
        else:
            score_mvk = max(0.0, 1.0 - (rmse_mvk - threshold_mvk) / threshold_mvk)
        if rmse_mts <= threshold_mts:
            score_mts = 1.0
        else:
            score_mts = max(0.0, 1.0 - (rmse_mts - threshold_mts) / threshold_mts)
        combined = wmvk * score_mvk + wmts * score_mts
        return combined


# === block: score_1 (check id='rotation_score') ===
def score_1(artifact, step, ctx):
        if not artifact:
            return 0.0
        gold_dict = ctx['rotation_gold']
        tolerance = step['params']['tolerance']
        scores = []
        for row in artifact:
            try:
                gamma = int(float(row['gamma']))
                if gamma not in gold_dict:
                    continue
                dgamma = float(row['dgamma_ddelta'])
                gold = gold_dict[gamma]
                if gold == 0:
                    continue
                rel_err = abs(dgamma - gold) / gold
                if rel_err <= tolerance:
                    scores.append(1.0)
                else:
                    scores.append(max(0.0, 1.0 - (rel_err - tolerance) / tolerance))
            except (KeyError, ValueError):
                continue
        if not scores:
            return 0.0
        return sum(scores) / len(scores)


_SCORERS = {
    'kink_score': score_0,
    'rotation_score': score_1,
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
