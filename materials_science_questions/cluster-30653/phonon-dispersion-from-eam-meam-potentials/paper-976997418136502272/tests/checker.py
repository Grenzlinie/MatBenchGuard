import os
import json
import csv

# === author imports / helpers ===
import math
from typing import Dict, Any


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
        steps_info = {}
        for step in spec.get('steps', []):
            sid = step.get('id')
            if sid:
                steps_info[sid] = {
                    'gold': step.get('gold', {}),
                    'tolerances': step.get('tolerances', {})
                }
        return {'steps_info': steps_info}


# === block: score_0 (check id='validation') ===
def score_0(artifact, step, ctx):
    def score_val(artifact, step, ctx):
        gold = ctx['steps_info']['validation']['gold']
        tol = ctx['steps_info']['validation']['tolerances']
        try:
            elastic = artifact.get('elastic_constants', {})
            pe = artifact.get('phonon_peaks', {})

            # Score elastic constants
            def rel_err(a, g):
                return abs(a - g) / max(abs(g), 1e-9)

            elastic_sub = 0
            elastic_items = 0
            for elem in ['Al_fcc', 'Li_bcc']:
                gelem = gold.get('elastic_constants', {}).get(elem, {})
                aelem = elastic.get(elem, {})
                for key in ['C11', 'C12', 'C44']:
                    if key in gelem and key in aelem:
                        err = rel_err(aelem[key], gelem[key])
                        rel_tol = tol.get('elastic_relative', 0.2)
                        s = 1.0 if err <= rel_tol else max(0.0, 1.0 - (err - rel_tol) / rel_tol)
                        elastic_sub += s
                        elastic_items += 1
            if elastic_items == 0:
                elastic_score = 0.0
            else:
                elastic_score = elastic_sub / elastic_items

            # Score phonon peaks
            phonon_sub = 0
            phonon_items = 0
            gphon = gold.get('phonon_peaks', {})
            for mat in ['fcc_Al', 'bcc_Li', 'AlLi', 'Al3Li']:
                gpeaks = gphon.get(mat, [])
                apeaks = pe.get(mat, [])
                if len(apeaks) != len(gpeaks):
                    phonon_sub += 0.0
                    phonon_items += len(gpeaks)
                else:
                    for i in range(len(gpeaks)):
                        diff = abs(apeaks[i] - gpeaks[i])
                        abs_tol = tol.get('phonon_abs', 1.0)
                        s = 1.0 if diff <= abs_tol else max(0.0, 1.0 - (diff - abs_tol) / abs_tol)
                        phonon_sub += s
                        phonon_items += 1
            if phonon_items == 0:
                phonon_score = 0.0
            else:
                phonon_score = phonon_sub / phonon_items

            return 0.5 * elastic_score + 0.5 * phonon_score
        except Exception:
            return 0.0


# === block: score_1 (check id='phase_diagram') ===
def score_1(artifact, step, ctx):
    def score_pd(artifact, step, ctx):
        gold = ctx['steps_info']['phase_diagram']['gold']
        tol = ctx['steps_info']['phase_diagram']['tolerances']
        try:
            eut_t = artifact.get('eutectic_temperature_K')
            eut_c = artifact.get('eutectic_composition_Li_fraction')
            sol = artifact.get('Li_solubility_in_fcc_Al_fraction')
            if eut_t is None or eut_c is None or sol is None:
                return 0.0
            # temperature
            diff_t = abs(eut_t - gold['eutectic_temperature_K'])
            ttol = tol.get('temperature_abs', 50.0)
            s_t = 1.0 if diff_t <= ttol else max(0.0, 1.0 - (diff_t - ttol) / ttol)
            # composition
            diff_c = abs(eut_c - gold['eutectic_composition_Li_fraction'])
            ctol = tol.get('composition_abs', 0.05)
            s_c = 1.0 if diff_c <= ctol else max(0.0, 1.0 - (diff_c - ctol) / ctol)
            # solubility
            diff_s = abs(sol - gold['Li_solubility_in_fcc_Al_fraction'])
            stol = tol.get('solubility_abs', 0.05)
            s_s = 1.0 if diff_s <= stol else max(0.0, 1.0 - (diff_s - stol) / stol)
            return (s_t + s_c + s_s) / 3.0
        except Exception:
            return 0.0


_SCORERS = {
    'validation': score_0,
    'phase_diagram': score_1,
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
