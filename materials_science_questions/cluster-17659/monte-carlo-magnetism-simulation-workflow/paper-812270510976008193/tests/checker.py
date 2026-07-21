import os
import json
import csv

# === author imports / helpers ===
import os, csv, math, collections


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


# === block: score_0 (check id='shape_raw') ===
def score_0(artifact, step, ctx):
    return 1.0 if artifact else 0.0


# === block: score_1 (check id='shape_norm') ===
def score_1(artifact, step, ctx):
    return 1.0 if artifact else 0.0


# === block: score_2 (check id='consistency') ===
def score_2(artifact, step, ctx):
    raw_path = '/app/outputs/raw_frequencies.csv'
    if not os.path.exists(raw_path): return 0.0
    raw_data = []
    with open(raw_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            raw_data.append(row)
    norm_data = artifact
    raw_by_key = {}
    for r in raw_data:
        try:
            eta = float(r['eta'])
            kx = float(r['kx'])
            ky = float(r['ky'])
            tj = float(r['T_J'])
            ome = float(r['omega_ck'])
        except: continue
        raw_by_key[(eta,kx,ky,tj)] = ome
    norm_by_key = {}
    for r in norm_data:
        try:
            eta = float(r['eta'])
            kx = float(r['kx'])
            ky = float(r['ky'])
            tj = float(r['T_J'])
            nf = float(r['normalized_freq'])
        except: continue
        norm_by_key[(eta,kx,ky,tj)] = nf
    tol = 1e-5
    matches = 0
    total = 0
    for key, ome in raw_by_key.items():
        if key not in norm_by_key:
            total += 1
            continue
        eta,kx,ky,tj = key
        gg = (math.cos(kx) + math.cos(ky))/2.0
        omega0 = 4.0 * math.sqrt((1-gg)*(1-eta*gg))
        expected = ome / omega0
        diff = abs(expected - norm_by_key[key])
        total += 1
        if diff < tol: matches += 1
    if total == 0: return 0.0
    return matches / total


# === block: score_3 (check id='k_independence') ===
def score_3(artifact, step, ctx):
    norm_data = artifact
    if not norm_data: return 0.0
    groups = collections.defaultdict(list)
    for r in norm_data:
        try:
            eta = float(r['eta'])
            tj = float(r['T_J'])
            nf = float(r['normalized_freq'])
        except: continue
        groups[(eta,tj)].append(nf)
    max_dev = 0.05
    passed = 0
    total = 0
    for key, vals in groups.items():
        if len(vals) < 2: continue
        total += 1
        mu = sum(vals)/len(vals)
        dev = max(abs(v-mu) for v in vals)
        if dev <= max_dev: passed += 1
    if total == 0: return 0.0
    return passed / total


# === block: score_4 (check id='monotonic_decrease') ===
def score_4(artifact, step, ctx):
    norm_data = artifact
    if not norm_data: return 0.0
    series = collections.defaultdict(list)
    for r in norm_data:
        try:
            eta = float(r['eta'])
            kx = float(r['kx'])
            ky = float(r['ky'])
            tj = float(r['T_J'])
            nf = float(r['normalized_freq'])
        except: continue
        series[(eta,kx,ky)].append((tj,nf))
    eps = 0.01
    valid = 0
    total = 0
    for key, pairs in series.items():
        if len(pairs) < 2: continue
        total += 1
        sorted_pairs = sorted(pairs, key=lambda x: x[0])
        ok = True
        for i in range(1, len(sorted_pairs)):
            if sorted_pairs[i][1] > sorted_pairs[i-1][1] + eps:
                ok = False
                break
        if ok: valid += 1
    if total == 0: return 0.0
    return valid / total


_SCORERS = {
    'shape_raw': score_0,
    'shape_norm': score_1,
    'consistency': score_2,
    'k_independence': score_3,
    'monotonic_decrease': score_4,
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
