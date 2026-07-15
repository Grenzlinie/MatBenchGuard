import os
import json
import csv

# === author imports / helpers ===
import os, re, csv, math


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
    return {
        "e_shell_target": 4.0,
        "e_shell_tolerance": 0.5,
        "N_TBA_shell_target": 56,
        "N_TBA_shell_tolerance": 5,
        "r_wall_low": 8.0,
        "r_core_high": 4.0,
        "min_ratio": 2.0,
    }


# === block: score_0 (check id='density_profiles') ===
def score_0(artifact, step, ctx):
    if not artifact:
        return 0.0
    rows = artifact
    comps = {}
    for row in rows:
        try:
            comp = float(row['composition'])
            r = float(row['radial_distance_angstrom'])
            d_tba = float(row['density_TBA'])
            d_tol = float(row['density_TOL'])
        except (KeyError, ValueError):
            continue
        if comp not in comps:
            comps[comp] = []
        comps[comp].append((r, d_tba, d_tol))

    required_comps = [0.49, 0.71]
    for c in required_comps:
        if c not in comps or not comps[c]:
            return 0.0

    def avg_in_range(data, r_low, r_high, idx):
        vals = [d[idx] for d in data if r_low <= d[0] < r_high]
        return sum(vals)/len(vals) if vals else 0.0

    min_ratio = ctx.get('min_ratio', 2.0)
    r_core = ctx.get('r_core_high', 4.0)
    r_wall = ctx.get('r_wall_low', 8.0)

    # x_TBA = 0.49: TBA should be enriched in the shell (r >= r_wall),
    #             TOL enriched in the core (r < r_core).
    comp049 = comps[0.49]
    tba_shell_049 = avg_in_range(comp049, r_wall, 999.0, 1)
    tol_shell_049 = avg_in_range(comp049, r_wall, 999.0, 2)
    tol_core_049 = avg_in_range(comp049, 0.0, r_core, 2)
    tba_core_049 = avg_in_range(comp049, 0.0, r_core, 1)
    cond1 = tba_shell_049 > min_ratio * tol_shell_049 and tba_shell_049 > 0
    cond2 = tol_core_049 > min_ratio * tba_core_049 and tol_core_049 > 0

    # x_TBA = 0.71: same pattern as above.
    comp071 = comps[0.71]
    tba_shell_071 = avg_in_range(comp071, r_wall, 999.0, 1)
    tol_shell_071 = avg_in_range(comp071, r_wall, 999.0, 2)
    tol_core_071 = avg_in_range(comp071, 0.0, r_core, 2)
    tba_core_071 = avg_in_range(comp071, 0.0, r_core, 1)
    cond3 = tba_shell_071 > min_ratio * tol_shell_071 and tba_shell_071 > 0
    cond4 = tol_core_071 > min_ratio * tba_core_071 and tol_core_071 > 0

    if cond1 and cond2 and cond3 and cond4:
        return 1.0
    # partial credit if at least one composition shows the two crucial patterns
    if (cond1 and cond2) or (cond3 and cond4):
        return 0.6
    return 0.0


# === block: score_1 (check id='shell_analysis') ===
def score_1(artifact, step, ctx):
    if not artifact:
        return 0.0
    text = artifact
    e_match = re.search(r'e_shell_angstrom\s*=\s*([0-9]*\.?[0-9]+)', text)
    n_match = re.search(r'N_TBA_shell\s*=\s*([0-9]+)', text)
    if not e_match or not n_match:
        return 0.0

    try:
        e_shell = float(e_match.group(1))
        n_shell = int(n_match.group(1))
    except (ValueError, TypeError):
        return 0.0

    target_e = ctx['e_shell_target']
    tol_e = ctx['e_shell_tolerance']
    target_n = ctx['N_TBA_shell_target']
    tol_n = ctx['N_TBA_shell_tolerance']

    ok_e = abs(e_shell - target_e) <= tol_e
    ok_n = abs(n_shell - target_n) <= tol_n

    if ok_e and ok_n:
        return 1.0
    # partial credit if exactly one matches
    if ok_e or ok_n:
        return 0.5
    return 0.0


_SCORERS = {
    'density_profiles': score_0,
    'shell_analysis': score_1,
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
