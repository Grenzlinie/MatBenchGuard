import os
import json
import csv

# === author imports / helpers ===
import math, json


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


# === block: score_0 (check id='step_1') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    lattice_val = artifact.get("lattice_constant_nm")
    if lattice_val is None:
        return 0.0
    if not isinstance(lattice_val, (int, float)):
        return 0.0
    unit = artifact.get("unit")
    if unit != "nm":
        return 0.0
    gold = step["gold_lattice_nm"]
    tol = step["tolerance_nm"]
    diff = abs(lattice_val - gold)
    if diff <= tol:
        return 1.0
    else:
        return 0.0


# === block: score_1 (check id='step_4') ===
def score_1(artifact, step, ctx):
    energy = artifact.get("energy_eV")
    U_DOS = artifact.get("U_DOS")
    O_DOS = artifact.get("O_DOS")
    if not energy or not U_DOS or not O_DOS:
        return 0.0
    de = energy[1] - energy[0] if len(energy) > 1 else 0.0
    if de <= 0:
        return 0.0
    hbar_eVs = 6.582119569e-16
    eV_to_J = 1.602176634e-19
    kB_eV_K = 8.617333262e-5
    amu_to_kg = 1.660539e-27
    angstrom = 1e-10
    T = step["temperature"]
    m_U_kg = step["m_U_amu"] * amu_to_kg
    m_O_kg = step["m_O_amu"] * amu_to_kg
    factor_U = (hbar_eVs ** 2) / (6.0 * m_U_kg) / eV_to_J / (angstrom ** 2)
    factor_O = (hbar_eVs ** 2) / (6.0 * m_O_kg) / eV_to_J / (angstrom ** 2)
    kB_T = kB_eV_K * T
    int_U = 0.0
    int_O = 0.0
    for i in range(len(energy)):
        e = energy[i]
        if e <= 0:
            continue
        arg = e / (2.0 * kB_T)
        if arg > 20:
            coth_val = 1.0
        else:
            e2arg = math.exp(2.0 * arg)
            coth_val = (e2arg + 1.0) / (e2arg - 1.0)
        int_U += (U_DOS[i] / e) * coth_val * de
        int_O += (O_DOS[i] / e) * coth_val * de
    W_U = factor_U * int_U
    W_O = factor_O * int_O
    gold_U = step["gold_W_U"]
    gold_O = step["gold_W_O"]
    tol = step["tolerance_rel"]
    def score_W(W, gold):
        rel_err = abs(W - gold) / gold if gold > 0 else 0.0
        if rel_err <= tol:
            return 1.0
        else:
            return 0.0
    s_U = score_W(W_U, gold_U)
    s_O = score_W(W_O, gold_O)
    return 0.5 * (s_U + s_O)


_SCORERS = {
    'step_1': score_0,
    'step_4': score_1,
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
