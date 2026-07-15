import os
import json
import csv

# === author imports / helpers ===
import math
import csv
import os


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


# === block: score_0 (check id='step_purdy') ===
def score_0(artifact, step, ctx):
        if not artifact:
            return 0.0
        required = ['V_Mn', 'Delta_G_dis']
        for col in required:
            if col not in artifact[0]:
                return 0.0
        rows = []
        for row in artifact:
            try:
                V = float(row['V_Mn'])
                dG = float(row['Delta_G_dis'])
            except (ValueError, TypeError):
                continue
            rows.append((V, dG))
        if len(rows) < 20:
            return 0.0

        # Reference recomputation always uses the hidden gold ΔE (paper-sourced).
        DeltaE_J = step['parameters']['DeltaE_J']

        C0_wt = step['parameters']['C0_wt']
        T_K = step['parameters']['T_K']
        R = step['parameters']['R']
        Emn = step['parameters']['Emn_J']
        delta = step['parameters']['delta_m']
        Dmn = step['parameters']['Dmn_m2s']
        mape_threshold = step['parameters']['mape_threshold']

        M_Fe = 55.845
        M_Mn = 54.938
        C0_at = (C0_wt / M_Mn) / (C0_wt / M_Mn + (100 - C0_wt) / M_Fe)

        def E_dE(xx):
            arg = (xx / delta) ** 2
            E = -Emn * math.exp(-arg)
            dE = 2 * xx / (delta ** 2) * Emn * math.exp(-arg)
            return E, dE

        L = 5.0 * delta
        N = 4000
        dx = 2 * L / (N - 1)
        xs = [-L + i * dx for i in range(N)]

        def compute_ref(V_Mn):
            v = V_Mn * Dmn / delta
            C = [0.0] * N
            C[0] = C0_at
            for i in range(1, N):
                xi = xs[i]
                _, dEi = E_dE(xi)
                dC = -(C[i-1] / (R * T_K)) * dEi - (v / Dmn) * (C[i-1] - C0_at)
                C[i] = C[i-1] + dC * dx
                if C[i] < 0.0: C[i] = 0.0
                if C[i] > 1.0: C[i] = 1.0
            integral = 0.0
            for i in range(N):
                _, dEi = E_dE(xs[i])
                integral += (C[i] - C0_at) * dEi * dx
            DeltaG_J_per_mol = -6.02214076e23 * integral
            DeltaG_kJ = DeltaG_J_per_mol / 1000.0
            if DeltaG_kJ < 0.0:
                DeltaG_kJ = 0.0
            return DeltaG_kJ

        rel_errs = []
        for V, dG_agent in rows:
            ref = compute_ref(V)
            if ref < 1e-12:
                if dG_agent < 1e-12:
                    rel_err = 0.0
                else:
                    rel_err = 1.0
            else:
                rel_err = abs(dG_agent - ref) / ref
            rel_errs.append(rel_err)
        mape = sum(rel_errs) / len(rel_errs) if rel_errs else 1.0

        mape_score = 1.0 if mape <= mape_threshold else max(0.0, 1.0 - (mape - mape_threshold) / mape_threshold)

        max_idx = max(range(len(rows)), key=lambda i: rows[i][1])
        V_peak = rows[max_idx][0]
        peak_val = rows[max_idx][1]
        if 0.5 <= V_peak <= 2.0:
            if len(rows) > 1:
                V_min_val = rows[0][1]
                V_max_val = rows[-1][1]
            else:
                V_min_val = V_max_val = peak_val
            if V_min_val < peak_val and V_max_val < peak_val:
                shape_ok = 1.0
            else:
                shape_ok = 0.5
        else:
            shape_ok = 0.5

        return 0.8 * mape_score + 0.2 * shape_ok


_SCORERS = {
    'step_purdy': score_0,
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
