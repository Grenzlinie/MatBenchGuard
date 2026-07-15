import os
import json
import csv

# === author imports / helpers ===
import csv
import json
import math
import os

# Replace numpy and scipy with pure Python equivalents
class _mock_np:
    @staticmethod
    def array(iterable):
        return list(iterable)
    @staticmethod
    def max(iterable):
        return max(iterable) if iterable else 0.0

np = _mock_np()

def _find_peaks(sequence, height=0.0):
    """Simple peak detection: return indices where value is a local maximum and > height."""
    if len(sequence) < 3:
        return [], {}
    peaks = []
    for i in range(1, len(sequence)-1):
        if sequence[i] >= sequence[i-1] and sequence[i] > sequence[i+1] and sequence[i] > height:
            peaks.append(i)
    return peaks, {}

find_peaks = _find_peaks


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
        curve_path = os.path.join(outputs_dir, "dos_curve.csv")
        gold_peaks = []
        for step in spec.get("steps", spec.get("checks", [])):
            if step.get("id") == "step1_peak_recompute":
                gold_peaks = step.get("parameters", {}).get("gold_peaks", [])
                break
        ref_energies = []
        if os.path.exists(curve_path):
            with open(curve_path, newline="") as f:
                reader = csv.DictReader(f)
                rows = list(reader)
            if rows:
                energies, dos_vals = [], []
                for row in rows:
                    try:
                        energies.append(float(row["energy_eV"]))
                        dos_vals.append(float(row["dos"]))
                    except (KeyError, ValueError):
                        pass
                if energies:
                    darr = np.array(dos_vals)
                    max_dos = np.max(darr) if len(darr) else 0.0
                    if max_dos > 0.0:
                        peaks_idx, _ = find_peaks(darr, height=0.1 * max_dos)
                        ref_energies = [energies[i] for i in peaks_idx]
        return {"gold_peaks": gold_peaks, "ref_energies": ref_energies}


# === block: score_0 (check id='step1_peak_recompute') ===
def score_0(artifact, step, ctx):
        gold_peaks = ctx.get("gold_peaks", [])
        ref_energies = ctx.get("ref_energies", [])
        if not gold_peaks or not ref_energies:
            return 0.0
        tolerance = step.get("parameters", {}).get("tolerance", 1.0)
        available = list(ref_energies)
        matched = 0
        for gp in gold_peaks:
            exp = gp["expected"]
            best_dist = None
            best_idx = None
            for idx, val in enumerate(available):
                dist = abs(val - exp)
                if dist <= tolerance:
                    if best_dist is None or dist < best_dist:
                        best_dist = dist
                        best_idx = idx
            if best_idx is not None:
                matched += 1
                available.pop(best_idx)
        return matched / len(gold_peaks)


# === block: score_1 (check id='step2_ordering_and_consistency') ===
def score_1(artifact, step, ctx):
        if not artifact or not isinstance(artifact, list):
            return 0.0
        peaks_by_label = {}
        for item in artifact:
            try:
                lbl = item["peak"]
                e = float(item["energy_eV"])
                peaks_by_label[lbl] = e
            except (KeyError, ValueError, TypeError):
                pass
        valence_order = step.get("parameters", {}).get("valence_order", ["A","B","C","D"])
        conduction_order = step.get("parameters", {}).get("conduction_order", ["d","e","f","g","h"])
        tolerance = step.get("parameters", {}).get("tolerance", 1.0)
        # ordering checks
        valence_ok = all(
            peaks_by_label.get(valence_order[i], float('inf')) > peaks_by_label.get(valence_order[i+1], float('-inf'))
            for i in range(len(valence_order)-1)
        ) if all(lbl in peaks_by_label for lbl in valence_order) else False
        conduction_ok = all(
            peaks_by_label.get(conduction_order[i], float('-inf')) < peaks_by_label.get(conduction_order[i+1], float('inf'))
            for i in range(len(conduction_order)-1)
        ) if all(lbl in peaks_by_label for lbl in conduction_order) else False
        ordering_score = 0.0
        if valence_ok:
            ordering_score += 0.5
        if conduction_ok:
            ordering_score += 0.5
        # consistency with refitted peaks
        ref_energies = ctx.get("ref_energies", [])
        if not ref_energies:
            consistency = 0.0
        else:
            matched_labels = 0
            for lbl, e_val in peaks_by_label.items():
                min_dist = min((abs(e_val - r) for r in ref_energies), default=float('inf'))
                if min_dist <= tolerance:
                    matched_labels += 1
            consistency = matched_labels / len(peaks_by_label) if peaks_by_label else 0.0
        return ordering_score * consistency


_SCORERS = {
    'step1_peak_recompute': score_0,
    'step2_ordering_and_consistency': score_1,
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
