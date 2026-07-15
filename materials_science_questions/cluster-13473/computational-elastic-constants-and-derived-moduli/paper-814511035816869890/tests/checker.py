import os
import json
import csv

# === author imports / helpers ===
import json, os, math


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
    def prepare(outputs_dir, spec):
        s_path = os.path.join(outputs_dir, 's_matrix_results.json')
        if not os.path.exists(s_path):
            return {'s_matrix': {}}
        with open(s_path) as f:
            s_data = json.load(f)
        results = s_data.get('results', [])
        s_matrix = {}
        for rec in results:
            sys = rec['system']
            key = (sys['layout'], sys['channel'], str(sys['sigma_prime_over_sigma']))
            s_matrix[key] = {'B11': float(rec['B11']), 'B12': float(rec['B12']), 'B44': float(rec['B44'])}
        return {'s_matrix': s_matrix}


# === block: score_0 (check id='cubic_symmetry') ===
def score_0(artifact, step, ctx):
    def score_cubic_symmetry(artifact, step, ctx):
        tol = step.get('tolerance', 0.03)
        results = artifact.get('results', [])
        if not results:
            return 0.0
        passed = 0
        for rec in results:
            try:
                s11 = float(rec['S11'])
                s22 = float(rec['S22'])
                s33 = float(rec['S33'])
                s44 = float(rec['S44'])
                s55 = float(rec['S55'])
                s66 = float(rec['S66'])
                s12 = float(rec['S12'])
                s13 = float(rec['S13'])
                s23 = float(rec['S23'])
                other = float(rec['other_S_max_abs'])
                if (abs(s11-s22) <= tol and abs(s11-s33) <= tol and
                    abs(s44-s55) <= tol and abs(s44-s66) <= tol and
                    abs(s12-s13) <= tol and abs(s12-s23) <= tol and
                    other <= tol):
                    passed += 1
            except (KeyError, ValueError):
                pass
        return passed / len(results) if results else 0.0


# === block: score_1 (check id='pr_consistency') ===
def score_1(artifact, step, ctx):
    def compute_pr(B11, B12, B44):
        PR_100 = B12/(B11+B12)
        denom = B11**2 - 2*B12**2 + B11*(B12+2*B44)
        PR_110_1m10 = (B11**2 - 2*B12**2 + B11*(B12-2*B44))/denom
        PR_110_001 = (4*B12*B44)/denom
        PR_111 = (B11+2*B12-2*B44)/(2*(B11+2*B12+B44))
        return PR_100, PR_110_1m10, PR_110_001, PR_111

    def score_pr_consistency(artifact, step, ctx):
        tol = step.get('tolerance', 0.05)
        s_matrix = ctx.get('s_matrix', {})
        results = artifact.get('results', [])
        if not results:
            return 0.0
        matched = 0
        total = 0
        for rec in results:
            sys = rec['system']
            key = (sys['layout'], sys['channel'], str(sys['sigma_prime_over_sigma']))
            if key not in s_matrix:
                continue
            B = s_matrix[key]
            B11, B12, B44 = B['B11'], B['B12'], B['B44']
            try:
                r_PR_100, r_PR_110_1m10, r_PR_110_001, r_PR_111 = compute_pr(B11, B12, B44)
                a_PR_100 = float(rec['PR_100'])
                a_PR_110_1m10 = float(rec['PR_110_1m10'])
                a_PR_110_001 = float(rec['PR_110_001'])
                a_PR_111 = float(rec['PR_111'])
                if (abs(r_PR_100 - a_PR_100) <= tol and
                    abs(r_PR_110_1m10 - a_PR_110_1m10) <= tol and
                    abs(r_PR_110_001 - a_PR_110_001) <= tol and
                    abs(r_PR_111 - a_PR_111) <= tol):
                    matched += 1
            except (KeyError, ValueError):
                pass
            total += 1
        return matched / total if total else 0.0


# === block: score_2 (check id='auxeticity_trend') ===
def score_2(artifact, step, ctx):
    def score_auxeticity_trend(artifact, step, ctx):
        expected = step.get('hidden_expected_signs', {})
        if not expected:
            return 0.0
        results = artifact.get('results', [])
        if not results:
            return 0.0
        ok = 0
        total = 0
        for rec in results:
            sys = rec['system']
            layout = sys['layout']
            chan = sys['channel']
            ratio_str = str(sys['sigma_prime_over_sigma'])
            PR_min = float(rec['PR_min'])
            if layout not in expected:
                continue
            if ratio_str not in expected[layout]:
                continue
            expected_sign = expected[layout][ratio_str]
            actual_neg = PR_min < 0.0
            if expected_sign == 'negative':
                if actual_neg:
                    ok += 1
            elif expected_sign == 'non_negative':
                if PR_min >= 0.0:
                    ok += 1
            else:
                ok += 1  # treat as pass
            total += 1
        return ok / total if total else 0.0


# === block: score_3 (check id='isotropy_trend') ===
def score_3(artifact, step, ctx):
    def score_isotropy_trend(artifact, step, ctx):
        results = artifact.get('results', [])
        if not results:
            return 0.0
        # Collect isotropy_ratio for separate D-type channels
        ratio_at_1_0 = None
        ratio_at_1_1 = None
        for rec in results:
            sys = rec['system']
            if sys['layout'] != 'separate' or sys['channel'] != 'D':
                continue
            ratio = float(sys['sigma_prime_over_sigma'])
            isotropy = float(rec['isotropy_ratio'])
            if abs(ratio - 1.0) < 1e-6:
                ratio_at_1_0 = isotropy
            if abs(ratio - 1.1) < 1e-6:
                ratio_at_1_1 = isotropy
        if ratio_at_1_0 is not None and ratio_at_1_1 is not None and ratio_at_1_1 > ratio_at_1_0:
            return 1.0
        return 0.0


_SCORERS = {
    'cubic_symmetry': score_0,
    'pr_consistency': score_1,
    'auxeticity_trend': score_2,
    'isotropy_trend': score_3,
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
