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
    def prepare(outputs_dir, spec):
        native_path = os.path.join(outputs_dir, "native_defect_formation_energies.csv")
        rows = []
        with open(native_path, newline='') as f:
            reader = csv.DictReader(f)
            for r in reader:
                rows.append(dict(r))
        mu_e_ints = {}
        conditions = set(r['condition'] for r in rows)
        for cond in conditions:
            eta_vbm = None
            vac_vbm = None
            for r in rows:
                if r['condition'] == cond and r['defect'].strip() == 'eta_Ce^-' and abs(float(r['fermi_level_eV'])) < 1e-6:
                    eta_vbm = float(r['formation_energy_eV'])
                if r['condition'] == cond and r['defect'].strip() == 'V_O^{2+}' and abs(float(r['fermi_level_eV'])) < 1e-6:
                    vac_vbm = float(r['formation_energy_eV'])
            if eta_vbm is not None and vac_vbm is not None:
                mu_e_ints[cond] = (eta_vbm - vac_vbm) / 3.0   # charges -1 and +2
            else:
                mu_e_ints[cond] = None
        return {"mu_e_ints": mu_e_ints, "native_rows": rows}


# === block: score_0 (check id='bulk_properties') ===
def score_0(artifact, step, ctx):
    fields = step['fields']
    scores = []
    for key, info in fields.items():
        val = artifact.get(key)
        if val is None:
            scores.append(0.0)
            continue
        target = info['target']
        if 'tolerance' in info:
            tol = info['tolerance']
            scores.append(1.0 if abs(val - target) <= tol else 0.0)
        elif 'tolerance_percent' in info:
            tol = abs(target) * info['tolerance_percent'] / 100.0
            scores.append(1.0 if abs(val - target) <= tol else 0.0)
        else:
            scores.append(0.0)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_1 (check id='native_defects') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        rows = ctx['native_rows']
        gold = step['gold']
        tol_mu = step['tolerances']['mu_e_int_abs']
        tol_ef = step['tolerances']['E_f_abs']
        conditions = step['conditions']
        scores = []
        for cond in conditions:
            cond_gold = gold[cond]
            eta_vbm = None
            vac_vbm = None
            for r in rows:
                if r['condition'] == cond and r['defect'].strip() == 'eta_Ce^-':
                    eta_vbm = float(r['formation_energy_eV'])
                if r['condition'] == cond and r['defect'].strip() == 'V_O^{2+}':
                    vac_vbm = float(r['formation_energy_eV'])
            if eta_vbm is None or vac_vbm is None:
                scores.append(0.0)
                continue
            mu_e_int = (eta_vbm - vac_vbm) / 3.0
            ef_eta = eta_vbm - mu_e_int
            ef_vac = vac_vbm + 2 * mu_e_int
            score_mu = 1.0 if abs(mu_e_int - cond_gold['mu_e_int']) <= tol_mu else 0.0
            score_ef = 1.0 if abs(ef_eta - cond_gold['E_f_eta_VO']) <= tol_ef and abs(ef_vac - cond_gold['E_f_eta_VO']) <= tol_ef else 0.0
            dom_score = 1.0
            if step.get('dominance'):
                min_ef = float('inf')
                for r in rows:
                    if r['condition'] == cond:
                        charge = int(r['charge'])
                        ef = float(r['formation_energy_eV']) + charge * mu_e_int
                        if ef < min_ef:
                            min_ef = ef
                if ef_eta <= min_ef + 0.01 and ef_vac <= min_ef + 0.01:
                    dom_score = 1.0
                else:
                    dom_score = 0.0
            cond_score = 0.2 * score_mu + 0.4 * score_ef + 0.4 * dom_score
            scores.append(cond_score)
        if not scores:
            return 0.0
        return sum(scores) / len(scores)


# === block: score_2 (check id='impurity_dopants') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        mu_e_ints = ctx['mu_e_ints']
        cond = step['condition']
        mu_e = mu_e_ints.get(cond)
        if mu_e is None:
            return 0.0
        ef = {}
        for r in artifact:
            if r['condition'] == cond:
                defect = r['defect'].strip()
                charge = int(r['charge'])
                ef_val = float(r['formation_energy_eV']) + charge * mu_e
                ef[defect] = ef_val
        trends = step['trends']
        passed = 0
        for trend in trends:
            d1 = trend['defect1']
            d2 = trend['defect2']
            if d1 in ef and d2 in ef:
                if trend['relation'] == 'lt' and ef[d1] < ef[d2]:
                    passed += 1
        if not trends:
            return 0.0
        return passed / len(trends)


# === block: score_3 (check id='migration_barriers') ===
def score_3(artifact, step, ctx):
    def score(artifact, step, ctx):
        fields = step['fields']
        scores = []
        for key, info in fields.items():
            val = artifact.get(key)
            if val is None:
                scores.append(0.0)
                continue
            target = info['target']
            tol = info.get('tolerance_abs', 0.0)
            scores.append(1.0 if abs(val - target) <= tol else 0.0)
        if not scores:
            return 0.0
        return sum(scores) / len(scores)


_SCORERS = {
    'bulk_properties': score_0,
    'native_defects': score_1,
    'impurity_dopants': score_2,
    'migration_barriers': score_3,
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
