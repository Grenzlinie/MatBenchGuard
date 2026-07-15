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


# === block: score_0 (check id='step_03_band_structure') ===
def score_0(artifact, step, ctx):
        config = step.get("config", {})
        target_kpoints = config.get("target_kpoints", {})
        tol_coord = config.get("tol_coordinate", 0.02)
        gamma_zero_rms = config.get("gamma_zero_rms", 0.01)
        min_mag = config.get("min_magnitude", 0.05)
        frac_sign_rev = config.get("fraction_sign_reversal", 0.8)

        if not artifact:
            return 0.0

        rows = []
        for r in artifact:
            try:
                rows.append({
                    'k_index': int(r['k_index']),
                    'kx': float(r['kx']),
                    'ky': float(r['ky']),
                    'kz': float(r['kz']),
                    'spin': int(r['spin']),
                    'band_index': int(r['band_index']),
                    'energy': float(r['energy'])
                })
            except (ValueError, KeyError):
                return 0.0

        def get_bands(kx0, ky0, kz0):
            up = {}
            down = {}
            for r in rows:
                if abs(r['kx'] - kx0) < tol_coord and abs(r['ky'] - ky0) < tol_coord and abs(r['kz'] - kz0) < tol_coord:
                    spin = r['spin']
                    idx = r['band_index']
                    en = r['energy']
                    if spin == 1:
                        up[idx] = en
                    elif spin == -1:
                        down[idx] = en
            common_bands = sorted(set(up.keys()) & set(down.keys()))
            up_vals = [up[b] for b in common_bands]
            down_vals = [down[b] for b in common_bands]
            return up_vals, down_vals

        up_g, down_g = get_bands(*target_kpoints["Gamma"])
        up_m, down_m = get_bands(*target_kpoints["Mp"])
        up_mpp, down_mpp = get_bands(*target_kpoints["Mpp"])

        # sub-scores
        s_gamma = 0.0
        if up_g and down_g:
            splits = [u - d for u, d in zip(up_g, down_g)]
            rms = math.sqrt(sum(s * s for s in splits) / len(splits)) if splits else 0.0
            if rms <= gamma_zero_rms:
                s_gamma = 1.0
            else:
                s_gamma = max(0.0, 1.0 - rms / gamma_zero_rms)

        s_mag = 0.0
        if up_m and down_m:
            splits_m = [u - d for u, d in zip(up_m, down_m)]
            max_abs = max(abs(s) for s in splits_m) if splits_m else 0.0
            s_mag = 1.0 if max_abs >= min_mag else 0.0

        s_mag_mpp = 0.0
        if up_mpp and down_mpp:
            splits_mpp = [u - d for u, d in zip(up_mpp, down_mpp)]
            max_abs_mpp = max(abs(s) for s in splits_mpp) if splits_mpp else 0.0
            s_mag_mpp = 1.0 if max_abs_mpp >= min_mag else 0.0

        s_sign = 0.0
        if up_m and down_m and up_mpp and down_mpp:
            splits_m = [u - d for u, d in zip(up_m, down_m)]
            splits_mpp = [u - d for u, d in zip(up_mpp, down_mpp)]
            n_nonzero = 0
            n_reversed = 0
            for sm, smpp in zip(splits_m, splits_mpp):
                if abs(sm) > 0.001 or abs(smpp) > 0.001:
                    n_nonzero += 1
                    if sm * smpp < 0:
                        n_reversed += 1
            if n_nonzero > 0:
                fraction = n_reversed / n_nonzero
                s_sign = min(1.0, fraction / frac_sign_rev)

        total = 0.2 * s_gamma + 0.2 * s_mag + 0.2 * s_mag_mpp + 0.4 * s_sign
        return min(1.0, max(0.0, total))


_SCORERS = {
    'step_03_band_structure': score_0,
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
