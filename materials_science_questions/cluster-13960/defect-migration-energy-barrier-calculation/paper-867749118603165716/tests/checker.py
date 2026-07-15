import os
import json
import csv

# === author imports / helpers ===
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
    import os
    import csv

    ctx = {}
    outputs_dir = outputs_dir
    # Load energy path artifact
    energy_csv = os.path.join(outputs_dir, "step_01_energy_path.csv")
    if os.path.exists(energy_csv):
        with open(energy_csv, newline='') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        energies = [float(r['energy_eV']) for r in rows]
        if energies:
            max_energy = max(energies)
            ctx['energy_path'] = {'max_energy': max_energy, 'energies': energies, 'ep_start': energies[0], 'ep_end': energies[-1]}
        else:
            ctx['energy_path'] = None
    else:
        ctx['energy_path'] = None

    # Extract hidden gold from spec steps
    for step in spec.get('steps', []):
        if step.get('id') == 'energy_path':
            ctx['target_barrier'] = step.get('target_barrier_eV', 0.40)
            ctx['tolerance_rel'] = step.get('tolerance_rel', 0.50)
        elif step.get('id') == 'band_gaps':
            ctx['band_gaps_params'] = step.get('params', {})
    return ctx


# === block: score_0 (check id='energy_path') ===
def score_0(artifact, step, ctx):
    energies = [float(r['energy_eV']) for r in artifact]
    if len(energies) < 3:
        return 0.0
    max_e = max(energies)
    start_e = energies[0]
    end_e = energies[-1]
    barrier = max_e - (start_e + end_e) / 2.0
    target = ctx.get('target_barrier', 0.40)
    tol = ctx.get('tolerance_rel', 0.50)
    if target <= 0:
        return 0.0
    rel_err = abs(barrier - target) / target
    if rel_err <= tol:
        return 1.0
    else:
        if rel_err >= 1.0:
            return 0.0
        return max(0.0, 1.0 - (rel_err - tol) / (1.0 - tol))


# === block: score_1 (check id='band_gaps') ===
def score_1(artifact, step, ctx):
    band_gaps = []
    for row in artifact:
        try:
            band_gaps.append((row['step'].strip(), float(row['band_gap_eV'])))
        except:
            return 0.0
    if len(band_gaps) < 1:
        return 0.0
    params = ctx.get('band_gaps_params', {})
    m1_min = params.get('m1_gap_min', 0.5)
    metallic_th = params.get('metallic_threshold', 0.1)
    sub_w = [0.1, 0.15, 0.15]
    total = 0.0
    # 1) M1 insulating
    if band_gaps[0][0].lower() == 'm1' and band_gaps[0][1] >= m1_min:
        total += sub_w[0]
    # 2) monotonic non-increasing (row order defines the listed sequence)
    mono = True
    for i in range(1, len(band_gaps)):
        if band_gaps[i][1] > band_gaps[i-1][1] + 1e-9:
            mono = False
            break
    if mono:
        total += sub_w[1]
    # 3) closure before barrier: at least one step with gap <= metallic_th
    #    has its NEB image energy lower than the maximum energy; map step label to index
    def _step_to_idx(step_str):
        s = step_str.strip().lower()
        if s == 'm1':
            return 0
        if s.startswith('step'):
            try:
                return int(s[4:])
            except:
                return None
        # plain integer label
        try:
            return int(s)
        except:
            return None
    ep = ctx.get('energy_path', {})
    if ep and 'energies' in ep and 'max_energy' in ep:
        energies = ep['energies']
        max_energy = ep['max_energy']
        found_closure = False
        for step_str, gap in band_gaps:
            idx = _step_to_idx(step_str)
            if idx is not None and 0 <= idx < len(energies):
                if energies[idx] < max_energy and gap <= metallic_th:
                    found_closure = True
                    break
        if found_closure:
            total += sub_w[2]
    return total


_SCORERS = {
    'energy_path': score_0,
    'band_gaps': score_1,
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
