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
    def prepare(outputs_dir, spec):
        steps = spec.get("steps", [])
        gold = {}
        for step in steps:
            sid = step.get("id")
            if "gold_orbits" in step:
                gold[sid] = step["gold_orbits"]
            elif "gold_total" in step:
                gold[sid] = step["gold_total"]
            elif "gold_mode_counts" in step:
                gold[sid] = step["gold_mode_counts"]
        return {"gold": gold}


# === block: score_0 (check id='orbit_decompositions') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold_orbits = ctx["gold"].get(step["id"], [])
        if not gold_orbits:
            return 0.0
        submitted = artifact.get("orbit_decompositions", [])
        if len(submitted) != len(gold_orbits):
            return 0.0
        gold_dict = {g["orbit"]: g for g in gold_orbits}
        correct = 0
        for s in submitted:
            orbit = s.get("orbit")
            if orbit not in gold_dict:
                continue
            gold = gold_dict[orbit]
            if s.get("multiplicity") != gold["multiplicity"]:
                continue
            if sorted(s.get("irreps", [])) == sorted(gold["irreps"]):
                correct += 1
        return correct / len(gold_orbits)


# === block: score_1 (check id='total_decomposition') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold_total = ctx["gold"].get(step["id"], {})
        if not gold_total:
            return 0.0
        submitted_total = artifact.get("total_decomposition", {})
        orbits = artifact.get("orbit_decompositions", [])
        expected = {}
        for orb in orbits:
            mult = orb.get("multiplicity", 0)
            irrs = orb.get("irreps", [])
            for irr in irrs:
                expected[irr] = expected.get(irr, 0) + mult
        if expected != submitted_total:
            return 0.0
        if submitted_total != gold_total:
            return 0.0
        return 1.0


# === block: score_2 (check id='mode_counts') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold_counts = ctx["gold"].get(step["id"], [])
        if not gold_counts:
            return 0.0
        submitted = artifact.get("mode_counts", [])
        key = lambda x: (x.get("orbit",""), x.get("activity",""))
        gold_sorted = sorted(gold_counts, key=key)
        sub_sorted = sorted(submitted, key=key)
        if len(sub_sorted) != len(gold_sorted):
            return 0.0
        correct = 0
        for g, s in zip(gold_sorted, sub_sorted):
            if g == s:
                correct += 1
        return correct / len(gold_sorted)


_SCORERS = {
    'orbit_decompositions': score_0,
    'total_decomposition': score_1,
    'mode_counts': score_2,
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
