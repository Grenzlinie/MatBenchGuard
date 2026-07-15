import os
import json
import csv

# === author imports / helpers ===
import numpy as np
import json
import os


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
    def parse_xyz(path):
        try:
            with open(path) as f:
                lines = f.readlines()
            n_atoms = int(lines[0].strip())
            atoms = []
            for line in lines[2:2+n_atoms]:
                parts = line.split()
                elem = parts[0]
                coords = np.array([float(x) for x in parts[1:4]])
                atoms.append((elem, coords))
            return atoms
        except Exception:
            return []

    outputs_dir = os.path.join("/app", "outputs")
    mono_atoms = parse_xyz(os.path.join(outputs_dir, "monometallic_optimized_geometry.xyz"))
    bimet_atoms = parse_xyz(os.path.join(outputs_dir, "bimetallic_optimized_geometry.xyz"))

    cutoff = 2.3
    def compute_cu_o_dists(atoms):
        cu = next((a for a in atoms if a[0] == 'Cu'), None)
        if cu is None:
            return [], 0
        o_atoms = [a for a in atoms if a[0] == 'O']
        dists = []
        for o in o_atoms:
            d = np.linalg.norm(cu[1] - o[1])
            if d <= cutoff:
                dists.append(float(d))
        return dists, len(dists)

    mono_dists, mono_cn = compute_cu_o_dists(mono_atoms)
    bimet_dists, bimet_cn = compute_cu_o_dists(bimet_atoms)

    return {
        "mono_cu_o_dists": mono_dists,
        "mono_cn": mono_cn,
        "bimet_cu_o_dists": bimet_dists,
        "bimet_cn": bimet_cn
    }


# === block: score_0 (check id='step_mono_geom') ===
def score_0(artifact, step, ctx):
    params = step.get("params", {})
    target_min = params["target_cu_o_min"]
    target_max = params["target_cu_o_max"]
    tol = params.get("tolerance", 0.05)
    expected_cn = params.get("target_cn", 3)

    dists = ctx.get("mono_cu_o_dists", [])
    cn = ctx.get("mono_cn", 0)

    if cn == 0 or len(dists) == 0:
        return 0.0

    fraction_in_range = 0.0
    for d in dists:
        if target_min - tol <= d <= target_max + tol:
            fraction_in_range += 1
    fraction_in_range /= len(dists)

    score = 0.3 * (1.0 if cn == expected_cn else 0.0) + 0.7 * fraction_in_range
    return max(0.0, min(1.0, score))


# === block: score_1 (check id='step_bimet_geom') ===
def score_1(artifact, step, ctx):
    params = step.get("params", {})
    target_min = params["target_cu_o_min"]
    target_max = params["target_cu_o_max"]
    tol = params.get("tolerance", 0.05)
    expected_cn = params.get("target_cn", 3)

    dists = ctx.get("bimet_cu_o_dists", [])
    cn = ctx.get("bimet_cn", 0)

    if cn == 0 or len(dists) == 0:
        return 0.0

    fraction_in_range = 0.0
    for d in dists:
        if target_min - tol <= d <= target_max + tol:
            fraction_in_range += 1
    fraction_in_range /= len(dists)

    score = 0.3 * (1.0 if cn == expected_cn else 0.0) + 0.7 * fraction_in_range
    return max(0.0, min(1.0, score))


# === block: score_2 (check id='step_structural_params') ===
def score_2(artifact, step, ctx):
    params = step.get("params", {})
    mono_params = params["monometallic"]
    bimet_params = params["bimetallic"]

    json_data = artifact   # already validated JSON
    mono = json_data.get("monometallic", {})
    bimet = json_data.get("bimetallic", {})

    mono_bader = mono.get("Cu Bader_charge", None)
    bimet_cu_bader = bimet.get("Cu Bader_charge", None)
    bimet_cr_bader = bimet.get("Cr Bader_charge", None)
    mono_cn_reported = mono.get("Cu coordination_number", -1)
    bimet_cn_reported = bimet.get("Cu coordination_number", -1)

    tol = mono_params["bader_tolerance"]

    mono_bader_ok = 1.0 if mono_bader is not None and abs(mono_bader - mono_params["bader_cu"]) <= tol else 0.0
    mono_cn_ok = 1.0 if mono_cn_reported == ctx["mono_cn"] else 0.0

    bimet_cu_bader_ok = 1.0 if bimet_cu_bader is not None and abs(bimet_cu_bader - bimet_params["bader_cu"]) <= tol else 0.0
    bimet_cr_bader_ok = 1.0 if bimet_cr_bader is not None and abs(bimet_cr_bader - bimet_params["bader_cr"]) <= tol else 0.0
    bimet_cn_ok = 1.0 if bimet_cn_reported == ctx["bimet_cn"] else 0.0

    mono_score = 0.8 * mono_bader_ok + 0.2 * mono_cn_ok
    bimet_score = 0.5 * bimet_cu_bader_ok + 0.3 * bimet_cr_bader_ok + 0.2 * bimet_cn_ok

    return 0.5 * mono_score + 0.5 * bimet_score


_SCORERS = {
    'step_mono_geom': score_0,
    'step_bimet_geom': score_1,
    'step_structural_params': score_2,
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
