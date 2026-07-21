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
        step = next(s for s in spec['steps'] if s['id'] == 'results_eval')
        return {'gold': step['gold']}


# === block: score_0 (check id='results_eval') ===
def score_0(artifact, step, ctx):
        gold = ctx['gold']
        structures = gold['structures']
        tol = gold['tolerances']
        art_map = {item['structure']: item for item in artifact}
        required = set(structures.keys())
        if not required.issubset(art_map.keys()):
            return 0.0
        def in_tol(val, ref, eps):
            return abs(val - ref) <= eps

        ef_tol = 2.0  # relaxed tolerance for formation energy due to code-dependent absolute values
        cells_explicit = ['Al14Ti1Ce1N16_d2.923', 'Al14Ti1Ce1N16_d5.697']
        ef_ok = all(in_tol(art_map[c]['E_f'], structures[c]['E_f'], ef_tol) for c in cells_explicit)
        lat_ok = all(in_tol(art_map[c]['a'], structures[c]['a'], tol['a_abs']) and in_tol(art_map[c]['c'], structures[c]['c'], tol['c_abs']) for c in cells_explicit)
        de_ok = all(in_tol(art_map[c]['delta_E'], structures[c]['delta_E'], tol['delta_E_abs']) for c in required)
        mm_ok = all(in_tol(art_map[c]['M_total'], structures[c]['M_total'], tol['M_total_abs']) for c in required)
        c3 = 'Al30Ti1Ce1N32_d2.923'
        val3 = art_map[c3]
        struct64_ok = val3['E_f'] < 0 and val3['a'] > 3.11 and val3['c'] > 4.98
        nn = 'Al14Ti1Ce1N16_d2.923'
        nnn = 'Al14Ti1Ce1N16_d5.697'
        ord1 = art_map[nn]['E_f'] < art_map[nnn]['E_f']
        ord2 = all(art_map[c]['delta_E'] > 0 for c in required)
        ordering_ok = ord1 and ord2

        weights = {
            'ef_explicit': 0.25,
            'lat_explicit': 0.15,
            'delta_E_all': 0.20,
            'M_total_all': 0.10,
            'struct_64': 0.10,
            'ordering': 0.20
        }
        comp = {
            'ef_explicit': 1.0 if ef_ok else 0.0,
            'lat_explicit': 1.0 if lat_ok else 0.0,
            'delta_E_all': 1.0 if de_ok else 0.0,
            'M_total_all': 1.0 if mm_ok else 0.0,
            'struct_64': 1.0 if struct64_ok else 0.0,
            'ordering': 1.0 if ordering_ok else 0.0
        }
        return sum(comp[k] * w for k, w in weights.items())


_SCORERS = {
    'results_eval': score_0,
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
