import os
import json
import csv


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


# === block: score_0 (check id='formation_energies') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        import math
        gold_v = step.get('gold_voltages_V', {})
        tol = step.get('tolerance_V', 0.1)
        li_metal = step.get('li_metal_energy_eV', -1.91)
        ref_lims2 = step.get('ref_LiMS2_energies_eV', {})
        # artifact is list of dicts with material, Li_content_x, formation_energy_eV_per_fu
        ms2_energies = {}
        for row in artifact:
            mat = row.get('material', '').strip()
            try:
                x = float(row.get('Li_content_x', ''))
            except:
                continue
            energy = float(row.get('formation_energy_eV_per_fu'))
            if abs(x - 0.0) < 1e-6:
                ms2_energies[mat] = energy
        correct = 0
        total = 0
        for mat, gold in gold_v.items():
            if mat not in ms2_energies:
                continue
            ems2 = ms2_energies[mat]
            elims2 = ref_lims2.get(mat)
            if elims2 is None:
                continue
            V = elims2 - ems2 - li_metal
            if abs(V - gold) <= tol:
                correct += 1
            total += 1
        return correct / max(total, 1)


# === block: score_1 (check id='relaxed_volumes') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold_vc = step.get('gold_volume_change_pct', {})
        tol = step.get('tolerance_pct', 2.0)
        # artifact list of dicts with material, composition, volume_ang3
        volumes = {}
        for row in artifact:
            mat = row.get('material', '').strip()
            comp = row.get('composition', '').strip()
            vol = float(row.get('volume_ang3'))
            volumes.setdefault(mat, {})[comp] = vol
        correct = 0
        total = 0
        for mat, gold in gold_vc.items():
            if mat not in volumes or 'LiMS2' not in volumes[mat] or 'MS2' not in volumes[mat]:
                continue
            v_lims2 = volumes[mat]['LiMS2']
            v_ms2 = volumes[mat]['MS2']
            delta = (v_ms2 - v_lims2) / v_lims2 * 100.0
            if abs(delta - gold) <= tol:
                correct += 1
            total += 1
        return correct / max(total, 1)


# === block: score_2 (check id='neb_energy_profiles') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold_barriers = step.get('gold_barriers_eV', {})
        tol = step.get('tolerance_eV', 0.05)
        required = set(gold_barriers.keys())
        correct = 0
        total = 0
        for mat in required:
            if mat not in artifact or not isinstance(artifact[mat], list):
                continue
            energies = [float(x) for x in artifact[mat]]
            barrier = max(energies) - min(energies)
            gold = gold_barriers[mat]
            eff_tol = max(tol, 0.2 * gold)
            if abs(barrier - gold) <= eff_tol:
                correct += 1
            total += 1
        return correct / max(total, 1)


# === block: score_3 (check id='interface_neb_profile') ===
def score_3(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold = step.get('gold_barrier_eV', 0.68)
        tol = step.get('tolerance_eV', 0.1)
        if not isinstance(artifact, list):
            return 0.0
        energies = [float(x) for x in artifact]
        barrier = max(energies) - min(energies)
        if abs(barrier - gold) <= tol:
            return 1.0
        return 0.0


_SCORERS = {
    'formation_energies': score_0,
    'relaxed_volumes': score_1,
    'neb_energy_profiles': score_2,
    'interface_neb_profile': score_3,
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
