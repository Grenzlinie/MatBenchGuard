import os
import json
import csv

# === author imports / helpers ===
import subprocess, sys
try:
    import numpy as np
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "--no-cache-dir", "-i", "https://pypi.tuna.tsinghua.edu.cn/simple", "numpy"])
    import numpy as np


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


# === block: score_0 (check id='step_h0p125') ===
def score_0(artifact, step, ctx):
    data = artifact
    Ts = np.array([float(r['T']) for r in data])
    ds = np.array([float(r['d']) for r in data])
    Ms = np.abs(np.array([float(r['M']) for r in data]))
    if len(Ms) == 0:
        return 0.0
    score = 0.0
    # F3/2 existence
    if np.max(Ms) >= 1.0:
        score += 0.2
    # F1/2 existence
    if np.any((Ms > 0.3) & (Ms < 0.7)):
        score += 0.2
    # P existence
    if np.any(Ms < 0.1):
        score += 0.1
    # First-order jump: at low T (T<0.3), max diff in Ms across sorted d
    low_T_mask = Ts < 0.3
    if np.sum(low_T_mask) > 1:
        idx = np.argsort(ds[low_T_mask])
        M_sort = Ms[low_T_mask][idx]
        diffs = np.diff(M_sort)
        max_diff = np.max(np.abs(diffs)) if len(diffs) > 0 else 0.0
        if max_diff >= 0.5:
            score += 0.3
        else:
            score += 0.15 * min(1.0, max_diff / 0.5)
    else:
        score += 0.15  # insufficient data, give partial
    # High T paramagnetic
    high_T_mask = Ts > 1.5
    if np.sum(high_T_mask) > 0 and np.max(Ms[high_T_mask]) < 0.2:
        score += 0.2
    return min(1.0, score)


# === block: score_1 (check id='step_h0p35') ===
def score_1(artifact, step, ctx):
    data = artifact
    Ts = np.array([float(r['T']) for r in data])
    ds = np.array([float(r['d']) for r in data])
    Ms = np.abs(np.array([float(r['M']) for r in data]))
    if len(Ms) == 0:
        return 0.0
    score = 0.0
    if np.max(Ms) >= 1.0:
        score += 0.2
    if np.any((Ms > 0.3) & (Ms < 0.7)):
        score += 0.2
    if np.any(Ms < 0.1):
        score += 0.1
    low_T_mask = Ts < 0.3
    if np.sum(low_T_mask) > 1:
        idx = np.argsort(ds[low_T_mask])
        M_sort = Ms[low_T_mask][idx]
        diffs = np.diff(M_sort)
        max_diff = np.max(np.abs(diffs)) if len(diffs) > 0 else 0.0
        if max_diff >= 0.5:
            score += 0.3
        else:
            score += 0.15 * min(1.0, max_diff / 0.5)
    else:
        score += 0.15
    high_T_mask = Ts > 1.5
    if np.sum(high_T_mask) > 0 and np.max(Ms[high_T_mask]) < 0.2:
        score += 0.2
    return min(1.0, score)


# === block: score_2 (check id='step_h0p375') ===
def score_2(artifact, step, ctx):
    data = artifact
    Ts = np.array([float(r['T']) for r in data])
    ds = np.array([float(r['d']) for r in data])
    Ms = np.abs(np.array([float(r['M']) for r in data]))
    if len(Ms) == 0:
        return 0.0
    score = 0.0
    # F3/2 existence
    if np.max(Ms) >= 1.0:
        score += 0.25
    # No pure F1/2 at low T (require that at T<0.3 no |M| in (0.3,0.7))
    low_T_mask = Ts < 0.3
    has_f12_low = np.any(Ms[low_T_mask] > 0.3) and np.any(Ms[low_T_mask] < 0.7)
    if not has_f12_low:
        score += 0.15
    # P existence
    if np.any(Ms < 0.1):
        score += 0.1
    # First-order jump
    if np.sum(low_T_mask) > 1:
        idx = np.argsort(ds[low_T_mask])
        M_sort = Ms[low_T_mask][idx]
        diffs = np.diff(M_sort)
        max_diff = np.max(np.abs(diffs)) if len(diffs) > 0 else 0.0
        if max_diff >= 0.5:
            score += 0.3
        else:
            score += 0.15 * min(1.0, max_diff / 0.5)
    else:
        score += 0.15
    # High T paramagnetic
    high_T_mask = Ts > 1.5
    if np.sum(high_T_mask) > 0 and np.max(Ms[high_T_mask]) < 0.2:
        score += 0.2
    return min(1.0, score)


# === block: score_3 (check id='step_h1p3') ===
def score_3(artifact, step, ctx):
    data = artifact
    Ts = np.array([float(r['T']) for r in data])
    ds = np.array([float(r['d']) for r in data])
    Ms = np.abs(np.array([float(r['M']) for r in data]))
    if len(Ms) == 0:
        return 0.0
    score = 0.0
    # F3/2+P coexistence implies possible max |M| near 1.5
    if np.max(Ms) >= 1.0:
        score += 0.2
    # F1/2 existence
    if np.any((Ms > 0.3) & (Ms < 0.7)):
        score += 0.2
    # P existence
    if np.any(Ms < 0.1):
        score += 0.1
    low_T_mask = Ts < 0.3
    if np.sum(low_T_mask) > 1:
        idx = np.argsort(ds[low_T_mask])
        M_sort = Ms[low_T_mask][idx]
        diffs = np.diff(M_sort)
        max_diff = np.max(np.abs(diffs)) if len(diffs) > 0 else 0.0
        if max_diff >= 0.5:
            score += 0.3
        else:
            score += 0.15 * min(1.0, max_diff / 0.5)
    else:
        score += 0.15
    high_T_mask = Ts > 1.5
    if np.sum(high_T_mask) > 0 and np.max(Ms[high_T_mask]) < 0.2:
        score += 0.2
    return min(1.0, score)


# === block: score_4 (check id='step_h1p5') ===
def score_4(artifact, step, ctx):
    data = artifact
    Ts = np.array([float(r['T']) for r in data])
    ds = np.array([float(r['d']) for r in data])
    Ms = np.abs(np.array([float(r['M']) for r in data]))
    if len(Ms) == 0:
        return 0.0
    score = 0.0
    # No pure F3/2 phase: max |M| should be < 1.0
    if np.max(Ms) < 1.0:
        score += 0.25
    # F1/2 existence
    if np.any((Ms > 0.3) & (Ms < 0.7)):
        score += 0.25
    # P existence
    if np.any(Ms < 0.1):
        score += 0.1
    # First-order jump (weaker weight)
    low_T_mask = Ts < 0.3
    if np.sum(low_T_mask) > 1:
        idx = np.argsort(ds[low_T_mask])
        M_sort = Ms[low_T_mask][idx]
        diffs = np.diff(M_sort)
        max_diff = np.max(np.abs(diffs)) if len(diffs) > 0 else 0.0
        if max_diff >= 0.5:
            score += 0.2
        else:
            score += 0.1 * min(1.0, max_diff / 0.5)
    else:
        score += 0.1
    # High T paramagnetic
    high_T_mask = Ts > 1.5
    if np.sum(high_T_mask) > 0 and np.max(Ms[high_T_mask]) < 0.2:
        score += 0.2
    return min(1.0, score)


_SCORERS = {
    'step_h0p125': score_0,
    'step_h0p35': score_1,
    'step_h0p375': score_2,
    'step_h1p3': score_3,
    'step_h1p5': score_4,
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
