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
    return {}


# === block: score_0 (check id='magnetization_decay') ===
def score_0(artifact, step, ctx):
    # Step 01: structural checks on M(t)
    def score(artifact, step, ctx):
        if not artifact or len(artifact) < 2:
            return 0.0
        try:
            t = [float(r['t']) for r in artifact]
            mp = [float(r['M_parallel']) for r in artifact]
            mpe = [float(r['M_perpendicular']) for r in artifact]
            n = len(t)
            # Check monotonic decreasing (allow tiny noise)
            mono_par_viol = 0
            mono_perp_viol = 0
            for i in range(n-1):
                if mp[i] + 1e-12 < mp[i+1]:
                    mono_par_viol += 1
                if mpe[i] + 1e-12 < mpe[i+1]:
                    mono_perp_viol += 1
            mono_par_score = max(0.0, 1.0 - mono_par_viol / (n-1))
            mono_perp_score = max(0.0, 1.0 - mono_perp_viol / (n-1))
            # Check ordering: M_parallel >= M_perpendicular at every time
            order_viol = sum(1 for a,b in zip(mp,mpe) if a + 1e-12 < b)
            order_score = max(0.0, 1.0 - order_viol / n)
            # Initial condition near 1
            init_par_ok = abs(mp[0] - 1.0) < 0.05
            init_perp_ok = abs(mpe[0] - 1.0) < 0.05
            init_score = (1.0 if init_par_ok and init_perp_ok else 0.0)
            # Final values near 0
            final_par_ok = mp[-1] < 0.02
            final_perp_ok = mpe[-1] < 0.02
            final_score = (1.0 if final_par_ok and final_perp_ok else 0.0)
            weights = [0.3, 0.3, 0.25, 0.1, 0.05]
            scores = [mono_par_score, order_score, init_score, final_score, mono_perp_score]
            return sum(w*s for w,s in zip(weights, scores))
        except (ValueError, TypeError):
            return 0.0


# === block: score_1 (check id='f_epsilon') ===
def score_1(artifact, step, ctx):
    # Step 02: structural checks on f(epsilon)
    def score(artifact, step, ctx):
        if not artifact or len(artifact) < 2:
            return 0.0
        eps = [float(r['epsilon']) for r in artifact]
        fp = [float(r['f_parallel']) for r in artifact]
        fpe = [float(r['f_perpendicular']) for r in artifact]
        # Check non-negative
        if any(v < 0 for v in fp) or any(v < 0 for v in fpe):
            return 0.0
        # Check normalization over epsilon grid (assume uniform step)
        deps = eps[1] - eps[0]
        integral_p = sum(fp)*deps
        integral_pe = sum(fpe)*deps
        norm_p_ok = abs(integral_p - 1.0) < 0.1
        norm_pe_ok = abs(integral_pe - 1.0) < 0.1
        norm_score = (1.0 if norm_p_ok and norm_pe_ok else 0.0)
        # Peak epsilon ordering
        if max(fp) > 0 and max(fpe) > 0:
            idx_p = fp.index(max(fp))
            idx_pe = fpe.index(max(fpe))
            peak_order_ok = eps[idx_p] > eps[idx_pe]
        else:
            peak_order_ok = False
        peak_score = 1.0 if peak_order_ok else 0.0
        # Simple shape: both densities should be non-trivial (max > 0)
        shape_score = 1.0 if max(fp) > 0 and max(fpe) > 0 else 0.0
        weights = [0.3, 0.4, 0.3]
        scores = [norm_score, peak_score, shape_score]
        return sum(w*s for w,s in zip(weights, scores))


# === block: score_2 (check id='epsilon_bar_I') ===
def score_2(artifact, step, ctx):
    # Step 03: structural checks on epsilon_bar vs I
    def score(artifact, step, ctx):
        if not artifact or len(artifact) != 11:
            return 0.0
        I_vals = []
        chain_par = []
        chain_perp = []
        pyr_par = []
        pyr_perp = []
        for row in artifact:
            try:
                I_vals.append(float(row['I_relative']))
                chain_par.append(float(row['ε̄_chain_parallel']))
                chain_perp.append(float(row['ε̄_chain_perp']))
                pyr_par.append(float(row['ε̄_pyramid_parallel']))
                pyr_perp.append(float(row['ε̄_pyramid_perp']))
            except:
                return 0.0
        n = len(I_vals)
        # Check expected I range (0 to 1 step 0.1)
        if any(abs(I_vals[i] - i*0.1) > 0.001 for i in range(n)):
            return 0.0
        # Monotonic trends (allow small violations)
        # chain_par should be non-decreasing
        mono_par = all(chain_par[i+1] + 1e-12 >= chain_par[i] for i in range(n-1))
        # chain_perp should be non-increasing
        mono_perp = all(chain_perp[i+1] - 1e-12 <= chain_perp[i] for i in range(n-1))
        mono_score = (1.0 if mono_par and mono_perp else 0.0)
        # Pyramid: small difference between parallel and perpendicular across I
        max_diff = max(abs(pyr_par[i]-pyr_perp[i]) for i in range(n))
        pyr_diff_score = 1.0 if max_diff < 0.8 else max(0.0, 1.0 - (max_diff - 0.8)/0.5)
        # Pyramid I-dependence small: range of pyr_par < 0.5
        pyr_range = max(pyr_par) - min(pyr_par)
        pyr_range_score = 1.0 if pyr_range < 0.5 else max(0.0, 1.0 - (pyr_range-0.5)/0.5)
        weights = [0.35, 0.35, 0.15, 0.15]
        scores = [mono_score, mono_score * 0.5 + 0.5, pyr_diff_score, pyr_range_score]  # give partial credit if only one direction holds
        # Actually let's compute direct: chain_par monotonic, chain_perp monotonic, pyramid diff, pyramid range
        weights = [0.3, 0.3, 0.2, 0.2]
        scores = [1.0 if mono_par else 0.0,
                  1.0 if mono_perp else 0.0,
                  pyr_diff_score,
                  pyr_range_score]
        return sum(w*s for w,s in zip(weights, scores))


_SCORERS = {
    'magnetization_decay': score_0,
    'f_epsilon': score_1,
    'epsilon_bar_I': score_2,
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
