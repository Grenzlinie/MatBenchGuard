import os
import json
import csv

# === author imports / helpers ===
import numpy as np
import h5py


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


# === block: score_0 (check id='lattice_constants') ===
def score_0(artifact, step, ctx):
    gold = step["gold"]
    tol = step["tolerance"]
    total = 0.0
    n = 0
    for row in artifact:
        x_str = str(row.get("x", "")).strip()
        if x_str in gold:
            a0_val = float(row.get("a0_angstrom", 0.0))
            diff = abs(a0_val - gold[x_str])
            if diff <= tol:
                score_x = 1.0
            else:
                score_x = max(0.0, 1.0 - (diff - tol) / (2.0 * tol))
            total += score_x
            n += 1
    return total / n if n > 0 else 0.0


# === block: score_1 (check id='absorption_onsets') ===
def score_1(artifact, step, ctx):
    gold = step["gold"]
    tol = step["tolerance"]
    h5_path = "/app/outputs/dielectric_data.h5"
    try:
        f = h5py.File(h5_path, "r")
    except Exception:
        return 0.0
    scores = []
    for x_str, gold_val in gold.items():
        found = False
        for key_cand in [f"/x_{x_str}/e2", f"/{x_str}/e2", f"x_{x_str}/e2", f"{x_str}/e2"]:
            if key_cand in f:
                ds = f[key_cand][:]
                found = True
                break
        if not found:
            continue
        energy = ds[:, 0]
        e2 = ds[:, 1]
        threshold = 1e-3
        idx = np.argmax(e2 > threshold)
        if idx == 0 and e2[0] <= threshold:
            continue
        onset = energy[idx]
        diff = abs(onset - gold_val)
        if diff <= tol:
            score_x = 1.0
        else:
            score_x = max(0.0, 1.0 - (diff - tol) / (2.0 * tol))
        scores.append(score_x)
    f.close()
    return np.mean(scores) if scores else 0.0


# === block: score_2 (check id='static_refractive_index') ===
def score_2(artifact, step, ctx):
    gold = step["gold"]
    tol = step["tolerance"]
    h5_path = "/app/outputs/dielectric_data.h5"
    try:
        f = h5py.File(h5_path, "r")
    except Exception:
        return 0.0
    scores = []
    for x_str, gold_val in gold.items():
        found = False
        for key_cand in [f"/x_{x_str}/e2", f"/{x_str}/e2", f"x_{x_str}/e2", f"{x_str}/e2"]:
            if key_cand in f:
                ds = f[key_cand][:]
                found = True
                break
        if not found:
            continue
        energy = ds[:, 0]
        e2 = ds[:, 1]
        de = energy[1] - energy[0]
        denom = energy**2
        denom[0] = de  # avoid 0/0 later
        kernel = 2.0/np.pi * e2 * energy / (denom)
        e1 = 1.0 + np.trapz(kernel, energy)
        n0 = np.sqrt(max(e1, 0.0))
        diff = abs(n0 - gold_val)
        if diff <= tol:
            score_x = 1.0
        else:
            score_x = max(0.0, 1.0 - (diff - tol) / (2.0 * tol))
        scores.append(score_x)
    f.close()
    return np.mean(scores) if scores else 0.0


# === block: score_3 (check id='plasmon_peak_energies') ===
def score_3(artifact, step, ctx):
    gold = step["gold"]
    tol = step["tolerance"]
    h5_path = "/app/outputs/dielectric_data.h5"
    try:
        f = h5py.File(h5_path, "r")
    except Exception:
        return 0.0
    scores = []
    for x_str, gold_val in gold.items():
        found = False
        for key_cand in [f"/x_{x_str}/e2", f"/{x_str}/e2", f"x_{x_str}/e2", f"{x_str}/e2"]:
            if key_cand in f:
                ds = f[key_cand][:]
                found = True
                break
        if not found:
            continue
        energy = ds[:, 0]
        e2 = ds[:, 1]
        de = energy[1] - energy[0]
        denom = energy**2
        denom[0] = de
        kernel = 2.0/np.pi * e2 * energy / (denom)
        e1 = 1.0 + np.trapz(kernel, energy)
        L = e2 / (e1**2 + e2**2 + 1e-30)
        mask = energy > 10.0
        if not np.any(mask):
            continue
        idx = np.argmax(L[mask])
        plasmon = energy[mask][idx]
        diff = abs(plasmon - gold_val)
        if diff <= tol:
            score_x = 1.0
        else:
            score_x = max(0.0, 1.0 - (diff - tol) / (2.0 * tol))
        scores.append(score_x)
    f.close()
    return np.mean(scores) if scores else 0.0


_SCORERS = {
    'lattice_constants': score_0,
    'absorption_onsets': score_1,
    'static_refractive_index': score_2,
    'plasmon_peak_energies': score_3,
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
