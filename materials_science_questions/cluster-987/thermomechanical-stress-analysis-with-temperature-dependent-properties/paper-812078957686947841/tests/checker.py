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
    return {}


# === block: score_0 (check id='thermo_main') ===
def score_0(artifact, step, ctx):
    import math

    gold = step.get('gold', {})
    reported = artifact

    def _check_arrays(rep_list, gold_list, tol):
        scores = []
        for r, g in zip(rep_list, gold_list):
            error = abs(r - g)
            if error <= tol:
                score = 1.0 - error / tol
            else:
                score = 0.0
            scores.append(score)
        return scores

    all_scores = []

    try:
        r2 = reported.get('reaction_2', {})
        g2 = gold.get('reaction_2', {})
        if r2:
            delta_g = r2.get('delta_G_kcal_per_mol', [])
            logk = r2.get('log_K', [])
            g_dg = g2.get('delta_G_kcal_per_mol', [])
            g_logk = g2.get('log_K', [])
            if len(delta_g) == len(g_dg) and len(delta_g) > 0:
                all_scores.extend(_check_arrays(delta_g, g_dg, 2.0))
            if len(logk) == len(g_logk) and len(logk) > 0:
                all_scores.extend(_check_arrays(logk, g_logk, 0.2))

        r3 = reported.get('reaction_3', {})
        g3 = gold.get('reaction_3', {})
        if r3:
            delta_g = r3.get('delta_G_kcal_per_mol', [])
            logk = r3.get('log_K', [])
            g_dg = g3.get('delta_G_kcal_per_mol', [])
            g_logk = g3.get('log_K', [])
            if len(delta_g) == len(g_dg) and len(delta_g) > 0:
                all_scores.extend(_check_arrays(delta_g, g_dg, 2.0))
            if len(logk) == len(g_logk) and len(logk) > 0:
                all_scores.extend(_check_arrays(logk, g_logk, 0.2))

        equil = reported.get('equilibrium_partial_pressures_at_1650C', {})
        g_equil = gold.get('equilibrium_partial_pressures_at_1650C', {})
        for env in ['air', 'He']:
            rep_env = equil.get(env, {})
            gold_env = g_equil.get(env, {})
            for sp in ['P_SiO', 'P_SiO2']:
                rep_val = rep_env.get(f'{sp}_atm', None)
                gold_log = gold_env.get(f'{sp}_log10', None)
                if rep_val is not None and gold_log is not None:
                    if rep_val <= 0:
                        all_scores.append(0.0)
                    else:
                        rep_log = math.log10(rep_val)
                        error = abs(rep_log - gold_log)
                        tol = 0.2
                        if error <= tol:
                            all_scores.append(1.0 - error / tol)
                        else:
                            all_scores.append(0.0)

        if all_scores:
            score = sum(all_scores) / len(all_scores)
        else:
            score = 0.0
        return score
    except Exception as e:
        return 0.0


_SCORERS = {
    'thermo_main': score_0,
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
