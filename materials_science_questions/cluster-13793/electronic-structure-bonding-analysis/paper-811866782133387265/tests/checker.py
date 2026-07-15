import os
import json
import csv

# === author imports / helpers ===
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
    return spec.get('steps', [])


# === block: score_0 (check id='geometry_optimization') ===
def score_0(artifact, step, ctx):
    # geometry_optimization scorer
    def score_field(val, ref, tol):
        if val is None:
            return 0.0
        diff = abs(val - ref)
        if diff <= tol:
            return 1.0
        if diff <= 2 * tol:
            return 1.0 - (diff - tol) / tol
        return 0.0

    cfg = step.get('config', {})
    systems = cfg.get('systems', [])
    fields_cfg = cfg.get('fields', {})
    trends = cfg.get('trends', {})
    # parse artifact rows: list of dicts
    rows = {}
    for r in artifact:
        sys = str(r.get('system', '')).strip()
        rows[sys] = r
    # field scoring
    field_scores = []
    for sys in systems:
        row = rows.get(sys)
        if row is None:
            field_scores.append(0.0)
            continue
        for fname, fcfg in fields_cfg.items():
            raw = row.get(fname)
            if raw is None:
                field_scores.append(0.0)
                continue
            try:
                val = float(raw)
            except (ValueError, TypeError):
                field_scores.append(0.0)
                continue
            ref = fcfg['ref'].get(sys)
            if ref is None:
                field_scores.append(0.0)
                continue
            tol = fcfg.get('tol_abs', 0.0)
            field_scores.append(score_field(val, ref, tol))
    field_avg = sum(field_scores) / len(field_scores) if field_scores else 0.0

    # trend scoring
    trend_score = 1.0
    trend_count = 0
    if trends.get('volume_increase'):
        trend_count += 1
        vals = []
        for sys in systems:
            row = rows.get(sys)
            if row:
                try:
                    vals.append(float(row.get('volume_per_4fu', None)))
                except:
                    vals.append(None)
            else:
                vals.append(None)
        if len(vals) == len(systems) and all(v is not None for v in vals):
            if not all(vals[i] < vals[i+1] for i in range(len(vals)-1)):
                trend_score = 0.0
        else:
            trend_score = 0.0
    if trends.get('energy_decrease'):
        trend_count += 1
        vals = []
        for sys in systems:
            row = rows.get(sys)
            if row:
                try:
                    vals.append(float(row.get('total_energy_per_4fu', None)))
                except:
                    vals.append(None)
            else:
                vals.append(None)
        if len(vals) == len(systems) and all(v is not None for v in vals):
            # energy should strictly decrease (more negative) with H content
            if not all(vals[i] > vals[i+1] for i in range(len(vals)-1)):
                trend_score = 0.0
        else:
            trend_score = 0.0

    # combine field and trend scores
    field_weight = 1.0 - trends.get('volume_increase', {}).get('weight_in_step', 0.0) - trends.get('energy_decrease', {}).get('weight_in_step', 0.0)
    trend_weight = trends.get('volume_increase', {}).get('weight_in_step', 0.0) + trends.get('energy_decrease', {}).get('weight_in_step', 0.0)
    step_score = field_weight * field_avg + trend_weight * trend_score
    return max(0.0, min(1.0, step_score))


# === block: score_1 (check id='eos_fit') ===
def score_1(artifact, step, ctx):
    # eos_fit scorer
    cfg = step.get('config', {})
    systems = cfg.get('systems', [])
    H2_e = cfg.get('H2_energy')
    target_stab = cfg.get('target_stabilization', {})
    weights = cfg.get('weights_within_step', {})

    rows = {}
    for r in artifact:
        sys = str(r.get('system', '')).strip()
        rows[sys] = r

    # field comparison
    def score_field(val, ref, tol):
        if val is None:
            return 0.0
        diff = abs(val - ref)
        if diff <= tol:
            return 1.0
        if diff <= 2 * tol:
            return 1.0 - (diff - tol) / tol
        return 0.0

    field_scores = []
    for fname, fcfg in [('equilibrium_energy_per_4fu', cfg.get('equilibrium_energy', {})),
                           ('equilibrium_volume_per_4fu', cfg.get('equilibrium_volume', {})),
                           ('bulk_modulus', cfg.get('bulk_modulus', {}))]:
        if not fcfg:
            continue
        ref_map = fcfg.get('ref', {})
        tol = fcfg.get('tol_abs', 0.0)
        for sys in systems:
            row = rows.get(sys)
            if not row:
                field_scores.append(0.0)
                continue
            try:
                val = float(row.get(fname))
            except:
                field_scores.append(0.0)
                continue
            ref = ref_map.get(sys)
            if ref is None:
                field_scores.append(0.0)
                continue
            field_scores.append(score_field(val, ref, tol))
    field_avg = sum(field_scores) / len(field_scores) if field_scores else 0.0

    # stabilization recompute
    stab_scores = []
    e_ZrNi = None
    try:
        row0 = rows.get('ZrNi')
        if row0:
            e_ZrNi = float(row0.get('equilibrium_energy_per_4fu'))
    except:
        e_ZrNi = None

    # check ZrNi stabilization is NaN or empty
    if 'ZrNi' in rows:
        val = rows['ZrNi'].get('stabilization_energy_per_H2')
        if val is None or (isinstance(val, str) and val.strip().lower() == 'nan'):
            stab_scores.append(1.0)
        else:
            stab_scores.append(0.0)

    x_map = {'ZrNiH': 1, 'ZrNiH2': 2, 'ZrNiH3': 3}
    for sys in ['ZrNiH', 'ZrNiH2', 'ZrNiH3']:
        row = rows.get(sys)
        if not row or e_ZrNi is None:
            stab_scores.append(0.0)
            continue
        try:
            e = float(row.get('equilibrium_energy_per_4fu'))
        except:
            stab_scores.append(0.0)
            continue
        x = x_map.get(sys, 1)
        recomputed_stab = (e - e_ZrNi - x * H2_e) / x
        target = target_stab.get(sys)
        if target is None:
            stab_scores.append(0.0)
            continue
        # threshold_or_better: more negative is better, so recomputed_stab <= target gives full credit
        if recomputed_stab <= target:
            stab_scores.append(1.0)
        elif recomputed_stab >= 0.0:
            stab_scores.append(0.0)
        else:
            # error = recomputed_stab - target (positive)
            # penalize when recomputed_stab > target, up to 0.2 eV difference
            error = recomputed_stab - target
            tol = cfg.get('stabilization_tol_abs', 0.1) + 0.1  # allow some margin
            stab_scores.append(max(0.0, 1.0 - error / tol))
    stab_avg = sum(stab_scores) / len(stab_scores) if stab_scores else 0.0

    # trend: recomputed stabilization should strictly decrease (more negative) from ZrNiH to ZrNiH3
    trend_score = 1.0
    if cfg.get('trends', {}).get('stab_magnitude_increase'):
        recomputed_stabs = []
        for sys in ['ZrNiH', 'ZrNiH2', 'ZrNiH3']:
            row = rows.get(sys)
            if not row or e_ZrNi is None:
                recomputed_stabs.append(None)
                continue
            try:
                e = float(row.get('equilibrium_energy_per_4fu'))
            except:
                recomputed_stabs.append(None)
                continue
            x = x_map.get(sys, 1)
            recomputed_stabs.append((e - e_ZrNi - x * H2_e) / x)
        if len(recomputed_stabs) == 3 and all(v is not None for v in recomputed_stabs):
            if not (recomputed_stabs[0] > recomputed_stabs[1] > recomputed_stabs[2]):
                trend_score = 0.0
        else:
            trend_score = 0.0

    w_field = weights.get('field_comparison', 0.4)
    w_stab = weights.get('stabilization_recompute', 0.5)
    w_trend = weights.get('trend', 0.1)
    step_score = w_field * field_avg + w_stab * stab_avg + w_trend * trend_score
    return max(0.0, min(1.0, step_score))


_SCORERS = {
    'geometry_optimization': score_0,
    'eos_fit': score_1,
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
