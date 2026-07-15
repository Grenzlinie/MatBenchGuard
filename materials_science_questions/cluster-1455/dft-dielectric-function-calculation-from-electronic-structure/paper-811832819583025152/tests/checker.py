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
    gold = spec['steps'][0]['gold']
    ctx = {
        'gold_compositions': gold['compositions'],
        'tol_bandgap': gold['tolerances']['band_gap'],
        'tol_dielectric_rel': gold['tolerances']['dielectric_constant_relative'],
        'tol_cp': gold['tolerances']['critical_point_energy']
    }
    return ctx


# === block: score_0 (check id='check_dft_results') ===
def score_0(artifact, step, ctx):
    import math

    if not isinstance(artifact, dict) or 'compositions' not in artifact:
        return 0.0

    agent_comps = artifact['compositions']
    gold_comps = ctx['gold_compositions']
    tol_bg = ctx['tol_bandgap']
    tol_dc_rel = ctx['tol_dielectric_rel']
    tol_cp = ctx['tol_cp']

    # Paper-reported band-gap fields per (name, phase):
    # Only score a field if the paper explicitly reports that type of gap.
    PAPER_FIELDS = {
        ('GeTe', 'stable'):               ['indirect', 'direct'],
        ('Ge2Sb2Te5', 'stable'):          ['indirect'],
        ('Ge2Sb2Te5', 'metastable'):      ['indirect'],
        ('Ge1Sb2Te4', 'stable'):          ['indirect', 'direct'],
        ('Ge1Sb2Te4', 'metastable'):      ['indirect'],
        ('Ge1Sb4Te7', 'stable'):          ['direct'],
        ('Ge1Sb4Te7', 'metastable'):      ['indirect'],
        ('Sb2Te3', 'stable'):             ['direct'],
    }

    def find_agent(name, phase):
        for c in agent_comps:
            if c.get('name') == name and c.get('phase') == phase:
                return c
        return None

    pair_scores = []
    for g in gold_comps:
        a = find_agent(g['name'], g['phase'])
        if a is None:
            pair_scores.append(0.0)
            continue
        ok = []
        # Decide which band-gap fields are scored.
        fields_to_score = PAPER_FIELDS.get((g['name'], g['phase']), [])
        if 'indirect' in fields_to_score:
            if 'band_gap_indirect' in a and isinstance(a['band_gap_indirect'], (int, float)):
                ok.append(1.0 if abs(a['band_gap_indirect'] - g['band_gap_indirect']) <= tol_bg else 0.0)
            else:
                ok.append(0.0)
        if 'direct' in fields_to_score:
            if 'band_gap_direct_min' in a and isinstance(a['band_gap_direct_min'], (int, float)):
                ok.append(1.0 if abs(a['band_gap_direct_min'] - g['band_gap_direct_min']) <= tol_bg else 0.0)
            else:
                ok.append(0.0)
        # static dielectric constant (always scored)
        if 'static_dielectric_constant' in a and isinstance(a['static_dielectric_constant'], (int, float)):
            rel_err = abs(a['static_dielectric_constant'] - g['static_dielectric_constant']) / abs(g['static_dielectric_constant']) if g['static_dielectric_constant'] != 0 else abs(a['static_dielectric_constant'] - g['static_dielectric_constant'])
            ok.append(1.0 if rel_err <= tol_dc_rel else 0.0)
        else:
            ok.append(0.0)
        # critical-point energies (only scored for GeTe)
        gold_cp = g.get('critical_point_energies', [])
        if gold_cp:
            agent_cp = a.get('critical_point_energies', [])
            if isinstance(agent_cp, list) and len(agent_cp) == len(gold_cp):
                sorted_agent = sorted(agent_cp)
                sorted_gold = sorted(gold_cp)
                matches = sum(1 for va, vg in zip(sorted_agent, sorted_gold) if abs(va - vg) <= tol_cp)
                cp_score = matches / len(sorted_gold)
            else:
                cp_score = 0.0
            ok.append(cp_score)
        pair_score = sum(ok) / len(ok) if ok else 0.0
        pair_scores.append(pair_score)

    if not pair_scores:
        return 0.0
    return sum(pair_scores) / len(pair_scores)


_SCORERS = {
    'check_dft_results': score_0,
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
