import os
import json
import csv

# === author imports / helpers ===
import math
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


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    gold = step.get('params', {}).get('gold', [])
    tol = step.get('params', {}).get('tolerance_meV', 0.5)
    if not artifact or not gold:
        return 0.0
    gold_lookup = {(g['q_point_label'], g['mode_index']): g['frequency_meV'] for g in gold}
    matches = 0
    total = len(gold)
    seen = set()
    for row in artifact:
        key = (row.get('q_point_label'), int(row.get('mode_index')))
        if key in gold_lookup and key not in seen:
            diff = abs(float(row.get('frequency_meV', 0)) - gold_lookup[key])
            if diff <= tol:
                matches += 1
            seen.add(key)
    return matches / total if total > 0 else 0.0


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    gold_list = step.get('params', {}).get('gold', [])
    tol = step.get('params', {}).get('tolerance_meV', 1.0)
    if not artifact or not gold_list:
        return 0.0
    gold_by_T = {g['temperature_K']: g for g in gold_list}
    matches_anh = 0
    matches_exp = 0
    count = 0
    for row in artifact:
        T = int(row.get('temperature_K'))
        if T in gold_by_T:
            g = gold_by_T[T]
            diff_anh = abs(float(row.get('anharmonic_renormalized_frequency_meV', 0)) - g['anharmonic_renormalized_frequency_meV'])
            if diff_anh <= tol:
                matches_anh += 1
            diff_exp = abs(float(row.get('experimental_frequency_meV', 0)) - g['experimental_frequency_meV'])
            if diff_exp <= tol:
                matches_exp += 1
            count += 1
    if count == 0:
        return 0.0
    score_anh = matches_anh / count
    score_exp = matches_exp / count
    return (score_anh + score_exp) / 2.0


# === block: score_2 (check id='step_03') ===
def score_2(artifact, step, ctx):
    params = step.get('params', {})
    gold_peaks_str = params.get('gold_peaks', {})
    tol = params.get('tolerance_meV', 0.5)
    TO_double = params.get('TO_double_peaks', [])
    if not artifact:
        return 0.0
    from collections import defaultdict
    data_by_q_mode = defaultdict(list)
    for row in artifact:
        q = float(row.get('q_fractional'))
        mode = row.get('mode_label')
        energy = float(row.get('energy_transfer_meV', 0))
        intensity = float(row.get('intensity_arb', 0))
        data_by_q_mode[(q, mode)].append((energy, intensity))
    agent_peaks = {}
    for (q, mode), entries in data_by_q_mode.items():
        max_entry = max(entries, key=lambda x: x[1])
        agent_peaks[(q, mode)] = max_entry[0]
    scored = 0
    total = 0
    for q_str, mode_peaks in gold_peaks_str.items():
        q = float(q_str)
        for mode, target in mode_peaks.items():
            total += 1
            if target == 'double':
                if (q, mode) in data_by_q_mode:
                    entries = data_by_q_mode[(q, mode)]
                    sorted_entries = sorted(entries, key=lambda x: x[1], reverse=True)
                    peaks_found = [e[0] for e in sorted_entries[:2]]
                    peaks_found.sort()
                    target_peaks = sorted(TO_double)
                    if len(peaks_found) >= 2 and abs(peaks_found[0] - target_peaks[0]) <= tol and abs(peaks_found[1] - target_peaks[1]) <= tol:
                        scored += 1
            else:
                agent_val = agent_peaks.get((q, mode))
                if agent_val is not None:
                    if isinstance(target, (int, float)):
                        diff = abs(agent_val - target)
                        if diff <= tol:
                            scored += 1
    return scored / total if total > 0 else 0.0


# === block: score_3 (check id='step_04') ===
def score_3(artifact, step, ctx):
    params = step.get('params', {})
    gold_peaks_str = params.get('gold_peaks', {})
    tol = params.get('tolerance_meV', 0.5)
    TO_double = params.get('TO_double_peaks', [])
    if not artifact:
        return 0.0
    from collections import defaultdict
    data_by_q_mode = defaultdict(list)
    for row in artifact:
        q = row.get('q_fractional')
        mode = row.get('mode_label')
        energy = float(row.get('energy_transfer_meV', 0))
        intensity = float(row.get('intensity_arb', 0))
        data_by_q_mode[(q, mode)].append((energy, intensity))
    agent_peaks = {}
    for (q, mode), entries in data_by_q_mode.items():
        max_entry = max(entries, key=lambda x: x[1])
        agent_peaks[(q, mode)] = max_entry[0]
    scored = 0
    total = 0
    for q_str, mode_peaks in gold_peaks_str.items():
        q = float(q_str)
        for mode, target in mode_peaks.items():
            total += 1
            if target == 'double':
                if (q, mode) in data_by_q_mode:
                    entries = data_by_q_mode[(q, mode)]
                    sorted_entries = sorted(entries, key=lambda x: x[1], reverse=True)
                    peaks_found = [e[0] for e in sorted_entries[:2]]
                    peaks_found.sort()
                    target_peaks = sorted(TO_double)
                    if len(peaks_found) >= 2 and abs(peaks_found[0] - target_peaks[0]) <= tol and abs(peaks_found[1] - target_peaks[1]) <= tol:
                        scored += 1
            else:
                agent_val = agent_peaks.get((q, mode))
                if agent_val is not None:
                    if isinstance(target, (int, float)):
                        diff = abs(agent_val - target)
                        if diff <= tol:
                            scored += 1
    return scored / total if total > 0 else 0.0


# === block: score_4 (check id='step_05') ===
def score_4(artifact, step, ctx):
    gold_list = step.get('params', {}).get('gold', [])
    rel_tol = step.get('params', {}).get('tolerance_relative', 0.2)
    if not artifact or not gold_list:
        return 0.0
    gold_by_T = {g['temperature_K']: g['resistivity_mK_per_W'] for g in gold_list}
    matches = 0
    total = 0
    for row in artifact:
        T = float(row.get('temperature_K'))
        if T in gold_by_T:
            gold_val = gold_by_T[T]
            agent_val = float(row.get('resistivity_mK_per_W', 0))
            if gold_val == 0:
                continue
            rel_err = abs(agent_val - gold_val) / gold_val
            if rel_err <= rel_tol:
                matches += 1
            total += 1
    return matches / total if total > 0 else 0.0


_SCORERS = {
    'step_01': score_0,
    'step_02': score_1,
    'step_03': score_2,
    'step_04': score_3,
    'step_05': score_4,
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
