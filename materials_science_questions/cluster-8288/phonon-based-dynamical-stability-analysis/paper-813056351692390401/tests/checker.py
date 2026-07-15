import os
import json
import csv

# === author imports / helpers ===
import json


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


# === block: score_0 (check id='energy_asymptotes') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        try:
            ref = step.get('reference', {})
            rel_tol = step.get('tolerance_relative', 0.05)
            min_abs_tol = step.get('min_absolute_tol', 0.001)
            energies = artifact.get('energies', {})
            if not isinstance(energies, dict):
                return 0.0
            phases = ["1T'", '2H', '3R']
            fields = [
                'surface_energy_asymptote_J_per_m2',
                'cleaving_energy_asymptote_J_per_m2',
                'binding_energy_asymptote_eV',
                'vdw_energy_asymptote_J_per_m2'
            ]
            total = 0
            correct = 0
            for phase in phases:
                agent_phase = energies.get(phase)
                gold_phase = ref.get(phase)
                if not isinstance(agent_phase, dict) or not isinstance(gold_phase, dict):
                    continue
                for field in fields:
                    total += 1
                    agent_val = agent_phase.get(field)
                    gold_val = gold_phase.get(field)
                    if agent_val is None or gold_val is None:
                        continue
                    try:
                        tol = max(rel_tol * abs(float(gold_val)), min_abs_tol)
                        if abs(float(agent_val) - float(gold_val)) <= tol:
                            correct += 1
                    except (TypeError, ValueError):
                        continue
            if total == 0:
                return 0.0
            return float(correct) / float(total)
        except Exception:
            return 0.0


# === block: score_1 (check id='bandgap_2H') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        entries = artifact.get('bandgap_2H', [])
        if not entries:
            return 0.0
        sorted_entries = sorted(entries, key=lambda e: e.get('layer', 0))
        gaps = [e['bandgap_eV'] for e in sorted_entries if 'bandgap_eV' in e]
        if len(gaps) < 2:
            return 0.0
        monotonic = all(gaps[i] >= gaps[i+1] for i in range(len(gaps)-1))
        first_entry = sorted_entries[0]
        last_entry = sorted_entries[-1]
        abs_tol = step['abs_tol_eV']
        mono_score = 0.5 if monotonic else 0.0
        endpoint_score = 0.0
        first_gap = first_entry.get('bandgap_eV')
        last_gap = last_entry.get('bandgap_eV')
        if first_gap is not None and abs(first_gap - step['monolayer_bandgap_eV']) <= abs_tol:
            endpoint_score += 0.25
        if last_gap is not None and abs(last_gap - step['bulk_bandgap_eV']) <= abs_tol:
            endpoint_score += 0.25
        return mono_score + endpoint_score


# === block: score_2 (check id='optical_coeffs') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        ref = step['reference']
        rel_tol = step['tolerance_relative']
        optical = artifact.get('optical', {})
        phases = ["1T'", '2H', '3R']
        quantities = [
            'eps1_0_fit_coeffs',
            'n_0_fit_coeffs',
            'eps1_inf_fit_coeffs',
            'n_inf_fit_coeffs',
            'absorption_fit_coeffs',
            'reflectivity_fit_coeffs'
        ]
        total = 0
        correct = 0
        for phase in phases:
            agent_phase = optical.get(phase, {})
            gold_phase = ref.get(phase, {})
            for qty in quantities:
                total += 1
                agent_coeffs = agent_phase.get(qty, [])
                gold_coeffs = gold_phase.get(qty, [])
                if len(agent_coeffs) != 3 or len(gold_coeffs) != 3:
                    continue
                all_ok = True
                for a, g in zip(agent_coeffs, gold_coeffs):
                    tol = max(rel_tol * abs(g), 1e-8)
                    if abs(a - g) > tol:
                        all_ok = False
                        break
                if all_ok:
                    correct += 1
        if total == 0:
            return 0.0
        return correct / total


_SCORERS = {
    'energy_asymptotes': score_0,
    'bandgap_2H': score_1,
    'optical_coeffs': score_2,
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
