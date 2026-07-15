import os
import json
import csv

# === author imports / helpers ===
import numpy as np
import math
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
    return {}


# === block: score_0 (check id='avg_energy_ordering') ===
def score_0(artifact, step, ctx):
    rows = artifact
    required_fields = [2, 5, 10, 15, 20, 25, 30]
    data = {}
    for r in rows:
        f = float(r['field_kVcm'])
        if f in required_fields:
            data[f] = (float(r['avg_energy_traditional']), float(r['avg_energy_CBMC']))
    if set(required_fields) != set(data.keys()):
        return 0.0
    sorted_fields = sorted(required_fields)
    trad_vals = [data[f][0] for f in sorted_fields]
    cbmc_vals = [data[f][1] for f in sorted_fields]
    for t, c in zip(trad_vals, cbmc_vals):
        if c <= t:
            return 0.0
    if not all(trad_vals[i] < trad_vals[i+1] for i in range(len(trad_vals)-1)):
        return 0.0
    if not all(cbmc_vals[i] < cbmc_vals[i+1] for i in range(len(cbmc_vals)-1)):
        return 0.0
    return 1.0


# === block: score_1 (check id='energy_histogram_tail') ===
def score_1(artifact, step, ctx):
    rows = artifact
    total_trad = 0.0
    total_cbmc = 0.0
    tail_trad = 0.0
    tail_cbmc = 0.0
    for r in rows:
        elow = float(r['energy_low'])
        ehigh = float(r['energy_high'])
        cnt_trad = float(r['count_traditional'])
        cnt_cbmc = float(r['count_CBMC'])
        if cnt_trad < 0 or cnt_cbmc < 0:
            return 0.0
        total_trad += cnt_trad
        total_cbmc += cnt_cbmc
        if elow >= 0.1:
            tail_trad += cnt_trad
            tail_cbmc += cnt_cbmc
    if total_trad == 0 or total_cbmc == 0:
        return 0.0
    tail_prob_trad = tail_trad / total_trad
    tail_prob_cbmc = tail_cbmc / total_cbmc
    if tail_prob_trad == 0:
        return 0.0
    ratio = tail_prob_cbmc / tail_prob_trad
    if 1.0 <= ratio <= 2.0:
        return 1.0
    elif 0.8 <= ratio < 1.0 or 2.0 < ratio <= 2.5:
        return 0.5
    else:
        return 0.0


# === block: score_2 (check id='dispersion_broadening') ===
def score_2(artifact, step, ctx):
    rows = artifact
    trad_pts = []
    cbmc_pts = []
    for r in rows:
        alg = r['algorithm'].strip().lower()
        p = float(r['momentum'])
        e = float(r['energy'])
        if alg == 'traditional':
            trad_pts.append((p, e))
        elif alg == 'cb-mc':
            cbmc_pts.append((p, e))
    if len(trad_pts) < 100 or len(cbmc_pts) < 100:
        return 0.0
    trad_p = np.array([x[0] for x in trad_pts])
    trad_e = np.array([x[1] for x in trad_pts])
    cbmc_p = np.array([x[0] for x in cbmc_pts])
    cbmc_e = np.array([x[1] for x in cbmc_pts])
    trad_p2 = trad_p ** 2
    A = np.vstack([trad_p2, np.ones_like(trad_p2)]).T
    coeff_trad, _, _, _ = np.linalg.lstsq(A, trad_e, rcond=None)
    trad_pred = coeff_trad[0] * trad_p2 + coeff_trad[1]
    trad_res = trad_e - trad_pred
    rms_trad = np.sqrt(np.mean(trad_res ** 2))
    cbmc_p2 = cbmc_p ** 2
    A2 = np.vstack([cbmc_p2, np.ones_like(cbmc_p2)]).T
    coeff_cbmc, _, _, _ = np.linalg.lstsq(A2, cbmc_e, rcond=None)
    cbmc_pred = coeff_cbmc[0] * cbmc_p2 + coeff_cbmc[1]
    cbmc_res = cbmc_e - cbmc_pred
    rms_cbmc = np.sqrt(np.mean(cbmc_res ** 2))
    if rms_trad < 1e-12:
        rms_trad = 1e-12
    if rms_cbmc / rms_trad > 100.0:
        return 1.0
    else:
        return 0.0


_SCORERS = {
    'avg_energy_ordering': score_0,
    'energy_histogram_tail': score_1,
    'dispersion_broadening': score_2,
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
