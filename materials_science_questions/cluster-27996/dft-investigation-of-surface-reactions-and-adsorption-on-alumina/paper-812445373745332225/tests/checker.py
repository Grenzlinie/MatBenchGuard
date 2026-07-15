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


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    expected = step.get("expected_rows", [])
    tolerance = step.get("tolerance", 0.5)

    def norm_species(s):
        s = str(s).strip()
        # strip trailing parenthetical notes (e.g., "C6H10 (diallyl)" -> "C6H10")
        s = s.split(' ')[0].split('(')[0].split('（')[0] if s else s
        # map common unicode formatting to ascii
        s = s.replace('\u03b7', 'eta')  # η
        s = s.replace('\u03c0', 'pi')   # π
        s = s.replace('\u03c3', 'sigma') # σ
        s = s.replace('\u00b9', '1')    # ¹
        s = s.replace('\u00b2', '2')    # ²
        s = s.replace('\u00b3', '3')    # ³
        s = s.replace('\u2013', '-')    # en dash
        s = s.replace('\u2014', '-')    # em dash
        s = s.replace('~', '-')
        s = s.replace('=', '-')
        s = s.replace(',', '-')
        # keep only alphanumeric and hyphens
        return ''.join(ch for ch in s if ch.isalnum() or ch == '-').lower()

    matched = 0
    for er in expected:
        target_norm = norm_species(er["species"])
        target_q = float(er["Q_kcal_mol"])
        target_d = float(er["D_kcal_mol"])
        target_dq = float(er["D_plus_Q_kcal_mol"])
        found = False
        for row in artifact:
            if norm_species(row.get("species", "")) == target_norm:
                try:
                    q = float(row.get("Q_kcal_mol", -1e9))
                    if abs(q - target_q) <= tolerance:
                        d = float(row.get("D_kcal_mol", -1e9))
                        dq = float(row.get("D_plus_Q_kcal_mol", -1e9))
                        if abs(d - target_d) <= tolerance and abs(dq - target_dq) <= tolerance:
                            found = True
                            break
                except:
                    pass
        if found:
            matched += 1
    return matched / len(expected) if expected else 1.0


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    expected = step.get("expected_rows", [])
    tolerance = step.get("tolerance", 0.5)
    matched = 0
    for er in expected:
        found = False
        for row in artifact:
            if (row.get("table_id","") == er["table_id"] and row.get("reaction_equation","") == er["reaction_equation"]):
                qcl_expected = str(er.get("Q_Cl_value_if_applicable", ""))
                qcl_agent = str(row.get("Q_Cl_value_if_applicable", ""))
                if qcl_agent == qcl_expected:
                    try:
                        def_ = float(row.get("DeltaE_f_kcal_mol", -1e9))
                        der = float(row.get("DeltaE_r_kcal_mol", -1e9))
                        if abs(def_ - float(er["DeltaE_f_kcal_mol"])) <= tolerance and abs(der - float(er["DeltaE_r_kcal_mol"])) <= tolerance:
                            found = True
                            break
                    except:
                        pass
        if found:
            matched += 1
    return matched / len(expected) if expected else 1.0


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
