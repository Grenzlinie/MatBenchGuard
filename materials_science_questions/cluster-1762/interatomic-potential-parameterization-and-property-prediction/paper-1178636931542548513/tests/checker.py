import os
import json
import csv

# === author imports / helpers ===
import math, json


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


# === block: score_0 (check id='activation_energy_check') ===
def score_0(artifact, step, ctx):
        temps = artifact.get('temperatures')
        D = artifact.get('D_total')
        if not temps or not D or len(temps) != len(D) or len(temps) < 2 or any(d <= 0 for d in D):
            return 0.0
        inv_t = [1.0/t for t in temps]
        log_D = [math.log(d) for d in D]
        n = len(inv_t)
        sum_x = sum(inv_t)
        sum_y = sum(log_D)
        sum_xy = sum(x*y for x, y in zip(inv_t, log_D))
        sum_xx = sum(x*x for x in inv_t)
        denom = n * sum_xx - sum_x * sum_x
        if denom == 0:
            return 0.0
        m = (n * sum_xy - sum_x * sum_y) / denom
        kB = 8.617333262145e-5
        Ea_calc = -m * kB
        ref_Ea = step.get('reference_activation_energy', 0.78)
        tol = step.get('tolerance_activation_energy', 0.15)
        diff = abs(Ea_calc - ref_Ea)
        if diff <= tol:
            return 1.0
        elif diff <= 2*tol:
            return 0.5
        else:
            return 0.0


# === block: score_1 (check id='diffusion_anisotropy_check') ===
def score_1(artifact, step, ctx):
        Da = artifact.get('D_a_1473K')
        Db = artifact.get('D_b_1473K')
        Dc = artifact.get('D_c_1473K')
        if None in (Da, Db, Dc) or Db <= 0:
            return 0.0
        ratio_ab = Da / Db
        ratio_cb = Dc / Db
        min_ratio = step.get('min_anisotropy_ratio_a_over_b', 10)
        max_c = step.get('max_c_over_b', 0.1)
        cond1 = ratio_ab > min_ratio
        cond2 = ratio_cb < max_c
        if cond1 and cond2:
            return 1.0
        elif cond1 or cond2:
            return 0.5
        else:
            return 0.0


# === block: score_2 (check id='total_diffusion_range_check') ===
def score_2(artifact, step, ctx):
        temps = artifact.get('temperatures')
        D = artifact.get('D_total')
        if not temps or not D or len(temps) != len(D) or len(temps) != 5:
            return 0.0
        if any(d <= 0 for d in D):
            return 0.0
        if any(D[i] > D[i+1] for i in range(len(D)-1)):
            return 0.0
        min_D_1473 = step.get('min_D_total_1473', 1e-7)
        max_D_1473 = step.get('max_D_total_1473', 1e-4)
        min_D_2273 = step.get('min_D_total_2273', 1e-6)
        max_D_2273 = step.get('max_D_total_2273', 5e-4)
        try:
            idx_1473 = temps.index(1473)
            idx_2273 = temps.index(2273)
        except ValueError:
            return 0.0
        if not (min_D_1473 <= D[idx_1473] <= max_D_1473):
            return 0.0
        if not (min_D_2273 <= D[idx_2273] <= max_D_2273):
            return 0.0
        return 1.0


_SCORERS = {
    'activation_energy_check': score_0,
    'diffusion_anisotropy_check': score_1,
    'total_diffusion_range_check': score_2,
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
