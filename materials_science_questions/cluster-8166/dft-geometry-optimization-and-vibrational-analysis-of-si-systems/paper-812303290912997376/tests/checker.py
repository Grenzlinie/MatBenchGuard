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


# === block: score_0 (check id='step_03_results') ===
def score_0(artifact, step, ctx):
    clusters = artifact.get("clusters", [])
    if not isinstance(clusters, list) or len(clusters) != 4:
        return 0.0
    cluster_map = {c["name"]: c for c in clusters if isinstance(c, dict) and "name" in c}
    required_names = {"Si-C-N", "Si-N-C", "Si-C=N", "Si-N=C"}
    if not required_names.issubset(cluster_map.keys()):
        return 0.0

    def get_energy(name):
        return cluster_map[name].get("total_energy_eV", None)

    def get_bl(name, bond):
        bl = cluster_map[name].get("bond_lengths", {})
        return bl.get(bond, None)

    e_sicn = get_energy("Si-C-N")
    e_sinc = get_energy("Si-N-C")
    e_sicn_d = get_energy("Si-C=N")
    e_sinc_d = get_energy("Si-N=C")

    threshold = float(step.get("config", {}).get("energy_diff_threshold", 0.3))

    diff_single = e_sicn - e_sinc  # Si-C-N minus Si-N-C; should be positive if Si-N-C more stable
    diff_double = e_sicn_d - e_sinc_d

    score = 0.0
    if all(v is not None and isinstance(v, (int, float)) for v in [e_sicn, e_sinc, e_sicn_d, e_sinc_d]):
        # negative energy check
        if all(v < 0 for v in [e_sicn, e_sinc, e_sicn_d, e_sinc_d]):
            score += 0.1
        # single-bond energy ordering
        if diff_single >= threshold:
            score += 0.4
        elif diff_single > 0:
            score += 0.1
        # double-bond energy ordering
        if diff_double >= threshold:
            score += 0.3
        elif diff_double > 0:
            score += 0.1

    # bond length ordering: Si-N shorter than Si-C in single-bond pair
    bl_sic = get_bl("Si-C-N", "Si-C")
    bl_sin = get_bl("Si-N-C", "Si-N")
    if bl_sic is not None and bl_sin is not None and isinstance(bl_sic, (int, float)) and isinstance(bl_sin, (int, float)):
        if bl_sin < bl_sic:
            score += 0.1

    # bond length ordering: Si-N shorter than Si-C in double-bond pair
    bl_sic_d = get_bl("Si-C=N", "Si-C")
    bl_sin_d = get_bl("Si-N=C", "Si-N")
    if bl_sic_d is not None and bl_sin_d is not None and isinstance(bl_sic_d, (int, float)) and isinstance(bl_sin_d, (int, float)):
        if bl_sin_d < bl_sic_d:
            score += 0.1

    return min(1.0, score)


_SCORERS = {
    'step_03_results': score_0,
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
