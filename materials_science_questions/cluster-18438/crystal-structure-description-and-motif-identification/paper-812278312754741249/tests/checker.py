import os
import json
import csv

# === author imports / helpers ===
import numpy as np


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


# === block: score_0 (check id='step_compute_geometry') ===
def score_0(artifact, step, ctx):
        # Recompute reference values
        a = 6.105
        b = 8.658
        c = 11.072
        alpha = np.deg2rad(71.35)
        beta  = np.deg2rad(77.58)
        gamma = np.deg2rad(71.09)

        cos_a = np.cos(alpha); cos_b = np.cos(beta); cos_g = np.cos(gamma)
        sin_g = np.sin(gamma)
        v_star = np.sqrt(1 - cos_a**2 - cos_b**2 - cos_g**2 + 2*cos_a*cos_b*cos_g)

        cell = np.array([
            [a, 0, 0],
            [b*cos_g, b*sin_g, 0],
            [c*cos_b, c*(cos_a - cos_b*cos_g)/sin_g, c*v_star/sin_g]
        ])

        frac_to_cart = lambda frac: frac @ cell

        Br1 = np.array([0.5, 0.5, 0.0])
        Br2 = np.array([0.4894, 0.7294, 0.0982])
        O4  = np.array([0.0, 0.0, 0.5])

        O1 = np.array([0.804, 0.7706, 0.4596])
        O2 = np.array([0.854, 1.0563, 0.2714])
        O3 = np.array([1.119, 1.2499, 0.2988])

        O1_sym = np.array([-0.804, -0.7706, 1 - 0.4596])
        O2_sym = np.array([-0.854, -1.0563, 1 - 0.2714])
        O3_sym = np.array([-1.119, -1.2499, 1 - 0.2988])

        Br1_cart = frac_to_cart(Br1)
        Br2_cart = frac_to_cart(Br2)
        br_br_ref = np.linalg.norm(Br2_cart - Br1_cart)

        crown_O_cart = frac_to_cart(np.array([O1, O2, O3, O1_sym, O2_sym, O3_sym]))
        centroid = crown_O_cart.mean(axis=0)
        _, _, vh = np.linalg.svd(crown_O_cart - centroid, full_matrices=False)
        normal = vh[-1]
        O4_cart = frac_to_cart(O4)
        displacement_ref = abs(np.dot(O4_cart - centroid, normal))

        dists = np.linalg.norm(crown_O_cart - O4_cart, axis=1)
        min_dist_ref = dists.min()
        max_dist_ref = dists.max()

        ref_values = {
            "br_br_bond_length_angstrom": round(float(br_br_ref), 6),
            "oxonium_out_of_plane_displacement_angstrom": round(float(displacement_ref), 6),
            "o_ox_crown_min_dist_angstrom": round(float(min_dist_ref), 6),
            "o_ox_crown_max_dist_angstrom": round(float(max_dist_ref), 6)
        }

        if not isinstance(artifact, dict):
            return 0.0

        tol = step.get('tolerance', 1e-5)
        score = 0.0
        for key, ref_val in ref_values.items():
            agent_val = artifact.get(key)
            if agent_val is None:
                continue
            try:
                if abs(float(agent_val) - ref_val) <= tol:
                    score += 0.25
            except:
                pass
        return score


_SCORERS = {
    'step_compute_geometry': score_0,
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
