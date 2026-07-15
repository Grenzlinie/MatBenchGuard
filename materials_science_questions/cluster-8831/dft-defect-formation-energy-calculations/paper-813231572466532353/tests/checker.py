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
    return {"output_dir": outputs_dir}


# === block: score_0 (check id='s1_lattice_struct') ===
def score_0(artifact, step, ctx):
    expected = step.get("expected_compounds", ["SrO","TiO2","SrTiO3","1_p","2_p","3_p","4_p"])
    compounds = {entry["compound"] for entry in artifact} if isinstance(artifact, list) else set()
    all_neg = all(entry["energy"] < 0 for entry in artifact if isinstance(entry, dict) and "energy" in entry)
    return 1.0 if (compounds == set(expected) and all_neg) else 0.0


# === block: score_1 (check id='s2_defect_struct') ===
def score_1(artifact, step, ctx):
    if not (isinstance(artifact, dict) and "V_Sr" in artifact and "V_O" in artifact):
        return 0.0
    try:
        v_sr = float(artifact["V_Sr"]["energy"])
        v_o = float(artifact["V_O"]["energy"])
    except (KeyError, TypeError, ValueError):
        return 0.0
    return 1.0 if (v_sr > 0 and v_o > 0) else 0.0


# === block: score_2 (check id='s3_formation_struct') ===
def score_2(artifact, step, ctx):
    if not isinstance(artifact, list):
        return 0.0
    expected = ["1_p","2_p","3_p","4_p"]
    mapping = {}
    for entry in artifact:
        if isinstance(entry, dict) and "compound" in entry and "Delta_U_p+r" in entry:
            mapping[entry["compound"]] = entry["Delta_U_p+r"]
    if set(expected).difference(mapping.keys()):
        return 0.0
    values = [mapping[c] for c in expected]
    lo, hi = step.get("value_range", [-1.0, 1.0])
    range_ok = all(lo <= v <= hi for v in values)
    variation = max(values) - min(values) if values else 0
    diff_max = step.get("diff_max", 0.5)
    return 1.0 if (range_ok and variation <= diff_max) else 0.0


# === block: score_3 (check id='s4_schottky_recompute') ===
def score_3(artifact, step, ctx):
    import json, os
    try:
        output_dir = ctx["output_dir"]
        with open(os.path.join(output_dir, "lattice_energies.json")) as f:
            lat = json.load(f)
        with open(os.path.join(output_dir, "defect_energies.json")) as f:
            defs = json.load(f)
    except Exception:
        return 0.0
    lat_map = {}
    for entry in lat:
        if isinstance(entry, dict):
            lat_map[entry.get("compound","")] = entry.get("energy")
    try:
        E_SrO = float(lat_map["SrO"])
        E_SrTiO3 = float(lat_map["SrTiO3"])
        E_1 = float(lat_map["1_p"])
        E_2 = float(lat_map["2_p"])
        E_3 = float(lat_map["3_p"])
        E_4 = float(lat_map["4_p"])
        V_Sr = float(defs["V_Sr"]["energy"])
        V_O  = float(defs["V_O"]["energy"])
    except (KeyError, TypeError, ValueError):
        return 0.0
    computed = [
        V_Sr + V_O + E_SrO,                  # n=0
        V_Sr + V_O + E_1  - 1*E_SrTiO3,      # n=1
        V_Sr + V_O + E_2  - 2*E_SrTiO3,
        V_Sr + V_O + E_3  - 3*E_SrTiO3,
        V_Sr + V_O + E_4  - 4*E_SrTiO3
    ]
    gold = step.get("gold_u_sch", [4.89, 4.78, 4.76, 4.76, 4.76])
    tol = float(step.get("tolerance", 0.5))
    abs_hits = sum(1 for c, g in zip(computed, gold) if abs(c - g) <= tol)
    score_abs = abs_hits / 5.0
    variation_ok = (max(computed) - min(computed)) <= float(step.get("variation_max", 0.3))
    return 0.7 * score_abs + 0.3 * (1.0 if variation_ok else 0.0)


_SCORERS = {
    's1_lattice_struct': score_0,
    's2_defect_struct': score_1,
    's3_formation_struct': score_2,
    's4_schottky_recompute': score_3,
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
