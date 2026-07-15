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


# === block: score_0 (check id='verify_properties') ===
def score_0(artifact, step, ctx):
    from collections import defaultdict

    _n = lambda v, d=0.0: v if isinstance(v, (int, float)) else d

    systems = artifact.get("systems", [])
    if not isinstance(systems, list):
        return 0.0

    entry_map = defaultdict(list)
    for s in systems:
        key = (s.get("composition"), s.get("structure_type"))
        entry_map[key].append(s)

    expected_combos = {
        ("ScFeO3", "hexagonal"), ("InFeO3", "hexagonal"), ("LuFeO3", "hexagonal"),
        ("YbFeO3", "hexagonal"), ("ErFeO3", "hexagonal"), ("HoFeO3", "hexagonal"),
        ("YFeO3", "hexagonal"), ("DyFeO3", "hexagonal"),
        ("HoScO3", "hexagonal"), ("HoInO3", "hexagonal"), ("HoGaO3", "hexagonal"),
        ("HoCrO3", "hexagonal"), ("HoAlO3", "hexagonal"),
        ("CeFeO3", "orthorhombic"), ("SmFeO3", "orthorhombic"),
        ("GdFeO3", "orthorhombic"), ("DyFeO3", "orthorhombic"),
        ("HoAlO3", "orthorhombic"), ("HoCrO3", "orthorhombic"), ("HoGaO3", "orthorhombic")
    }
    found = sum(1 for combo in expected_combos if combo in entry_map)
    n_expected = len(expected_combos)
    presence_score = 1.0 - (n_expected - found) / n_expected if n_expected else 1.0

    # 1. Elastic isotropy (hexagonal)
    hex_el = [s for s in systems if s.get("structure_type") == "hexagonal"
              and _n(s.get("C11")) and _n(s.get("C33"))]
    elastic_ok = 0
    for s in hex_el:
        c11 = _n(s["C11"])
        c33 = _n(s["C33"])
        if c33 == 0:
            continue
        if 0.85 <= c11 / c33 <= 1.15:
            elastic_ok += 1
    elastic_score = elastic_ok / len(hex_el) if hex_el else 0.0

    # 2. Thermal expansion anisotropy (hexagonal)
    hex_exp = [s for s in systems if s.get("structure_type") == "hexagonal"
               and _n(s.get("alpha11")) and _n(s.get("alpha33"))]
    exp_ok = 0
    for s in hex_exp:
        a11 = _n(s["alpha11"])
        a33 = _n(s["alpha33"])
        if a33 == 0:
            continue
        if a11 / a33 > 2.0:
            exp_ok += 1
    exp_score = exp_ok / len(hex_exp) if hex_exp else 0.0

    # 3. Thermal conductivity isotropy (hexagonal)
    hex_k = [s for s in systems if s.get("structure_type") == "hexagonal"
             and _n(s.get("k11")) and _n(s.get("k33"))]
    k_iso_ok = 0
    for s in hex_k:
        k11 = _n(s["k11"])
        k33 = _n(s["k33"])
        if k33 == 0:
            continue
        if 0.7 <= k11 / k33 <= 1.3:
            k_iso_ok += 1
    k_iso_score = k_iso_ok / len(hex_k) if hex_k else 0.0

    # 4. Hexagonal vs orthorhombic thermal conductivity for overlapping compositions
    overlaps = [("DyFeO3",), ("HoAlO3",), ("HoCrO3",), ("HoGaO3",)]
    status = []
    for (comp,) in overlaps:
        hex_entry = entry_map.get((comp, "hexagonal"))
        ortho_entry = entry_map.get((comp, "orthorhombic"))
        if hex_entry and ortho_entry:
            h = hex_entry[0]
            o = ortho_entry[0]
            hex_k_avg = (_n(h.get("k11")) + _n(h.get("k33"))) / 2.0
            ortho_k_avg = (_n(o.get("k11")) + _n(o.get("k33"))) / 2.0
            status.append(1.0 if hex_k_avg > ortho_k_avg else 0.0)
        else:
            status.append(0.0)
    compare_score = sum(status) / len(status) if status else 0.0

    # 5. Monotonic increase of a and V with A ionic radius for AFeO3 hexagonal
    r_A = {
        "Sc": 0.745, "In": 0.800, "Lu": 0.861, "Yb": 0.868,
        "Er": 0.890, "Ho": 0.901, "Y": 0.900, "Dy": 0.912
    }
    feo_entries = []
    for A in ["Sc", "In", "Lu", "Yb", "Er", "Ho", "Y", "Dy"]:
        key = (f"{A}FeO3", "hexagonal")
        if key in entry_map:
            feo_entries.append((r_A[A], entry_map[key][0]))
    feo_entries.sort(key=lambda x: x[0])
    eps = 1e-6
    a_ok = 0
    v_ok = 0
    prev_a = -1e9
    prev_v = -1e9
    for _, s in feo_entries:
        a_val = _n(s.get("a"), None)
        v_val = _n(s.get("V"), None)
        if a_val is not None:
            if a_val >= prev_a - eps:
                a_ok += 1
            prev_a = a_val
        if v_val is not None:
            if v_val >= prev_v - eps:
                v_ok += 1
            prev_v = v_val
    total_a = len(feo_entries)
    total_v = len(feo_entries)
    a_mono = a_ok / total_a if total_a > 0 else 0.0
    v_mono = v_ok / total_v if total_v > 0 else 0.0
    monotonic_score = 0.5 * a_mono + 0.5 * v_mono

    weights = {
        "presence": 0.05,
        "elastic": 0.20,
        "expansion": 0.20,
        "k_iso": 0.15,
        "compare": 0.15,
        "monotonic": 0.25
    }
    total = (weights["presence"] * presence_score +
             weights["elastic"] * elastic_score +
             weights["expansion"] * exp_score +
             weights["k_iso"] * k_iso_score +
             weights["compare"] * compare_score +
             weights["monotonic"] * monotonic_score)
    return min(max(total, 0.0), 1.0)


_SCORERS = {
    'verify_properties': score_0,
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
