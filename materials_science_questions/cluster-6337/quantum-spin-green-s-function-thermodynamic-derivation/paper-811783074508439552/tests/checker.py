import os
import json
import csv

# === author imports / helpers ===
import csv, os, math, json


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


# === block: score_0 (check id='magnetization') ===
def score_0(artifact, step, ctx):
    try:
        # Expect optional columns D_div_J and Omega_div_J to identify parameter sets
        rows = [r for r in artifact if "T_div_J" in r and "M" in r and "D_div_J" in r and "Omega_div_J" in r]
        if not rows:
            return 0.0
        groups = {}
        for r in rows:
            d = float(r["D_div_J"])
            o = float(r["Omega_div_J"])
            t = float(r["T_div_J"])
            m = float(r["M"])
            groups.setdefault((d, o), []).append((t, m))
        curves = step.get("curves", [])
        tol = step.get("tolerance", 0.1)
        errors = []
        for c in curves:
            d = c["D"]
            o = c["Omega"]
            key = (d, o)
            if key not in groups:
                return 0.0
            agent_data = sorted(groups[key], key=lambda x: x[0])
            ref_pts = c["reference_points"]
            # Compute MAE by linear interpolation of agent data at each reference T
            total_err = 0.0
            count = 0
            for (tr, mr) in ref_pts:
                # find two nearest agent T's
                ts = [p[0] for p in agent_data]
                ms = [p[1] for p in agent_data]
                if tr <= ts[0]:
                    interp_m = ms[0]
                elif tr >= ts[-1]:
                    interp_m = ms[-1]
                else:
                    # binary search
                    idx = 0
                    for i in range(len(ts)-1):
                        if ts[i] <= tr <= ts[i+1]:
                            idx = i
                            break
                    t1, m1 = ts[idx], ms[idx]
                    t2, m2 = ts[idx+1], ms[idx+1]
                    if t2 - t1 > 0:
                        interp_m = m1 + (m2 - m1) * (tr - t1) / (t2 - t1)
                    else:
                        interp_m = m1
                if interp_m < 0:
                    interp_m = 0.0
                if interp_m > 1.0:
                    interp_m = 1.0
                total_err += abs(interp_m - mr)
                count += 1
            if count > 0:
                errors.append(total_err / count)
            else:
                errors.append(0.0)
        if not errors:
            return 0.0
        overall_mae = sum(errors) / len(errors)
        if overall_mae <= tol:
            return 1.0
        else:
            return max(0.0, 1.0 - (overall_mae - tol) / 0.3)
    except Exception:
        return 0.0


# === block: score_1 (check id='spinwave') ===
def score_1(artifact, step, ctx):
    try:
        rows = [r for r in artifact if "k_x" in r and "k_y" in r and "E" in r and "k_path" in r]
        if not rows:
            return 0.0
        # Check for parameter identification; attempt to read D_div_J from a column or from k_path string
        # Use the fact that required_D and Omega are known from step.
        required_D = step.get("required_D", [])
        omega = step.get("Omega", 0.005)
        T_val = step.get("T_div_J", 0.1)
        ref_by_D = step.get("reference_points", {})
        k_tol = step.get("k_tolerance", 0.001)
        E_tol = step.get("E_tolerance", 0.3)
        total_score = 0.0
        n_D = 0
        for d_val in required_D:
            d_str = str(d_val)
            # filter rows belonging to this D; assume agent includes D_div_J column, else try to parse from k_path
            sub_rows = []
            for r in rows:
                if "D_div_J" in r:
                    if abs(float(r["D_div_J"]) - d_val) < 1e-6:
                        sub_rows.append(r)
                else:
                    # fallback: check if k_path contains "D=..."
                    if f"D={d_str}" in r["k_path"] or f"d={d_str}" in r["k_path"]:
                        sub_rows.append(r)
            if not sub_rows:
                continue
            n_D += 1
            ref_kpts = ref_by_D.get(d_str, {}).get("k_points", [])
            if not ref_kpts:
                continue
            d_score = 0.0
            n_pts = 0
            for ref in ref_kpts:
                xr, yr, Er = ref[0], ref[1], ref[2]
                # find closest k-point
                best_dist = float('inf')
                best_E = None
                for r in sub_rows:
                    x = float(r["k_x"])
                    y = float(r["k_y"])
                    dist = math.sqrt((x - xr)**2 + (y - yr)**2)
                    if dist < best_dist:
                        best_dist = dist
                        best_E = float(r["E"])
                if best_dist > k_tol or best_E is None:
                    continue
                n_pts += 1
                if abs(best_E - Er) <= E_tol:
                    d_score += 1.0
            if n_pts > 0:
                total_score += d_score / n_pts
        if n_D == 0:
            return 0.0
        return total_score / n_D
    except Exception:
        return 0.0


# === block: score_2 (check id='tc') ===
def score_2(artifact, step, ctx):
    try:
        rows = artifact  # list of dicts
        required_entries = step.get("required_entries", [])
        rel_tol = step.get("relative_tolerance", 0.10)
        total_score = 0.0
        n_entries = 0
        for entry in required_entries:
            param = entry["parameter"]
            val = entry["value"]
            ref_tc = entry["Tc_div_J"]
            # find matching row
            matched = None
            for r in rows:
                if r.get("parameter", "").strip() == param:
                    try:
                        r_val = float(r["value"])
                    except:
                        continue
                    if abs(r_val - val) < 1e-9:
                        matched = r
                        break
            if matched is None:
                continue
            try:
                agent_tc = float(matched["Tc_div_J"])
            except:
                continue
            n_entries += 1
            if ref_tc == 0.0:
                if agent_tc == 0.0:
                    total_score += 1.0
                continue
            rel_err = abs(agent_tc - ref_tc) / abs(ref_tc)
            if rel_err <= rel_tol:
                total_score += 1.0
            else:
                total_score += max(0.0, 1.0 - (rel_err - rel_tol) / 0.5)
        if n_entries == 0:
            return 0.0
        return total_score / n_entries
    except Exception:
        return 0.0


_SCORERS = {
    'magnetization': score_0,
    'spinwave': score_1,
    'tc': score_2,
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
