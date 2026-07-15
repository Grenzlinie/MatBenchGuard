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
    ctx = {}
    for step in spec.get("steps", []):
        if step.get("id") == "formation_energy_tolerance":
            ctx["gold_E_F"] = step["gold_E_F"]
        elif step.get("id") == "magnetic_moment_tolerance":
            ctx["gold_mu_Cr"] = step["gold_mu_Cr"]
    return ctx


# === block: score_0 (check id='internal_consistency') ===
def score_0(artifact, step, ctx):
    tolerance = step.get("tolerance_ef_consistency", 1e-4)
    rows = artifact
    if not rows:
        return 0.0
    passed = 0
    for row in rows:
        try:
            ef = float(row["E_F"])
            ec = float(row["E_CrSi12"])
            es = float(row["E_Si111"])
            et = float(row["E_T"])
            expected = ec + es - et
            if abs(ef - expected) <= tolerance:
                passed += 1
        except (ValueError, KeyError):
            continue
    return passed / max(len(rows), 1)


# === block: score_1 (check id='formation_energy_tolerance') ===
def score_1(artifact, step, ctx):
    tolerance = step.get("tolerance_E_F", 0.2)
    gold = ctx.get("gold_E_F", {})
    rows = artifact
    if not rows:
        return 0.0
    passed = 0
    for row in rows:
        config = row.get("Configuration", "").strip()
        if config not in gold:
            continue
        try:
            ef = float(row["E_F"])
            if abs(ef - gold[config]) <= tolerance:
                passed += 1
        except (ValueError, KeyError):
            continue
    return min(1.0, passed / len(gold))


# === block: score_2 (check id='magnetic_moment_tolerance') ===
def score_2(artifact, step, ctx):
    tolerance = step.get("tolerance_mu_Cr", 0.1)
    gold = ctx.get("gold_mu_Cr", {})
    rows = artifact
    if not rows:
        return 0.0
    passed = 0
    for row in rows:
        config = row.get("Configuration", "").strip()
        if config not in gold:
            continue
        try:
            mu = float(row["mu_Cr"])
            if abs(mu - gold[config]) <= tolerance:
                passed += 1
        except (ValueError, KeyError):
            continue
    return min(1.0, passed / len(gold))


# === block: score_3 (check id='energy_ordering') ===
def score_3(artifact, step, ctx):
    expected_order = step.get("expected_ordering", ["I","II","III","IV"])
    rows = artifact
    ef_dict = {}
    for row in rows:
        config = row.get("Configuration", "").strip()
        try:
            ef = float(row["E_F"])
            ef_dict[config] = ef
        except (ValueError, KeyError):
            pass
    if len(expected_order) < 2:
        return 1.0 if len(ef_dict) >= 1 else 0.0
    correct_pairs = 0
    total_pairs = len(expected_order) - 1
    for i in range(total_pairs):
        a = expected_order[i]
        b = expected_order[i+1]
        if a in ef_dict and b in ef_dict:
            if ef_dict[a] >= ef_dict[b]:
                correct_pairs += 1
    score = correct_pairs / total_pairs if total_pairs > 0 else 1.0
    return score


_SCORERS = {
    'internal_consistency': score_0,
    'formation_energy_tolerance': score_1,
    'magnetic_moment_tolerance': score_2,
    'energy_ordering': score_3,
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
