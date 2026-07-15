import os
import json
import csv

# === author imports / helpers ===
import json, re, math, os
from math import lgamma, log


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

    def parse_key_for_m(key):
        for m in ["Ir","Pt","Rh","Ag","Au"]:
            if m.lower() in key.lower():
                return m
        return None

    def extract_x_from_key(key):
        match = re.search(r'x(\d+\.?\d*)', key)
        if match:
            return float(match.group(1))
        match = re.search(r'(\d+)at%', key)
        if match:
            return float(match.group(1)) / 100.0
        return None

    def compute_binary_entropy(n_pd, n_ru):
        N = n_pd + n_ru
        lnW = lgamma(N+1) - lgamma(n_pd+1) - lgamma(n_ru+1)
        S_total = k_B * lnW
        return S_total / N

    gold_entropy = {}
    for s in spec.get("steps", []):
        if s.get("output_file") == "configurational_entropy.json":
            gold_entropy = s.get("config", {}).get("gold", {})
            break
    return {"gold_entropy": gold_entropy}


# === block: score_0 (check id='step3') ===
def score_0(artifact, step, ctx):
    tol = step.get("config", {}).get("tol_rel", 0.1)
    gold = ctx.get("gold_entropy", {})
    if not artifact or not isinstance(artifact, list):
        return 0.0
    scores = []
    for item in artifact:
        x = item.get("x")
        ent = item.get("entropy_per_atom_eV")
        if x is None or ent is None:
            continue
        rx = str(round(x, 2))
        if rx in gold:
            ref = gold[rx]
            if ref == 0:
                s = 1.0 if ent == 0 else 0.0
            else:
                rel_err = abs(ent - ref) / abs(ref)
                if rel_err <= tol:
                    s = 1.0
                else:
                    s = max(0.0, 1.0 - (rel_err - tol) / 0.1)
        else:
            s = 0.0
        scores.append(s)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_1 (check id='step4') ===
def score_1(artifact, step, ctx):
    if not artifact or not isinstance(artifact, dict):
        return 0.0
    valid_count = 0
    total = 0
    for key, val in artifact.items():
        if not isinstance(val, dict):
            continue
        ss = val.get("solid_solution")
        seg = val.get("segregated")
        if not (isinstance(ss, list) and isinstance(seg, list)):
            continue
        if len(ss) == 0 or len(seg) == 0:
            continue
        ss_mean = sum(ss) / len(ss)
        seg_mean = sum(seg) / len(seg)
        total += 1
        if ss_mean > seg_mean:
            valid_count += 1
    if total == 0:
        return 0.0
    return valid_count / total


# === block: score_2 (check id='step5') ===
def score_2(artifact, step, ctx):
    k_B = 8.617333262145e-5

    def parse_key_for_m(key):
        for m in ["Ir","Pt","Rh","Ag","Au"]:
            if m.lower() in key.lower():
                return m
        return None

    def extract_x_from_key(key):
        match = re.search(r'x(\d+\.\?\d*)', key)
        if match:
            return float(match.group(1))
        match = re.search(r'(\d+)at%', key)
        if match:
            return float(match.group(1)) / 100.0
        return None

    def compute_binary_entropy(n_pd, n_ru):
        N = n_pd + n_ru
        if n_pd < 0 or n_ru < 0 or N <= 0:
            return 0.0
        lnW = lgamma(N+1) - lgamma(n_pd+1) - lgamma(n_ru+1)
        S_total = k_B * lnW
        return S_total / N

    outputs_dir = "/app/outputs"
    excess_path = os.path.join(outputs_dir, "excess_energies.json")
    if not os.path.exists(excess_path):
        return 0.0
    with open(excess_path) as f:
        excess = json.load(f)
    entropy_path = os.path.join(outputs_dir, "configurational_entropy.json")
    if not os.path.exists(entropy_path):
        return 0.0
    with open(entropy_path) as f:
        ent_array = json.load(f)

    entropy_lookup = {}
    for item in ent_array:
        x = item.get("x")
        ent = item.get("entropy_per_atom_eV")
        if x is not None and ent is not None:
            entropy_lookup[round(x, 2)] = ent

    def compute_tc_for_system(system):
        m = parse_key_for_m(system)
        if m:
            matching_keys = []
            for key in excess:
                if m.lower() in key.lower():
                    matching_keys.append(key)
            best_key = None
            best_dist = float('inf')
            for key in matching_keys:
                x = extract_x_from_key(key)
                if x is not None:
                    dist = abs(x - 0.33)
                    if dist < best_dist:
                        best_dist = dist
                        best_key = key
            if best_key is None and matching_keys:
                best_key = matching_keys[0]
            if not best_key:
                return None
            entry = excess[best_key]
            ss = entry.get("solid_solution", [])
            seg = entry.get("segregated", [])
            if not (isinstance(ss, list) and isinstance(seg, list)):
                return None
            if len(ss) == 0 or len(seg) == 0:
                return None
            ss_mean = sum(ss) / len(ss)
            seg_mean = sum(seg) / len(seg)
            delta_e = ss_mean - seg_mean
            if delta_e <= 0:
                return 0.0
            s_per_atom = entropy_lookup.get(0.33, None)
            if s_per_atom is None or s_per_atom <= 0:
                return None
            return delta_e / s_per_atom
        else:
            matching_keys = []
            for key in excess:
                low = key.lower()
                if 'pd' in low and 'ru' in low and not any(m in low for m in ["ir","pt","rh","ag","au"]):
                    matching_keys.append(key)
            if not matching_keys:
                return None
            key = matching_keys[0]
            entry = excess[key]
            ss = entry.get("solid_solution", [])
            seg = entry.get("segregated", [])
            if not (isinstance(ss, list) and isinstance(seg, list)):
                return None
            if len(ss) == 0 or len(seg) == 0:
                return None
            ss_mean = sum(ss) / len(ss)
            seg_mean = sum(seg) / len(seg)
            delta_e = ss_mean - seg_mean
            if delta_e <= 0:
                return 0.0
            x = extract_x_from_key(key)
            if x is not None:
                n_pd = int(round(x * 201))
                n_ru = 201 - n_pd
            else:
                n_pd = 100
                n_ru = 101
            s_per_atom = compute_binary_entropy(n_pd, n_ru)
            if s_per_atom <= 0:
                return None
            return delta_e / s_per_atom

    def score_tc(system, tc):
        config = step.get("config", {})
        stabilizers = config.get("stabilizers", [])
        non_stabilizers = config.get("non_stabilizers", [])
        if system in stabilizers:
            Tc_max = config.get("Tc_max_stabilizer", 800)
            Tc_decay = config.get("Tc_max_decay_end", 1200)
            if tc <= Tc_max:
                return 1.0
            elif tc >= Tc_decay:
                return 0.0
            else:
                s = 1.0 - (tc - Tc_max) / (Tc_decay - Tc_max)
                return max(0.0, s)
        else:
            Tc_min = config.get("Tc_min_non_stabilizer", 1000)
            Tc_start = config.get("Tc_min_decay_start", 600)
            if tc >= Tc_min:
                return 1.0
            elif tc <= Tc_start:
                return 0.0
            else:
                s = (tc - Tc_start) / (Tc_min - Tc_start)
                return max(0.0, s)

    systems = ["PdRu", "PdRuIr", "PdRuPt", "PdRuRh", "PdRuAg", "PdRuAu"]
    scores = []
    for sys in systems:
        tc = compute_tc_for_system(sys)
        s = 0.0
        if tc is not None:
            s = score_tc(sys, tc)
        scores.append(s)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


_SCORERS = {
    'step3': score_0,
    'step4': score_1,
    'step5': score_2,
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
