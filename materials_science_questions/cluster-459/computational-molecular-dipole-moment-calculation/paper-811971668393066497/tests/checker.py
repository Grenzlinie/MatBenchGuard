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


# === block: score_0 (check id='shape_check') ===
def score_0(artifact, step, ctx):
    systems = artifact.get("systems", [])
    expected = ["O2+H2", "O2+C2H4", "O2+C2H4+H2_model_I", "O2+C2H4+H2_model_II"]
    found = {s["name"] for s in systems}
    if not all(e in found for e in expected):
        return 0.0
    # minimal R presence check
    for s in systems:
        if not isinstance(s.get("R_values"), list) or len(s["R_values"]) == 0:
            return 0.0
    return 1.0


# === block: score_1 (check id='self_consistency') ===
def score_1(artifact, step, ctx):
    systems = artifact.get("systems", [])
    tol = 0.01
    entries = []
    for sys in systems:
        if sys["name"] not in ("O2+C2H4+H2_model_I", "O2+C2H4+H2_model_II"):
            continue
        for rv in sys.get("R_values", []):
            if "M_ba_SCF" in rv and "M_ba_CI" in rv and "M_ba_tot" in rv:
                scf, ci, tot = rv["M_ba_SCF"], rv["M_ba_CI"], rv["M_ba_tot"]
                denom = max(abs(tot), 1e-6)
                rel = abs(tot - (scf + ci)) / denom
                entries.append(rel)
    if not entries:
        return 0.0
    pass_count = sum(1 for e in entries if e <= tol)
    return pass_count / len(entries)


# === block: score_2 (check id='model_I_enhancement') ===
def score_2(artifact, step, ctx):
    systems = {s["name"]: s for s in artifact.get("systems", [])}
    required_R = [3.8, 3.4, 4.0]
    model_I = systems.get("O2+C2H4+H2_model_I")
    binary_H2 = systems.get("O2+H2")
    binary_C2H4 = systems.get("O2+C2H4")
    if not model_I or not binary_H2 or not binary_C2H4:
        return 0.0
    def get_M_ba(sys):
        return {rv["R"]: rv["M_ba"] for rv in sys.get("R_values", []) if "M_ba" in rv}
    H2_ba = get_M_ba(binary_H2)
    C2H4_ba = get_M_ba(binary_C2H4)
    I_ba = {rv["R"]: rv.get("M_ba_tot") for rv in model_I.get("R_values", []) if "M_ba_tot" in rv}
    passed = 0
    for R in required_R:
        if R not in I_ba or R not in H2_ba or R not in C2H4_ba:
            continue
        if I_ba[R] is None:
            continue
        max_bin = max(H2_ba[R], C2H4_ba[R])
        if I_ba[R] > 1.1 * max_bin:
            passed += 1
    return passed / len(required_R) if required_R else 0.0


# === block: score_3 (check id='model_II_suppression') ===
def score_3(artifact, step, ctx):
    systems = {s["name"]: s for s in artifact.get("systems", [])}
    required_R = [3.6, 3.4, 3.0]
    model_II = systems.get("O2+C2H4+H2_model_II")
    binary_H2 = systems.get("O2+H2")
    binary_C2H4 = systems.get("O2+C2H4")
    if not model_II or not binary_H2 or not binary_C2H4:
        return 0.0
    def get_M_ba(sys):
        return {rv["R"]: rv["M_ba"] for rv in sys.get("R_values", []) if "M_ba" in rv}
    H2_ba = get_M_ba(binary_H2)
    C2H4_ba = get_M_ba(binary_C2H4)
    II_ba = {rv["R"]: rv.get("M_ba_tot") for rv in model_II.get("R_values", []) if "M_ba_tot" in rv}
    passed = 0
    for R in required_R:
        if R not in II_ba or R not in H2_ba or R not in C2H4_ba:
            continue
        if II_ba[R] is None:
            continue
        min_bin = min(H2_ba[R], C2H4_ba[R])
        if II_ba[R] < min_bin:
            passed += 1
    return passed / len(required_R) if required_R else 0.0


_SCORERS = {
    'shape_check': score_0,
    'self_consistency': score_1,
    'model_I_enhancement': score_2,
    'model_II_suppression': score_3,
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
