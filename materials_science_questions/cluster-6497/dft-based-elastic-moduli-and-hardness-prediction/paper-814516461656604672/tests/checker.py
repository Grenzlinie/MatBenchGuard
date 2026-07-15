import os
import json
import csv

# === author imports / helpers ===
import os
import json
import math

from typing import Dict, Any, List, Tuple


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
        # Load gold tables into spec for easy access
        steps = spec.get('steps', [])
        ctx = {}
        for step in steps:
            if 'gold_table' in step:
                step['gold_table_parsed'] = {}
                for key, val in step['gold_table'].items():
                    # Key is "(Re, Os)" string; parse to tuple
                    parts = key.strip('()').split(',')
                    if len(parts) == 2:
                        try:
                            re = float(parts[0].strip())
                            os = float(parts[1].strip())
                            step['gold_table_parsed'][(re, os)] = val
                        except:
                            pass
        return ctx


# === block: score_0 (check id='single_crystal_constants_file_check') ===
def score_0(artifact, step, ctx):
        import json as _json
        import os as _os
        # Load single crystal constants file to make it available for trends scorer
        single_path = _os.path.join('/app/outputs', 'single_crystal_elastic_constants.json')
        if _os.path.isfile(single_path):
            try:
                with open(single_path) as _f:
                    ctx['single_constants'] = _json.load(_f)
            except Exception:
                ctx['single_constants'] = []
        else:
            ctx['single_constants'] = []

        if not isinstance(artifact, list):
            return 0.0
        required = step.get('required_compositions', [])
        keys = set()
        for comp in required:
            keys.add(tuple(comp))
        present = set()
        for entry in artifact:
            if 'Re' in entry and 'Os' in entry:
                present.add((entry['Re'], entry['Os']))
        if keys.issubset(present):
            return 1.0
        return 0.0


# === block: score_1 (check id='single_crystal_constants_values') ===
def score_1(artifact, step, ctx):
        import os as _os
        import json as _json

        # Ensure single crystal constants are available for downstream scorers (e.g., trends)
        if 'single_constants' not in ctx:
            single_path = _os.path.join('/app/outputs', 'single_crystal_elastic_constants.json')
            if _os.path.isfile(single_path):
                try:
                    with open(single_path) as _f:
                        ctx['single_constants'] = _json.load(_f)
                except Exception:
                    ctx['single_constants'] = []
            else:
                ctx['single_constants'] = []

        gold_table = step.get('gold_table_parsed', {})
        tolerances = step.get('tolerances', {})
        if not gold_table:
            return 0.0
        scores = []
        for entry in artifact:
            key = (entry.get('Re'), entry.get('Os'))
            if key not in gold_table:
                continue
            gold = gold_table[key]
            for field in gold:
                if field not in entry:
                    continue
                tol = tolerances.get(field, {})
                atol = tol.get('atol', 0.0)
                rtol = tol.get('rtol', 0.0)
                agent_val = entry[field]
                gold_val = gold[field]
                # Handle NaN/inf
                if not math.isfinite(agent_val) or not math.isfinite(gold_val):
                    scores.append(0.0)
                    continue
                diff = abs(agent_val - gold_val)
                allowed = atol + rtol * abs(gold_val)
                scores.append(1.0 if diff <= allowed else 0.0)
        if not scores:
            return 0.0
        return sum(scores) / len(scores)


# === block: score_2 (check id='single_crystal_constants_consistency') ===
def score_2(artifact, step, ctx):
        import os as _os
        import json as _json
        if 'single_constants' not in ctx:
            single_path = _os.path.join('/app/outputs', 'single_crystal_elastic_constants.json')
            if _os.path.isfile(single_path):
                try:
                    with open(single_path) as _f:
                        ctx['single_constants'] = _json.load(_f)
                except Exception:
                    ctx['single_constants'] = []
            else:
                ctx['single_constants'] = []
        if not isinstance(artifact, list):
            return 0.0
        relations = step.get('relations', [])
        total = 0
        count = 0
        for entry in artifact:
            if not all(k in entry for k in ('C11_GPa','C12_GPa','bulk_modulus_GPa','Cprime_GPa')):
                continue
            C11 = entry['C11_GPa']
            C12 = entry['C12_GPa']
            B_reported = entry['bulk_modulus_GPa']
            Cprime_reported = entry['Cprime_GPa']
            B_pred = (C11 + 2*C12) / 3.0
            Cprime_pred = (C11 - C12) / 2.0
            for rel in relations:
                if rel['name'] == 'bulk_from_Cij':
                    tol = rel.get('tolerance_rel', 0.01)
                    if B_reported:
                        if abs(B_pred - B_reported) / abs(B_reported) <= tol:
                            score = 1.0
                        else:
                            score = max(0.0, 1.0 - (abs(B_pred - B_reported) / abs(B_reported) - tol)/tol)
                    else:
                        score = 0.0
                    total += score
                    count += 1
                elif rel['name'] == 'Cprime_from_Cij':
                    tol = rel.get('tolerance_rel', 0.01)
                    if Cprime_reported:
                        if abs(Cprime_pred - Cprime_reported) / abs(Cprime_reported) <= tol:
                            score = 1.0
                        else:
                            score = max(0.0, 1.0 - (abs(Cprime_pred - Cprime_reported) / abs(Cprime_reported) - tol)/tol)
                    else:
                        score = 0.0
                    total += score
                    count += 1
        if count == 0:
            return 0.0
        return total / count


# === block: score_3 (check id='derived_properties_file_check') ===
def score_3(artifact, step, ctx):
    def score_derived_properties_file(artifact, step, ctx):
        if not isinstance(artifact, list):
            return 0.0
        required = step.get('required_compositions', [])
        keys = set()
        for comp in required:
            keys.add(tuple(comp))
        present = set()
        for entry in artifact:
            if 'Re' in entry and 'Os' in entry:
                present.add((entry['Re'], entry['Os']))
        if keys.issubset(present):
            return 1.0
        return 0.0


# === block: score_4 (check id='derived_properties_values') ===
def score_4(artifact, step, ctx):
    def score_derived_properties_values(artifact, step, ctx):
        gold_table = step.get('gold_table_parsed', {})
        tolerances = step.get('tolerances', {})
        if not gold_table:
            return 0.0
        scores = []
        for entry in artifact:
            key = (entry.get('Re'), entry.get('Os'))
            if key not in gold_table:
                continue
            gold = gold_table[key]
            for field in gold:
                if field not in entry:
                    continue
                tol = tolerances.get(field, {})
                atol = tol.get('atol', 0.0)
                rtol = tol.get('rtol', 0.0)
                agent_val = entry[field]
                gold_val = gold[field]
                if not math.isfinite(agent_val) or not math.isfinite(gold_val):
                    scores.append(0.0)
                    continue
                diff = abs(agent_val - gold_val)
                allowed = atol + rtol * abs(gold_val)
                scores.append(1.0 if diff <= allowed else 0.0)
        if not scores:
            return 0.0
        return sum(scores) / len(scores)


# === block: score_5 (check id='derived_properties_consistency') ===
def score_5(artifact, step, ctx):
    def score_derived_properties_consistency(artifact, step, ctx):
        if not isinstance(artifact, list):
            return 0.0
        relations = step.get('relations', [])
        total = 0
        count = 0
        for entry in artifact:
            cp = entry.get('cauchy_pressure_GPa')
            for rel in relations:
                if rel['name'] == 'cauchy_positive' and cp is not None:
                    if cp > 0:
                        total += 1.0
                    else:
                        total += 0.0
                    count += 1
        if count == 0:
            return 0.0
        return total / count


# === block: score_6 (check id='trends') ===
def score_6(artifact, step, ctx):
        import json as _json
        import os as _os

        # Load single_crystal_elastic_constants.json directly
        single_path = _os.path.join('/app/outputs', 'single_crystal_elastic_constants.json')
        single_artifact = []
        if _os.path.isfile(single_path):
            try:
                with open(single_path) as _f:
                    single_artifact = _json.load(_f)
            except Exception:  # noqa: BLE001
                single_artifact = []
        if not isinstance(single_artifact, list):
            single_artifact = []

        artifact_derived = artifact  # artifact passed to scorer is derived_properties.json
        if not isinstance(artifact_derived, list) or not isinstance(single_artifact, list):
            return 0.0

        def get_field(composition, field):
            # Search in both artifacts
            for art in [artifact_derived, single_artifact]:
                for entry in art:
                    if entry.get('Re') == composition[0] and entry.get('Os') == composition[1]:
                        if field in entry:
                            return entry[field]
            return None

        trend_defs = step.get('trend_definitions', [])
        scores = []
        for trend_def in trend_defs:
            fixed_elem = trend_def['fixed_element']
            fixed_val = trend_def['fixed_value']
            var_elem = trend_def['variable_element']
            values = trend_def['values']
            fields = trend_def['fields']
            # Build list of compositions
            comps = []
            for val in values:
                if fixed_elem == 'Re' and var_elem == 'Os':
                    comps.append((fixed_val, val))
                elif fixed_elem == 'Os' and var_elem == 'Re':
                    comps.append((val, fixed_val))
                else:
                    continue
            # For each field, check monotonicity
            for fdef in fields:
                field = fdef['field']
                direction = fdef['direction']
                vals = []
                for comp in comps:
                    v = get_field(comp, field)
                    if v is not None:
                        vals.append(v)
                if len(vals) < 2:
                    scores.append(0.0)
                    continue
                # Check monotonicity
                ok = True
                if direction == 'increasing':
                    for i in range(len(vals)-1):
                        if vals[i+1] < vals[i]:
                            ok = False
                            break
                elif direction == 'decreasing':
                    for i in range(len(vals)-1):
                        if vals[i+1] > vals[i]:
                            ok = False
                            break
                scores.append(1.0 if ok else 0.0)
        if not scores:
            return 0.0
        return sum(scores) / len(scores)


_SCORERS = {
    'single_crystal_constants_file_check': score_0,
    'single_crystal_constants_values': score_1,
    'single_crystal_constants_consistency': score_2,
    'derived_properties_file_check': score_3,
    'derived_properties_values': score_4,
    'derived_properties_consistency': score_5,
    'trends': score_6,
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
