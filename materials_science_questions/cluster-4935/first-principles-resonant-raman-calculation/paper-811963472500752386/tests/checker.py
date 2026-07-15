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
    import math

    def compute_spectrum(N):
        # Constants
        F = 0.06   # a*c/v in cm (a=1e-6 cm, c=3e10 cm/s, v=5e5 cm/s) -> 0.06 cm
        kT_meV = 0.517   # 6 K
        conversion = 0.123984  # 1 cm^-1 to meV
        intensities = []
        for nu in range(0, 51):
            x = F * nu
            # Sin factor
            if x == 0:
                sin_factor = 1.0
            else:
                px = math.pi * x
                sin_factor = math.sin(px) / px
            # N-pole factor
            Nsq = N * N
            denom = Nsq - x * x
            if abs(denom) < 1e-12:
                # removable singularity at x=N
                # limit = (-1)^{N+1} * N / (2*N) = (-1)^{N+1}/2
                sign = (-1)**(N+1)
                factor_N = sign * 0.5  # coarse but exact
                # More precise with L'Hopital using x = N
                # However the product sin(πx)/(πx) * N²/(N² - x²) at x=N is finite.
                # We compute directly using limit formula:
                # limit = N² * [ sin(πx) / (πx*(N²-x²)) ]
                # for x→N, using L'Hopital on numerator/denominator:
                # d/dx sin(πx) = π cos(πx) = π * (-1)^N
                # d/dx (πx*(N²-x²)) = π*(N² - x²) - 2πx² = π(N² - 3x²)
                # evaluate at x=N: π(N² - 3N²) = -2π N²
                # So limit = N² * [ π (-1)^N / (-2π N²) ] = -(-1)^N / 2 = (-1)^{N+1}/2
                factor_N = (-1)**(N+1) * 0.5
            else:
                factor_N = Nsq / denom
            # Bose factor
            if nu == 0:
                # limit product nu * n_bose = kT_meV / conversion
                I = (kT_meV / conversion) * (sin_factor**2) * (factor_N**2)
            else:
                E_meV = nu * conversion
                n_bose = 1.0 / (math.exp(E_meV / kT_meV) - 1.0)
                I = nu * (sin_factor**2) * (factor_N**2) * n_bose
            intensities.append(I)
        # normalize
        max_val = max(intensities)
        if max_val == 0:
            return [0.0] * 51
        return [v / max_val for v in intensities]

    ref_N1 = compute_spectrum(1)
    ref_N2 = compute_spectrum(2)
    return {"ref_N1": ref_N1, "ref_N2": ref_N2}


# === block: score_0 (check id='step1') ===
def score_0(artifact, step, ctx):
    import math

    # Agent intensities
    agent_intensity = []
    for row in artifact:
        try:
            val = float(row['Intensity_arb_units'])
        except (ValueError, KeyError):
            return 0.0
        agent_intensity.append(val)
    if len(agent_intensity) != 51:
        return 0.0

    ref = ctx['ref_N1']
    if len(ref) != 51:
        return 0.0

    # Compute NCC
    mean_a = sum(agent_intensity) / 51.0
    mean_r = sum(ref) / 51.0
    num = sum((a - mean_a) * (r - mean_r) for a, r in zip(agent_intensity, ref))
    den = math.sqrt(sum((a - mean_a) ** 2 for a in agent_intensity) * sum((r - mean_r) ** 2 for r in ref))
    if den < 1e-12:
        ncc = 0.0
    else:
        ncc = num / den
    # NCC float may exceed 1 due to rounding; clip
    ncc = max(0.0, min(1.0, ncc))

    # Score using declared target and tolerance from grading_spec
    target = step.get('target', 0.98)
    tol   = step.get('tolerance', 0.02)

    if ncc >= target:
        score_ncc = 1.0
    else:
        lower = target - tol
        if lower >= target:
            score_ncc = 0.0
        else:
            score_ncc = max(0.0, (ncc - lower) / tol)

    # No zero check for N1
    return max(0.0, min(1.0, score_ncc))


# === block: score_1 (check id='step2') ===
def score_1(artifact, step, ctx):
    import math

    # Agent intensities
    shifts = []
    agent_intensity = []
    for row in artifact:
        try:
            s = float(row['Raman_shift_cm1'])
            v = float(row['Intensity_arb_units'])
        except (ValueError, KeyError):
            return 0.0
        shifts.append(s)
        agent_intensity.append(v)
    if len(agent_intensity) != 51:
        return 0.0

    ref = ctx['ref_N2']
    if len(ref) != 51:
        return 0.0

    # Compute NCC
    mean_a = sum(agent_intensity) / 51.0
    mean_r = sum(ref) / 51.0
    num = sum((a - mean_a) * (r - mean_r) for a, r in zip(agent_intensity, ref))
    den = math.sqrt(sum((a - mean_a) ** 2 for a in agent_intensity) * sum((r - mean_r) ** 2 for r in ref))
    if den < 1e-12:
        ncc = 0.0
    else:
        ncc = num / den
    ncc = max(0.0, min(1.0, ncc))

    # Score NCC
    score_ncc = ncc / 0.98 if ncc < 0.98 else 1.0

    # Find first zero (local minimum with intensity < 1e-3)
    first_zero_pos = None
    for i in range(1, len(agent_intensity) - 1):
        if agent_intensity[i] < 1e-3 and agent_intensity[i] < agent_intensity[i-1] and agent_intensity[i] < agent_intensity[i+1]:
            first_zero_pos = shifts[i]
            break

    zero_score = 0.0
    if first_zero_pos is not None:
        if abs(first_zero_pos - 16.67) <= 2.0:
            zero_score = 1.0
        else:
            zero_score = 0.0
    else:
        zero_score = 0.0

    # Combined: 70% NCC, 30% zero position
    combined = 0.7 * score_ncc + 0.3 * zero_score
    return max(0.0, min(1.0, combined))


_SCORERS = {
    'step1': score_0,
    'step2': score_1,
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
