import os
import json
import csv

# === author imports / helpers ===
import os
import json
import csv
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


# === block: score_0 (check id='step_extremum') ===
def score_0(artifact, step, ctx):
    import math

    def _compute_ref():
        R = 8.314462618
        sigma = 1.0
        v_A = 1e-5
        T = 300.0
        n_A = 1e-4
        N = 1e14
        x_A_sat = 1e-5
        S_ini = n_A / x_A_sat
        RT = R * T
        num = 5000
        r_start, r_end = 0.01, 10.0
        dr = (r_end - r_start) / (num - 1)
        r_vals = [r_start + i * dr for i in range(num)]
        G_vals = []
        for r_nm in r_vals:
            r_i = r_nm * 1e-9
            nAn = (4 * math.pi * r_i**3 * N) / (3 * v_A)
            term1 = 4 * math.pi * r_i**2 * sigma
            term2 = (nAn * RT / N) * math.log(S_ini)
            # guard log domains
            arg3_num = 1 - nAn / n_A
            arg3_den = 1 - nAn
            if arg3_num > 0 and arg3_den > 0:
                term3 = (n_A - nAn) * (RT / N) * math.log(arg3_num / arg3_den)
            else:
                term3 = 0.0
            denom4 = 1 - nAn
            if denom4 > 0:
                term4 = (1 - n_A) * (RT / N) * math.log(1.0 / denom4)
            else:
                term4 = 0.0
            G = term1 - term2 + term3 + term4
            G_vals.append(G)

        # Numerical derivative
        dG = [0.0] * num
        dG[0] = (G_vals[1] - G_vals[0]) / dr
        dG[-1] = (G_vals[-1] - G_vals[-2]) / dr
        for i in range(1, num-1):
            dG[i] = (G_vals[i+1] - G_vals[i-1]) / (2 * dr)

        # Identify extrema
        max_idx = None
        min_idx = None
        for i in range(num-1):
            if dG[i] > 0 and dG[i+1] < 0:
                max_idx = i
                break
        if max_idx is not None:
            for i in range(max_idx+1, num-1):
                if dG[i] < 0 and dG[i+1] > 0:
                    min_idx = i
                    break
        # Fallback: use global extremum of G in interior
        margin = num // 20
        if max_idx is None:
            max_idx = max(range(margin, num-margin), key=lambda i: G_vals[i])
        if min_idx is None:
            min_idx = min(range(margin, num-margin), key=lambda i: G_vals[i])

        def _refine(idx):
            dri = r_vals[idx+1] - r_vals[idx]
            dd = dG[idx+1] - dG[idx]
            if abs(dd) < 1e-300:
                r_ext = r_vals[idx]
            else:
                r_ext = r_vals[idx] - dG[idx] * dri / dd
            t = (r_ext - r_vals[idx]) / dri if dri != 0 else 0.0
            G_ext = G_vals[idx] + t * (G_vals[idx+1] - G_vals[idx])
            return r_ext, G_ext

        r_max_r, dG_max = _refine(max_idx)
        r_min_r, dG_min = _refine(min_idx)
        return r_max_r, dG_max, r_min_r, dG_min

    def _tol_score(ref, val, tol):
        if ref == 0:
            return 1.0 if abs(val) < 1e-20 else 0.0
        re = abs(val - ref) / abs(ref)
        if re <= tol:
            return 1.0
        elif re >= 2 * tol:
            return 0.0
        else:
            return 1.0 - (re - tol) / tol

    rows = artifact
    if not isinstance(rows, list) or len(rows) != 1:
        return 0.0
    row = rows[0]
    try:
        r_max = float(row['r_max'])
        dG_max = float(row['DeltaG_max'])
        r_min = float(row['r_min'])
        dG_min = float(row['DeltaG_min'])
    except (ValueError, KeyError):
        return 0.0

    ref_r_max, ref_dG_max, ref_r_min, ref_dG_min = _compute_ref()
    s1 = _tol_score(ref_r_max, r_max, 0.05)
    s2 = _tol_score(ref_dG_max, dG_max, 0.10)
    s3 = _tol_score(ref_r_min, r_min, 0.05)
    s4 = _tol_score(ref_dG_min, dG_min, 0.10)
    return (s1 + s2 + s3 + s4) / 4.0


_SCORERS = {
    'step_extremum': score_0,
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
