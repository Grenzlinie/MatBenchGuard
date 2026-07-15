import os
import json
import csv

# === author imports / helpers ===
import os
import csv
import numpy as np
from collections import defaultdict


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


# === block: score_0 (check id='check_eigenstate_properties') ===
def score_0(artifact, step, ctx):
        if not artifact or len(artifact) == 0:
            return 0.0
        energies, fGs, Ls = [], [], []
        for row in artifact:
            try:
                e = float(row['energy'])
                fG = float(row['fractional_Gamma'])
                L = float(row['localisation_factor'])
                energies.append(e)
                fGs.append(fG)
                Ls.append(L)
            except (ValueError, KeyError):
                continue
        if len(energies) == 0:
            return 0.0
        energies = np.array(energies)
        fGs = np.array(fGs)
        Ls = np.array(Ls)
        low_mask = energies < 0.1
        mid_mask = (energies >= 0.18) & (energies <= 0.28)
        high_mask = energies > 0.35
        fG_low = float(np.mean(fGs[low_mask])) if np.any(low_mask) else 0.0
        fG_mid = float(np.mean(fGs[mid_mask])) if np.any(mid_mask) else 0.0
        fG_high = float(np.mean(fGs[high_mask])) if np.any(high_mask) else 0.0
        score_G = 0.0
        if fG_mid > 0:
            if fG_low > fG_mid:
                score_G += 0.5
            if fG_high > fG_mid:
                score_G += 0.5
        L_low = float(np.mean(Ls[low_mask])) if np.any(low_mask) else 0.0
        L_mid = float(np.mean(Ls[mid_mask])) if np.any(mid_mask) else 0.0
        L_high = float(np.mean(Ls[high_mask])) if np.any(high_mask) else 0.0
        score_L = 0.0
        if L_mid > 0:
            if L_mid > L_low:
                score_L += 0.5
            if L_mid > L_high:
                score_L += 0.5
        return (score_G + score_L) / 2.0


# === block: score_1 (check id='check_projected_dos_selected_k') ===
def score_1(artifact, step, ctx):
        if not artifact:
            return 0.0
        groups = defaultdict(list)
        for row in artifact:
            lbl = row.get('k_state_label')
            try:
                e = float(row['energy'])
                dos = float(row['projected_DOS'])
            except (ValueError, KeyError):
                continue
            groups[lbl].append((e, dos))
        if len(groups) < 6:
            return 0.0
        expected_labels = ['EM_0.0', 'EM_0.1', 'EM_0.2', 'EM_0.23', 'EM_0.25', 'EM_0.3']
        spreads = {}
        for lbl, pairs in groups.items():
            if lbl not in expected_labels:
                continue
            energies = np.array([p[0] for p in pairs])
            dos_vals = np.array([p[1] for p in pairs])
            total = np.sum(dos_vals)
            if total == 0:
                spreads[lbl] = 0.0
                continue
            mean = np.sum(energies * dos_vals) / total
            var = np.sum(((energies - mean) ** 2) * dos_vals) / total
            std = np.sqrt(max(var, 0.0))
            spreads[lbl] = float(std)
        far_labels = ['EM_0.0', 'EM_0.1', 'EM_0.3']
        near_labels = ['EM_0.2', 'EM_0.23', 'EM_0.25']
        far_stds = [spreads.get(l, 0.0) for l in far_labels]
        near_stds = [spreads.get(l, 0.0) for l in near_labels]
        avg_far = np.mean(far_stds) if far_stds else 0.0
        avg_near = np.mean(near_stds) if near_stds else 0.0
        if avg_near > avg_far:
            return 1.0
        else:
            return 0.0


# === block: score_2 (check id='check_host_projected_dos') ===
def score_2(artifact, step, ctx):
        if not artifact:
            return 0.0
        energies, dos_vals = [], []
        for row in artifact:
            try:
                e = float(row['energy'])
                d = float(row['host_projected_DOS'])
                energies.append(e)
                dos_vals.append(d)
            except (ValueError, KeyError):
                continue
        if len(energies) == 0:
            return 0.0
        energies = np.array(energies)
        dos_vals = np.array(dos_vals)
        # Sort by energy
        idx = np.argsort(energies)
        energies = energies[idx]
        dos_vals = dos_vals[idx]
        # Find local minimum near EN (0.2-0.25 eV)
        mask_center = (energies >= 0.2) & (energies <= 0.25)
        if not np.any(mask_center):
            return 0.0
        min_val = float(np.min(dos_vals[mask_center]))
        # Compare with neighbouring bands
        mask_left = (energies >= 0.15) & (energies < 0.2)
        mask_right = (energies > 0.25) & (energies <= 0.3)
        avg_left = float(np.mean(dos_vals[mask_left])) if np.any(mask_left) else 0.0
        avg_right = float(np.mean(dos_vals[mask_right])) if np.any(mask_right) else 0.0
        if avg_left == 0 and avg_right == 0:
            return 0.0
        avg_side = (avg_left + avg_right) / 2.0 if (avg_left > 0 and avg_right > 0) else max(avg_left, avg_right)
        if avg_side == 0:
            return 0.0
        # A detectable dip if min_val is at least 10% lower than the side average
        if min_val < 0.9 * avg_side:
            return 1.0
        else:
            return 0.0


_SCORERS = {
    'check_eigenstate_properties': score_0,
    'check_projected_dos_selected_k': score_1,
    'check_host_projected_dos': score_2,
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
