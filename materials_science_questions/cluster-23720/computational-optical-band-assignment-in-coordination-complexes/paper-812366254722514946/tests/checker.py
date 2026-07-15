import os
import json
import csv

# === author imports / helpers ===
import json
import math
import unicodedata


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
            # map superscript/subscript digits to ASCII, and normalize arrows
            sup_map = str.maketrans(
                {
                    '\u2070': '0', '\u00b9': '1', '\u00b2': '2', '\u00b3': '3',
                    '\u2074': '4', '\u2075': '5', '\u2076': '6', '\u2077': '7',
                    '\u2078': '8', '\u2079': '9',
                    '\u2080': '0', '\u2081': '1', '\u2082': '2', '\u2083': '3',
                    '\u2084': '4', '\u2085': '5', '\u2086': '6', '\u2087': '7',
                    '\u2088': '8', '\u2089': '9',
                }
            )
            def normalize_transition(s):
                """Normalize Unicode superscripts/digits and arrows."""
                if not isinstance(s, str):
                    return str(s)
                s = unicodedata.normalize('NFC', s)
                s = s.translate(sup_map)
                # normalize arrow variants to '→'
                s = s.replace('->', '→').replace('\u2794', '→').replace('\u27a1', '→').replace('\u2b62', '→').replace('\u2192', '→')
                return s
            return {"normalize_transition": normalize_transition}
        


# === block: score_0 (check id='osc_strengths_odd_vib') ===
def score_0(artifact, step, ctx):
            gold = step.get('gold', [])
            tols = step.get('tolerances', {}).get('oscillator_strength', {})
            rel_tol = tols.get('rel', 0.01)
            abs_tol = tols.get('abs', 0.01e-07)
            if not isinstance(artifact, list) or not gold:
                return 0.0
            normalize = ctx.get('normalize_transition', lambda x: x)
            correct = 0
            for g in gold:
                g_trans = normalize(g['transition'])
                g_mode = g.get('vibration_mode', '')
                matched = False
                for entry in artifact:
                    a_trans = normalize(entry.get('transition', ''))
                    a_mode = entry.get('vibration_mode', '')
                    if a_trans == g_trans and a_mode == g_mode:
                        val = entry.get('oscillator_strength')
                        if val is None:
                            break
                        gold_val = g['oscillator_strength']
                        if abs(val - gold_val) <= abs_tol or (abs(gold_val) > 1e-30 and abs(val - gold_val) / abs(gold_val) <= rel_tol):
                            correct += 1
                        matched = True
                        break
                if not matched:
                    pass  # missing entry counts as incorrect
            return correct / len(gold) if gold else 0.0
        


# === block: score_1 (check id='osc_strengths_odd_cf') ===
def score_1(artifact, step, ctx):
            gold = step.get('gold', [])
            tols = step.get('tolerances', {}).get('oscillator_strength', {})
            rel_tol = tols.get('rel', 0.01)
            abs_tol = tols.get('abs', 0.01e-07)
            if not isinstance(artifact, list) or not gold:
                return 0.0
            normalize = ctx.get('normalize_transition', lambda x: x)
            correct = 0
            for g in gold:
                g_trans = normalize(g['transition'])
                g_pol = g.get('polarization', '')
                for entry in artifact:
                    a_trans = normalize(entry.get('transition', ''))
                    a_pol = entry.get('polarization', '')
                    if a_trans == g_trans and a_pol == g_pol:
                        val = entry.get('oscillator_strength')
                        if val is None:
                            break
                        gold_val = g['oscillator_strength']
                        if abs(val - gold_val) <= abs_tol or (abs(gold_val) > 1e-30 and abs(val - gold_val) / abs(gold_val) <= rel_tol):
                            correct += 1
                        break
            return correct / len(gold) if gold else 0.0
        


# === block: score_2 (check id='faraday_odd_vib') ===
def score_2(artifact, step, ctx):
            gold = step.get('gold', [])
            field_tols = step.get('tolerances', {})
            if not isinstance(artifact, list) or not gold:
                return 0.0
            normalize = ctx.get('normalize_transition', lambda x: x)
            correct = 0
            fields = ['A', 'B', 'C', 'B_plus_C_over_kT']
            for g in gold:
                g_trans = normalize(g['transition'])
                g_mode = g.get('vibration_mode', '')
                matched_entry = None
                for entry in artifact:
                    a_trans = normalize(entry.get('transition', ''))
                    a_mode = entry.get('vibration_mode', '')
                    if a_trans == g_trans and a_mode == g_mode:
                        matched_entry = entry
                        break
                if matched_entry is None:
                    continue
                ok = True
                for fname in fields:
                    agent_val = matched_entry.get(fname)
                    gold_val = g.get(fname)
                    if agent_val is None or gold_val is None:
                        ok = False
                        break
                    tol = field_tols.get(fname, {})
                    rel_tol = tol.get('rel', 0.01)
                    abs_tol = tol.get('abs', 0.0)
                    if not (abs(agent_val - gold_val) <= abs_tol or (abs(gold_val) > 1e-30 and abs(agent_val - gold_val) / abs(gold_val) <= rel_tol)):
                        ok = False
                        break
                if ok:
                    correct += 1
            return correct / len(gold) if gold else 0.0
        


# === block: score_3 (check id='faraday_odd_cf') ===
def score_3(artifact, step, ctx):
            gold = step.get('gold', [])
            field_tols = step.get('tolerances', {})
            if not isinstance(artifact, list) or not gold:
                return 0.0
            normalize = ctx.get('normalize_transition', lambda x: x)
            correct = 0
            fields = ['A', 'B', 'C', 'B_plus_C_over_kT']
            for g in gold:
                g_trans = normalize(g['transition'])
                matched_entry = None
                for entry in artifact:
                    a_trans = normalize(entry.get('transition', ''))
                    if a_trans == g_trans:
                        matched_entry = entry
                        break
                if matched_entry is None:
                    continue
                ok = True
                for fname in fields:
                    agent_val = matched_entry.get(fname)
                    gold_val = g.get(fname)
                    if agent_val is None or gold_val is None:
                        ok = False
                        break
                    tol = field_tols.get(fname, {})
                    rel_tol = tol.get('rel', 0.01)
                    abs_tol = tol.get('abs', 0.0)
                    if not (abs(agent_val - gold_val) <= abs_tol or (abs(gold_val) > 1e-30 and abs(agent_val - gold_val) / abs(gold_val) <= rel_tol)):
                        ok = False
                        break
                if ok:
                    correct += 1
            return correct / len(gold) if gold else 0.0
        


_SCORERS = {
    'osc_strengths_odd_vib': score_0,
    'osc_strengths_odd_cf': score_1,
    'faraday_odd_vib': score_2,
    'faraday_odd_cf': score_3,
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
