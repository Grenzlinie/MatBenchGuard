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


# === block: score_0 (check id='step_energy') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) != 3:
        return 0.0
    energies = {}
    for item in artifact:
        if not isinstance(item, dict):
            return 0.0
        poly = item.get("polymorph")
        val = item.get("total_lattice_energy_eV")
        if poly is not None and isinstance(val, (int, float)):
            energies[poly] = val
    required = ["rock_salt", "zinc_blende", "wurtzite"]
    if not all(p in energies for p in required):
        return 0.0
    order_ok = (energies["rock_salt"] < energies["wurtzite"] < energies["zinc_blende"])
    gold = step["gold"]
    tol = step["tolerance_energy_abs"]
    ok = 0
    for p in required:
        if abs(energies[p] - gold[p]) <= tol:
            ok += 1
    energy_score = ok / 3.0
    score = 0.2 * int(order_ok) + 0.8 * energy_score
    return float(score)


# === block: score_1 (check id='step_lattice') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) != 3:
        return 0.0
    polys = {}
    for item in artifact:
        poly = item.get("polymorph")
        a = item.get("a_nm")
        c = item.get("c_nm")
        if poly and isinstance(a, (int, float)):
            polys[poly] = (a, c)
    required = ["rock_salt", "zinc_blende", "wurtzite"]
    if not all(p in polys for p in required):
        return 0.0
    gold = step["gold"]
    tol_a = step["tolerance_a_relative"]
    tol_c = step["tolerance_c_relative"]
    checks = []
    # rock salt a
    ga = gold["rock_salt"]["a_nm"]
    a_rs = polys["rock_salt"][0]
    checks.append(abs(a_rs - ga) <= tol_a * abs(ga) if ga else True)
    # zinc blende a
    ga_zb = gold["zinc_blende"]["a_nm"]
    a_zb = polys["zinc_blende"][0]
    checks.append(abs(a_zb - ga_zb) <= tol_a * abs(ga_zb))
    # wurtzite a and c
    gw = gold["wurtzite"]
    a_w = polys["wurtzite"][0]
    c_w = polys["wurtzite"][1]
    checks.append(abs(a_w - gw["a_nm"]) <= tol_a * abs(gw["a_nm"]))
    checks.append(abs(c_w - gw["c_nm"]) <= tol_c * abs(gw["c_nm"]) if isinstance(c_w, (int, float)) else False)
    score = sum(checks) / len(checks)
    return float(score)


# === block: score_2 (check id='step_dielectric') ===
def score_2(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) != 3:
        return 0.0
    polys_data = {}
    for item in artifact:
        poly = item.get("polymorph")
        if not poly:
            return 0.0
        polys_data[poly] = item
    required = ["rock_salt", "zinc_blende", "wurtzite"]
    if not all(p in polys_data for p in required):
        return 0.0
    gold = step["gold"]
    tol = step["tolerance_relative"]
    fields_all = ["epsilon_0", "epsilon_inf", "epsilon_0_11", "epsilon_0_33", "epsilon_inf_11", "epsilon_inf_33"]
    checks = []
    for poly in required:
        g = gold[poly]
        data = polys_data[poly]
        for f in fields_all:
            expected = g.get(f)
            val = data.get(f)
            if expected is None:
                checks.append(val is None)
            else:
                if isinstance(val, (int, float)):
                    checks.append(abs(val - expected) <= tol * abs(expected))
                else:
                    checks.append(False)
    score = sum(checks) / len(checks)
    return float(score)


_SCORERS = {
    'step_energy': score_0,
    'step_lattice': score_1,
    'step_dielectric': score_2,
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
