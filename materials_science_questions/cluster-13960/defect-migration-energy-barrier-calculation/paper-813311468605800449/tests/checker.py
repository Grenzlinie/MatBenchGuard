import os
import json
import csv

# === author imports / helpers ===
import csv
import re
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
    gold_freq = {}
    gold_lifetimes = {}
    gold_ea = {}
    steps = spec.get('steps', [])
    for step in steps:
        if step.get('id') == 'step_core_shell_freq':
            gold_freq = step['gold']
        elif step.get('id') == 'step_oxygen_fp_recombination_times':
            params = step['gold_params']
            temps = step['temperatures_K']
            kB = step['k_B_eV_K']
            for rank, p in params.items():
                tau0 = p['tau0']
                Ea = p['Ea']
                for T in temps:
                    gold_lifetimes[(rank, T)] = tau0 * math.exp(Ea / (kB * T))
        elif step.get('id') == 'step_oxygen_fp_arrhenius_params':
            gold_ea = step['gold_activation_energies']
            expected_order = step['expected_ordering']
            ea_tol = step['Ea_tolerance']
            ctx = {
                'gold_freq': gold_freq,
                'gold_lifetimes': gold_lifetimes,
                'gold_ea': gold_ea,
                'expected_order': expected_order,
                'ea_tol': ea_tol
            }
            return ctx
    return {}


# === block: score_0 (check id='step_core_shell_freq') ===
def score_0(artifact, step, ctx):
    text = artifact
    lines = text.strip().splitlines()
    if len(lines) < 2:
        return 0.0
    gold = ctx['gold_freq']
    tol = 0.01
    import re
    def parse_line(line):
        m = re.search(r'(\d+\.?\d*)\s*THz\s*\(\s*(\d+\.?\d*)\s*cm', line)
        if m:
            return float(m.group(1)), float(m.group(2))
        return None, None
    ok = True
    parsed = {}
    for line in lines:
        if line.startswith('O:'):
            f, w = parse_line(line)
            parsed['O'] = (f, w)
        elif line.startswith('U:'):
            f, w = parse_line(line)
            parsed['U'] = (f, w)
    if 'O' not in parsed or 'U' not in parsed:
        return 0.0
    for elem in ['O', 'U']:
        f, w = parsed[elem]
        gf = gold[elem]['freq_THz']
        gw = gold[elem]['wavenumber_cm-1']
        if f is None or w is None:
            ok = False
            break
        if abs(f - gf) / gf > tol or abs(w - gw) / gw > tol:
            ok = False
            break
    return 1.0 if ok else 0.0


# === block: score_1 (check id='step_oxygen_fp_recombination_times') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    gold_times = ctx['gold_lifetimes']
    rel_threshold = 0.20
    total = 0
    passed = 0
    for row in rows:
        rank = row.get('rank', '').strip()
        try:
            T = int(row.get('temperature_K', ''))
            mean_val = float(row.get('mean_lifetime_ps', ''))
            std_val = float(row.get('std_lifetime_ps', ''))
        except (ValueError, TypeError):
            continue
        key = (rank, T)
        if key not in gold_times:
            continue
        gold_val = gold_times[key]
        if gold_val == 0.0:
            passed += 1
            total += 1
            continue
        rel_err = abs(mean_val - gold_val) / gold_val
        if rel_err <= rel_threshold or abs(mean_val - gold_val) <= std_val:
            passed += 1
        total += 1
    if total == 0:
        return 0.0
    return passed / total


# === block: score_2 (check id='step_oxygen_fp_arrhenius_params') ===
def score_2(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    gold_ea = ctx['gold_ea']
    ea_tol = ctx['ea_tol']
    expected_order = ctx['expected_order']
    found = {}
    rank_ea = {}
    for row in rows:
        rank = row.get('rank', '').strip()
        try:
            ea = float(row.get('Ea_eV', ''))
        except (ValueError, TypeError):
            continue
        found[rank] = True
        rank_ea[rank] = ea
    ea_score = 0.0
    ea_count = 0
    for rank, gea in gold_ea.items():
        if rank in rank_ea:
            if abs(rank_ea[rank] - gea) <= ea_tol:
                ea_score += 1.0
            ea_count += 1
    if ea_count == 0:
        return 0.0
    ea_score /= ea_count
    ordering_ok = 1.0
    if len(expected_order) >= 2:
        values = []
        for r in expected_order:
            if r not in rank_ea:
                ordering_ok = 0.0
                break
            values.append(rank_ea[r])
        if ordering_ok:
            for i in range(len(values)-1):
                if values[i] <= values[i+1]:
                    ordering_ok = 0.0
                    break
    return 0.8 * ea_score + 0.2 * ordering_ok


_SCORERS = {
    'step_core_shell_freq': score_0,
    'step_oxygen_fp_recombination_times': score_1,
    'step_oxygen_fp_arrhenius_params': score_2,
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
