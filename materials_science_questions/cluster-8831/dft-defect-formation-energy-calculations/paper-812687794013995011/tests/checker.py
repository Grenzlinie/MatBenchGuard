import os
import json
import csv

# === author imports / helpers ===
import os, json, csv, math


def compute_avg_vn(csv_path):
    if not os.path.exists(csv_path):
        return None, None
    rows = []
    with open(csv_path, newline='') as f:
        reader = csv.DictReader(f)
        for r in reader:
            if r.get('vacancy_type', '').strip() == 'V_N':
                rows.append({'structure': r['structure'].strip(),
                             'formation_energy': float(r['formation_energy'])})
    if not rows:
        return None, None
    znon_vals = [r['formation_energy'] for r in rows if r['structure'] == 'ZnON']
    si_vals = [r['formation_energy'] for r in rows if r['structure'] == 'Si_doped']
    zn_avg = sum(znon_vals) / len(znon_vals) if znon_vals else None
    si_avg = sum(si_vals) / len(si_vals) if si_vals else None
    return zn_avg, si_avg


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


# === block: score_0 (check id='formation_energies_csv') ===
def score_0(artifact, step, ctx):
    zn_avg, si_avg = compute_avg_vn(os.path.join('/app/outputs', 'formation_energies.csv'))
    if zn_avg is None or si_avg is None:
        return 0.0
    # sub-scores
    c1 = 1.0 if zn_avg <= -0.1 else 0.0   # ZnON V_N should be negative or near zero
    c2 = 1.0 if si_avg >= 0.5 else 0.0    # Si-doped V_N should be significantly positive
    c3 = 1.0 if si_avg > zn_avg else 0.0   # trend: Si-doped higher than ZnON
    return 0.4 * c1 + 0.4 * c2 + 0.2 * c3


# === block: score_1 (check id='summary_json') ===
def score_1(artifact, step, ctx):
    import json
    summary_path = os.path.join('/app/outputs', 'summary.json')
    if not os.path.exists(summary_path):
        return 0.0
    with open(summary_path) as f:
        summary = json.load(f)
    zn_summary = summary.get('ZnON', {})
    si_summary = summary.get('Si_doped', {})
    zn_avg_sum = zn_summary.get('E_form_V_N_avg')
    si_avg_sum = si_summary.get('E_form_V_N_avg')
    zn_bg = zn_summary.get('band_gap')
    si_bg = si_summary.get('band_gap')
    if None in (zn_avg_sum, si_avg_sum, zn_bg, si_bg):
        return 0.0
    # recompute averages from CSV
    zn_avg_csv, si_avg_csv = compute_avg_vn(os.path.join('/app/outputs', 'formation_energies.csv'))
    if zn_avg_csv is None or si_avg_csv is None:
        return 0.0
    # consistency of avg V_N with CSV
    c1 = 1.0 if abs(zn_avg_sum - zn_avg_csv) <= 0.01 else 0.0
    c2 = 1.0 if abs(si_avg_sum - si_avg_csv) <= 0.01 else 0.0
    # band gap within reasonable range
    c3 = 1.0 if 1.8 <= zn_bg <= 2.3 else 0.0
    c4 = 1.0 if 1.9 <= si_bg <= 2.4 else 0.0
    # band gap increase
    c5 = 1.0 if (si_bg - zn_bg) >= 0.05 else 0.0
    return 0.2 * c1 + 0.2 * c2 + 0.2 * c3 + 0.2 * c4 + 0.2 * c5


_SCORERS = {
    'formation_energies_csv': score_0,
    'summary_json': score_1,
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
