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


# === block: score_0 (check id='step_coexistence') ===
def score_0(artifact, step, ctx):
    try:
        tc_val = None
        for row in artifact:
            n_val = str(row.get('N', '')).strip()
            if n_val.lower() == 'tc':
                tc_val = float(row.get('x_B_coex', float('nan')))
                break
        if tc_val is None:
            # fallback: maybe Tc row has empty T
            for row in artifact:
                if str(row.get('T', '')).strip() == '' and row.get('N','') == 'Tc':
                    tc_val = float(row.get('x_B_coex', float('nan')))
                    break
        if tc_val is None:
            return 0.0
        target_tc = step['target']['Tc']['value']
        tol = step['target']['Tc']['tolerance']
        diff = abs(tc_val - target_tc)
        score = max(0.0, 1.0 - diff / (2*tol))
        return score
    except Exception:
        return 0.0


# === block: score_1 (check id='step_static') ===
def score_1(artifact, step, ctx):
    try:
        ref = step['target']['reference']
        tols = step['target']['tolerances']
        by_T = {}
        for row in artifact:
            by_T[str(row.get('T', '')).strip()] = row
        scores = []
        for T_str, exp in ref.items():
            row = by_T.get(T_str)
            if row is None:
                scores.append(0.0)
                continue
            try:
                k_val = float(row['kappa_T'])
                chi_val = float(row['chi'])
            except (ValueError, KeyError):
                scores.append(0.0)
                continue
            k_ref = exp['kappa_T']
            k_rel_err = abs(k_val - k_ref) / (abs(k_ref) + 1e-12)
            k_abs_err = abs(k_val - k_ref)
            if k_rel_err <= tols['kappa_T']['rel_tol'] or k_abs_err <= tols['kappa_T']['abs_tol']:
                k_score = 1.0
            else:
                k_score = max(0.0, 1.0 - (k_rel_err - tols['kappa_T']['rel_tol']) / 0.5)
            chi_ref = exp['chi']
            chi_rel_err = abs(chi_val - chi_ref) / (abs(chi_ref) + 1e-12)
            chi_abs_err = abs(chi_val - chi_ref)
            if chi_rel_err <= tols['chi']['rel_tol'] or chi_abs_err <= tols['chi']['abs_tol']:
                chi_score = 1.0
            else:
                chi_score = max(0.0, 1.0 - (chi_rel_err - tols['chi']['rel_tol']) / 0.5)
            scores.append(0.5 * k_score + 0.5 * chi_score)
        return sum(scores) / len(scores) if scores else 0.0
    except Exception:
        return 0.0


# === block: score_2 (check id='step_viscosities') ===
def score_2(artifact, step, ctx):
    try:
        ref = step['target']['reference']
        tols = step['target']['tolerances']
        by_T = {}
        for row in artifact:
            by_T[str(row.get('T', '')).strip()] = row
        scores = []
        eta_B_vals = []
        temps_ordered = sorted(ref.keys(), key=lambda x: float(x))
        for T_str in temps_ordered:
            exp = ref[T_str]
            row = by_T.get(T_str)
            if row is None:
                scores.append(0.0)
                eta_B_vals.append(None)
                continue
            try:
                es = float(row['eta_s'])
                eb = float(row['eta_B'])
                # column name as per contract
                ratio_col = [c for c in row if 'ratio' in c.lower()]
                ratio = float(row[ratio_col[0]]) if ratio_col else 0.0
            except (ValueError, KeyError):
                scores.append(0.0)
                eta_B_vals.append(None)
                continue
            es_ref = exp['eta_s']
            es_rel_err = abs(es - es_ref) / (abs(es_ref) + 1e-12)
            es_score = 1.0 if es_rel_err <= tols['eta_s']['rel_tol'] else max(0.0, 1.0 - es_rel_err / 0.5)
            eb_ref = exp['eta_B']
            eb_rel_err = abs(eb - eb_ref) / (abs(eb_ref) + 1e-12)
            eb_score = 1.0 if eb_rel_err <= tols['eta_B']['rel_tol'] else max(0.0, 1.0 - eb_rel_err / 0.5)
            ratio_ref = exp['ratio']
            ratio_rel_err = abs(ratio - ratio_ref) / (abs(ratio_ref) + 1e-12)
            ratio_score = 1.0 if ratio_rel_err <= tols['ratio']['rel_tol'] else max(0.0, 1.0 - ratio_rel_err / 0.3)
            scores.append((es_score + eb_score + ratio_score) / 3.0)
            eta_B_vals.append(eb)
        trend_ok = True
        eb_clean = [v for v in eta_B_vals if v is not None]
        for i in range(len(eb_clean) - 1):
            if eb_clean[i] <= eb_clean[i+1]:
                trend_ok = False
                break
        factor = 1.0 if trend_ok else 0.5
        avg_score = sum(scores) / len(scores) if scores else 0.0
        return min(1.0, avg_score * factor)
    except Exception:
        return 0.0


_SCORERS = {
    'step_coexistence': score_0,
    'step_static': score_1,
    'step_viscosities': score_2,
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
