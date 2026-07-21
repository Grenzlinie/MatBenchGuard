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
    with open("/tests/gold.json") as f:
        gold_data = json.load(f)
    ctx = {}
    ctx["fe_gold"] = gold_data["formation_energies"]["gold_relative_energies"]
    ctx["fe_tol"] = gold_data["formation_energies"]["tolerance_eV"]
    ctx["bs_gold"] = gold_data["band_structure_summary"]
    return ctx


# === block: score_0 (check id='formation_energies') ===
def score_0(artifact, step, ctx):
    # Load CSV artifact; assume format as per contract
    fe_gold = ctx['fe_gold']  # dict: e.g. {'3Au_1Al': 0.73, ...}
    tol = ctx['fe_tol']
    # artifact is list of dicts with 'composition' and 'relative_energy_eV'
    energies = {}
    for row in artifact:
        comp = row.get('composition', '').strip()
        try:
            val = float(row['relative_energy_eV'])
        except (KeyError, ValueError):
            return 0.0
        energies[comp] = val

    # The baseline corresponds to the reference composition; not scored.
    scored = 0
    count = 0
    for comp, gold in fe_gold.items():
        if comp in energies:
            count += 1
            if abs(energies[comp] - gold) <= tol:
                scored += 1
    if count == 0:
        return 0.0
    return scored / count


# === block: score_1 (check id='band_structure_summary') ===
def score_1(artifact, step, ctx):
    # artifact is the json object
    bs_gold = ctx['bs_gold']
    sub = bs_gold['sub_weights']
    metallic = sub['metallic'] * (1.0 if artifact.get('metallic') == bs_gold['gold_metallic'] else 0.0)

    # band_shift_trend check
    trend = artifact.get('band_shift_trend', '').lower()
    phrases = bs_gold.get('band_shift_expected_phrases', [])
    trend_score = 0.0
    if phrases:
        matches = sum(1 for p in phrases if p in trend)
        trend_score = matches / len(phrases)
    else:
        trend_score = 1.0  # no phrases specified -> pass
    trend_contrib = sub['band_shift_trend'] * trend_score

    # spin_splitting numbers
    spin = artifact.get('spin_splitting', {})
    if not isinstance(spin, dict):
        spin = {}
    gold_spin = bs_gold['gold_spin_splitting']
    tols = bs_gold['tolerances']
    dk_tol = tols['delta_k_parallel']
    de_tol = tols['delta_E_meV']

    dk = float(spin.get('delta_k_parallel', 0.0))
    dE11 = float(spin.get('delta_E_meV_11minus2', 0.0))
    dE211 = float(spin.get('delta_E_meV_2minus1minus1', 0.0))

    dk_score = 1.0 if abs(dk - gold_spin['delta_k_parallel']) <= dk_tol else 0.0
    dE11_score = 1.0 if abs(dE11 - gold_spin['delta_E_meV_11minus2']) <= de_tol else 0.0
    dE211_score = 1.0 if abs(dE211 - gold_spin['delta_E_meV_2minus1minus1']) <= de_tol else 0.0

    score = metallic + trend_contrib + sub['delta_k_parallel']*dk_score + sub['delta_E_11minus2']*dE11_score + sub['delta_E_2minus1minus1']*dE211_score
    return min(score, 1.0)


_SCORERS = {
    'formation_energies': score_0,
    'band_structure_summary': score_1,
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