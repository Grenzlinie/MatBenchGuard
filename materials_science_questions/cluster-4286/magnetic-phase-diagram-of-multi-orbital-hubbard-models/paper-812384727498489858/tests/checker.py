import os
import json
import csv

# === author imports / helpers ===
import csv
import os
import math


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


# === block: score_0 (check id='energy-curves') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        data = artifact
        groups = {}
        for row in data:
            donor = row['donor_spin'].strip()
            jf = float(row['j_f'])
            groups.setdefault((donor, jf), []).append(row)
        total_groups = 0
        passed = 0
        for donor in ['none', '-1/2']:
            for jf in [0.2, 0.3, 0.5]:
                key = (donor, jf)
                if key not in groups:
                    continue
                total_groups += 1
                rows = sorted(groups[key], key=lambda r: float(r['srz_expectation']))
                energies = [float(r['total_energy']) for r in rows]
                if len(energies) == 6 and all(energies[i+1] <= energies[i] for i in range(5)):
                    passed += 1
        for donor in ['1/2']:
            for jf in [0.2, 0.3, 0.5]:
                key = (donor, jf)
                if key not in groups:
                    continue
                total_groups += 1
                rows = sorted(groups[key], key=lambda r: float(r['srz_expectation']))
                energies = [float(r['total_energy']) for r in rows]
                if len(energies) != 6:
                    continue
                if jf == 0.2:
                    srz_list = [float(r['srz_expectation']) for r in rows]
                    try:
                        idx02 = srz_list.index(0.2)
                    except ValueError:
                        continue
                    if energies[idx02] < energies[0] and energies[idx02] < energies[5]:
                        passed += 1
                else:
                    if all(energies[i+1] <= energies[i] for i in range(5)):
                        passed += 1
        if total_groups == 0:
            return 0.0
        return passed / total_groups


# === block: score_1 (check id='polaron-profile') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        min_std_ratio = float(step.get('params', {}).get('min_std_ratio', 0.05))
        data = artifact
        groups = {}
        for row in data:
            ds = row['donor_spin'].strip()
            if float(row['j_f']) != 0.3:
                continue
            groups.setdefault(ds, []).append(row)
        if len(groups) != 2:
            return 0.0
        passed = 0
        for ds, rows in groups.items():
            rows_sorted = sorted(rows, key=lambda r: int(r['site_index']))
            vals = [float(r['spin_density']) for r in rows_sorted]
            abs_vals = [abs(v) for v in vals]
            n = len(abs_vals)
            if n == 0:
                continue
            mean_abs = sum(abs_vals) / n
            if mean_abs == 0:
                continue
            std_abs = math.sqrt(sum((x - mean_abs) ** 2 for x in abs_vals) / n)
            if std_abs > min_std_ratio * mean_abs:
                passed += 1
        return passed / 2


# === block: score_2 (check id='energy-summary') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        summary = artifact
        energy_path = '/app/outputs/energy_curves.csv'
        if not os.path.exists(energy_path):
            return 0.0
        with open(energy_path, newline='') as f:
            reader = csv.DictReader(f)
            energy_data = list(reader)
        egroup = {}
        for row in energy_data:
            donor = row['donor_spin'].strip()
            jf = float(row['j_f'])
            key = (donor, jf)
            egroup.setdefault(key, []).append(row)
        computed = {}
        for key, rows in egroup.items():
            srz_to_energy = {}
            for r in rows:
                srz = float(r['srz_expectation'])
                srz_to_energy[srz] = float(r['total_energy'])
            if 0.0 in srz_to_energy and 0.5 in srz_to_energy:
                computed[key] = srz_to_energy[0.0] - srz_to_energy[0.5]
        relation_tol = float(step.get('params', {}).get('relation_tol', 0.001))
        value_tol = float(step.get('params', {}).get('value_tol', 1e-9))
        sum_by_jf = {}
        for row in summary:
            donor = row['donor_spin'].strip()
            jf = float(row['j_f'])
            key = (donor, jf)
            if key in computed and abs(float(row['delta_E2']) - computed[key]) <= value_tol:
                sum_by_jf.setdefault(jf, {'ok': True, 'rows': []})
                sum_by_jf[jf]['rows'].append(row)
            else:
                sum_by_jf.setdefault(jf, {'ok': False})
        jfs = [0.2, 0.3, 0.5]
        passed = 0
        for jf in jfs:
            if jf not in sum_by_jf or not sum_by_jf[jf].get('ok'):
                continue
            rows = sum_by_jf[jf]['rows']
            if len(rows) < 2:  # need -1/2 and +1/2
                continue
            row_minus = None
            row_plus = None
            for r in rows:
                ds = r['donor_spin'].strip()
                if ds == '-1/2':
                    row_minus = r
                elif ds == '1/2':
                    row_plus = r
            if row_minus is None or row_plus is None:
                continue
            delta_E2_minus = float(row_minus['delta_E2'])
            delta_E2_plus = float(row_plus['delta_E2'])
            delta_E1 = float(row_minus.get('delta_E1', 0))
            if abs(delta_E2_minus - delta_E2_plus - delta_E1) <= relation_tol:
                passed += 1
        return passed / len(jfs)


_SCORERS = {
    'energy-curves': score_0,
    'polaron-profile': score_1,
    'energy-summary': score_2,
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
