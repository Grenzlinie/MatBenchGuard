import os
import json
import csv

# === author imports / helpers ===
import csv, os


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
    csv_path = os.path.join(outputs_dir, 'absorption_spectra.csv')
    if not os.path.exists(csv_path):
        return {}
    with open(csv_path, newline='') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    energies, alpha2, alpha5 = [], [], []
    for row in rows:
        energies.append(float(row['photon_energy_eV']))
        alpha2.append(float(row['alpha_n2e18_cm_minus1']))
        alpha5.append(float(row['alpha_n5e18_cm_minus1']))
    sorted_idx = sorted(range(len(energies)), key=lambda i: energies[i])
    energies = [energies[i] for i in sorted_idx]
    alpha2 = [alpha2[i] for i in sorted_idx]
    alpha5 = [alpha5[i] for i in sorted_idx]
    def interp_edge(e_arr, a_arr):
        for i in range(len(a_arr)-1):
            if (a_arr[i] - 100) * (a_arr[i+1] - 100) <= 0:
                if a_arr[i+1] == a_arr[i]:
                    continue
                t = (100 - a_arr[i]) / (a_arr[i+1] - a_arr[i])
                return e_arr[i] + t * (e_arr[i+1] - e_arr[i])
        return None
    edge2 = interp_edge(energies, alpha2)
    edge5 = interp_edge(energies, alpha5)
    return {'edge2': edge2, 'edge5': edge5, 'energies': energies, 'alpha2': alpha2, 'alpha5': alpha5}


# === block: score_0 (check id='check_spectra') ===
def score_0(artifact, step, ctx):
    edge2 = ctx.get('edge2')
    edge5 = ctx.get('edge5')
    if edge2 is None or edge5 is None:
        return 0.0
    energies = ctx.get('energies', [])
    alpha2 = ctx.get('alpha2', [])
    alpha5 = ctx.get('alpha5', [])
    nonneg = all(a >= 0 for a in alpha2 + alpha5)
    plausible = (0.3 <= edge2 <= 1.0) and (0.3 <= edge5 <= 1.0)
    shift_ok = (edge5 - edge2) >= 0.005
    def frac_monotonic(e, a):
        if len(a) < 2:
            return 1.0
        inc = sum(1 for i in range(len(a)-1) if a[i+1] >= a[i])
        return inc / (len(a)-1)
    mono2 = frac_monotonic(energies, alpha2)
    mono5 = frac_monotonic(energies, alpha5)
    mono_ok = (mono2 >= 0.95) and (mono5 >= 0.95)
    score = 0.0
    if nonneg:
        score += 0.2
    if plausible:
        score += 0.3
    if shift_ok:
        score += 0.3
    if mono_ok:
        score += 0.2
    return score


# === block: score_1 (check id='check_edges_json') ===
def score_1(artifact, step, ctx):
    edge2_recomp = ctx.get('edge2')
    edge5_recomp = ctx.get('edge5')
    if edge2_recomp is None or edge5_recomp is None:
        return 0.0
    n2 = float(artifact.get('n2e18_edge_eV', -999))
    n5 = float(artifact.get('n5e18_edge_eV', -999))
    ok2 = abs(n2 - edge2_recomp) <= 0.001
    ok5 = abs(n5 - edge5_recomp) <= 0.001
    return (0.5 if ok2 else 0.0) + (0.5 if ok5 else 0.0)


_SCORERS = {
    'check_spectra': score_0,
    'check_edges_json': score_1,
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
