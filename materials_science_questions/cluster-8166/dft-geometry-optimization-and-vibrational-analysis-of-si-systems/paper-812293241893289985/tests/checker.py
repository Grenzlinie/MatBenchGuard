import os
import json
import csv

# === author imports / helpers ===
import math, json, os


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


# === block: score_0 (check id='step_geometry_check') ===
def score_0(artifact, step, ctx):
    references = step.get('references', [])
    if not references:
        return 0.0
    tol_R = step.get('tolerance_R_SiS', 0.02)
    tol_r = step.get('tolerance_r_XH', 0.02)
    tol_alpha = step.get('tolerance_alpha', 1.0)
    tol_E = step.get('tolerance_total_energy', 0.005)

    if not isinstance(artifact, list):
        return 0.0

    lookup = {}
    for ref in references:
        key = (ref['species'], ref['state_label'])
        lookup[key] = ref

    total_fields = 0
    matched_fields = 0
    for item in artifact:
        try:
            species = item['species']
            state_label = item['state_label']
        except (KeyError, TypeError):
            continue
        ref = lookup.get((species, state_label))
        if ref is None:
            continue
        total_fields += 4
        try:
            if math.isclose(item.get('R_SiS'), ref['R_SiS'], rel_tol=0, abs_tol=tol_R):
                matched_fields += 1
            if math.isclose(item.get('r_XH'), ref['r_XH'], rel_tol=0, abs_tol=tol_r):
                matched_fields += 1
            if math.isclose(item.get('alpha'), ref['alpha'], rel_tol=0, abs_tol=tol_alpha):
                matched_fields += 1
            if math.isclose(item.get('total_energy'), ref['total_energy'], rel_tol=0, abs_tol=tol_E):
                matched_fields += 1
        except (TypeError, KeyError):
            pass

    if total_fields == 0:
        return 0.0
    return matched_fields / total_fields


# === block: score_1 (check id='step_frequencies_check') ===
def score_1(artifact, step, ctx):
    references = step.get('references', [])
    if not references:
        return 0.0
    tol = step.get('tolerance_omega', 20.0)

    if not isinstance(artifact, list):
        return 0.0

    lookup = {}
    for ref in references:
        key = (ref['species'], ref['state_label'])
        lookup[key] = ref

    total_fields = 0
    matched_fields = 0
    for item in artifact:
        try:
            species = item['species']
            state_label = item['state_label']
        except (KeyError, TypeError):
            continue
        ref = lookup.get((species, state_label))
        if ref is None:
            continue
        total_fields += 3
        try:
            if math.isclose(item.get('omega_SiS'), ref['omega_SiS'], rel_tol=0, abs_tol=tol):
                matched_fields += 1
            if math.isclose(item.get('omega_XH'), ref['omega_XH'], rel_tol=0, abs_tol=tol):
                matched_fields += 1
            if math.isclose(item.get('omega_HAB'), ref['omega_HAB'], rel_tol=0, abs_tol=tol):
                matched_fields += 1
        except (TypeError, KeyError):
            pass

    ref_score = matched_fields / total_fields if total_fields > 0 else 0.0

    trends = step.get('structural_trends', {})
    trend_ok = True
    if trends:
        try:
            hsis_family = trends.get('HSiS_family', {})
            anion = None
            neutral = None
            cation = None
            for item in artifact:
                sp = item.get('species')
                st = item.get('state_label')
                if hsis_family and sp == hsis_family.get('anion_species') and st == hsis_family.get('anion_state'):
                    anion = item.get('omega_SiS')
                if hsis_family and sp == hsis_family.get('neutral_species') and st == hsis_family.get('neutral_state'):
                    neutral = item.get('omega_SiS')
                if hsis_family and sp == hsis_family.get('cation_species') and st == hsis_family.get('cation_state'):
                    cation = item.get('omega_SiS')
            if not (anion is not None and neutral is not None and cation is not None and anion < neutral < cation):
                trend_ok = False
        except Exception:
            trend_ok = False

        try:
            sish_family = trends.get('SiSH_family', {})
            anion = None
            neutral = None
            cation = None
            for item in artifact:
                sp = item.get('species')
                st = item.get('state_label')
                if sish_family and sp == sish_family.get('anion_species') and st == sish_family.get('anion_state'):
                    anion = item.get('omega_SiS')
                if sish_family and sp == sish_family.get('neutral_species') and st == sish_family.get('neutral_state'):
                    neutral = item.get('omega_SiS')
                if sish_family and sp == sish_family.get('cation_species') and st == sish_family.get('cation_state'):
                    cation = item.get('omega_SiS')
            if not (anion is not None and neutral is not None and cation is not None and anion < neutral < cation):
                trend_ok = False
        except Exception:
            trend_ok = False

    trend_score = 1.0 if trend_ok else 0.0
    final_score = 0.6 * ref_score + 0.4 * trend_score
    return final_score


# === block: score_2 (check id='step_rel_energies_check') ===
def score_2(artifact, step, ctx):
    expected = step.get('expected', {})
    tol = step.get('tolerance_eV', 0.05)
    if not isinstance(artifact, dict):
        return 0.0
    if not expected:
        return 0.0
    matched = 0
    for k, v in expected.items():
        val = artifact.get(k)
        if val is not None and isinstance(val, (int, float)):
            if math.isclose(val, v, rel_tol=0, abs_tol=tol):
                matched += 1
    score = matched / len(expected)
    return score


_SCORERS = {
    'step_geometry_check': score_0,
    'step_frequencies_check': score_1,
    'step_rel_energies_check': score_2,
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
