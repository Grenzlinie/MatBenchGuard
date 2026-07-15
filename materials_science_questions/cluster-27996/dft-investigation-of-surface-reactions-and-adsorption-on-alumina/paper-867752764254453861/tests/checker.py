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


# === block: score_0 (check id='chemisorption_results') ===
def score_0(artifact, step, ctx):
    gold = step.get("gold", {})
    entries = gold.get("entries", [])
    tolerances = gold.get("tolerances", {})
    if not isinstance(artifact, list):
        return 0.0

    # All possible fields; some may be excluded per entry.
    all_fields = ["Ec", "bond_length", "HOMO_LUMO_gap", "Mulliken_charge_Al"]

    # Build index of agent entries by (cluster, site, basis)
    agent_index = {}
    for entry in artifact:
        if not isinstance(entry, dict):
            continue
        key = (entry.get("cluster"), entry.get("site"), entry.get("basis"))
        agent_index.setdefault(key, []).append(entry)

    # Ensure Ec tolerance is at least 0.5 eV to account for code/basis-set spread.
    ec_tolerance = max(tolerances.get("Ec", 0.0), 0.5)

    def _fields_for_entry(gold_entry):
        """Return the subset of all_fields that should be checked for this entry."""
        cluster = gold_entry.get("cluster", "")
        site   = gold_entry.get("site", "")
        # The paper does not report Mulliken charges for the Ga4As4H12 top site.
        if cluster == "Ga4As4H12" and site == "top":
            return [f for f in all_fields if f != "Mulliken_charge_Al"]
        return list(all_fields)

    total_score = 0.0
    num_required = len(entries)
    if num_required == 0:
        return 1.0

    for gold_entry in entries:
        key = (gold_entry["cluster"], gold_entry["site"], gold_entry["basis"])
        matches = agent_index.get(key, [])
        if not matches:
            continue  # entry missing
        match = matches[0]  # first match only
        fields_to_check = _fields_for_entry(gold_entry)
        if not fields_to_check:
            continue
        fields_ok = 0
        for field in fields_to_check:
            val = match.get(field)
            if val is None or not isinstance(val, (int, float)):
                continue
            if field == "Ec":
                # Trend-based checks: cage must be strongly negative, trough strongly positive.
                cluster_name = gold_entry["cluster"]
                site_name = gold_entry["site"]
                if cluster_name == "Ga4As4H12" and site_name == "cage":
                    # cage site is expected to be unbound (strongly negative)
                    if val < -2.0:
                        fields_ok += 1
                        continue
                elif cluster_name == "Ga19As15H39" and site_name == "trough":
                    # trough 5a site is expected to be strongly bound
                    if val > 4.0:
                        fields_ok += 1
                        continue
                # Fallback: absolute tolerance with generous margin
                if abs(val - gold_entry["Ec"]) <= ec_tolerance:
                    fields_ok += 1
            else:
                diff = abs(val - gold_entry[field])
                tol = tolerances.get(field, 0.0)
                if diff <= tol:
                    fields_ok += 1
        total_score += fields_ok / len(fields_to_check)

    return total_score / num_required


_SCORERS = {
    'chemisorption_results': score_0,
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
