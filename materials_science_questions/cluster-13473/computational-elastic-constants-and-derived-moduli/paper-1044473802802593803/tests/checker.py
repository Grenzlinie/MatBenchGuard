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
    gold_list = spec["gold_moduli"]
    tolerances = spec["tolerances"]
    gold_by_strain = {float(g["strain_percent"]): g for g in gold_list}
    low_strains = sorted([s for s in gold_by_strain if s <= 1.0])
    high_strains = sorted([s for s in gold_by_strain if s >= 1.75])
    return {
        "gold_by_strain": gold_by_strain,
        "tolerances": tolerances,
        "low_strains": low_strains,
        "high_strains": high_strains,
    }


# === block: score_0 (check id='csv_shape') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) != 10:
        return 0.0
    required = {"strain_percent", "bulk_modulus_mean", "bulk_modulus_std", "shear_modulus_mean", "shear_modulus_std", "youngs_modulus_mean", "youngs_modulus_std", "poisson_ratio_mean", "poisson_ratio_std"}
    cols = set(artifact[0].keys()) if artifact else set()
    if not required.issubset(cols):
        return 0.0
    expected_strains = [0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5]
    strains = [float(r["strain_percent"]) for r in artifact]
    if strains != expected_strains:
        return 0.0
    # Reject trivial constant-value submissions: all means equal across rows
    mean_keys = ["bulk_modulus_mean", "shear_modulus_mean", "youngs_modulus_mean", "poisson_ratio_mean"]
    for key in mean_keys:
        vals = [float(r[key]) for r in artifact]
        if len(set(vals)) == 1:
            return 0.0
    # All standard deviations must be positive
    std_keys = ["bulk_modulus_std", "shear_modulus_std", "youngs_modulus_std", "poisson_ratio_std"]
    for row in artifact:
        for key in std_keys:
            if float(row.get(key, -1)) <= 0:
                return 0.0
    # Structural trend: K, G, E should decrease with strain (mean of first three strains > mean of last three)
    def mean(lst):
        return sum(lst)/len(lst) if lst else 0.0
    for key in ["bulk_modulus_mean", "shear_modulus_mean", "youngs_modulus_mean"]:
        vals = [float(r[key]) for r in artifact]
        if mean(vals[:3]) <= mean(vals[-3:]):
            return 0.0
    # Poisson ratio should also show a slight decrease
    poisson_vals = [float(r["poisson_ratio_mean"]) for r in artifact]
    if mean(poisson_vals[:3]) <= mean(poisson_vals[-3:]):
        return 0.0
    return 1.0


# === block: score_1 (check id='bulk_mean_match') ===
def score_1(artifact, step, ctx):
    gold_by_strain = ctx["gold_by_strain"]
    tol = ctx["tolerances"]["bulk_tol"]
    score = 0
    for row in artifact:
        strain = float(row.get("strain_percent", -1))
        if strain in gold_by_strain:
            diff = abs(float(row["bulk_modulus_mean"]) - gold_by_strain[strain]["bulk_mean"])
            if diff <= tol:
                score += 1
    return score / 10.0


# === block: score_2 (check id='shear_mean_match') ===
def score_2(artifact, step, ctx):
    gold_by_strain = ctx["gold_by_strain"]
    tol = ctx["tolerances"]["shear_tol"]
    score = 0
    for row in artifact:
        strain = float(row.get("strain_percent", -1))
        if strain in gold_by_strain:
            diff = abs(float(row["shear_modulus_mean"]) - gold_by_strain[strain]["shear_mean"])
            if diff <= tol:
                score += 1
    return score / 10.0


# === block: score_3 (check id='young_mean_match') ===
def score_3(artifact, step, ctx):
    gold_by_strain = ctx["gold_by_strain"]
    tol = ctx["tolerances"]["young_tol"]
    score = 0
    for row in artifact:
        strain = float(row.get("strain_percent", -1))
        if strain in gold_by_strain:
            diff = abs(float(row["youngs_modulus_mean"]) - gold_by_strain[strain]["young_mean"])
            if diff <= tol:
                score += 1
    return score / 10.0


# === block: score_4 (check id='poisson_mean_match') ===
def score_4(artifact, step, ctx):
    gold_by_strain = ctx["gold_by_strain"]
    tol = ctx["tolerances"]["poisson_tol"]
    score = 0
    for row in artifact:
        strain = float(row.get("strain_percent", -1))
        if strain in gold_by_strain:
            diff = abs(float(row["poisson_ratio_mean"]) - gold_by_strain[strain]["poisson_mean"])
            if diff <= tol:
                score += 1
    return score / 10.0


# === block: score_5 (check id='trend_and_std') ===
def score_5(artifact, step, ctx):
    gold_by_strain = ctx["gold_by_strain"]
    low_strains = ctx["low_strains"]
    high_strains = ctx["high_strains"]
    rows_by_strain = {float(r["strain_percent"]): r for r in artifact}
    def avg(key, strain_list):
        vals = [float(rows_by_strain[s][key]) for s in strain_list if s in rows_by_strain]
        if not vals:
            return 0.0
        return sum(vals)/len(vals)
    modulus_keys = [("bulk_modulus_mean", "bulk_mean"), ("shear_modulus_mean", "shear_mean"), ("youngs_modulus_mean", "young_mean"), ("poisson_ratio_mean", "poisson_mean")]
    trend_ok = 0
    for art_key, _ in modulus_keys:
        low_avg = avg(art_key, low_strains)
        high_avg = avg(art_key, high_strains)
        if high_avg > 0 and low_avg / high_avg > 1.01:
            trend_ok += 1
    std_keys = ["bulk_modulus_std", "shear_modulus_std", "youngs_modulus_std", "poisson_ratio_std"]
    pos = 0
    total_std = 0
    for row in artifact:
        for sk in std_keys:
            val = float(row.get(sk, -1))
            if val > 0:
                pos += 1
            total_std += 1
    score = 0.9 * (trend_ok / 4.0) + 0.1 * (pos / max(1, total_std))
    return score


_SCORERS = {
    'csv_shape': score_0,
    'bulk_mean_match': score_1,
    'shear_mean_match': score_2,
    'young_mean_match': score_3,
    'poisson_mean_match': score_4,
    'trend_and_std': score_5,
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
