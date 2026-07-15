import os
import json
import csv

# === author imports / helpers ===
import csv, math


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
    def prepare(output_dir, spec):
        return {}


# === block: score_0 (check id='dlith') ===
def score_0(artifact, step, ctx):
    if artifact is None or not isinstance(artifact, list):
        return 0.0
    try:
        pts = sorted([row for row in artifact if row.get('ThF4_mol_percent') is not None and row.get('D_LiTh_m2_per_s') is not None],
                     key=lambda r: float(r['ThF4_mol_percent']))
        if not pts:
            return 0.0
        m = [float(r['ThF4_mol_percent']) for r in pts]
        d = [float(r['D_LiTh_m2_per_s']) for r in pts]
        signs = [1 if v >= 0 else -1 for v in d]
        cross_count = 0
        for i in range(len(signs)-1):
            if signs[i] != signs[i+1]:
                cross_count += 1
        params = step.get('params', {})
        expected = params.get('expected_sign_changes', 5)
        count_score = max(0.0, 1.0 - abs(cross_count - expected) / 2.0)
        small_conc = params.get('small_concentration', 6.0)
        large_conc = params.get('large_concentration', 45.0)
        ratio_max = params.get('amplitude_ratio_max', 0.2)
        d_small = None
        d_large = None
        for mc, dc in zip(m, d):
            if abs(mc - small_conc) < 0.5:
                d_small = abs(dc)
            if abs(mc - large_conc) < 0.5:
                d_large = abs(dc)
        ratio_score = 1.0
        if d_small is not None and d_large is not None and d_small > 1e-12:
            ratio = d_large / d_small
            if ratio > ratio_max:
                ratio_score = max(0.0, 1.0 - (ratio - ratio_max))
        return (count_score + ratio_score) / 2.0
    except Exception:
        return 0.0


# === block: score_1 (check id='density_enthalpy') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        eutectic_mol = step.get('params', {}).get('eutectic_mol_pct', 22.0)
        target_rho = step.get('params', {}).get('target_density', 4.15)
        rho_tol = step.get('params', {}).get('density_tolerance', 0.15)
        target_h = step.get('params', {}).get('target_enthalpy', -27.85)
        h_tol = step.get('params', {}).get('enthalpy_tolerance', 1.0)
        best_row = None
        best_diff = float('inf')
        for row in artifact:
            diff = abs(float(row['ThF4_mol_percent']) - eutectic_mol)
            if diff < best_diff:
                best_diff = diff
                best_row = row
        rho_score = 0.0
        h_score = 0.0
        if best_row is not None:
            rho = float(best_row['density_g_per_cm3'])
            if abs(rho - target_rho) <= rho_tol:
                rho_score = 1.0
            else:
                rho_score = max(0.0, 1.0 - (abs(rho - target_rho) - rho_tol) / (0.1 * target_rho))
            enth = float(best_row['specific_enthalpy_kJ_per_g'])
            if abs(enth - target_h) <= h_tol:
                h_score = 1.0
            else:
                h_score = max(0.0, 1.0 - (abs(enth - target_h) - h_tol) / (0.1 * abs(target_h)))
        pts = sorted(artifact, key=lambda r: float(r['ThF4_mol_percent']))
        dens = [float(r['density_g_per_cm3']) for r in pts]
        enthalpies = [float(r['specific_enthalpy_kJ_per_g']) for r in pts]
        trend_rho = 1.0 if len(dens) >= 2 and dens[-1] > dens[0] + rho_tol else 0.0
        trend_h = 1.0 if len(enthalpies) >= 2 and enthalpies[-1] > enthalpies[0] + h_tol else 0.0
        return (rho_score + h_score + trend_rho + trend_h) / 4.0


_SCORERS = {
    'dlith': score_0,
    'density_enthalpy': score_1,
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
