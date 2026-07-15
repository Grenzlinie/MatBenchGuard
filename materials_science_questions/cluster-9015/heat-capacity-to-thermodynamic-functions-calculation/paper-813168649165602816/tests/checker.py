import os
import json
import csv

# === author imports / helpers ===
import csv
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
    # Heat capacity functions (kJ K-1 kg-1)
    def cp_low(T):
        return 1.025 - 0.247e-3 * T + 0.395e-6 * T**2 - 11550 * T**(-2)

    def cp_high(T):
        return 1.689

    def cp_liq(T):
        return 1.187

    # Integration step
    dT = 0.01

    # Temperature points to evaluate (exact order expected in CSV)
    T_points = [
        298, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400,
        1424, 1424, 1500, 1600, 1695, 1695, 1700, 1800, 1900
    ]

    H_ref = []
    S_ref = []

    # Integration helper
    current_T = 298.0
    H = 0.0
    S = 0.0

    # Start with low-temperature cp function
    cp_func = cp_low

    # Process each point in order
    for i, point in enumerate(T_points):
        if point == 1424 and i == 12:
            # integrate to 1424 (pre-transition)
            while current_T < point - 1e-6:
                T_mid = current_T + dT / 2.0
                cp_val = cp_low(T_mid)
                H += cp_val * dT
                S += cp_val * dT / T_mid
                current_T += dT
            H_ref.append(H)
            S_ref.append(S)
            # add transition
            H += 13.2
            S += 13.2 / 1424.0
            # switch to high-temperature solid
            cp_func = cp_high
        elif point == 1424 and i == 13:
            # post-transition value already stored after adding transition; just record
            H_ref.append(H)
            S_ref.append(S)
            # continue with cp_high until next discontinuity
            cp_func = cp_high
        elif point == 1695 and i == 16:
            # integrate from current_T to 1695 (pre-fusion)
            while current_T < point - 1e-6:
                T_mid = current_T + dT / 2.0
                cp_val = cp_func(T_mid)
                H += cp_val * dT
                S += cp_val * dT / T_mid
                current_T += dT
            H_ref.append(H)
            S_ref.append(S)
            # add fusion
            H += 393.0
            S += 393.0 / 1695.0
            cp_func = cp_liq
        elif point == 1695 and i == 17:
            # post-fusion value
            H_ref.append(H)
            S_ref.append(S)
        else:
            # integrate from current_T to requested point
            while current_T < point - 1e-6:
                T_mid = current_T + dT / 2.0
                cp_val = cp_func(T_mid)
                H += cp_val * dT
                S += cp_val * dT / T_mid
                current_T += dT
            H_ref.append(H)
            S_ref.append(S)

    return {'T_points': T_points, 'H_ref': H_ref, 'S_ref': S_ref}


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    tol_H = step.get('tolerances', {}).get('enthalpy_relative', 0.01)
    tol_S = step.get('tolerances', {}).get('entropy_relative', 0.005)
    ref_T = ctx.get('T_points', [])
    ref_H = ctx.get('H_ref', [])
    ref_S = ctx.get('S_ref', [])
    if not ref_T or not artifact:
        return 0.0
    passing = 0
    for i, row in enumerate(artifact):
        try:
            T_agent = float(row.get('T', float('nan')))
            H_agent = float(row.get('enthalpy_increment', float('nan')))
            S_agent = float(row.get('entropy_increment', float('nan')))
        except (ValueError, TypeError):
            continue
        if i >= len(ref_T) or abs(T_agent - ref_T[i]) > 0.5:
            continue
        H_ref_val = ref_H[i]
        S_ref_val = ref_S[i]
        rel_H = abs(H_agent - H_ref_val) / max(abs(H_ref_val), 1e-6)
        rel_S = abs(S_agent - S_ref_val) / max(abs(S_ref_val), 1e-6)
        if rel_H <= tol_H and rel_S <= tol_S:
            passing += 1
    return passing / len(ref_T)


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
