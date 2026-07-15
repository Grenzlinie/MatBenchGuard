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


# === block: score_0 (check id='epc_numeric') ===
def score_0(artifact, step, ctx):
    artifact_dict = artifact
    refs = step['reference']
    tols = step['tolerances']
    systems = ['0.2e_strain_0pct', '0.2e_strain_5pct', 'Li_deposited']
    scores = []
    for sys in systems:
        if sys not in artifact_dict:
            scores.append(0.0)
            continue
        vals = artifact_dict[sys]
        ref = refs[sys]
        # lambda
        lam = vals.get('lambda')
        lam_ref = ref['lambda']
        lam_tol = tols['lambda']
        if lam is None:
            sl = 0.0
        else:
            diff = abs(lam - lam_ref)
            if diff <= lam_tol:
                sl = 1.0
            else:
                sl = max(0.0, 1.0 - (diff - lam_tol) / (lam_tol * 3.0))
        # omega_log
        olog = vals.get('omega_log_cm1')
        olog_ref = ref['omega_log_cm1']
        olog_tol = tols['omega_log_cm1']
        if olog is None:
            so = 0.0
        else:
            diff = abs(olog - olog_ref)
            if diff <= olog_tol:
                so = 1.0
            else:
                so = max(0.0, 1.0 - (diff - olog_tol) / (olog_tol * 3.0))
        # Tc
        tc = vals.get('Tc_K')
        tc_ref = ref['Tc_K']
        if tc is None:
            st = 0.0
        else:
            if tc_ref == 0:
                st = 1.0 if tc <= tols['Tc_K_zero'] else 0.0
            else:
                diff = abs(tc - tc_ref)
                tc_tol = tols['Tc_K_nonzero']
                if diff <= tc_tol:
                    st = 1.0
                else:
                    st = max(0.0, 1.0 - (diff - tc_tol) / (tc_tol * 3.0))
        score_sys = (sl + so + st) / 3.0
        scores.append(score_sys)
    return sum(scores) / len(systems) if systems else 0.0


# === block: score_1 (check id='epc_trend') ===
def score_1(artifact, step, ctx):
    artifact_dict = artifact
    required_systems = ['0.2e_strain_0pct', '0.2e_strain_5pct', 'Li_deposited']
    if not all(sys in artifact_dict for sys in required_systems):
        return 0.0
    d = {sys: artifact_dict[sys] for sys in required_systems}
    # lambda: 0pct < 5pct < Li
    cond_lambda = (d['0.2e_strain_0pct']['lambda'] < d['0.2e_strain_5pct']['lambda'] < d['Li_deposited']['lambda'])
    # omega_log: 0pct > 5pct > Li
    cond_omega = (d['0.2e_strain_0pct']['omega_log_cm1'] > d['0.2e_strain_5pct']['omega_log_cm1'] > d['Li_deposited']['omega_log_cm1'])
    # Tc: 0pct and 5pct zero (≤0.5), Li > 0.5 and > both
    cond_tc = (d['0.2e_strain_0pct']['Tc_K'] <= 0.5 and d['0.2e_strain_5pct']['Tc_K'] <= 0.5 and d['Li_deposited']['Tc_K'] > 0.5 and d['Li_deposited']['Tc_K'] > d['0.2e_strain_0pct']['Tc_K'] and d['Li_deposited']['Tc_K'] > d['0.2e_strain_5pct']['Tc_K'])
    if cond_lambda and cond_omega and cond_tc:
        return 1.0
    else:
        return 0.0


_SCORERS = {
    'epc_numeric': score_0,
    'epc_trend': score_1,
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
