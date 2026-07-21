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


# === block: score_0 (check id='structural_relationships') ===
def score_0(artifact, step, ctx):
    d = artifact  # already a dict
    # 1. range check
    fractions = [
        d['AuPd_monomer_fraction_theta015_T300'],
        d['AuPd_dimer_fraction_theta015_T300'],
        d['AuPt_monomer_fraction_theta015_T300'],
        d['AuPt_dimer_fraction_theta015_T300'],
    ]
    alphas = [
        d['AuPd_short_range_order_1NN_theta01_T300'],
        d['AuPd_short_range_order_2NN_theta01_T300'],
        d['AuPd_short_range_order_3NN_theta01_T300'],
    ]
    if any(not (0.0 <= f <= 1.0) for f in fractions) or any(not (-1.0 <= a <= 1.0) for a in alphas):
        return 0.0

    # 2. random baseline exact values
    theta = 0.15
    exact_mon = (1.0 - theta)**4
    exact_dim = 4.0 * theta * (1.0 - theta)**6
    tol = 1e-12
    rand_ok = (
        abs(d['random_monomer_fraction_theta015'] - exact_mon) < tol and
        abs(d['random_dimer_fraction_theta015'] - exact_dim) < tol
    )
    rand_score = 1.0 if rand_ok else 0.0

    # 3. structural relationships
    mon_rand = exact_mon
    dim_rand = exact_dim

    # AuPd
    apd_mon = d['AuPd_monomer_fraction_theta015_T300']
    apd_dim = d['AuPd_dimer_fraction_theta015_T300']
    check_apd = [apd_mon > mon_rand, apd_dim < dim_rand]

    # AuPt
    apt_mon = d['AuPt_monomer_fraction_theta015_T300']
    apt_dim = d['AuPt_dimer_fraction_theta015_T300']
    check_apt = [apt_mon < mon_rand, apt_dim < dim_rand]

    # SRO
    alpha1 = d['AuPd_short_range_order_1NN_theta01_T300']
    alpha2 = d['AuPd_short_range_order_2NN_theta01_T300']
    alpha3 = d['AuPd_short_range_order_3NN_theta01_T300']
    check_sro = [alpha1 < 0.0, alpha2 > 0.0, abs(alpha3) <= 0.05]

    all_structural = check_apd + check_apt + check_sro
    struct_score = sum(all_structural) / len(all_structural)

    # 4. combine (0.4 random exact, 0.6 structural)
    final = 0.4 * rand_score + 0.6 * struct_score
    return final


_SCORERS = {
    'structural_relationships': score_0,
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
