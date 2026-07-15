import os
import json
import csv

# === author imports / helpers ===
import numpy as np
import csv, json, os


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
    steps = spec.get('steps', [])
    ctx = {'gold': {}}
    for s in steps:
        if 'gold' in s:
            ctx['gold'][s['id']] = s['gold']
    return ctx


# === block: score_0 (check id='step_03') ===
def score_0(artifact, step, ctx):
    data = artifact  # list of dicts from csv
    if not data or len(data) < 4*50:
        return 0.0
    import collections
    by_sys = collections.defaultdict(list)
    for row in data:
        by_sys[row['system']].append(row)
    required = ['undoped','Fe','Co','Ni']
    if any(s not in by_sys for s in required):
        return 0.0

    gold = ctx['gold']['step_03']
    tol_seebeck_rel = gold['tolerances']['seebeck_enhance_rel']
    tol_zt_abs = gold['tolerances']['zt_enhance_abs']

    def get_arrays(sys_name):
        rows = by_sys[sys_name]
        n = np.array([float(r['carrier_concentration']) for r in rows])
        s = np.array([float(r['Seebeck_coefficient']) for r in rows])
        zt = np.array([float(r['ZT']) for r in rows])
        idx = np.argsort(n)
        return n[idx], s[idx], zt[idx]

    n_und, s_und, zt_und = get_arrays('undoped')
    undoped_max_zt = float(np.max(zt_und))

    scores = []
    for dopant in ['Fe','Co','Ni']:
        n_d, s_d, zt_d = get_arrays(dopant)
        i_max = np.argmax(np.abs(s_d))
        S_max = s_d[i_max]
        n_at_max = n_d[i_max]
        # undoped S at same n (nearest interpolation)
        try:
            S_und = float(np.interp(n_at_max, n_und, s_und))
        except Exception:
            idx_und = np.argmin(np.abs(n_und - n_at_max))
            S_und = float(s_und[idx_und])

        if np.abs(S_und) < 1e-12:
            enhance = 0.0
        else:
            enhance = np.abs(S_max) / np.abs(S_und)

        target_seeb = gold['seebeck_enhance'][dopant]
        if enhance >= target_seeb:
            score_enh = 1.0
        else:
            shortfall = target_seeb - enhance
            score_enh = max(0.0, 1.0 - shortfall / (target_seeb * tol_seebeck_rel))

        d_max_zt = float(np.max(zt_d))
        zt_enh = d_max_zt / undoped_max_zt if undoped_max_zt > 1e-12 else 0.0
        if dopant == 'Fe':
            target_zt_enh = 1.0
        else:
            target_zt_enh = gold['zt_enhance'][dopant]
        if zt_enh >= target_zt_enh:
            score_zt = 1.0
        else:
            score_zt = max(0.0, 1.0 - (target_zt_enh - zt_enh) / tol_zt_abs)

        scores.append(0.6 * score_enh + 0.4 * score_zt)

    # structural ordering: Ni > Co > Fe
    enh_vals = {}
    for d in ['Fe','Co','Ni']:
        n_d, s_d, _ = get_arrays(d)
        i_max = np.argmax(np.abs(s_d))
        n_at = n_d[i_max]
        try:
            S_und = float(np.interp(n_at, n_und, s_und))
        except Exception:
            idx_und = np.argmin(np.abs(n_und - n_at))
            S_und = float(s_und[idx_und])
        if np.abs(S_und) < 1e-12:
            enh_vals[d] = 0.0
        else:
            enh_vals[d] = np.abs(s_d[i_max]) / np.abs(S_und)
    ordering_ok = (enh_vals['Ni'] > enh_vals['Co'] > enh_vals['Fe'])
    score_order = 1.0 if ordering_ok else 0.0

    # sign change
    sign_score = 0.0
    for d in ['Fe','Co','Ni']:
        _, s_d, _ = get_arrays(d)
        has_pos = np.any(s_d > 0)
        has_neg = np.any(s_d < 0)
        sign_score += 0.5 if (has_pos and has_neg) else 0.0
    sign_score = sign_score / 3.0

    avg_meta = 0.5 * np.mean(scores) + 0.3 * score_order + 0.2 * sign_score
    return float(min(max(avg_meta, 0.0), 1.0))


# === block: score_1 (check id='step_04') ===
def score_1(artifact, step, ctx):
    data = artifact
    if not isinstance(data, dict):
        return 0.0
    gold = ctx['gold']['step_04']
    tol = step.get('tolerances', {})

    def check_field_symmetric(dopant, field, target, rel_tol=None, abs_tol=None):
        try:
            val = float(data[dopant][field])
        except:
            return 0.0
        if rel_tol:
            if target == 0:
                if val == 0: return 1.0
                else: return 0.0
            err = abs(val - target) / abs(target * rel_tol)
            return max(0.0, 1.0 - err)
        elif abs_tol:
            return max(0.0, 1.0 - abs(val - target) / abs_tol)
        else:
            return 1.0 if val == target else 0.0

    def check_directional(value, target, tol_type, tol_val):
        if tol_type == 'relative':
            if value >= target:
                return 1.0
            shortfall = target - value
            return max(0.0, 1.0 - shortfall / (target * tol_val))
        else:  # absolute
            if value >= target:
                return 1.0
            return max(0.0, 1.0 - (target - value) / tol_val)

    required_keys = ['undoped','Fe','Co','Ni']
    if any(k not in data for k in required_keys):
        return 0.0

    scores = []
    # undoped peak_ZT (directional, absolute)
    try:
        val = float(data['undoped']['peak_ZT'])
        scores.append(check_directional(val, gold['undoped']['peak_ZT'], 'absolute', tol.get('peak_ZT_abs', 0.05)))
    except:
        scores.append(0.0)

    for d in ['Fe','Co','Ni']:
        gd = gold[d]
        # Seebeck enhancement (directional, relative)
        try:
            s1 = check_directional(float(data[d]['max_Seebeck_enhancement']), gd['max_Seebeck_enhancement'], 'relative', tol.get('max_Seebeck_enhancement_rel', 0.3))
        except:
            s1 = 0.0
        # carrier concentration (symmetric, relative)
        s2 = check_field_symmetric(d, 'carrier_concentration_at_max_S', gd['carrier_concentration_at_max_S'], rel_tol=tol.get('carrier_concentration_rel', 0.5))
        # ZT enhancement (directional, absolute)
        try:
            s3 = check_directional(float(data[d]['ZT_enhancement']), gd['ZT_enhancement'], 'absolute', tol.get('ZT_enhancement_abs', 0.1))
        except:
            s3 = 0.0
        # peak ZT (directional, absolute)
        try:
            s4 = check_directional(float(data[d]['peak_ZT']), gd['peak_ZT'], 'absolute', tol.get('peak_ZT_abs', 0.05))
        except:
            s4 = 0.0
        scores.append(np.mean([s1,s2,s3,s4]))
    final_score = np.mean(scores)
    return float(min(max(final_score, 0.0), 1.0))


_SCORERS = {
    'step_03': score_0,
    'step_04': score_1,
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
