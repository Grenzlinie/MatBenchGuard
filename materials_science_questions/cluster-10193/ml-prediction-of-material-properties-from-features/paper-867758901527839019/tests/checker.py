import os
import json
import csv

# === author imports / helpers ===
import csv, json, os, math
from collections import defaultdict

def compute_metrics(predictions):
    total = len(predictions)
    if total == 0:
        return {"overall_site_accuracy": 0.0, "compound_level_accuracy": 0.0, "per_element": {}}
    correct_sites = 0
    comp_sites = defaultdict(lambda: {"total": 0, "correct": 0})
    elem_sites = defaultdict(lambda: {"total": 0, "correct": 0})
    for row in predictions:
        true_os = int(row["true_oxidation_state"])
        pred_os = int(row["predicted_oxidation_state"])
        correct = 1 if true_os == pred_os else 0
        correct_sites += correct
        comp = row["composition"]
        elem = row["element"]
        comp_sites[comp]["total"] += 1
        comp_sites[comp]["correct"] += correct
        elem_sites[elem]["total"] += 1
        elem_sites[elem]["correct"] += correct
    overall = (correct_sites / total) * 100.0
    comp_correct = sum(1 for comp in comp_sites if comp_sites[comp]["correct"] == comp_sites[comp]["total"])
    compound = (comp_correct / len(comp_sites)) * 100.0 if len(comp_sites) > 0 else 0.0
    per_elem = {elem: (v["correct"] / v["total"]) * 100.0 for elem, v in elem_sites.items()}
    return {"overall_site_accuracy": overall, "compound_level_accuracy": compound, "per_element": per_elem}


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


# === block: score_0 (check id='os_icsd_predictions_overall') ===
def score_0(artifact, step, ctx):
    metrics = compute_metrics(artifact)
    overall = metrics["overall_site_accuracy"]
    gold = step["gold_site_accuracy"]
    tol = step.get("tolerance_fp_floor", 0.5)
    threshold = gold - tol
    if overall >= threshold:
        score = 1.0
    else:
        threshold = max(threshold, 1e-9)
        score = min(1.0, overall / threshold)
    return score


# === block: score_1 (check id='os_icsd_predictions_compound') ===
def score_1(artifact, step, ctx):
    metrics = compute_metrics(artifact)
    comp = metrics["compound_level_accuracy"]
    min_acc = step.get("min_compound_accuracy", 85.0)
    if comp >= min_acc:
        score = 1.0
    else:
        score = max(0.0, comp / min_acc)
    return score


# === block: score_2 (check id='os_icsd_predictions_per_element') ===
def score_2(artifact, step, ctx):
    metrics = compute_metrics(artifact)
    per_elem = metrics.get("per_element", {})
    if not isinstance(per_elem, dict) or len(per_elem) == 0:
        return 0.0
    per_element_gold = step.get("per_element_gold", {})
    if not per_element_gold:
        return 0.0
    tol = step.get("per_element_tolerance", 2.0)
    scores = []
    for elem, gold_val in per_element_gold.items():
        agent_val = per_elem.get(elem)
        if agent_val is None:
            scores.append(0.0)
            continue
        threshold = gold_val - tol
        if agent_val >= threshold:
            scores.append(1.0)
        else:
            scores.append(max(0.0, agent_val / threshold if threshold > 0 else 0.0))
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_3 (check id='os_icsd_metrics_struct') ===
def score_3(artifact, step, ctx):
    required_keys = ["overall_site_accuracy", "compound_level_accuracy", "per_element_site_accuracy"]
    if not isinstance(artifact, dict):
        return 0.0
    for key in required_keys:
        if key not in artifact:
            return 0.0
    site_acc = artifact["overall_site_accuracy"]
    comp_acc = artifact["compound_level_accuracy"]
    per = artifact["per_element_site_accuracy"]
    if not isinstance(site_acc, (int, float)) or not (0 <= site_acc <= 100):
        return 0.0
    if not isinstance(comp_acc, (int, float)) or not (0 <= comp_acc <= 100):
        return 0.0
    if not isinstance(per, dict) or len(per) == 0:
        return 0.0
    for elem, val in per.items():
        if not isinstance(val, (int, float)) or not (0 <= val <= 100):
            return 0.0
    return 1.0


# === block: score_4 (check id='os_icsd_oxide_predictions_overall') ===
def score_4(artifact, step, ctx):
    metrics = compute_metrics(artifact)
    overall = metrics["overall_site_accuracy"]
    gold = step["gold_site_accuracy"]
    tol = step.get("tolerance_fp_floor", 0.5)
    threshold = gold - tol
    if overall >= threshold:
        score = 1.0
    else:
        threshold = max(threshold, 1e-9)
        score = min(1.0, overall / threshold)
    return score


# === block: score_5 (check id='os_icsd_oxide_predictions_compound') ===
def score_5(artifact, step, ctx):
    metrics = compute_metrics(artifact)
    comp = metrics["compound_level_accuracy"]
    min_acc = step.get("min_compound_accuracy", 85.0)
    if comp >= min_acc:
        score = 1.0
    else:
        score = max(0.0, comp / min_acc)
    return score


# === block: score_6 (check id='os_icsd_oxide_metrics_struct') ===
def score_6(artifact, step, ctx):
    required_keys = ["overall_site_accuracy", "compound_level_accuracy", "per_element_site_accuracy"]
    if not isinstance(artifact, dict):
        return 0.0
    for key in required_keys:
        if key not in artifact:
            return 0.0
    site_acc = artifact["overall_site_accuracy"]
    comp_acc = artifact["compound_level_accuracy"]
    per = artifact["per_element_site_accuracy"]
    if not isinstance(site_acc, (int, float)) or not (0 <= site_acc <= 100):
        return 0.0
    if not isinstance(comp_acc, (int, float)) or not (0 <= comp_acc <= 100):
        return 0.0
    if not isinstance(per, dict) or len(per) == 0:
        return 0.0
    for elem, val in per.items():
        if not isinstance(val, (int, float)) or not (0 <= val <= 100):
            return 0.0
    return 1.0


_SCORERS = {
    'os_icsd_predictions_overall': score_0,
    'os_icsd_predictions_compound': score_1,
    'os_icsd_predictions_per_element': score_2,
    'os_icsd_metrics_struct': score_3,
    'os_icsd_oxide_predictions_overall': score_4,
    'os_icsd_oxide_predictions_compound': score_5,
    'os_icsd_oxide_metrics_struct': score_6,
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
