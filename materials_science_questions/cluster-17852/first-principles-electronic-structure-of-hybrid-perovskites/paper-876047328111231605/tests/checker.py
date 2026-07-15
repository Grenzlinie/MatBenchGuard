import os
import json
import csv

# === author imports / helpers ===
import json
from typing import Any, Dict, List


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


# === block: score_0 (check id='step06_compile_results') ===
def score_0(artifact, step, ctx):
        gold_compounds = step["gold"]["compounds"]
        tolerances = step["gold"]["tolerances"]
        if not isinstance(artifact, dict) or "compounds" not in artifact:
            return 0.0
        agent_compounds = {}  
        for c in artifact["compounds"]:
            name = c.get("name", "")
            agent_compounds[name] = c
        total = 0.0
        for gc in gold_compounds:
            name = gc["name"]
            w = gc["weight"]
            if name not in agent_compounds:
                continue  # missing compound scores 0
            ac = agent_compounds[name]
            sub_scores = []
            # band_gap_eV
            if "band_gap_eV" in gc:
                val = ac.get("band_gap_eV")
                if isinstance(val, (int, float)):
                    diff = abs(val - gc["band_gap_eV"])
                    tol = tolerances["band_gap_eV"]
                    sub_scores.append(1.0 if diff <= tol else max(0.0, 1.0 - (diff - tol) / (3.0*tol)))
                else:
                    sub_scores.append(0.0)
            # gap_type
            if "gap_type" in gc:
                sub_scores.append(1.0 if ac.get("gap_type") == gc["gap_type"] else 0.0)
            # cbm_kpoint
            if "cbm_kpoint" in gc:
                sub_scores.append(1.0 if ac.get("cbm_kpoint") == gc["cbm_kpoint"] else 0.0)
            # vbm_kpoint
            if "vbm_kpoint" in gc:
                sub_scores.append(1.0 if ac.get("vbm_kpoint") == gc["vbm_kpoint"] else 0.0)
            # formation_energy
            if "formation_energy_kJ_per_mol" in gc:
                val = ac.get("formation_energy_kJ_per_mol")
                if isinstance(val, (int, float)):
                    diff = abs(val - gc["formation_energy_kJ_per_mol"])
                    tol = tolerances["formation_energy_kJ_per_mol"]
                    sub_scores.append(1.0 if diff <= tol else max(0.0, 1.0 - (diff - tol) / (3.0*tol)))
                else:
                    sub_scores.append(0.0)
            # optical fields for I compound
            if "dielectric_constant_zero_freq" in gc:
                val = ac.get("dielectric_constant_zero_freq")
                if isinstance(val, (int, float)):
                    diff = abs(val - gc["dielectric_constant_zero_freq"])
                    tol = tolerances["dielectric_constant_zero_freq"]
                    sub_scores.append(1.0 if diff <= tol else max(0.0, 1.0 - (diff - tol) / (5.0*tol)))
                else:
                    sub_scores.append(0.0)
            if "max_refractive_index" in gc:
                val = ac.get("max_refractive_index")
                if isinstance(val, (int, float)):
                    diff = abs(val - gc["max_refractive_index"])
                    tol = tolerances["max_refractive_index"]
                    sub_scores.append(1.0 if diff <= tol else max(0.0, 1.0 - (diff - tol) / (5.0*tol)))
                else:
                    sub_scores.append(0.0)
            if "absorption_coefficient_order" in gc:
                sub_scores.append(1.0 if ac.get("absorption_coefficient_order") == gc["absorption_coefficient_order"] else 0.0)
            if sub_scores:
                total += w * (sum(sub_scores) / len(sub_scores))
        return total


_SCORERS = {
    'step06_compile_results': score_0,
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
