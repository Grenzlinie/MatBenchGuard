import os
import json
import csv

# === author imports / helpers ===
import math


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


# === block: score_0 (check id='exchange_integrals_main') ===
def score_0(artifact, step, ctx):
    artifact_rows = artifact  # list of dicts
    gold = step.get("gold", {})

    if not artifact_rows:
        return 0.0

    agent_by_system = {}
    for row in artifact_rows:
        sys = row.get("system", "").strip()
        if not sys:
            continue
        row_clean = {}
        for k in ("t","J","J_kin","J_ind","J_eff","Delta_epsilon","U"):
            val = row.get(k, "").strip()
            if val == "":
                row_clean[k] = None
            else:
                try:
                    row_clean[k] = float(val)
                except:
                    row_clean[k] = None
        agent_by_system[sys] = row_clean

    system_scores = []
    for sys_name, gold_vals in gold.items():
        if sys_name not in agent_by_system:
            system_scores.append(0.0)
            continue
        agent = agent_by_system[sys_name]

        # magnitude
        mag_parts = []
        for field in ("t","J","J_kin","J_ind","J_eff","Delta_epsilon"):
            g = gold_vals.get(field)
            if g is not None:
                a = agent.get(field)
                if a is None:
                    mag_parts.append(0.0)
                else:
                    err = abs(a - g)
                    tol = max(0.005, 0.2 * abs(g))
                    mag_parts.append(1.0 if err <= tol else 0.0)
        if "U" in gold_vals and gold_vals["U"] is not None:
            gu = gold_vals["U"]
            au = agent.get("U")
            if au is None:
                mag_parts.append(0.0)
            else:
                err = abs(au - gu)
                tol = max(0.005, 0.2 * abs(gu))
                mag_parts.append(1.0 if err <= tol else 0.0)
        mag_score = sum(mag_parts) / len(mag_parts) if mag_parts else 0.0

        # trend
        trend_ok = True
        is_F = sys_name.endswith("-F")
        is_A = sys_name.endswith("-A")
        if sys_name == "W-W":
            is_A_like = True
            is_F_like = False
        elif sys_name == "W-Cor-W":
            is_A_like = False
            is_F_like = True
        else:
            is_A_like = is_A
            is_F_like = is_F

        if is_F_like:
            t_val = agent.get("t")
            jkin_val = agent.get("J_kin")
            jeff_val = agent.get("J_eff")
            if None in (t_val, jkin_val, jeff_val):
                trend_ok = False
            else:
                if not (jeff_val > 0 and abs(t_val) <= 0.005 and abs(jkin_val) <= 0.005):
                    trend_ok = False
        else:  # A-like
            jeff_val = agent.get("J_eff")
            if jeff_val is None:
                trend_ok = False
            else:
                if not (jeff_val < 0):
                    trend_ok = False

        # internal consistency for W systems
        if "U" in gold_vals and gold_vals["U"] is not None:
            t_val = agent.get("t")
            u_val = agent.get("U")
            jkin_rep = agent.get("J_kin")
            if None not in (t_val, u_val, jkin_rep):
                if u_val != 0:
                    expected = -2 * (t_val * t_val) / u_val
                    if abs(jkin_rep - expected) > 1e-4:
                        trend_ok = False
                else:
                    trend_ok = False
            else:
                trend_ok = False

        trend_score = 1.0 if trend_ok else 0.0
        sys_score = 0.7 * mag_score + 0.3 * trend_score
        system_scores.append(sys_score)

    overall = sum(system_scores) / len(system_scores) if system_scores else 0.0
    return overall


_SCORERS = {
    'exchange_integrals_main': score_0,
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
