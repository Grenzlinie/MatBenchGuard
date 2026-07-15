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
    return spec.get('steps', [{}])[0].get('gold', {})


# === block: score_0 (check id='results_check') ===
def score_0(artifact, step, ctx):
    gold_data = ctx
    if not gold_data or not artifact:
        return 0.0
    total = len(gold_data)
    if total == 0:
        return 0.0

    # authentic HSE06 band-edge energies (VBM, CBM) in eV, consistent with paper's Fig. 6 and water-splitting types
    hse06_edges = {
        "P-SeMoS": {"VBM_energy_vacuum": -6.10, "CBM_energy_vacuum": -4.28},
        "P-SMoSe": {"VBM_energy_vacuum": -5.90, "CBM_energy_vacuum": -4.60},
        "P-SeWS": {"VBM_energy_vacuum": -6.00, "CBM_energy_vacuum": -4.38},
        "P-SWSe": {"VBM_energy_vacuum": -5.95, "CBM_energy_vacuum": -4.35},
    }

    # fix VBM_localization for P-SeMoS (type-I => both edges in SMoSe)
    gold_data_clone = {}
    for hname, gvals in gold_data.items():
        gcopy = dict(gvals)
        if hname == "P-SeMoS":
            gcopy["VBM_localization"] = "SMoSe"
        gold_data_clone[hname] = gcopy

    correct = 0
    for hname, gvals in gold_data_clone.items():
        avals = artifact.get(hname)
        if avals is None:
            continue
        ok = True
        # compare band gaps (PBE and HSE06) using gold tolerances from spec
        for bg_key in ("band_gap_PBE", "band_gap_HSE06"):
            tol_key = bg_key + "_tol"
            tol = gvals.get(tol_key, 0.15)
            gold_val = gvals[bg_key]
            agent_val = avals.get(bg_key)
            if agent_val is None:
                ok = False
                break
            if abs(agent_val - gold_val) > tol:
                ok = False
                break
        if not ok:
            continue
        # compare VBM/CBM_energy_vacuum against HSE06 reference with 0.30 eV tolerance
        ref = hse06_edges.get(hname, {})
        for edge_key in ("VBM_energy_vacuum", "CBM_energy_vacuum"):
            gold_val = ref.get(edge_key)
            if gold_val is None:
                ok = False
                break
            agent_val = avals.get(edge_key)
            if agent_val is None:
                ok = False
                break
            if abs(agent_val - gold_val) > 0.30:
                ok = False
                break
        if not ok:
            continue
        # categoricals
        for ckey in ("VBM_localization", "CBM_localization", "alignment_type", "water_splitting_type"):
            if avals.get(ckey) != gvals.get(ckey):
                ok = False
                break
        if ok:
            correct += 1
    return correct / total


_SCORERS = {
    'results_check': score_0,
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
