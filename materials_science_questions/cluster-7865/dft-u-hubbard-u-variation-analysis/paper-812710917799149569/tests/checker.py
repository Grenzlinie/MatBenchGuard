import os
import json
import csv

# === author imports / helpers ===
import os
import csv
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
    csv_path = os.path.join(outputs_dir, 'step_02_band_structure.csv')
    raw = load_artifact(csv_path)
    if not raw or not isinstance(raw, list) or len(raw) == 0:
        return {'csv_data': None}
    return {'csv_data': raw}


# === block: score_0 (check id='step_01_weyl_nodes') ===
def score_0(artifact, step, ctx):
    # Recompute Weyl nodes from the band structure CSV.
    # ctx['csv_data'] is list of dicts with keys 'kz','band_index','energy'.
    # target from step: k0, k_tol_abs, energy_tol_abs, max_energy_range, min_nodes, max_nodes.
    csv_rows = ctx.get('csv_data')
    if csv_rows is None:
        return 0.0

    # Build mapping: band_index -> list of (kz, energy) sorted by kz
    bands = {}
    for row in csv_rows:
        try:
            kz = float(row['kz'])
            bi = int(row['band_index'])
            energy = float(row['energy'])
        except (ValueError, KeyError):
            continue
        bands.setdefault(bi, []).append((kz, energy))

    if len(bands) < 2:
        return 0.0

    # Sort each band list by kz
    for bi in bands:
        bands[bi].sort(key=lambda x: x[0])

    # Parameters
    k0 = step['target']['k0']
    k_tol = step['target']['k_tol_abs']
    energy_tol = step['target']['energy_tol_abs']
    max_e_range = step['target']['max_energy_range']
    min_nodes = step['target']['min_nodes']
    max_nodes = step['target']['max_nodes']

    # Find all band pairs and detect sign changes in energy difference
    band_indices = sorted(bands.keys())
    crossings = []
    for i in range(len(band_indices)):
        for j in range(i+1, len(band_indices)):
            bi = band_indices[i]
            bj = band_indices[j]
            points1 = bands[bi]
            points2 = bands[bj]
            # merge on identical kz? Assume same kz grid for all bands. We'll pair nearest kz.
            # Simple: use a kz dict from one band
            kz_map1 = {kz: e for kz, e in points1}
            kz_map2 = {kz: e for kz, e in points2}
            common_kz = sorted(set(kz_map1.keys()).intersection(kz_map2.keys()))
            if len(common_kz) < 2:
                continue
            for idx in range(len(common_kz)-1):
                kz_a = common_kz[idx]
                kz_b = common_kz[idx+1]
                e1a = kz_map1[kz_a]
                e2a = kz_map2[kz_a]
                e1b = kz_map1[kz_b]
                e2b = kz_map2[kz_b]
                diff_a = e1a - e2a
                diff_b = e1b - e2b
                # Only consider crossing where both energies are within max_e_range of Fermi
                if (abs(e1a) > max_e_range or abs(e2a) > max_e_range or
                    abs(e1b) > max_e_range or abs(e2b) > max_e_range):
                    continue
                # sign change
                if diff_a * diff_b < 0:
                    # linear interpolation to crossing point
                    t = -diff_a / (diff_b - diff_a)
                    kz_cross = kz_a + t * (kz_b - kz_a)
                    e_cross = e1a + t * (e1b - e1a)  # energy at crossing (should equal e2a + t*(e2b - e2a))
                    crossings.append((kz_cross, e_cross))

    # Remove duplicates (symmetric nodes may appear twice with swapped band indices)
    unique_crossings = []
    tol = 1e-6
    for c in crossings:
        kc, ec = c
        # Only keep if energy near Fermi (within energy_tol)
        if abs(ec) > energy_tol:
            continue
        # check if kz is already present within tol
        found = False
        for uc in unique_crossings:
            if abs(kc - uc[0]) < 1e-4 and abs(ec - uc[1]) < 1e-4:
                found = True
                break
        if not found:
            unique_crossings.append((kc, ec))

    num_found = len(unique_crossings)

    # Score node count
    if num_found == 2:
        count_score = 1.0
    elif num_found == 1:
        count_score = 0.5
    else:
        count_score = 0.0

    # Score positions: each node should be at |kz| ~ k0, energy ~ 0
    pos_scores = []
    for kc, ec in unique_crossings:
        pos_err = abs(abs(kc) - k0)
        pos_score = max(0.0, 1.0 - pos_err / k_tol)
        # energy already filtered, but penalize if outside? not needed.
        pos_scores.append(pos_score)

    if num_found == 2:
        # Average position score of both nodes
        avg_pos_score = sum(pos_scores) / 2.0
    else:
        avg_pos_score = max(pos_scores) if pos_scores else 0.0

    # Optional chirality check: use the provided artifact (the agent's weyl_nodes.json)
    if isinstance(artifact, list) and len(artifact) == 2:
        try:
            c1 = int(artifact[0].get('chirality', 0))
            c2 = int(artifact[1].get('chirality', 0))
            if c1 == 1 and c2 == -1 or c1 == -1 and c2 == 1:
                chirality_ok = True
            else:
                chirality_ok = False
        except:
            chirality_ok = False
    else:
        chirality_ok = False

    # Combine: main weight on recomputed positions, chirality is small bonus but not required
    final_score = 0.9 * (count_score * 0.5 + avg_pos_score * 0.5) + 0.1 * (1.0 if chirality_ok else 0.5)
    # Ensure proper bounding
    final_score = max(0.0, min(1.0, final_score))
    return float(final_score)


# === block: score_1 (check id='step_02_band_structure') ===
def score_1(artifact, step, ctx):
    # Structural audit of band structure CSV.
    csv_rows = ctx.get('csv_data')
    if csv_rows is None:
        return 0.0

    schema = step.get('schema', {})
    required_cols = schema.get('required_columns', [])
    min_rows = schema.get('min_rows', 0)
    kz_range = schema.get('kz_range', None)
    monotonic = schema.get('monotonic', False)

    # Check columns
    if not all(col in csv_rows[0] for col in required_cols):
        return 0.0

    # Check row count
    if len(csv_rows) < min_rows:
        return 0.0

    # Extract kz values from rows that have kz and band_index=0 to get monotonic grid
    kz_vals = []
    for row in csv_rows:
        try:
            kz = float(row['kz'])
            bi = int(row['band_index'])
            if bi == 0:
                kz_vals.append(kz)
        except:
            pass
    if not kz_vals:
        return 0.0

    # Check range
    if kz_range:
        min_kz = min(kz_vals)
        max_kz = max(kz_vals)
        if min_kz > kz_range[0] + 1e-6 or max_kz < kz_range[1] - 1e-6:
            return 0.0

    # Check monotonic (strictly increasing)
    if monotonic:
        for i in range(len(kz_vals)-1):
            if kz_vals[i+1] <= kz_vals[i]:
                return 0.5  # partial for non-strictly monotonic but maybe still okay? The spec says monotonic, so 0 if fails.
        # all good

    return 1.0


_SCORERS = {
    'step_01_weyl_nodes': score_0,
    'step_02_band_structure': score_1,
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
