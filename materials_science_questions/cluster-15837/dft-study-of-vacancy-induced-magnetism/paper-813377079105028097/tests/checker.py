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
    gold = {
        "single_vacancies": {
            "Bi2S3_V_Bi": {"mu_B": 1.5, "tol": 0.3},
            "Bi2S3_V_S": {"mu_B": 0.0, "tol": 0.2},
            "ZnS_V_Zn": {"mu_B": 1.1, "tol": 0.3},
            "ZnS_V_S": {"mu_B": 0.0, "tol": 0.2},
        },
        "two_vacancies": {
            "Bi2S3_V_Bi_Bi1_Bi2": {"mu_B": 3.01, "tol": 0.3},
            "Bi2S3_V_Bi_Bi1_Bi3": {"mu_B": 3.6, "tol": 0.3},
            "Bi2S3_V_Bi_Bi2_Bi3": {"mu_B": 4.29, "tol": 0.3},
            "ZnS_V_Zn_Zn1_Zn2": {"mu_B": 2.21, "tol": 0.3},
            "ZnS_V_Zn_Zn1_Zn3": {"mu_B": 2.62, "tol": 0.3},
            "ZnS_V_Zn_Zn1_Zn4": {"mu_B": 3.04, "tol": 0.3},
        },
        "single_interstitials": {
            "ZnS_Zn_i": {"mu_B": 0.582, "tol": 0.3},
            "Bi2S3_Bi_i": {"mu_B": 0.591, "tol": 0.3},
        }
    }
    return {"gold": gold}


# === block: score_0 (check id='defect_results') ===
def score_0(artifact, step, ctx):
        gold = ctx["gold"]
        total = 0
        correct = 0
        # single vacancies
        for entry in artifact.get("single_vacancies", []):
            sys = entry.get("system")
            if sys in gold["single_vacancies"]:
                total += 1
                mu = entry.get("mu_B")
                if isinstance(mu, (int, float)):
                    exp = gold["single_vacancies"][sys]
                    if abs(mu - exp["mu_B"]) <= exp["tol"]:
                        correct += 1
        # two vacancies
        for entry in artifact.get("two_vacancies", []):
            sys = entry.get("system")
            if sys in gold["two_vacancies"]:
                total += 2  # mu_B and FM_lower_than_AFM
                mu = entry.get("mu_B")
                fm = entry.get("FM_lower_than_AFM")
                exp = gold["two_vacancies"][sys]
                if isinstance(mu, (int, float)) and abs(mu - exp["mu_B"]) <= exp["tol"]:
                    correct += 1
                if isinstance(fm, bool) and fm == True:
                    correct += 1
        # single interstitials
        for entry in artifact.get("single_interstitials", []):
            sys = entry.get("system")
            if sys in gold["single_interstitials"]:
                total += 1
                mu = entry.get("mu_B")
                if isinstance(mu, (int, float)):
                    exp = gold["single_interstitials"][sys]
                    if abs(mu - exp["mu_B"]) <= exp["tol"]:
                        correct += 1
        if total == 0:
            return 0.0
        return correct / total


_SCORERS = {
    'defect_results': score_0,
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
