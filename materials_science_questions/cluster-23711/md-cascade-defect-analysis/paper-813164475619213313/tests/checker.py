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
    return {}


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    import sys

    def score(artifact, step, ctx):
        try:
            times = [float(r['time_ps']) for r in artifact]
            kin = [float(r['kinetic_norm']) for r in artifact]
            pot = [float(r['potential_norm']) for r in artifact]
        except Exception:
            return 0.0
        score_val = 0.0
        # 1) kinetic_norm drops below 0.55
        t_kin = None
        for t, k in zip(times, kin):
            if k < 0.55:
                t_kin = t
                break
        if t_kin is not None and 0.2 <= t_kin <= 0.5:
            score_val += 0.4
        # 2) potential_norm rises above 0.45
        t_pot = None
        for t, p in zip(times, pot):
            if p > 0.45:
                t_pot = t
                break
        if t_pot is not None and 0.2 <= t_pot <= 0.5:
            score_val += 0.4
        # 3) final state
        if kin[-1] < 0.6 and pot[-1] > 0.4:
            score_val += 0.2
        return min(score_val, 1.0)


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    import sys

    def score(artifact, step, ctx):
        try:
            kin = [float(r['kinetic_norm']) for r in artifact]
            pot = [float(r['potential_norm']) for r in artifact]
        except Exception:
            return 0.0
        score_val = 0.0
        if min(kin) >= 0.85:
            score_val += 0.5
        if max(pot) <= 0.15:
            score_val += 0.5
        return score_val


# === block: score_2 (check id='step_03') ===
def score_2(artifact, step, ctx):
    import sys

    def score(artifact, step, ctx):
        try:
            energies = [float(r['energy_keV']) for r in artifact]
            volumes = [float(r['max_volume_nm3']) for r in artifact]
        except Exception:
            return 0.0
        n = len(energies)
        if n < 2:
            return 0.0
        sum_xy = sum(e * v for e, v in zip(energies, volumes))
        sum_x2 = sum(e * e for e in energies)
        if sum_x2 == 0:
            return 0.0
        slope = sum_xy / sum_x2
        target = float(step.get('target', 9.0))
        tol_rel = float(step.get('tolerance', 0.5))
        rel_diff = abs(slope - target) / target
        if rel_diff <= tol_rel:
            return 1.0
        if rel_diff <= 2 * tol_rel:
            return 0.5
        return 0.0


_SCORERS = {
    'step_01': score_0,
    'step_02': score_1,
    'step_03': score_2,
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
