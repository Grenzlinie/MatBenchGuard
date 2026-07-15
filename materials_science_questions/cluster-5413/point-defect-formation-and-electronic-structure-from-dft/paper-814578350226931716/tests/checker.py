import os
import json
import csv

# === author imports / helpers ===
import csv, json, math


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


# === block: score_0 (check id='step5') ===
def score_0(artifact, step, ctx):
    try:
        rows = artifact
        if not rows:
            return 0.0
    except Exception:
        return 0.0

    energies = []
    mos = []
    total_dos = []
    for r in rows:
        try:
            e = float(r['energy'])
        except (ValueError, KeyError):
            continue
        energies.append(e)
        mo = float(r.get('Mo_DOS', 0.0))
        s = float(r.get('S_DOS', 0.0))
        mos.append(mo + s)
        total_dos.append(float(r.get('total_DOS', 0.0)))

    if not energies:
        return 0.0

    # VBM: maximum Mo+S DOS in [-4, 0.1]
    vbm = None
    max_mos = -1
    for i, e in enumerate(energies):
        if -4.0 <= e <= 0.1:
            if mos[i] > max_mos:
                max_mos = mos[i]
                vbm = e

    if vbm is None:
        return 0.0

    # CBM: after VBM find where total DOS drops below 0.1 and then rises again
    vbm_idx = min(range(len(energies)), key=lambda i: abs(energies[i] - vbm))
    threshold = 0.1
    low_start = None
    for i in range(vbm_idx + 1, len(energies)):
        if energies[i] > 0.0:
            break
        if total_dos[i] < threshold:
            low_start = i
            break
    if low_start is None:
        cbm = 0.0
    else:
        cbm = None
        for i in range(low_start + 1, len(energies)):
            if total_dos[i] >= threshold:
                cbm = energies[i]
                break
        if cbm is None:
            cbm = 0.0

    score = 0.0
    if vbm is not None and cbm is not None:
        score += 0.2

    # Hf defect peak inside gap
    hf_peak_e = None
    hf_max = 0.0
    for r in rows:
        e = float(r['energy'])
        if vbm < e < cbm:
            hf = float(r.get('Hf_DOS', 0.0))
            if hf > hf_max:
                hf_max = hf
                hf_peak_e = e

    if hf_peak_e is not None and hf_peak_e < 0.0 and hf_max >= 0.5:
        score += 0.5

    # Fermi pinning: at E=0 total_DOS >= 0.2, or CBM <= 0.01 eV
    fermi_pinned = False
    for r in rows:
        e = float(r['energy'])
        if abs(e) < 0.005:
            if float(r.get('total_DOS', 0.0)) >= 0.2:
                fermi_pinned = True
            break
    if not fermi_pinned and cbm is not None and cbm <= 0.01:
        fermi_pinned = True
    if fermi_pinned:
        score += 0.3

    return min(1.0, max(0.0, score))


_SCORERS = {
    'step5': score_0,
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
