import os
import json
import csv

# === author imports / helpers ===
from collections import defaultdict
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
    return spec


# === block: score_0 (check id='water_flux') ===
def score_0(artifact, step, ctx):
    data = [row for row in artifact if all(k in row for k in ['membrane_name', 'applied_pressure_MPa', 'water_flux_ns-1'])]
    if not data:
        return 0.0
    canonical = {'n-graphene': 'N-graphene', 'nh-graphene': 'NH-graphene', 'nh3-graphene': 'NH3-graphene', 'noh-graphene': 'NOH-graphene', 'h-graphene': 'H-graphene'}
    ref = ctx.get('reference_data', {}).get('water_flux', {})
    target_flux = ref.get('N_graphene_130_flux', 66.0)
    min_ratio = ref.get('min_acceptable_flux_ratio', 0.8)
    acceptable_min = target_flux * min_ratio

    mem_data = {}
    for row in data:
        mem_raw = row['membrane_name'].strip().lower()
        mem = canonical.get(mem_raw, mem_raw)
        pressure = float(row['applied_pressure_MPa'])
        flux = float(row['water_flux_ns-1'])
        mem_data.setdefault(mem, []).append((pressure, flux))

    # 1) N-graphene at 130 MPa
    n_graphene_rows = [f for p,f in mem_data.get('N-graphene', []) if abs(p - 130) < 0.1]
    flux_130 = n_graphene_rows[0] if n_graphene_rows else 0.0
    score_flux = min(1.0, flux_130 / acceptable_min) if flux_130 > 0 else 0.0

    # 2) ordering: N-graphene flux highest at each pressure
    ng_pressures = [p for p,f in mem_data.get('N-graphene', [])]
    common_pressures = ng_pressures
    if not common_pressures:
        score_ordering = 0.0
    else:
        cnt_highest = 0
        for p in common_pressures:
            fluxes = {}
            for mem, vals in mem_data.items():
                for pp, ff in vals:
                    if abs(pp - p) < 0.1:
                        fluxes[mem] = max(fluxes.get(mem, 0), ff)
            if fluxes:
                max_flux = max(fluxes.values())
                n_flux = fluxes.get('N-graphene', 0)
                if n_flux == max_flux:
                    cnt_highest += 1
        score_ordering = cnt_highest / len(common_pressures) if common_pressures else 0.0

    # 3) linear trend
    from math import isclose
    trend_scores = []
    for mem, vals in mem_data.items():
        sorted_vals = sorted(vals, key=lambda x: x[0])
        inc = 0
        for i in range(1, len(sorted_vals)):
            if sorted_vals[i][1] >= sorted_vals[i-1][1]:
                inc += 1
        trend_scores.append(inc / max(len(sorted_vals)-1, 1))
    trend_score = sum(trend_scores)/len(trend_scores) if trend_scores else 0.0

    total_score = 0.6 * score_flux + 0.2 * score_ordering + 0.2 * trend_score
    return max(0.0, min(1.0, total_score))


# === block: score_1 (check id='salt_rejection') ===
def score_1(artifact, step, ctx):
    data = [row for row in artifact if all(k in row for k in ['membrane_name', 'applied_pressure_MPa', 'salt_rejection'])]
    if not data:
        return 0.0
    canonical = {'n-graphene': 'N-graphene', 'nh-graphene': 'NH-graphene', 'nh3-graphene': 'NH3-graphene', 'noh-graphene': 'NOH-graphene', 'h-graphene': 'H-graphene'}
    noh_rows = []
    other_rows = []
    for row in data:
        mem_raw = row['membrane_name'].strip().lower()
        mem = canonical.get(mem_raw, mem_raw)
        rejection = float(row['salt_rejection'])
        if mem == 'NOH-graphene':
            noh_rows.append(rejection)
        else:
            other_rows.append(rejection)

    noh_score = 1.0
    if noh_rows:
        if min(noh_rows) < 0.99:
            noh_score = 0.5
    else:
        noh_score = 0.0

    other_score = 1.0
    if other_rows:
        avg_rej = sum(other_rows)/len(other_rows)
        if avg_rej < 0.7:
            other_score = 0.5
        elif avg_rej < 0.5:
            other_score = 0.0

    total_score = 0.8 * noh_score + 0.2 * other_score
    return max(0.0, min(1.0, total_score))


# === block: score_2 (check id='pmf_profiles') ===
def score_2(artifact, step, ctx):
    data = artifact
    required = ['membrane_name', 'species', 'z_angstrom', 'pmf_kcal_per_mol']
    if not data or not all(k in data[0] for k in required):
        return 0.0
    canonical = {'n-graphene': 'N-graphene', 'nh-graphene': 'NH-graphene', 'nh3-graphene': 'NH3-graphene', 'noh-graphene': 'NOH-graphene', 'h-graphene': 'H-graphene'}
    ref = ctx.get('reference_data', {}).get('pmf', {})
    water_order = ref.get('water_barrier_order', [])
    na_lowest = ref.get('na_barrier_lowest', 'N-graphene')
    cl_min = ref.get('cl_barrier_min', 15.0)
    water_range = ref.get('water_barrier_range', [2.0, 3.5])
    na_min = ref.get('na_barrier_min', 3.0)

    profiles = defaultdict(lambda: defaultdict(list))
    for row in data:
        mem_raw = row['membrane_name'].strip().lower()
        mem = canonical.get(mem_raw, mem_raw)
        species = row['species'].strip().lower()
        z = float(row['z_angstrom'])
        pmf = float(row['pmf_kcal_per_mol'])
        profiles[mem][species].append((z, pmf))

    def barrier(profile_list):
        if not profile_list:
            return None
        pmf_vals = [v for z,v in profile_list]
        return max(pmf_vals) - min(pmf_vals)

    # water
    water_barriers = {}
    for mem in water_order:
        water_profile = profiles.get(mem, {}).get('water', [])
        water_barriers[mem] = barrier(water_profile)
    water_score = 0.0
    if water_barriers:
        range_pass = [1.0 if (b is not None and water_range[0] <= b <= water_range[1]) else 0.0 for b in water_barriers.values()]
        range_score = sum(range_pass)/len(range_pass)
        correct_pairs = 0
        for i in range(len(water_order)-1):
            b_prev = water_barriers.get(water_order[i])
            b_next = water_barriers.get(water_order[i+1])
            if b_prev is not None and b_next is not None and b_prev <= b_next:
                correct_pairs += 1
        order_score = correct_pairs / max(len(water_order)-1, 1)
        water_score = 0.5*range_score + 0.5*order_score

    # Na+
    na_barriers = {}
    for mem in profiles:
        na_profile = profiles[mem].get('na+', [])
        na_barriers[mem] = barrier(na_profile)
    na_score = 0.0
    if na_barriers:
        na_min_ok = [1.0 if b is not None and b >= na_min else 0.0 for b in na_barriers.values()]
        na_min_score = sum(na_min_ok)/len(na_min_ok)
        n_na = na_barriers.get('N-graphene')
        if n_na is not None:
            others = [b for mem,b in na_barriers.items() if mem != 'N-graphene' and b is not None]
            lowest = all(n_na <= b for b in others) if others else True
        else:
            lowest = False
        na_score = 0.6*na_min_score + 0.4*(1.0 if lowest else 0.0)

    # Cl-
    cl_barriers = {}
    for mem in profiles:
        cl_profile = profiles[mem].get('cl-', [])
        cl_barriers[mem] = barrier(cl_profile)
    cl_score = 0.0
    if cl_barriers:
        cl_ok = [1.0 if b is not None and b >= cl_min else 0.0 for b in cl_barriers.values()]
        cl_score = sum(cl_ok)/len(cl_ok)

    total_score = 0.4*water_score + 0.3*na_score + 0.3*cl_score
    return max(0.0, min(1.0, total_score))


_SCORERS = {
    'water_flux': score_0,
    'salt_rejection': score_1,
    'pmf_profiles': score_2,
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
