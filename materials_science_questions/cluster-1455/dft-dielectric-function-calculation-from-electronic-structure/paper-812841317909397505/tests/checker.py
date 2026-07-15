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
    return spec.get("gold", {})


# === block: score_0 (check id='structural') ===
def score_0(artifact, step, ctx):
        gold = ctx.get("structural", {})
        if not gold:
            return 0.0
        systems = ["undoped", "Sb_defect1", "Sb_defect2"]
        tol = 0.1  # Angstrom
        scores = []
        for sys_name in systems:
            row = next((r for r in artifact if r["system"] == sys_name), None)
            if row is None:
                scores.append(0.0)
                continue
            try:
                lat = float(row["lattice_parameter_A"])
                bond = float(row["bond_length_A"])
            except (ValueError, KeyError):
                scores.append(0.0)
                continue
            g = gold[sys_name]
            lat_g = g["lattice_parameter_A"]
            bond_g = g["bond_length_A"]
            lat_s = 1.0 if abs(lat - lat_g) <= tol else (0.5 if abs(lat - lat_g) <= 2*tol else 0.0)
            bond_s = 1.0 if abs(bond - bond_g) <= tol else (0.5 if abs(bond - bond_g) <= 2*tol else 0.0)
            scores.append(0.5 * lat_s + 0.5 * bond_s)
        return sum(scores) / len(systems)


# === block: score_1 (check id='band_gap') ===
def score_1(artifact, step, ctx):
        gold = ctx.get("band_gap", {})
        if not gold:
            return 0.0
        systems = ["undoped", "Sb_defect1", "Sb_defect2"]
        scores = []
        for sys_name in systems:
            row = next((r for r in artifact if r["system"] == sys_name), None)
            if row is None:
                scores.append(0.0)
                continue
            try:
                gap = float(row["band_gap_eV"])
            except (ValueError, KeyError):
                scores.append(0.0)
                continue
            if sys_name == "Sb_defect2":
                if gap <= 0.0:
                    scores.append(1.0)
                elif gap <= 0.2:
                    scores.append(0.5)
                else:
                    scores.append(0.0)
            else:
                target = gold[sys_name]
                if abs(gap - target) <= 0.2:
                    scores.append(1.0)
                elif abs(gap - target) <= 0.4:
                    scores.append(0.5)
                else:
                    scores.append(0.0)
        return sum(scores) / len(systems)


# === block: score_2 (check id='dielectric') ===
def score_2(artifact, step, ctx):
        import math
        gold = ctx.get("dielectric", {})
        if not gold:
            return 0.0
        spectra = {}
        for row in artifact:
            sys = row["system"]
            e = float(row["energy_eV"])
            eps = float(row["epsilon2"])
            spectra.setdefault(sys, []).append((e, eps))
        systems = ["undoped", "Sb_defect1", "Sb_defect2"]
        scores = []
        for sys_name in systems:
            if sys_name not in spectra:
                scores.append(0.0)
                continue
            points = sorted(spectra[sys_name], key=lambda x: x[0])
            energies, eps2 = zip(*points)
            de = energies[1] - energies[0]
            integral = 0.0
            for e_v, eps_v in zip(energies, eps2):
                if e_v == 0.0:
                    continue
                integral += eps_v / e_v
            integral *= de
            eps1_0 = 1.0 + (2.0 / math.pi) * integral
            peak_e = None
            max_eps = -1.0
            for e_v, eps_v in points:
                if e_v >= 0.5 and eps_v > max_eps:
                    max_eps = eps_v
                    peak_e = e_v
            if peak_e is None:
                scores.append(0.0)
                continue
            g = gold[sys_name]
            static_t = g["static_eps1"]
            peak_t = g["first_peak_eV"]
            static_s = 1.0 if abs(eps1_0 - static_t) <= 0.5 else (0.5 if abs(eps1_0 - static_t) <= 1.0 else 0.0)
            peak_s = 1.0 if abs(peak_e - peak_t) <= 0.5 else (0.5 if abs(peak_e - peak_t) <= 1.0 else 0.0)
            scores.append(0.5 * static_s + 0.5 * peak_s)
        return sum(scores) / len(systems)


_SCORERS = {
    'structural': score_0,
    'band_gap': score_1,
    'dielectric': score_2,
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
