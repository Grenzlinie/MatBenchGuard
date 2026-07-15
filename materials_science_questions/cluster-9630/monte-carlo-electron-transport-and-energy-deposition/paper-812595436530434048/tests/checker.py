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
        # Extract gold from grading spec steps
        backscattered_step = next(s for s in spec['steps'] if s['id'] == 'step_backscattered_coeff')
        depth_step = next(s for s in spec['steps'] if s['id'] == 'step_depth_distributions')

        # Backscattered gold
        gold_emax = backscattered_step['gold']
        backscattered_gold = {entry['Emax']: entry['coeff'] for entry in gold_emax}

        # Depth gold parameters
        depth_params = depth_step['gold_params']
        bins = [5.0 + 10.0 * i for i in range(50)]
        depth_gold = {}
        for case in ('uncharged', 'charged'):
            params = depth_params[case]
            peak = params['peak_nm']
            sigma = params['sigma']
            mu = math.log(peak) + sigma ** 2
            y = []
            for d in bins:
                if d <= 0:
                    y.append(0.0)
                else:
                    y.append((1.0 / (d * sigma * math.sqrt(2 * math.pi))) *
                             math.exp(-(math.log(d) - mu) ** 2 / (2 * sigma ** 2)))
            total_raw = sum(y) * 10.0
            scale = params['total_ev'] / total_raw
            total_loss = [v * scale for v in y]
            bethe_loss = [v * params['bethe_fraction'] for v in total_loss]
            electric_loss = [v * params['electric_fraction'] for v in total_loss]
            depth_gold[case] = {
                'bins': bins,
                'total_loss': total_loss,
                'bethe_loss': bethe_loss,
                'electric_loss': electric_loss
            }

        return {
            'backscattered_gold': backscattered_gold,
            'depth_gold': depth_gold,
            'depth_params': depth_params,
            'backscattered_step': backscattered_step
        }


# === block: score_0 (check id='step_backscattered_coeff') ===
def score_0(artifact, step, ctx):
        gold = ctx['backscattered_gold']
        tol = step.get('abs_tol', 0.02)
        mono_w = step.get('monotonic_weight', 0.2)
        expected_emax = sorted(gold.keys())
        observed = {}
        for row in artifact:
            try:
                emax = float(row['Emax'])
                coeff = float(row['backscattered_coefficient'])
                observed[emax] = coeff
            except (ValueError, KeyError, TypeError):
                return 0.0
        if len(observed) != len(expected_emax):
            return 0.0
        for e in expected_emax:
            if e not in observed:
                return 0.0
        # Per-Emax accuracy
        scores = []
        for e in expected_emax:
            obs = observed[e]
            gold_val = gold[e]
            err = abs(obs - gold_val)
            if err <= tol:
                s = 1.0
            else:
                s = max(0.0, 1.0 - (err - tol) / tol)
            scores.append(s)
        accuracy_score = sum(scores) / len(scores)
        # Monotonicity
        sorted_emax = sorted(expected_emax)
        coeff_list = [observed[e] for e in sorted_emax]
        mono = all(coeff_list[i] <= coeff_list[i+1] for i in range(len(coeff_list)-1))
        mono_score = 1.0 if mono else 0.0
        return accuracy_score * (1 - mono_w) + mono_score * mono_w


# === block: score_1 (check id='step_depth_distributions') ===
def score_1(artifact, step, ctx):
        gold_cases = ctx['depth_gold']
        rel_tol = step.get('rel_tol', 0.15)
        if not isinstance(artifact, dict) or 'uncharged' not in artifact or 'charged' not in artifact:
            return 0.0
        for case in ('uncharged', 'charged'):
            data = artifact[case]
            gold = gold_cases[case]
            if data.get('depth_bins') != gold['bins']:
                return 0.0
            for arr_name in ('total_loss', 'bethe_loss', 'electric_loss'):
                if arr_name not in data:
                    return 0.0
                if len(data[arr_name]) != len(gold[arr_name]):
                    return 0.0
        case_scores = []
        for case in ('uncharged', 'charged'):
            gold = gold_cases[case]
            data = artifact[case]
            penalties = []
            for arr_name in ('total_loss', 'bethe_loss', 'electric_loss'):
                gold_arr = gold[arr_name]
                obs_arr = data[arr_name]
                for i, g in enumerate(gold_arr):
                    if g < 1e-12:
                        if abs(obs_arr[i]) < 1e-12:
                            continue
                        else:
                            penalties.append(1.0)
                        continue
                    rel_err = abs(obs_arr[i] - g) / g
                    if rel_err <= rel_tol:
                        continue
                    else:
                        penalty = (rel_err - rel_tol) / (1.0 - rel_tol)
                        penalty = min(1.0, penalty)
                        penalties.append(penalty)
            if penalties:
                mean_penalty = sum(penalties) / len(penalties)
            else:
                mean_penalty = 0.0
            case_scores.append(max(0.0, 1.0 - mean_penalty))
        return 0.5 * case_scores[0] + 0.5 * case_scores[1]


_SCORERS = {
    'step_backscattered_coeff': score_0,
    'step_depth_distributions': score_1,
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
