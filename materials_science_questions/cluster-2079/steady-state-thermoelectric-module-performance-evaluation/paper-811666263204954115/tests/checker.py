import os
import json
import csv

# === author imports / helpers ===
import json
import csv
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


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not isinstance(rows, list) or len(rows) < 20:
        return 0.0
    cols_ok = all(col in rows[0] for col in ['I','V','P','eta','T_h','T_c'])
    if not cols_ok:
        return 0.0
    score = 0.0
    score += 0.3  # existence of columns and min rows
    # numeric conversion
    try:
        I = [float(r['I']) for r in rows]
        V = [float(r['V']) for r in rows]
        P = [float(r['P']) for r in rows]
        eta = [float(r['eta']) for r in rows]
        T_h = [float(r['T_h']) for r in rows]
        T_c = [float(r['T_c']) for r in rows]
    except (ValueError, KeyError):
        return 0.0
    # I monotonically increasing? assume sorted
    if I == sorted(I):
        # V should monotonically decrease (or at least non-increasing)
        if all(V[i] >= V[i+1] for i in range(len(V)-1)):
            score += 0.3
        else:
            score += 0.0
    else:
        # if not sorted, penalize slightly but check trend anyway
        # just give a small fraction if still reasonable
        pass
    # P >= 0 and eta >= 0
    if all(p >= 0 for p in P) and all(e >= 0 for e in eta):
        score += 0.2
    else:
        score += 0.0
    # T_h > T_c for all rows
    if all(th > tc for th, tc in zip(T_h, T_c)):
        score += 0.2
    else:
        score += 0.0
    return min(score, 1.0)


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    json_artifact = artifact
    csv_path = '/app/outputs/step_01_simulation_results.csv'
    csv_rows = []
    with open(csv_path, newline='') as f:
        reader = csv.DictReader(f)
        csv_rows = list(reader)
    if not csv_rows:
        return 0.0
    # recompute metrics from CSV
    I = [float(r['I']) for r in csv_rows]
    V = [float(r['V']) for r in csv_rows]
    P = [float(r['P']) for r in csv_rows]
    eta = [float(r['eta']) for r in csv_rows]
    # V_oc: voltage at smallest I (closest to zero)
    min_i_idx = I.index(min(I))
    V_oc_csv = V[min_i_idx]
    # I_sc: interpolate current where V=0
    # find where V crosses zero
    I_sc_csv = None
    for i in range(len(V)-1):
        if V[i] * V[i+1] <= 0:
            if V[i] == V[i+1]:
                continue
            frac = -V[i] / (V[i+1] - V[i])
            I_sc_csv = I[i] + frac * (I[i+1] - I[i])
            break
    if I_sc_csv is None:
        # if no crossing, take max I
        I_sc_csv = max(I)
    P_max_csv = max(P)
    eta_max_csv = max(eta)
    # Check JSON consistency
    json_V_oc = json_artifact.get('V_oc')
    json_I_sc = json_artifact.get('I_sc')
    json_P_max = json_artifact.get('P_max')
    json_eta_max = json_artifact.get('eta_max')
    if None in (json_V_oc, json_I_sc, json_P_max, json_eta_max):
        consistency = 0.0
    else:
        # allow small relative tolerance for consistency
        tol = 0.01
        c1 = abs(json_V_oc - V_oc_csv) <= tol * max(abs(V_oc_csv), 1e-6)
        c2 = abs(json_I_sc - I_sc_csv) <= tol * max(abs(I_sc_csv), 1e-6)
        c3 = abs(json_P_max - P_max_csv) <= tol * max(abs(P_max_csv), 1e-6)
        c4 = abs(json_eta_max - eta_max_csv) <= tol * max(abs(eta_max_csv), 1e-6)
        consistency = 1.0 if all([c1, c2, c3, c4]) else 0.0
    # Use recomputed values (or JSON if consistent, for robustness)
    use_V_oc = V_oc_csv
    use_I_sc = I_sc_csv
    use_P_max = P_max_csv
    use_eta_max = eta_max_csv
    if consistency == 1.0 and all(v is not None for v in [json_V_oc, json_I_sc, json_P_max, json_eta_max]):
        use_V_oc = json_V_oc
        use_I_sc = json_I_sc
        use_P_max = json_P_max
        use_eta_max = json_eta_max
    # Compare to gold tolerances
    t = step.get('targets', {})
    def metric_score(name, value, cfg):
        target = cfg.get('value')
        if 'rel_tol' in cfg and cfg['rel_tol']:
            tol = cfg['rel_tol'] * abs(target)
        else:
            tol = cfg.get('abs_tol', 0.01)
        if abs(value - target) <= tol:
            return 1.0
        # gradient partial credit: linearly decay to 0 at 3*tol
        err = abs(value - target)
        if err >= 3*tol:
            return 0.0
        return 1.0 - (err - tol) / (2*tol)
    scores = []
    scores.append(metric_score('V_oc', use_V_oc, t.get('V_oc', {})))
    scores.append(metric_score('I_sc', use_I_sc, t.get('I_sc', {})))
    scores.append(metric_score('P_max', use_P_max, t.get('P_max', {})))
    scores.append(metric_score('eta_max', use_eta_max, t.get('eta_max', {})))
    accuracy = sum(scores) / 4.0
    final = 0.2 * consistency + 0.8 * accuracy
    return min(max(final, 0.0), 1.0)


_SCORERS = {
    'step_01': score_0,
    'step_02': score_1,
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
