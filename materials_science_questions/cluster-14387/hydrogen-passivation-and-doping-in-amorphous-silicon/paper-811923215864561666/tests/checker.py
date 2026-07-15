import os
import json
import csv

# === author imports / helpers ===
import math

def calc_avg(vals):
    return sum(vals)/len(vals) if vals else 0.0

def score_orbital_character(bands, step, has_ca):
    sigma_bands = [b for b in bands if 1 <= b['band_index'] <= 6]
    pi_bands = [b for b in bands if 7 <= b['band_index'] <= 8]
    s_bands = [b for b in bands if 9 <= b['band_index'] <= 10]

    sigma_score = 1.0 if calc_avg([b['px']+b['py'] for b in sigma_bands]) >= step.get('sigma_threshold',0.5) else 0.0
    pi_score = 1.0 if calc_avg([b['pz'] for b in pi_bands]) >= step.get('pi_threshold',0.5) else 0.0
    s_score = 1.0 if calc_avg([b['s'] for b in s_bands]) >= step.get('s_threshold',0.5) else 0.0

    scores = [sigma_score, pi_score, s_score]
    total = 3
    if has_ca:
        pd_threshold_p = step.get('pi_d_threshold_sip',0.2)
        pd_threshold_d = step.get('pi_d_threshold_cad',0.2)
        pd_found = False
        for b in bands:
            d_Ca = b.get('d_Ca')
            if isinstance(d_Ca, dict):
                si_p = b.get('px',0)+b.get('py',0)+b.get('pz',0)
                ca_d = sum(d_Ca.get(k,0) for k in ('d_xy','d_yz','d_z2','d_xz'))
                if si_p >= pd_threshold_p and ca_d >= pd_threshold_d:
                    pd_found = True
                    break
        scores.append(1.0 if pd_found else 0.0)
        total = 4
    return sum(scores)/total


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


# === block: score_0 (check id='char_casi2_alb2') ===
def score_0(artifact, step, ctx):
    return score_orbital_character(artifact, step, has_ca=True)


# === block: score_1 (check id='char_casi2_ths2') ===
def score_1(artifact, step, ctx):
    return score_orbital_character(artifact, step, has_ca=True)


# === block: score_2 (check id='char_si_alb2') ===
def score_2(artifact, step, ctx):
    return score_orbital_character(artifact, step, has_ca=False)


# === block: score_3 (check id='char_si_ths2') ===
def score_3(artifact, step, ctx):
    return score_orbital_character(artifact, step, has_ca=False)


_SCORERS = {
    'char_casi2_alb2': score_0,
    'char_casi2_ths2': score_1,
    'char_si_alb2': score_2,
    'char_si_ths2': score_3,
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
