import os
import json
import csv

# === author imports / helpers ===
import csv
from collections import defaultdict


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


# === block: score_0 (check id='delta_GH_table') ===
def score_0(artifact, step, ctx):
    gold_rows = step.get("gold_values", [])
    if not gold_rows:
        return 0.0
    tol_dg = step.get("tolerances", {}).get("DeltaG_H", 0.05)
    tol_charge = step.get("tolerances", {}).get("ChargeTransfer", 0.01)
    agent = {}
    if not artifact:
        return 0.0
    for row in artifact:
        sys = str(row.get("System", "")).strip().lower()
        cov = str(row.get("Coverage", "")).strip().lower()
        site = str(row.get("ActiveSite", "")).strip().upper()
        try:
            dg = float(row.get("DeltaG_H", None))
            ct = float(row.get("ChargeTransfer", None))
        except (TypeError, ValueError):
            continue
        agent[(sys, cov, site)] = (dg, ct)
    row_scores = []
    for g in gold_rows:
        key = (g["System"].strip().lower(), g["Coverage"].strip().lower(), g["ActiveSite"].strip().upper())
        dg_gold = g["DeltaG_H"]
        ct_gold = g["ChargeTransfer"]
        agent_tuple = agent.get(key)
        if agent_tuple is None:
            row_scores.append(0.0)
            continue
        dg_agent, ct_agent = agent_tuple
        dg_ok = 1.0 if abs(dg_agent - dg_gold) <= tol_dg else 0.0
        ct_ok = 1.0 if abs(ct_agent - ct_gold) <= tol_charge else 0.0
        row_score = 0.7 * dg_ok + 0.3 * ct_ok
        row_scores.append(row_score)
    if not row_scores:
        return 0.0
    return sum(row_scores) / len(row_scores)


# === block: score_1 (check id='strain_dependence') ===
def score_1(artifact, step, ctx):
        tol = step.get("tolerances", {}).get("DeltaG_H", 0.05)
        expected_unstrained = {
            "t0(12.5% co)": -0.23,
            "t1(12.5% fe)": -0.16,
            "t2(12.5% co)": -0.03,
            "t3(25% ni)":   -0.01,
            "t3(25% co)":   0.10,
        }
        zero_points = {
            ("t2(12.5% co)", -0.005): 0.0,
            ("t3(25% ni)", -0.0027): 0.0,
        }
        allow_one_inversion = step.get("allow_one_inversion", True)

        if not artifact:
            return 0.0
        agent_data = {}
        for row in artifact:
            sys = str(row.get("System", "")).strip().lower()
            strain = None
            dg = None
            try:
                strain = float(row.get("Strain", None))
                dg = float(row.get("DeltaG_H", None))
            except (TypeError, ValueError):
                continue
            if sys and strain is not None and dg is not None:
                agent_data[(sys, strain)] = dg

        unstrained_ok = 0
        for sys_key, gold_val in expected_unstrained.items():
            val = agent_data.get((sys_key, 0.0))
            if val is not None and abs(val - gold_val) <= tol:
                unstrained_ok += 1
        unstrained_score = unstrained_ok / len(expected_unstrained)

        zero_ok = 0
        for (sys_key, strain_val), gold_val in zero_points.items():
            val = agent_data.get((sys_key, strain_val))
            if val is None:
                for (s2, s), v in agent_data.items():
                    if s2 == sys_key and abs(s - strain_val) < 1e-4:
                        val = v
                        break
            if val is not None and abs(val - gold_val) <= tol:
                zero_ok += 1
        zero_score = zero_ok / len(zero_points) if zero_points else 0.0

        systems = defaultdict(list)
        for (sys, strain), dg in agent_data.items():
            if sys in expected_unstrained:
                systems[sys].append((strain, dg))
        monotonic_fail = 0
        for pts in systems.values():
            pts_sorted = sorted(pts, key=lambda x: x[0])
            values = [p[1] for p in pts_sorted]
            inversions = 0
            for i in range(len(values)-1):
                if values[i+1] > values[i]:
                    inversions += 1
            if inversions > (1 if allow_one_inversion else 0):
                monotonic_fail += 1
        monotonic_score = 1.0 if monotonic_fail == 0 else 0.0

        return 0.5 * unstrained_score + 0.3 * zero_score + 0.2 * monotonic_score


_SCORERS = {
    'delta_GH_table': score_0,
    'strain_dependence': score_1,
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
