import os
import json
import csv

# === author imports / helpers ===
import csv, math, os


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
    import csv, math, os
    outputs_dir = "/app/outputs"
    occ0_path = os.path.join(outputs_dir, "occupancy_phi_0.csv")
    occ13_path = os.path.join(outputs_dir, "occupancy_phi_1.3.csv")
    transport_path = os.path.join(outputs_dir, "transport_summary.csv")
    ctx = {}

    def compute_weighted_mean(rows):
        if not rows or len(rows) < 2:
            return None
        nc = [float(r["N_c"]) for r in rows]
        pd = [float(r["probability_density"]) for r in rows]
        bin_width = nc[1] - nc[0]
        return sum(ci * pi for ci, pi in zip(nc, pd)) * bin_width

    try:
        with open(occ0_path) as f:
            occ0 = list(csv.DictReader(f))
        ctx["occ0_mean"] = compute_weighted_mean(occ0)
        ctx["occ0_data"] = occ0
    except Exception:
        ctx["occ0_mean"] = None
        ctx["occ0_data"] = []

    try:
        with open(occ13_path) as f:
            occ13 = list(csv.DictReader(f))
        ctx["occ13_mean"] = compute_weighted_mean(occ13)
    except Exception:
        ctx["occ13_mean"] = None

    try:
        with open(transport_path) as f:
            rows = list(csv.DictReader(f))
        ctx["transport_rows"] = rows
    except Exception:
        ctx["transport_rows"] = []

    return ctx


# === block: score_0 (check id='step_occ_phi0_shape') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, list) or not artifact:
        return 0.0
    cols = set(artifact[0].keys())
    if "N_c" not in cols or "probability_density" not in cols:
        return 0.0
    try:
        nc_vals = [float(r["N_c"]) for r in artifact]
        pd_vals = [float(r["probability_density"]) for r in artifact]
    except ValueError:
        return 0.0
    if min(nc_vals) < -0.01 or max(nc_vals) > 8.01:
        return 0.0
    if min(pd_vals) < -1e-12:
        return 0.0
    if len(artifact) < 2:
        return 0.0
    bin_width = nc_vals[1] - nc_vals[0]
    integral = sum(p * bin_width for p in pd_vals)
    if abs(integral - 1.0) > 0.05:
        return 0.0
    # check uniform bin spacing
    for i in range(1, len(nc_vals)-1):
        if abs((nc_vals[i+1]-nc_vals[i]) - bin_width) > 1e-9:
            return 0.0
    return 1.0


# === block: score_1 (check id='step_occ_phi13_shape') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, list) or not artifact:
        return 0.0
    cols = set(artifact[0].keys())
    if "N_c" not in cols or "probability_density" not in cols:
        return 0.0
    try:
        nc_vals = [float(r["N_c"]) for r in artifact]
        pd_vals = [float(r["probability_density"]) for r in artifact]
    except ValueError:
        return 0.0
    if min(nc_vals) < -0.01 or max(nc_vals) > 8.01:
        return 0.0
    if min(pd_vals) < -1e-12:
        return 0.0
    if len(artifact) < 2:
        return 0.0
    bin_width = nc_vals[1] - nc_vals[0]
    integral = sum(p * bin_width for p in pd_vals)
    if abs(integral - 1.0) > 0.05:
        return 0.0
    for i in range(1, len(nc_vals)-1):
        if abs((nc_vals[i+1]-nc_vals[i]) - bin_width) > 1e-9:
            return 0.0
    return 1.0


# === block: score_2 (check id='step_transport_shape') ===
def score_2(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) < 2:
        return 0.0
    required = {"phi", "avg_N_w", "N_exit", "t_tr_ps"}
    try:
        for row in artifact:
            if not required.issubset(row.keys()):
                return 0.0
            float(row["phi"]); float(row["avg_N_w"]); int(row["N_exit"]); float(row["t_tr_ps"])
        phis = {float(r["phi"]) for r in artifact}
        if 0.0 not in phis or 1.3 in phis is False:
            return 0.0  # check presence of both values
        return 1.0
    except (ValueError, KeyError):
        return 0.0


# === block: score_3 (check id='step_occ_trend') ===
def score_3(artifact, step, ctx):
    mean0 = ctx.get("occ0_mean")
    mean13 = ctx.get("occ13_mean")
    if mean0 is None or mean13 is None:
        return 0.0
    return 1.0 if mean13 < mean0 - 1e-12 else 0.0


# === block: score_4 (check id='step_transport_trend') ===
def score_4(artifact, step, ctx):
    rows = ctx.get("transport_rows", [])
    if not rows:
        return 0.0
    try:
        row0 = next((r for r in rows if abs(float(r["phi"]) - 0.0) < 0.01), None)
        row13 = next((r for r in rows if abs(float(r["phi"]) - 1.3) < 0.01), None)
    except (KeyError, ValueError):
        return 0.0
    if row0 is None or row13 is None:
        return 0.0
    try:
        avg0 = float(row0["avg_N_w"])
        avg13 = float(row13["avg_N_w"])
        nexit0 = float(row0["N_exit"])
        nexit13 = float(row13["N_exit"])
        ttr0 = float(row0["t_tr_ps"])
        ttr13 = float(row13["t_tr_ps"])
    except (KeyError, ValueError):
        return 0.0
    passed = 0
    if avg13 < avg0 - 1e-12: passed += 1
    if nexit13 < nexit0 - 0.5: passed += 1
    if ttr13 > ttr0 + 1e-12: passed += 1
    return passed / 3.0


_SCORERS = {
    'step_occ_phi0_shape': score_0,
    'step_occ_phi13_shape': score_1,
    'step_transport_shape': score_2,
    'step_occ_trend': score_3,
    'step_transport_trend': score_4,
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
