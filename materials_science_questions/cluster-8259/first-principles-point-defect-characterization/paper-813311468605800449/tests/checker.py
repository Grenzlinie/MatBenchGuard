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
    k_B = 8.617333262145e-5
    T = 600.0
    kT = k_B * T
    tau_cs_gold = 0.01 * math.exp(0.57 / kT)
    tau_ri_gold = 0.15 * math.exp(0.30 / kT)
    # Expected analytic frequencies
    gold_freq = {
        'nu_O_core_shell_THz': 109.8,
        'nutilde_O_core_shell_cm-1': 3663.76,
        'nu_U_core_shell_THz': 133.6,
        'nutilde_U_core_shell_cm-1': 4457.39
    }
    return {
        'gold_freq': gold_freq,
        'tau_cs_gold': tau_cs_gold,
        'tau_ri_gold': tau_ri_gold,
        'factor': 2.0
    }


# === block: score_0 (check id='freq_check') ===
def score_0(artifact, step, ctx):
    expected = ctx['gold_freq']
    field_score = {}
    for key, exp_val in expected.items():
        val = artifact.get(key)
        if val is None:
            field_score[key] = 0.0
            continue
        tol = 0.01 if 'THz' in key else 0.1
        if abs(val - exp_val) <= tol:
            field_score[key] = 1.0
        else:
            field_score[key] = 0.0
    n = len(expected) if expected else 1
    score = sum(field_score.values()) / n
    return score


# === block: score_1 (check id='vacf_check') ===
def score_1(artifact, step, ctx):
    freq = artifact.get('highest_ionic_frequency_cm-1')
    if freq is None or freq > 800:
        return 0.0
    return 1.0


# === block: score_2 (check id='recomb_check') ===
def score_2(artifact, step, ctx):
    tau_cs = artifact.get('oxygen_rank5_tau_core_shell')
    tau_ri = artifact.get('oxygen_rank5_tau_rigid_ion')
    factor = ctx['factor']
    tau_cs_gold = ctx['tau_cs_gold']
    tau_ri_gold = ctx['tau_ri_gold']
    def passes(val, gold):
        return val >= 0.5 * gold and val <= factor * gold
    s = 0.0
    if passes(tau_cs, tau_cs_gold):
        s += 0.5
    if passes(tau_ri, tau_ri_gold):
        s += 0.5
    return s


_SCORERS = {
    'freq_check': score_0,
    'vacf_check': score_1,
    'recomb_check': score_2,
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
