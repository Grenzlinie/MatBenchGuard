import os
import json
import csv


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
    gold = spec.get("hidden_gold", {})
    return {"gold": gold}


# === block: score_0 (check id='schema_check') ===
def score_0(artifact, step, ctx):
    required = ["formation_energy", "HOMO_undoped", "HOMO_doped", "LUMO_undoped", "LUMO_doped", "effective_work_function_undoped", "effective_work_function_doped", "ldos_undoped", "ldos_doped", "anti_bonding_peak_undoped", "anti_bonding_peak_doped"]
    return 1.0 if all(k in artifact for k in required) else 0.0


# === block: score_1 (check id='peak_recompute') ===
def score_1(artifact, step, ctx):
    gold = ctx.get("gold", {})
    target_undoped = gold.get("anti_bonding_peak_undoped", 0.8)
    target_doped = gold.get("anti_bonding_peak_doped", 0.15)
    tol = 0.20

    def find_peak(ldos):
        energy = ldos.get("energy", [])
        dos = ldos.get("total_dos", [])
        if len(energy) != len(dos) or len(energy) == 0:
            return None
        best_e, best_v = None, -1e9
        for e, d in zip(energy, dos):
            if 0.0 <= e <= 1.5 and d > best_v:
                best_v = d
                best_e = e
        return best_e

    peak_u = find_peak(artifact.get("ldos_undoped", {}))
    peak_d = find_peak(artifact.get("ldos_doped", {}))
    if peak_u is None or peak_d is None:
        return 0.0

    score_closeness = 0.0
    if abs(peak_u - target_undoped) <= tol and abs(peak_d - target_doped) <= tol:
        score_closeness = 1.0
    else:
        du = abs(peak_u - target_undoped)
        dd = abs(peak_d - target_doped)
        su = max(0.0, 1.0 - du / (3 * tol))
        sd = max(0.0, 1.0 - dd / (3 * tol))
        score_closeness = (su + sd) / 2.0

    score_trend = 1.0 if peak_d < peak_u else 0.0
    return 0.5 * score_closeness + 0.5 * score_trend


# === block: score_2 (check id='ldos_ef') ===
def score_2(artifact, step, ctx):
    def ldos_at_ef(ldos):
        energy = ldos.get("energy", [])
        dos = ldos.get("total_dos", [])
        if len(energy) != len(dos) or len(energy) == 0:
            return None
        idx = 0
        dist = abs(energy[0] - 0.0)
        for i, e in enumerate(energy):
            d = abs(e - 0.0)
            if d < dist:
                dist = d
                idx = i
        return dos[idx]

    dos_u = ldos_at_ef(artifact.get("ldos_undoped", {}))
    dos_d = ldos_at_ef(artifact.get("ldos_doped", {}))
    if dos_u is None or dos_d is None:
        return 0.0
    return 1.0 if dos_d > dos_u else 0.0


# === block: score_3 (check id='formation_energy') ===
def score_3(artifact, step, ctx):
    gold = ctx.get("gold", {})
    target = gold.get("formation_energy", 1.19)
    tol = 0.10
    reported = artifact.get("formation_energy")
    if reported is None:
        return 0.0
    diff = abs(reported - target)
    if diff <= tol:
        return 1.0
    return max(0.0, 1.0 - (diff - tol) / (2 * tol))


# === block: score_4 (check id='homo_lumo') ===
def score_4(artifact, step, ctx):
    gold = ctx.get("gold", {})
    targets = {
        "HOMO_undoped": gold.get("HOMO_undoped", -4.745),
        "HOMO_doped": gold.get("HOMO_doped", -4.708),
        "LUMO_undoped": gold.get("LUMO_undoped", -3.936),
        "LUMO_doped": gold.get("LUMO_doped", -4.124)
    }
    tol = 0.15
    scores = []
    for key, target in targets.items():
        val = artifact.get(key)
        if val is None:
            scores.append(0.0)
        else:
            diff = abs(val - target)
            if diff <= tol:
                scores.append(1.0)
            else:
                scores.append(max(0.0, 1.0 - (diff - tol) / (2 * tol)))
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_5 (check id='eff_work_function') ===
def score_5(artifact, step, ctx):
    gold = ctx.get("gold", {})
    undoped_target = gold.get("effective_work_function_undoped", 0.405)
    doped_target = gold.get("effective_work_function_doped", 0.292)
    tol = 0.15

    undoped_val = artifact.get("effective_work_function_undoped")
    doped_val = artifact.get("effective_work_function_doped")
    if undoped_val is None or doped_val is None:
        return 0.0

    def score_val(val, target):
        diff = abs(val - target)
        if diff <= tol:
            return 1.0
        return max(0.0, 1.0 - (diff - tol) / (2 * tol))

    score_u = score_val(undoped_val, undoped_target)
    score_d = score_val(doped_val, doped_target)
    trend = 1.0 if doped_val < undoped_val else 0.0
    return 0.5 * (score_u + score_d) / 2.0 + 0.5 * trend


_SCORERS = {
    'schema_check': score_0,
    'peak_recompute': score_1,
    'ldos_ef': score_2,
    'formation_energy': score_3,
    'homo_lumo': score_4,
    'eff_work_function': score_5,
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
