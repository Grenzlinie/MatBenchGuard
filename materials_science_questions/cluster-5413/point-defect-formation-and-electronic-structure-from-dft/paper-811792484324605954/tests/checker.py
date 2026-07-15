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
    import os, json
    step_01_path = os.path.join(outputs_dir, 'step_01_binding_energies.json')
    try:
        with open(step_01_path) as f:
            step_01 = json.load(f)
        clusters = {c['label']: c['delta_E'] for c in step_01.get('clusters', []) if isinstance(c, dict) and 'label' in c and 'delta_E' in c}
    except Exception:
        step_01 = None
        clusters = {}
    return {'clusters': clusters, 'step_01': step_01}


# === block: score_0 (check id='step_00') ===
def score_0(artifact, step, ctx):
    import math
    targets = step.get('hidden_targets', {})
    tol = step.get('tolerance_abs', 0.1)
    total = len(targets)
    if total == 0:
        return 1.0
    ok = 0
    for path, expected in targets.items():
        parts = path.split('.')
        val = artifact
        try:
            for p in parts:
                val = val[p]
            if abs(val - expected) <= tol:
                ok += 1
        except (KeyError, TypeError):
            pass
    return ok / total


# === block: score_1 (check id='step_01') ===
def score_1(artifact, step, ctx):
    targets = step.get('reaction_targets', {})
    react_tol = step.get('reaction_tolerance', 0.15)
    cluster_targets = step.get('cluster_targets', {})
    cluster_tol = step.get('cluster_tolerance', 0.1)
    total = len(targets) + len(cluster_targets)
    if total == 0:
        return 1.0
    ok = 0
    # check reaction energies
    if isinstance(artifact.get('reaction_energies'), dict):
        for key, expected in targets.items():
            val = artifact['reaction_energies'].get(key)
            if val is not None and abs(val - expected) <= react_tol:
                ok += 1
    # check clusters
    actual_clusters = {c['label']: c['delta_E'] for c in artifact.get('clusters', []) if isinstance(c, dict) and 'label' in c and 'delta_E' in c}
    for label, expected in cluster_targets.items():
        val = actual_clusters.get(label)
        if val is not None and abs(val - expected) <= cluster_tol:
            ok += 1
    return ok / total


# === block: score_2 (check id='step_02') ===
def score_2(artifact, step, ctx):
    clusters_lookup = ctx.get('clusters', {})
    expected_labels = step.get('expected_labels', {})
    try:
        ni_n1 = clusters_lookup.get(expected_labels.get('Ni_n1', ''), None)
        ni_n2 = clusters_lookup.get(expected_labels.get('Ni_n2', ''), None)
        gd_n1 = clusters_lookup.get(expected_labels.get('Gd_n1', ''), None)
        gd_n2 = clusters_lookup.get(expected_labels.get('Gd_n2', ''), None)
    except (TypeError, KeyError):
        ni_n1 = ni_n2 = gd_n1 = gd_n2 = None
    score = 0.0
    checks = 0
    # Ni clusters
    if isinstance(artifact.get('Ni_clusters'), list):
        ni_sub = {item.get('n_vacancies'): item for item in artifact['Ni_clusters'] if isinstance(item, dict)}
        if 1 in ni_sub and ni_n1 is not None:
            d = ni_sub[1]
            if abs(d.get('delta_E', 0) - ni_n1) <= 0.02:
                score += 0.1
            if abs(d.get('delta_E_per_vac', 0) - (ni_n1/1)) <= 0.02:
                score += 0.05
            checks += 2
        if 2 in ni_sub and ni_n2 is not None:
            d = ni_sub[2]
            if abs(d.get('delta_E', 0) - ni_n2) <= 0.02:
                score += 0.1
            if abs(d.get('delta_E_per_vac', 0) - (ni_n2/2)) <= 0.02:
                score += 0.05
            checks += 2
    # Gd clusters
    if isinstance(artifact.get('Gd_clusters'), list):
        gd_sub = {item.get('n_vacancies'): item for item in artifact['Gd_clusters'] if isinstance(item, dict)}
        if 1 in gd_sub and gd_n1 is not None:
            d = gd_sub[1]
            if abs(d.get('delta_E', 0) - gd_n1) <= 0.02:
                score += 0.1
            if abs(d.get('delta_E_per_vac', 0) - (gd_n1/1)) <= 0.02:
                score += 0.05
            checks += 2
        if 2 in gd_sub and gd_n2 is not None:
            d = gd_sub[2]
            if abs(d.get('delta_E', 0) - gd_n2) <= 0.02:
                score += 0.1
            if abs(d.get('delta_E_per_vac', 0) - (gd_n2/2)) <= 0.02:
                score += 0.05
            checks += 2
    # increase checks
    try:
        inc_ni = artifact.get('increase_Ni')
        inc_gd = artifact.get('increase_Gd')
        if ni_n1 is not None and ni_n2 is not None:
            exp_ni_delta = ni_n2 - ni_n1
            exp_ni_per_vac = (ni_n2/2) - (ni_n1/1)
            if inc_ni:
                if abs(inc_ni.get('delta_E', 0) - exp_ni_delta) <= 0.02:
                    score += 0.1
                if abs(inc_ni.get('delta_E_per_vac', 0) - exp_ni_per_vac) <= 0.02:
                    score += 0.05
            checks += 2
        if gd_n1 is not None and gd_n2 is not None:
            exp_gd_delta = gd_n2 - gd_n1
            exp_gd_per_vac = (gd_n2/2) - (gd_n1/1)
            if inc_gd:
                if abs(inc_gd.get('delta_E', 0) - exp_gd_delta) <= 0.02:
                    score += 0.1
                if abs(inc_gd.get('delta_E_per_vac', 0) - exp_gd_per_vac) <= 0.02:
                    score += 0.05
            checks += 2
    except Exception:
        pass
    # trend checks (require both Ni and Gd data)
    if ni_n1 is not None and ni_n2 is not None and gd_n1 is not None and gd_n2 is not None:
        ni_delta_inc = ni_n2 - ni_n1
        gd_delta_inc = gd_n2 - gd_n1
        ni_pervac_inc = (ni_n2/2) - (ni_n1/1)
        gd_pervac_inc = (gd_n2/2) - (gd_n1/1)
        if ni_delta_inc > gd_delta_inc:
            score += 0.05
        if ni_pervac_inc > gd_pervac_inc:
            score += 0.05
        checks += 2
    if checks == 0:
        return 0.0
    else:
        return min(score / checks, 1.0)


_SCORERS = {
    'step_00': score_0,
    'step_01': score_1,
    'step_02': score_2,
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
