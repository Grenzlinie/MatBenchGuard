import os
import json
import csv

# === author imports / helpers ===
import json
from typing import Any, List, Optional

def _get_nested(data: Any, keys: List[str]) -> Optional[Any]:
    for k in keys:
        if not isinstance(data, dict):
            return None
        data = data.get(k)
    return data

def compare_row(artifact: dict, step: dict) -> float:
    row_key = step['config']['row_key']
    expected = step['config']['expected']
    tolerances = step['config']['tolerances']
    row_data = _get_nested(artifact, row_key)
    if not isinstance(row_data, dict):
        return 0.0
    fields = ['Elatt', 'Eform', 'Volume', 'HS_area', 'Elatt_HS_ratio']
    scores = []
    for f in fields:
        actual = row_data.get(f)
        exp = expected.get(f)
        tol = tolerances.get(f, 0.0)
        if actual is None or exp is None:
            scores.append(0.0)
        else:
            diff = abs(actual - exp)
            if diff <= tol:
                scores.append(1.0)
            else:
                # partial credit decays beyond tolerance
                scores.append(max(0.0, 1.0 - (diff - tol) / tol))
    return sum(scores) / len(scores) if scores else 0.0

def check_self_consistency(artifact: dict, step: dict) -> float:
    row_key = step['config']['row_key']
    tol = step['config']['tol']
    row_data = _get_nested(artifact, row_key)
    if not row_data:
        return 0.0
    elatt = row_data.get('Elatt')
    hs = row_data.get('HS_area')
    ratio = row_data.get('Elatt_HS_ratio')
    if None in (elatt, hs, ratio):
        return 0.0
    try:
        computed = elatt / hs
    except ZeroDivisionError:
        return 0.0
    return 1.0 if abs(computed - ratio) <= tol else 0.0

def check_trend(artifact: dict, step: dict) -> float:
    val1 = _get_nested(artifact, step['config']['path1'])
    val2 = _get_nested(artifact, step['config']['path2'])
    op = step['config']['operator']
    if None in (val1, val2):
        return 0.0
    if op == '>':
        return 1.0 if val1 > val2 else 0.0
    elif op == '<':
        return 1.0 if val1 < val2 else 0.0
    else:
        return 0.0


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


# === block: score_0 (check id='1Si_exp') ===
def score_0(artifact, step, ctx):
    import os, json
    artifact_key = step['config']['row_key']
    # Attempt to verify from raw evidence
    try:
        raw_path = os.path.join(ctx.get('outputs_dir', '/app/outputs'), 'dft_raw.json')
        with open(raw_path) as f:
            raw = json.load(f)
        # raw must contain '1Si' with 'crystal_energy_exp' and 'isolated_energy_exp' (in Hartree?)
        exp_raw = raw.get('1Si', {}).get('exp')
        if exp_raw and 'crystal_energy' in exp_raw and 'isolated_energy' in exp_raw:
            # Compute Elatt (as paper defines: E(crystal) - E(isolated), then invert?)
            # Assume raw energies are in Hartree; paper uses positive kcal/mol, so we convert
            # E_latt = -(crystal - isolated) * 627.5095 (kcal/mol per Hartree)
            hartree_to_kcal = 627.5095
            crystal = float(exp_raw['crystal_energy'])
            isolated = float(exp_raw['isolated_energy'])
            computed_elatt = -(crystal - isolated) * hartree_to_kcal
            # Compare to reported Elatt in artifact
            reported = _get_nested(artifact, artifact_key).get('Elatt')
            if reported is not None and abs(computed_elatt - reported) < 0.2:
                # Raw evidence consistent; proceed with standard compare
                pass
            else:
                # Raw evidence inconsistent; this scorer gives zero
                return 0.0
    except Exception:
        pass
    # Fallback: original compare (for oracle which lacks raw evidence)
    return compare_row(artifact, step)


# === block: score_1 (check id='1Si_DFT') ===
def score_1(artifact, step, ctx):
    return compare_row(artifact, step)


# === block: score_2 (check id='1Si_in_1C') ===
def score_2(artifact, step, ctx):
    return compare_row(artifact, step)


# === block: score_3 (check id='1C_exp') ===
def score_3(artifact, step, ctx):
    return compare_row(artifact, step)


# === block: score_4 (check id='1C_DFT') ===
def score_4(artifact, step, ctx):
    return compare_row(artifact, step)


# === block: score_5 (check id='1C_in_1Si') ===
def score_5(artifact, step, ctx):
    return compare_row(artifact, step)


# === block: score_6 (check id='self_1Si_exp') ===
def score_6(artifact, step, ctx):
    return check_self_consistency(artifact, step)


# === block: score_7 (check id='self_1Si_DFT') ===
def score_7(artifact, step, ctx):
    return check_self_consistency(artifact, step)


# === block: score_8 (check id='self_1Si_in_1C') ===
def score_8(artifact, step, ctx):
    return check_self_consistency(artifact, step)


# === block: score_9 (check id='self_1C_exp') ===
def score_9(artifact, step, ctx):
    return check_self_consistency(artifact, step)


# === block: score_10 (check id='self_1C_DFT') ===
def score_10(artifact, step, ctx):
    return check_self_consistency(artifact, step)


# === block: score_11 (check id='self_1C_in_1Si') ===
def score_11(artifact, step, ctx):
    return check_self_consistency(artifact, step)


# === block: score_12 (check id='trend_Elatt_1Si_gt_1C_exp') ===
def score_12(artifact, step, ctx):
    return check_trend(artifact, step)


# === block: score_13 (check id='trend_Elatt_1Si_gt_1C_DFT') ===
def score_13(artifact, step, ctx):
    return check_trend(artifact, step)


# === block: score_14 (check id='trend_1Si_swap_less_stable_exp') ===
def score_14(artifact, step, ctx):
    return check_trend(artifact, step)


# === block: score_15 (check id='trend_1C_swap_less_stable_exp') ===
def score_15(artifact, step, ctx):
    return check_trend(artifact, step)


# === block: score_16 (check id='trend_Elatt_1Si_swapped_gt_1C_swapped') ===
def score_16(artifact, step, ctx):
    return check_trend(artifact, step)


_SCORERS = {
    '1Si_exp': score_0,
    '1Si_DFT': score_1,
    '1Si_in_1C': score_2,
    '1C_exp': score_3,
    '1C_DFT': score_4,
    '1C_in_1Si': score_5,
    'self_1Si_exp': score_6,
    'self_1Si_DFT': score_7,
    'self_1Si_in_1C': score_8,
    'self_1C_exp': score_9,
    'self_1C_DFT': score_10,
    'self_1C_in_1Si': score_11,
    'trend_Elatt_1Si_gt_1C_exp': score_12,
    'trend_Elatt_1Si_gt_1C_DFT': score_13,
    'trend_1Si_swap_less_stable_exp': score_14,
    'trend_1C_swap_less_stable_exp': score_15,
    'trend_Elatt_1Si_swapped_gt_1C_swapped': score_16,
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
