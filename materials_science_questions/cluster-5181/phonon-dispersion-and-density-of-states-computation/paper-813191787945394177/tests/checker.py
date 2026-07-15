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


# === block: score_0 (check id='check_structural_params') ===
def score_0(artifact, step, ctx):
        tol_a = step.get('tol_a', 0.01)
        gold_a = step.get('gold_a', 3.691)
        ionic_a = step.get('ionic_a', 3.978)
        a = artifact.get('a')
        if a is None or not isinstance(a, (int, float)):
            return 0.0
        score_a = 0.0
        if a < ionic_a:
            err = abs(a - gold_a)
            score_a = max(0.0, 1.0 - err / tol_a) if tol_a > 0 else 0.0
        else:
            score_a = 0.0
        tol_c = step.get('tol_c_over_a', 0.01)
        gold_c = step.get('gold_c_over_a', 3.376)
        c = artifact.get('c_over_a')
        if c is None:
            return 0.0
        err_c = abs(c - gold_c)
        score_c = max(0.0, 1.0 - err_c / tol_c) if tol_c > 0 else 0.0
        tol_oz = step.get('tol_z_Oz', 0.002)
        gold_oz = step.get('gold_z_Oz', 0.189)
        oz = artifact.get('z_Oz')
        if oz is None:
            return 0.0
        err_oz = abs(oz - gold_oz)
        score_oz = max(0.0, 1.0 - err_oz / tol_oz) if tol_oz > 0 else 0.0
        tol_la = step.get('tol_z_La', 0.002)
        gold_la = step.get('gold_z_La', 0.362)
        la = artifact.get('z_La')
        if la is None:
            return 0.0
        err_la = abs(la - gold_la)
        score_la = max(0.0, 1.0 - err_la / tol_la) if tol_la > 0 else 0.0
        return (score_a + score_c + score_oz + score_la) / 4.0


# === block: score_1 (check id='check_mode_stabilities') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        e1 = artifact.get('E_u_mode_1_frequency_THz')
        e2 = artifact.get('E_u_mode_2_frequency_THz')
        eg = artifact.get('E_g_mode_frequency_THz')
        if any(v is None for v in [e1, e2, eg]):
            return 0.0
        pos_count = sum(1 for v in [e1, e2, eg] if v > 0)
        return pos_count / 3.0


_SCORERS = {
    'check_structural_params': score_0,
    'check_mode_stabilities': score_1,
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
