import os
import json
import csv

# === author imports / helpers ===
import csv, io, os, math, json


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


# === block: score_0 (check id='binding_enthalpies') ===
def score_0(artifact, step, ctx):
        if not isinstance(artifact, list):
            return 0.0
        mol_map = {row.get('molecule',''): row for row in artifact if row.get('molecule')}
        gold = step['gold']
        tol_H = float(step.get('tolerance_H', 1.5))
        tol_G = float(step.get('tolerance_G', 1.5))
        h_hits = 0
        g_hits = 0
        total_mols = len(gold)
        for mol, ref in gold.items():
            row = mol_map.get(mol)
            if row is None:
                continue
            try:
                h_val = float(row.get('delta_H298_kcalmol', float('inf')))
                if abs(h_val - ref['delta_H298_kcalmol']) <= tol_H + 1e-9:
                    h_hits += 1
            except:
                pass
            try:
                g_val = float(row.get('delta_G298_kcalmol', float('inf')))
                if abs(g_val - ref['delta_G298_kcalmol']) <= tol_G + 1e-9:
                    g_hits += 1
            except:
                pass
        value_score = 0.5 * (h_hits / total_mols) + 0.5 * (g_hits / total_mols) if total_mols > 0 else 0.0
        expected_order = step.get('expected_order', [])
        if expected_order:
            agent_vals = []
            for mol in expected_order:
                row = mol_map.get(mol)
                if row:
                    try:
                        agent_vals.append(float(row.get('delta_H298_kcalmol', float('inf'))))
                    except:
                        agent_vals.append(float('inf'))
                else:
                    agent_vals.append(float('inf'))
            n = len(agent_vals)
            inversions = 0
            for i in range(n):
                for j in range(i+1, n):
                    if agent_vals[i] > agent_vals[j] + 1e-6:
                        inversions += 1
            max_inv = n*(n-1)//2 if n>1 else 0
            order_score = max(0.0, 1.0 - inversions / max_inv) if max_inv > 0 else 1.0
        else:
            order_score = 1.0
        weight_value = 0.7
        weight_order = 0.3
        return weight_value * value_score + weight_order * order_score


# === block: score_1 (check id='dhb_isomer_energies') ===
def score_1(artifact, step, ctx):
        gold = step['gold']
        tolerances = step.get('tolerances', {})
        if not isinstance(artifact, list):
            return 0.0
        isomer_map = {}
        for row in artifact:
            label_raw = row.get('isomer_label')
            if label_raw is None:
                continue
            try:
                ilabel = str(int(label_raw))
            except:
                ilabel = str(label_raw)
            isomer_map[ilabel] = row
        passed = 0
        total = len(gold)
        for ilabel, ref_val in gold.items():
            row = isomer_map.get(ilabel)
            if row is None:
                continue
            if ref_val == 'not found':
                val_str = str(row.get('relative_delta_H_kcalmol', '')).strip().lower()
                if val_str in ('', 'not found', 'not_found', 'nan', 'none', '-'):
                    passed += 1
            else:
                try:
                    val = float(row.get('relative_delta_H_kcalmol'))
                    tol = float(tolerances.get(ilabel, 1.5))
                    if abs(val - ref_val) <= tol + 1e-9:
                        passed += 1
                except (ValueError, TypeError):
                    pass
        score = passed / total if total > 0 else 0.0
        return score


_SCORERS = {
    'binding_enthalpies': score_0,
    'dhb_isomer_energies': score_1,
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
