import os
import json
import csv

# === author imports / helpers ===
import json, os


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
        ctx = {}
        try:
            with open(os.path.join(outputs_dir, 'electrostatic_contributions.json')) as f:
                elec = json.load(f)
            ctx['electrostatic'] = elec
        except Exception:
            ctx['electrostatic'] = None
        try:
            with open(os.path.join(outputs_dir, 'exchange_contributions.json')) as f:
                exch = json.load(f)
            ctx['exchange'] = exch
        except Exception:
            ctx['exchange'] = None
        conv = spec.get('conversion', {})
        e_sq = conv.get('e_sq', 2.307077e-19)
        lattice = conv.get('lattice_constants', {})
        structures = conv.get('crystal_structure', {})
        n_atoms_map = {'fcc': 4, 'bcc': 2}
        factors = {}
        for metal, delta in lattice.items():
            struct = structures.get(metal, 'bcc')
            n = n_atoms_map.get(struct, 2)
            factor = (e_sq * n) / (2 * (delta ** 4) * 1e11)
            factors[metal] = factor
        ctx['factors'] = factors
        return ctx


# === block: score_0 (check id='electrostatic_check') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        try:
            fcc = artifact['fcc']
            bcc = artifact['bcc']
        except (KeyError, TypeError):
            return 0.0
        target = step['target']
        tol = step['tolerance_abs']
        diffs = []
        for struct, keys in [('fcc', ['A_l', '2B_l']), ('bcc', ['A_l', '2B_l'])]:
            data = fcc if struct == 'fcc' else bcc
            for k in keys:
                val = data.get(k)
                if val is None:
                    return 0.0
                diff = abs(val - target[struct][k])
                score = max(0.0, 1.0 - diff / (5.0 * tol))
                diffs.append(score)
        if not diffs:
            return 0.0
        return sum(diffs) / len(diffs)


# === block: score_1 (check id='exchange_check') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        target = step['target']
        tol = step['tolerance_abs']
        if not isinstance(artifact, list):
            return 0.0
        scores = []
        for entry in artifact:
            metal = entry.get('metal')
            if not metal or metal not in target:
                return 0.0
            for k in ['A_I', '2B_I']:
                val = entry.get(k)
                if val is None:
                    return 0.0
                diff = abs(val - target[metal][k])
                score = max(0.0, 1.0 - diff / (5.0 * tol))
                scores.append(score)
        if not scores:
            return 0.0
        return sum(scores) / len(scores)


# === block: score_2 (check id='total_elastic_check') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        target = step['target']
        tol_rel = step['tolerance_rel']
        consistency_tol_rel = step['consistency_tolerance_rel']
        gold_scores = []
        for entry in artifact:
            metal = entry.get('metal')
            if not metal or metal not in target:
                return 0.0
            for k in ['A', '2B', 'c11', 'c12']:
                val = entry.get(k)
                if val is None:
                    return 0.0
                ref = target[metal][k]
                if abs(ref) < 1e-9:
                    score = 1.0 if val == ref else max(0.0, 1.0 - abs(val - ref))
                else:
                    rel_diff = abs(val - ref) / abs(ref)
                    score = max(0.0, 1.0 - rel_diff / tol_rel)
                gold_scores.append(score)
        gold_score = sum(gold_scores) / len(gold_scores) if gold_scores else 0.0
        elec = ctx.get('electrostatic')
        exch = ctx.get('exchange')
        factors = ctx.get('factors')
        if not elec or not exch or not factors:
            consistency_score = 0.5
        else:
            consistency_scores = []
            for entry in artifact:
                metal = entry['metal']
                factor = factors.get(metal)
                if factor is None:
                    continue
                str_type = 'fcc' if metal == 'Cu' else 'bcc'
                A_l = elec[str_type]['A_l']
                B2_l = elec[str_type]['2B_l']
                exch_entry = next((e for e in exch if e['metal'] == metal), None)
                if exch_entry is None:
                    continue
                expected_A = A_l * factor + exch_entry['A_I']
                expected_2B = B2_l * factor + exch_entry['2B_I']
                for key, expected in [('A', expected_A), ('2B', expected_2B)]:
                    val = entry.get(key)
                    if val is None:
                        continue
                    rel_diff = abs(val - expected) / max(1e-9, abs(expected))
                    score = max(0.0, 1.0 - rel_diff / consistency_tol_rel)
                    consistency_scores.append(score)
            consistency_score = sum(consistency_scores) / len(consistency_scores) if consistency_scores else 0.0
        return 0.5 * gold_score + 0.5 * consistency_score


# === block: score_3 (check id='debye_check') ===
def score_3(artifact, step, ctx):
    def score(artifact, step, ctx):
        target = step['target']
        tol = step['tolerance_abs']
        scores = []
        for entry in artifact:
            metal = entry.get('metal')
            if metal not in target:
                return 0.0
            val = entry.get('Theta')
            if val is None:
                return 0.0
            diff = abs(val - target[metal])
            score = max(0.0, 1.0 - diff / tol)
            scores.append(score)
        if not scores:
            return 0.0
        return sum(scores) / len(scores)


_SCORERS = {
    'electrostatic_check': score_0,
    'exchange_check': score_1,
    'total_elastic_check': score_2,
    'debye_check': score_3,
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
