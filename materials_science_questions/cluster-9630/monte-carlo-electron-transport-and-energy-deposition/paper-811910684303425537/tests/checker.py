import os
import json
import csv

# === author imports / helpers ===
import json


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


# === block: score_0 (check id='step_03_aggregate') ===
def score_0(artifact, step, ctx):
    try:
        if not isinstance(artifact, dict):
            return 0.0
        te = artifact.get('time_evolution', [])
        mx = artifact.get('max_secondaries', [])
        if not te or not mx:
            return 0.0
        config = step.get('config', {})
        energies = config['energies']
        cases = config['cases']
        # Normalise energies to int for consistent lookups
        energies_num = [int(e) for e in energies]

        def classify_case(case_str):
            s = str(case_str).lower()
            if 'no' in s and 'loss' in s:
                return 'no_loss'
            return 'with_loss'

        te_dict = {}
        for row in te:
            energy = row.get('energy_eV')
            if energy is None:
                continue
            energy = int(round(float(energy)))
            case = classify_case(row.get('limiting_case', ''))
            key = (energy, case)
            if key not in te_dict:
                te_dict[key] = []
            t_val = row.get('time_fs')
            v_val = row.get('mean_num_secondaries')
            if t_val is None or v_val is None:
                continue
            te_dict[key].append((float(t_val), float(v_val)))
        for k in te_dict:
            te_dict[k].sort()

        max_dict = {}
        for row in mx:
            energy = row.get('energy_eV')
            if energy is None:
                continue
            energy = int(round(float(energy)))
            case = classify_case(row.get('limiting_case', ''))
            val = row.get('max_num')
            if val is None:
                continue
            max_dict[(energy, case)] = float(val)

        # 1. 100 fs check for 250 eV
        ref_100 = config['time_100fs_ref']['250']
        sc1 = 0.0
        for case in ('no_loss', 'with_loss'):
            key = (250, case)
            if key in te_dict:
                vals = [v for t, v in te_dict[key] if abs(t - 100) <= 1]
                if vals:
                    val = vals[0]
                    ref = ref_100[case]
                    err = abs(val - ref)
                    if err <= 3:
                        sc1 += 0.5
                    elif err <= 5:
                        sc1 += 0.25

        # 2. Monotonicity
        sc2 = 0.0
        ok = 0
        total = 0
        for case in ('no_loss', 'with_loss'):
            prev = -1.0
            case_ok = True
            for e in sorted(energies_num):
                v = max_dict.get((e, case))
                if v is None:
                    continue
                if v <= prev:
                    case_ok = False
                prev = v
            if case_ok:
                ok += 1
            total += 1
        sc2 = ok / total if total > 0 else 0.0

        # 3. Ordering: no_loss >= with_loss for each energy
        ordering_ok = 0
        for e in energies_num:
            v_no = max_dict.get((e, 'no_loss'))
            v_with = max_dict.get((e, 'with_loss'))
            if v_no is not None and v_with is not None and v_no >= v_with - 0.001:
                ordering_ok += 1
        sc3 = ordering_ok / len(energies_num) if energies_num else 0.0

        # 4. Approximate ratio to expected max
        sc4 = 0.0
        exp = config['expected_max_per_17eV']
        for i, e in enumerate(energies_num):
            v_no = max_dict.get((e, 'no_loss'))
            if v_no is not None:
                expected = float(exp[i]) if i < len(exp) else e / 14.66
                if expected == 0:
                    continue
                if abs(v_no - expected) / expected < 0.3:
                    sc4 += 0.5 / len(energies_num)
            v_with = max_dict.get((e, 'with_loss'))
            if v_with is not None:
                expected_no = float(exp[i]) if i < len(exp) else e / 14.66
                if v_with >= 0.5 * expected_no:
                    sc4 += 0.5 / len(energies_num)

        total_score = 0.3 * sc1 + 0.3 * sc2 + 0.2 * sc3 + 0.2 * sc4
        return max(0.0, min(1.0, total_score))
    except Exception:
        return 0.0


_SCORERS = {
    'step_03_aggregate': score_0,
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
