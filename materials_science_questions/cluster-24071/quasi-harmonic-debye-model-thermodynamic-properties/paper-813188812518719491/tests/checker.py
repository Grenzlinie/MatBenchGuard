import os
import json
import csv

# === author imports / helpers ===
import math
import json
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


# === block: score_0 (check id='check_poisson') ===
def score_0(artifact, step, ctx):
        t = step.get('targets', {})
        nu_t = t.get('nu')
        BH_t = t.get('B_H')
        GH_t = t.get('G_H')
        tol_nu = t.get('tolerance_nu', 0.005)
        tol_mod = t.get('tolerance_moduli', 15.0)
        try:
            nu = float(artifact.get('nu'))
            BH = float(artifact.get('B_H'))
            GH = float(artifact.get('G_H'))
        except (TypeError, ValueError):
            return 0.0
        # check self-consistency: nu computed from B_H, G_H using formula
        denom = 2 * (3 * BH + GH)
        if denom == 0:
            return 0.0
        expected_nu = (3 * BH - 2 * GH) / denom
        consistency_pass = 1.0 if abs(expected_nu - nu) < 0.001 else 0.0
        nu_close = 1.0 if abs(nu - nu_t) <= tol_nu else 0.0
        BH_close = 1.0 if abs(BH - BH_t) <= tol_mod else 0.0
        GH_close = 1.0 if abs(GH - GH_t) <= tol_mod else 0.0
        total = (consistency_pass + nu_close + BH_close + GH_close) / 4.0
        return total


# === block: score_1 (check id='check_alpha_avg') ===
def score_1(artifact, step, ctx):
        import math
        try:
            val = float(artifact.strip())
        except (ValueError, AttributeError, TypeError):
            return 0.0
        target = float(step.get('target', 24.86))
        tol = float(step.get('tolerance', 2.0))
        delta = abs(val - target)
        if delta <= tol:
            return 1.0
        else:
            # linear decay from tol to 2*tol, zero beyond
            return max(0.0, 1.0 - (delta - tol) / tol)


# === block: score_2 (check id='check_thermal') ===
def score_2(artifact, step, ctx):
        required_cols = ['T(K)', 'alpha(10⁻⁶ K⁻¹)', 'C_V(J/mol-K)']
        try:
            if not artifact or not isinstance(artifact, list) or len(artifact) == 0:
                return 0.0
            rows = artifact
        except Exception:
            return 0.0
        # check columns exist
        for col in required_cols:
            if col not in rows[0]:
                return 0.0
        target_temps = step.get('target_temperatures', [300,500,1000,1500,2000])
        dulong = step.get('dulong_petit', 74.85)
        # extract data
        try:
            temps = [float(row['T(K)']) for row in rows]
            alphas = [float(row['alpha(10⁻⁶ K⁻¹)']) for row in rows]
            cvs = [float(row['C_V(J/mol-K)']) for row in rows]
            if len(temps) != len(target_temps):
                return 0.0
        except (ValueError, KeyError):
            return 0.0
        # check exact T values
        for i, t in enumerate(target_temps):
            if temps[i] != t:
                return 0.0
        score = 0.0
        # alpha strictly increasing
        if all(alphas[i] < alphas[i+1] for i in range(len(alphas)-1)):
            score += 0.3
        # C_V strictly increasing
        if all(cvs[i] < cvs[i+1] for i in range(len(cvs)-1)):
            score += 0.3
        # C_V at max T close to Dulong-Petit
        if abs(cvs[-1] - dulong) <= 2.0:
            score += 0.2
        # T correctness already checked above, add small rest
        # total 0.2 for temperature correctness? We'll assign 0.2 for temperature matching
        score += 0.2  # for correct T values (already verified)
        return score


_SCORERS = {
    'check_poisson': score_0,
    'check_alpha_avg': score_1,
    'check_thermal': score_2,
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
