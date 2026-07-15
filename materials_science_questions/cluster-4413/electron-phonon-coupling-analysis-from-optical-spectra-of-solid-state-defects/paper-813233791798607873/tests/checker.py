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
    compounds = [
        {'name': 'LiMgBF6', 'deltaE_S': 7296, 'FWHM': 5636},
        {'name': 'Li2NaBF6', 'deltaE_S': 9063, 'FWHM': 6300},
        {'name': 'Li3BF6', 'deltaE_S': 11906, 'FWHM': 5853},
    ]
    return {
        'compounds': compounds,
        'T': 300.0,
        'kB': 0.69503476,
    }


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    import math

    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0

    data = {}
    for row in artifact:
        name = row.get('compound', '').strip()
        if name:
            data[name] = row

    def solve_viirs(deltaE_S, FWHM, T, kB):
        sqrt_8ln2 = math.sqrt(8 * math.log(2))
        def f(S):
            if S <= 0.5:
                return 1e10
            hw = deltaE_S / (2*S - 1)
            arg = hw / (2 * kB * T)
            coth = 1.0 / math.tanh(arg)
            return sqrt_8ln2 * hw * math.sqrt(S * coth) - FWHM
        # bisection
        lo = 0.51
        hi = 20.0
        for _ in range(100):
            mid = (lo + hi) / 2
            if f(mid) > 0:
                hi = mid
            else:
                lo = mid
        S = (lo + hi) / 2
        hw = deltaE_S / (2*S - 1)
        return S, hw

    def compute_regime(S_val):
        if S_val < 1:
            return 'weak'
        elif S_val <= 5:
            return 'intermediate'
        else:
            return 'strong'

    T = ctx['T']
    kB = ctx['kB']
    compounds = ctx['compounds']

    tol_S = 0.1
    tol_hw = 10.0
    total_score = 0.0
    weight_per_compound = 1.0 / len(compounds)

    for comp in compounds:
        name = comp['name']
        row = data.get(name)
        if not row:
            continue
        try:
            S_agent = float(row['S'])
            hw_agent = float(row['hbar_omega'])
            regime_agent = str(row.get('regime', '')).strip().lower()
        except (ValueError, KeyError):
            continue

        S_ref, hw_ref = solve_viirs(comp['deltaE_S'], comp['FWHM'], T, kB)

        diff_S = abs(S_agent - S_ref)
        s_score = max(0.0, 1.0 - diff_S / tol_S) if diff_S <= tol_S else 0.0
        diff_hw = abs(hw_agent - hw_ref)
        hw_score = max(0.0, 1.0 - diff_hw / tol_hw) if diff_hw <= tol_hw else 0.0

        expected_regime = compute_regime(S_ref)
        regime_score = 1.0 if regime_agent == expected_regime else 0.0

        compound_score = (s_score + hw_score + regime_score) / 3.0
        total_score += compound_score * weight_per_compound

    return total_score


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
