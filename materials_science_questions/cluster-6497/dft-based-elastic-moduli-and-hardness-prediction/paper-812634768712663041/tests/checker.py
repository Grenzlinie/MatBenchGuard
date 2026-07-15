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


# === block: score_0 (check id='step_01_map') ===
def score_0(artifact, step, ctx):
    def compute_energy_AB(D_A, D_B, sigma_A, sigma_B, sigma_AB, eps_AA, eps_BB, eps_AB):
        return (sigma_A + sigma_B + sigma_AB
                - eps_AB / (D_A + D_B) ** 2
                + (eps_AB - eps_AA) / (D_A ** 2)
                + (eps_AB - eps_BB) / (D_B ** 2))

    def compute_energy_ABA(D_A, D_B, sigma_A, sigma_B, sigma_AB, eps_AA, eps_BB, eps_AB):
        D_A1 = D_A / 2.0
        D_A2 = D_A / 2.0
        term1 = - eps_AA / ((D_A + D_B) ** 2)
        bracket = (-1.0 / (D_A1 ** 2) - 1.0 / (D_A2 ** 2) + 1.0 / ((D_A1 + D_B) ** 2) + 1.0 / ((D_A2 + D_B) ** 2))
        term2 = - (eps_AB - eps_AA) * bracket
        term3 = (2 * eps_AB - eps_AA - eps_BB) / (D_B ** 2)
        return 2 * sigma_A + 2 * sigma_AB + term1 + term2 + term3

    try:
        map_data = artifact.get('stability_map', [])
        if not isinstance(map_data, list) or len(map_data) == 0:
            return 0.0
        sigma_A=0.626; sigma_B=0.647; sigma_AB=0.016
        eps_AA=0.33; eps_BB=0.053; eps_AB=0.042
        correct = 0
        for point in map_data:
            D_A = float(point['D_A']); D_B = float(point['D_B'])
            E_AB = compute_energy_AB(D_A, D_B, sigma_A, sigma_B, sigma_AB, eps_AA, eps_BB, eps_AB)
            E_ABA = compute_energy_ABA(D_A, D_B, sigma_A, sigma_B, sigma_AB, eps_AA, eps_BB, eps_AB)
            pred = 'AB' if E_AB <= E_ABA else 'ABA'
            if point.get('structure', '') == pred:
                correct += 1
        return correct / len(map_data)
    except:
        return 0.0


# === block: score_1 (check id='step_01_threshold') ===
def score_1(artifact, step, ctx):
    try:
        thresh = artifact.get('transition_threshold', {})
        if not isinstance(thresh, dict):
            return 0.0
        # Correct analytic transition threshold from Eq. (8): D_A^2 = 7*(eps_AB - eps_AA) / (sigma_B - sigma_A - sigma_AB)
        gold = 7.0 * (0.042 - 0.33) / (0.647 - 0.626 - 0.016)  # approx -403.2
        comp = float(thresh.get('computed_D_A_sq', 0.0))
        rel_err = abs(comp - gold) / max(abs(gold), 1e-12)
        num_score = max(0.0, 1.0 - rel_err / 0.01)
        formula = str(thresh.get('formula_D_A_sq', ''))
        str_score = 1.0 if (formula and 'D_A' in formula and ('eps' in formula or 'epsilon' in formula)) else 0.0
        return num_score * 0.7 + str_score * 0.3
    except:
        return 0.0


_SCORERS = {
    'step_01_map': score_0,
    'step_01_threshold': score_1,
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
