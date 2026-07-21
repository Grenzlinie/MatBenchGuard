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


# === block: score_0 (check id='step_01_check') ===
def score_0(artifact, step, ctx):
        import math, json, os
        artifact_path = os.path.join('/app/outputs', step.get('output_file', ''))
        props = load_artifact(artifact_path)
        if props is None:
            return 0.0
        try:
            T = float(props.get('T'))
            Tc = float(props.get('Tc'))
            alpha = float(props.get('alpha'))
            b = float(props.get('b'))
            c1 = float(props.get('c1'))
        except (TypeError, KeyError):
            return 0.0
        if Tc <= T:
            return 0.0
        # recompute static quantities
        eta_recom = math.sqrt(b / (alpha * (Tc - T)))
        d_recom = math.sqrt(2 * c1 / (b * eta_recom**2))
        omega_perp_sq_recom = 2 * alpha * (Tc - T)
        # reported values
        eta_rep = float(props.get('eta', 0))
        d_rep = float(props.get('d', 0))
        omega_rep = float(props.get('omega_perp_sq', 0))
        tol = 1e-4
        rel_err_eta = abs(eta_rep - eta_recom) / max(abs(eta_recom), 1e-15)
        rel_err_d = abs(d_rep - d_recom) / max(abs(d_recom), 1e-15)
        rel_err_omega = abs(omega_rep - omega_perp_sq_recom) / max(abs(omega_perp_sq_recom), 1e-15)
        score = 1.0
        if rel_err_eta > tol:
            score -= 0.33
        if rel_err_d > tol:
            score -= 0.33
        if rel_err_omega > tol:
            score -= 0.34
        return max(0.0, score)


# === block: score_1 (check id='step_02_check') ===
def score_1(artifact, step, ctx):
        import math, json, os
        # load parameters from step_01
        props_path = os.path.join('/app/outputs', 'domain_wall_properties.json')
        props = load_artifact(props_path)
        if props is None:
            return 0.0
        try:
            T = float(props.get('T'))
            Tc = float(props.get('Tc'))
            alpha = float(props.get('alpha'))
            b = float(props.get('b'))
            c1 = float(props.get('c1'))
            M = float(props.get('M'))
        except (TypeError, KeyError):
            return 0.0
        if Tc <= T:
            return 0.0
        eta_recom = math.sqrt(b / (alpha * (Tc - T)))
        d_recom = math.sqrt(2 * c1 / (b * eta_recom**2))
        omega_perp_sq_recom = 2 * alpha * (Tc - T)
        # recompute localized frequencies
        omega_x1_sq_recom = omega_perp_sq_recom - c1 / (M * d_recom**2)
        omega_x2_sq_recom = omega_perp_sq_recom - 4 * c1 / (M * d_recom**2)
        # load step_02 artifact
        artifact_path = os.path.join('/app/outputs', step.get('output_file', ''))
        freqs = load_artifact(artifact_path)
        if freqs is None:
            return 0.0
        try:
            omega_x1_rep = float(freqs.get('omega_x1_sq'))
            omega_x2_rep = float(freqs.get('omega_x2_sq'))
            omega_perp_rep = float(freqs.get('omega_perp_sq'))
            gap_sq_rep = float(freqs.get('gap_sq'))
        except (TypeError, KeyError):
            return 0.0
        tol = 1e-6
        score_consist = 0.0
        mx = max(abs(omega_x1_sq_recom), 1e-15)
        if abs(omega_x1_rep - omega_x1_sq_recom) / mx <= tol:
            score_consist += 0.2
        mx = max(abs(omega_x2_sq_recom), 1e-15)
        if abs(omega_x2_rep - omega_x2_sq_recom) / mx <= tol:
            score_consist += 0.2
        mx = max(abs(omega_perp_sq_recom), 1e-15)
        if abs(omega_perp_rep - omega_perp_sq_recom) / mx <= tol:
            score_consist += 0.1
        # gap_sq consistency
        gap_recom = math.sqrt(omega_perp_sq_recom) - math.sqrt(omega_x1_sq_recom)
        gap_sq_recom = gap_recom ** 2
        mx = max(abs(gap_sq_recom), 1e-15)
        if abs(gap_sq_rep - gap_sq_recom) / mx <= tol:
            score_consist += 0.1
        # ordering & positivity
        if omega_x1_sq_recom > 0 and omega_x2_sq_recom > 0 and omega_x1_sq_recom > omega_x2_sq_recom:
            score_consist += 0.1
        # gap magnitude check
        if 1e10 <= gap_recom <= 1e11:
            gap_score = 0.3
        elif 5e9 <= gap_recom <= 2e11:
            gap_score = 0.15
        else:
            gap_score = 0.0
        return min(1.0, score_consist + gap_score)


_SCORERS = {
    'step_01_check': score_0,
    'step_02_check': score_1,
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
