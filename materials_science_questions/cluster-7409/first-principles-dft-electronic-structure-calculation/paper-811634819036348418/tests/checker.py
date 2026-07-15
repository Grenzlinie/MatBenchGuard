import os
import json
import csv

# === author imports / helpers ===
import csv, os, math


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
    import json
    def prepare(outputs_dir, spec):
        return spec


# === block: score_0 (check id='step_01_ground_state') ===
def score_0(artifact, step, ctx):
    def score(artifact_rows, step, ctx):
        gold = step['gold']
        params = {}
        for row in artifact_rows:
            name = row.get('parameter', '').strip()
            try:
                val = float(row.get('value', ''))
            except:
                continue
            params[name] = val

        checks = []
        # a
        if 'a' in params and 'a' in gold.get('a', {}):
            checks.append(1.0 if abs(params['a'] - gold['a']['value']) <= gold['a']['tol'] else 0.0)
        else:
            checks.append(0.0)
        # c
        if 'c' in params and 'c' in gold.get('c', {}):
            checks.append(1.0 if abs(params['c'] - gold['c']['value']) <= gold['c']['tol'] else 0.0)
        else:
            checks.append(0.0)
        # W-O distance
        if 'W-O distance' in params and 'W-O distance' in gold.get('W-O distance', {}):
            checks.append(1.0 if abs(params['W-O distance'] - gold['W-O distance']['value']) <= gold['W-O distance']['tol'] else 0.0)
        else:
            checks.append(0.0)
        # angle_alpha
        if 'angle_alpha' in params and 'angle_alpha' in gold.get('angle_alpha', {}):
            checks.append(1.0 if abs(params['angle_alpha'] - gold['angle_alpha']['value']) <= gold['angle_alpha']['tol'] else 0.0)
        else:
            checks.append(0.0)
        # angle_beta
        if 'angle_beta' in params and 'angle_beta' in gold.get('angle_beta', {}):
            checks.append(1.0 if abs(params['angle_beta'] - gold['angle_beta']['value']) <= gold['angle_beta']['tol'] else 0.0)
        else:
            checks.append(0.0)
        # total_energy presence check (low weight)
        te_check = 0.0
        if 'total_energy' in params:
            if gold.get('total_energy', {}).get('must_be_negative', False):
                te_check = 1.0 if params['total_energy'] < 0 else 0.0
            else:
                te_check = 1.0
        # band_gap
        if 'band_gap' in params and 'band_gap' in gold.get('band_gap', {}):
            checks.append(1.0 if abs(params['band_gap'] - gold['band_gap']['value']) <= gold['band_gap']['tol'] else 0.0)
        else:
            checks.append(0.0)
        # Combine with small weight for total_energy check
        main_checks = sum(checks)
        total = len(checks)  # 5 main + band_gap = 6? Actually appended above: a+c+WO+alpha+beta = 5, then band_gap makes 6.
        # So we have 6 checks + te_check as a separate bonus.
        base_score = main_checks / 6.0
        # add te_check as a tiny fraction (0.02 weight total, but ensure it doesn't cap total score to <1)
        # The weight of this step in aggregator is 0.35. We'll just make scorer return between 0 and 1 with base_score = (main_checks + te_check*0.1) / (6.0 + 0.1) approx.
        # More robust: treat total_energy as a soft gate: if missing, subtract a small penalty.
        final = (main_checks + te_check * 0.1) / (6.0 + 0.1)
        return round(min(1.0, max(0.0, final)), 4)


# === block: score_1 (check id='step_02_excited_state') ===
def score_1(artifact, step, ctx):
    def score(artifact_rows, step, ctx):
        gold = step['gold']
        params = {}
        for row in artifact_rows:
            name = row.get('parameter', '').strip()
            try:
                val = float(row.get('value', ''))
            except:
                continue
            params[name] = val

        checks = []
        if 'a' in params and 'a' in gold.get('a', {}):
            checks.append(1.0 if abs(params['a'] - gold['a']['value']) <= gold['a']['tol'] else 0.0)
        else:
            checks.append(0.0)
        if 'c' in params and 'c' in gold.get('c', {}):
            checks.append(1.0 if abs(params['c'] - gold['c']['value']) <= gold['c']['tol'] else 0.0)
        else:
            checks.append(0.0)
        if 'W-O distance' in params and 'W-O distance' in gold.get('W-O distance', {}):
            checks.append(1.0 if abs(params['W-O distance'] - gold['W-O distance']['value']) <= gold['W-O distance']['tol'] else 0.0)
        else:
            checks.append(0.0)
        if 'angle_alpha' in params and 'angle_alpha' in gold.get('angle_alpha', {}):
            checks.append(1.0 if abs(params['angle_alpha'] - gold['angle_alpha']['value']) <= gold['angle_alpha']['tol'] else 0.0)
        else:
            checks.append(0.0)
        if 'angle_beta' in params and 'angle_beta' in gold.get('angle_beta', {}):
            checks.append(1.0 if abs(params['angle_beta'] - gold['angle_beta']['value']) <= gold['angle_beta']['tol'] else 0.0)
        else:
            checks.append(0.0)
        te_check = 0.0
        if 'total_energy' in params:
            if gold.get('total_energy', {}).get('must_be_negative', False):
                te_check = 1.0 if params['total_energy'] < 0 else 0.0
            else:
                te_check = 1.0
        if 'band_gap' in params and 'band_gap' in gold.get('band_gap', {}):
            checks.append(1.0 if abs(params['band_gap'] - gold['band_gap']['value']) <= gold['band_gap']['tol'] else 0.0)
        else:
            checks.append(0.0)
        main_checks = sum(checks)
        final = (main_checks + te_check * 0.1) / (6.0 + 0.1)
        return round(min(1.0, max(0.0, final)), 4)


# === block: score_2 (check id='step_03_energy_comparison') ===
def score_2(artifact, step, ctx):
    def score(artifact_text, step, ctx):
        gold = step['gold']
        if not artifact_text:
            return 0.0
        lines = artifact_text.strip().split('\n')
        delta_e = None
        is_minimum = None
        for line in lines:
            if line.startswith('Delta_E (eV):'):
                try:
                    delta_e = float(line.split(':', 1)[1].strip())
                except:
                    pass
            elif line.startswith('s_star_is_minimum:'):
                val = line.split(':', 1)[1].strip().lower()
                is_minimum = val == 'true'
        score = 0.0
        count = 0
        if delta_e is not None:
            count += 1
            if abs(delta_e - gold['delta_e']) <= gold.get('delta_e_tol', 0.05):
                score += 1.0
        if is_minimum is not None:
            count += 1
            if is_minimum == gold.get('s_star_is_minimum', True):
                score += 1.0
        if count == 0:
            return 0.0
        return round(score / count, 4)


_SCORERS = {
    'step_01_ground_state': score_0,
    'step_02_excited_state': score_1,
    'step_03_energy_comparison': score_2,
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
