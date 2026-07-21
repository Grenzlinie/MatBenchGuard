import os
import json
import csv

# === author imports / helpers ===
import csv, os, math

def compare_sif_table(rows_agent, gold_rows, key_cols, sif_cols, tolerance):
    agent_entries = []
    for row in rows_agent:
        try:
            key = []
            for c in key_cols:
                val = row[c]
                try:
                    key.append(float(val))
                except (ValueError, TypeError):
                    key.append(str(val))
            agent_entries.append((tuple(key), row))
        except Exception:
            continue
    if not gold_rows:
        return 0.0
    matched = 0
    for gold in gold_rows:
        try:
            gold_key = []
            for c in key_cols:
                val = gold[c]
                try:
                    gold_key.append(float(val))
                except (ValueError, TypeError):
                    gold_key.append(str(val))
            gold_key = tuple(gold_key)
        except Exception:
            continue
        best_row = None
        for agent_key, agent_row in agent_entries:
            if len(agent_key) != len(gold_key):
                continue
            ok = True
            for a, g in zip(agent_key, gold_key):
                if isinstance(g, float) and isinstance(a, float):
                    if abs(a - g) > 1e-6:
                        ok = False
                        break
                else:
                    if str(a) != str(g):
                        ok = False
                        break
            if ok:
                best_row = agent_row
                break
        if best_row is None:
            continue
        row_ok = True
        for c in sif_cols:
            try:
                val = float(best_row.get(c, None))
                gold_val = float(gold[c])
            except (ValueError, TypeError, KeyError):
                row_ok = False
                break
            if gold_val == 0.0:
                if abs(val) > tolerance:
                    row_ok = False
                    break
            else:
                if abs(val - gold_val) / abs(gold_val) > tolerance:
                    row_ok = False
                    break
        if row_ok:
            matched += 1
    return matched / len(gold_rows)


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


# === block: score_0 (check id='table_1_2_check') ===
def score_0(artifact, step, ctx):
    rows = artifact if isinstance(artifact, list) else []
    key_cols = step.get("gold_key_columns", ["R1_over_R2_minus_R1"])
    sif_cols = step.get("gold_sif_columns", ["ki_k0_modeI", "ko_k0_modeI", "ki_k0_modeII", "ko_k0_modeII"])
    tol = step.get("tolerance", 0.001)
    # corrected gold rows: removed R1_over_R2_minus_R1=5.0 because Table 1 does not provide Mode I values for that ratio
    corrected_gold_rows = [
        {"R1_over_R2_minus_R1": 0.05, "ki_k0_modeI": 1.1477, "ko_k0_modeI": 1.2046, "ki_k0_modeII": 1.1024, "ko_k0_modeII": 1.1403},
        {"R1_over_R2_minus_R1": 0.1,  "ki_k0_modeI": 1.1498, "ko_k0_modeI": 1.2030, "ki_k0_modeII": 1.1130, "ko_k0_modeII": 1.1439},
        {"R1_over_R2_minus_R1": 0.25, "ki_k0_modeI": 1.1580, "ko_k0_modeI": 1.2018, "ki_k0_modeII": 1.1437, "ko_k0_modeII": 1.1581},
        {"R1_over_R2_minus_R1": 0.5,  "ki_k0_modeI": 1.1664, "ko_k0_modeI": 1.2007, "ki_k0_modeII": 1.1730, "ko_k0_modeII": 1.1753},
        {"R1_over_R2_minus_R1": 1.0,  "ki_k0_modeI": 1.1736, "ko_k0_modeI": 1.1980, "ki_k0_modeII": 1.1931, "ko_k0_modeII": 1.1903},
        {"R1_over_R2_minus_R1": 2.0,  "ki_k0_modeI": 1.1788, "ko_k0_modeI": 1.1943, "ki_k0_modeII": 1.2010, "ko_k0_modeII": 1.1981},
        {"R1_over_R2_minus_R1": 3.0,  "ki_k0_modeI": 1.1809, "ko_k0_modeI": 1.1923, "ki_k0_modeII": 1.2024, "ko_k0_modeII": 1.2002},
        {"R1_over_R2_minus_R1": 4.0,  "ki_k0_modeI": 1.1822, "ko_k0_modeI": 1.1911, "ki_k0_modeII": 1.2027, "ko_k0_modeII": 1.2009}
    ]
    return compare_sif_table(rows, corrected_gold_rows, key_cols, sif_cols, tol)


# === block: score_1 (check id='table_3_4_check') ===
def score_1(artifact, step, ctx):
    rows = artifact if isinstance(artifact, list) else []
    key_cols = ["R1_over_R2_minus_R1", "d_minus_R1_over_R2_minus_R1"]
    sif_cols = ["ki_k0_modeI", "ki_k0_modeII"]
    tol = step.get("tolerance", 0.01)

    corrected_gold = [
        {"R1_over_R2_minus_R1": 1/3, "d_minus_R1_over_R2_minus_R1": 0.1, "ki_k0_modeI": 1.1694, "ki_k0_modeII": 1.1192},
        {"R1_over_R2_minus_R1": 1/3, "d_minus_R1_over_R2_minus_R1": 0.2, "ki_k0_modeI": 1.2321, "ki_k0_modeII": 1.1424},
        {"R1_over_R2_minus_R1": 1/3, "d_minus_R1_over_R2_minus_R1": 0.3, "ki_k0_modeI": 1.3010, "ki_k0_modeII": 1.1904},
        {"R1_over_R2_minus_R1": 1/3, "d_minus_R1_over_R2_minus_R1": 0.4, "ki_k0_modeI": 1.3805, "ki_k0_modeII": 1.2592},
        {"R1_over_R2_minus_R1": 1/3, "d_minus_R1_over_R2_minus_R1": 0.5, "ki_k0_modeI": 1.4753, "ki_k0_modeII": 1.3538},
        {"R1_over_R2_minus_R1": 1/3, "d_minus_R1_over_R2_minus_R1": 0.6, "ki_k0_modeI": 1.5928, "ki_k0_modeII": 1.4872},
        {"R1_over_R2_minus_R1": 1/3, "d_minus_R1_over_R2_minus_R1": 0.7, "ki_k0_modeI": 1.7486, "ki_k0_modeII": 1.6880},
        {"R1_over_R2_minus_R1": 0.5, "d_minus_R1_over_R2_minus_R1": 0.1, "ki_k0_modeI": 1.1605, "ki_k0_modeII": 1.1207},
        {"R1_over_R2_minus_R1": 0.5, "d_minus_R1_over_R2_minus_R1": 0.2, "ki_k0_modeI": 1.2324, "ki_k0_modeII": 1.1286},
        {"R1_over_R2_minus_R1": 0.5, "d_minus_R1_over_R2_minus_R1": 0.3, "ki_k0_modeI": 1.3151, "ki_k0_modeII": 1.1644},
        {"R1_over_R2_minus_R1": 0.5, "d_minus_R1_over_R2_minus_R1": 0.4, "ki_k0_modeI": 1.4092, "ki_k0_modeII": 1.2249},
        {"R1_over_R2_minus_R1": 0.5, "d_minus_R1_over_R2_minus_R1": 0.5, "ki_k0_modeI": 1.5182, "ki_k0_modeII": 1.3140},
        {"R1_over_R2_minus_R1": 0.5, "d_minus_R1_over_R2_minus_R1": 0.6, "ki_k0_modeI": 1.6484, "ki_k0_modeII": 1.4434},
        {"R1_over_R2_minus_R1": 0.5, "d_minus_R1_over_R2_minus_R1": 0.7, "ki_k0_modeI": 1.8145, "ki_k0_modeII": 1.6407},
        {"R1_over_R2_minus_R1": 1.0, "d_minus_R1_over_R2_minus_R1": 0.1, "ki_k0_modeI": 1.1543, "ki_k0_modeII": 1.1363},
        {"R1_over_R2_minus_R1": 1.0, "d_minus_R1_over_R2_minus_R1": 0.2, "ki_k0_modeI": 1.2486, "ki_k0_modeII": 1.1267},
        {"R1_over_R2_minus_R1": 1.0, "d_minus_R1_over_R2_minus_R1": 0.3, "ki_k0_modeI": 1.3690, "ki_k0_modeII": 1.1461},
        {"R1_over_R2_minus_R1": 1.0, "d_minus_R1_over_R2_minus_R1": 0.4, "ki_k0_modeI": 1.5087, "ki_k0_modeII": 1.1926},
        {"R1_over_R2_minus_R1": 1.0, "d_minus_R1_over_R2_minus_R1": 0.5, "ki_k0_modeI": 1.6667, "ki_k0_modeII": 1.2708},
        {"R1_over_R2_minus_R1": 1.0, "d_minus_R1_over_R2_minus_R1": 0.6, "ki_k0_modeI": 1.8446, "ki_k0_modeII": 1.3920},
        {"R1_over_R2_minus_R1": 1.0, "d_minus_R1_over_R2_minus_R1": 0.7, "ki_k0_modeI": 2.0505, "ki_k0_modeII": 1.5830},
        {"R1_over_R2_minus_R1": 2.0, "d_minus_R1_over_R2_minus_R1": 0.1, "ki_k0_modeI": 1.1572, "ki_k0_modeII": 1.1675},
        {"R1_over_R2_minus_R1": 2.0, "d_minus_R1_over_R2_minus_R1": 0.2, "ki_k0_modeI": 1.2786, "ki_k0_modeII": 1.1425},
        {"R1_over_R2_minus_R1": 2.0, "d_minus_R1_over_R2_minus_R1": 0.3, "ki_k0_modeI": 1.4476, "ki_k0_modeII": 1.1519},
        {"R1_over_R2_minus_R1": 2.0, "d_minus_R1_over_R2_minus_R1": 0.4, "ki_k0_modeI": 1.6581, "ki_k0_modeII": 1.1889},
        {"R1_over_R2_minus_R1": 2.0, "d_minus_R1_over_R2_minus_R1": 0.5, "ki_k0_modeI": 1.9072, "ki_k0_modeII": 1.2584},
        {"R1_over_R2_minus_R1": 2.0, "d_minus_R1_over_R2_minus_R1": 0.6, "ki_k0_modeI": 2.1905, "ki_k0_modeII": 1.3727},
        {"R1_over_R2_minus_R1": 2.0, "d_minus_R1_over_R2_minus_R1": 0.7, "ki_k0_modeI": 2.4998, "ki_k0_modeII": 1.5585},
    ]
    return compare_sif_table(rows, corrected_gold, key_cols, sif_cols, tol)


# === block: score_2 (check id='table_9_10_check') ===
def score_2(artifact, step, ctx):
    rows = artifact if isinstance(artifact, list) else []
    gold_rows = step.get("gold_rows", [])
    key_cols = step.get("gold_key_columns", [])
    sif_cols = step.get("gold_sif_columns", [])
    tol = step.get("tolerance", 0.01)
    return compare_sif_table(rows, gold_rows, key_cols, sif_cols, tol)


# === block: score_3 (check id='table_11_12_check') ===
def score_3(artifact, step, ctx):
    rows = artifact if isinstance(artifact, list) else []
    gold_rows = step.get("gold_rows", [])
    key_cols = step.get("gold_key_columns", [])
    sif_cols = step.get("gold_sif_columns", [])
    tol = step.get("tolerance", 0.01)
    return compare_sif_table(rows, gold_rows, key_cols, sif_cols, tol)


_SCORERS = {
    'table_1_2_check': score_0,
    'table_3_4_check': score_1,
    'table_9_10_check': score_2,
    'table_11_12_check': score_3,
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
