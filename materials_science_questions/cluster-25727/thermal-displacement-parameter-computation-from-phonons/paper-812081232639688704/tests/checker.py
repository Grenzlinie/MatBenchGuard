import os
import json
import csv

# === author imports / helpers ===
import csv, math


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
    step = spec['steps'][0]
    return {'expected_rows': step['expected_rows'], 'tol': step['tolerance']}


# === block: score_0 (check id='compute_ratios') ===
def score_0(artifact, step, ctx):
    if not artifact:
        return 0.0

    R = 8.314

    free_params = {
        'Fe': (0.2482, 6.42),
        'β-Sn': (0.3181, 9.25),
        'Se': (0.4366, 10.93),
        'Cu': (0.2556, 8.08),
        'Co': (0.2507, 7.83),
        'Au': (0.2884, 7.74),
        'Pb': (0.3500, 6.71),
    }

    h_Ar = 0.3650
    Tm_Ar = 83.80
    h_M = 0.2863
    TM_Al = 933.47

    def alpha_free(delS):
        return 2 * delS / (3 * R) + 1

    def alpha_embedded():
        return ((h_M / h_Ar) ** 2 * Tm_Ar / TM_Al + 1) / 2

    def compute_expected(material, d, D, interface_type):
        if interface_type == 'free':
            h, delS = free_params[material]
            alpha = alpha_free(delS)
        elif interface_type == 'embedded':
            if material != 'Ar':
                raise ValueError('Only Ar is supported for embedded')
            h = h_Ar
            alpha = alpha_embedded()
        else:
            raise ValueError('Unknown interface type')
        D0 = 2 * (3 - d) * h
        factor = (alpha - 1) / (D / D0 - 1)
        td = math.exp(-factor / 2)
        te = td
        av = math.exp(factor)
        return td, te, av

    test_cases = []
    for size in [5.0, 10.0, 20.0, 50.0]:
        test_cases.append(('Fe', 0, size, 'free'))
    for size in [10.0, 20.0, 50.0]:
        test_cases.append(('β-Sn', 0, size, 'free'))
    for size in [10.0, 20.0, 50.0]:
        test_cases.append(('Se', 0, size, 'free'))
    for size in [10.0, 20.0, 50.0]:
        test_cases.append(('Cu', 0, size, 'free'))
    for size in [10.0, 20.0, 50.0]:
        test_cases.append(('Co', 0, size, 'free'))
    for size in [10.0, 20.0, 50.0]:
        test_cases.append(('Au', 0, size, 'free'))
    for size in [10.0, 20.0, 50.0]:
        test_cases.append(('Pb', 0, size, 'free'))
    for size in [5.0, 10.0, 20.0, 50.0]:
        test_cases.append(('Ar', 0, size, 'embedded'))
    for size in [10.0, 20.0, 50.0]:
        test_cases.append(('Fe', 1, size, 'free'))
    for size in [10.0, 20.0, 50.0]:
        test_cases.append(('Fe', 2, size, 'free'))
    for size in [10.0, 20.0, 50.0]:
        test_cases.append(('Cu', 1, size, 'free'))
    for size in [10.0, 20.0, 50.0]:
        test_cases.append(('Cu', 2, size, 'free'))

    agent_rows = {}
    for row in artifact:
        try:
            key = (row['material'].strip(), int(row['dimension']), float(row['size_nm']), row['interface_type'].strip())
        except Exception:
            continue
        if key not in agent_rows:
            agent_rows[key] = row

    tol = 1e-12
    correct = 0
    total = len(test_cases)
    for (mat, d, size, iface) in test_cases:
        key = (mat, d, size, iface)
        agent_row = agent_rows.get(key)
        if agent_row is None:
            continue
        td_exp, te_exp, av_exp = compute_expected(mat, d, size, iface)
        try:
            td_agent = float(agent_row['ThetaD_ratio'])
            te_agent = float(agent_row['ThetaE_ratio'])
            av_agent = float(agent_row['alphav_ratio'])
        except Exception:
            continue
        if any(abs(a - e) > tol * max(1.0, abs(e)) for a, e in [(td_agent, td_exp), (te_agent, te_exp), (av_agent, av_exp)]):
            continue
        correct += 1

    score = correct / total if total > 0 else 0.0
    return score


_SCORERS = {
    'compute_ratios': score_0,
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
