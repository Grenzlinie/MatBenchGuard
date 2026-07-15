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


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    artifact = artifact  # list of dicts
    step_cfg = step
    gold_300K = {
        11.5: {"yield": 3.7, "tensile": 5.44, "E": 120},
        9.9: {"yield": 3.8, "tensile": 5.6, "E": 115},
        7.7: {"yield": 4.2, "tensile": 5.65, "E": 131},
        4.1: {"yield": 3.9, "tensile": 5.1, "E": 130},
        3.6: {"yield": 3.75, "tensile": 4.8, "E": 129},
        2.5: {"yield": 3.5, "tensile": 4.9, "E": 124}
    }
    tol_yield = 0.5
    tol_tensile = 0.5
    tol_E = 10

    w_props = step_cfg.get("weight_300K_properties", 0.7)
    w_trends = step_cfg.get("weight_trends", 0.3)

    # 300K property scoring
    rows_300 = [r for r in artifact if int(float(r["temperature_K"])) == 300]
    total_checks = 0
    correct = 0
    for row in rows_300:
        try:
            grain = float(row["grain_size_nm"])
        except:
            continue
        match = None
        for g, vals in gold_300K.items():
            if abs(grain - g) < 0.02:
                match = vals
                break
        if match is None:
            continue
        for key, tol, gold_key in [("yield_strength_GPa", tol_yield, "yield"),
                                   ("tensile_strength_GPa", tol_tensile, "tensile"),
                                   ("youngs_modulus_GPa", tol_E, "E")]:
            try:
                val = float(row[key])
                gold_val = match[gold_key]
                if abs(val - gold_val) <= tol:
                    correct += 1
            except:
                pass
            total_checks += 1

    prop_score = (correct / total_checks) if total_checks > 0 else 0.0

    # trend scoring
    rows_25 = []
    for r in artifact:
        try:
            g = float(r["grain_size_nm"])
            if abs(g - 2.5) < 0.02:
                rows_25.append(r)
        except:
            pass
    temp_order = [10, 100, 300, 600, 900]
    temp_rows = {}
    for row in rows_25:
        try:
            t = int(float(row["temperature_K"]))
            if t in temp_order:
                temp_rows[t] = row
        except:
            pass
    if len(temp_rows) < 2:
        trend_score = 0.0
    else:
        yields = []
        E_vals = []
        for t in temp_order:
            if t in temp_rows:
                try:
                    y = float(temp_rows[t]["yield_strength_GPa"])
                    e = float(temp_rows[t]["youngs_modulus_GPa"])
                    yields.append(y)
                    E_vals.append(e)
                except:
                    pass
        if len(yields) < 2:
            trend_score = 0.0
        else:
            yield_mono = all(yields[i] >= yields[i+1] for i in range(len(yields)-1))
            E_mono = all(E_vals[i] >= E_vals[i+1] for i in range(len(E_vals)-1))
            yield_score = 1.0 if yield_mono else sum(1.0 for i in range(len(yields)-1) if yields[i] >= yields[i+1]) / (len(yields)-1)
            E_score = 1.0 if E_mono else sum(1.0 for i in range(len(E_vals)-1) if E_vals[i] >= E_vals[i+1]) / (len(E_vals)-1)
            trend_score = 0.5 * yield_score + 0.5 * E_score

    final_score = w_props * prop_score + w_trends * trend_score
    final_score = max(0.0, min(1.0, final_score))
    return final_score


_SCORERS = {
    'step_01': score_0,
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
