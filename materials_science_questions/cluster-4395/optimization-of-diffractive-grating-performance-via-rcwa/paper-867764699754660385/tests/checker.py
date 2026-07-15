import os
import json
import csv

# === author imports / helpers ===
import csv, os, json


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
    def prepare(outputs_dir, spec):
        eff_path = os.path.join(outputs_dir, 'efficiency.txt')
        if os.path.exists(eff_path):
            with open(eff_path, 'r') as f:
                val = float(f.read().strip())
        else:
            val = 0.0
        return {'efficiency_from_file': val}


# === block: score_0 (check id='gen_rate') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not artifact or len(artifact) < 2:
            return 0.0
        try:
            sorted_art = sorted(artifact, key=lambda r: float(r.get('z', 0)))
        except Exception:
            return 0.0
        prev = None
        for row in sorted_art:
            try:
                g = float(row['G'])
            except Exception:
                return 0.0
            if prev is not None and g > prev + 1e-6:
                return 0.0
            prev = g
        for row in artifact:
            try:
                if float(row['G']) < 0:
                    return 0.0
            except Exception:
                return 0.0
        return 1.0


# === block: score_1 (check id='jv_curve') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not artifact or len(artifact) < 2:
            return 0.0
        sorted_art = sorted(artifact, key=lambda row: float(row['Vext']))
        prev = None
        monotonic = True
        for row in sorted_art:
            j = float(row['J'])
            if prev is not None and j > prev + 1e-6:
                monotonic = False
                break
            prev = j
        max_power = 0.0
        for row in artifact:
            V = float(row['Vext'])
            J_val = float(row['J'])
            power = J_val * V
            if power > max_power:
                max_power = power
        eta_from_jv = max_power
        eta_from_file = ctx.get('efficiency_from_file', None)
        if eta_from_file is None:
            return 0.0
        rel_err = abs(eta_from_jv - eta_from_file) / max(eta_from_file, 1e-9)
        consist_ok = 1.0 if rel_err <= step.get('params', {}).get('tolerance_rel', 0.05) else 0.0
        return 0.5 * (1.0 if monotonic else 0.0) + 0.5 * consist_ok


# === block: score_2 (check id='efficiency') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        try:
            val = float(artifact.strip())
        except:
            return 0.0
        ref = float(step['params']['reference'])
        min_ratio = float(step['params']['min_acceptable_ratio'])
        min_acc = ref * min_ratio
        if val >= ref - 1e-6:
            return 1.0
        score = max(0.0, (val - min_acc) / (ref - min_acc))
        return min(1.0, score)


_SCORERS = {
    'gen_rate': score_0,
    'jv_curve': score_1,
    'efficiency': score_2,
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
