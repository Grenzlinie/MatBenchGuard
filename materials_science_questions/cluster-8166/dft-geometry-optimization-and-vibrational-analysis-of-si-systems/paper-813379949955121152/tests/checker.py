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
    return {}  # no shared context needed; gold is in step params


# === block: score_0 (check id='ef_recompute_consistency') ===
def score_0(artifact, step, ctx):
    data = artifact  # list of dicts
    if not isinstance(data, list) or len(data) != 3:
        return 0.0
    tol = step['params']['tolerance_eV']
    for entry in data:
        try:
            ef_computed = entry['E_doped'] - entry['E_perfect'] - entry['E_H']
            if abs(ef_computed - entry['formation_energy_eV']) > tol:
                return 0.0
        except (KeyError, TypeError):
            return 0.0
    return 1.0


# === block: score_1 (check id='formation_energy_reference') ===
def score_1(artifact, step, ctx):
    data = artifact
    if not isinstance(data, list) or len(data) != 3:
        return 0.0
    gold = step['params']['gold']
    tol = step['params']['tolerance_eV']
    # recompute formation energies from raw totals, just as in consistency check
    sites_ef = {}
    for entry in data:
        try:
            ef = entry['E_doped'] - entry['E_perfect'] - entry['E_H']
            sites_ef[entry['site']] = ef
        except (KeyError, TypeError):
            return 0.0
    # per-site value scores
    if not all(s in gold for s in sites_ef):
        return 0.0
    site_scores = []
    for site, ef in sites_ef.items():
        delta = abs(ef - gold[site])
        # linear decay: full credit at delta <= tol, 0 at delta >= 2*tol
        s = max(0.0, 1.0 - delta / (2 * tol))
        site_scores.append(s)
    avg_val_score = sum(site_scores) / len(site_scores)
    # ordering score: max(Ef(I-SiC), Ef(I-SiTi)) <= Ef(I-Ti) + small slack
    ordering_slack = 0.05  # eV
    ef_ti = sites_ef.get('I-Ti')
    ef_sic = sites_ef.get('I-SiC')
    ef_siti = sites_ef.get('I-SiTi')
    if ef_ti is None or ef_sic is None or ef_siti is None:
        return 0.0
    ordering_score = 1.0 if max(ef_sic, ef_siti) <= ef_ti + ordering_slack else 0.0
    # combine with equal weight
    return 0.5 * avg_val_score + 0.5 * ordering_score


# === block: score_2 (check id='volume_change_reference') ===
def score_2(artifact, step, ctx):
    data = artifact
    if not isinstance(data, list) or len(data) != 3:
        return 0.0
    gold = step['params']['gold']
    tol = step['params']['tolerance_pp']
    sites_dv = {}
    for entry in data:
        try:
            sites_dv[entry['site']] = entry['volume_change_percent']
        except (KeyError, TypeError):
            return 0.0
    if not all(s in gold for s in sites_dv):
        return 0.0
    # per-site value scores (tolerance in percentage points)
    site_scores = []
    for site, dv in sites_dv.items():
        delta = abs(dv - gold[site])
        s = max(0.0, 1.0 - delta / (2 * tol))
        site_scores.append(s)
    avg_val_score = sum(site_scores) / len(site_scores)
    # ordering: dV(I-SiC) <= dV(I-SiTi) <= dV(I-Ti)
    dv_sic = sites_dv.get('I-SiC')
    dv_siti = sites_dv.get('I-SiTi')
    dv_ti = sites_dv.get('I-Ti')
    if dv_sic is None or dv_siti is None or dv_ti is None:
        return 0.0
    # allow small slack for near-ordering
    slack = 0.05  # percentage points
    if dv_sic <= dv_siti + slack and dv_siti <= dv_ti + slack:
        ordering_score = 1.0
    else:
        ordering_score = 0.0
    return 0.5 * avg_val_score + 0.5 * ordering_score


# === block: score_3 (check id='constant_energies') ===
def score_3(artifact, step, ctx):
    data = artifact
    if not isinstance(data, list) or len(data) != 3:
        return 0.0
    try:
        e_perfects = [entry['E_perfect'] for entry in data]
        e_hs = [entry['E_H'] for entry in data]
    except (KeyError, TypeError):
        return 0.0
    tol = step['params']['tolerance_eV']
    if max(e_perfects) - min(e_perfects) <= tol and max(e_hs) - min(e_hs) <= tol:
        return 1.0
    else:
        return 0.0


_SCORERS = {
    'ef_recompute_consistency': score_0,
    'formation_energy_reference': score_1,
    'volume_change_reference': score_2,
    'constant_energies': score_3,
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
