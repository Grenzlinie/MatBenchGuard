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
        ref = {
            'ref_total_at_minus18': {
                '100-type': -34.32,
                'wandering': -34.11,
                '110-type': -34.36
            },
            'tolerance_total_meV': 2.0,
            'wandering_max_diff_from_min_meV': 1.5,
            'strain_low_threshold': -1.6,
            'strain_high_threshold': -2.1,
            'ordering_margin': 0.2  # strain range where crossover can happen, we consider strains > -1.6+margin as low, < -2.1-margin as high
        }
        return ref


# === block: score_0 (check id='step_csv_valid') ===
def score_0(artifact, step, ctx):
        rows = artifact
        if not rows or len(rows) == 0:
            return 0.0
        required = {'strain', 'configuration', 'total_energy', 'short_range_energy', 'self_strain_energy', 'long_range_dipole_energy'}
        if not required.issubset(rows[0].keys()):
            return 0.0
        # check at least one row per config per strain
        strains = set()
        configs_seen = set()
        for r in rows:
            try:
                s_val = float(r['strain'])
                strains.add(s_val)
                configs_seen.add(r['configuration'].strip())
            except (ValueError, KeyError):
                continue
        # we expect roughly 11 strains from -3.0 to -1.0 step 0.2
        if len(strains) < 8 or len(configs_seen) < 3:
            return 0.0
        return 1.0


# === block: score_1 (check id='step_total_energy_trend') ===
def score_1(artifact, step, ctx):
        rows = artifact
        ref = ctx
        strain_low = ref['strain_low_threshold']
        strain_high = ref['strain_high_threshold']
        order_margin = ref['ordering_margin']
        tol = ref['tolerance_total_meV']
        wand_tol = ref['wandering_max_diff_from_min_meV']

        # build dict: strain -> {config: total_energy}
        data = {}
        for r in rows:
            try:
                s = float(r['strain'])
                cfg = r['configuration'].strip()
                e = float(r['total_energy'])
            except (ValueError, KeyError):
                continue
            data.setdefault(s, {})[cfg] = e

        # collect scores
        low_scores = []
        high_scores = []
        wand_scores = []

        for s, cfgs in data.items():
            if not {'100-type', '110-type', 'wandering'}.issubset(cfgs):
                continue
            e100 = cfgs['100-type']
            e110 = cfgs['110-type']
            ewand = cfgs['wandering']
            if s > strain_low + order_margin:  # low-magnitude strain (closer to 0)
                low_scores.append(1.0 if e100 <= e110 + tol else 0.0)
            if s < strain_high - order_margin:  # high-magnitude strain
                high_scores.append(1.0 if e110 <= e100 + tol else 0.0)
            # wandering check for intermediate strains around -1.8%
            if abs(s - (-1.8)) < 0.4:
                min_other = min(e100, e110)
                wand_scores.append(1.0 if abs(ewand - min_other) <= wand_tol else 0.0)

        # combine sub-scores
        n_low = len(low_scores)
        n_high = len(high_scores)
        n_wand = len(wand_scores)
        score_low = (sum(low_scores) / n_low) if n_low else 0.0
        score_high = (sum(high_scores) / n_high) if n_high else 0.0
        score_wand = (sum(wand_scores) / n_wand) if n_wand else 0.0

        # total for this step: average over the three criteria
        total = (score_low + score_high + score_wand) / 3.0
        # but if no low/high strains available, adjust
        active = 0
        s = 0.0
        if n_low > 0:
            s += score_low
            active += 1
        if n_high > 0:
            s += score_high
            active += 1
        if n_wand > 0:
            s += score_wand
            active += 1
        return s / active if active > 0 else 0.0


# === block: score_2 (check id='step_decomposition_trend') ===
def score_2(artifact, step, ctx):
        rows = artifact
        # for each strain where all three configs exist, check ordering:
        # short_range_energy: 100-type < 110-type
        # self_strain_energy: 110-type < 100-type
        # long_range_dipole_energy: 110-type < 100-type
        data = {}
        for r in rows:
            try:
                s = float(r['strain'])
                cfg = r['configuration'].strip()
                sr = float(r['short_range_energy'])
                ss = float(r['self_strain_energy'])
                lr = float(r['long_range_dipole_energy'])
            except (ValueError, KeyError):
                continue
            data.setdefault(s, {})[cfg] = (sr, ss, lr)

        total_check = 0
        passed = 0
        for s, cfgs in data.items():
            if '100-type' not in cfgs or '110-type' not in cfgs:
                continue
            sr100, ss100, lr100 = cfgs['100-type']
            sr110, ss110, lr110 = cfgs['110-type']
            # short-range: 100-type should be lower (more negative) or equal
            passed_sr = 1.0 if sr100 <= sr110 else 0.0
            # self-strain: 110-type lower
            passed_ss = 1.0 if ss110 <= ss100 else 0.0
            # long-range dipole: 110-type lower
            passed_lr = 1.0 if lr110 <= lr100 else 0.0
            passed += (passed_sr + passed_ss + passed_lr)
            total_check += 3

        return (passed / total_check) if total_check > 0 else 0.0


_SCORERS = {
    'step_csv_valid': score_0,
    'step_total_energy_trend': score_1,
    'step_decomposition_trend': score_2,
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
