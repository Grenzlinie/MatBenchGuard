import os
import json
import csv

# === author imports / helpers ===
import math
from collections import defaultdict


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
    gold = spec.get('hidden_gold', {})
    exp_refs = gold.get('experimental_references', {})
    return {'exp_refs': exp_refs}


# === block: score_0 (check id='ccsd_extrapolated') ===
def score_0(artifact, step, ctx):
    rows = artifact  # list of dicts with keys molecule, property, extrapolated_value, method
    if not rows:
        return 0.0
    method = step.get('method', '')
    expected = step.get('expected_molecule_properties', {})
    gold_mad = step['gold_total_mad_kcal_mol']
    margin = step['margin_kcal_mol']
    max_decay = step['max_decay_kcal_mol']
    exp_refs = ctx['exp_refs']

    # filter rows for this method
    method_rows = [r for r in rows if r.get('method', '').strip() == method]
    if len(method_rows) != 40:
        return 0.0

    # build lookup: key (molecule, property) -> extrapolated_value
    ext_val = {}
    for r in method_rows:
        mol = r['molecule'].strip()
        prop = r['property'].strip()
        try:
            val = float(r['extrapolated_value'])
        except (ValueError, KeyError):
            return 0.0
        ext_val[(mol, prop)] = val

    # compute per-property MAD and total absolute deviation sum
    total_abs_diff = 0.0
    total_count = 0
    for prop in ['AE', 'IE', 'EA', 'PA']:
        expected_mols = expected.get(prop, [])
        prop_refs = exp_refs.get(prop, {})
        for mol in expected_mols:
            exp = prop_refs.get(mol)
            if exp is None:
                return 0.0  # missing reference
            key = (mol, prop)
            if key not in ext_val:
                return 0.0
            calc = ext_val[key]
            if prop == 'AE':
                diff = abs(calc - exp)  # already kcal/mol
            else:
                diff = abs(calc - exp) * 23.0605  # eV to kcal/mol
            total_abs_diff += diff
            total_count += 1
    if total_count != 40:
        return 0.0

    total_mad = total_abs_diff / total_count

    # score using threshold_or_better: lower is better; full credit if <= gold + margin, linear decay to max_decay
    threshold = gold_mad + margin
    if total_mad <= threshold:
        return 1.0
    else:
        if total_mad >= max_decay:
            return 0.0
        return max(0.0, (max_decay - total_mad) / (max_decay - threshold))


# === block: score_1 (check id='b3lyp_extrapolated') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    method = step.get('method', '')
    expected = step.get('expected_molecule_properties', {})
    gold_mad = step['gold_total_mad_kcal_mol']
    margin = step['margin_kcal_mol']
    max_decay = step['max_decay_kcal_mol']
    exp_refs = ctx['exp_refs']

    method_rows = [r for r in rows if r.get('method', '').strip() == method]
    if len(method_rows) != 40:
        return 0.0

    ext_val = {}
    for r in method_rows:
        mol = r['molecule'].strip()
        prop = r['property'].strip()
        try:
            val = float(r['extrapolated_value'])
        except (ValueError, KeyError):
            return 0.0
        ext_val[(mol, prop)] = val

    total_abs_diff = 0.0
    total_count = 0
    for prop in ['AE', 'IE', 'EA', 'PA']:
        expected_mols = expected.get(prop, [])
        prop_refs = exp_refs.get(prop, {})
        for mol in expected_mols:
            exp = prop_refs.get(mol)
            if exp is None:
                return 0.0
            key = (mol, prop)
            if key not in ext_val:
                return 0.0
            calc = ext_val[key]
            if prop == 'AE':
                diff = abs(calc - exp)
            else:
                diff = abs(calc - exp) * 23.0605
            total_abs_diff += diff
            total_count += 1
    if total_count != 40:
        return 0.0

    total_mad = total_abs_diff / total_count

    threshold = gold_mad + margin
    if total_mad <= threshold:
        return 1.0
    else:
        if total_mad >= max_decay:
            return 0.0
        return max(0.0, (max_decay - total_mad) / (max_decay - threshold))


# === block: score_2 (check id='metrics_summary') ===
def score_2(artifact, step, ctx):
    if not isinstance(artifact, list):
        return 0.0

    # recompute per-property and total MAD for both methods from the CSV files
    import os, csv

    paths = {
        'CCSD(T)': '/app/outputs/extrapolated_values_ccsd.csv',
        'B3LYP': '/app/outputs/extrapolated_values_b3lyp.csv'
    }
    expected_mols = {
        'AE': ["GeH4","AsH","AsH2","AsH3","SeH","SeH2","HBr","GeO","GeS2","As2","BrCl","BrF","BrO","BBr","Br2","CH3Br","GaCl","KrF2","NaBr"],
        'IE': ["Ga","Ge","As","Se","Br","Kr","AsH","AsH2","SeH","SeH2","HBr","BrF","HOBr","Br2","NaBr"],
        'EA': ["Ge","Br","SeH","BrO"],
        'PA': ["HBr","CH3Br"]
    }
    exp_refs = ctx['exp_refs']

    def compute_mad(method):
        path = paths[method]
        if not os.path.exists(path):
            return None
        rows = []
        with open(path, newline='') as f:
            reader = csv.DictReader(f)
            for r in reader:
                if r.get('method','').strip() == method:
                    rows.append(r)
        if len(rows) != 40:
            return None
        ext_val = {}
        for r in rows:
            mol = r['molecule'].strip()
            prop = r['property'].strip()
            try:
                val = float(r['extrapolated_value'])
            except (ValueError, KeyError):
                return None
            ext_val[(mol, prop)] = val
        per_mad = {}
        total_abs = 0.0
        total_cnt = 0
        for prop in ['AE','IE','EA','PA']:
            emols = expected_mols[prop]
            p_refs = exp_refs.get(prop, {})
            s = 0.0
            cnt = 0
            for mol in emols:
                exp = p_refs.get(mol)
                if exp is None:
                    return None
                key = (mol, prop)
                if key not in ext_val:
                    return None
                calc = ext_val[key]
                if prop == 'AE':
                    diff = abs(calc - exp)
                else:
                    diff = abs(calc - exp) * 23.0605
                s += diff
                cnt += 1
            total_abs += s
            total_cnt += cnt
            per_mad[prop] = s / cnt if cnt else 0.0
        total_mad = total_abs / total_cnt if total_cnt else 0.0
        return {'total_mad': total_mad, 'per_mad': per_mad}

    ccsd = compute_mad('CCSD(T)')
    b3lyp = compute_mad('B3LYP')
    if ccsd is None or b3lyp is None:
        return 0.0

    tol = step.get('tolerance_mad_kcal_mol', 0.1)
    score = 0.0
    for entry in artifact:
        if not isinstance(entry, dict):
            continue
        meth = entry.get('method', '')
        if meth not in ('CCSD(T)', 'B3LYP'):
            continue
        ref = ccsd if meth == 'CCSD(T)' else b3lyp
        reported_total = entry.get('total_mad_kcal_mol')
        if reported_total is None:
            continue
        try:
            reported_total = float(reported_total)
        except (ValueError, TypeError):
            continue
        if abs(reported_total - ref['total_mad']) <= tol:
            score += 0.5  # each method worth 0.5
        # option: also check per-property MAD if present
    # return score clamped to 1.0
    return min(score, 1.0)


_SCORERS = {
    'ccsd_extrapolated': score_0,
    'b3lyp_extrapolated': score_1,
    'metrics_summary': score_2,
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
