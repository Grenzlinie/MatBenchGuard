import os
import json
import csv

# === author imports / helpers ===
import os, csv


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
        return {'outputs_dir': outputs_dir}


# === block: score_0 (check id='gs_config_exact') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold = step.get('gold_configs', {})
        if not gold or not artifact:
            return 0.0
        count = 0
        total = len(artifact)
        for row in artifact:
            sys = row.get('system', '')
            if sys in gold and row.get('atomic_config') == gold[sys]:
                count += 1
        return count / total if total else 0.0


# === block: score_1 (check id='gs_binding_energy') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold = step.get('gold_binding_energies', {})
        tol = step.get('binding_tol', 0.1)
        if not gold or not artifact:
            return 0.0
        count = 0
        total = len(artifact)
        for row in artifact:
            sys = row.get('system', '')
            if sys in gold:
                try:
                    val = float(row['binding_energy_per_atom'])
                    if abs(val - gold[sys]) <= tol:
                        count += 1
                except (ValueError, KeyError):
                    pass
        return count / total if total else 0.0


# === block: score_2 (check id='gs_relative_stability') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        comps = step.get('compositions', ['Cu13Ni42','Cu27Ni28','Cu13Pd42','Cu27Pd28'])
        if not artifact:
            return 0.0
        energies = {}
        for row in artifact:
            key = (row.get('composition',''), row.get('structure',''))
            try:
                energies[key] = float(row['binding_energy_per_atom'])
            except (ValueError, KeyError):
                pass
        passed = 0
        for comp in comps:
            val_ico = energies.get((comp, 'ico'))
            val_cubo = energies.get((comp, 'cubo'))
            if val_ico is not None and val_cubo is not None and val_ico > val_cubo:
                passed += 1
        return passed / len(comps) if comps else 0.0


# === block: score_3 (check id='br_consistency') ===
def score_3(artifact, step, ctx):
    def score(artifact, step, ctx):
        gs_path = os.path.join(ctx['outputs_dir'], 'ground_state_configs.csv')
        try:
            with open(gs_path, newline='') as f:
                gs_rows = list(csv.DictReader(f))
        except Exception:
            return 0.0
        gs_map = {}
        for row in gs_rows:
            sys = row.get('system','')
            try:
                gs_map[sys] = (float(row['binding_energy_per_atom']), float(row['average_Cu_radial_distance']))
            except (ValueError, KeyError):
                pass
        max_map = {}
        for row in artifact:
            sys = row.get('system','')
            try:
                val = float(row['binding_energy_per_atom'])
                if sys not in max_map or val > max_map[sys][0]:
                    max_map[sys] = (val, float(row.get('average_Cu_radial_distance', 0)))
            except (ValueError, KeyError):
                pass
        tol_bind = step.get('tolerance_binding', 0.1)
        tol_rad = step.get('tolerance_radial', 0.1)
        matches = 0
        total = 0
        for sys in gs_map:
            if sys in max_map:
                total += 1
                max_bind, max_rad = max_map[sys]
                gs_bind, gs_rad = gs_map[sys]
                if abs(max_bind - gs_bind) <= tol_bind and abs(max_rad - gs_rad) <= tol_rad:
                    matches += 1
        return matches / total if total else 0.0


# === block: score_4 (check id='br_relative_stability') ===
def score_4(artifact, step, ctx):
        comps = ['Cu13Ni42','Cu27Ni28']
        if not artifact:
            return 0.0
        max_map = {}
        for row in artifact:
            key = (row.get('composition',''), row.get('structure',''))
            try:
                val = float(row['binding_energy_per_atom'])
                if key not in max_map or val > max_map[key]:
                    max_map[key] = val
            except (ValueError, KeyError):
                pass
        passed = 0
        for comp in comps:
            val_ico = max_map.get((comp, 'ico'))
            val_cubo = max_map.get((comp, 'cubo'))
            if val_ico is not None and val_cubo is not None and val_ico > val_cubo:
                passed += 1
        return passed / len(comps) if comps else 0.0


_SCORERS = {
    'gs_config_exact': score_0,
    'gs_binding_energy': score_1,
    'gs_relative_stability': score_2,
    'br_consistency': score_3,
    'br_relative_stability': score_4,
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
