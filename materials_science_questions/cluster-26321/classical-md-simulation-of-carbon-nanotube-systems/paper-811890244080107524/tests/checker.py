import os
import json
import csv

# === author imports / helpers ===
import math, csv


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


# === block: score_0 (check id='simulation_results') ===
def score_0(artifact, step, ctx):
    gold = step['gold']
    tol = gold['tolerance_relative']
    col_map = {
        'ekin_max': 'EKIN_kcal_per_mol',
        'epot_max': 'EPOT_kcal_per_mol',
        'etot_max': 'ETOT_kcal_per_mol',
        'temp_max': 'TEMP_K'
    }
    scores = {}
    for key, col in col_map.items():
        try:
            series = [float(row[col]) for row in artifact]
        except (KeyError, ValueError):
            scores[key] = 0.0
        else:
            val_max = max(series)
            gold_val = gold[key]
            diff = abs(val_max - gold_val)
            if diff <= gold_val * tol:
                scores[key] = 1.0
            else:
                scores[key] = 0.0
    # structural checks
    # molar specific heat: initial peak and asymptotic constant
    try:
        spheat = [float(row['molar_specific_heat_kcal_per_mol_K']) for row in artifact]
        if len(spheat) > 200:
            initial_avg = sum(spheat[:10]) / 10
            final_avg = sum(spheat[200:]) / (len(spheat) - 200)
            if initial_avg > 5 * final_avg:
                scores['specific_heat_peak'] = 1.0
            else:
                scores['specific_heat_peak'] = 0.0
        else:
            scores['specific_heat_peak'] = 0.0
    except (KeyError, ValueError):
        scores['specific_heat_peak'] = 0.0
    # entropy-efficiency inverse relationship (Pearson r without numpy)
    try:
        entropy = [float(row['molar_entropy_variation_kcal_per_mol_K']) for row in artifact]
        efficiency = [float(row['efficiency']) for row in artifact]
        n = len(entropy)
        if n > 1:
            # compute means
            mean_e = sum(entropy) / n
            mean_ef = sum(efficiency) / n
            # compute std
            var_e = sum((x - mean_e) ** 2 for x in entropy)
            var_ef = sum((x - mean_ef) ** 2 for x in efficiency)
            if var_e > 0 and var_ef > 0:
                cov = sum((entropy[i] - mean_e) * (efficiency[i] - mean_ef) for i in range(n))
                corr = cov / ((var_e ** 0.5) * (var_ef ** 0.5))
                if corr < -0.5:
                    scores['entropy_eff_corr'] = 1.0
                else:
                    scores['entropy_eff_corr'] = 0.0
            else:
                scores['entropy_eff_corr'] = 0.0
        else:
            scores['entropy_eff_corr'] = 0.0
    except (KeyError, ValueError):
        scores['entropy_eff_corr'] = 0.0
    # combine sub-scores
    total = (0.15 * scores['ekin_max'] + 0.15 * scores['epot_max'] + 0.15 * scores['etot_max'] + 0.15 * scores['temp_max'] + 0.2 * scores['specific_heat_peak'] + 0.2 * scores['entropy_eff_corr'])
    return max(0.0, min(1.0, total))


_SCORERS = {
    'simulation_results': score_0,
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
