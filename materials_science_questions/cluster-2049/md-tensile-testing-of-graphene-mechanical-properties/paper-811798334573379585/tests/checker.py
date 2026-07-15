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
    steps = spec.get("steps", [])
    gold_store = {}
    tol_store = {}
    for s in steps:
        sid = s.get("id")
        if sid in ("energies_check", "lattice_check"):
            gold_store[sid] = s.get("gold", {})
            tol_store[sid] = s.get("hidden_tolerances", {})
    return {"gold": gold_store, "tolerances": tol_store}


# === block: score_0 (check id='energies_check') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    gold_energies = ctx["gold"]["energies_check"]
    tol_erel = ctx["tolerances"]["energies_check"].get("E_rel", {})
    abs_tol = tol_erel.get("absolute", 0.005)
    rel_tol = tol_erel.get("relative", 0.10)
    mode = tol_erel.get("mode", "max")
    keys = ["CF_C","CF_W","CF_B","CH_C","CH_W","CH_B"]
    total = 0.0
    order_ok = True
    for mat in ["CF","CH"]:
        ek = [mat+"_C", mat+"_W", mat+"_B"]
        e_c = artifact.get(ek[0], {}).get("E_rel")
        e_w = artifact.get(ek[1], {}).get("E_rel")
        e_b = artifact.get(ek[2], {}).get("E_rel")
        if e_c is None or e_w is None or e_b is None:
            order_ok = False
        elif not (abs(e_c) <= abs_tol and e_w > e_c and e_b > e_w):
            order_ok = False
    for k in keys:
        v = artifact.get(k)
        if not isinstance(v, dict):
            return 0.0
        g = gold_energies.get(k, {}).get("E_rel")
        if g is None:
            continue
        sub = v.get("E_rel")
        if sub is None:
            return 0.0
        if mode == "max":
            tol = max(abs_tol, rel_tol * abs(g))
        else:
            tol = abs_tol
        diff = abs(sub - g)
        total += max(0.0, 1.0 - diff / tol)
    avg = total / len(keys)
    return 0.0 if not order_ok else avg


# === block: score_1 (check id='lattice_check') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    gold_latt = ctx["gold"]["lattice_check"]
    tol_params = {"a":0.01, "b":0.01}
    keys = ["CF_C","CF_W","CF_B","CH_C","CH_W","CH_B"]
    total = 0.0
    cnt = 0
    for k in keys:
        v = artifact.get(k)
        if not isinstance(v, dict):
            return 0.0
        g = gold_latt.get(k)
        if g is None:
            continue
        for p in ["a","b"]:
            sub = v.get(p)
            gold_val = g.get(p)
            if sub is None or gold_val is None:
                return 0.0
            diff = abs(sub - gold_val)
            tol = tol_params.get(p, 0.01)
            total += max(0.0, 1.0 - diff / tol)
            cnt += 1
    avg = total / cnt if cnt else 0.0
    contraction_ok = True
    for mat in ["CF","CH"]:
        b_C = artifact.get(mat+"_C", {}).get("b")
        b_W = artifact.get(mat+"_W", {}).get("b")
        if b_C is not None and b_W is not None and b_W >= b_C:
            contraction_ok = False
            break
    if not contraction_ok:
        avg = 0.0
    return avg


_SCORERS = {
    'energies_check': score_0,
    'lattice_check': score_1,
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
