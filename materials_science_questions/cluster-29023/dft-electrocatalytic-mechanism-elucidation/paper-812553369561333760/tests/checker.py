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
    ref_rows = []
    tol_map = {}
    for step in spec.get("steps", []):
        if step.get("id") == "adsorption_energies_check":
            ref_rows = step.get("reference_rows", [])
            tol_map = step.get("tolerance_map", {})
            break
    return {"reference_rows": ref_rows, "tolerance_map": tol_map}


# === block: score_0 (check id='adsorption_energies_check') ===
def score_0(artifact, step, ctx):
    ref_rows = ctx["reference_rows"]
    tol_map = ctx["tolerance_map"]
    if not artifact:
        return 0.0
    agent_rows = []
    for row in artifact:
        try:
            e = float(row.get("adsorption_energy_eV", "nan"))
            s = row.get("surface", "")
            a = row.get("adsorbate", "")
        except:
            continue
        agent_rows.append((s, a, e))
    used = set()
    n_gold = len(ref_rows)
    n_matched = 0
    for gold in ref_rows:
        g_surf = gold["surface"]
        g_ads = gold["adsorbate"]
        g_val = gold["adsorption_energy_eV"]
        tol = tol_map.get(g_ads, 0.3)
        found = False
        for i, (s, a, e) in enumerate(agent_rows):
            if i in used:
                continue
            if s == g_surf and a == g_ads and abs(e - g_val) <= tol:
                used.add(i)
                found = True
                break
        if found:
            n_matched += 1
    return n_matched / n_gold if n_gold > 0 else 0.0


# === block: score_1 (check id='dos_structure_check') ===
def score_1(artifact, step, ctx):
    expected_surfaces = step.get("expected_surfaces", ["001", "111_Co", "111_CoZn"])
    if not artifact:
        return 0.0
    surf_has_unoccupied = {s: False for s in expected_surfaces}
    for row in artifact:
        s = row.get("surface", "")
        try:
            e = float(row.get("energy_eV", 0))
            p = float(row.get("pdos_Co", 0))
        except:
            continue
        if s in surf_has_unoccupied and e > 0 and p > 0:
            surf_has_unoccupied[s] = True
    count = sum(1 for v in surf_has_unoccupied.values() if v)
    return count / len(expected_surfaces) if expected_surfaces else 0.0


_SCORERS = {
    'adsorption_energies_check': score_0,
    'dos_structure_check': score_1,
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
