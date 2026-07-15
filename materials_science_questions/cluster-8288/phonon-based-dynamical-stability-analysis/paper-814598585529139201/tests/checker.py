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
        ctx = {}
        for step in spec.get('steps', []):
            ctx[step['id']] = step.get('gold', {})
        return ctx


# === block: score_0 (check id='pristine') ===
def score_0(artifact, step, ctx):
        gold = ctx.get(step['id'], {})
        if not isinstance(artifact, dict):
            return 0.0
        n = 5.0
        total = 0.0
        # numeric fields
        for field in ['lattice_constant_A', 'Ni_magnetic_moment_muB', 'AFM_FM_energy_diff_meV', 'HSE06_band_gap_eV']:
            val = artifact.get(field)
            if val is not None and field in gold and isinstance(gold[field], dict) and 'value' in gold[field]:
                ref = gold[field]['value']
                tol = gold[field]['tolerance']
                if abs(val - ref) <= tol:
                    total += 1.0
        # direct gap
        direct = artifact.get('band_gap_direct')
        if isinstance(direct, bool) and direct == gold.get('band_gap_direct', True):
            total += 1.0
        return total / n


# === block: score_1 (check id='strain') ===
def score_1(artifact, step, ctx):
        gold = ctx.get(step['id'], {})
        entries_gold = gold.get('entries', [])
        energy_tol = gold.get('energy_diff_tolerance', 15.0)
        gap_tol = gold.get('band_gap_tolerance', 0.2)
        expected_signs = gold.get('expected_signs', {})
        ref_by_strain = {}
        for entry in entries_gold:
            s = entry['strain_percent']
            ref_by_strain[s] = entry
        required_strains = set(ref_by_strain.keys())
        if not isinstance(artifact, list):
            return 0.0
        energy_score = 0.0
        gap_score = 0.0
        sign_score = 0.0
        gaps = {}
        count = len(required_strains)
        for item in artifact:
            s = item.get('strain_percent')
            if s is None:
                continue
            ref = ref_by_strain.get(s)
            if ref is None:
                continue
            e_diff = item.get('AFM_FM_energy_diff_meV')
            if e_diff is not None and abs(e_diff - ref['AFM_FM_energy_diff_meV']) <= energy_tol:
                energy_score += 1.0
            bg = item.get('HSE06_band_gap_eV')
            if bg is not None and abs(bg - ref['HSE06_band_gap_eV']) <= gap_tol:
                gap_score += 1.0
            sign_expected = expected_signs.get(str(int(s)))
            if sign_expected is not None and e_diff is not None:
                if (sign_expected == 'positive' and e_diff > 0) or (sign_expected == 'negative' and e_diff < 0):
                    sign_score += 1.0
            gaps[s] = bg
        # normalize per entry
        energy_score /= count
        gap_score /= count
        sign_score /= count
        # band gap ordering: must be strictly increasing from -10% to +10%
        sorted_strains = sorted(required_strains)
        gap_values = [gaps.get(s) for s in sorted_strains]
        order_ok = False
        if len(gap_values) == len(sorted_strains) and all(isinstance(v, (int, float)) for v in gap_values):
            if all(gap_values[i] + 1e-12 < gap_values[i+1] for i in range(len(gap_values)-1)):
                order_ok = True
        ordering_score = 1.0 if order_ok else 0.0
        w_energy = 0.3
        w_gap = 0.3
        w_sign = 0.2
        w_order = 0.2
        score = w_energy * energy_score + w_gap * gap_score + w_sign * sign_score + w_order * ordering_score
        return max(0.0, min(1.0, score))


_SCORERS = {
    'pristine': score_0,
    'strain': score_1,
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
