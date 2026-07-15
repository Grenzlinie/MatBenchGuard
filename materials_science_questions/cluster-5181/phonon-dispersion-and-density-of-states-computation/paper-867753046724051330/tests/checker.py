import os
import json
import csv

# === author imports / helpers ===
import re
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


# === block: score_0 (check id='lattice_check') ===
def score_0(artifact, step, ctx):
    text = artifact if isinstance(artifact, str) else ''
    if not text:
        return 0.0

    def extract_val(pattern, txt):
        m = re.search(pattern, txt, re.IGNORECASE)
        if m:
            try:
                return float(m.group(1))
            except:
                pass
        return None

    a = extract_val(r'a\s*=\s*([\d\.]+)', text)
    b = extract_val(r'b\s*=\s*([\d\.]+)', text)
    c = extract_val(r'c\s*=\s*([\d\.]+)', text)

    if a is None or b is None or c is None:
        return 0.0

    gold_a = step.get('gold_lattice_a', 5.8164)
    gold_b = step.get('gold_lattice_b', 5.8167)
    gold_c = step.get('gold_lattice_c', 8.2271)
    tol = step.get('tolerance', 0.02)

    rel_err_a = abs(a - gold_a) / gold_a
    rel_err_b = abs(b - gold_b) / gold_b
    rel_err_c = abs(c - gold_c) / gold_c
    max_err = max(rel_err_a, rel_err_b, rel_err_c)

    if max_err <= tol:
        return 1.0
    else:
        # linear decay: score = max(0, 1 - (max_err - tol)/tol)
        score = 1.0 - (max_err - tol) / tol
        return max(0.0, min(1.0, score))


# === block: score_1 (check id='phonon_aard_theo') ===
def score_1(artifact, step, ctx):
    data = artifact if isinstance(artifact, dict) else {}
    key = step.get('key', 'theoretical_lattice_constants_frequencies')
    ref = step.get('experimental_frequencies', [])
    threshold = step.get('threshold_aard', 10.0)

    freqs = data.get(key, [])
    if not isinstance(freqs, list) or len(freqs) < len(ref):
        return 0.0

    # compute AARD as percent (same as paper formula)
    s = 0.0
    N = len(ref)
    for v, r in zip(freqs[:N], ref):
        if r <= 0:
            return 0.0
        s += abs(v - r) / r

    aard = (100.0 / N) * s

    if aard <= threshold:
        return 1.0
    else:
        # linear decay: 0 at threshold + 10% (absolute),
        decay = (aard - threshold) / 10.0
        return max(0.0, 1.0 - decay)


# === block: score_2 (check id='phonon_aard_exp') ===
def score_2(artifact, step, ctx):
    data = artifact if isinstance(artifact, dict) else {}
    key = step.get('key', 'experimental_lattice_constants_frequencies')
    ref = step.get('experimental_frequencies', [])
    threshold = step.get('threshold_aard', 15.0)

    freqs = data.get(key, [])
    if not isinstance(freqs, list) or len(freqs) < len(ref):
        return 0.0

    s = 0.0
    N = len(ref)
    for v, r in zip(freqs[:N], ref):
        if r <= 0:
            return 0.0
        s += abs(v - r) / r

    aard = (100.0 / N) * s

    if aard <= threshold:
        return 1.0
    else:
        decay = (aard - threshold) / 10.0
        return max(0.0, 1.0 - decay)


# === block: score_3 (check id='phonon_structural') ===
def score_3(artifact, step, ctx):
    data = artifact if isinstance(artifact, dict) else {}
    min_f = step.get('min_freq', 50)
    max_f = step.get('max_freq', 1000)

    lists = []
    for k in ['theoretical_lattice_constants_frequencies', 'experimental_lattice_constants_frequencies']:
        lst = data.get(k, [])
        if not isinstance(lst, list) or len(lst) < 15:
            return 0.0
        lists.append(lst)

    for lst in lists:
        for v in lst:
            if not isinstance(v, (int, float)) or v <= 0 or v < min_f or v > max_f:
                return 0.0
    return 1.0


_SCORERS = {
    'lattice_check': score_0,
    'phonon_aard_theo': score_1,
    'phonon_aard_exp': score_2,
    'phonon_structural': score_3,
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
