import os
import json
import csv

# === author imports / helpers ===
import numpy as np

def _parse_dos(content):
    lines = content.strip().splitlines()
    energies, dos = [], []
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        parts = line.split()
        if len(parts) < 2:
            continue
        try:
            e = float(parts[0])
            d = float(parts[1])
            energies.append(e)
            dos.append(d)
        except ValueError:
            continue
    return np.array(energies), np.array(dos)

def _compute_gap(energies, dos, dos_threshold_factor):
    if len(energies) == 0:
        return None
    # sort by energy
    idx = np.argsort(energies)
    e_sorted = energies[idx]
    d_sorted = dos[idx]
    max_dos = np.max(np.abs(d_sorted))
    if max_dos == 0:
        max_dos = 1.0
    threshold = dos_threshold_factor * max_dos
    # find region around Fermi (0 eV)
    ef_idx = np.searchsorted(e_sorted, 0.0)
    # scan left for last energy where dos > threshold (VBM)
    vbm = None
    for i in range(ef_idx - 1, -1, -1):
        if d_sorted[i] > threshold:
            vbm = e_sorted[i]
            break
    if vbm is None:
        return None  # no occupied band edge found
    # scan right for first energy where dos > threshold after some region where dos <= threshold
    cbm = None
    for i in range(ef_idx, len(e_sorted)):
        if d_sorted[i] > threshold:
            # check that we passed a region of low dos
            # but just take first above threshold after Ef
            cbm = e_sorted[i]
            break
    if cbm is None:
        return None
    gap = cbm - vbm
    if gap <= 0:
        return None
    return float(gap)

def _score_threshold(value, ref, delta):
    # threshold_or_better: full credit if value >= ref - delta
    threshold = ref - delta
    if value >= threshold:
        return 1.0
    # linear decay to 0 at ref - 2*delta (hard floor)
    floor = ref - 2 * delta
    if value <= floor:
        return 0.0
    return (value - floor) / (threshold - floor)


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


# === block: score_0 (check id='dos_structure') ===
def score_0(artifact, step, ctx):
    # Parse DOS file
    energies, dos = _parse_dos(artifact)
    if len(energies) == 0:
        return 0.0
    score = 0.0
    # check energy range covers [-5, 5]
    min_e = np.min(energies)
    max_e = np.max(energies)
    if min_e <= -5.0 and max_e >= 5.0:
        score += 0.5
    # check for a gap region near Ef
    ef_idx = np.searchsorted(np.sort(energies), 0.0)
    e_sorted = np.sort(energies)
    idx = np.argsort(energies)
    d_sorted = dos[idx]
    max_dos = np.max(np.abs(d_sorted))
    thresh = step["config"]["gap_region_threshold_factor"] * max_dos if max_dos != 0 else 0.01
    # find energies in [-0.5, 0.5] eV
    mask = (e_sorted >= -0.5) & (e_sorted <= 0.5)
    doses_near = d_sorted[mask]
    if len(doses_near) == 0:
        return score
    if np.all(doses_near < thresh):
        score += 0.5
    return min(1.0, score)


# === block: score_1 (check id='bandgap_recompute') ===
def score_1(artifact, step, ctx):
    energies, dos = _parse_dos(artifact)
    if len(energies) == 0:
        return 0.0
    gap = _compute_gap(energies, dos, step["config"]["dos_threshold_factor"])
    if gap is None:
        return 0.0
    ref = step["config"]["reference_gap"]
    delta = step["config"]["tolerance"]
    return _score_threshold(gap, ref, delta)


# === block: score_2 (check id='bandgap_file') ===
def score_2(artifact, step, ctx):
    val_str = artifact.strip()
    if not val_str:
        return 0.0
    try:
        val = float(val_str.split()[0])  # first token
    except (ValueError, IndexError):
        return 0.0
    ref = step["config"]["reference"]
    delta = step["config"]["delta"]
    return _score_threshold(val, ref, delta)


_SCORERS = {
    'dos_structure': score_0,
    'bandgap_recompute': score_1,
    'bandgap_file': score_2,
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
