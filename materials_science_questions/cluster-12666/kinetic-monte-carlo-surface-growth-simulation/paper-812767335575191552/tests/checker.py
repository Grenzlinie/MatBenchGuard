import os
import json
import csv

# === author imports / helpers ===
import json, math


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
    N_ML = 160 * 160   # atoms per monolayer for the paper's 160x160 surface
    ctx = {'N_ML': N_ML}
    return ctx


# === block: score_0 (check id='monomer_rel_decrease_100K') ===
def score_0(artifact, step, ctx):
    data = artifact.get('temperatures', [])

    def find_entry(dep_type):
        for entry in data:
            if entry.get('temperature') == 100 and entry.get('deposition_type') == dep_type:
                return entry
        return None

    conv = find_entry('conventional')
    energ = find_entry('energetic')
    if conv is None or energ is None:
        return 0.0

    def get_monomer_coverage(entry):
        """Return monomer coverage (ML) from island size distribution."""
        dist = entry.get('island_size_distribution', [])
        for item in dist:
            size = item.get('size')
            cov = item.get('coverage')
            if size == 1 and cov is not None:
                return cov
        return None

    conv_cov = get_monomer_coverage(conv)
    energ_cov = get_monomer_coverage(energ)
    if conv_cov is None or energ_cov is None or conv_cov == 0:
        return 0.0

    # total deposited coverage is 0.2 ML for both conditions
    TOTAL_COVERAGE = 0.2
    conv_frac = conv_cov / TOTAL_COVERAGE
    energ_frac = energ_cov / TOTAL_COVERAGE
    rel_decrease = (conv_frac - energ_frac) / conv_frac
    threshold = 0.035   # paper reports 3.5% monomer decrease at 100 K
    if rel_decrease >= threshold:
        return 1.0
    elif rel_decrease > 0:
        return rel_decrease / threshold
    else:
        return 0.0


# === block: score_1 (check id='monomer_monotonic_trend') ===
def score_1(artifact, step, ctx):
    data = artifact.get('temperatures', [])
    convs = [entry for entry in data if entry.get('deposition_type') == 'conventional' and entry.get('temperature') in [100, 300, 400, 450]]
    convs.sort(key=lambda x: x['temperature'])
    def compute_monomer_fraction(entry):
        dist = entry.get('island_size_distribution', [])
        monomer_cov = None
        for item in dist:
            if item.get('size') == 1:
                monomer_cov = item.get('coverage')
                break
        if monomer_cov is None:
            return None
        # total deposited coverage is 0.2 ML
        return monomer_cov / 0.2
    fracs = []
    for entry in convs:
        f = compute_monomer_fraction(entry)
        if f is None:
            return 0.0
        fracs.append(f)
    if len(fracs) < 2:
        return 0.0
    for i in range(1, len(fracs)):
        if fracs[i] > fracs[i-1]:
            return 0.0
    return 1.0


# === block: score_2 (check id='bragg_rel_increase_100K') ===
def score_2(artifact, step, ctx):
    data = artifact.get('temperatures', [])
    def find_entry(dep_type):
        for entry in data:
            if entry.get('temperature') == 100 and entry.get('deposition_type') == dep_type:
                return entry
        return None
    conv = find_entry('conventional')
    energ = find_entry('energetic')
    if conv is None or energ is None:
        return 0.0
    # arrays must be provided and have same length
    conv_cov = conv.get('coverage', [])
    conv_int = conv.get('bragg_intensity', [])
    energ_cov = energ.get('coverage', [])
    energ_int = energ.get('bragg_intensity', [])
    if not conv_cov or not conv_int or len(conv_cov) != len(conv_int):
        return 0.0
    if not energ_cov or not energ_int or len(energ_cov) != len(energ_int):
        return 0.0
    # Find the data point at 5 ML (within 0.1 ML) for conventional deposition
    def value_at_5ml(covs, vals):
        for c, v in zip(covs, vals):
            if abs(c - 5.0) < 0.1:
                return v
        return None
    c_5 = value_at_5ml(conv_cov, conv_int)
    e_5 = value_at_5ml(energ_cov, energ_int)
    if c_5 is None or e_5 is None or c_5 == 0:
        return 0.0
    rel_increase = (e_5 - c_5) / c_5
    threshold = step.get('threshold', 0.30)
    if rel_increase >= threshold:
        return 1.0
    elif rel_increase > 0:
        return rel_increase / threshold
    else:
        return 0.0


# === block: score_3 (check id='bragg_negligible_450K') ===
def score_3(artifact, step, ctx):
    data = artifact.get('temperatures', [])
    def find_entry(dep_type):
        for entry in data:
            if entry.get('temperature') == 450 and entry.get('deposition_type') == dep_type:
                return entry
        return None
    conv = find_entry('conventional')
    energ = find_entry('energetic')
    if conv is None or energ is None:
        return 0.0

    def find_value_at_5ml(covs, vals):
        """Return the value at the coverage point closest to 5 ML within 0.1 ML tolerance."""
        best = None
        best_dist = float('inf')
        for c, v in zip(covs, vals):
            d = abs(c - 5.0)
            if d < best_dist:
                best_dist = d
                best = v
        if best_dist > 0.1:
            return None
        return best

    conv_cov = conv.get('coverage', [])
    conv_int = conv.get('bragg_intensity', [])
    conv_rough = conv.get('roughness', [])
    energ_cov = energ.get('coverage', [])
    energ_int = energ.get('bragg_intensity', [])
    energ_rough = energ.get('roughness', [])
    if not conv_cov or not conv_int or len(conv_cov) != len(conv_int):
        return 0.0
    if not energ_cov or not energ_int or len(energ_cov) != len(energ_int):
        return 0.0
    if not conv_rough or len(conv_cov) != len(conv_rough):
        return 0.0
    if not energ_rough or len(energ_cov) != len(energ_rough):
        return 0.0

    c_bragg = find_value_at_5ml(conv_cov, conv_int)
    e_bragg = find_value_at_5ml(energ_cov, energ_int)
    c_rough = find_value_at_5ml(conv_cov, conv_rough)
    e_rough = find_value_at_5ml(energ_cov, energ_rough)

    if c_bragg is None or e_bragg is None or c_rough is None or e_rough is None:
        return 0.0
    if c_bragg == 0 or c_rough == 0:
        return 0.0

    bragg_rel_diff = abs((e_bragg - c_bragg) / c_bragg)
    rough_rel_diff = abs((e_rough - c_rough) / c_rough)
    tol = step.get('threshold', 0.05)
    return 1.0 if bragg_rel_diff <= tol and rough_rel_diff <= tol else 0.0


# === block: score_4 (check id='bragg_oscillation_highT') ===
def score_4(artifact, step, ctx):
    data = artifact.get('temperatures', [])
    # choose a high‑T condition, e.g., T=450 K energetic
    for entry in data:
        if entry.get('temperature') == 450 and entry.get('deposition_type') == 'energetic':
            bragg = entry.get('bragg_intensity', [])
            if len(bragg) < 3:
                return 0.0
            # look for a local maximum
            has_peak = any(bragg[i] > bragg[i-1] and bragg[i] > bragg[i+1] for i in range(1, len(bragg)-1))
            return 1.0 if has_peak else 0.0
    # fallback: try T=400 K energetic if 450 missing
    for entry in data:
        if entry.get('temperature') == 400 and entry.get('deposition_type') == 'energetic':
            bragg = entry.get('bragg_intensity', [])
            if len(bragg) >= 3 and any(bragg[i] > bragg[i-1] and bragg[i] > bragg[i+1] for i in range(1, len(bragg)-1)):
                return 1.0
            return 0.0
    return 0.0


_SCORERS = {
    'monomer_rel_decrease_100K': score_0,
    'monomer_monotonic_trend': score_1,
    'bragg_rel_increase_100K': score_2,
    'bragg_negligible_450K': score_3,
    'bragg_oscillation_highT': score_4,
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
