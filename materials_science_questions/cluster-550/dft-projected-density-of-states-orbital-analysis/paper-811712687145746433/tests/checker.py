import os
import json
import csv

# === author imports / helpers ===
import csv
import math


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
        ctx = {
            "band_gap_gold": 0.80,
            "band_gap_tol": 0.1,
            "cbm_gold": "Hf 5d_xy",
            "bec_gold": {
                "Hf": {"Zxx": 4.52, "Zzz": 3.09},
                "N1": {"Zxx": -4.66, "Zzz": -1.65},
                "N2": {"Zxx": -2.59, "Zzz": -4.58},
                "Ba": {"Zxx": 2.73, "Zzz": 3.14},
            },
            "bec_tol": 0.3,
            "dielectric_gold": [7.47, 7.55, 33.8, 21.4],
            "dielectric_tols": [1.0, 1.0, 5.0, 5.0],
            "phonon_undoped_gold": {
                "1-2": {"TO": 72, "LO": 93},
                "3-4": {"TO": 82, "LO": None},
                "5": {"TO": 105, "LO": 144},
                "6": {"TO": 120, "LO": None},
                "7-8": {"TO": 152, "LO": None},
                "9": {"TO": 172, "LO": None},
                "10-11": {"TO": 210, "LO": 240},
                "12-13": {"TO": 232, "LO": None},
                "14": {"TO": 341, "LO": None},
                "15-16": {"TO": 424, "LO": 614},
                "17": {"TO": 468, "LO": 492},
                "18-19": {"TO": 623, "LO": None},
                "20": {"TO": 641, "LO": 751},
                "21": {"TO": 717, "LO": None},
            },
            "phonon_doped_gold": {
                "1-2": 76,
                "3-4": 94,
                "5": 144,
                "6": 136,
                "7-8": 148,
                "9": 175,
                "10-11": 210,
                "12-13": 283,
                "14": 328,
                "15-16": 475,
                "17": 457,
                "18-19": 651,
                "20": 596,
                "21": 646,
            },
        }
        return ctx


# === block: score_0 (check id='step_bandgap') ===
def score_0(artifact, step, ctx):
        if artifact is None:
            return 0.0
        lines = artifact.strip().splitlines()
        if not lines:
            return 0.0
        try:
            val = float(lines[0])
        except ValueError:
            return 0.0
        ref = ctx["band_gap_gold"]
        tol = ctx["band_gap_tol"]
        return 1.0 if abs(val - ref) <= tol else 0.0


# === block: score_1 (check id='step_cbm_character') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        if artifact is None:
            return 0.0
        return 1.0 if artifact.strip() == ctx["cbm_gold"] else 0.0


# === block: score_2 (check id='step_bec') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not isinstance(artifact, list) or not artifact:
            return 0.0
        gold = ctx["bec_gold"]
        tol = ctx["bec_tol"]
        found = {}
        for row in artifact:
            try:
                atom = row["atom"].strip()
                zxx = float(row["Zxx"])
                zzz = float(row["Zzz"])
            except (KeyError, ValueError):
                return 0.0
            found[atom] = (zxx, zzz)
        total = len(gold) * 2  # Zxx and Zzz for each atom
        correct = 0
        for atom, g in gold.items():
            if atom not in found:
                continue
            f = found[atom]
            if abs(f[0] - g["Zxx"]) <= tol:
                correct += 1
            if abs(f[1] - g["Zzz"]) <= tol:
                correct += 1
        return correct / total if total > 0 else 0.0


# === block: score_3 (check id='step_dielectric') ===
def score_3(artifact, step, ctx):
    def score(artifact, step, ctx):
        if artifact is None:
            return 0.0
        lines = artifact.strip().splitlines()
        if len(lines) < 4:
            return 0.0
        vals = []
        for i in range(4):
            try:
                vals.append(float(lines[i]))
            except ValueError:
                return 0.0
        g = ctx["dielectric_gold"]
        tols = ctx["dielectric_tols"]
        correct = 0
        for i in range(4):
            if abs(vals[i] - g[i]) <= tols[i]:
                correct += 1
        return correct / 4.0


# === block: score_4 (check id='step_phonon_undoped') ===
def score_4(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not isinstance(artifact, list) or not artifact:
            return 0.0
        gold = ctx["phonon_undoped_gold"]
        rows_by_label = {}
        for row in artifact:
            label = row.get("mode_label", "").strip()
            if label:
                rows_by_label[label] = row
        total_comparisons = sum(1 for g in gold.values() if g["TO"] is not None) + sum(1 for g in gold.values() if g["LO"] is not None)
        if total_comparisons == 0:
            return 0.0
        correct = 0
        for label, g in gold.items():
            if label not in rows_by_label:
                continue
            row = rows_by_label[label]
            if g["TO"] is not None:
                try:
                    to_val = float(row["frequency_TO"])
                except (ValueError, KeyError):
                    continue
                tol = 10.0 if g["TO"] < 400 else 20.0
                if abs(to_val - g["TO"]) <= tol:
                    correct += 1
            if g["LO"] is not None:
                try:
                    lo_val = float(row["frequency_LO"])
                except (ValueError, KeyError):
                    continue
                tol = 10.0 if g["LO"] < 400 else 20.0
                if abs(lo_val - g["LO"]) <= tol:
                    correct += 1
        return correct / total_comparisons


# === block: score_5 (check id='step_doped_phonons') ===
def score_5(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not isinstance(artifact, list) or not artifact:
            return 0.0
        gold = ctx["phonon_doped_gold"]
        rows_by_label = {}
        for row in artifact:
            label = row.get("mode_label", "").strip()
            if label:
                rows_by_label[label] = row
        total = len(gold)
        if total == 0:
            return 0.0
        correct = 0
        for label, gval in gold.items():
            if label not in rows_by_label:
                continue
            try:
                fval = float(rows_by_label[label]["frequency"])
            except (ValueError, KeyError):
                continue
            tol = 10.0 if gval < 400 else 20.0
            if abs(fval - gval) <= tol:
                correct += 1
        return correct / total


_SCORERS = {
    'step_bandgap': score_0,
    'step_cbm_character': score_1,
    'step_bec': score_2,
    'step_dielectric': score_3,
    'step_phonon_undoped': score_4,
    'step_doped_phonons': score_5,
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
