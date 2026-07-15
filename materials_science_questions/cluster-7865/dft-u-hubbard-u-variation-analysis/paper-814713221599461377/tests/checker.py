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


# === block: score_0 (check id='file_schema') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not isinstance(artifact, list):
            return 0.0

        required_entries = [
            # PBE+U LS band gaps
            ('PBE+U', 3.0, 'LS'),
            ('PBE+U', 5.0, 'LS'),
            ('PBE+U', 7.0, 'LS'),
            # PBE+U spin energies at U=3.0 eV
            ('PBE+U', 3.0, 'IS_FM'),
            ('PBE+U', 3.0, 'LS-HS_1:1_FM'),
            # PBE+U spin energies at U=5.0 eV (LS, IS_FM, HS_FM)
            ('PBE+U', 5.0, 'IS_FM'),
            ('PBE+U', 5.0, 'HS_FM'),
            # PBE+U spin energies at U=7.0 eV (LS, IS_FM, HS_FM)
            ('PBE+U', 7.0, 'IS_FM'),
            ('PBE+U', 7.0, 'HS_FM'),
            # HSE LS band gaps
            ('HSE', 0.05, 'LS'),
            ('HSE', 0.15, 'LS'),
            ('HSE', 0.25, 'LS'),
            # HSE spin energies (LS and IS_FM)
            ('HSE', 0.05, 'IS_FM'),
            ('HSE', 0.15, 'IS_FM'),
            ('HSE', 0.25, 'IS_FM'),
        ]

        present = set()
        for item in artifact:
            if not isinstance(item, dict):
                return 0.0
            for field in ['method','parameter','spin_state','band_gap_eV','total_energy_eV']:
                if field not in item:
                    return 0.0
            present.add((item['method'], item['parameter'], item['spin_state']))

        for entry in required_entries:
            if entry not in present:
                return 0.0
        return 1.0


# === block: score_1 (check id='pbeu_ls_bandgaps') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        config = step.get('config', {})
        gold = config.get('gold_bandgaps', {})
        tol = config.get('tolerance', 0.3)
        method = config.get('method', 'PBE+U')
        spin = config.get('spin_state', 'LS')
        param_key = config.get('parameter_key', 'parameter')
        entries = [e for e in artifact if e.get('method') == method and e.get('spin_state') == spin]
        if len(entries) != len(gold):
            return 0.0
        gaps = {}
        for e in entries:
            p = e.get(param_key)
            gap = e.get('band_gap_eV')
            if p is None or gap is None:
                return 0.0
            gaps[p] = gap
        ok = 0
        expected_params = sorted(gold.keys(), key=float)
        for p_str in expected_params:
            p = float(p_str)
            if p not in gaps:
                return 0.0
            diff = abs(gaps[p] - gold[p_str])
            if diff <= tol:
                ok += 1
            else:
                ok += max(0.0, 1.0 - (diff - tol) / tol)
        gap_score = ok / len(gold) if len(gold) > 0 else 1.0
        # monotonic: band gaps must increase with U
        sorted_params = sorted(gaps.keys())
        gaps_sorted = [gaps[u] for u in sorted_params]
        monotonic = all(gaps_sorted[i] <= gaps_sorted[i+1] for i in range(len(gaps_sorted)-1))
        monotonic_score = 1.0 if monotonic else 0.0
        return 0.6 * gap_score + 0.4 * monotonic_score


# === block: score_2 (check id='hse_ls_bandgaps') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        config = step.get('config', {})
        gold_exact = config.get('gold_exact', {})
        tol_exact = config.get('tolerance_exact', 0.2)
        range_alpha = config.get('range_alpha', 0.15)
        range_low = config.get('range_low', 0.3)
        range_high = config.get('range_high', 0.9)
        method = config.get('method', 'HSE')
        spin = config.get('spin_state', 'LS')
        param_key = config.get('parameter_key', 'parameter')
        entries = [e for e in artifact if e.get('method') == method and e.get('spin_state') == spin]
        if len(entries) != 3:
            return 0.0
        gaps = {}
        for e in entries:
            p = e.get(param_key)
            gap = e.get('band_gap_eV')
            if p is None or gap is None:
                return 0.0
            gaps[p] = gap
        # score exact golds
        exact_sum = 0.0
        count_exact = 0
        for p_s, target in gold_exact.items():
            p = float(p_s)
            if p not in gaps:
                return 0.0
            diff = abs(gaps[p] - target)
            if diff <= tol_exact:
                exact_sum += 1.0
            else:
                exact_sum += max(0.0, 1.0 - (diff - tol_exact) / tol_exact)
            count_exact += 1
        exact_part = exact_sum / count_exact if count_exact > 0 else 1.0
        # range check for α=0.15
        if range_alpha not in gaps:
            return 0.0
        gap_15 = gaps[range_alpha]
        range_part = 0.0
        if range_low <= gap_15 <= range_high:
            range_part = 1.0
        else:
            dist = (range_low - gap_15) if gap_15 < range_low else (gap_15 - range_high)
            range_part = max(0.0, 1.0 - dist / range_low)
        # monotonic increase with α
        sorted_alphas = sorted(gaps.keys())
        gaps_sorted = [gaps[a] for a in sorted_alphas]
        monotonic = all(gaps_sorted[i] <= gaps_sorted[i+1] for i in range(len(gaps_sorted)-1))
        monotonic_score = 1.0 if monotonic else 0.0
        return 0.4 * exact_part + 0.3 * range_part + 0.3 * monotonic_score


# === block: score_3 (check id='spin_energies_u3') ===
def score_3(artifact, step, ctx):
    def score(artifact, step, ctx):
        config = step.get('config', {})
        method = config.get('method', 'PBE+U')
        param = config.get('parameter', 3.0)
        max_diff = config.get('max_diff_eV', 0.15)
        spin_states = config.get('spin_states', ['LS','IS_FM','LS-HS_1:1_FM'])
        entries = [e for e in artifact if e.get('method') == method and e.get('parameter') == param
                    and e.get('spin_state') in spin_states]
        if len(entries) != len(spin_states):
            return 0.0
        energies = {}
        for e in entries:
            en = e.get('total_energy_eV')
            if en is None:
                return 0.0
            energies[e['spin_state']] = en
        for s in spin_states:
            if s not in energies:
                return 0.0
        en_vals = list(energies.values())
        diff = max(en_vals) - min(en_vals)
        diff_score = 1.0 if diff <= max_diff else max(0.0, 1.0 - (diff - max_diff) / max_diff)
        e_ls = energies['LS']
        e_is = energies['IS_FM']
        e_mix = energies['LS-HS_1:1_FM']
        order_correct = (e_is <= e_mix <= e_ls)
        order_score = 1.0 if order_correct else 0.0
        return 0.6 * diff_score + 0.4 * order_score


_SCORERS = {
    'file_schema': score_0,
    'pbeu_ls_bandgaps': score_1,
    'hse_ls_bandgaps': score_2,
    'spin_energies_u3': score_3,
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
