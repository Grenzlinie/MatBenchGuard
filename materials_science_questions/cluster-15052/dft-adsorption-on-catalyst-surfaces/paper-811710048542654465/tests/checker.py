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


# === block: score_0 (check id='step_5') ===
def score_0(artifact, step, ctx):
    try:
        data = artifact
        E_O2 = float(data["E_O2"])
        E_reduced = float(data["E_reduced"])
        E_bare = float(data["E_bare"])
        E_atomic_O = float(data["E_atomic_O"])
        configs = data.get("configurations", {})
        most_stable = data.get("most_stable", "")
    except (KeyError, ValueError, TypeError):
        return 0.0

    refs = step.get("reference_E_ads_per_O2", {})
    tol_ads = float(step.get("tolerance_abs_ads", 0.2))
    ref_atomic = float(step.get("reference_E_ads_atomic_O", -2.11))
    tol_atomic = float(step.get("tolerance_abs_atomic", 0.2))
    expected_most_stable = "3e"

    ads_scores = []
    all_recomputed = {}
    for k in refs:
        conf = configs.get(k)
        if conf is None:
            ads_scores.append(0.0)
            continue
        E_total = float(conf.get("E_total", None))
        if E_total is None:
            ads_scores.append(0.0)
            continue
        E_ads_recomputed = E_total - E_reduced - E_O2
        all_recomputed[k] = E_ads_recomputed
        diff = abs(E_ads_recomputed - refs[k])
        ads_scores.append(1.0 if diff <= tol_ads else 0.0)

    ads_score = sum(ads_scores) / len(ads_scores) if ads_scores else 0.0

    stable_score = 0.0
    if most_stable == expected_most_stable:
        if all_recomputed:
            lowest = min(all_recomputed.values())
            if abs(all_recomputed.get(expected_most_stable, 0.0) - lowest) < 1e-6:
                stable_score = 1.0
            else:
                stable_score = 0.5
        else:
            stable_score = 0.5

    E_total_3e = float(configs.get("3e", {}).get("E_total", None))
    if E_total_3e is not None:
        E_ads_atomic_recomputed = E_total_3e - E_bare - E_atomic_O
        atomic_score = 1.0 if abs(E_ads_atomic_recomputed - ref_atomic) <= tol_atomic else 0.0
    else:
        atomic_score = 0.0

    w_ads = 0.7
    w_stable = 0.2
    w_atomic = 0.1
    return w_ads * ads_score + w_stable * stable_score + w_atomic * atomic_score


# === block: score_1 (check id='step_6') ===
def score_1(artifact, step, ctx):
    try:
        bond_len = float(str(artifact).strip())
    except (ValueError, TypeError):
        return 0.0
    ref = float(step.get("reference_bond", 1.50))
    tol = float(step.get("tolerance_abs", 0.1))
    return 1.0 if abs(bond_len - ref) <= tol else 0.0


_SCORERS = {
    'step_5': score_0,
    'step_6': score_1,
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
