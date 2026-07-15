import os
import json
import csv

# === author imports / helpers ===
import json
import math


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
    import json, os
    ctx = {"artifacts": {}}
    for step in spec.get("steps", []):
        fname = step.get("output_file")
        if fname:
            path = os.path.join(outputs_dir, fname)
            if os.path.exists(path):
                with open(path) as f:
                    ctx["artifacts"][fname] = json.load(f)
            else:
                ctx["artifacts"][fname] = None
    return ctx


# === block: score_0 (check id='site_preference') ===
def score_0(artifact, step, ctx):
    checks = step.get("checks", [])
    if not checks:
        return 1.0
    total = 0
    for check in checks:
        field = check["field"]
        parts = field.split(".")
        val = artifact
        for p in parts:
            if isinstance(val, dict) and p in val:
                val = val[p]
            else:
                val = None
                break
        if val is None:
            continue
        if check.get("exact"):
            total += 1 if val == check["value"] else 0
        else:
            total += 1 if abs(val - check["value"]) <= check["tolerance"] else 0
    return total / len(checks)


# === block: score_1 (check id='elastic_constants') ===
def score_1(artifact, step, ctx):
    compositions = step.get("compositions", {})
    tolerances = step.get("tolerances", {})
    if not compositions:
        return 0.0
    fields = ["C11_GPa", "C12_GPa", "C44_GPa", "B_GPa", "G_GPa", "E_GPa", "nu", "A_Z"]
    total_fields = 0
    passed = 0
    for comp, gold in compositions.items():
        art_comp = artifact.get(comp)
        if not isinstance(art_comp, dict):
            continue
        for field in fields:
            gold_val = gold.get(field)
            if gold_val is None:
                continue
            art_val = art_comp.get(field)
            if art_val is None:
                continue
            tol = tolerances.get(field, 5.0)
            if field in ("nu", "A_Z"):
                tol = tolerances.get(field, 0.01 if field == "nu" else 0.1)
            if abs(art_val - gold_val) <= tol:
                passed += 1
            total_fields += 1
    return passed / total_fields if total_fields > 0 else 0.0


# === block: score_2 (check id='electron_density') ===
def score_2(artifact, step, ctx):
    elastic = ctx["artifacts"].get("elastic_constants.json")
    if elastic is None:
        return 0.0
    comps = ["pure_RuAl", "Ru8Al7Ti", "Ru7Al8Ni", "Ru8Al7W"]
    cross_ok = 0
    n_vals = []
    b_vals = []
    for comp in comps:
        art_comp = artifact.get(comp)
        if art_comp is None:
            continue
        art_n = art_comp.get("electron_density_el_per_atom")
        art_b = art_comp.get("bulk_modulus_GPa")
        if art_n is None or art_b is None:
            continue
        if elastic.get(comp) and elastic[comp].get("B_GPa") is not None:
            if abs(art_b - elastic[comp]["B_GPa"]) <= 0.1:
                cross_ok += 1
        n_vals.append(art_n)
        b_vals.append(art_b)
    if len(n_vals) < 2:
        return 0.0
    def rankdata(x):
        argsort = sorted(range(len(x)), key=lambda i: x[i])
        ranks = [0]*len(x)
        for rank, idx in enumerate(argsort, start=1):
            ranks[idx] = rank
        return ranks
    n_rank = rankdata(n_vals)
    b_rank = rankdata(b_vals)
    n_mean = sum(n_rank)/len(n_rank)
    b_mean = sum(b_rank)/len(b_rank)
    num = sum((nr - n_mean) * (br - b_mean) for nr, br in zip(n_rank, b_rank))
    den = math.sqrt(sum((nr - n_mean)**2 for nr in n_rank) * sum((br - b_mean)**2 for br in b_rank))
    spearman = num / den if den != 0 else 0.0
    spearman_min = step.get("spearman_min", 0.8)
    if spearman >= spearman_min:
        corr_score = 1.0
    elif spearman > spearman_min - 0.2:
        corr_score = (spearman - (spearman_min - 0.2)) / 0.2
    else:
        corr_score = 0.0
    cross_score = cross_ok / len(comps) if comps else 0.0
    return 0.2 * cross_score + 0.8 * corr_score


_SCORERS = {
    'site_preference': score_0,
    'elastic_constants': score_1,
    'electron_density': score_2,
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
