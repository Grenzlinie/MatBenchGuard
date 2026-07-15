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


# === block: score_0 (check id='crystal_geometry') ===
def score_0(artifact, step, ctx):
    # scorer body for crystal_geometry
    lengths = {item["id"]: item["value_angstrom"] for item in artifact.get("bond_lengths", [])}
    angles = {item["id"]: item["value_degree"] for item in artifact.get("bond_angles", [])}
    score_len = 0.0
    score_ang = 0.0
    tol_len = step["config"]["bond_lengths_tolerance_angstrom"]
    tol_ang = step["config"]["bond_angles_tolerance_degree"]
    gold_len = step["config"]["gold_bond_lengths"]
    gold_ang = step["config"]["gold_bond_angles"]
    n_len = len(gold_len)
    n_ang = len(gold_ang)
    if n_len > 0:
        correct = 0
        for k, expected in gold_len.items():
            got = lengths.get(k)
            if got is not None and abs(got - expected) <= tol_len:
                correct += 1
        score_len = correct / n_len
    if n_ang > 0:
        correct = 0
        for k, expected in gold_ang.items():
            got = angles.get(k)
            if got is not None and abs(got - expected) <= tol_ang:
                correct += 1
        score_ang = correct / n_ang
    # equal weight to lengths and angles
    if n_len + n_ang > 0:
        final = (score_len * n_len + score_ang * n_ang) / (n_len + n_ang)
    else:
        final = 0.0
    return final


# === block: score_1 (check id='mulliken_population') ===
def score_1(artifact, step, ctx):
    # scorer body for mulliken_population
    crystal = artifact.get("crystal", {})
    gas = artifact.get("gas", {})
    tol_charge = step["config"]["charge_tolerance"]
    tol_bond = step["config"]["bond_population_tolerance"]
    gold_crystal_charges = step["config"]["gold_crystal_charges"]
    gold_crystal_bonds = step["config"]["gold_crystal_bonds"]
    gold_gas_charges = step["config"]["gold_gas_charges"]
    gold_gas_bonds = step["config"]["gold_gas_bonds"]

    crystal_charges = crystal.get("atomic_charges", {})
    crystal_bonds = crystal.get("bond_populations", {})
    gas_charges = gas.get("atomic_charges", {})
    gas_bonds = gas.get("bond_populations", {})

    correct = 0
    total = 0

    def check_dict(agent_dict, gold_dict, tol):
        c = 0
        t = 0
        for k, expected in gold_dict.items():
            t += 1
            got = agent_dict.get(k)
            if got is not None and abs(got - expected) <= tol:
                c += 1
        return c, t

    c1, t1 = check_dict(crystal_charges, gold_crystal_charges, tol_charge)
    c2, t2 = check_dict(crystal_bonds, gold_crystal_bonds, tol_bond)
    c3, t3 = check_dict(gas_charges, gold_gas_charges, tol_charge)
    c4, t4 = check_dict(gas_bonds, gold_gas_bonds, tol_bond)

    correct = c1 + c2 + c3 + c4
    total = t1 + t2 + t3 + t4
    if total == 0:
        return 0.0
    return correct / total


# === block: score_2 (check id='pDOS_hb') ===
def score_2(artifact, step, ctx):
    # scorer body for pDOS_hb
    overlap = artifact.get("overlap_energy_range", "")
    bonds = artifact.get("hydrogen_bonds", [])
    cfg = step["config"]
    expected_range = cfg["expected_overlap_range"]
    required = cfg["required_hbonds"]
    energy_range = cfg.get("max_overlap_energy_range", [])
    energy_weight = cfg["energy_range_weight"]
    hbond_weight = cfg["hbonds_weight"]

    score_range = 1.0 if overlap == expected_range else 0.0

    # check required hydrogen bonds exist with correct donor/acceptor/type
    present = set()
    for b in bonds:
        donor = b.get("donor")
        acceptor = b.get("acceptor")
        typ = b.get("type")
        if donor and acceptor and typ:
            present.add((donor, acceptor, typ))

    required_set = set((r["donor"], r["acceptor"], r["type"]) for r in required)
    score_hb = 1.0 if required_set.issubset(present) else 0.0

    # optionally check max_overlap_energy plausibility for required bonds
    if score_hb > 0 and energy_range:
        lo, hi = energy_range
        for r in required:
            for b in bonds:
                if b.get("donor") == r["donor"] and b.get("acceptor") == r["acceptor"] and b.get("type") == r["type"]:
                    eng = b.get("max_overlap_energy")
                    if isinstance(eng, (int, float)) and not (lo <= eng <= hi):
                        score_hb = 0.0
                        break
            if score_hb == 0.0:
                break

    return energy_weight * score_range + hbond_weight * score_hb


_SCORERS = {
    'crystal_geometry': score_0,
    'mulliken_population': score_1,
    'pDOS_hb': score_2,
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
