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
    U = 8.0
    B = 1.5

    # Expected energies at Gamma and X
    expected_energies = [
        {'kx': 0.0, 'ky': 0.0, 'E_plus': math.sqrt((U/2)**2 + 4*B**2 * (math.cos(0)+math.cos(0))**2), 'E_minus': -math.sqrt((U/2)**2 + 4*B**2 * (math.cos(0)+math.cos(0))**2)},
        {'kx': math.pi, 'ky': 0.0, 'E_plus': 4.0, 'E_minus': -4.0}
    ]

    def _G(s):
        Nk = 600
        total = Nk * Nk
        sU = s * U
        Phi_val = math.sqrt(0.25 - s*s) if s < 0.5 else 0.0
        Uphi = U * Phi_val
        sum_val = 0.0
        for i in range(Nk):
            kx = -math.pi + (i + 0.5) * (2*math.pi / Nk)
            for j in range(Nk):
                ky = -math.pi + (j + 0.5) * (2*math.pi / Nk)
                c = math.cos(kx) + math.cos(ky)
                tk = math.sqrt((sU)**2 + 4 * B * B * c * c)
                if tk >= Uphi:
                    sum_val += U / tk
        avg = sum_val / total
        return avg - 1.0

    # bisection
    lo, hi = 0.001, 0.5
    flo = _G(lo)
    fhi = _G(hi)
    for _ in range(60):
        mid = (lo + hi) / 2.0
        fmid = _G(mid)
        if fmid == 0.0:
            break
        if flo * fmid < 0.0:
            hi = mid
            fhi = fmid
        else:
            lo = mid
            flo = fmid
    S_root = (lo + hi) / 2.0

    return {
        'expected_energies': expected_energies,
        'S_root': S_root,
        'tol_energy': 1e-6,
        'tol_mag': 1e-4
    }


# === block: score_0 (check id='step_energy') ===
def score_0(artifact, step, ctx):
    import csv, io
    rows = list(csv.DictReader(io.StringIO(artifact)))
    correct = 0
    total_vals = 0
    for r in rows:
        try:
            kx = float(r['kx'])
            ky = float(r['ky'])
            E_plus = float(r['E_plus'])
            E_minus = float(r['E_minus'])
        except (ValueError, KeyError):
            return 0.0
        # find matching expected row (tolerance for k-point matching is not strict; just match by kx,ky to known points)
        # Since there are only two expected points, we can match by exact equality of kx,ky within tolerance
        matched = None
        for exp in ctx['expected_energies']:
            if abs(kx - exp['kx']) < 1e-9 and abs(ky - exp['ky']) < 1e-9:
                matched = exp
                break
        if matched is None:
            continue
        # check each energy
        if abs(E_plus - matched['E_plus']) <= ctx['tol_energy']:
            correct += 1
        total_vals += 1
        if abs(E_minus - matched['E_minus']) <= ctx['tol_energy']:
            correct += 1
        total_vals += 1
    # If less than 2 rows, score proportionally
    if total_vals == 0:
        return 0.0
    return correct / total_vals


# === block: score_1 (check id='step_magnetization') ===
def score_1(artifact, step, ctx):
    s = artifact.strip()
    try:
        S_agent = float(s)
    except (ValueError, TypeError):
        return 0.0
    diff = abs(S_agent - ctx['S_root'])
    tol = ctx['tol_mag']
    if diff <= tol:
        return 1.0
    elif diff > 2*tol:
        return 0.0
    else:
        return 1.0 - (diff - tol) / tol


_SCORERS = {
    'step_energy': score_0,
    'step_magnetization': score_1,
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
