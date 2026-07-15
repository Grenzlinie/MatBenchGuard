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
    return {}


# === block: score_0 (check id='ambient_properties') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    metals = ["Np","Pu","Am","Cm"]
    target = step.get("target_values", {})
    if not target:
        return 0.0
    tol_moments = step.get("tolerances", {}).get("moments", 0.2)
    tol_eig = step.get("tolerances", {}).get("eigenvalues", 0.03)
    tol_od = step.get("tolerances", {}).get("OD", 0.05)
    metal_scores = []
    for metal in metals:
        if metal not in artifact:
            metal_scores.append(0.0)
            continue
        vals = artifact[metal]
        if not isinstance(vals, dict):
            metal_scores.append(0.0)
            continue
        tval = target.get(metal, {})
        if not tval or not isinstance(tval, dict):
            metal_scores.append(0.0)
            continue
        checks = 0
        passed = 0
        # moments
        for field in ["S","L","J","mu_eff"]:
            if field in vals and field in tval:
                v = vals[field]
                tv = tval[field]
                if isinstance(v, (int, float)) and isinstance(tv, (int, float)):
                    checks += 1
                    if abs(v - tv) <= tol_moments:
                        passed += 1
                elif v is not None and tv is not None:
                    try:
                        vf = float(v)
                        tf = float(tv)
                        checks += 1
                        if abs(vf - tf) <= tol_moments:
                            passed += 1
                    except (ValueError, TypeError):
                        pass
        # occupation eigenvalues
        if "occupation_eigenvalues" in vals and "occupation_eigenvalues" in tval:
            ag = vals["occupation_eigenvalues"]
            tg = tval["occupation_eigenvalues"]
            if isinstance(ag, list) and isinstance(tg, list) and len(ag) == len(tg):
                checks += 1
                try:
                    ag_filtered = [float(x) for x in ag if x is not None]
                    tg_filtered = [float(x) for x in tg if x is not None]
                    if len(ag_filtered) == len(tg_filtered):
                        max_diff = max(abs(a - b) for a, b in zip(ag_filtered, tg_filtered))
                        if max_diff <= tol_eig:
                            passed += 1
                except (TypeError, ValueError):
                    pass
        # OD
        for field in ["OD_LS","OD_jmj"]:
            if field in vals and field in tval:
                v = vals[field]
                tv = tval[field]
                if isinstance(v, (int, float)) and isinstance(tv, (int, float)):
                    checks += 1
                    if abs(v - tv) <= tol_od:
                        passed += 1
                elif v is not None and tv is not None:
                    try:
                        vf = float(v)
                        tf = float(tv)
                        checks += 1
                        if abs(vf - tf) <= tol_od:
                            passed += 1
                    except (ValueError, TypeError):
                        pass
        metal_scores.append(passed / max(checks, 1))
    return sum(metal_scores) / len(metal_scores) if metal_scores else 0.0


# === block: score_1 (check id='bandwidth_volume') ===
def score_1(artifact, step, ctx):
    import csv
    import io
    from collections import defaultdict

    def score(artifact, step, ctx):
        if not artifact or not isinstance(artifact, list):
            return 0.0
        rows = artifact
        # check columns
        cols_needed = {"material","volume_ratio","j5_2_bandwidth","j7_2_bandwidth","total_magnetic_moment"}
        if not rows or not cols_needed.issubset(rows[0].keys()):
            return 0.0
        data = defaultdict(list)
        for r in rows:
            try:
                mat = r["material"]
                v = float(r["volume_ratio"])
                j5 = float(r["j5_2_bandwidth"])
                j7 = float(r["j7_2_bandwidth"])
                data[mat].append((v, j5, j7))
            except (ValueError, KeyError):
                pass
        metals = ["Np","Pu","Am","Cm"]
        mono_checks = 0
        mono_total = 0
        pu_increase_ok = False
        for mat in metals:
            if mat not in data:
                continue
            pts = sorted(data[mat], key=lambda x: x[0], reverse=True)  # decreasing volume (largest first)
            if len(pts) < 2:
                continue
            j5_vals = [p[1] for p in pts]
            j7_vals = [p[2] for p in pts]
            j5_mono = all(j5_vals[i+1] >= j5_vals[i] for i in range(len(j5_vals)-1))
            j7_mono = all(j7_vals[i+1] >= j7_vals[i] for i in range(len(j7_vals)-1))
            mono_checks += (int(j5_mono) + int(j7_mono))
            mono_total += 2
            if mat == "Pu":
                v0 = None
                v80 = None
                for p in pts:
                    if abs(p[0] - 1.0) < 1e-6:
                        v0 = p[1]
                    if abs(p[0] - 0.80) < 1e-6:
                        v80 = p[1]
                if v0 is not None and v80 is not None:
                    inc = v80 - v0
                    ref = step.get("targets", {}).get("pu_j5_2_increase", 1.0)
                    tol = step.get("targets", {}).get("pu_tolerance", 0.3)
                    if abs(inc - ref) <= tol:
                        pu_increase_ok = True
        monotonic_score = mono_checks / max(mono_total, 1)
        pu_score = 0.3 if pu_increase_ok else 0.0
        return round(min(0.7 * monotonic_score + pu_score, 1.0), 6)


_SCORERS = {
    'ambient_properties': score_0,
    'bandwidth_volume': score_1,
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
