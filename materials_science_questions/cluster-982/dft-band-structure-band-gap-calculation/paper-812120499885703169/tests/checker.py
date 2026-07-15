import os
import json
import csv

# === author imports / helpers ===
import csv, re, math
from collections import namedtuple


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


# === block: score_0 (check id='scored_band_gap') ===
def score_0(artifact, step, ctx):
    import os

    # Verify that the agent produced the raw band structure data from the required
    # process step (DFT band structure calculation). Without this file,
    # the computation was not performed.
    bands_file = os.path.join("/app/outputs", "bands.dat.gnu")
    if not os.path.exists(bands_file):
        bands_file = os.path.join("/app/outputs", "bands.out")
    if not os.path.exists(bands_file):
        return 0.0

    try:
        with open(bands_file, "r") as f:
            lines = [l.strip() for l in f if l.strip() and not l.startswith("#")]
        if not lines:
            return 0.0
        # Attempt to parse standard Quantum ESPRESSO bands.dat.gnu: first line may
        # contain nkpts and nbands.
        parts = lines[0].split()
        if len(parts) == 2:
            nkpts, nbands = int(parts[0]), int(parts[1])
            start_idx = 1
        else:
            nkpts = len(lines)
            nbands = None
            start_idx = 0

        all_energies = []
        for i in range(start_idx, len(lines)):
            vals = list(map(float, lines[i].split()))
            if len(vals) < 2:
                continue
            # The first column is typically the k-distance, the rest are band energies
            band_energies = vals[1:]
            if nbands is None:
                nbands = len(band_energies)
            all_energies.append(sorted(band_energies))

        if len(all_energies) != nkpts:
            nkpts = len(all_energies)

        # Find valence band maximum and conduction band minimum across all k-points.
        vbm_energy = -1e9
        cbm_energy = 1e9
        vbm_kpt = None
        cbm_kpt = None
        for ik, energies in enumerate(all_energies):
            # Explore gaps between consecutive bands at this k-point
            for j in range(len(energies) - 1):
                e_low  = energies[j]
                e_high = energies[j + 1]
                gap = e_high - e_low
                # A gap > 0.1 eV is indicative of the band gap
                if gap > 0.1:
                    if e_low > vbm_energy:
                        vbm_energy = e_low
                        vbm_kpt = ik
                    if e_high < cbm_energy:
                        cbm_energy = e_high
                        cbm_kpt = ik

        if cbm_energy < vbm_energy or (cbm_energy - vbm_energy) < 0.05:
            return 0.0

        band_gap = cbm_energy - vbm_energy
        direct = (vbm_kpt == cbm_kpt)
        gap_type_is_indirect = not direct   # the paper reports an indirect gap

    except Exception:
        return 0.0

    # Compare recomputed quantities to hidden reference
    ref_gap  = step['target']
    tol      = step['tolerance_abs']

    gap_ok = abs(band_gap - ref_gap) <= tol
    type_ok = gap_type_is_indirect

    score = 0.0
    if gap_ok:
        score += 0.5
    if type_ok:
        score += 0.5
    return score


# === block: score_1 (check id='scored_epsilon_peak') ===
def score_1(artifact, step, ctx):
    # Read CSV, find global maximum of Epsilon_im in energy range 6-8 eV
    if not artifact or not isinstance(artifact, list):
        return 0.0
    candidates = []
    try:
        for row in artifact:
            e = float(row['Energy_eV'])
            eps = float(row['Epsilon_im'])
            if 6.0 <= e <= 8.0:
                candidates.append((e, eps))
        if not candidates:
            return 0.0
        max_row = max(candidates, key=lambda x: x[1])
        peak_energy = max_row[0]
        target = step['target']
        tol = step['tolerance_abs']
        if abs(peak_energy - target) <= tol:
            return 1.0
        else:
            return 0.0
    except (KeyError, ValueError):
        return 0.0


_SCORERS = {
    'scored_band_gap': score_0,
    'scored_epsilon_peak': score_1,
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
