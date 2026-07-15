import os
import json
import csv

# === author imports / helpers ===
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


# === block: score_0 (check id='optical_conductivity') ===
def score_0(artifact, step, ctx):
    def trapezoidal(energy, sigma, emax=1.0):
        e_slice = []
        s_slice = []
        for e, s in zip(energy, sigma):
            if e <= emax:
                e_slice.append(e)
                s_slice.append(s)
            else:
                break
        if len(e_slice) < 2:
            return 0.0
        integral = 0.0
        for i in range(len(e_slice)-1):
            de = e_slice[i+1] - e_slice[i]
            integral += (s_slice[i] + s_slice[i+1]) * de / 2.0
        return integral

    cfg = step.get('configuration', {})
    sub_w = cfg.get('sub_weights', {})

    try:
        undisplaced = artifact.get('undisplaced', {})
        A_g_displaced = artifact.get('A_g_displaced', {})
        B_1g_displaced = artifact.get('B_1g_displaced', {})

        w_und = trapezoidal(undisplaced.get('energy_ev', []), undisplaced.get('sigma1', []))
        w_ag = trapezoidal(A_g_displaced.get('energy_ev', []), A_g_displaced.get('sigma1', []))
        w_b1g = trapezoidal(B_1g_displaced.get('energy_ev', []), B_1g_displaced.get('sigma1', []))
    
        # ratio checks
        ratio1 = w_ag / w_und if w_und > 1e-12 else float('inf')
        ratio2 = w_ag / w_b1g if w_b1g > 1e-12 else float('inf')
        thresh = cfg.get('ratio_threshold', 4.0)
        score_ratio1 = min(1.0, max(0.0, ratio1 / thresh))
        score_ratio2 = min(1.0, max(0.0, ratio2 / thresh))
    
        # negligible weight checks
        max_frac = cfg.get('max_weight_ratio', 0.06)
        score_und_neg = 1.0 if (w_und / w_ag if w_ag > 0 else 1.0) <= max_frac else 0.0
        score_b1g_neg = 1.0 if (w_b1g / w_ag if w_ag > 0 else 1.0) <= max_frac else 0.0
    
        # monotonic check for A_g below 1 eV
        ag_energy = A_g_displaced.get('energy_ev', [])
        ag_sigma = A_g_displaced.get('sigma1', [])
        mono_count = 0
        total_pairs = 0
        for i in range(len(ag_energy)):
            if ag_energy[i] > 1.0:
                break
            if i+1 < len(ag_energy) and ag_energy[i+1] <= 1.0:
                total_pairs += 1
                if ag_sigma[i] >= ag_sigma[i+1]:
                    mono_count += 1
        frac_mono = mono_count / total_pairs if total_pairs > 0 else 0.0
        mono_thresh = cfg.get('monotonic_fraction_threshold', 0.9)
        score_mono = min(1.0, frac_mono / mono_thresh) if mono_thresh > 0 else 0.0
    
        total = (sub_w.get('ratio_undisplaced', 0.3) * score_ratio1 +
                 sub_w.get('ratio_b1g', 0.3) * score_ratio2 +
                 sub_w.get('negligible_undisplaced', 0.2) * score_und_neg +
                 sub_w.get('negligible_b1g', 0.1) * score_b1g_neg +
                 sub_w.get('monotonic', 0.1) * score_mono)
        return total

    except Exception:
        return 0.0


_SCORERS = {
    'optical_conductivity': score_0,
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
