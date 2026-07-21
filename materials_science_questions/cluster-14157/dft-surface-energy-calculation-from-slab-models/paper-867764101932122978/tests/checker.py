import os
import json
import csv

# === author imports / helpers ===
import csv, json, os


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


# --- Gold data embedded directly in the checker (never exposed to the agent) ---
_GOLD_E_VBM = {
    "(001)": -2.6358,
    "(100)": -1.8181,
}
_GOLD_MU_O2 = -10.4857
_GOLD_DEFECT_TABLE = [
    {"surface": "(001)", "site": "site1", "charge": 0, "E_form": 5.1378, "is_LEMS": False},
    {"surface": "(001)", "site": "site1", "charge": 1, "E_form": 5.3593, "is_LEMS": True},
    {"surface": "(001)", "site": "site1", "charge": 2, "E_form": 5.9628, "is_LEMS": True},
    {"surface": "(001)", "site": "site2", "charge": 0, "E_form": 5.2306, "is_LEMS": False},
    {"surface": "(001)", "site": "site2", "charge": 1, "E_form": 5.3537, "is_LEMS": True},
    {"surface": "(001)", "site": "site2", "charge": 2, "E_form": 5.9717, "is_LEMS": True},
    {"surface": "(001)", "site": "subsurface", "charge": 0, "E_form": 5.5779, "is_LEMS": False},
    {"surface": "(001)", "site": "subsurface", "charge": 1, "E_form": 5.5137, "is_LEMS": True},
    {"surface": "(001)", "site": "subsurface", "charge": 2, "E_form": 2.7874, "is_LEMS": False},
    {"surface": "(100)", "site": "bridge", "charge": 0, "E_form": 5.2099, "is_LEMS": False},
    {"surface": "(100)", "site": "bridge", "charge": 1, "E_form": 3.6295, "is_LEMS": True},
    {"surface": "(100)", "site": "bridge", "charge": 2, "E_form": 3.6239, "is_LEMS": True},
    {"surface": "(100)", "site": "metastable ring", "charge": 0, "E_form": 5.3224, "is_LEMS": False},
    {"surface": "(100)", "site": "metastable ring", "charge": 1, "E_form": 3.1666, "is_LEMS": True},
    {"surface": "(100)", "site": "metastable ring", "charge": 2, "E_form": 1.2963, "is_LEMS": False},
    {"surface": "(100)", "site": "ring 2III-O", "charge": 0, "E_form": 3.4193, "is_LEMS": False},
    {"surface": "(100)", "site": "ring 2III-O", "charge": 1, "E_form": 0.6417, "is_LEMS": True},
    {"surface": "(100)", "site": "ring 2III-O", "charge": 2, "E_form": -1.1842, "is_LEMS": False},
]

_ALLOWED_GEOMETRIES = {"Si-Si dimer", "puckered configuration", "2III-O"}


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
    # Gold data is now embedded; spec is no longer used to retrieve it.
    return {
        'gold_table': _GOLD_DEFECT_TABLE,
        'gold_E_VBM': _GOLD_E_VBM,
        'gold_mu_O2': _GOLD_MU_O2,
    }


# === block: score_0 (check id='check_slab_energies') ===
def score_0(artifact, step, ctx):
    if artifact is None:
        return 0.0
    gold = ctx['gold_E_VBM']
    tol = step.get('tolerance_E_VBM', 0.01)
    found = {}
    for row in artifact:
        if not isinstance(row, dict):
            continue
        if 'surface' not in row or 'E_VBM' not in row:
            continue
        try:
            val = float(row['E_VBM'])
        except (ValueError, TypeError):
            continue
        found[row['surface']] = val
    if sorted(found.keys()) != ['(001)', '(100)']:
        return 0.0
    if abs(found['(001)'] - gold['(001)']) <= tol and abs(found['(100)'] - gold['(100)']) <= tol:
        return 1.0
    else:
        return 0.0


# === block: score_0b (check id='check_slab_total_energy') ===
def score_0b(artifact, step, ctx):
    """Verify that slab_total_energy is present and numeric for both surfaces."""
    if artifact is None:
        return 0.0
    surfaces_seen = set()
    for row in artifact:
        if not isinstance(row, dict):
            continue
        surf = row.get('surface')
        val_str = row.get('slab_total_energy')
        if surf is None or val_str is None:
            continue
        try:
            float(val_str)
            surfaces_seen.add(str(surf))
        except (ValueError, TypeError):
            return 0.0
    if surfaces_seen == {'(001)', '(100)'}:
        return 1.0
    return 0.0


# === block: score_1 (check id='check_mu_O2') ===
def score_1(artifact, step, ctx):
    gold = ctx['gold_mu_O2']
    tol = step.get('tolerance', 0.001)
    try:
        val = float(artifact.strip())
    except:
        return 0.0
    if abs(val - gold) <= tol:
        return 1.0
    else:
        return 0.0


# === block: score_2 (check id='check_formation_energies') ===
def score_2(artifact, step, ctx):
    gold_table = ctx['gold_table']
    tol = step.get('tolerance_E_form', 0.5)
    gold_lookup = {}
    for g in gold_table:
        key = (g['surface'], g['site'], g['charge'])
        gold_lookup[key] = g['E_form']
    correct = 0
    total = 0
    for row in artifact:
        try:
            surface = row['surface']
            site = row['site']
            charge = int(row['charge'])
            agent_val = float(row['E_form'])
        except (KeyError, ValueError):
            continue
        key = (surface, site, charge)
        if key in gold_lookup:
            if abs(agent_val - gold_lookup[key]) <= tol:
                correct += 1
            total += 1
    if total == 0:
        return 0.0
    return correct / total


# === block: score_3 (check id='check_LEMS') ===
def score_3(artifact, step, ctx):
    gold_table = ctx['gold_table']
    gold_lookup = {}
    for g in gold_table:
        key = (g['surface'], g['site'], g['charge'])
        gold_lookup[key] = g['is_LEMS']
    correct = 0
    total = 0
    for row in artifact:
        try:
            surface = row['surface']
            site = row['site']
            charge = int(row['charge'])
            agent_LEMS = row['is_LEMS']
        except (KeyError, ValueError):
            continue
        if isinstance(agent_LEMS, str):
            agent_LEMS = agent_LEMS.strip().lower() in ('true', '1', 'yes')
        else:
            agent_LEMS = bool(agent_LEMS)
        key = (surface, site, charge)
        if key in gold_lookup:
            if agent_LEMS == gold_lookup[key]:
                correct += 1
            total += 1
    if total == 0:
        return 0.0
    return correct / total


# === block: score_4 (check id='check_geometry_type') ===
def score_4(artifact, step, ctx):
    """Verify geometry_type is one of the allowed strings."""
    if artifact is None:
        return 0.0
    allowed = _ALLOWED_GEOMETRIES
    total = 0
    correct = 0
    for row in artifact:
        if not isinstance(row, dict):
            continue
        geom = row.get('geometry_type')
        if geom is None:
            continue
        total += 1
        if str(geom).strip() in allowed:
            correct += 1
    if total == 0:
        return 0.0
    return correct / total


# === block: score_5 (check id='check_magnetic_moment') ===
def score_5(artifact, step, ctx):
    """Check magnetic_moment_ground_state consistency with is_LEMS."""
    if artifact is None:
        return 0.0
    total = 0
    correct = 0
    for row in artifact:
        if not isinstance(row, dict):
            continue
        try:
            mag = float(row.get('magnetic_moment_ground_state', ''))
            lems_raw = row.get('is_LEMS', '')
            if isinstance(lems_raw, str):
                lems = lems_raw.strip().lower() in ('true', '1', 'yes')
            else:
                lems = bool(lems_raw)
            total += 1
            # Non-zero moment for magnetic, zero for non-magnetic.
            if (lems and abs(mag) > 1e-6) or (not lems and abs(mag) < 1e-6):
                correct += 1
        except (ValueError, TypeError):
            continue
    if total == 0:
        return 0.0
    return correct / total


_SCORERS = {
    'check_slab_energies': score_0,
    'check_slab_total_energy': score_0b,
    'check_mu_O2': score_1,
    'check_formation_energies': score_2,
    'check_LEMS': score_3,
    'check_geometry_type': score_4,
    'check_magnetic_moment': score_5,
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