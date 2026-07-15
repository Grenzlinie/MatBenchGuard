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
    import csv, json, math
    gold_list = spec.get('gold_values', [])
    gold_dict = {}
    for item in gold_list:
        key = (item['length_nm'], item['temperature_K'], round(item['ITCA_deg'], 2))
        gold_dict[key] = item['k']
    return {'gold': gold_dict}


# === block: score_0 (check id='main') ===
def score_0(artifact, step, ctx):
    def row_match(agent_row, gold_key):
        try:
            sys = agent_row.get('system', '')
            if sys != 'DWCNT':
                return False
            l = float(agent_row['length_nm'])
            t = float(agent_row['temperature_K'])
            itca = float(agent_row['ITCA_deg'])
            return (abs(l - gold_key[0]) < 0.001 and abs(t - gold_key[1]) < 0.001 and abs(itca - gold_key[2]) < 0.01)
        except (ValueError, KeyError):
            return False

    gold = ctx['gold']
    agent_k = {}
    for row in artifact:
        if not all(col in row for col in ['system', 'length_nm', 'temperature_K', 'ITCA_deg', 'thermal_conductivity_W_mK']):
            continue
        for gkey, gk in gold.items():
            if row_match(row, gkey):
                if gkey not in agent_k:
                    try:
                        agent_k[gkey] = float(row['thermal_conductivity_W_mK'])
                    except:
                        pass
                break

    rel_tol = 0.15
    abs_correct = 0
    total_gold = len(gold)
    for gkey, gk in gold.items():
        if gkey in agent_k:
            err = abs(agent_k[gkey] - gk) / gk if gk != 0 else (0 if agent_k[gkey] == 0 else 1)
            if err <= rel_tol:
                abs_correct += 1
    score_abs = (abs_correct / total_gold) * 0.5 if total_gold else 0

    itca_keys = [(10, 200, round(itca, 2)) for itca in [0.0, 5.82, 14.70, 23.41, 30.00]]
    itca_vals = []
    for key in itca_keys:
        if key in agent_k:
            itca_vals.append(agent_k[key])
        else:
            itca_vals = None
            break
    if itca_vals is not None:
        increasing = all(itca_vals[i] < itca_vals[i+1] for i in range(len(itca_vals)-1))
        score_itca = 0.2 if increasing else 0.0
    else:
        score_itca = 0.0

    len_keys = [(5, 200, 0.0), (10, 200, 0.0), (20, 200, 0.0)]
    len_vals = []
    for key in len_keys:
        if key in agent_k:
            len_vals.append(agent_k[key])
        else:
            len_vals = None
            break
    score_len = 0.0
    if len_vals is not None:
        k5, k10, k20 = len_vals
        mono = k10 > k5 and k20 > k10
        growth_rate_decrease = (k20 - k10)/10 < (k10 - k5)/5
        if mono and growth_rate_decrease:
            score_len = 0.15
        elif mono:
            score_len = 0.075

    temp_keys = [(10, 200, 0.0), (10, 300, 0.0), (10, 400, 0.0)]
    temp_vals = []
    for key in temp_keys:
        if key in agent_k:
            temp_vals.append(agent_k[key])
        else:
            temp_vals = None
            break
    score_temp = 0.0
    if temp_vals is not None:
        k200, k300, k400 = temp_vals
        mono_dec = k200 > k300 > k400
        frac_drop = (k200 - k300)/k200 if k200 != 0 else 0
        target_drop = 0.2138
        drop_tol = 0.05
        drop_ok = abs(frac_drop - target_drop) <= drop_tol
        if mono_dec and drop_ok:
            score_temp = 0.15
        elif mono_dec:
            score_temp = 0.075

    total = score_abs + score_itca + score_len + score_temp
    return min(1.0, total)


_SCORERS = {
    'main': score_0,
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
