import os
import json
import csv

# === author imports / helpers ===
import csv
import numpy as np
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
    return {}


# === block: score_0 (check id='step_band_energies') ===
def score_0(artifact, step, ctx):
    # Parse artifact (list of dicts expected)
    rows = artifact
    by_geom = defaultdict(lambda: defaultdict(list))
    for r in rows:
        try:
            k = float(r['k'])
            b = int(r['band'])
            E = float(r['E'])
            g = r['geometry']
        except (KeyError, ValueError):
            return 0.0
        by_geom[g][k].append((b, E))

    # Sub-score weights
    w_k = 0.1
    w_degen = 0.3
    w_spl125 = 0.3
    w_spl50 = 0.3

    score_k = 0.0
    score_degen = 0.0
    score_spl125 = 0.0
    score_spl50 = 0.0

    required_geoms = ['linear', 'helix125', 'helix50']
    for geom in required_geoms:
        if geom not in by_geom:
            return 0.0
        unique_k = np.array(sorted(by_geom[geom].keys()))
        nk = len(unique_k)
        if nk >= 200:
            score_k += w_k / 3.0  # equally shared among three geometries

    # Linear degeneracy check: the two p-derived bands (middle two when sorted)
    # must be degenerate within 1e-4 eV at every k point.
    def has_exactly_one_degenerate_pair(entries):
        """Return True if exactly one pair of the four bands is within 1e-4 eV."""
        energies = sorted([e for _, e in entries])
        if len(energies) < 4:
            return False
        tol = 1e-4
        num_pairs = 0
        for i in range(4):
            for j in range(i + 1, 4):
                if abs(energies[i] - energies[j]) <= tol:
                    num_pairs += 1
        return num_pairs == 1

    if 'linear' in by_geom:
        total_k = len(by_geom['linear'])
        if total_k == 0:
            score_degen = 0.0
        else:
            passed = 0
            for entries in by_geom['linear'].values():
                if has_exactly_one_degenerate_pair(entries):
                    passed += 1
            score_degen = w_degen * (passed / total_k)

    # Helper to extract the p-band splitting from the two middle energies at k=0
    def middle_gap_at_k0(geom):
        ks = np.array(sorted(by_geom[geom].keys()))
        if len(ks) == 0:
            return None
        # nearest k to 0
        idx = np.argmin(np.abs(ks))
        entries = by_geom[geom][ks[idx]]
        energies = sorted([e for _, e in entries])
        if len(energies) < 4:
            return None
        return energies[2] - energies[1]

    spl125 = middle_gap_at_k0('helix125') if 'helix125' in by_geom else None
    spl50 = middle_gap_at_k0('helix50') if 'helix50' in by_geom else None

    if spl125 is not None and 0.04 <= spl125 <= 0.06:
        score_spl125 = w_spl125

    if spl50 is not None and spl125 is not None:
        if spl50 > spl125:
            score_spl50 = w_spl50
        else:
            # smaller than helix125 but still some splitting -> partial credit
            if spl50 >= 0.01:
                score_spl50 = w_spl50 * 0.5

    total = score_k + score_degen + score_spl125 + score_spl50
    # Ensure within [0,1]
    return min(max(total, 0.0), 1.0)


_SCORERS = {
    'step_band_energies': score_0,
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
