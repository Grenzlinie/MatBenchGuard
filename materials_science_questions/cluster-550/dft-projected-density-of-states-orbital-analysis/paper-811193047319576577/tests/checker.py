import os
import json
import csv

# === author imports / helpers ===
import csv, os, json, math


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
    import json
    def prepare(outputs_dir, spec):
        ctx = {}
        for step in spec.get("steps", []):
            if step["id"] == "ir_freq":
                ctx["ir_gold"] = step.get("gold_entries", [])
                ctx["ir_tol"] = step.get("tolerance_cm1", 30.0)
            elif step["id"] == "homo_lumo":
                ctx["homo_gold"] = {entry["compound"]: entry for entry in step.get("gold_entries", [])}
                ctx["orbital_tol"] = step.get("tolerance_eV", 0.2)
            elif step["id"] == "binding":
                ctx["binding_gold"] = {entry["compound"]: entry for entry in step.get("gold_entries", [])}
                ctx["binding_tol_kcal"] = step.get("tolerance_kcal", 5.0)
                ctx["dipole_tol"] = step.get("tolerance_dipole", 0.5)
        return ctx


# === block: score_0 (check id='ir_freq') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not artifact:
            return 0.0
        gold = ctx.get("ir_gold", [])
        if not gold:
            return 0.0
        tol = ctx.get("ir_tol", 30.0)
        # build lookup from artifact
        data = {}
        for row in artifact:
            compound = row.get("compound", "").strip()
            band = row.get("band_label", "").strip()
            key = (compound, band)
            data[key] = row
        correct = 0
        total = len(gold)
        for entry in gold:
            compound = entry["compound"]
            band = entry["band_label"]
            exp_freq = entry.get("expected_frequency")
            exp_present = entry["expected_present"]
            key = (compound, band)
            row = data.get(key)
            if row is None:
                # row missing, treat as absent
                if not exp_present:
                    correct += 1
                continue
            # check presence
            present_str = str(row.get("present", "False")).strip().lower()
            agent_present = present_str in ("true", "1", "yes")
            if agent_present != exp_present:
                continue
            if not exp_present:
                correct += 1
                continue
            # check frequency
            freq_str = row.get("frequency_cm1", "")
            if freq_str == "" or freq_str is None:
                continue
            try:
                freq = float(freq_str)
            except (ValueError, TypeError):
                continue
            if exp_freq is not None and abs(freq - exp_freq) <= tol:
                correct += 1
        return correct / total if total > 0 else 0.0


# === block: score_1 (check id='homo_lumo') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not artifact:
            return 0.0
        gold_map = ctx.get("homo_gold", {})
        if not gold_map:
            return 0.0
        tol = ctx.get("orbital_tol", 0.2)
        total_comps = len(gold_map)
        if total_comps == 0:
            return 0.0
        data = {}
        for row in artifact:
            name = row.get("compound", "").strip()
            data[name] = row
        orbital_ok = 0
        descriptor_ok = 0
        for name, gold in gold_map.items():
            row = data.get(name)
            if row is None:
                continue
            try:
                homo = float(row["homo_eV"])
                lumo = float(row["lumo_eV"])
                gap = float(row["gap_eV"])
                elec = float(row["electronegativity_eV"])
                hard = float(row["hardness_eV"])
                soft = float(row["softness_eV_recip"])
                omega = float(row["electrophilicity_eV"])
            except (KeyError, ValueError, TypeError):
                continue
            # check HOMO, LUMO, gap against gold
            if (abs(homo - gold["homo_eV"]) <= tol and
                abs(lumo - gold["lumo_eV"]) <= tol and
                abs(gap - gold["gap_eV"]) <= tol):
                orbital_ok += 1
            # check derived descriptors consistency with own HOMO/LUMO
            calc_elec = -0.5 * (lumo + homo)
            calc_hard = 0.5 * (lumo - homo)
            if calc_hard <= 0:
                calc_soft = 0.0
                calc_omega = 0.0
            else:
                calc_soft = 1.0 / calc_hard
                calc_omega = (calc_elec ** 2) / (2 * calc_hard)
            if (abs(elec - calc_elec) < 0.05 and
                abs(hard - calc_hard) < 0.05 and
                (calc_hard <= 0 or abs(soft - calc_soft) < 0.1) and
                (calc_hard <= 0 or abs(omega - calc_omega) < 1.0)):
                descriptor_ok += 1
        orb_score = orbital_ok / total_comps if total_comps > 0 else 0.0
        desc_score = descriptor_ok / total_comps if total_comps > 0 else 0.0
        return 0.7 * orb_score + 0.3 * desc_score


# === block: score_2 (check id='binding') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not artifact:
            return 0.0
        gold_map = ctx.get("binding_gold", {})
        if not gold_map:
            return 0.0
        tol_kcal = ctx.get("binding_tol_kcal", 5.0)
        tol_dipole = ctx.get("dipole_tol", 0.5)
        data = {}
        for row in artifact:
            name = row.get("compound", "").strip()
            data[name] = row
        correct = 0
        total = len(gold_map)
        for name, gold in gold_map.items():
            row = data.get(name)
            if row is None:
                continue
            try:
                be = float(row["binding_energy_kcal_per_mol"])
                dp = float(row["dipole_moment_debye"])
            except (KeyError, ValueError, TypeError):
                continue
            binding_ok = abs(be - gold["binding_energy_kcal_per_mol"]) <= tol_kcal
            dipole_ok = abs(dp - gold["dipole_moment_debye"]) <= tol_dipole
            if binding_ok and dipole_ok:
                correct += 1
        return correct / total if total > 0 else 0.0


_SCORERS = {
    'ir_freq': score_0,
    'homo_lumo': score_1,
    'binding': score_2,
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
