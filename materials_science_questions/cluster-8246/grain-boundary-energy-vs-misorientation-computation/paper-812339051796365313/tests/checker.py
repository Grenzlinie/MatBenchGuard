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
    return {}


# === block: score_0 (check id='bulk_consistency') ===
def score_0(artifact, step, ctx):
    def to_num(v):
        try:
            return float(v)
        except (TypeError, ValueError):
            return 0.0

    tol = step.get("tolerance", 0.005)
    metrics = step.get("metrics", [])
    if not metrics or not artifact:
        return 0.0

    ensembles = {}
    for row in artifact:
        if not isinstance(row, dict):
            continue
        ens = (row.get("ensemble", "") or "").strip()
        pbc = (row.get("pbc_type", "") or "").strip().lower()
        if not ens or pbc not in ("mobius", "bvk"):
            continue
        ensembles.setdefault(ens, {})[pbc] = row

    all_ok = True
    for ens, vals in ensembles.items():
        if "mobius" not in vals or "bvk" not in vals:
            all_ok = False
            break
        mobius = vals["mobius"]
        bvk = vals["bvk"]
        for m in metrics:
            mv = to_num(mobius.get(m, 0))
            bv = to_num(bvk.get(m, 0))
            denom = max(abs(bv), 1e-9)
            rel_diff = abs(mv - bv) / denom
            if rel_diff > tol:
                all_ok = False
                break
        if not all_ok:
            break
    return 1.0 if all_ok else 0.0


# === block: score_1 (check id='rmsad_slices_consistency') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        tol = step.get("tolerance", 0.01)
        rows = artifact
        if not rows:
            return 0.0
        total = 0
        ok = 0
        for row in rows:
            try:
                mobius = float(row.get("mobius_rmsad_Angstrom", 0) or 0)
                bvk = float(row.get("bvk_rmsad_Angstrom", 0) or 0)
                denom = max(abs(bvk), 1e-9)
                rel_diff = abs(mobius - bvk) / denom
                if rel_diff <= tol:
                    ok += 1
                total += 1
            except Exception:
                continue
        if total == 0:
            return 0.0
        return ok / total


# === block: score_2 (check id='gb_minimized_energy_equivalence') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        tol_ev = step.get("tolerance_ev", 0.001)
        rows = artifact
        structures = {}
        for row in rows:
            struct = (row.get("structure", "") or "").strip()
            pbc = (row.get("pbc_type", "") or "").strip().lower()
            if not struct or pbc not in ("mobius", "bvk"):
                continue
            val = float(row.get("minimized_energy_eVperatom", 0) or 0)
            structures.setdefault(struct, {})[pbc] = val
        ok_count = 0
        total_structures = 0
        for struct, vals in structures.items():
            if "mobius" in vals and "bvk" in vals:
                total_structures += 1
                if abs(vals["mobius"] - vals["bvk"]) <= tol_ev:
                    ok_count += 1
        if total_structures == 0:
            return 0.0
        return ok_count / total_structures


# === block: score_3 (check id='gb_interfacial_energy_gold') ===
def score_3(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold = step.get("gold_values", {})
        tol_frac = step.get("tolerance_frac", 0.05)
        rows = artifact
        mobius_vals = {}
        for row in rows:
            pbc = (row.get("pbc_type", "") or "").strip().lower()
            if pbc != "mobius":
                continue
            struct = (row.get("structure", "") or "").strip()
            if struct not in gold:
                continue
            energy = float(row.get("interfacial_energy_mJperm2", 0) or 0)
            mobius_vals[struct] = energy
        if set(gold.keys()) != set(mobius_vals.keys()):
            return 0.0
        for struct, gold_val in gold.items():
            if struct not in mobius_vals:
                return 0.0
            rel_err = abs(mobius_vals[struct] - gold_val) / gold_val
            if rel_err > tol_frac:
                return 0.0
        if mobius_vals.get("Σ11A", 1e9) < mobius_vals.get("Σ11B", -1e9):
            return 1.0
        return 0.0


_SCORERS = {
    'bulk_consistency': score_0,
    'rmsad_slices_consistency': score_1,
    'gb_minimized_energy_equivalence': score_2,
    'gb_interfacial_energy_gold': score_3,
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
