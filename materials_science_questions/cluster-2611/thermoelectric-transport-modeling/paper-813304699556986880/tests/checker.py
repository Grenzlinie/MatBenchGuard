import os
import json
import csv

# === author imports / helpers ===
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
    return {}


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    rows = artifact
    gold = step.get("gold_values", {})
    if not rows:
        return 0.0
    row_scores = []
    for row in rows:
        sample = str(row.get("sample", "")).strip()
        if sample not in gold:
            continue
        g = gold[sample]
        try:
            ef = float(row["Ef_eV"])
            lam = float(row["lambda"])
            n_cm3 = float(row["n_cm3"])
            mu_val = float(row["mu_cm2Vs"])
            Pf = float(row["P_uW_K2m"])
            # handle possible null strings
        except (KeyError, ValueError, TypeError):
            return 0.0
        # Ef absolute tolerance
        ef_gold = g["Ef_eV"]
        ef_err = abs(ef - ef_gold)
        if ef_err <= 0.05:
            sef = 1.0
        else:
            sef = max(0.0, 1.0 - (ef_err - 0.05) / 0.2)
        # lambda relative tolerance
        lam_gold = g["lambda"]
        lam_rel = abs(lam - lam_gold) / abs(lam_gold)
        if lam_rel <= 0.10:
            slam = 1.0
        else:
            slam = max(0.0, 1.0 - (lam_rel - 0.10) / 0.4)
        # n_cm3 relative
        n_gold = g["n_cm3"]
        n_rel = abs(n_cm3 - n_gold) / abs(n_gold)
        if n_rel <= 0.10:
            sn = 1.0
        else:
            sn = max(0.0, 1.0 - (n_rel - 0.10) / 0.4)
        # mu_cm2Vs relative
        mu_gold = g["mu_cm2Vs"]
        mu_rel = abs(mu_val - mu_gold) / abs(mu_gold)
        if mu_rel <= 0.10:
            smu = 1.0
        else:
            smu = max(0.0, 1.0 - (mu_rel - 0.10) / 0.4)
        # P_uW_K2m relative
        pf_gold = g["P_uW_K2m"]
        pf_rel = abs(Pf - pf_gold) / abs(pf_gold)
        if pf_rel <= 0.10:
            spf = 1.0
        else:
            spf = max(0.0, 1.0 - (pf_rel - 0.10) / 0.4)
        row_score = (sef + slam + sn + smu + spf) / 5.0
        row_scores.append(row_score)
    if not row_scores:
        return 0.0
    return sum(row_scores) / len(row_scores)


_SCORERS = {
    'step_01': score_0,
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
