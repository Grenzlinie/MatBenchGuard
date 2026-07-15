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


# === block: score_0 (check id='temperature_intensity') ===
def score_0(artifact, step, ctx):
    score = 0.0
    gold_temps = step["gold_temperatures"]
    gold_pt = step["gold_P_transverse"]
    gold_pl = step["gold_P_longitudinal"]
    tol = step["tolerance_P"]
    n = len(gold_temps)
    data = {}
    for row in artifact:
        try:
            t = float(row["T"])
            pt = float(row["P_transverse"])
            pl = float(row["P_longitudinal"])
            data[t] = (pt, pl)
        except:
            pass
    pass_pt = 0
    pass_pl = 0
    for i, tref in enumerate(gold_temps):
        if tref in data:
            pt, pl = data[tref]
            if abs(pt - gold_pt[i]) / abs(gold_pt[i]) <= tol:
                pass_pt += 1
            if abs(pl - gold_pl[i]) / abs(gold_pl[i]) <= tol:
                pass_pl += 1
    score = (pass_pt + pass_pl) / (2.0 * n)
    return score


# === block: score_1 (check id='anisotropy_polarization') ===
def score_1(artifact, step, ctx):
    score = 0.0
    gold_temps = step["gold_temperatures"]
    gold_K = step["gold_K"]
    gold_D = step["gold_D"]
    tol_K = step["tolerance_K"]
    tol_D = step["tolerance_D"]
    n = len(gold_temps)
    data = {}
    for row in artifact:
        try:
            t = float(row["T"])
            k = float(row["K"])
            d = float(row["D"])
            data[t] = (k, d)
        except:
            pass
    pass_K = 0
    pass_D = 0
    for i, tref in enumerate(gold_temps):
        if tref in data:
            k, d = data[tref]
            if abs(k - gold_K[i]) / abs(gold_K[i]) <= tol_K:
                pass_K += 1
            if abs(d - gold_D[i]) / abs(gold_D[i]) <= tol_D:
                pass_D += 1
    score = (pass_K + pass_D) / (2.0 * n)
    return score


# === block: score_2 (check id='structural_trends') ===
def score_2(artifact, step, ctx):
    rows = [(float(r["T"]), float(r["K"]), float(r["D"])) for r in artifact]
    if not rows: return 0.0
    rows.sort(key=lambda x: x[0])
    n = len(rows)
    ks = [k for _,k,_ in rows]
    ds = [d for _,_,d in rows]
    k_gt1_score = 1.0 if all(k > 1.0 for k in ks) else sum(1 for k in ks if k > 1) / n
    eps = 1e-9
    if n > 1:
        inc_K = sum(1 for i in range(n-1) if ks[i] < ks[i+1] - eps)
        inc_D = sum(1 for i in range(n-1) if ds[i] < ds[i+1] - eps)
        k_mono_score = max(0.0, 1.0 - inc_K / (n-1))
        d_mono_score = max(0.0, 1.0 - inc_D / (n-1))
    else:
        k_mono_score = d_mono_score = 1.0
    score = (k_gt1_score + k_mono_score + d_mono_score) / 3.0
    return score


_SCORERS = {
    'temperature_intensity': score_0,
    'anisotropy_polarization': score_1,
    'structural_trends': score_2,
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
