import os
import json
import csv

# === author imports / helpers ===
import csv
import math
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
    return {}


# === block: score_0 (check id='bulk_max') ===
def score_0(artifact, step, ctx):
    def score(rows, step, ctx):
        gold_by_mat = step['gold']
        zt_tol_rel = step['tolerances']['ZT_rel']
        ef_tol_abs = step['tolerances']['EF_abs']
        # group rows by material
        mat_vals = {}
        for r in rows:
            mat = r['material']
            ef = float(r['EF_meV'])
            zt = float(r['ZT_b'])
            if mat not in mat_vals:
                mat_vals[mat] = {'ef': [], 'zt': []}
            mat_vals[mat]['ef'].append(ef)
            mat_vals[mat]['zt'].append(zt)
        matched = 0
        total = 0
        for mat, gold in gold_by_mat.items():
            total += 1
            if mat not in mat_vals:
                continue
            arr = mat_vals[mat]
            if not arr['zt']:
                continue
            zt_max = max(arr['zt'])
            idx = arr['zt'].index(zt_max)
            ef_at_max = arr['ef'][idx]
            zt_ok = abs(zt_max - gold['ZT_max']) <= zt_tol_rel * abs(gold['ZT_max'])
            ef_ok = abs(ef_at_max - gold['EF_meV']) <= ef_tol_abs
            if zt_ok and ef_ok:
                matched += 1
        return matched / total if total else 0.0


# === block: score_1 (check id='surface_max') ===
def score_1(artifact, step, ctx):
    def score(rows, step, ctx):
        gold_dict = step['gold']
        zt_tol_rel = step['tolerances']['ZT_rel']
        ef_tol_abs = step['tolerances']['EF_abs']
        # key -> list of (ef, zt)
        groups = {}
        for r in rows:
            diam = r['diameter_nm']
            mat = r['material']
            key = mat + '_' + diam
            ef = float(r['EF_meV'])
            zt = float(r['ZT_s'])
            if key not in groups:
                groups[key] = {'ef': [], 'zt': []}
            groups[key]['ef'].append(ef)
            groups[key]['zt'].append(zt)
        matched = 0
        total = 0
        for key, gold in gold_dict.items():
            total += 1
            if key not in groups:
                continue
            arr = groups[key]
            if not arr['zt']:
                continue
            zt_max = max(arr['zt'])
            idx = arr['zt'].index(zt_max)
            ef_at_max = arr['ef'][idx]
            zt_ok = abs(zt_max - gold['ZT_max']) <= zt_tol_rel * abs(gold['ZT_max'])
            ef_ok = abs(ef_at_max - gold['EF_meV']) <= ef_tol_abs
            if zt_ok and ef_ok:
                matched += 1
        return matched / total if total else 0.0


# === block: score_2 (check id='nanowire_opt') ===
def score_2(artifact, step, ctx):
    def score(rows, step, ctx):
        # Validate required diameters per material
        required_diameters = {10, 50, 100, 500, 1000, 10000}
        materials = set()
        mat_data = {}
        for r in rows:
            mat = r['material']
            d = int(r['diameter_nm'])
            zt = float(r['ZT_opt'])
            ef = float(r['EF_opt_meV'])
            materials.add(mat)
            if mat not in mat_data:
                mat_data[mat] = {}
            mat_data[mat][d] = {'ZT_opt': zt, 'EF_opt_meV': ef}
        # shape score: all materials have all diameters
        shape_ok = True
        for mat in materials:
            if set(mat_data[mat].keys()) != required_diameters:
                shape_ok = False
                break
        shape_score = 1.0 if shape_ok else 0.0

        # ZT_10nm score
        gold_10nm = step['gold_10nm']
        tol10 = step['tolerance_ZT10']
        zt10_matched = 0
        for mat in gold_10nm:
            if mat in mat_data and 10 in mat_data[mat]:
                zt = mat_data[mat][10]['ZT_opt']
                if abs(zt - gold_10nm[mat]) <= tol10:
                    zt10_matched += 1
        zt10_score = zt10_matched / len(gold_10nm) if gold_10nm else 0.0

        # bulk convergence: ZT at 10000nm
        gold_bulk = step['gold_bulk_ZT']
        tol_bulk = step['tolerance_bulk']
        bulk_matched = 0
        for mat in gold_bulk:
            if mat in mat_data and 10000 in mat_data[mat]:
                zt = mat_data[mat][10000]['ZT_opt']
                if abs(zt - gold_bulk[mat]) <= tol_bulk:
                    bulk_matched += 1
        bulk_score = bulk_matched / len(gold_bulk) if gold_bulk else 0.0

        # structural trend
        structural = step['structural_expected']
        struct_matched = 0
        for mat, relation in structural.items():
            if mat in mat_data and 10 in mat_data[mat] and 10000 in mat_data[mat]:
                zt10 = mat_data[mat][10]['ZT_opt']
                zt1e4 = mat_data[mat][10000]['ZT_opt']
                if relation == 'lt' and zt10 < zt1e4:
                    struct_matched += 1
                elif relation == 'gt' and zt10 > zt1e4:
                    struct_matched += 1
        struct_score = struct_matched / len(structural) if structural else 0.0

        # Combine weights
        w_shape = 0.1
        w_zt10 = 0.3
        w_bulk = 0.3
        w_struct = 0.3
        total = w_shape * shape_score + w_zt10 * zt10_score + w_bulk * bulk_score + w_struct * struct_score
        return total


_SCORERS = {
    'bulk_max': score_0,
    'surface_max': score_1,
    'nanowire_opt': score_2,
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
