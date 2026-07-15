import os
import json
import csv

# === author imports / helpers ===
import math
from scipy.integrate import quad


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


# === block: score_0 (check id='elastic_constants') ===
def score_0(artifact, step, ctx):
    def scorer(artifact, step, ctx):
        gold = step.get('gold', {})
        tolerances = step.get('tolerance', {})
        total = 0
        ok = 0
        for thick, expected in gold.items():
            data = artifact.get(thick, {})
            ec = data.get('elastic_constants', {})
            tol = tolerances.get(thick, 0.10)
            for key, gval in expected.items():
                # try elastic_constants sub-object first, then top-level keys (A_B, A_G)
                if key in ec:
                    val = ec[key]
                else:
                    val = data.get(key)
                if val is None:
                    continue
                total += 1
                # handle zero gold with absolute tolerance
                if abs(gval) < 1e-6:
                    if abs(val - gval) <= 0.01:
                        ok += 1
                else:
                    rel_err = abs(val - gval) / abs(gval)
                    if rel_err <= tol:
                        ok += 1
        return ok / total if total else 0.0


# === block: score_1 (check id='moduli') ===
def score_1(artifact, step, ctx):
    def scorer(artifact, step, ctx):
        gold = step.get('gold', {})
        tolerances = step.get('tolerance', {})
        total = 0
        ok = 0
        for thick, expected in gold.items():
            data = artifact.get(thick, {})
            tol = tolerances.get(thick, 0.10)
            for key, gval in expected.items():
                val = data.get(key)
                if val is None:
                    continue
                total += 1
                if abs(gval) < 1e-6:
                    if abs(val - gval) <= 0.01:
                        ok += 1
                else:
                    rel_err = abs(val - gval) / abs(gval)
                    if rel_err <= tol:
                        ok += 1
        return ok / total if total else 0.0


# === block: score_2 (check id='sound_velocities') ===
def score_2(artifact, step, ctx):
    def scorer(artifact, step, ctx):
        gold = step.get('gold', {})
        tolerances = step.get('tolerance', {})
        total = 0
        ok = 0
        for thick, expected in gold.items():
            data = artifact.get(thick, {})
            tol = tolerances.get(thick, 0.03)
            for key, gval in expected.items():
                val = data.get(key)
                if val is None:
                    continue
                total += 1
                if abs(gval) < 1e-6:
                    if abs(val - gval) <= 1.0:
                        ok += 1
                else:
                    rel_err = abs(val - gval) / abs(gval)
                    if rel_err <= tol:
                        ok += 1
        return ok / total if total else 0.0


# === block: score_3 (check id='Theta_D') ===
def score_3(artifact, step, ctx):
    def scorer(artifact, step, ctx):
        gold = step.get('gold', {})
        tol = step.get('tolerance', 0.05)
        total = 0
        ok = 0
        for thick, gval in gold.items():
            val = artifact.get(thick, {}).get('Theta_D')
            if val is None:
                continue
            total += 1
            rel_err = abs(val - gval) / abs(gval)
            if rel_err <= tol:
                ok += 1
        return ok / total if total else 0.0


# === block: score_4 (check id='k_min') ===
def score_4(artifact, step, ctx):
    def scorer(artifact, step, ctx):
        gold = step.get('gold', {})
        tol = step.get('tolerance', 0.05)
        total = 0
        ok = 0
        for thick, gval in gold.items():
            val = artifact.get(thick, {}).get('k_min')
            if val is None:
                continue
            total += 1
            rel_err = abs(val - gval) / abs(gval)
            if rel_err <= tol:
                ok += 1
        return ok / total if total else 0.0


# === block: score_5 (check id='C_V_saturated') ===
def score_5(artifact, step, ctx):
    def scorer(artifact, step, ctx):
        gold = step.get('gold', {})
        tol = step.get('tolerance', 0.05)
        total = 0
        ok = 0
        for thick, gval in gold.items():
            val = artifact.get(thick, {}).get('C_V_saturated')
            if val is None:
                continue
            total += 1
            rel_err = abs(val - gval) / abs(gval)
            if rel_err <= tol:
                ok += 1
        return ok / total if total else 0.0


# === block: score_6 (check id='trends') ===
def score_6(artifact, step, ctx):
    def scorer(artifact, step, ctx):
        # expected order: k_min monolayer > bilayer > trilayer > bulk
        # Theta_D bulk > trilayer > bilayer > monolayer
        try:
            km = {'mono': artifact['monolayer']['k_min'],
                  'bi': artifact['bilayer']['k_min'],
                  'tri': artifact['trilayer']['k_min'],
                  'bulk': artifact['bulk']['k_min']}
            td = {'bulk': artifact['bulk']['Theta_D'],
                  'tri': artifact['trilayer']['Theta_D'],
                  'bi': artifact['bilayer']['Theta_D'],
                  'mono': artifact['monolayer']['Theta_D']}
            score = 0.0
            if km['mono'] > km['bi'] > km['tri'] > km['bulk']:
                score += 0.5
            if td['bulk'] > td['tri'] > td['bi'] > td['mono']:
                score += 0.5
            return score
        except Exception:
            return 0.0


# === block: score_7 (check id='C_V_curves') ===
def score_7(artifact, step, ctx):
    def scorer(artifact, step, ctx):
        import os, json
        summary_path = os.path.join('/app/outputs', 'results_summary.json')
        if not os.path.exists(summary_path):
            return 0.0
        with open(summary_path) as f:
            summary = json.load(f)
        R = 8.314462618
        def debye_CV(T, theta_D):
            if T == 0:
                return 0.0
            xm = theta_D / T
            def integrand(x):
                if x == 0:
                    return 0.0
                return x**4 * math.exp(x) / (math.exp(x) - 1)**2
            res, _ = quad(integrand, 0, xm, limit=200)
            return 9 * R * (T / theta_D)**3 * res
        thicknesses = ['bulk', 'monolayer', 'bilayer', 'trilayer']
        scores = []
        for thick in thicknesses:
            if thick not in summary:
                continue
            theta = summary[thick].get('Theta_D')
            sat = summary[thick].get('C_V_saturated')
            if theta is None or sat is None:
                continue
            scale = sat / (3 * R)
            rows = [r for r in artifact if r.get('thickness') == thick]
            if not rows:
                scores.append(0.0)
                continue
            # sort by temperature
            try:
                rows.sort(key=lambda r: float(r['temperature_K']))
            except:
                scores.append(0.0)
                continue
            # check monotonicity (non-decreasing)
            monotonic = True
            prev = -1.0
            for r in rows:
                cv = float(r['C_V_J_mol_K'])
                if cv < prev - 1e-6:
                    monotonic = False
                    break
                prev = cv
            if not monotonic:
                scores.append(0.0)
                continue
            # evaluate deviation from Debye model at 10 temperature points
            temps = [100, 300, 500, 700, 900, 950, 980, 990, 995, 999]
            dev_ok = 0
            total = 0
            for T in temps:
                # find nearest data point
                nearest = min(rows, key=lambda r: abs(float(r['temperature_K']) - T))
                try:
                    t_act = float(nearest['temperature_K'])
                    cv_act = float(nearest['C_V_J_mol_K'])
                except:
                    continue
                cv_model = scale * debye_CV(T, theta)
                if cv_model > 0:
                    rel_err = abs(cv_act - cv_model) / cv_model
                    if rel_err <= 0.05:
                        dev_ok += 1
                total += 1
            if total > 0:
                scores.append(dev_ok / total)
            else:
                scores.append(0.0)
        if not scores:
            return 0.0
        return sum(scores) / len(scores)


_SCORERS = {
    'elastic_constants': score_0,
    'moduli': score_1,
    'sound_velocities': score_2,
    'Theta_D': score_3,
    'k_min': score_4,
    'C_V_saturated': score_5,
    'trends': score_6,
    'C_V_curves': score_7,
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
