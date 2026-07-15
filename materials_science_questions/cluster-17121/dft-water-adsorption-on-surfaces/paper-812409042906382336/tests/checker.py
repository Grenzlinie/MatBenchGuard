import os
import json
import csv

# === author imports / helpers ===
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


# === block: score_0 (check id='step03_benzene_density_profile') ===
def score_0(artifact, step, ctx):
    try:
        # group by system and collect density vs z
        z_data = {}
        for row in artifact:
            sys = row.get("system", "").strip()
            z = float(row.get("z_nm", 0))
            dens = float(row.get("density_nm3", 0))
            if sys not in z_data:
                z_data[sys] = []
            z_data[sys].append((z, dens))
        if "NaNa" not in z_data or "ClCl" not in z_data:
            return 0.0
        # compute integrated density in [z_min, z_max] for each system
        z_min = step.get("thresholds", {}).get("z_min", 0.7)
        z_max = step.get("thresholds", {}).get("z_max", 0.931)
        integrals = {}
        for sys, points in z_data.items():
            points.sort(key=lambda x: x[0])
            zs = [p[0] for p in points]
            if len(zs) < 2:
                return 0.0
            avg_dz = (zs[-1] - zs[0]) / (len(zs) - 1)
            integral = 0.0
            for z, d in points:
                if z_min <= z <= z_max:
                    integral += d * avg_dz
            integrals[sys] = integral
        cl_val = integrals["ClCl"]
        na_val = integrals["NaNa"]
        if cl_val <= 0:
            return 0.0
        ratio = na_val / cl_val
        thr = step.get("thresholds", {}).get("ratio_threshold", 0.2)
        span = step.get("thresholds", {}).get("decay_span", 0.3)
        if ratio <= thr:
            return 1.0
        else:
            return max(0.0, 1.0 - (ratio - thr) / span)
    except Exception:
        return 0.0


# === block: score_1 (check id='step04_electric_field_profile') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        try:
            target_z = step.get("thresholds", {}).get("z_nm_target", 0.9)
            na_min = step.get("thresholds", {}).get("NaNa_min", 3.0)
            cl_max = step.get("thresholds", {}).get("ClCl_max", 1.0)
            e_na = None
            e_cl = None
            dist_na = float('inf')
            dist_cl = float('inf')
            for row in artifact:
                sys = row.get("system", "").strip()
                z = float(row.get("z_nm", 0))
                e = float(row.get("E_V_per_nm", 0))
                if sys == "NaNa":
                    d = abs(z - target_z)
                    if d < dist_na:
                        dist_na = d
                        e_na = e
                elif sys == "ClCl":
                    d = abs(z - target_z)
                    if d < dist_cl:
                        dist_cl = d
                        e_cl = e
            if e_na is None or e_cl is None:
                return 0.0
            cond1 = 1.0 if e_na >= na_min else 0.0
            cond2 = 1.0 if e_cl <= cl_max else 0.0
            return 0.5 * cond1 + 0.5 * cond2
        except Exception:
            return 0.0


_SCORERS = {
    'step03_benzene_density_profile': score_0,
    'step04_electric_field_profile': score_1,
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
