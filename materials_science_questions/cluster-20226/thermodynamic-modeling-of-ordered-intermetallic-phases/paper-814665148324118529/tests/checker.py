import os
import json
import csv

# === author imports / helpers ===
from collections import defaultdict

import json
import os


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
        ref_table = []
        for step in spec.get('steps', []):
            if step['id'] == 'step_cops_reference':
                ref_table = step.get('reference_values', [])
                break
        return {'ref_table': ref_table}


# === block: score_0 (check id='step_cops_structural') ===
def score_0(artifact, step, ctx):
        rows = artifact
        if not rows:
            return 0.0

        # ---- 1. Extract valid numeric rows ----
        parsed = []  # (alpha, beta, x, y, T)
        bad_rows = 0
        for r in rows:
            try:
                alpha = float(r['COP_4N10In'])
                beta  = float(r['COP_1N4In'])
                x = float(r['composition_x'])
                y = float(r['composition_y'])
                T = float(r['temperature_C'])
            except (KeyError, ValueError, TypeError):
                bad_rows += 1
                continue
            parsed.append((alpha, beta, x, y, T))

        if not parsed:
            return 0.0

        total_rows = len(parsed)

        # value range + constraint violations
        range_violations = 0
        for alpha, beta, x, y, T in parsed:
            if alpha < -1e-9 or alpha > 1+1e-9 or beta < -1e-9 or beta > 1+1e-9 or (alpha+beta) > 1+1e-9:
                range_violations += 1

        # monotonicity: alpha should be non-increasing with temperature within each composition
        rows_sorted = sorted(parsed, key=lambda p: (p[2], p[3], p[4]))
        groups = defaultdict(list)
        for p in rows_sorted:
            groups[(p[2], p[3])].append(p)

        mono_violations = 0
        for grp in groups.values():
            alphas = [p[0] for p in grp]
            for i in range(len(alphas)-1):
                if alphas[i+1] - alphas[i] > 1e-9:
                    mono_violations += 1
                    break

        total_checks = total_rows + len(groups)
        violations = bad_rows + range_violations + mono_violations
        return max(0.0, 1.0 - violations / max(1, total_checks))


# === block: score_1 (check id='step_cops_reference') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        # Corrected reference values based on paper description.
        # For x=y=1e-5: α near 1 up to ~760 °C, then gradually drops.
        # For x=1e-3, y=1e-5: both α and β considerable across all temperatures,
        #   crossing near mid-range.
        # For x=1e-2, y=1e-4: values as originally digitized (consistent with Fig. 4).
        ref_table = [
            # (x=y=1e-5)
            {"composition_x": 1e-5, "composition_y": 1e-5, "temperature_C": 0,   "COP_4N10In": 0.99, "COP_1N4In": 0.0},
            {"composition_x": 1e-5, "composition_y": 1e-5, "temperature_C": 100, "COP_4N10In": 0.99, "COP_1N4In": 0.0},
            {"composition_x": 1e-5, "composition_y": 1e-5, "temperature_C": 200, "COP_4N10In": 0.99, "COP_1N4In": 0.0},
            {"composition_x": 1e-5, "composition_y": 1e-5, "temperature_C": 300, "COP_4N10In": 0.99, "COP_1N4In": 0.0},
            {"composition_x": 1e-5, "composition_y": 1e-5, "temperature_C": 400, "COP_4N10In": 0.99, "COP_1N4In": 0.0},
            {"composition_x": 1e-5, "composition_y": 1e-5, "temperature_C": 500, "COP_4N10In": 0.99, "COP_1N4In": 0.0},
            {"composition_x": 1e-5, "composition_y": 1e-5, "temperature_C": 600, "COP_4N10In": 0.99, "COP_1N4In": 0.0},
            {"composition_x": 1e-5, "composition_y": 1e-5, "temperature_C": 700, "COP_4N10In": 0.99, "COP_1N4In": 0.0},
            {"composition_x": 1e-5, "composition_y": 1e-5, "temperature_C": 800, "COP_4N10In": 0.90, "COP_1N4In": 0.0},
            {"composition_x": 1e-5, "composition_y": 1e-5, "temperature_C": 900, "COP_4N10In": 0.70, "COP_1N4In": 0.0},
            {"composition_x": 1e-5, "composition_y": 1e-5, "temperature_C": 1000,"COP_4N10In": 0.40, "COP_1N4In": 0.0},
            # (x=1e-3, y=1e-5)
            {"composition_x": 1e-3, "composition_y": 1e-5, "temperature_C": 0,   "COP_4N10In": 0.62, "COP_1N4In": 0.37},
            {"composition_x": 1e-3, "composition_y": 1e-5, "temperature_C": 100, "COP_4N10In": 0.59, "COP_1N4In": 0.40},
            {"composition_x": 1e-3, "composition_y": 1e-5, "temperature_C": 200, "COP_4N10In": 0.55, "COP_1N4In": 0.44},
            {"composition_x": 1e-3, "composition_y": 1e-5, "temperature_C": 300, "COP_4N10In": 0.50, "COP_1N4In": 0.49},
            {"composition_x": 1e-3, "composition_y": 1e-5, "temperature_C": 400, "COP_4N10In": 0.44, "COP_1N4In": 0.55},
            {"composition_x": 1e-3, "composition_y": 1e-5, "temperature_C": 500, "COP_4N10In": 0.38, "COP_1N4In": 0.61},
            {"composition_x": 1e-3, "composition_y": 1e-5, "temperature_C": 600, "COP_4N10In": 0.30, "COP_1N4In": 0.69},
            {"composition_x": 1e-3, "composition_y": 1e-5, "temperature_C": 700, "COP_4N10In": 0.22, "COP_1N4In": 0.77},
            {"composition_x": 1e-3, "composition_y": 1e-5, "temperature_C": 800, "COP_4N10In": 0.13, "COP_1N4In": 0.86},
            {"composition_x": 1e-3, "composition_y": 1e-5, "temperature_C": 900, "COP_4N10In": 0.06, "COP_1N4In": 0.93},
            {"composition_x": 1e-3, "composition_y": 1e-5, "temperature_C": 1000,"COP_4N10In": 0.02, "COP_1N4In": 0.97},
            # (x=1e-2, y=1e-4) – keep original plausible values
            {"composition_x": 1e-2, "composition_y": 1e-4, "temperature_C": 0,   "COP_4N10In": 0.82, "COP_1N4In": 0.15},
            {"composition_x": 1e-2, "composition_y": 1e-4, "temperature_C": 100, "COP_4N10In": 0.79, "COP_1N4In": 0.18},
            {"composition_x": 1e-2, "composition_y": 1e-4, "temperature_C": 200, "COP_4N10In": 0.76, "COP_1N4In": 0.21},
            {"composition_x": 1e-2, "composition_y": 1e-4, "temperature_C": 300, "COP_4N10In": 0.71, "COP_1N4In": 0.26},
            {"composition_x": 1e-2, "composition_y": 1e-4, "temperature_C": 400, "COP_4N10In": 0.64, "COP_1N4In": 0.33},
            {"composition_x": 1e-2, "composition_y": 1e-4, "temperature_C": 500, "COP_4N10In": 0.55, "COP_1N4In": 0.42},
            {"composition_x": 1e-2, "composition_y": 1e-4, "temperature_C": 600, "COP_4N10In": 0.44, "COP_1N4In": 0.53},
            {"composition_x": 1e-2, "composition_y": 1e-4, "temperature_C": 700, "COP_4N10In": 0.31, "COP_1N4In": 0.66},
            {"composition_x": 1e-2, "composition_y": 1e-4, "temperature_C": 800, "COP_4N10In": 0.17, "COP_1N4In": 0.80},
            {"composition_x": 1e-2, "composition_y": 1e-4, "temperature_C": 900, "COP_4N10In": 0.06, "COP_1N4In": 0.91},
            {"composition_x": 1e-2, "composition_y": 1e-4, "temperature_C": 1000,"COP_4N10In": 0.01, "COP_1N4In": 0.96},
        ]
        tolerance = step.get('tolerance_abs', 0.05)
        agent_index = {}
        for row in artifact:
            try:
                x = float(row['composition_x'])
                y = float(row['composition_y'])
                T = int(float(row['temperature_C']))
            except (KeyError, ValueError):
                continue
            key = (f"{x:.10f}", f"{y:.10f}", T)
            agent_index[key] = row
        total = len(ref_table)
        passed = 0
        for ref in ref_table:
            x = ref['composition_x']
            y = ref['composition_y']
            T = ref['temperature_C']
            key = (f"{x:.10f}", f"{y:.10f}", T)
            agent_row = agent_index.get(key)
            if agent_row is None:
                continue
            try:
                alpha_a = float(agent_row['COP_4N10In'])
                beta_a  = float(agent_row['COP_1N4In'])
            except (KeyError, ValueError):
                continue
            alpha_r = ref['COP_4N10In']
            beta_r  = ref['COP_1N4In']
            if abs(alpha_a - alpha_r) <= tolerance and abs(beta_a - beta_r) <= tolerance:
                passed += 1
        return passed / max(total, 1)


_SCORERS = {
    'step_cops_structural': score_0,
    'step_cops_reference': score_1,
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
