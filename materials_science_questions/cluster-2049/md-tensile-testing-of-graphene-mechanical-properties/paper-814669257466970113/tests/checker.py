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


# === block: score_0 (check id='data_integrity') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        rows = artifact
        required_concs = {0.0, 0.5, 1.0, 2.0, 3.0}
        concs = set()
        strains = set()
        for row in rows:
            concs.add(float(row['defect_concentration']))
            strains.add(float(row['engineering_strain']))
        if len(rows) < 50:
            return 0.0
        if not required_concs.issubset(concs):
            return 0.0
        max_strain = max(strains) if strains else 0
        if max_strain < 0.10:
            return 0.0
        return 1.0


# === block: score_1 (check id='pristine_young') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        cand = None
        min_strain = float('inf')
        for row in artifact:
            conc = float(row['defect_concentration'])
            strain = float(row['engineering_strain'])
            if conc == 0.0 and strain < min_strain:
                min_strain = strain
                cand = float(row['young_modulus_GPa'])
        if cand is None:
            return 0.0
        diff = abs(cand - 1000)
        if diff <= 100:
            return 1.0
        elif diff <= 200:
            return 0.5
        else:
            return 0.0


# === block: score_2 (check id='pristine_nu') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        cand = None
        min_strain = float('inf')
        for row in artifact:
            conc = float(row['defect_concentration'])
            strain = float(row['engineering_strain'])
            if conc == 0.0 and strain < min_strain:
                min_strain = strain
                cand = float(row['poisson_ratio'])
        if cand is None:
            return 0.0
        if 0.15 <= cand <= 0.25:
            return 1.0
        elif 0.10 <= cand <= 0.30:
            return 0.5
        else:
            return 0.0


# === block: score_3 (check id='auxetic_p3') ===
def score_3(artifact, step, ctx):
    def score(artifact, step, ctx):
        rows_p3 = [row for row in artifact if float(row['defect_concentration']) == 3.0]
        if not rows_p3:
            return 0.0
        max_strain_row = max(rows_p3, key=lambda r: float(r['engineering_strain']))
        nu = float(max_strain_row['poisson_ratio'])
        if nu <= -0.12:
            return 1.0
        elif nu <= -0.10:
            return 0.5
        else:
            return 0.0


# === block: score_4 (check id='nu_monotonic') ===
def score_4(artifact, step, ctx):
    def score(artifact, step, ctx):
        conc_order = [0.0, 0.5, 1.0, 2.0, 3.0]
        nu_vals = []
        for conc in conc_order:
            cand = None
            min_strain = float('inf')
            for row in artifact:
                if float(row['defect_concentration']) == conc and float(row['engineering_strain']) < min_strain:
                    min_strain = float(row['engineering_strain'])
                    cand = float(row['poisson_ratio'])
            if cand is None:
                return 0.0
            nu_vals.append(cand)
        for i in range(len(nu_vals)-1):
            if not nu_vals[i] > nu_vals[i+1]:
                return 0.0
        return 1.0


# === block: score_5 (check id='E_monotonic') ===
def score_5(artifact, step, ctx):
    def score(artifact, step, ctx):
        conc_order = [0.0, 0.5, 1.0, 2.0, 3.0]
        E_vals = []
        for conc in conc_order:
            cand = None
            min_strain = float('inf')
            for row in artifact:
                if float(row['defect_concentration']) == conc and float(row['engineering_strain']) < min_strain:
                    min_strain = float(row['engineering_strain'])
                    cand = float(row['young_modulus_GPa'])
            if cand is None:
                return 0.0
            E_vals.append(cand)
        for i in range(len(E_vals)-1):
            if not E_vals[i] > E_vals[i+1]:
                return 0.0
        return 1.0


# === block: score_6 (check id='nu_strain_inc_p3') ===
def score_6(artifact, step, ctx):
    def score(artifact, step, ctx):
        rows_p3 = [row for row in artifact if float(row['defect_concentration']) == 3.0]
        if len(rows_p3) < 2:
            return 0.0
        min_strain_row = min(rows_p3, key=lambda r: float(r['engineering_strain']))
        max_strain_row = max(rows_p3, key=lambda r: float(r['engineering_strain']))
        nu_min = float(min_strain_row['poisson_ratio'])
        nu_max = float(max_strain_row['poisson_ratio'])
        return 1.0 if nu_max > nu_min else 0.0


_SCORERS = {
    'data_integrity': score_0,
    'pristine_young': score_1,
    'pristine_nu': score_2,
    'auxetic_p3': score_3,
    'nu_monotonic': score_4,
    'E_monotonic': score_5,
    'nu_strain_inc_p3': score_6,
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
