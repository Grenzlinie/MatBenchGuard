import os
import json
import csv

# === author imports / helpers ===
import csv, json, math, os


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


# === block: score_0 (check id='step2') ===
def score_0(artifact, step, ctx):
        import csv, math

        def _extract_float(s):
            if s is None:
                return None
            s = str(s).strip()
            if s == '':
                return None
            # split on '±' and take the first part
            if '±' in s:
                s = s.split('±')[0].strip()
            elif '+' in s and '-' in s:  # handle potential '+-'
                s = s.split('+')[0].strip()
            try:
                return float(s)
            except ValueError:
                return None

        required_cols = ['system', 'V_cm3mol', 'E_kcalmol', 'S_calmolK', 'G_kcalmol',
                         'delta_V_cm3mol', 'delta_E_calmolK', 'delta_S_calmolK', 'delta_G_kcalmol']
        # artifact is a list of dicts from CSV
        rows = artifact
        gold = step['gold']
        mixing_gold = step['mixing_gold']
        tols = step['tolerances']
        factor = step['max_falloff_factor']
        required_systems = step['required_systems']
        pure_salts = step['pure_salts']

        # Build dict by system
        data = {}
        for row in rows:
            sys = str(row.get('system', '')).strip()
            if sys not in required_systems:
                continue
            data[sys] = row

        # Sub-scores: 4 per system (V,E,S,G) + for mixture: 4 mixing + for pure salts: 1 emptiness check each
        sub_scores = []
        for sys in required_systems:
            if sys not in data:
                # missing row -> all sub-properties 0
                sub_scores.extend([0.0] * 4)
                if sys in pure_salts:
                    sub_scores.append(0.0)  # empty mixing check
                continue
            row = data[sys]
            props = gold[sys]
            for prop_name in ['V', 'E', 'S', 'G']:
                val = _extract_float(row.get(prop_name + '_cm3mol' if prop_name == 'V' else prop_name + '_kcalmol' if prop_name in ('E','G') else prop_name + '_calmolK', ''))
                target = props[prop_name]
                tol = tols[prop_name]
                if val is None:
                    sub = 0.0
                else:
                    err = abs(val - target)
                    if err <= tol:
                        sub = 1.0
                    elif err >= tol * factor:
                        sub = 0.0
                    else:
                        sub = 1.0 - (err - tol) / (tol * (factor - 1))
                sub_scores.append(sub)
            # mixing properties only for mixture
            if sys == '(Na,K)Cl':
                for mprop in ['delta_V', 'delta_E', 'delta_S', 'delta_G']:
                    val = _extract_float(row.get(mprop + '_cm3mol' if mprop == 'delta_V' else mprop + '_kcalmol' if mprop in ('delta_E','delta_G') else mprop + '_calmolK', ''))
                    target = mixing_gold[mprop]
                    tol = tols[mprop]
                    if val is None:
                        sub = 0.0
                    else:
                        err = abs(val - target)
                        if err <= tol:
                            sub = 1.0
                        elif err >= tol * factor:
                            sub = 0.0
                        else:
                            sub = 1.0 - (err - tol) / (tol * (factor - 1))
                    sub_scores.append(sub)
            # pure salt mixing columns should be empty
            if sys in pure_salts:
                empty = True
                for mcol in ['delta_V_cm3mol', 'delta_E_kcalmol', 'delta_S_calmolK', 'delta_G_kcalmol']:
                    val_str = str(row.get(mcol, '')).strip()
                    if val_str not in ('', 'None'):
                        empty = False
                        break
                sub_scores.append(1.0 if empty else 0.0)

        if not sub_scores:
            return 0.0
        return sum(sub_scores) / len(sub_scores)


_SCORERS = {
    'step2': score_0,
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
