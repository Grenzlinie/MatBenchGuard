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


# === block: score_0 (check id='score_defect_energies') ===
def score_0(artifact, step, ctx):
        try:
            # Artifact must be a dict
            if not isinstance(artifact, dict):
                return 0.0
            gold = step.get('params', {}).get('gold', {})
            tols = step.get('params', {}).get('tolerances', {})
            if not isinstance(gold, dict) or not isinstance(tols, dict):
                return 0.0

            checks = []

            # formation energies
            fe = artifact.get('formation_energies')
            fe_gold = gold.get('formation_energies', {})
            fe_tol = tols.get('formation_energies', 0.0)
            if isinstance(fe, dict) and isinstance(fe_gold, dict):
                for k in ['Cs', 'Ci_100_DB', 'Sii_110_DB', 'V']:
                    v = fe.get(k)
                    g = fe_gold.get(k)
                    checks.append((v, g, fe_tol))
            else:
                # missing or non-dict: skip all formation checks
                pass

            # binding energies
            be = artifact.get('binding_energies')
            be_gold = gold.get('binding_energies', {})
            be_tol = tols.get('binding_energies', 0.0)
            if isinstance(be, dict) and isinstance(be_gold, dict):
                for k in ['Ci_Ci', 'Ci_V', 'Cs_Sii']:
                    v = be.get(k)
                    g = be_gold.get(k)
                    checks.append((v, g, be_tol))

            # migration barriers
            mb = artifact.get('migration_barriers')
            mb_gold = gold.get('migration_barriers', {})
            mb_tols = tols.get('migration_barriers', {})
            if isinstance(mb, dict) and isinstance(mb_gold, dict):
                for k in ['Ci_diff', 'CiV_to_Cs', 'CsSii_to_Ci']:
                    v = mb.get(k)
                    g = mb_gold.get(k)
                    t = mb_tols.get(k, 0.0) if isinstance(mb_tols, dict) else 0.0
                    checks.append((v, g, t))

            # md_result
            v_md = artifact.get('md_result', '')
            g_md = gold.get('md_result', '')
            checks.append((v_md, g_md, None))

            passed = 0
            for v, g, tol in checks:
                if v is None or g is None:
                    continue
                if tol is None:
                    # exact string match
                    if str(v) == str(g):
                        passed += 1
                else:
                    try:
                        vf = float(v)
                        gf = float(g)
                    except (ValueError, TypeError):
                        continue
                    try:
                        tf = float(tol)
                    except (ValueError, TypeError):
                        continue
                    if abs(vf - gf) <= tf:
                        passed += 1

            total = len(checks)
            if total == 0:
                return 0.0
            return passed / total
        except Exception:
            return 0.0


_SCORERS = {
    'score_defect_energies': score_0,
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
