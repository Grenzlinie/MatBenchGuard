import os
import json
import csv

# === author imports / helpers ===
import math
import csv
import io


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


# === block: score_0 (check id='occupancies_check') ===
def score_0(artifact, step, ctx):
    artifact_data = artifact
    required_cols = ["param_set", "n_d", "n_p_h", "n_p_n"]
    if not artifact_data or not all(col in artifact_data[0] for col in required_cols):
        return 0.0
    gold_rows = {r["param_set"]: r for r in step["config"]["gold_rows"]}
    tol = step["config"]["tolerance"]
    total = 0.0
    count = 0
    for row in artifact_data:
        ps = row.get("param_set", "")
        if ps in gold_rows:
            gold = gold_rows[ps]
            nd = float(row["n_d"])
            nph = float(row["n_p_h"])
            npn = float(row["n_p_n"])
            gnd = float(gold["n_d"])
            g_total2p = float(gold["n_p_h"]) + float(gold["n_p_n"])
            if abs(nd - gnd) <= tol and abs((nph + npn) - g_total2p) <= tol:
                total += 1.0
            count += 1
    if count == 0:
        return 0.0
    return total / count


# === block: score_1 (check id='eigenvalues_check') ===
def score_1(artifact, step, ctx):
    artifact_data = artifact
    required_cols = ["T_over_tpd", "lambda_d", "lambda_sstar"]
    if not artifact_data or not all(col in artifact_data[0] for col in required_cols):
        return 0.0
    gold_rows = {r["T_over_tpd"]: r for r in step["config"]["gold_rows"]}
    tol = step["config"]["tolerance"]
    count = 0
    total_val_score = 0.0
    total_order_score = 0.0
    for row in artifact_data:
        try:
            T = float(row.get("T_over_tpd", -1))
        except (ValueError, TypeError):
            continue
        if T in gold_rows:
            gold = gold_rows[T]
            ld = float(row["lambda_d"])
            ls = float(row["lambda_sstar"])
            gld = float(gold["lambda_d"])
            gls = float(gold["lambda_sstar"])
            v1 = 1.0 if abs(ld - gld) <= tol else 0.0
            v2 = 1.0 if abs(ls - gls) <= tol else 0.0
            val_score = (v1 + v2) / 2.0
            order_score = 1.0 if ld > ls else 0.0
            total_val_score += val_score
            total_order_score += order_score
            count += 1
    if count == 0:
        return 0.0
    avg_val = total_val_score / count
    avg_order = total_order_score / count
    return 0.5 * avg_val + 0.5 * avg_order


# === block: score_2 (check id='tn_check') ===
def score_2(artifact, step, ctx):
    artifact_data = artifact
    required_cols = ["Ud_over_tpd", "TN_over_tpd"]
    if not artifact_data or not all(col in artifact_data[0] for col in required_cols):
        return 0.0
    gold_rows = {r["Ud_over_tpd"]: r for r in step["config"]["gold_rows"]}
    tol = step["config"]["tolerance"]
    count = 0
    total_score = 0.0
    for row in artifact_data:
        try:
            Ud = float(row.get("Ud_over_tpd", -1))
        except (ValueError, TypeError):
            continue
        if Ud in gold_rows:
            gold = gold_rows[Ud]
            TN = float(row["TN_over_tpd"])
            gTN = float(gold["TN_over_tpd"])
            dist = abs(TN - gTN)
            if dist <= tol:
                total_score += 1.0
            else:
                total_score += max(0.0, 1.0 - dist / tol)
            count += 1
    if count == 0:
        return 0.0
    return total_score / count


_SCORERS = {
    'occupancies_check': score_0,
    'eigenvalues_check': score_1,
    'tn_check': score_2,
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
