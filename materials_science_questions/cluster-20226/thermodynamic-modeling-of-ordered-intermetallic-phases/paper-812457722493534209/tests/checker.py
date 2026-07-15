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
    gold_raw = spec.get("gold_table", [])
    gold_map = {}
    for g in gold_raw:
        gold_map[(g["system"], g["model_type"])] = g
    return {"gold_map": gold_map, "tolerance_surface": 5.0, "tolerance_edge_corner": 8.0}


# === block: score_0 (check id='step_02_segregation') ===
def score_0(artifact, step, ctx):
    gold_map = ctx["gold_map"]
    tol_s = ctx["tolerance_surface"]
    tol_ec = ctx["tolerance_edge_corner"]
    rows = artifact
    if not rows:
        return 0.0
    agent_data = {}
    for r in rows:
        key = (r.get("system", "").strip(), r.get("model_type", "").strip())
        try:
            sf = float(r["surface_fraction"])
            ec = float(r["edge_corner_fraction"])
        except (ValueError, KeyError):
            sf = None
            ec = None
        agent_data[key] = (sf, ec)
    surface_ok = 0
    edge_corner_ok = 0
    total = len(gold_map)
    for key, gold in gold_map.items():
        gold_sf = float(gold["surface_fraction"])
        gold_ec = float(gold["edge_corner_fraction"])
        agent_val = agent_data.get(key)
        if agent_val is None:
            continue
        sf, ec = agent_val
        if sf is not None and abs(sf - gold_sf) <= tol_s:
            surface_ok += 1
        if ec is not None and abs(ec - gold_ec) <= tol_ec:
            edge_corner_ok += 1
    surface_subscore = surface_ok / total if total else 1.0
    edge_corner_subscore = edge_corner_ok / total if total else 1.0
    # ordering check 1: with_size Ni-Pd surface_fraction smallest among the three
    ws_rows = {k: v for k, v in agent_data.items() if k[1] == "with_size"}
    ni_pd_sf = ws_rows.get(("Ni-Pd", "with_size"), (None, None))[0]
    rni_sf = ws_rows.get(("Rh-Ni", "with_size"), (None, None))[0]
    pdcu_sf = ws_rows.get(("Pd-Cu", "with_size"), (None, None))[0]
    order1_pass = 0.0
    if ni_pd_sf is not None and rni_sf is not None and pdcu_sf is not None:
        if ni_pd_sf < rni_sf and ni_pd_sf < pdcu_sf:
            order1_pass = 1.0
    # ordering check 2: Ni-Pd without_size surface_fraction > with_size surface_fraction
    ni_pd_wo_sf = agent_data.get(("Ni-Pd", "without_size"), (None, None))[0]
    order2_pass = 0.0
    if ni_pd_wo_sf is not None and ni_pd_sf is not None:
        if ni_pd_wo_sf > ni_pd_sf:
            order2_pass = 1.0
    total_score = 0.45 * surface_subscore + 0.35 * edge_corner_subscore + 0.1 * order1_pass + 0.1 * order2_pass
    return min(1.0, max(0.0, total_score))


_SCORERS = {
    'step_02_segregation': score_0,
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
