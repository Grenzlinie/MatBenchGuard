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


# === block: score_0 (check id='phonon_freqs') ===
def score_0(artifact, step, ctx):
    gold_modes = step["gold"]["modes"]
    tol = step["gold"].get("tol_phonon", 5.0)
    phonons = artifact.get("zone_center_phonons", [])
    if not isinstance(phonons, list):
        return 0.0
    total = 0
    matched = 0
    for gmode in gold_modes:
        mode_name = gmode["mode"]
        g_to = gmode["to"]
        g_lo = gmode["lo"]
        # find matching mode in artifact
        art_modes = [m for m in phonons if m.get("mode") == mode_name]
        if not art_modes:
            total += 1
            if g_lo is not None:
                total += 1
            continue
        art = art_modes[0]
        art_to = art.get("frequency_TO")
        if art_to is not None and abs(art_to - g_to) <= tol:
            matched += 1
        total += 1
        if g_lo is not None:
            art_lo = art.get("frequency_LO")
            total += 1
            if art_lo is not None and abs(art_lo - g_lo) <= tol:
                matched += 1
    return matched / total if total > 0 else 0.0


# === block: score_1 (check id='born_charges') ===
def score_1(artifact, step, ctx):
    gold_atoms = step["gold"]["atoms"]
    tol = step["gold"].get("tol_born", 0.2)
    charges = artifact.get("born_effective_charges", [])
    if not isinstance(charges, list):
        return 0.0
    total = 0
    matched = 0
    for gatom in gold_atoms:
        atom_name = gatom["atom"]
        art_list = [a for a in charges if a.get("atom") == atom_name]
        if not art_list:
            total += 4
            continue
        art = art_list[0]
        g_eigs = sorted(gatom["eigenvalues"])
        a_eigs = sorted(art.get("eigenvalues", []))
        if len(a_eigs) != 3:
            total += 4
            continue
        for i in range(3):
            if abs(a_eigs[i] - g_eigs[i]) <= tol:
                matched += 1
            total += 1
        if abs(art.get("average", 0.0) - gatom["average"]) <= tol:
            matched += 1
        total += 1
    return matched / total if total > 0 else 0.0


# === block: score_2 (check id='dielectric_constants') ===
def score_2(artifact, step, ctx):
    gold = step["gold"]
    tol = gold.get("tol_dielectric", 1.5)
    dielec = artifact.get("dielectric_constants", {})
    if not isinstance(dielec, dict):
        return 0.0
    total = 0
    matched = 0
    for key in ["epsilon_inf_perp", "epsilon_inf_par", "epsilon_0_perp", "epsilon_0_par"]:
        total += 1
        val = dielec.get(key)
        if val is not None and abs(val - gold[key]) <= tol:
            matched += 1
    return matched / total if total > 0 else 0.0


_SCORERS = {
    'phonon_freqs': score_0,
    'born_charges': score_1,
    'dielectric_constants': score_2,
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
