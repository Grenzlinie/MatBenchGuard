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
    return {'spec': spec}


# === block: score_0 (check id='bg_check') ===
def score_0(artifact, step, ctx):
    rows = artifact
    gap = {}
    for r in rows:
        try:
            gap[r['System']] = float(r['BandGap'])
        except (KeyError, ValueError):
            pass
    required = step['config']['required_systems']
    presence = sum(1 for s in required if s in gap) / len(required) if required else 1.0

    scores = []
    weights = [0.2, 0.2, 0.2, 0.1, 0.3]

    # 0: presence
    scores.append(presence)

    # 1: undoped gap near 3.61
    ref = step['config']['undoped_gap_ref']
    tol = step['config']['undoped_tol']
    if 'undoped' in gap:
        scores.append(1.0 if abs(gap['undoped'] - ref) <= tol else 0.0)
    else:
        scores.append(0.0)

    # 2: codoped gaps less than undoped
    undoped_gap = gap.get('undoped')
    codoped_systems = [s for s in required if 'codoped' in s and s in gap]
    if undoped_gap and codoped_systems:
        ok = all(gap[s] < undoped_gap for s in codoped_systems)
        scores.append(1.0 if ok else 0.0)
    else:
        scores.append(0.0)

    # 3: (N,F) strII < strI
    if '(N,F)_codoped_strI' in gap and '(N,F)_codoped_strII' in gap:
        scores.append(1.0 if gap['(N,F)_codoped_strII'] < gap['(N,F)_codoped_strI'] else 0.0)
    else:
        scores.append(0.0)

    # 4: (N,F) codoped are the smallest among all codoped
    nf_keys = ['(N,F)_codoped_strI','(N,F)_codoped_strII']
    other_codoped = [s for s in codoped_systems if s not in nf_keys and s in gap]
    if all(k in gap for k in nf_keys) and other_codoped:
        nf_gaps = [gap[k] for k in nf_keys]
        max_nf = max(nf_gaps)
        ok = all(max_nf < gap[s] for s in other_codoped)
        scores.append(1.0 if ok else 0.0)
    else:
        scores.append(0.0)

    total = sum(w*s for w,s in zip(weights, scores))
    return max(0.0, min(1.0, total))


# === block: score_1 (check id='fe_check') ===
def score_1(artifact, step, ctx):
    rows = artifact
    data = {}
    for r in rows:
        try:
            s = r['System']
            rich = float(r['FormationEnergy_OxygenRich'])
            poor = float(r['FormationEnergy_OxygenPoor'])
            data[s] = {'rich': rich, 'poor': poor}
        except (KeyError, ValueError):
            pass
    required = step['config']['required_systems']
    presence = sum(1 for s in required if s in data) / len(required) if required else 1.0

    scores = []
    weights = [0.1, 0.1, 0.1, 0.1, 0.15, 0.15, 0.15, 0.15]

    # 0: presence
    scores.append(presence)

    # 1: N mono rich within tolerance
    N_rich = data.get('N_monodoped', {}).get('rich')
    if N_rich is not None:
        scores.append(1.0 if abs(N_rich - step['config']['N_mono_rich_ref']) <= step['config']['N_mono_rich_tol'] else 0.0)
    else:
        scores.append(0.0)

    # 2: N mono poor within tolerance
    N_poor = data.get('N_monodoped', {}).get('poor')
    if N_poor is not None:
        scores.append(1.0 if abs(N_poor - step['config']['N_mono_poor_ref']) <= step['config']['N_mono_poor_tol'] else 0.0)
    else:
        scores.append(0.0)

    # 3: (N,F) poor negative
    nf_poor_neg = True
    for k in ['(N,F)_codoped_strI','(N,F)_codoped_strII']:
        v = data.get(k, {}).get('poor')
        if v is not None and v >= 0:
            nf_poor_neg = False
    scores.append(1.0 if nf_poor_neg else 0.0)

    # 4: (N,F) poor < N mono poor
    nf_poor_vs_N = True
    if N_poor is not None:
        for k in ['(N,F)_codoped_strI','(N,F)_codoped_strII']:
            v = data.get(k, {}).get('poor')
            if v is not None and v >= N_poor:
                nf_poor_vs_N = False
    scores.append(1.0 if nf_poor_vs_N else 0.0)

    # 5: (N,F) strI and strII poor difference <= max_diff
    nf1 = data.get('(N,F)_codoped_strI', {}).get('poor')
    nf2 = data.get('(N,F)_codoped_strII', {}).get('poor')
    if nf1 is not None and nf2 is not None:
        diff = abs(nf1 - nf2)
        scores.append(1.0 if diff <= step['config']['nf_strI_strII_poor_diff_max'] else 0.0)
    else:
        scores.append(0.0)

    # 6: halogen rich ordering
    hal_rich = step['config']['halogen_rich_ordering']
    rvals = [data.get(k, {}).get('rich') for k in hal_rich]
    if all(v is not None for v in rvals):
        ok = all(rvals[i] < rvals[i+1] for i in range(len(rvals)-1))
        scores.append(1.0 if ok else 0.0)
    else:
        scores.append(0.0)

    # 7: halogen poor ordering
    hal_poor = step['config']['halogen_poor_ordering']
    pvals = [data.get(k, {}).get('poor') for k in hal_poor]
    if all(v is not None for v in pvals):
        ok = all(pvals[i] < pvals[i+1] for i in range(len(pvals)-1))
        scores.append(1.0 if ok else 0.0)
    else:
        scores.append(0.0)

    total = sum(w*s for w,s in zip(weights, scores))
    return max(0.0, min(1.0, total))


# === block: score_2 (check id='ae_check') ===
def score_2(artifact, step, ctx):
    rows = artifact
    wav = {}
    for r in rows:
        try:
            wav[r['System']] = float(r['AbsorptionEdgeWavelength'])
        except (KeyError, ValueError):
            pass
    required = step['config']['required_systems']
    presence = sum(1 for s in required if s in wav) / len(required) if required else 1.0

    scores = []
    weights = [0.2, 0.5, 0.3]

    # 0: presence
    scores.append(presence)

    # 1: (N,F) codoped have longest wavelength among codoped
    nf_sys = ['(N,F)_codoped_strI','(N,F)_codoped_strII']
    other_codoped = [s for s in required if 'codoped' in s and s not in nf_sys]
    nf_vals = [wav.get(k) for k in nf_sys if k in wav]
    other_vals = [wav.get(k) for k in other_codoped if k in wav]
    if nf_vals and other_vals:
        max_nf = max(nf_vals)
        ok = all(max_nf > v for v in other_vals)
        scores.append(1.0 if ok else 0.0)
    else:
        scores.append(0.0)

    # 2: all codoped wavelengths > undoped wavelength
    undoped = wav.get('undoped')
    all_codoped = [s for s in required if 'codoped' in s and s in wav]
    if undoped is not None and all_codoped:
        ok = all(wav[s] > undoped for s in all_codoped)
        scores.append(1.0 if ok else 0.0)
    else:
        scores.append(0.0)

    total = sum(w*s for w,s in zip(weights, scores))
    return max(0.0, min(1.0, total))


# === block: score_3 (check id='bea_check') ===
def score_3(artifact, step, ctx):
    rows = artifact
    data = {}
    for r in rows:
        try:
            data[r['System']] = {
                'vbm': float(r['VBM_vs_vacuum']),
                'cbm': float(r['CBM_vs_vacuum'])
            }
        except (KeyError, ValueError):
            pass
    required = step['config']['required_systems']
    presence = sum(1 for s in required if s in data) / len(required) if required else 1.0

    scores = []
    weights = [0.1, 0.5, 0.4]

    # 0: presence
    scores.append(presence)

    # 1: CBM > threshold for all systems
    cbm_th = step['config']['cbm_threshold']
    cbm_ok = all(data[s]['cbm'] > cbm_th for s in required if s in data)
    scores.append(1.0 if cbm_ok else 0.0)

    # 2: VBM < threshold for all systems
    vbm_th = step['config']['vbm_threshold']
    vbm_ok = all(data[s]['vbm'] < vbm_th for s in required if s in data)
    scores.append(1.0 if vbm_ok else 0.0)

    total = sum(w*s for w,s in zip(weights, scores))
    return max(0.0, min(1.0, total))


_SCORERS = {
    'bg_check': score_0,
    'fe_check': score_1,
    'ae_check': score_2,
    'bea_check': score_3,
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
