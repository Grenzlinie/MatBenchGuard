import os
import json
import csv

# === author imports / helpers ===
import json
import math
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
        two_channel_gold = []
        three_channel_gold = []
        tolerance = 0.5
        for step in spec.get("steps", []):
            if step.get("id") == "sbc_efficiencies":
                cfg = step.get("config", {})
                tolerance = cfg.get("tolerance", 0.5)
                two_channel_gold = cfg.get("two_channel_gold", [])
                three_channel_gold = cfg.get("three_channel_gold", [])
                break
        return {
            "two_channel_gold": two_channel_gold,
            "three_channel_gold": three_channel_gold,
            "tolerance": tolerance,
        }


# === block: score_0 (check id='sbc_efficiencies') ===
def score_0(artifact, step, ctx):
        two_channel_gold = ctx["two_channel_gold"]
        three_channel_gold = ctx["three_channel_gold"]
        tolerance = ctx["tolerance"]
        # artifact is the loaded JSON dict (shape gate already passed)
        if not isinstance(artifact, dict):
            return 0.0
        tc = artifact.get("two_channel")
        thc = artifact.get("three_channel")
        if not isinstance(tc, list) or not isinstance(thc, list):
            return 0.0
        # Build lookup by w
        tc_dict = {}
        for entry in tc:
            if isinstance(entry, dict) and "w" in entry:
                tc_dict[entry["w"]] = entry
        thc_dict = {}
        for entry in thc:
            if isinstance(entry, dict) and "w" in entry:
                thc_dict[entry["w"]] = entry
    
        checks = []  # list of booleans
        # Check two-channel entries
        for gold in two_channel_gold:
            w = gold["w"]
            entry = tc_dict.get(w)
            if not entry:
                checks.append(False)
                continue
            for key in ["eta_T", "eta_D", "eta"]:
                val = entry.get(key)
                if val is None:
                    checks.append(False)
                else:
                    diff = abs(float(val) - float(gold[key]))
                    checks.append(diff <= tolerance)
            # consistency: recompute eta from eta_T and eta_D using Eq.5: eta = (eta_T * 0.985 + eta_D)/2
            try:
                eta_T = float(entry["eta_T"])
                eta_D = float(entry["eta_D"])
                eta_expected = (eta_T * 0.985 + eta_D) / 2.0
                eta_reported = float(entry["eta"])
                # small tolerance for arithmetic consistency
                checks.append(abs(eta_reported - eta_expected) <= 0.1)
            except Exception:
                checks.append(False)
        # Check three-channel entries
        for gold in three_channel_gold:
            w = gold["w"]
            entry = thc_dict.get(w)
            if not entry:
                checks.append(False)
                continue
            for key in ["eta_1D", "eta_2T_prime", "eta_1T", "eta_1T_prime", "eta_2D", "eta"]:
                val = entry.get(key)
                if val is None:
                    checks.append(False)
                else:
                    diff = abs(float(val) - float(gold[key]))
                    checks.append(diff <= tolerance)
            # consistency: recompute total eta using Eq.6
            # eta = (eta_2D + eta_1D * 0.985 * eta_2T_prime + eta_1T * 0.985 * 0.985 * eta_1T_prime) / 3
            try:
                eta_1D = float(entry["eta_1D"])
                eta_2Tp = float(entry["eta_2T_prime"])
                eta_1T = float(entry["eta_1T"])
                eta_1Tp = float(entry["eta_1T_prime"])
                eta_2D = float(entry["eta_2D"])
                eta_expected = (eta_2D + eta_1D * 0.985 * eta_2Tp + eta_1T * 0.985 * 0.985 * eta_1Tp) / 3.0
                eta_reported = float(entry["eta"])
                checks.append(abs(eta_reported - eta_expected) <= 0.15)
            except Exception:
                checks.append(False)
        if not checks:
            return 0.0
        return sum(checks) / len(checks)


_SCORERS = {
    'sbc_efficiencies': score_0,
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
