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
    return {}


# === block: score_0 (check id='filter_alpha_rp') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not rows or not isinstance(rows, list): return 0.0
    try:
        wl = [float(r.get('wavelength', float('nan'))) for r in rows]
        rp = [float(r.get('Rp', float('nan'))) for r in rows]
        alph = [float(r.get('alpha', float('nan'))) for r in rows]
    except Exception:
        return 0.0
    if not wl:
        return 0.0
    import math
    idx_min = min(range(len(rp)), key=lambda i: rp[i])
    rp_min = rp[idx_min]
    wl_min = wl[idx_min]
    cfg = step.get('config', {})
    rp_thr = cfg.get('rp_threshold', 0.2)
    alpha_thr = cfg.get('alpha_threshold', 0.01)
    lo, hi = cfg.get('wavelength_range', [1.54, 1.56])
    if not (lo <= wl_min <= hi) or rp_min > rp_thr:
        return 0.0
    alph_in_range = [alph[i] for i in range(len(wl)) if lo <= wl[i] <= hi]
    if alph_in_range:
        if max(alph_in_range) > alpha_thr:
            return 0.0
    else:
        if max(alph) > alpha_thr:
            return 0.0
    return 1.0


# === block: score_1 (check id='resonator_alpha_vs_Lambda') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not rows: return 0.0
    try:
        lam_col = [float(r.get('Lambda', float('nan'))) for r in rows]
        alpha = [float(r.get('alpha', float('nan'))) for r in rows]
    except Exception:
        return 0.0
    if not lam_col:
        return 0.0
    idx_min = min(range(len(alpha)), key=lambda i: alpha[i])
    alpha_min = alpha[idx_min]
    lam_min = lam_col[idx_min]
    cfg = step.get('config', {})
    p_min, p_max = cfg.get('period_min', 0.247), cfg.get('period_max', 0.251)
    alpha_thr = cfg.get('alpha_threshold', 0.01)
    if p_min <= lam_min <= p_max and alpha_min <= alpha_thr:
        return 1.0
    return 0.0


# === block: score_2 (check id='resonator_Rp_vs_lambda') ===
def score_2(artifact, step, ctx):
    rows = artifact
    if not rows: return 0.0
    try:
        wl = [float(r.get('wavelength', float('nan'))) for r in rows]
        rp = [float(r.get('Rp', float('nan'))) for r in rows]
    except Exception:
        return 0.0
    if not wl:
        return 0.0
    idx_min = min(range(len(rp)), key=lambda i: rp[i])
    rp_min = rp[idx_min]
    wl_min = wl[idx_min]
    cfg = step.get('config', {})
    lo, hi = cfg.get('wavelength_range', [1.54, 1.56])
    rp_thr = cfg.get('rp_threshold', 0.2)
    if lo <= wl_min <= hi and rp_min <= rp_thr:
        return 1.0
    return 0.0


# === block: score_3 (check id='brillouin_diagram') ===
def score_3(artifact, step, ctx):
    rows = artifact
    if not rows: return 0.0
    try:
        for r in rows:
            wl = float(r.get('wavelength', 0))
            alpha = float(r.get('alpha', 1))
            beta = float(r.get('beta', 0))
            cfg = step.get('config', {})
            if (cfg.get('alpha_threshold', 0.01) >= alpha and
                cfg.get('wavelength_min', 1.5) <= wl <= cfg.get('wavelength_max', 1.6) and
                cfg.get('beta_min', 0.0) <= beta <= cfg.get('beta_max', 50.0)):
                return 1.0
    except Exception:
        return 0.0
    return 0.0


_SCORERS = {
    'filter_alpha_rp': score_0,
    'resonator_alpha_vs_Lambda': score_1,
    'resonator_Rp_vs_lambda': score_2,
    'brillouin_diagram': score_3,
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
