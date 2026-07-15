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
        ctx = {}
        for step in spec.get("steps", []):
            sid = step.get("id", "")
            if sid == "band_gap_recompute":
                ctx["gap_gold"] = float(step["gold_value"])
                ctx["gap_tol"] = float(step["tolerance"])
                ctx["gap_decay"] = float(step.get("decay_range", 1.0))
            elif sid == "band_gap_text":
                ctx["gap_gold_text"] = float(step["gold_value"])
                ctx["gap_tol_text"] = float(step["tolerance"])
                ctx["gap_decay_text"] = float(step.get("decay_range", 1.0))
            elif sid == "dos_gap_check":
                ctx["dos_window"] = step.get("energy_fermi_window", [-0.2, 0.2])
                ctx["dos_thresh"] = step.get("dos_threshold", 1e-6)
        return ctx


# === block: score_0 (check id='band_gap_recompute') ===
def score_0(artifact, step, ctx):
        if not artifact:
            return 0.0
        lines = artifact.strip().splitlines()
        data = []
        for line in lines:
            parts = line.split()
            if len(parts) < 2:
                continue
            try:
                k = float(parts[0])
                e = float(parts[1])
                data.append((k, e))
            except:
                continue
        if not data:
            return 0.0
        k_vals = sorted(set(k for k, e in data))
        gamma_k = k_vals[0] if k_vals else None
        if gamma_k is None:
            return 0.0
        gamma_eigs = [e for k, e in data if abs(k - gamma_k) < 1e-8]
        if not gamma_eigs:
            return 0.0
        # Fermi level at 0 eV
        valence = [e for e in gamma_eigs if e < -1e-3]
        conduction = [e for e in gamma_eigs if e > 1e-3]
        if not valence or not conduction:
            valence = [e for e in gamma_eigs if e < 0]
            conduction = [e for e in gamma_eigs if e > 0]
        if not valence or not conduction:
            return 0.0
        vbm = max(valence)
        cbm = min(conduction)
        gap = cbm - vbm
        diff = abs(gap - ctx["gap_gold"])
        if diff <= ctx["gap_tol"]:
            return 1.0
        excess = diff - ctx["gap_tol"]
        decay = excess / (ctx["gap_decay"] - ctx["gap_tol"])
        return max(0.0, 1.0 - decay)


# === block: score_1 (check id='band_gap_text') ===
def score_1(artifact, step, ctx):
        if not artifact:
            return 0.0
        try:
            gap = float(artifact.strip().split()[0])
        except:
            return 0.0
        diff = abs(gap - ctx["gap_gold_text"])
        if diff <= ctx["gap_tol_text"]:
            return 1.0
        excess = diff - ctx["gap_tol_text"]
        decay = excess / (ctx["gap_decay_text"] - ctx["gap_tol_text"])
        return max(0.0, 1.0 - decay)


# === block: score_2 (check id='dos_gap_check') ===
def score_2(artifact, step, ctx):
        if not artifact:
            return 0.0
        lines = artifact.strip().splitlines()
        energies = []
        dos_vals = []
        for line in lines:
            parts = line.split()
            if len(parts) < 2:
                continue
            try:
                e = float(parts[0])
                d = float(parts[1])
                energies.append(e)
                dos_vals.append(d)
            except:
                continue
        if not energies:
            return 0.0
        low, high = ctx["dos_window"]
        thresh = ctx["dos_thresh"]
        gap_clean = True
        for e, d in zip(energies, dos_vals):
            if low <= e <= high and d > thresh:
                gap_clean = False
                break
        return 1.0 if gap_clean else 0.0


_SCORERS = {
    'band_gap_recompute': score_0,
    'band_gap_text': score_1,
    'dos_gap_check': score_2,
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
