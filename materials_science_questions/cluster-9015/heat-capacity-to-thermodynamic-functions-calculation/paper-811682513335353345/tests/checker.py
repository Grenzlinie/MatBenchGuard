import os
import json
import csv

# === author imports / helpers ===
import sys
import subprocess
try:
    import numpy as np
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "numpy"])
    import numpy as np
import csv
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
        checks = spec.get("checks", [])
        gold_data = {}
        for check in checks:
            if check.get("id") != "step_01":
                continue
            config = check.get("config", {})
            phases = config.get("phases", {})
            for phase, pdata in phases.items():
                temps_raw = pdata["temperatures"]
                temps = np.array(sorted(temps_raw))
                c = pdata["coeffs"]
                a0, a1, a2, a3, a4 = c["a0"], c["a1"], c["a2"], c["a3"], c["a4"]
                Cp = a0 + a1 * temps + a2 * temps**2 + a3 * temps**(-0.5) + a4 * temps**(-2)
                H = np.zeros_like(temps)
                S = np.zeros_like(temps)
                for i in range(1, len(temps)):
                    dt = temps[i] - temps[i-1]
                    H[i] = H[i-1] + 0.5 * (Cp[i-1] + Cp[i]) * dt
                    S[i] = S[i-1] + 0.5 * (Cp[i-1]/temps[i-1] + Cp[i]/temps[i]) * dt
                phase_dict = {}
                for i in range(len(temps)):
                    key = round(float(temps[i]), 5)
                    phase_dict[key] = {
                        "Cp_J_mol_K": Cp[i],
                        "H_diff_J_mol": H[i],
                        "S_diff_J_mol_K": S[i]
                    }
                gold_data[phase] = phase_dict
            break
        return {"gold_data": gold_data}


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
        config = step.get("config", {})
        tollist = config.get("tolerances", {})
        phases = config.get("phases", {})
    
        # Compute gold values on the fly in pure Python (no numpy dependency)
        gold_data = {}
        for phase, pdata in phases.items():
            temps_raw = pdata["temperatures"]
            temps = sorted(temps_raw)
            c = pdata["coeffs"]
            a0, a1, a2, a3, a4 = c["a0"], c["a1"], c["a2"], c["a3"], c["a4"]
            n = len(temps)
            Cp = [0.0] * n
            H = [0.0] * n
            S = [0.0] * n
            for i in range(n):
                t = temps[i]
                Cp[i] = a0 + a1 * t + a2 * t**2 + a3 * t**(-0.5) + a4 * t**(-2)
            for i in range(1, n):
                dt = temps[i] - temps[i-1]
                H[i] = H[i-1] + 0.5 * (Cp[i-1] + Cp[i]) * dt
                S[i] = S[i-1] + 0.5 * (Cp[i-1]/temps[i-1] + Cp[i]/temps[i]) * dt
            phase_dict = {}
            for i in range(n):
                key = round(float(temps[i]), 5)
                phase_dict[key] = {
                    "Cp_J_mol_K": Cp[i],
                    "H_diff_J_mol": H[i],
                    "S_diff_J_mol_K": S[i]
                }
            gold_data[phase] = phase_dict
    
        if not isinstance(artifact, list) or not artifact:
            return 0.0
        cols = config.get("columns", [])
        if not all(c in artifact[0] for c in cols):
            return 0.0
        total = 0
        correct = 0
        for row in artifact:
            phase = row.get("Phase", "").strip()
            try:
                T = float(row["T_K"])
            except Exception:
                continue
            if phase not in gold_data:
                continue
            T_key = round(T, 5)
            gold = gold_data[phase].get(T_key)
            if gold is None:
                continue
            ok = True
            for col in ["Cp_J_mol_K", "H_diff_J_mol", "S_diff_J_mol_K"]:
                try:
                    val = float(row[col])
                except Exception:
                    ok = False
                    break
                if abs(val - gold[col]) > tollist.get(col, 1e9):
                    ok = False
                    break
            total += 1
            if ok:
                correct += 1
        if total == 0:
            return 0.0
        return correct / total


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
