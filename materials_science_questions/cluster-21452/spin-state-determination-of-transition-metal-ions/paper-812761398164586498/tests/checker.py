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


# === block: score_0 (check id='step_relative_energies') ===
def score_0(artifact, step, ctx):
        artifact = artifact  # list
        step_config = step
        gold = step_config.get("gold", {})
        tolerance = float(step_config.get("tolerance_kcal", 2.0))
        hartree = float(step_config.get("hartree_to_kcal", 627.50947))

        if not isinstance(artifact, list):
            return 0.0

        # index agent entries by (complex, electromer)
        agent_idx = {}
        for entry in artifact:
            c = entry.get("complex")
            e = entry.get("electromer")
            if isinstance(c, str) and isinstance(e, str):
                agent_idx[(c, e)] = entry

        scores = []
        for comp, comp_gold in gold.items():
            ground_em = None
            for em, em_gold in comp_gold.get("electromers", {}).items():
                if em_gold.get("dE_kcal") == 0.0:
                    ground_em = em
                    break
            if ground_em is None:
                continue
            ground_entry = agent_idx.get((comp, ground_em))
            if ground_entry is None or ground_entry.get("E_au") is None:
                continue
            ground_e_au = float(ground_entry["E_au"])
            for em, em_gold in comp_gold.get("electromers", {}).items():
                entry = agent_idx.get((comp, em))
                if entry is None or entry.get("E_au") is None:
                    continue
                e_au = float(entry["E_au"])
                dE_calc = (e_au - ground_e_au) * hartree
                gold_dE = em_gold["dE_kcal"]
                diff = abs(dE_calc - gold_dE)
                s = max(0.0, 1.0 - diff / tolerance)
                scores.append(s)

        if not scores:
            return 0.0
        return sum(scores) / len(scores)


# === block: score_1 (check id='step_exchange_parameters') ===
def score_1(artifact, step, ctx):
        artifact = artifact  # dict
        step_config = step
        gold_j = step_config.get("gold_j", {})
        tol_ferro = float(step_config.get("tolerance_ferro", 100.0))
        tol_antiferro = float(step_config.get("tolerance_antiferro", 50.0))

        if not isinstance(artifact, dict):
            return 0.0

        scores = []
        for elec_key, expected in gold_j.items():
            submitted = artifact.get(elec_key)
            if not isinstance(submitted, dict):
                continue
            for j_name, gold_val in expected.items():
                agent_val = submitted.get(j_name)
                if not isinstance(agent_val, (int, float)):
                    continue
                tol = tol_ferro if gold_val > 0 else tol_antiferro
                diff = abs(agent_val - gold_val)
                s = max(0.0, 1.0 - diff / tol)
                scores.append(s)

        if not scores:
            return 0.0
        return sum(scores) / len(scores)


_SCORERS = {
    'step_relative_energies': score_0,
    'step_exchange_parameters': score_1,
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
