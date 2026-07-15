import os
import json
import csv

# === author imports / helpers ===
import csv, os, json
from collections import defaultdict


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
        lattice_gold = {}
        for step in spec["steps"]:
            if step["id"] == "lattice_check":
                lattice_gold = step.get("gold", {})
                break
        return {"lattice_gold": lattice_gold}


# === block: score_0 (check id='lattice_check') ===
def score_0(artifact, step, ctx):
        if not isinstance(artifact, list) or not artifact:
            return 0.0
        gold = ctx["lattice_gold"]
        tolerance = step.get("tolerance", 0.05)
        required_materials = ["KNbO3","KTaO3","SrTiO3","BaTiO3","PbTiO3"]
        if not all(col in artifact[0] for col in ["material","WDA_original_lattice_constant","WDA_new_lattice_constant"]):
            return 0.0
        total = 0
        matched = 0
        for row in artifact:
            mat = row["material"]
            if mat not in gold:
                continue
            try:
                wda_orig = float(row["WDA_original_lattice_constant"])
                wda_new = float(row["WDA_new_lattice_constant"])
            except (ValueError, KeyError):
                continue
            total += 1
            if abs(wda_orig - gold[mat]["WDA_original"]) <= tolerance:
                matched += 1
            total += 1
            if abs(wda_new - gold[mat]["WDA_new"]) <= tolerance:
                matched += 1
        if total == 0:
            return 0.0
        return matched / total


# === block: score_1 (check id='frozen_phonon_check') ===
def score_1(artifact, step, ctx):
        if not isinstance(artifact, list) or not artifact:
            return 0.0
        checks = step.get("checks", {})
        min_range = checks.get("min_displacement_cover", [0.0, 1.2])
        min_points = checks.get("min_points", 7)
        well_relation = checks.get("well_depth_relation", {})
        required_cols = ["material","method","displacement","total_energy"]
        if not all(col in artifact[0] for col in required_cols):
            return 0.0

        # Group data
        groups = defaultdict(list)
        for row in artifact:
            if row["method"] not in ("WDA_original", "WDA_new"):
                continue
            key = (row["material"], row["method"])
            try:
                d = float(row["displacement"])
                e = float(row["total_energy"])
            except (ValueError, KeyError):
                continue
            groups[key].append((d, e))

        conditions = []
        well_depths = {}
        for (mat, meth), pairs in groups.items():
            if len(pairs) < min_points:
                conditions.append(False)
                continue
            pairs.sort(key=lambda x: x[0])
            displacements = [p[0] for p in pairs]
            energies = [p[1] for p in pairs]
            # range check
            if displacements[0] > 1e-6 or displacements[-1] < min_range[1] - 1e-6:
                conditions.append(False)
            else:
                conditions.append(True)
            # well depth check: energy at 0 is max, min at nonzero
            e0_idx = min(range(len(displacements)), key=lambda i: abs(displacements[i]))
            e0 = energies[e0_idx]
            min_e = min(energies)
            # Check if e0 is >= all other energies (allow small numeric noise)
            is_double_well = all(e0 >= e - 1e-6 for e in energies)
            conditions.append(is_double_well)
            well_depth = e0 - min_e
            conditions.append(well_depth > 1e-6)
            well_depths[(mat, meth)] = well_depth

        # Cross-method relations
        for mat in ("BaTiO3","PbTiO3"):
            orig = well_depths.get((mat, "WDA_original"), None)
            neww = well_depths.get((mat, "WDA_new"), None)
            if orig is None or neww is None:
                conditions.append(False)
            else:
                conditions.append(orig > neww + 1e-6)
        mat = "KNbO3"
        orig = well_depths.get((mat, "WDA_original"), None)
        neww = well_depths.get((mat, "WDA_new"), None)
        if orig is None or neww is None:
            conditions.append(False)
        else:
            # well depths should be similar (within factor 2)
            if orig < 1e-6 and neww < 1e-6:
                conditions.append(True)
            else:
                ratio = min(orig, neww) / max(orig, neww) if max(orig, neww) > 1e-6 else 0.0
                conditions.append(ratio > 0.5)

        if not conditions:
            return 0.0
        return sum(conditions) / len(conditions)


_SCORERS = {
    'lattice_check': score_0,
    'frozen_phonon_check': score_1,
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
