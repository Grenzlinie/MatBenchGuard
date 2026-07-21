import os
import json
import csv

# === author imports / helpers ===
import csv, os, math


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


# === block: score_0 (check id='uv_phase_diagram') ===
def score_0(artifact, step, ctx):
    artifact_csv = artifact  # list of dicts from csv.DictReader
    lookup = {}
    for row in artifact_csv:
        try:
            u = float(row['U'])
            v = float(row['V'])
            lookup[(u,v)] = row
        except (ValueError, KeyError):
            continue

    # Sub-conditions (each worth 0.25)
    checks = []

    # U=8.4, V=4: CO dominant
    row1 = lookup.get((8.4, 4.0))
    if row1:
        co1 = float(row1.get('CO_pi_pi_pi', 0))
        s1  = float(row1.get('S_pi_pi_pi', 0))
        checks.append(co1 > 0.05 and s1 < 0.01)
        dos1 = float(row1.get('DOS0', 100))
        rho1 = float(row1.get('resistivity', 0))
        checks.append(dos1 < 0.05 and rho1 > 1)
    else:
        checks.extend([False, False])

    # U=8.5, V=4: AF dominant
    row2 = lookup.get((8.5, 4.0))
    if row2:
        s2  = float(row2.get('S_pi_pi_pi', 0))
        co2 = float(row2.get('CO_pi_pi_pi', 0))
        checks.append(s2 > 0.05 and co2 < 0.01)
        dos2 = float(row2.get('DOS0', 100))
        rho2 = float(row2.get('resistivity', 0))
        checks.append(dos2 < 0.05 and rho2 > 1)
    else:
        checks.extend([False, False])

    if not checks:
        return 0.0
    score = sum(1 for c in checks if c) / len(checks)
    return score


# === block: score_1 (check id='vt_phase_diagram') ===
def score_1(artifact, step, ctx):
    artifact_csv = artifact  # list of dicts
    lookup = {}
    for row in artifact_csv:
        try:
            v = float(row['V'])
            t = float(row['T'])
            lookup[(v, t)] = row
        except (ValueError, KeyError):
            continue

    checks = []

    # ---- Point 1: V=3.7, T=0.005 -> AF insulating
    row_af = lookup.get((3.7, 0.005))
    if row_af:
        s_af = float(row_af.get('S_pi_pi_pi', 0))
        co_af = float(row_af.get('CO_pi_pi_pi', 0))
        checks.append(s_af > 0.05 and co_af < 0.01)
        checks.append(float(row_af.get('DOS0', 100)) < 0.05 and float(row_af.get('resistivity', 0)) > 1)
    else:
        checks.extend([False, False])

    # ---- Point 2: V=3.8, T=0.005 -> CO insulating
    row_co = lookup.get((3.8, 0.005))
    if row_co:
        co2 = float(row_co.get('CO_pi_pi_pi', 0))
        s2 = float(row_co.get('S_pi_pi_pi', 0))
        checks.append(co2 > 0.05 and s2 < 0.01)
        checks.append(float(row_co.get('DOS0', 100)) < 0.05 and float(row_co.get('resistivity', 0)) > 1)
    else:
        checks.extend([False, False])

    # ---- Point 3: V=3.7, T=0.25 -> metallic
    row_met1 = lookup.get((3.7, 0.25))
    if row_met1:
        checks.append(float(row_met1.get('DOS0', 0)) > 0.1 and float(row_met1.get('resistivity', 100)) < 0.5)
    else:
        checks.append(False)

    # ---- Point 4: V=3.8, T=0.25 -> metallic
    row_met2 = lookup.get((3.8, 0.25))
    if row_met2:
        checks.append(float(row_met2.get('DOS0', 0)) > 0.1 and float(row_met2.get('resistivity', 100)) < 0.5)
    else:
        checks.append(False)

    # ---- BPO trend for V=3.7 (BP-M*): decreases with cooling
    bp_rows_37 = [row for (v,t), row in lookup.items() if abs(v-3.7)<1e-9 and t in (0.005, 1.0)]
    bpo_37 = {}
    for r in bp_rows_37:
        t = float(r['T'])
        bpo_37[t] = float(r.get('bipolaronic_order_parameter', 0.5))
    if 0.005 in bpo_37 and 1.0 in bpo_37:
        checks.append(bpo_37[0.005] < bpo_37[1.0])
    else:
        checks.append(False)

    # ---- BPO trend for V=3.8 (BP-M): increases with cooling
    bp_rows_38 = [row for (v,t), row in lookup.items() if abs(v-3.8)<1e-9 and t in (0.005, 0.25)]
    bpo_38 = {}
    for r in bp_rows_38:
        t = float(r['T'])
        bpo_38[t] = float(r.get('bipolaronic_order_parameter', 0.5))
    if 0.005 in bpo_38 and 0.25 in bpo_38:
        checks.append(bpo_38[0.005] > bpo_38[0.25])
    else:
        checks.append(False)

    if not checks:
        return 0.0
    score = sum(1 for c in checks if c) / len(checks)
    return score


_SCORERS = {
    'uv_phase_diagram': score_0,
    'vt_phase_diagram': score_1,
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
