import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.optimize import brentq
from collections import OrderedDict


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
        # Model parameters (units consistent with kJ)
        R = 0.008314  # kJ/(mol K)
        S_diff1 = 0.00613  # kJ/(mol K)   (6.13 J)
        E1_diff = 154.3    # kJ/mol
        E11 = -3.918       # kJ/mol
        S_diff2 = 0.04417  # kJ/(mol K)   (44.17 J)
        E2_diff = 78.30    # kJ/mol
        E22 = 5.887        # kJ/mol
        c = 12

        def a_c1(theta1, T):
            if theta1 <= 0.0 or theta1 >= 1.0:
                return float('inf')
            prefactor = theta1 / (1.0 - theta1)
            term1 = np.exp(S_diff1 / R)
            term2 = np.exp((E1_diff + c * theta1 * E11) / (R * T))
            return prefactor * term1 * term2

        def a_c2(r, T):
            if r <= 0.0 or r >= 1.0:
                return 0.0 if r == 0.0 else float('inf')
            prefactor = r / (1.0 - r)
            term1 = np.exp(S_diff2 / R)
            term2 = np.exp((E2_diff + c * r * E22) / (R * T))
            return prefactor * term1 * term2

        def f(r, x, T):
            theta1 = x / (1.0 + r)
            if theta1 <= 0.0 or theta1 >= 1.0:
                return 1e6
            return a_c1(theta1, T) - a_c2(r, T)

        def solve_activity(x, T):
            # feasible r in [max(0, x-1), 1)
            lo = max(0.0, x - 1.0 + 1e-12)
            hi = 1.0 - 1e-12
            if lo >= hi:
                # Extremely high x (not in our grid), fallback
                return a_c1(x, T)
            try:
                # Check sign at boundaries; if no sign change scan for zero crossing
                f_lo = f(lo, x, T)
                f_hi = f(hi, x, T)
                if f_lo * f_hi > 0:
                    # No sign change: try scanning for zero or use r=0 boundary
                    for r_try in np.linspace(lo, hi, 200):
                        val = f(r_try, x, T)
                        if abs(val) < 1e-12:
                            r = r_try
                            break
                    else:
                        # If no crossing, assume only type‑1 sites are occupied
                        r = lo
                else:
                    r = brentq(f, lo, hi, args=(x, T), xtol=1e-12)
            except Exception:
                r = lo
            theta1 = x / (1.0 + r)
            return a_c1(theta1, T)

        # Grid
        xs = np.arange(0.90, 1.951, 0.05)  # 0.90 to 1.95
        Ts = [1173, 1473, 1773, 2073, 2373]

        ref_values = OrderedDict()
        required_pairs = []
        for x in xs:
            x_round = round(float(x), 2)
            for T in Ts:
                key = (x_round, int(T))
                required_pairs.append(key)
                ref_values[key] = float(solve_activity(x_round, T))

        return {'ref_values': ref_values, 'required_pairs': required_pairs}


# === block: score_0 (check id='s1') ===
def score_0(artifact, step, ctx):
            required_pairs = ctx['required_pairs']
            ref_values = ctx['ref_values']
            if not artifact or not isinstance(artifact, list) or len(artifact) == 0:
                return 0.0
            # Check required columns
            if not all(col in artifact[0] for col in ('x', 'T', 'a_c')):
                return 0.0

            agent_vals = {}
            parse_errors = []
            for row in artifact:
                try:
                    x = round(float(row['x']), 2)
                    T = int(float(row['T']))
                    a = float(row['a_c'])
                    key = (x, T)
                    if key in agent_vals:
                        parse_errors.append('duplicate')
                    agent_vals[key] = a
                except Exception:
                    parse_errors.append('parse error')
                    continue
            if parse_errors:
                return 0.0

            total = len(required_pairs)
            matches = 0
            for key, a_ref in ref_values.items():
                if key in agent_vals:
                    a_agent = agent_vals[key]
                    tol = max(0.1, 0.15 * abs(a_ref))
                    if abs(a_agent - a_ref) <= tol:
                        matches += 1
                # else missing pair counts as non-matching
            return matches / total if total > 0 else 0.0


_SCORERS = {
    's1': score_0,
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
