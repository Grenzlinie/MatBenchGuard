import os
import json
import csv

# === author imports / helpers ===
import json
import os
import numpy as np


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
        steps = spec['steps']
        props_step = next(s for s in steps if s['id'] == 'props_table')
        gold_table = props_step.get('gold_table', {})
        tolerances = props_step.get('tolerances', {})
        sw_step = next(s for s in steps if s['id'] == 'spectral_width_reduction')
        target_reduction_Si = sw_step['target_reduction_Si']
        tolerance_Si = sw_step['tolerance_Si']
        target_reduction_Ge = sw_step['target_reduction_Ge']
        tolerance_Ge = sw_step['tolerance_Ge']
        ord_step = next(s for s in steps if s['id'] == 'ordering_and_flatbands')
        flatband_regions = ord_step['flatband_regions']
        ordering_check = ord_step['ordering_check']
        return {
            'gold_table': gold_table,
            'tolerances': tolerances,
            'target_reduction_Si': target_reduction_Si,
            'tolerance_Si': tolerance_Si,
            'target_reduction_Ge': target_reduction_Ge,
            'tolerance_Ge': tolerance_Ge,
            'flatband_regions': flatband_regions,
            'ordering_check': ordering_check,
        }


# === block: score_0 (check id='props_table') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold = ctx.get('gold_table', {})
        tolerances = ctx.get('tolerances', {})
        if not isinstance(artifact, list):
            return 0.0
        try:
            agent = {item['name']: item for item in artifact}
        except (KeyError, TypeError):
            return 0.0
        total_weight = 0.0
        score_val = 0.0
        n_gold = max(len(gold.keys()), 1)
        # Safely unwrap tolerance values
        try:
            tol_kappa = float(tolerances.get('kappa', 0.2))
            tol_theta = float(tolerances.get('theta', 0.1))
            tol_v = float(tolerances.get('v', 0.1))
            tol_gamma = float(tolerances.get('gamma_abs', 0.2))
        except (TypeError, ValueError):
            return 0.0
        def safe_float(value):
            """Return float or None if conversion fails."""
            if value is None:
                return None
            try:
                return float(value)
            except (TypeError, ValueError):
                return None
        for comp, ref in gold.items():
            a = agent.get(comp, {})
            if not isinstance(a, dict):
                continue
            # --- kappa (80% of step weight) ---
            if 'kappa_l_300' in ref:
                agent_kappa = safe_float(a.get('kappa_l_300'))
                ref_kappa = safe_float(ref['kappa_l_300'])
                if ref_kappa is None or ref_kappa == 0:
                    # can't compute relative error; treat as mismatch
                    ok = (agent_kappa is not None and abs(agent_kappa) <= 1e-6)
                else:
                    ok = (agent_kappa is not None and abs(agent_kappa - ref_kappa) / ref_kappa <= tol_kappa)
                w = 0.8 / n_gold
                total_weight += w
                if ok:
                    score_val += w
            # --- other fields (20% of step weight) ---
            other_fields = ['theta_TA','theta_LA','theta_D','v_TA','v_LA','v_s','gamma_300','gamma_TA','gamma_LA']
            n_other = len(other_fields)
            for field in other_fields:
                if field not in ref:
                    continue
                ref_val = safe_float(ref[field])
                agent_val = safe_float(a.get(field))
                if ref_val is None:
                    # skip if gold is missing/non-numeric
                    continue
                if agent_val is None:
                    ok = False
                elif 'theta' in field or 'v_' in field:
                    tol = tol_theta if 'theta' in field else tol_v
                    if ref_val == 0:
                        ok = (abs(agent_val) <= 1e-6)
                    else:
                        ok = (abs(agent_val - ref_val) / ref_val <= tol)
                else:  # gamma fields
                    ok = (abs(agent_val - ref_val) <= tol_gamma)
                w = 0.2 / (n_other * n_gold)
                total_weight += w
                if ok:
                    score_val += w
        if total_weight == 0:
            return 0.0
        return score_val / total_weight


# === block: score_1 (check id='spectral_width_reduction') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        import json
        props_path = '/app/outputs/computed_properties.json'
        with open(props_path) as f:
            props = json.load(f)
        props_dict = {p['name']: p for p in props}
        if not isinstance(artifact, dict):
            return 0.0
        recomputed_widths = {}
        for comp, data in artifact.items():
            if comp not in props_dict:
                continue
            freqs = data.get('frequencies', [])
            if not freqs:
                continue
            all_freqs = [f for branch in freqs for f in branch]
            if not all_freqs:
                continue
            maxf = max(all_freqs)
            minf = min(all_freqs)
            recomputed_widths[comp] = maxf - minf
        consistent = True
        for comp, sw in recomputed_widths.items():
            reported = props_dict[comp].get('spectral_width')
            if reported is None:
                consistent = False
                break
            if sw == 0:
                if abs(reported) > 1e-6:
                    consistent = False
                    break
            else:
                rel_diff = abs(reported - sw) / sw
                if rel_diff > 0.05:
                    consistent = False
                    break
        if not consistent:
            return 0.0
        # Si reduction
        si_ok = False
        if 'Si46' in recomputed_widths and 'Na8Si46' in recomputed_widths:
            sw_Si46 = recomputed_widths['Si46']
            sw_Na = recomputed_widths['Na8Si46']
            reduction_Si = (sw_Si46 - sw_Na) / sw_Si46
            si_ok = abs(reduction_Si - ctx['target_reduction_Si']) <= ctx['tolerance_Si']
        # Ge reduction
        ge_ok = False
        if 'Ge46' in recomputed_widths and 'K8Ge44□2' in recomputed_widths:
            sw_Ge = recomputed_widths['Ge46']
            sw_KGe = recomputed_widths['K8Ge44□2']
            reduction_Ge = (sw_Ge - sw_KGe) / sw_Ge
            ge_ok = abs(reduction_Ge - ctx['target_reduction_Ge']) <= ctx['tolerance_Ge']
        return (1.0 if si_ok else 0.0) + (1.0 if ge_ok else 0.0)


# === block: score_2 (check id='ordering_and_flatbands') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        import json
        if not isinstance(artifact, dict):
            return 0.0
        props_path = '/app/outputs/computed_properties.json'
        with open(props_path) as f:
            props = json.load(f)
        props_dict = {p['name']: p for p in props}
        # rattler ordering
        na = props_dict.get('Na8Si46', {}).get('rattler_freq')
        k = props_dict.get('K8Si46', {}).get('rattler_freq')
        order_score = 0.0
        if na is not None and k is not None and na < k:
            order_score = 0.5
        # flatbands in Si46
        if 'Si46' not in artifact:
            return order_score
        si_data = artifact['Si46']
        qpoints = si_data.get('qpoints', [])
        freqs = si_data.get('frequencies', [])
        if not qpoints or not freqs:
            return order_score
        # distances along path
        dist = [0.0]
        for i in range(1, len(qpoints)):
            d = np.sqrt(sum((a-b)**2 for a,b in zip(qpoints[i], qpoints[i-1])))
            dist.append(dist[-1] + d)
        # find flat segments
        flat_segments = []
        threshold = 2.0
        for branch in freqs:
            n = len(qpoints)
            if len(branch) < n:
                continue
            i = 0
            while i <= n - 3:
                segment = branch[i:i+3]
                if max(segment) - min(segment) < threshold:
                    median_freq = np.median(segment)
                    flat_segments.append(median_freq)
                    i += 3
                else:
                    i += 1
        regions = ctx['flatband_regions'].get('Si46', [])
        region_found = [False]*len(regions)
        for med in flat_segments:
            for idx, (low, high) in enumerate(regions):
                if low <= med <= high:
                    region_found[idx] = True
        fb_score = 0.5 * (sum(region_found) / len(regions))
        return order_score + fb_score


_SCORERS = {
    'props_table': score_0,
    'spectral_width_reduction': score_1,
    'ordering_and_flatbands': score_2,
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
