import os
import json
import csv

# === author imports / helpers ===
import csv
import math

class _ndarray(list):
    def __lt__(self, other):
        if isinstance(other, (int, float)):
            return _ndarray([x < other for x in self])
        return _ndarray([a < b for a, b in zip(self, other)])
    def __le__(self, other):
        if isinstance(other, (int, float)):
            return _ndarray([x <= other for x in self])
        return _ndarray([a <= b for a, b in zip(self, other)])
    def __gt__(self, other):
        if isinstance(other, (int, float)):
            return _ndarray([x > other for x in self])
        return _ndarray([a > b for a, b in zip(self, other)])
    def __ge__(self, other):
        if isinstance(other, (int, float)):
            return _ndarray([x >= other for x in self])
        return _ndarray([a >= b for a, b in zip(self, other)])
    def __getitem__(self, index):
        if isinstance(index, (_ndarray, list)) and len(index) > 0 and isinstance(index[0], (bool, int)):
            return _ndarray([self[i] for i, flag in enumerate(index) if flag])
        return super().__getitem__(index)

def _array(seq):
    return _ndarray(seq)

def _polyfit(x, y, deg):
    if deg != 1:
        raise ValueError("only linear fit supported")
    n = len(x)
    if n < 2:
        return _ndarray([0.0, 0.0])
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    num = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
    den = sum((xi - mean_x) ** 2 for xi in x)
    if den == 0:
        return _ndarray([0.0, mean_y])
    slope = num / den
    intercept = mean_y - slope * mean_x
    return _ndarray([slope, intercept])

def _sum(arr):
    return sum(arr)

def _max(arr):
    return max(arr)

def _argmax(arr):
    m = max(arr)
    return arr.index(m)

class _NumPyFallback:
    def __init__(self):
        self.array = _array
        self.polyfit = _polyfit
        self.sum = _sum
        self.max = _max
        self.argmax = _argmax

np = _NumPyFallback()


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
    targets = spec.get("steps", [])[0].get("target_values", {})
    tolerances = spec.get("steps", [])[0].get("tolerances", {})
    return {"targets": targets, "tolerances": tolerances}


# === block: score_0 (check id='step_mech_props') ===
def score_0(artifact, step, ctx):
    if artifact is None or len(artifact) == 0:
        return 0.0

    # Group data by ribbon_type
    groups = {}
    for row in artifact:
        rtype = row.get("ribbon_type", "").strip()
        try:
            strain = float(row["strain"])
            stress = float(row["stress"])
        except (KeyError, ValueError):
            continue
        groups.setdefault(rtype, []).append((strain, stress))

    targets = ctx["targets"]
    tolerances = ctx["tolerances"]
    E_tol = tolerances.get("E", {}).get("relative", 0.05)
    sig_tol = tolerances.get("sigma_y", {}).get("relative", 0.05)
    eps_tol = tolerances.get("eps_b", {}).get("absolute", 0.01)

    matches = 0
    for rtype, expected in targets.items():
        if rtype not in groups:
            continue
        points = sorted(groups[rtype], key=lambda p: p[0])
        strains = np.array([p[0] for p in points])
        stresses = np.array([p[1] for p in points])

        # Young's modulus: linear fit on low-strain points (strain < 0.02)
        low_mask = strains < 0.02
        if np.sum(low_mask) < 3:
            continue   # insufficient points, skip this ribbon
        low_strain = strains[low_mask]
        low_stress = stresses[low_mask]
        coeffs = np.polyfit(low_strain, low_stress, 1)
        E_computed = coeffs[0]   # GPa

        # Yielding strength: maximum stress
        sigma_y_computed = float(np.max(stresses))

        # Breaking strain: first strain after peak where stress drops below 1% of sigma_y
        max_idx = int(np.argmax(stresses))
        eps_b_computed = strains[-1]   # default to last strain if no drop
        for i in range(max_idx + 1, len(strains)):
            if stresses[i] < 0.01 * sigma_y_computed:
                eps_b_computed = strains[i]
                break

        # Check against targets
        E_tgt = expected["E"]
        if abs(E_computed - E_tgt) / max(abs(E_tgt), 1e-9) <= E_tol:
            matches += 1

        sig_tgt = expected["sigma_y"]
        if abs(sigma_y_computed - sig_tgt) / max(abs(sig_tgt), 1e-9) <= sig_tol:
            matches += 1

        eps_tgt = expected["eps_b"]
        if abs(eps_b_computed - eps_tgt) <= eps_tol:
            matches += 1

    return matches / 9.0


_SCORERS = {
    'step_mech_props': score_0,
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
