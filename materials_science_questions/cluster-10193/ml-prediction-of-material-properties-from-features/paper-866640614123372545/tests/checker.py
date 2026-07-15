import os
import json
import csv

# === author imports / helpers ===
import statistics


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


# === block: score_0 (check id='step_03_main_occupied_vs_unoccupied') ===
def score_0(artifact, step, ctx):
    if not artifact or len(artifact) == 0:
        return 0.0
    occupied = []
    unoccupied = []
    for row in artifact:
        try:
            oc = float(row['MSE_occupied'])
            un = float(row['MSE_unoccupied'])
            occupied.append(oc)
            unoccupied.append(un)
        except (ValueError, KeyError):
            pass
    if len(occupied) == 0:
        return 0.0
    med_occ = statistics.median(occupied)
    med_uno = statistics.median(unoccupied)
    return 1.0 if med_occ > med_uno else 0.0


# === block: score_1 (check id='step_05_extrapolation_brown_better_blue') ===
def score_1(artifact, step, ctx):
    green_20 = None
    brown_18 = None
    for row in artifact:
        try:
            n = int(row['n'])
        except (ValueError, KeyError):
            continue
        model = str(row.get('model_type', '')).strip().lower()
        try:
            mse = float(row['MSE'])
        except (ValueError, KeyError):
            continue
        if model == 'green' and n == 20:
            green_20 = mse
        elif model == 'brown' and n == 18:
            brown_18 = mse
    if green_20 is not None and brown_18 is not None:
        return 1.0 if brown_18 < green_20 else 0.0
    return 0.0


# === block: score_2 (check id='step_07_noise_matching') ===
def score_2(artifact, step, ctx):
    if not artifact:
        return 0.0
    groups = {}
    for row in artifact:
        try:
            tla = float(row['test_lambda'])
            sm = str(row['smoothing_width']).strip()
            tr = float(row['train_lambda'])
            mse = float(row['MSE'])
        except (ValueError, KeyError):
            continue
        groups.setdefault(tla, {}).setdefault(sm, {})[tr] = mse
    test_lambdas = sorted(groups.keys())
    if not test_lambdas:
        return 0.0
    total = 0
    passed = 0
    for tla in test_lambdas:
        unsm_d = groups[tla].get('none')
        if not unsm_d:
            continue
        opt_unsm = min(unsm_d.items(), key=lambda x: x[1])[0]
        if abs(opt_unsm - tla) < 1e-6:
            passed += 1
        total += 1
        for sm in ('0.3', '0.5'):
            sm_d = groups[tla].get(sm)
            if sm_d:
                opt_sm = min(sm_d.items(), key=lambda x: x[1])[0]
                if opt_sm >= opt_unsm - 1e-6:
                    passed += 1
                total += 1
    if total == 0:
        return 0.0
    return passed / total


# === block: score_3 (check id='step_09_augmentation_matched_better') ===
def score_3(artifact, step, ctx):
    if not artifact:
        return 0.0
    matched = {}
    aug = {}
    for row in artifact:
        try:
            lam = float(row['lambda'])
            meth = str(row['method']).strip()
            mse = float(row['MSE'])
        except (ValueError, KeyError):
            continue
        if meth == 'matched':
            matched[lam] = mse
        elif meth == 'augmentation':
            aug[lam] = mse
    common = set(matched) & set(aug)
    if not common:
        return 0.0
    passed = sum(1 for lam in common if matched[lam] < aug[lam])
    return passed / len(common)


_SCORERS = {
    'step_03_main_occupied_vs_unoccupied': score_0,
    'step_05_extrapolation_brown_better_blue': score_1,
    'step_07_noise_matching': score_2,
    'step_09_augmentation_matched_better': score_3,
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
