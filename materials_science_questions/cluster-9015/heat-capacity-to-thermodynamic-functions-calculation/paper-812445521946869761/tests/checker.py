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
    ctx = {'compounds': spec['steps'][0]['compounds']}
    return ctx


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    compounds_spec = ctx['compounds']
    tol_Cpm = step.get('tolerances', {}).get('Cpm_298', 0.5)
    tol_Sm = step.get('tolerances', {}).get('Sm_298', 1.0)

    def compute_expected(comp):
        T1 = comp['T1']; T2 = comp['T2']
        # entropy from 0 to T1
        A1 = comp['A1']; B1 = comp['B1']
        S1 = A1 * T1 + B1 * T1**3 / 3.0
        # T1 to T2
        A2 = comp['A2']; B2 = comp['B2']; C2 = comp['C2']; D2 = comp['D2']
        def _int2(t):
            return A2 * math.log(t) + B2 * t + C2 * t * t / 2.0 - D2 / (2.0 * t * t)
        S2 = _int2(T2) - _int2(T1)
        # T2 to 298.15
        A3 = comp['A3']; B3 = comp['B3']; C3 = comp['C3']; D3 = comp['D3']
        def _int3(t):
            return A3 * math.log(t) + B3 * t + C3 * t * t / 2.0 - D3 / (2.0 * t * t)
        S3 = _int3(298.15) - _int3(T2)
        Sm = S1 + S2 + S3
        # Cpm at 298.15
        A4 = comp['A4']; B4 = comp['B4']; C4 = comp['C4']
        Cpm = A4 + B4 * 298.15 + C4 / (298.15**2)
        return Sm, Cpm

    agent_by_name = {}
    for entry in artifact:
        name = entry.get('compound')
        if name:
            agent_by_name[name] = entry

    total = 0.0
    n = len(compounds_spec)
    for comp in compounds_spec:
        name = comp['name']
        agent_entry = agent_by_name.get(name)
        if agent_entry is None:
            total += 0.0
            continue
        Sm_exp, Cpm_exp = compute_expected(comp)
        agent_Cpm = agent_entry.get('Cpm_298')
        agent_Sm = agent_entry.get('Sm_298')
        cpm_ok = isinstance(agent_Cpm, (int, float)) and abs(agent_Cpm - Cpm_exp) <= tol_Cpm
        sm_ok = isinstance(agent_Sm, (int, float)) and abs(agent_Sm - Sm_exp) <= tol_Sm
        total += (cpm_ok + sm_ok) / 2.0
    return total / n


_SCORERS = {
    'step_01': score_0,
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
