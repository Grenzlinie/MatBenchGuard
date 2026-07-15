import os
import json
import csv

# === author imports / helpers ===
import math
from statistics import mean


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


# === block: score_0 (check id='elastic_properties') ===
def score_0(artifact, step, ctx):
    try:
        data = artifact
        gold = step["gold"]
        tolerances = step.get("tolerances", {})
        compounds = ["V3Fe", "V3Co", "V3Ni"]
        scores = []
        for comp in compounds:
            g = gold.get(comp)
            d = data.get(comp)
            if not g or not isinstance(d, dict):
                scores.append(0.0)
                continue
            comp_scores = []
            for field in ["C11","C12","C44","B","G","E","B/G","Cp"]:
                val = d.get(field)
                gold_val = g[field]
                tol = tolerances.get(field, 0.05)
                if val is None or not isinstance(val, (int, float)):
                    comp_scores.append(0.0)
                elif gold_val == 0:
                    comp_scores.append(1.0 if abs(val) < 1e-9 else 0.0)
                else:
                    err = abs(val - gold_val) / abs(gold_val)
                    if err <= tol:
                        comp_scores.append(1.0)
                    elif err <= 3 * tol:
                        comp_scores.append(max(0.0, 1.0 - (err - tol) / (2 * tol)))
                    else:
                        comp_scores.append(0.0)
            born_ok = (d.get("Born_stable") == g["Born_stable"])
            comp_scores.append(1.0 if born_ok else 0.0)
            scores.append(mean(comp_scores))
        return mean(scores) if scores else 0.0
    except Exception:
        return 0.0


# === block: score_1 (check id='phonon_gamma_frequencies') ===
def score_1(artifact, step, ctx):
    try:
        data = artifact
        gold = step["gold"]
        tol = step.get("tolerance_abs", 0.2)
        compounds = ["V3Fe", "V3Co", "V3Ni"]
        scores = []
        for comp in compounds:
            g = gold.get(comp)
            d = data.get(comp)
            if not g or not isinstance(d, dict):
                scores.append(0.0)
                continue
            g_freqs = sorted(g["frequencies_THz"])
            d_freqs = d.get("frequencies_THz")
            if not isinstance(d_freqs, list) or len(d_freqs) != 8:
                freq_score = 0.0
            else:
                d_sorted = sorted(d_freqs)
                freq_scores = []
                for gf, df in zip(g_freqs, d_sorted):
                    err = abs(df - gf)
                    if err <= tol:
                        freq_scores.append(1.0)
                    elif err <= 3 * tol:
                        freq_scores.append(max(0.0, 1.0 - (err - tol) / (2 * tol)))
                    else:
                        freq_scores.append(0.0)
                freq_score = mean(freq_scores) if freq_scores else 0.0
            allpos_ok = (d.get("all_positive") == g["all_positive"])
            allpos_score = 1.0 if allpos_ok else 0.0
            comp_score = (freq_score * 8 + allpos_score) / 9
            scores.append(comp_score)
        return mean(scores) if scores else 0.0
    except Exception:
        return 0.0


_SCORERS = {
    'elastic_properties': score_0,
    'phonon_gamma_frequencies': score_1,
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
