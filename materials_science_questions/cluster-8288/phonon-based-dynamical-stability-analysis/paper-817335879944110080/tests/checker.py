import os
import json
import csv

# === author imports / helpers ===
import json
import csv
import os
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
    def prepare(outputs_dir, spec):
        func_cfg = None
        for step in spec.get('steps', []):
            if step['id'] == 'functionalized_check':
                func_cfg = step.get('config', {})
                break
        if func_cfg is None:
            func_cfg = {}
        classification_list = func_cfg.get('classification', [])
        gold_map = {}
        for entry in classification_list:
            key = (entry['M'], entry['T'])
            gold_map[key] = (entry['half_metallic'], entry['semiconductor'])
        ctx = {
            'gold_classification': gold_map,
            'eu2cf2_spin_down_gap_min': func_cfg.get('eu2cf2_spin_down_gap_min', 2.0),
            'gd2cf2_band_gap_target': func_cfg.get('gd2cf2_band_gap_target', 1.38),
            'gd2cf2_band_gap_tol': func_cfg.get('gd2cf2_band_gap_tol_pct', 0.20),
            'gd2coh2_band_gap_target': func_cfg.get('gd2coh2_band_gap_target', 0.882),
            'gd2coh2_band_gap_tol': func_cfg.get('gd2coh2_band_gap_tol_pct', 0.20),
            'tm2coh2_work_function_target': func_cfg.get('tm2coh2_work_function_target', 1.46),
            'tm2coh2_work_function_tol': func_cfg.get('tm2coh2_work_function_tol', 0.15),
            'gd_magnetization_min': func_cfg.get('gd_magnetization_min', 13.7),
            'afm_magnetization_abs_max': func_cfg.get('afm_magnetization_abs_max', 0.1),
            'afm_entries': func_cfg.get('afm_entries', [{'M':'Ho','T':'F'},{'M':'Dy','T':'OH'}])
        }
        return ctx


# === block: score_0 (check id='bare_preference_check') ===
def score_0(artifact, step, ctx):
    try:
        if not isinstance(artifact, list) or len(artifact) != 12:
            return 0.0
        if not isinstance(artifact[0], dict) or 'delta_E' not in artifact[0]:
            return 0.0
        neg_count = 0
        for row in artifact:
            if not isinstance(row, dict):
                return 0.0
            val = row.get('delta_E')
            if val is None:
                return 0.0
            try:
                de = float(val)
            except (ValueError, TypeError):
                return 0.0
            if de < 0:
                neg_count += 1
        return neg_count / 12.0
    except Exception:
        return 0.0


# === block: score_1 (check id='stability_report_check') ===
def score_1(artifact, step, ctx):
    def score_stability(artifact, step, ctx):
        if not isinstance(artifact, dict):
            return 0.0
        expected = ["Ce","Pr","Nd","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb"]
        valid = 0
        for el in expected:
            if el not in artifact:
                continue
            entry = artifact[el]
            if not isinstance(entry, dict):
                continue
            if entry.get('phonon_imaginary_modes') == False and entry.get('min_frequency', -1000) > -5:
                valid += 1
        return valid / len(expected)


# === block: score_2 (check id='functionalized_check') ===
def score_2(artifact, step, ctx):
    def score_func(artifact, step, ctx):
        if not isinstance(artifact, list) or len(artifact) != 24:
            return 0.0
        gold_map = ctx.get('gold_classification', {})
        sub_scores = []

        # 1. Classification accuracy (fraction of correct flags among all entries)
        correct = 0
        total = 0
        for entry in artifact:
            M = entry.get('M')
            T = entry.get('T')
            if (M, T) not in gold_map:
                continue
            expected_hm, expected_sc = gold_map[(M, T)]
            actual_hm = entry.get('half_metallic', None)
            actual_sc = entry.get('semiconductor', None)
            if isinstance(actual_hm, bool) and isinstance(actual_sc, bool):
                if actual_hm == expected_hm and actual_sc == expected_sc:
                    correct += 1
            total += 1
        if total > 0:
            sub_scores.append(correct / total)
        else:
            sub_scores.append(0.0)

        # 2. Eu2CF2 spin-down band gap check
        eu2_found = False
        spin_gap_ok = False
        for entry in artifact:
            if entry.get('M') == 'Eu' and entry.get('T') == 'F':
                eu2_found = True
                if entry.get('half_metallic') == True:
                    gap = entry.get('spin_down_band_gap')
                    if isinstance(gap, (int, float)) and gap >= ctx.get('eu2cf2_spin_down_gap_min', 2.0):
                        spin_gap_ok = True
                break
        sub_scores.append(1.0 if eu2_found and spin_gap_ok else 0.0)

        # 3. Gd2CF2 band gap (semiconductor, within tolerance)
        def check_band_gap(entries, M, T, target, tol_pct):
            for entry in entries:
                if entry.get('M') == M and entry.get('T') == T:
                    if entry.get('semiconductor') != True:
                        return 0.0
                    gap = entry.get('band_gap')
                    if not isinstance(gap, (int, float)):
                        return 0.0
                    rel_err = abs(gap - target) / target if target != 0 else abs(gap)
                    if rel_err <= tol_pct:
                        return 1.0
                    else:
                        return 0.0
            return 0.0
        sub_scores.append(check_band_gap(artifact, 'Gd', 'F', ctx.get('gd2cf2_band_gap_target', 1.38), ctx.get('gd2cf2_band_gap_tol', 0.20)))
        # 4. Gd2C(OH)2 band gap
        sub_scores.append(check_band_gap(artifact, 'Gd', 'OH', ctx.get('gd2coh2_band_gap_target', 0.882), ctx.get('gd2coh2_band_gap_tol', 0.20)))

        # 5. Tm2C(OH)2 work function
        wf_target = ctx.get('tm2coh2_work_function_target', 1.46)
        wf_tol = ctx.get('tm2coh2_work_function_tol', 0.15)
        wf_ok = False
        for entry in artifact:
            if entry.get('M') == 'Tm' and entry.get('T') == 'OH':
                wf = entry.get('work_function')
                if isinstance(wf, (int, float)) and abs(wf - wf_target) <= wf_tol:
                    wf_ok = True
                break
        sub_scores.append(1.0 if wf_ok else 0.0)

        # 6. Magnetization checks: Gd2CT2 ≥ 13.7, AFM entries near 0
        mag_min = ctx.get('gd_magnetization_min', 13.7)
        afm_max = ctx.get('afm_magnetization_abs_max', 0.1)
        afm_entries = ctx.get('afm_entries', [])
        def mag_check(entries, M, T, min_val=None, max_val=None):
            for entry in entries:
                if entry.get('M') == M and entry.get('T') == T:
                    mag = entry.get('total_magnetization')
                    if not isinstance(mag, (int, float)):
                        return 0
                    if min_val is not None and mag < min_val:
                        return 0
                    if max_val is not None and abs(mag) > max_val:
                        return 0
                    return 1
            return 0
        mag_score = 0.0
        mag_score += mag_check(artifact, 'Gd', 'F', min_val=mag_min)
        mag_score += mag_check(artifact, 'Gd', 'OH', min_val=mag_min)
        for afm in afm_entries:
            mag_score += mag_check(artifact, afm['M'], afm['T'], max_val=afm_max)
        mag_entries_count = 2 + len(afm_entries)
        if mag_entries_count > 0:
            sub_scores.append(mag_score / mag_entries_count)
        else:
            sub_scores.append(1.0)

        if not sub_scores:
            return 0.0
        return sum(sub_scores) / len(sub_scores)


_SCORERS = {
    'bare_preference_check': score_0,
    'stability_report_check': score_1,
    'functionalized_check': score_2,
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
