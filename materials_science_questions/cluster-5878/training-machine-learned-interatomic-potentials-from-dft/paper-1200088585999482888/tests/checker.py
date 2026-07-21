import os
import json
import csv

# === author imports / helpers ===
import math
import collections
import itertools

def _choose2(n):
    return n * (n - 1) / 2.0

def adjusted_rand_index(labels_true, labels_pred):
    """Compute Adjusted Rand Index, pure Python."""
    labels_true = list(labels_true)
    labels_pred = list(labels_pred)
    if len(labels_true) != len(labels_pred):
        return 0.0
    n = len(labels_true)
    if n < 2:
        return 0.0
    # contingency table as dict of (class_true, class_pred) -> count
    contingency = collections.defaultdict(int)
    for t, p in zip(labels_true, labels_pred):
        contingency[(t, p)] += 1
    classes_true = list(set(labels_true))
    classes_pred = list(set(labels_pred))
    # row sums (true) and column sums (pred)
    true_counts = [sum(contingency[(t, p)] for p in classes_pred) for t in classes_true]
    pred_counts = [sum(contingency[(t, p)] for t in classes_true) for p in classes_pred]
    sum_comb_c = sum(_choose2(contingency[(t, p)]) for t in classes_true for p in classes_pred)
    sum_comb_true = sum(_choose2(c) for c in true_counts)
    sum_comb_pred = sum(_choose2(c) for c in pred_counts)
    expected_index = sum_comb_true * sum_comb_pred / _choose2(n)
    max_index = 0.5 * (sum_comb_true + sum_comb_pred)
    if max_index == expected_index:
        return 0.0
    return (sum_comb_c - expected_index) / (max_index - expected_index)


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
    # extract step configs from spec for easy lookup in scorers
    step_map = {s['id']: s for s in spec.get('steps', [])}
    return {'step_map': step_map}


# === block: score_0 (check id='test_predictions_mae') ===
def score_0(artifact, step, ctx):
    step_cfg = ctx['step_map'].get('test_predictions_mae', {})
    required_methods = step_cfg.get('required_methods', [])
    threshold = step_cfg.get('threshold', 0.10)
    max_mae = step_cfg.get('max_mae', 0.50)
    gold = step_cfg.get('gold', {})  # dict mapping (dimer_id, method) -> true_delta_energy
    if not artifact or not required_methods:
        return 0.0

    method_errors = collections.defaultdict(list)
    cheat_candidates = collections.defaultdict(list)  # store absolute differences for cheat check

    if gold:
        # Use hidden gold
        for row in artifact:
            dimer_id = row.get('dimer_id', '').strip()
            method = row.get('method', '').strip()
            try:
                pred = float(row['predicted_delta_energy'])
            except (KeyError, ValueError):
                continue
            true_val = gold.get((dimer_id, method))
            if true_val is None:
                continue
            method_errors[method].append(abs(pred - true_val))
    else:
        # Fallback: use agent-reported true_delta_energy column, with anti‑cheat
        for row in artifact:
            method = row.get('method', '').strip()
            try:
                pred = float(row['predicted_delta_energy'])
                true_val = float(row['true_delta_energy'])
            except (KeyError, ValueError):
                continue
            method_errors[method].append(abs(pred - true_val))
            cheat_candidates[method].append(abs(pred - true_val))

        # Cheat detection: if for EVERY method with at least 1 row, all abs differences are
        # effectively zero (predicted == true), the submission is trivially copied.
        all_cheat = True
        for method, diffs in cheat_candidates.items():
            if diffs and any(d > 1e-8 for d in diffs):
                all_cheat = False
                break
        if all_cheat and cheat_candidates:
            return 0.0

    per_method_scores = []
    for method in required_methods:
        errors = method_errors.get(method, [])
        if not errors:
            per_method_scores.append(0.0)
            continue
        mae = sum(errors) / len(errors)
        if mae <= threshold:
            per_method_scores.append(1.0)
        elif mae >= max_mae:
            per_method_scores.append(0.0)
        else:
            # linear decay: 1.0 at threshold, 0.0 at max_mae
            frac = (mae - threshold) / (max_mae - threshold)
            per_method_scores.append(1.0 - frac)

    if not per_method_scores:
        return 0.0
    return sum(per_method_scores) / len(per_method_scores)


# === block: score_1 (check id='method_clusters_ari') ===
def score_1(artifact, step, ctx):
    step_cfg = ctx['step_map'].get('method_clusters_ari', {})
    gold_map = step_cfg.get('gold', {})
    if not gold_map or not artifact:
        return 0.0
    # build lists aligned by method order
    methods_sorted = sorted(gold_map.keys())
    # map submitted method -> label
    submitted_map = {}
    for row in artifact:
        method = row.get('method', '').strip()
        try:
            label = int(row['cluster_label'])
            submitted_map[method] = label
        except (KeyError, ValueError):
            continue

    true_labels = []
    pred_labels = []
    for m in methods_sorted:
        if m in submitted_map:
            true_labels.append(gold_map[m])
            pred_labels.append(submitted_map[m])
        else:
            # missing method -> penalise
            true_labels.append(gold_map[m])
            pred_labels.append(999)  # dummy label

    if len(true_labels) < 2:
        return 0.0

    ari = adjusted_rand_index(true_labels, pred_labels)
    # full credit at ARI >= 0.8, scale linearly down to 0
    score = min(1.0, max(0.0, ari / 0.8))
    return score


_SCORERS = {
    'test_predictions_mae': score_0,
    'method_clusters_ari': score_1,
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
