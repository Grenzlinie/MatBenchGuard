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
    for s in spec.get('steps', []):
        if s['id'] == 'peierls_recompute':
            ctx['bla_range'] = s.get('target_BLA_range', [0.015,0.025])
            ctx['gain_range'] = s.get('target_energy_gain_range', [2,6])
        elif s['id'] == 'electronic_gaps':
            ctx['gap_metallic'] = 0.1
            ctx['gap_semiconducting'] = 0.1
    return ctx


# === block: score_0 (check id='phonon_stability') ===
def score_0(artifact, step, ctx):
    neg_thresh = -0.001
    freq_keys = {
        'LC_vac_phonon_freqs': 0.2,
        'ZZ_vac_phonon_freqs': 0.2,
        'LC_enc_phonon_freqs': 0.2,
        'ZZ_enc_phonon_freqs': 0.2,
        '3H_enc_phonon_freqs': 0.2
    }
    score = 0.0
    for key, weight in freq_keys.items():
        freqs = artifact.get(key)
        if not isinstance(freqs, list):
            continue
        has_neg = any(f < neg_thresh for f in freqs if isinstance(f, (int,float)))
        if 'enc' in key:
            if not has_neg:
                score += weight
        else:
            if has_neg:
                score += weight
    return round(score, 10)


# === block: score_1 (check id='peierls_recompute') ===
def score_1(artifact, step, ctx):
    curve = artifact.get('LC_PD_curve')
    if not isinstance(curve, dict):
        return 0.0
    bla = curve.get('BLA_nm')
    energy = curve.get('energy_meV_per_Te')
    if not isinstance(bla, list) or not isinstance(energy, list) or len(bla) < 3 or len(bla) != len(energy):
        return 0.0
    min_idx = energy.index(min(energy))
    bla_min = bla[min_idx]
    # reference energy at BLA closest to 0
    bla0_idx = min(range(len(bla)), key=lambda i: abs(bla[i]))
    e_ref = energy[bla0_idx]
    gain = e_ref - energy[min_idx]
    bla_range = step.get('target_BLA_range', [0.015,0.025])
    gain_range = step.get('target_energy_gain_range', [2,6])
    bla_ok = bla_range[0] <= bla_min <= bla_range[1]
    gain_ok = gain_range[0] <= gain <= gain_range[1]
    return 0.5 * (1.0 if bla_ok else 0.0) + 0.5 * (1.0 if gain_ok else 0.0)


# === block: score_2 (check id='electronic_gaps') ===
def score_2(artifact, step, ctx):
    gap_lc = artifact.get('band_gap_LC_eV')
    gap_zz = artifact.get('band_gap_ZZ_eV')
    gap_3h = artifact.get('band_gap_3H_eV')
    if gap_lc is None or gap_zz is None or gap_3h is None:
        return 0.0
    score = 0.0
    if gap_lc < 0.1:
        score += 1/3
    if gap_zz > 0.1:
        score += 1/3
    if gap_3h > 0.1:
        score += 1/3
    return score


_SCORERS = {
    'phonon_stability': score_0,
    'peierls_recompute': score_1,
    'electronic_gaps': score_2,
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
