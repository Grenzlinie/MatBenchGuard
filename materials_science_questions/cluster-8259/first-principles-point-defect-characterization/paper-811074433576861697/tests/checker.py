import os
import json
import csv

# === author imports / helpers ===
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
    formation_gold = {
        ("V_MA", "MAI"): 0.32,
        ("I_i", "flat"): -0.03,
        ("V_I", "flat"): 4.55,
        ("Pb_i", "flat"): 2.94,
        ("V_Pb", "flat"): -0.13,
        ("I_i", "vacant"): -0.12,
        ("V_I", "vacant"): 1.76,
        ("Pb_i", "vacant"): 2.71,
        ("V_Pb", "vacant"): -1.40
    }

    defect_levels_gold = {
        ("flat", "I_i"): {"level_eV": 0.65, "VBM_eV": 0.0, "CBM_eV": 1.55},
        ("vacant", "I_i"): {"level_eV": 0.65, "VBM_eV": 0.0, "CBM_eV": 1.55}
    }
    return {"formation_gold": formation_gold, "defect_levels_gold": defect_levels_gold}


# === block: score_0 (check id='formation_energies') ===
def score_0(artifact, step, ctx):
    rows = artifact
    gold = ctx["formation_gold"]
    agent = {}
    for r in rows:
        try:
            defn = r["defect_name"]
            term = r["termination"]
            e = float(r["formation_energy_eV"])
            agent[(defn, term)] = e
        except (ValueError, KeyError):
            continue

    tol = 0.1
    scores = []
    for key, gval in gold.items():
        aval = agent.get(key)
        if aval is None:
            scores.append(0.0)
        else:
            err = abs(aval - gval)
            sc = max(0.0, 1.0 - err / tol)
            scores.append(sc)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_1 (check id='defect_levels') ===
def score_1(artifact, step, ctx):
    rows = artifact
    gold = ctx["defect_levels_gold"]
    agent = {}
    for r in rows:
        try:
            term = r["termination"]
            defn = r["defect"]
            level = float(r["level_eV"])
            vbm = float(r["VBM_eV"])
            cbm = float(r["CBM_eV"])
            agent[(term, defn)] = {"level_eV": level, "VBM_eV": vbm, "CBM_eV": cbm}
        except (ValueError, KeyError):
            continue

    tol_level = 0.1
    tol_vbm = 0.02
    tol_cbm = 0.1
    scores = []
    for key, gvals in gold.items():
        avals = agent.get(key)
        if avals is None:
            scores.append(0.0)
            continue
        # per-component score
        sc_level = max(0.0, 1.0 - abs(avals["level_eV"] - gvals["level_eV"]) / tol_level)
        sc_vbm = max(0.0, 1.0 - abs(avals["VBM_eV"] - gvals["VBM_eV"]) / tol_vbm)
        sc_cbm = max(0.0, 1.0 - abs(avals["CBM_eV"] - gvals["CBM_eV"]) / tol_cbm)
        row_sc = (sc_level + sc_vbm + sc_cbm) / 3.0
        scores.append(row_sc)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


_SCORERS = {
    'formation_energies': score_0,
    'defect_levels': score_1,
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
