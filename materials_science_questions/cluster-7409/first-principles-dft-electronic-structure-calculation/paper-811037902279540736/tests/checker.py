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


# === block: score_0 (check id='electronic_structure') ===
def score_0(artifact, step, ctx):
    compounds = ['LiTi2O4', 'Li4Ti5O12', 'Li2Ti2O4', 'Li7Ti5O12']
    expected = step['expected']
    tol = step['tolerances']
    numeric_fields = ['band_gap', 'o2p_valence_band_width', 'valence_to_conduction_separation']
    total = 0
    correct = 0
    for comp in compounds:
        exp = expected.get(comp, {})
        act = artifact.get(comp, {})
        for f in numeric_fields:
            total += 1
            try:
                if abs(act.get(f, None) - exp[f]) <= tol[f]:
                    correct += 1
            except (TypeError, KeyError):
                pass
        total += 1
        if act.get('t2g_eg_splitting_observed', False) == exp.get('t2g_eg_splitting_observed', True):
            correct += 1
    return correct / total if total > 0 else 0.0


# === block: score_1 (check id='optical_properties') ===
def score_1(artifact, step, ctx):
    compounds = ['LiTi2O4', 'Li4Ti5O12', 'Li2Ti2O4', 'Li7Ti5O12']
    expected = step['expected']
    tol_epsilon = step['tolerances']['static_dielectric_constant']
    tol_peak = step['tolerances']['dielectric_peak_energy']
    tol_abs = step['tolerances']['absorption_peak_energy']
    total_comp = 0
    total_score = 0.0
    for comp in compounds:
        exp = expected.get(comp, {})
        act = artifact.get(comp, {})
        total_comp += 1
        cscore = 0.0
        # static_dielectric_constant
        if abs(act.get('static_dielectric_constant', None) - exp['static_dielectric_constant']) <= tol_epsilon:
            cscore += 1
        # dielectric_peak_A_energy
        exp_a = exp.get('dielectric_peak_A_energy')
        act_a = act.get('dielectric_peak_A_energy')
        if exp_a is None:
            if act_a is None:
                cscore += 1
        else:
            if act_a is not None and abs(act_a - exp_a) <= tol_peak:
                cscore += 1
        # dielectric_peak_B_energy
        if abs(act.get('dielectric_peak_B_energy', None) - exp['dielectric_peak_B_energy']) <= tol_peak:
            cscore += 1
        # absorption_peak_energies
        exp_peaks = sorted(exp.get('absorption_peak_energies', []))
        act_peaks = sorted(act.get('absorption_peak_energies', []))
        if len(act_peaks) == len(exp_peaks) and len(exp_peaks) > 0:
            matched = sum(1 for e, a in zip(exp_peaks, act_peaks) if abs(e - a) <= tol_abs)
            cscore += matched / float(len(exp_peaks))
        # normalise per compound (max possible 4.0)
        total_score += cscore / 4.0
    return total_score / total_comp if total_comp > 0 else 0.0


_SCORERS = {
    'electronic_structure': score_0,
    'optical_properties': score_1,
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
