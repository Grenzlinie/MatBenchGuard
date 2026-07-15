import os
import json
import csv

# === author imports / helpers ===
import csv, re, math, os


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
    spec_outputs = spec.get('output_contract', {}).get('outputs', [])
    csv_contract = next((o for o in spec_outputs if o.get('file') == 'computed_properties.csv'), {})
    required_cols = []
    for c in csv_contract.get('schema', {}).get('required_columns', []):
        if isinstance(c, str):
            required_cols.append(c)
        else:
            required_cols.append(c.get('name', ''))
    step1_config = spec['steps'][0]['config']
    step2_config = spec['steps'][1]['config']
    return {
        'required_cols': required_cols,
        'step1_config': step1_config,
        'step2_config': step2_config,
    }


# === block: score_0 (check id='step1') ===
def score_0(artifact, step, ctx):
        cfg = ctx['step1_config']
        required_cols = ctx['required_cols']
    
        # 1) Shape check: all required columns present, at least 16 rows
        if not isinstance(artifact, list) or len(artifact) < 16:
            shape_score = 0.0
        else:
            present = all(col in artifact[0] for col in required_cols)
            shape_score = 1.0 if present else 0.0
    
        rows = artifact if isinstance(artifact, list) else []
        by_re = {}
        for row in rows:
            re = row.get('RE', '').strip()
            if re:
                by_re[re] = row
    
        t_map = cfg['tolerance_factor_map']
        phase_map = cfg['phase_map']
        dielec_gold = cfg['dielectric_gold']
        elastic_ranges = cfg['elastic_ranges']
        B_fit = cfg['bulk_modulus_fit']
        E_fit = cfg['lattice_energy_fit']
        dielectric_tol = cfg['dielectric_tol']
        bulk_tol_rel = cfg['bulk_tol_rel']
        energy_tol_rel = cfg['energy_tol_rel']
        bulk_cons_tol = cfg['bulk_consistency_tol']
        t_tol = cfg['t_tol']
        total_re = len(t_map)
    
        def safe_float(v, default=0.0):
            try:
                return float(v)
            except:
                return default
    
        # 2) tolerance factor check
        t_ok = 0
        for re, truth_t in t_map.items():
            row = by_re.get(re)
            if row is None:
                continue
            agent_t = safe_float(row.get('t'))
            if abs(agent_t - truth_t) <= t_tol:
                t_ok += 1
        t_score = t_ok / total_re if total_re else 0.0
    
        # 3) space group check
        sg_ok = 0
        for re, truth_sg in phase_map.items():
            row = by_re.get(re)
            if row is None:
                continue
            agent_sg = row.get('space_group', '').strip().replace(' ', '')
            if agent_sg.lower() == truth_sg.replace(' ', '').lower():
                sg_ok += 1
        sg_score = sg_ok / total_re if total_re else 0.0
    
        # 4) dielectric constant check
        dc_ok = 0
        for re, gold_dc in dielec_gold.items():
            row = by_re.get(re)
            if row is None:
                continue
            agent_dc = safe_float(row.get('dielectric_constant'))
            if abs(agent_dc - gold_dc) <= dielectric_tol:
                dc_ok += 1
        dc_score = dc_ok / total_re if total_re else 0.0
    
        # 5) elastic quality: symmetry, range, internal bulk modulus consistency
        def get_elastic_dict(row):
            keys = ['C11','C12','C44','C13','C33','C66','C15','C25','C35','C46']
            d = {k: safe_float(row.get(k, 0.0)) for k in keys}
            return d
    
        elastic_ok = 0
        for re, phase in phase_map.items():
            row = by_re.get(re)
            if row is None:
                continue
            e = get_elastic_dict(row)
            range_conf = elastic_ranges.get(phase)
            if range_conf is None:
                continue
            # check zero components
            zero_passed = True
            for col in range_conf.get('zero', []):
                if abs(e.get(col, 0.0)) > 1.0:
                    zero_passed = False
                    break
            if not zero_passed:
                continue
            # check nonzero components in range
            nonzero_passed = True
            for col, bounds in range_conf.get('nonzero', {}).items():
                val = e.get(col, 0.0)
                if val < bounds[0] or val > bounds[1]:
                    nonzero_passed = False
                    break
            if not nonzero_passed:
                continue
            # recompute bulk modulus for cubic and tetragonal, compare to agent's bulk_modulus
            agent_B = safe_float(row.get('bulk_modulus'))
            if phase == 'Fm-3m':
                c11, c12, c44 = e['C11'], e['C12'], e['C44']
                B_recomputed = (c11 + 2*c12) / 3.0
            elif phase == 'I4/m':
                c11, c12, c13, c33, c44, c66 = e['C11'], e['C12'], e['C13'], e['C33'], e['C44'], e['C66']
                Bv = (2*(c11+c12) + c33 + 4*c13) / 9.0
                denom = c11 + c12 + 2*c33 - 4*c13
                if abs(denom) > 1e-6:
                    Br = (c33*(c11+c12) - 2*c13*c13) / denom
                else:
                    Br = Bv
                B_recomputed = (Bv + Br) / 2.0
            else:
                # monoclinic: skip recompute, use consistency with fit later
                B_recomputed = agent_B  # bypass
            if abs(agent_B - B_recomputed) > bulk_cons_tol * max(abs(agent_B), 1.0):
                continue
            elastic_ok += 1
        elastic_score = elastic_ok / total_re if total_re else 0.0
    
        # 6) bulk modulus vs expected linear fit
        B_ok = 0
        for re, t_val in t_map.items():
            row = by_re.get(re)
            if row is None:
                continue
            agent_B = safe_float(row.get('bulk_modulus'))
            expected_B = B_fit['a'] + B_fit['b'] * t_val
            if expected_B != 0:
                rel_err = abs(agent_B - expected_B) / abs(expected_B)
            else:
                rel_err = abs(agent_B - expected_B)
            if rel_err <= bulk_tol_rel:
                B_ok += 1
        B_score = B_ok / total_re if total_re else 0.0
    
        # 7) lattice energy vs expected linear fit
        E_ok = 0
        for re, t_val in t_map.items():
            row = by_re.get(re)
            if row is None:
                continue
            agent_E = safe_float(row.get('lattice_energy'))
            expected_E = E_fit['a'] + E_fit['b'] * t_val
            if expected_E != 0:
                rel_err = abs(agent_E - expected_E) / abs(expected_E)
            else:
                rel_err = abs(agent_E - expected_E)
            if rel_err <= energy_tol_rel:
                E_ok += 1
        E_score = E_ok / total_re if total_re else 0.0
    
        # 8) sound velocity plausibility (positive and reasonable range)
        v_ok = 0
        for row in rows:
            S = safe_float(row.get('S_wave_velocity'))
            P = safe_float(row.get('P_wave_velocity'))
            if S > 0 and P > 0 and S < 10000.0 and P < 15000.0 and S < P:
                v_ok += 1
        if rows:
            v_score = v_ok / len(rows)
        else:
            v_score = 0.0
    
        # aggregate sub-scores with weights
        sub_weights = {
            'shape': 0.02,
            't': 0.03,
            'sg': 0.05,
            'dc': 0.15,
            'elastic': 0.30,
            'bulk': 0.25,
            'energy': 0.15,
            'sound': 0.05
        }
        final = (shape_score * sub_weights['shape'] +
                 t_score * sub_weights['t'] +
                 sg_score * sub_weights['sg'] +
                 dc_score * sub_weights['dc'] +
                 elastic_score * sub_weights['elastic'] +
                 B_score * sub_weights['bulk'] +
                 E_score * sub_weights['energy'] +
                 v_score * sub_weights['sound'])
        return min(max(final, 0.0), 1.0)


# === block: score_1 (check id='step2') ===
def score_1(artifact, step, ctx):
        cfg = ctx['step2_config']
        text = artifact if isinstance(artifact, str) else ''
        expected_coeffs = {
            'B': (-525.89, 711.91),
            'E_L': (-165.25, -131.41)
        }
        patterns = [
            r'B\s*=\s*([-+]?\d*\.?\d+)\s*\+\s*([-+]?\d*\.?\d+)\s*\*\s*t',
            r'E_L\s*=\s*([-+]?\d*\.?\d+)\s*\+\s*([-+]?\d*\.?\d+)\s*\*\s*t'
        ]
        found = {'B': None, 'E_L': None}
        for line in text.split('\n'):
            line = line.strip()
            for i, pat in enumerate(patterns):
                m = re.search(pat, line)
                if m:
                    key = 'B' if i == 0 else 'E_L'
                    try:
                        a = float(m.group(1))
                        b = float(m.group(2))
                        found[key] = (a, b)
                    except:
                        pass
        score_parts = []
        for key in ['B', 'E_L']:
            if found[key] is None:
                score_parts.append(0.0)
                continue
            a_agent, b_agent = found[key]
            a_exp, b_exp = expected_coeffs[key]
            tol_rel = cfg['coeff_tol_rel']
            rel_err_a = abs(a_agent - a_exp) / (abs(a_exp) + 1e-9)
            rel_err_b = abs(b_agent - b_exp) / (abs(b_exp) + 1e-9)
            if rel_err_a <= tol_rel and rel_err_b <= tol_rel:
                score_parts.append(1.0)
            else:
                score_parts.append(0.0)
        final = (score_parts[0] + score_parts[1]) / 2.0
        return final


_SCORERS = {
    'step1': score_0,
    'step2': score_1,
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
