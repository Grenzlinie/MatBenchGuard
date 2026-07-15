import os
import json
import csv

# === author imports / helpers ===
import os, csv, math


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
    def load_dos(path):
        comps = []
        current_comp = None
        rows = []
        with open(path, newline='') as f:
            for line in f:
                line = line.strip()
                if line.startswith('# composition:'):
                    if current_comp is not None:
                        comps.append((current_comp, rows))
                        rows = []
                    current_comp = line.split(':', 1)[1].strip()
                elif not line or line.startswith('#'):
                    continue
                else:
                    parts = line.split('\t')
                    if len(parts) >= 3:
                        try:
                            energy = float(parts[1])
                            dos_val = float(parts[2])
                            rows.append((energy, dos_val))
                        except ValueError:
                            pass
        if current_comp is not None:
            comps.append((current_comp, rows))
        return comps

    def compute_gap(energies, dos_vals, dos_thresh=0.001, zero_tol=0.01):
        sorted_pairs = sorted(zip(energies, dos_vals), key=lambda x: x[0])
        for e, d in sorted_pairs:
            if abs(e) <= zero_tol and d > dos_thresh:
                return None, 'metal'
        vbm = None
        for e, d in sorted_pairs:
            if e < 0 and d > dos_thresh:
                vbm = max(vbm, e) if vbm is not None else e
        cbm = None
        for e, d in sorted_pairs:
            if e > 0 and d > dos_thresh:
                cbm = min(cbm, e) if cbm is not None else e
        if vbm is not None and cbm is not None:
            gap = cbm - vbm
            return gap, 'insulator'
        return None, 'unknown'

    dos_path = os.path.join(outputs_dir, 'total_dos_all_compositions.dat')
    computed = {}
    all_comps = load_dos(dos_path)
    for comp, rows in all_comps:
        energies, dos_values = zip(*rows) if rows else ([], [])
        gap, typ = compute_gap(energies, dos_values, dos_thresh=0.001, zero_tol=0.01)
        computed[comp.strip()] = {'gap': gap, 'type': typ}
    return {'computed': computed}


# === block: score_0 (check id='step_03_dos_recompute') ===
def score_0(artifact, step, ctx):
    computed = ctx['computed']
    gold = step['gold_table']
    total = 0.0
    n = 0
    for comp_key, info in gold.items():
        n += 1
        c = computed.get(comp_key.strip())
        if c is None:
            continue
        if info.get('type') == 'metal':
            if c['type'] == 'metal':
                total += 1.0
        else:
            if c['type'] == 'insulator':
                err = abs(c['gap'] - info['gap'])
                tol = info.get('tolerance', 0.3)
                if err <= tol:
                    total += 1.0
                else:
                    score_comp = max(0.0, 1.0 - (err - tol) / tol)
                    total += score_comp
    score = total / max(n, 1)
    return score


# === block: score_1 (check id='step_04_summary_consistency') ===
def score_1(artifact, step, ctx):
    computed = ctx['computed']
    rows = artifact
    total = 0
    n = 0
    for row in rows:
        comp = row['composition'].strip()
        bg = row['band_gap'].strip()
        c = computed.get(comp)
        if c is None:
            n += 1
            continue
        n += 1
        if c['type'] == 'metal':
            if bg.lower() == 'metallic':
                total += 1
        else:
            try:
                val = float(bg)
            except ValueError:
                pass
            else:
                gap_tol = step.get('gap_tolerance', 0.05)
                if abs(val - c['gap']) <= gap_tol:
                    total += 1
    score = total / max(n, 1)
    return score


_SCORERS = {
    'step_03_dos_recompute': score_0,
    'step_04_summary_consistency': score_1,
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
