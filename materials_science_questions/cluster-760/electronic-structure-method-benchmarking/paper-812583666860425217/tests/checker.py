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


# === block: score_0 (check id='dft_row_accuracy') ===
def score_0(artifact, step, ctx):
        gold_table = step.get("gold_table", [])
        tol_energy = step.get("tolerances", {}).get("binding_energy_kcal_mol", 2.0)
        tol_dist = step.get("tolerances", {}).get("K_O_distance_angstrom", 0.02)
        # build lookup from artifact rows by (complex, functional, basis)
        art_lookup = {}
        for row in artifact:
            key = (row.get("complex", "").strip(), row.get("functional", "").strip(), row.get("basis", "").strip())
            art_lookup[key] = row
        num_gold = len(gold_table)
        if num_gold == 0:
            return 0.0
        score = 0.0
        for grec in gold_table:
            key = (grec["complex"], grec["functional"], grec["basis"])
            arow = art_lookup.get(key)
            if arow is None:
                continue
            try:
                energy = float(arow.get("binding_energy_kcal_mol", None))
                dist = float(arow.get("K_O_distance_angstrom", None))
            except (TypeError, ValueError):
                continue
            if abs(energy - grec["binding_energy_kcal_mol"]) <= tol_energy and abs(dist - grec["K_O_distance_angstrom"]) <= tol_dist:
                score += 1.0
        return score / num_gold


# === block: score_1 (check id='trend_binding') ===
def score_1(artifact, step, ctx):
        # find SVWN and BLYP rows for K+:12c4
        svwn_energy = None
        blyp_energy = None
        for row in artifact:
            if row.get("complex", "").strip() == "K+:12c4":
                func = row.get("functional", "").strip()
                try:
                    val = float(row.get("binding_energy_kcal_mol", None))
                except (TypeError, ValueError):
                    continue
                if func == "SVWN":
                    svwn_energy = val
                elif func == "BLYP":
                    blyp_energy = val
        if svwn_energy is None or blyp_energy is None:
            return 0.0
        if blyp_energy - svwn_energy >= 4.0:
            return 1.0
        return 0.0


# === block: score_2 (check id='trend_distance') ===
def score_2(artifact, step, ctx):
        svwn_dist = None
        bp86_dist = None
        for row in artifact:
            if row.get("complex", "").strip() == "K+:12c4":
                func = row.get("functional", "").strip()
                try:
                    val = float(row.get("K_O_distance_angstrom", None))
                except (TypeError, ValueError):
                    continue
                if func == "SVWN":
                    svwn_dist = val
                elif func == "BP86":
                    bp86_dist = val
        if svwn_dist is None or bp86_dist is None:
            return 0.0
        if bp86_dist - svwn_dist >= 0.05:
            return 1.0
        return 0.0


_SCORERS = {
    'dft_row_accuracy': score_0,
    'trend_binding': score_1,
    'trend_distance': score_2,
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
