import os
import json
import csv

# === author imports / helpers ===
import math


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
    ctx = {}
    for step in spec.get("steps", []):
        ctx[step["id"]] = step
    return ctx


# === block: score_0 (check id='step_hydration_shell') ===
def score_0(artifact, step, ctx):
    gold = step["target"]["gold"]
    tol = step["target"]["tolerance_abs"]
    rh_to_gold = {g["RH"]: g["percentage_in_shell"] for g in gold}
    rows_by_rh = {}
    for row in artifact:
        try:
            rh = int(row["RH"].strip())
            rows_by_rh[rh] = row
        except: pass
    total = len(gold)
    ok = 0
    for g in gold:
        rh = g["RH"]
        row = rows_by_rh.get(rh)
        if row is None:
            continue
        try:
            val = float(row["percentage_in_shell"])
            if abs(val - g["percentage_in_shell"]) <= tol:
                ok += 1
        except: pass
    return ok / total if total>0 else 0.0


# === block: score_1 (check id='step_isotherm') ===
def score_1(artifact, step, ctx):
    gold = step["target"]["gold"]
    rel_tol = step["target"]["tolerance_relative"]
    rh_to_gold = {g["RH"]: g for g in gold}
    rows_by_rh = {}
    for item in artifact:
        try:
            rh = int(item.get("RH"))
            if isinstance(rh, float): rh = int(rh)
            rows_by_rh[rh] = item
        except: pass
    total = len(gold)
    ok = 0
    for g in gold:
        rh = g["RH"]
        row = rows_by_rh.get(rh)
        if row is None: continue
        try:
            load_ads = float(row.get("loading_adsorption"))
            load_des = float(row.get("loading_desorption"))
            g_ads = g["loading_adsorption"]
            g_des = g["loading_desorption"]
            if g_ads > 0:
                err_ads = abs(load_ads - g_ads) / g_ads
            else:
                err_ads = abs(load_ads - g_ads)
            if g_des > 0:
                err_des = abs(load_des - g_des) / g_des
            else:
                err_des = abs(load_des - g_des)
            if err_ads <= rel_tol and err_des <= rel_tol:
                ok += 1
        except: pass
    score_ref = ok / total if total > 0 else 0.0
    eps = 1e-6
    hysteresis_ok = all(float(row.get("loading_desorption",0)) >= float(row.get("loading_adsorption",0)) - eps for row in artifact)
    sorted_rows = sorted(artifact, key=lambda r: int(r.get("RH")))
    ads_loads = [float(r["loading_adsorption"]) for r in sorted_rows]
    mono_ads_ok = all(ads_loads[i] <= ads_loads[i+1] + eps for i in range(len(ads_loads)-1))
    struct_score = (hysteresis_ok + mono_ads_ok) / 2.0
    return 0.7 * score_ref + 0.3 * struct_score


# === block: score_2 (check id='step_subdiffusion') ===
def score_2(artifact, step, ctx):
    gold = step["target"]["gold"]
    tol = step["target"]["tolerance_abs"]
    rh_to_gold = {g["RH"]: g for g in gold}
    rows_by_rh = {}
    for row in artifact:
        try:
            rh = int(row["RH"].strip())
            rows_by_rh[rh] = row
        except: pass
    total = len(gold)
    ok = 0
    for g in gold:
        rh = g["RH"]
        row = rows_by_rh.get(rh)
        if row is None: continue
        try:
            r_g = float(row["rigid_gamma"])
            f_g = float(row["flexible_gamma"])
            if abs(r_g - g["rigid_gamma"]) <= tol and abs(f_g - g["flexible_gamma"]) <= tol:
                ok += 1
        except: pass
    score_ref = ok / total if total>0 else 0.0
    flexible_ge = all(float(row["flexible_gamma"]) >= float(row["rigid_gamma"]) - 0.01 for row in artifact)
    sorted_rows = sorted(artifact, key=lambda r: int(r["RH"]))
    rigid_seq = [float(r["rigid_gamma"]) for r in sorted_rows]
    flex_seq = [float(r["flexible_gamma"]) for r in sorted_rows]
    mono_rigid = all(rigid_seq[i] <= rigid_seq[i+1] + 0.01 for i in range(len(rigid_seq)-1))
    mono_flex = all(flex_seq[i] <= flex_seq[i+1] + 0.01 for i in range(len(flex_seq)-1))
    struct_score = (flexible_ge + mono_rigid + mono_flex) / 3.0
    return 0.7 * score_ref + 0.3 * struct_score


# === block: score_3 (check id='step_lattice') ===
def score_3(artifact, step, ctx):
    gold = step["target"]["gold"]
    rel_tol = step["target"]["tolerance_relative"]
    rh_to_gold = {g["RH"]: g for g in gold}
    rows_by_rh = {}
    for row in artifact:
        try:
            rh = int(row["RH"].strip())
            rows_by_rh[rh] = row
        except: pass
    total = len(gold)
    ok = 0
    for g in gold:
        rh = g["RH"]
        row = rows_by_rh.get(rh)
        if row is None: continue
        try:
            a = float(row["a"]); b = float(row["b"]); c = float(row["c"])
            ga = g["a"]; gb = g["b"]; gc = g["c"]
            err_a = abs(a-ga)/abs(ga) if abs(ga)>0 else abs(a-ga)
            err_b = abs(b-gb)/abs(gb) if abs(gb)>0 else abs(b-gb)
            err_c = abs(c-gc)/abs(gc) if abs(gc)>0 else abs(c-gc)
            if err_a <= rel_tol and err_b <= rel_tol and err_c <= rel_tol:
                ok += 1
        except: pass
    score_ref = ok / total if total>0 else 0.0
    sorted_rows = sorted(artifact, key=lambda r: int(r["RH"]))
    a_seq = [float(r["a"]) for r in sorted_rows]
    b_seq = [float(r["b"]) for r in sorted_rows]
    c_seq = [float(r["c"]) for r in sorted_rows]
    eps = 0.01
    mono_a = all(a_seq[i] <= a_seq[i+1] + eps for i in range(len(a_seq)-1))
    mono_b = all(b_seq[i] <= b_seq[i+1] + eps for i in range(len(b_seq)-1))
    mono_c = all(c_seq[i] <= c_seq[i+1] + eps for i in range(len(c_seq)-1))
    struct_score = (mono_a + mono_b + mono_c) / 3.0
    return 0.7 * score_ref + 0.3 * struct_score


_SCORERS = {
    'step_hydration_shell': score_0,
    'step_isotherm': score_1,
    'step_subdiffusion': score_2,
    'step_lattice': score_3,
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
