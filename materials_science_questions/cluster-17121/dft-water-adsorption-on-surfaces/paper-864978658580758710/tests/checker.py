import os
import json
import csv

# === author imports / helpers ===
import csv, json, os, math, statistics


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
    spec = json.loads(open("/tests/grading_spec.json").read())
    return {
        "gold": spec.get("gold", {}),
        "tolerances": spec.get("tolerances", {}),
        "expected_counts": spec.get("expected_snapshot_counts", {}),
        "output_contract": spec.get("output_contract", {})
    }


# === block: score_0 (check id='check_ds_energies') ===
def score_0(artifact, step, ctx):
    rows = [r for r in artifact if all(k in r for k in ["time_ps", "ds_energy_above_vbm_eV", "vbm_cbm_gap_eV"])]
    d3_rows = []
    u_rows = []
    for r in rows:
        t = float(r["time_ps"])
        if t <= 35.7:
            d3_rows.append(r)
        else:
            u_rows.append(r)

    if not d3_rows or not u_rows:
        return 0.0

    def stats(ky):
        vals = [float(r[ky]) for r in d3_rows]
        return statistics.mean(vals) if vals else 0.0, statistics.stdev(vals) if len(vals) > 1 else 0.0

    ds_d3_mean, ds_d3_std = stats("ds_energy_above_vbm_eV")
    gap_d3_mean, gap_d3_std = stats("vbm_cbm_gap_eV")

    def stats_u(ky):
        vals = [float(r[ky]) for r in u_rows]
        return statistics.mean(vals) if vals else 0.0, statistics.stdev(vals) if len(vals) > 1 else 0.0

    ds_u_mean, ds_u_std = stats_u("ds_energy_above_vbm_eV")
    gap_u_mean, gap_u_std = stats_u("vbm_cbm_gap_eV")

    gold = ctx.get("gold", {})
    tol = ctx.get("tolerances", {})
    tol_ds_mean = tol.get("ds_mean", 0.15)
    tol_ds_std = tol.get("ds_std", 0.10)
    tol_gap_mean = tol.get("gap_mean", 0.15)
    tol_gap_std = tol.get("gap_std", 0.10)

    def in_tol(v, g, t):
        return abs(v - g) <= t

    score = 0.0
    count = 0
    gold_d3 = gold.get("pbe_d3", {})
    gold_ud3 = gold.get("pbe_u_d3", {})

    if in_tol(ds_d3_mean, gold_d3.get("ds_mean", 0.83), tol_ds_mean):
        score += 1
    count += 1
    if in_tol(ds_d3_std, gold_d3.get("ds_std", 0.33), tol_ds_std):
        score += 1
    count += 1
    if in_tol(gap_d3_mean, gold_d3.get("gap_mean", 1.95), tol_gap_mean):
        score += 1
    count += 1
    if in_tol(gap_d3_std, gold_d3.get("gap_std", 0.22), tol_gap_std):
        score += 1
    count += 1

    if in_tol(ds_u_mean, gold_ud3.get("ds_mean", 0.37), tol_ds_mean):
        score += 1
    count += 1
    if in_tol(ds_u_std, gold_ud3.get("ds_std", 0.20), tol_ds_std):
        score += 1
    count += 1
    if in_tol(gap_u_mean, gold_ud3.get("gap_mean", 2.06), tol_gap_mean):
        score += 1
    count += 1
    if in_tol(gap_u_std, gold_ud3.get("gap_std", 0.17), tol_gap_std):
        score += 1
    count += 1

    numeric_sub = score / count if count else 0.0

    exp_counts = ctx.get("expected_counts", {})
    exp_d3 = exp_counts.get("pbe_d3", 179)
    exp_u = exp_counts.get("pbe_u_d3", 72)
    snap_tol = tol.get("snapshot_count", 2)
    count_ok = 0.0
    if abs(len(d3_rows) - exp_d3) <= snap_tol:
        count_ok += 0.5
    if abs(len(u_rows) - exp_u) <= snap_tol:
        count_ok += 0.5

    return 0.8 * numeric_sub + 0.2 * count_ok


# === block: score_1 (check id='check_ds_summary') ===
def score_1(artifact, step, ctx):
    required_cols = ["segment", "mean_ds_energy_eV", "std_ds_energy_eV", "mean_vbm_cbm_gap_eV", "std_vbm_cbm_gap_eV"]
    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0
    cols = set(artifact[0].keys())
    if all(col in cols for col in required_cols):
        return 1.0
    return 0.0


# === block: score_2 (check id='check_alignment') ===
def score_2(artifact, step, ctx):
    required_keys = ["vbm_vs_rhe_eV", "ds_mean_vs_rhe_eV", "ds_std_vs_rhe_eV", "offset_from_oer_eV"]
    if not isinstance(artifact, dict):
        return 0.0
    if not all(k in artifact for k in required_keys):
        return 0.0

    align_gold = ctx.get("gold", {}).get("alignment", {})
    tol_val = ctx.get("tolerances", {}).get("alignment_val", 0.15)

    def in_tol(v, g, t):
        return abs(v - g) <= t

    score = 0.0
    for k in required_keys:
        agent_v = float(artifact.get(k, 0))
        gold_v = align_gold.get(k, 0.0)
        if in_tol(agent_v, gold_v, tol_val):
            score += 1.0
    return score / len(required_keys)


# === block: score_3 (check id='check_hbond') ===
def score_3(artifact, step, ctx):
    hbond_gold = ctx.get("gold", {}).get("hbond", {})
    tol = ctx.get("tolerances", {})
    tau_tol = tol.get("hbond_tau_relative", 0.20)
    r2_min = tol.get("hbond_r2_min", 0.9)

    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0

    rows = artifact
    score = 0.0
    count = 0
    for row in rows:
        surf = str(row.get("surface_type", ""))
        bond = str(row.get("bond_type", ""))
        try:
            tau = float(row.get("tau_ps", 0))
            r2 = float(row.get("r_squared", 0))
        except (ValueError, TypeError):
            continue
        expected = hbond_gold.get(surf, {}).get(bond, None)
        if expected is None:
            continue
        gold_tau = expected.get("tau", 0.0)
        gold_r2 = expected.get("r2", 0.0)
        tau_ok = abs(tau - gold_tau) <= tau_tol * gold_tau
        r2_ok = r2 >= r2_min
        if tau_ok and r2_ok:
            row_score = 1.0
        else:
            row_score = 0.0
        score += row_score
        count += 1

    if count == 0:
        return 0.0
    return score / count


_SCORERS = {
    'check_ds_energies': score_0,
    'check_ds_summary': score_1,
    'check_alignment': score_2,
    'check_hbond': score_3,
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
