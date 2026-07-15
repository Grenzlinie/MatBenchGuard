import os
import json
import csv

# === author imports / helpers ===
import os
import re
from collections import OrderedDict


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


# === block: score_0 (check id='offretite_geometry') ===
def score_0(artifact, step, ctx):
    if artifact is None:
        return 0.0
    gold = step.get('gold', {})
    tols = step.get('tolerances', {})
    if not gold:
        return 0.0
    lines = artifact.strip().split('\n')
    parsed = {}
    for line in lines:
        if '=' not in line and ' = ' not in line:
            continue
        parts = line.split('=')
        if len(parts) >= 2:
            key = parts[0].strip()
            val_str = parts[1].strip()
            try:
                val = float(val_str)
            except ValueError:
                continue
            parsed[key] = val
    correct = 0
    total = len(gold)
    if total == 0:
        return 0.0
    for key, expected in gold.items():
        actual = parsed.get(key)
        if actual is None:
            continue
        if key.startswith('E_tot') or 'energy' in key.lower():
            tol = tols.get('energy_abs', 0.01)
        elif any(key.startswith(p) for p in ('O1T1','O2T1','O3T1','O4T1','T1O3','T2O6','O4T2','O5T2','O6T2','T1O','T2O')):
            # angle keys contain 'O' followed by 'T' pattern; a bit rough, use a check for 'angle' in description but we just check key pattern
            if any(kw in key for kw in ('T1O','T2O')) and not key.startswith('T1O1') and not key.startswith('T1O2') and not key.startswith('T1O3') and not key.startswith('T1O4') and not key.startswith('T2O4') and not key.startswith('T2O5') and not key.startswith('T2O6') and not key.startswith('T2O7'):
                # likely an angle like T1O3T1
                tol = tols.get('angle_abs', 2.0)
            elif key.startswith('O'):
                tol = tols.get('angle_abs', 2.0)
            else:
                tol = tols.get('length_abs', 0.02)
        elif key.startswith('T'):
            # bond lengths
            tol = tols.get('length_abs', 0.02)
        else:
            tol = 0.01  # fallback
        if abs(actual - expected) <= tol:
            correct += 1
    score = correct / total
    return score


# === block: score_1 (check id='al_substituted_geometries') ===
def score_1(artifact, step, ctx):
    if artifact is None:
        return 0.0
    gold = step.get('gold', {})
    tols = step.get('tolerances', {})
    if not gold:
        return 0.0
    # Parse blocks
    blocks = re.split(r'\n(?=Al\(T)', artifact)
    parsed = {}
    for block in blocks:
        if not block.strip():
            continue
        header_match = re.match(r'Al\((T[12])\)', block.strip())
        if not header_match:
            continue
        site_type = header_match.group(1)
        site_key = f'Al({site_type})'
        vals = {}
        for line in block.split('\n'):
            line = line.strip()
            if '=' not in line:
                continue
            k, v = line.split('=', 1)
            k = k.strip()
            try:
                v_float = float(v.strip())
            except ValueError:
                continue
            vals[k] = v_float
        parsed[site_key] = vals
    correct = 0
    total = 0
    for site_key, site_gold in gold.items():
        actual = parsed.get(site_key, {})
        if not actual:
            continue
        for param, expected in site_gold.items():
            actual_val = actual.get(param)
            if actual_val is None:
                continue
            if param.startswith('E_tot'):
                tol = tols.get('energy_abs', 0.01)
            elif param.startswith('d'):
                tol = tols.get('length_abs', 0.02)
            elif param.startswith('α'):
                tol = tols.get('angle_abs', 2.0)
            else:
                tol = 0.01
            total += 1
            if abs(actual_val - expected) <= tol:
                correct += 1
    if total == 0:
        return 0.0
    return correct / total


# === block: score_2 (check id='protonated_geometries') ===
def score_2(artifact, step, ctx):
    if artifact is None:
        return 0.0
    gold = step.get('gold', {})
    tols = step.get('tolerances', {})
    if not gold:
        return 0.0
    blocks = re.split(r'\n(?=[Tt]\dO)', artifact)
    parsed = {}
    for block in blocks:
        if not block.strip():
            continue
        lines = block.strip().split('\n')
        header = lines[0].strip()
        if not re.match(r'T[12]O[1-7]H', header):
            continue
        site = header
        vals = {}
        for line in lines[1:]:
            if '=' not in line:
                continue
            k, v = line.split('=', 1)
            k = k.strip()
            try:
                v_float = float(v.strip())
            except ValueError:
                continue
            vals[k] = v_float
        parsed[site] = vals
    correct = 0
    total = 0
    for site, site_gold in gold.items():
        actual = parsed.get(site, {})
        if not actual:
            continue
        for param, expected in site_gold.items():
            actual_val = actual.get(param)
            if actual_val is None:
                continue
            if param.startswith('E_tot'):
                tol = tols.get('energy_abs', 0.01)
            elif param.startswith('d'):
                tol = tols.get('length_abs', 0.02)
            elif param.startswith('α'):
                tol = tols.get('angle_abs', 2.0)
            else:
                tol = 0.01
            total += 1
            if abs(actual_val - expected) <= tol:
                correct += 1
    if total == 0:
        return 0.0
    return correct / total


# === block: score_3 (check id='protonated_energies') ===
def score_3(artifact, step, ctx):
    if artifact is None:
        return 0.0
    gold_data = step.get('gold', {})
    tols = step.get('tolerances', {})
    trend_check = step.get('trend_check', None)
    if not gold_data:
        return 0.0

    lines = artifact.strip().split('\n')
    parsed = {}
    for line in lines:
        parts = line.split()
        if len(parts) != 4:
            continue
        site = parts[0]
        try:
            total_e = float(parts[1])
            pa = float(parts[2])
            sub_e = float(parts[3])
        except ValueError:
            continue
        parsed[site] = {'total_energy': total_e, 'proton_affinity': pa, 'substitution_energy': sub_e}

    correct = 0
    total = 0
    for site, ref in gold_data.items():
        actual = parsed.get(site)
        if actual is None:
            continue
        total += 3
        if abs(actual['total_energy'] - ref['total_energy']) <= tols.get('total_energy_abs', 0.01):
            correct += 1
        if abs(actual['proton_affinity'] - ref['proton_affinity']) <= tols.get('derived_energy_abs', 2.0):
            correct += 1
        if abs(actual['substitution_energy'] - ref['substitution_energy']) <= tols.get('derived_energy_abs', 2.0):
            correct += 1

    numeric_score = correct / total if total > 0 else 0.0

    # Trend/ordering check
    if trend_check and parsed:
        sub_order = trend_check.get('substitution_energy_ordering')
        pa_order = trend_check.get('proton_affinity_ordering')
        trend_score = 0.0
        # Check if agent's ordering matches exactly
        if sub_order:
            agent_sub = sorted(parsed.items(), key=lambda x: x[1]['substitution_energy'], reverse=True)
            agent_sub_order = [s for s, _ in agent_sub]
            if agent_sub_order == sub_order:
                trend_score += 0.5
        if pa_order:
            agent_pa = sorted(parsed.items(), key=lambda x: x[1]['proton_affinity'])
            agent_pa_order = [s for s, _ in agent_pa]
            if agent_pa_order == pa_order:
                trend_score += 0.5
        final = numeric_score * 0.8 + trend_score * 0.2
        return final
    else:
        return numeric_score


# === block: score_4 (check id='al_substitution_energies') ===
def score_4(artifact, step, ctx):
    if artifact is None:
        return 0.0
    gold = step.get('gold', {})
    tols = step.get('tolerances', {})
    if not gold:
        return 0.0
    lines = artifact.strip().split('\n')
    parsed = {}
    for line in lines:
        parts = line.split()
        if len(parts) != 3:
            continue
        site = parts[0]
        try:
            total_e = float(parts[1])
            rel_e = float(parts[2])
        except ValueError:
            continue
        parsed[site] = {'total_energy': total_e, 'relative_substitution_energy': rel_e}
    correct = 0
    total = 0
    for site, ref in gold.items():
        actual = parsed.get(site)
        if actual is None:
            continue
        total += 2
        if abs(actual['total_energy'] - ref['total_energy']) <= tols.get('total_energy_abs', 0.01):
            correct += 1
        if abs(actual['relative_substitution_energy'] - ref['relative_substitution_energy']) <= tols.get('relative_energy_abs', 1.0):
            correct += 1
    if total == 0:
        return 0.0
    return correct / total


_SCORERS = {
    'offretite_geometry': score_0,
    'al_substituted_geometries': score_1,
    'protonated_geometries': score_2,
    'protonated_energies': score_3,
    'al_substitution_energies': score_4,
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
