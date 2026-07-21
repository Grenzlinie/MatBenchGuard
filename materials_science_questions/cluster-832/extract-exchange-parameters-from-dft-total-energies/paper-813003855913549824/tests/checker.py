import os
import json
import csv

# === author imports / helpers ===
import csv, json, os, math


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
    def prepare(outputs_dir, spec):
        steps_by_id = {s['id']: s for s in spec['steps']}
        return {'spec': spec, 'steps_by_id': steps_by_id}


# === block: score_0 (check id='step_5_total_energies_csv') ===
def score_0(artifact, step, ctx):
        if not isinstance(artifact, list) or not artifact:
            return 0.0
        data = {}
        for row in artifact:
            sys = row.get('system', '').strip()
            phase = row.get('phase', '').strip()
            try:
                energy = float(row['total_energy'])
            except (ValueError, KeyError):
                return 0.0
            data[(sys, phase)] = energy
        params = step.get('params', {})
        ordering_cfg = params.get('ordering_check', {})
        phases = ordering_cfg.get('pure', ['AF1','AF3','AF2','F'])
        ordered_pure = True
        for i in range(len(phases)-1):
            key1 = ('pure', phases[i])
            key2 = ('pure', phases[i+1])
            if key1 in data and key2 in data:
                if data[key1] >= data[key2] + 1e-6:
                    ordered_pure = False
                    break
        phases_d = ordering_cfg.get('doped', ['AF1','AF3','AF2','F'])
        ordered_doped = True
        for i in range(len(phases_d)-1):
            key1 = ('doped', phases_d[i])
            key2 = ('doped', phases_d[i+1])
            if key1 in data and key2 in data:
                if data[key1] >= data[key2] + 1e-6:
                    ordered_doped = False
                    break
        doping_checks = params.get('doping_effect_checks', [])
        sub_scores = []
        if doping_checks:
            for dcheck in doping_checks:
                diff_name = dcheck['difference']
                parts = diff_name.split('-')
                if len(parts) != 2: continue
                phaseA, phaseB = parts
                pure_keyA = ('pure', phaseA)
                pure_keyB = ('pure', phaseB)
                doped_keyA = ('doped', phaseA)
                doped_keyB = ('doped', phaseB)
                if all(key in data for key in [pure_keyA, pure_keyB, doped_keyA, doped_keyB]):
                    pure_diff = data[pure_keyA] - data[pure_keyB]
                    doped_diff = data[doped_keyA] - data[doped_keyB]
                    if dcheck.get('expect_doped_smaller', False):
                        passed = (pure_diff - doped_diff) > 1e-6
                    else:
                        passed = (doped_diff - pure_diff) > 1e-6
                    sub_scores.append(1.0 if passed else 0.0)
        score = 0.0
        if ordered_pure: score += 0.4
        if ordered_doped: score += 0.4
        if sub_scores:
            score += (sum(sub_scores)/len(sub_scores)) * 0.2
        return max(0.0, min(1.0, score))


# === block: score_1 (check id='step_6_magnetic_coupling') ===
def score_1(artifact, step, ctx):
        if not isinstance(artifact, dict):
            return 0.0
        params = step.get('params', {})
        targets = params.get('targets', {})
        tolerances = params.get('tolerances', {})
        pure = artifact.get('pure', {})
        doped = artifact.get('doped', {})
        vals = {
            'pure_J_c': pure.get('J_c'),
            'pure_J_ab': pure.get('J_ab'),
            'doped_J_c': doped.get('J_c'),
            'doped_J_ab': doped.get('J_ab')
        }
        components = []
        for key, target in targets.items():
            val = vals.get(key)
            if val is None:
                components.append(0.0)
                continue
            if 'J_c' in key:
                rel_tol = tolerances.get('J_c_relative_tol', 0.5)
                if target == 0:
                    comp = 1.0 if abs(val) < 1e-9 else 0.0
                else:
                    rel_err = abs((val - target)/target)
                    if rel_err <= rel_tol:
                        comp = 1.0
                    else:
                        comp = max(0.0, 1.0 - (rel_err - rel_tol))
            else:
                abs_tol = tolerances.get('J_ab_absolute_tol', 15.0)
                err = abs(val - target)
                if err <= abs_tol:
                    comp = 1.0
                else:
                    comp = max(0.0, 1.0 - (err - abs_tol)/(abs_tol+1))
            components.append(comp)
        if not components:
            return 0.0
        return sum(components) / len(components)


# === block: score_2 (check id='step_7_mulliken_orbitals') ===
def score_2(artifact, step, ctx):
        if not isinstance(artifact, dict):
            return 0.0
        params = step.get('params', {})
        thresholds = params.get('orbital_thresholds', {})
        def atom_passes(atom_data):
            required = ['d_xy','d_xz','d_yz','d_z2','d_x2-y2']
            for orb in required:
                if orb not in atom_data:
                    return False
            d_xy = atom_data['d_xy']
            d_xz = atom_data['d_xz']
            d_yz = atom_data['d_yz']
            d_z2 = atom_data['d_z2']
            d_x2y2 = atom_data['d_x2-y2']
            if d_xy < thresholds.get('d_xy_min', 1.5): return False
            if d_xz < thresholds.get('d_xz_min', 1.5): return False
            if d_yz < thresholds.get('d_yz_min', 1.5): return False
            if d_z2 < thresholds.get('d_z2_min', 1.5): return False
            if d_x2y2 < thresholds.get('d_x2-y2_min', 0.5): return False
            if d_x2y2 > thresholds.get('d_x2-y2_max', 1.8): return False
            return True
        atoms = []
        pure = artifact.get('pure', {})
        if 'Cu' in pure:
            atoms.append(pure['Cu'])
        elif isinstance(pure, dict):
            for key, val in pure.items():
                if isinstance(val, dict):
                    atoms.append(val)
        doped = artifact.get('doped', {})
        if doped and isinstance(doped, dict):
            for key, val in doped.items():
                if isinstance(val, dict):
                    atoms.append(val)
        if not atoms:
            return 0.0
        passed = sum(1 for a in atoms if atom_passes(a))
        return passed / len(atoms)


_SCORERS = {
    'step_5_total_energies_csv': score_0,
    'step_6_magnetic_coupling': score_1,
    'step_7_mulliken_orbitals': score_2,
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
