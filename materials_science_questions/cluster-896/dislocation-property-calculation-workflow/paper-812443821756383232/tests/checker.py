import os
import json
import csv

# === author imports / helpers ===
import json, math


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
    if artifact is None:
        return 0.0

    surface = artifact.get('surface', [])
    saddle = artifact.get('saddle_point', None)

    # 1. Grid validity (weight 0.05)
    score1 = 0.0
    grid_ok = False
    if isinstance(surface, list) and len(surface) == 117:
        valid = True
        for item in surface:
            if not (isinstance(item.get('r_p'), (int, float)) and isinstance(item.get('r_s'), (int, float)) and isinstance(item.get('E_I'), (int, float))):
                valid = False
                break
            if not (8.0 <= item['r_p'] <= 12.0 and 0.0 <= item['r_s'] <= 3.0):
                valid = False
                break
        if valid:
            score1 = 0.05
            grid_ok = True

    # 2. Discrete saddle‑point detection (weight 0.95)
    score2 = 0.0
    if grid_ok:
        grid = {(item['r_p'], item['r_s']): item['E_I'] for item in surface}
        rp_vals = sorted(set(item['r_p'] for item in surface))
        rs_vals = sorted(set(item['r_s'] for item in surface))

        saddle_candidates = []
        for i_rp in range(1, len(rp_vals)-1):
            r_p = rp_vals[i_rp]
            for i_rs in range(1, len(rs_vals)-1):
                r_s = rs_vals[i_rs]
                r_s_prev = rs_vals[i_rs-1]
                r_s_next = rs_vals[i_rs+1]
                r_p_prev = rp_vals[i_rp-1]
                r_p_next = rp_vals[i_rp+1]

                E = grid[(r_p, r_s)]
                E_rs_prev = grid[(r_p, r_s_prev)]
                E_rs_next = grid[(r_p, r_s_next)]
                E_rp_prev = grid[(r_p_prev, r_s)]
                E_rp_next = grid[(r_p_next, r_s)]

                if E > E_rs_prev and E > E_rs_next and E < E_rp_prev and E < E_rp_next:
                    saddle_candidates.append((r_p, r_s, E))

        # check whether the reported saddle matches a detected candidate
        reported_matches = False
        if isinstance(saddle, dict) and all(k in saddle for k in ('r_p_saddle', 'r_s_saddle', 'E_saddle')):
            rps = saddle['r_p_saddle']
            rss = saddle['r_s_saddle']
            es  = saddle['E_saddle']
            for cand_rp, cand_rs, cand_e in saddle_candidates:
                if abs(rps - cand_rp) <= 0.25 and abs(rss - cand_rs) <= 0.125:
                    # loose energy consistency check (prevents completely bogus labels)
                    if abs(es - cand_e) <= 0.01 * abs(cand_e) + 0.1:
                        reported_matches = True
                        break

        if reported_matches:
            score2 = 0.95
        elif len(saddle_candidates) > 0:
            score2 = 0.7   # saddle exists but report is inaccurate

    return score1 + score2


_SCORERS = {
    'step_01': score_0,
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
