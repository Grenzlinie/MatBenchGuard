import os
import json
import csv

# === author imports / helpers ===
import json, csv, math
from itertools import zip_longest


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


# === block: score_0 (check id='equilibrium_properties') ===
def score_0(artifact, step, ctx):
        gold = step['gold']
        tol = step['tolerances']
        if not isinstance(artifact, dict):
            return 0.0
        fields = ['lattice_constant_angstrom', 'total_magnetic_moment_muB',
                  'Mn_A_moment_muB', 'Mn_B_moment_muB', 'Sn_moment_muB',
                  'formation_energy_eV', 'cohesive_energy_eV']
        scores = []
        for f in fields:
            v = artifact.get(f)
            if v is None:
                scores.append(0.0)
                continue
            try:
                val = float(v)
            except (ValueError, TypeError):
                scores.append(0.0)
                continue
            if abs(val - gold[f]) <= tol.get(f, 0.0):
                scores.append(1.0)
            else:
                scores.append(0.0)
        return sum(scores) / len(scores) if scores else 0.0


# === block: score_1 (check id='elastic_constants') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold = step['gold']
        tol = step['tolerances']
        required = ['C11_GPa', 'C12_GPa', 'C44_GPa']
        for r in required:
            if r not in artifact:
                return 0.0
        try:
            c11 = float(artifact['C11_GPa'])
            c12 = float(artifact['C12_GPa'])
            c44 = float(artifact['C44_GPa'])
        except (ValueError, TypeError):
            return 0.0
        # recompute VRH moduli
        Bv = (c11 + 2*c12) / 3.0
        Gv = (c11 - c12 + 3*c44) / 5.0
        denom = 4*c44 + 3*(c11 - c12)
        Gr = 5*c44*(c11 - c12) / denom if denom != 0 else 0.0
        B = Bv  # Voigt-Reuss-Hill average (same for cubic)
        G = (Gv + Gr) / 2.0
        E = 9*G*B / (3*B + G) if (3*B + G) != 0 else 0.0
        B_over_G = B / G if G != 0 else 0.0
        # compare fields
        checks = [
            ('C11_GPa', c11),
            ('C12_GPa', c12),
            ('C44_GPa', c44),
            ('Bulk_modulus_GPa', B),
            ('Shear_modulus_GPa', G),
            ('Youngs_modulus_GPa', E),
            ('B_over_G', B_over_G)
        ]
        scores = []
        for key, comp in checks:
            if key not in artifact:
                scores.append(0.0)
                continue
            try:
                val = float(artifact[key])
            except (ValueError, TypeError):
                scores.append(0.0)
                continue
            if abs(comp - gold[key]) <= tol.get(key, 0.0) and abs(val - gold[key]) <= tol.get(key, 0.0):
                scores.append(1.0)
            elif abs(comp - gold[key]) <= tol.get(key, 0.0):
                scores.append(0.5)  # recomputed correct but self-reported wrong
            elif abs(val - gold[key]) <= tol.get(key, 0.0):
                scores.append(0.5)  # self-reported correct but recomputed wrong
            else:
                scores.append(0.0)
        return sum(scores) / len(scores) if scores else 0.0


# === block: score_2 (check id='strain_classification') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold_rows = step['gold']
        tol_gap = step.get('tolerance_gap_eV', 0.05)
        if not isinstance(artifact, list) or len(artifact) < len(gold_rows):
            return 0.0
        correct = 0
        for i, gold_row in enumerate(gold_rows):
            if i >= len(artifact):
                break
            agent_row = artifact[i]
            try:
                lat = str(agent_row.get('lattice_constant', '')).strip()
                gold_lat = str(gold_row['lattice_constant']).strip()
                if lat != gold_lat:
                    continue
                cls = str(agent_row.get('classification', '')).strip()
                if cls != gold_row['classification']:
                    continue
                maj = float(agent_row.get('majority_indirect_gap_eV', 999))
                mino = float(agent_row.get('minority_indirect_gap_eV', 999))
                if abs(maj - gold_row['majority_indirect_gap_eV']) <= tol_gap and \
                   abs(mino - gold_row['minority_indirect_gap_eV']) <= tol_gap:
                    correct += 1
            except (ValueError, TypeError, KeyError):
                continue
        return correct / len(gold_rows) if gold_rows else 0.0


_SCORERS = {
    'equilibrium_properties': score_0,
    'elastic_constants': score_1,
    'strain_classification': score_2,
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
