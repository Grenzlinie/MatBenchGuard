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
    import json
    with open('/app/outputs/perfect_dislocation_results.json', 'r') as f:
        perfect = json.load(f)
    return {'perfect_results': perfect}


# === block: score_0 (check id='perfect_values') ===
def score_0(artifact, step, ctx):
    # artifact: dict with Cu and Ag
    # step['gold'] contains expected values
    # step['tolerances'] has spacing_a, energy_eV, elastic_d_nm
    fields_cu = ['relaxed_d_nm', 'relaxed_d_a', 'energy_eV', 'elastic_d_nm']
    fields_ag = fields_cu

    passes = 0
    total = len(fields_cu) + len(fields_ag)

    for metal, fields in [('Cu', fields_cu), ('Ag', fields_ag)]:
        if metal not in artifact:
            continue
        gold_metal = step['gold'].get(metal, {})
        tol = step['tolerances']
        for key in fields:
            val = artifact[metal].get(key)
            gold = gold_metal.get(key)
            if val is None or gold is None:
                continue
            if 'd_a' in key:
                if abs(val - gold) <= tol['spacing_a']:
                    passes += 1
            elif 'energy' in key:
                if abs(val - gold) <= tol['energy_eV']:
                    passes += 1
            else:  # elastic_d_nm, relaxed_d_nm
                if abs(val - gold) <= tol['elastic_d_nm']:
                    passes += 1
    return passes / total if total > 0 else 0.0


# === block: score_1 (check id='displacement_cu_check') ===
def score_1(artifact, step, ctx):
    # artifact: list of csv rows with 'x' and 'delta_u_x'
    import sys
    import json

    thresholds = step['thresholds']  # [1/6, 2/3]
    tol_a = step['tolerance_a']

    x_vals = []
    du_vals = []
    for row in artifact:
        try:
            x = float(row['x'])
            du = float(row['delta_u_x'])
            x_vals.append(x)
            du_vals.append(du)
        except:
            continue

    if len(x_vals) < 10:
        return 0.0

    # sort by x
    pairs = sorted(zip(x_vals, du_vals), key=lambda p: p[0])
    x_sorted = [p[0] for p in pairs]
    du_sorted = [p[1] for p in pairs]

    def interp_x(target_du):
        # find segment where du crosses target_du
        for i in range(len(du_sorted)-1):
            if (du_sorted[i] <= target_du <= du_sorted[i+1]) or (du_sorted[i] >= target_du >= du_sorted[i+1]):
                frac = (target_du - du_sorted[i]) / (du_sorted[i+1] - du_sorted[i])
                return x_sorted[i] + frac * (x_sorted[i+1] - x_sorted[i])
        return None

    x1 = interp_x(thresholds[0])
    x2 = interp_x(thresholds[1])
    if x1 is None or x2 is None:
        return 0.0

    computed_d_a = abs(x2 - x1)

    # get reported d_a from perfect_results
    reported = ctx.get('perfect_results', {}).get('Cu', {}).get('relaxed_d_a')
    if reported is None:
        return 0.0

    diff = abs(computed_d_a - reported)
    if diff <= tol_a:
        return 1.0
    # partial credit: linear decay from tol_a to 3*tol_a
    if diff >= 3*tol_a:
        return 0.0
    return (3*tol_a - diff) / (2*tol_a)


# === block: score_2 (check id='lomer_cottrell_values') ===
def score_2(artifact, step, ctx):
    # artifact: dict with Cu and Ag
    # step['gold'] contains expected values
    # step['tolerances'] has spacing_a, energy_eV, elastic_a

    metals = ['Cu', 'Ag']
    spacing_fields = ['d1_a', 'd2_a', 'd_bar_a', 'elastic_d1_a', 'elastic_d2_a']
    energy_field = 'energy_eV'
    ratio_field = 'd1_d2_ratio'

    metal_scores = []
    for metal in metals:
        if metal not in artifact:
            metal_scores.append(0.0)
            continue
        gold_metal = step['gold'].get(metal, {})
        tol = step['tolerances']
        sub_checks = 0
        passes = 0
        # ratio structural check
        ratio_val = artifact[metal].get(ratio_field)
        if ratio_val is not None and ratio_val > 2.0:
            passes += 1
        sub_checks += 1
        # spacing numeric checks
        for key in spacing_fields:
            val = artifact[metal].get(key)
            gold = gold_metal.get(key)
            if val is not None and gold is not None:
                if abs(val - gold) <= tol['spacing_a']:
                    passes += 1
            sub_checks += 1
        # energy check
        val = artifact[metal].get(energy_field)
        gold = gold_metal.get(energy_field)
        if val is not None and gold is not None:
            if abs(val - gold) <= tol['energy_eV']:
                passes += 1
        sub_checks += 1
        metal_scores.append(passes / sub_checks if sub_checks > 0 else 0.0)

    return sum(metal_scores) / len(metal_scores) if metal_scores else 0.0


_SCORERS = {
    'perfect_values': score_0,
    'displacement_cu_check': score_1,
    'lomer_cottrell_values': score_2,
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
