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
        return {}


# === block: score_0 (check id='oscillator_params_scorer') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        rows = artifact
        if not rows or len(rows) < 10:
            return 0.0
        rules = step.get('structural_rules', {})
        trans_e = float(rules.get('transition_energy', -5.444))
        trans_tol = float(rules.get('transition_tolerance', 0.2))
        damp_pre_max = float(rules.get('damping_pre_threshold_max', 0.2))
        ratio_first_min = float(rules.get('ratio_first_row_min', 10.0))
        ratio_last_max = float(rules.get('ratio_last_row_max', 2.0))
        spring_ratio_min = float(rules.get('spring_post_pre_ratio_min', 1.1))

        try:
            data = []
            for row in rows:
                e = float(row['total_energy'])
                l = float(row['damping_coefficient'])
                m = float(row['reduced_mass_ratio'])
                k = float(row['spring_constant'])
                data.append((e, l, m, k))
            data.sort(key=lambda x: x[0])
        except (KeyError, ValueError, TypeError):
            return 0.0

        energies = [d[0] for d in data]
        lambdas = [d[1] for d in data]
        ratios = [d[2] for d in data]
        springs = [d[3] for d in data]
        n = len(data)

        pre_indices = [i for i in range(n) if energies[i] <= trans_e + trans_tol]
        post_indices = [i for i in range(n) if i not in pre_indices]

        # ---- damping behaviour (0.4 weight) ----
        damp_score = 0.0
        damp_ok1 = 0.3  # pre threshold lambda low
        damp_ok2 = 0.3  # post lambda increasing
        damp_ok3 = 0.4  # transition energy matches

        if pre_indices:
            max_pre = max(lambdas[i] for i in pre_indices)
            if max_pre <= damp_pre_max:
                damp_score += damp_ok1

        if len(post_indices) > 1:
            post_lambdas = [lambdas[i] for i in post_indices]
            if all(post_lambdas[i] <= post_lambdas[i+1] for i in range(len(post_lambdas)-1)):
                damp_score += damp_ok2

        trans_found = False
        trans_idx = None
        for i in range(n):
            if lambdas[i] > damp_pre_max:
                trans_idx = i
                break
        if trans_idx is not None:
            detected_e = energies[trans_idx]
            if abs(detected_e - trans_e) <= trans_tol:
                damp_score += damp_ok3

        # ---- reduced mass ratio (0.3 weight) ----
        ratio_score = 0.0
        ratio_ok1 = 0.3
        ratio_ok2 = 0.3
        ratio_ok3 = 0.4
        if ratios[0] >= ratio_first_min:
            ratio_score += ratio_ok1
        if ratios[-1] <= ratio_last_max:
            ratio_score += ratio_ok2
        if post_indices:
            post_ratios = [ratios[i] for i in post_indices]
            if len(post_ratios) > 1:
                if all(post_ratios[i] >= post_ratios[i+1] for i in range(len(post_ratios)-1)):
                    ratio_score += ratio_ok3

        # ---- spring constant (0.3 weight) ----
        spring_score = 0.0
        if pre_indices and post_indices:
            pre_vals = [springs[i] for i in pre_indices]
            post_vals = [springs[i] for i in post_indices]
            pre_avg = sum(pre_vals) / len(pre_vals)
            post_avg = sum(post_vals) / len(post_vals)
            if pre_avg > 0 and post_avg / pre_avg >= spring_ratio_min:
                spring_score += 1.0

        total = 0.4 * damp_score + 0.3 * ratio_score + 0.3 * spring_score
        return max(0.0, min(1.0, total))


_SCORERS = {
    'oscillator_params_scorer': score_0,
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
