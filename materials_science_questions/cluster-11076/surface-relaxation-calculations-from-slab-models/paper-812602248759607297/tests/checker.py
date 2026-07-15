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


# === block: score_0 (check id='phonon_dispersion') ===
def score_0(artifact, step, ctx):
    # Linear interpolation helper that reconstructs dispersion curves from the
    # submitted (zeta, frequency) points and evaluates the frequency at a
    # requested experimental zeta.
    def _interp_freqs(agent_rows, direction, zeta_exp):
        # Collect (z, f) for the given direction
        pts = []
        for r in agent_rows:
            try:
                z = float(r['reduced_wavevector'])
                f = float(r['frequency_cm1'])
                if r['direction'] == direction:
                    pts.append((z, f))
            except (KeyError, ValueError):
                continue
        if not pts:
            return []

        # Sort by zeta
        pts.sort(key=lambda t: t[0])

        # Group frequencies by zeta
        zeta_dict = {}
        for z, f in pts:
            zeta_dict.setdefault(z, []).append(f)
        zetas = sorted(zeta_dict.keys())

        # Handle zeta_exp outside the range: take nearest endpoint
        if zeta_exp <= zetas[0]:
            return zeta_dict[zetas[0]]
        if zeta_exp >= zetas[-1]:
            return zeta_dict[zetas[-1]]

        # Find the interval and linearly interpolate
        for i in range(len(zetas) - 1):
            z1 = zetas[i]
            z2 = zetas[i + 1]
            if z1 <= zeta_exp <= z2:
                f1_list = sorted(zeta_dict[z1])
                f2_list = sorted(zeta_dict[z2])
                # Pair modes by order up to the shorter list
                n = min(len(f1_list), len(f2_list))
                interp = []
                for j in range(n):
                    frac = (zeta_exp - z1) / (z2 - z1)
                    f = f1_list[j] + frac * (f2_list[j] - f1_list[j])
                    interp.append(f)
                return interp

        # Fallback (should not be reached)
        return []


    squared_errors = []
    for ep in step['experimental_points']:
        direction = ep['direction']
        zeta = ep['zeta']
        target = ep['frequency']

        interp_freqs = _interp_freqs(artifact, direction, zeta)
        if not interp_freqs:
            # No submission data for this direction — apply the default penalty
            squared_errors.append(200.0 ** 2)
        else:
            best = min(interp_freqs, key=lambda f: abs(f - target))
            error = abs(best - target)
            squared_errors.append(error ** 2)

    if not squared_errors:
        score = 0.0
    else:
        rmse = math.sqrt(sum(squared_errors) / len(squared_errors))
        score = 1.0 if rmse <= 10.0 else max(0.0, 1.0 - (rmse - 10.0) / 40.0)

    return score


_SCORERS = {
    'phonon_dispersion': score_0,
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
