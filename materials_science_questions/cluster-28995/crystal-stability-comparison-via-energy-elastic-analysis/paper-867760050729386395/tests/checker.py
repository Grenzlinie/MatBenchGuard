import os
import json
import csv

# === author imports / helpers ===
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
        uniform_params = {
            "rho0": 0.153,
            "eps0": -16.4,
            "K": 240,
            "S0": 33.4,
            "L": 84
        }
        # Gold phases for fixed Yp
        fixed_yp_gold = [
            {"rho_B": 0.01, "Y_p": 0.5, "phase": "droplet"},
            {"rho_B": 0.024, "Y_p": 0.5, "phase": "rod"},
            {"rho_B": 0.05, "Y_p": 0.5, "phase": "slab"},
            {"rho_B": 0.08, "Y_p": 0.5, "phase": "tube"},
            {"rho_B": 0.09, "Y_p": 0.5, "phase": "bubble"},
            {"rho_B": 0.01, "Y_p": 0.3, "phase": "droplet"},
            {"rho_B": 0.03, "Y_p": 0.3, "phase": "rod"},
            {"rho_B": 0.01, "Y_p": 0.1, "phase": "droplet"},
            {"rho_B": 0.03, "Y_p": 0.1, "phase": "rod"}
        ]
        # Gold droplet radii for Yp=0.5 (fcc) from Table III
        fixed_yp_radii = {
            0.012: 6.86,
            0.014: 7.04,
            0.016: 7.23,
            0.018: 7.61,
            0.020: 7.79
        }
        # Gold for catalyzed matter: densities, phase, lattice
        catalyzed_gold = {
            0.01: {"phase": "droplet", "lattice": "bcc", "R_fcc_tol": 6.67},
            0.03: {"phase": "droplet", "lattice": "fcc"},
            0.056: {"phase": "rod"}
        }
        return {
            "uniform_params": uniform_params,
            "fixed_yp_gold": fixed_yp_gold,
            "fixed_yp_radii": fixed_yp_radii,
            "catalyzed_gold": catalyzed_gold
        }


# === block: score_0 (check id='fixed_Yp') ===
def score_0(artifact, step, ctx):
        entries = artifact
        entry_map = {}
        for e in entries:
            rho = e.get("rho_B")
            yp = e.get("Y_p")
            if rho is not None and yp is not None:
                entry_map[(round(rho, 4), round(yp, 2))] = e

        total = 0
        passed = 0

        gold_phases = ctx["fixed_yp_gold"]
        for g in gold_phases:
            total += 1
            key = (round(g["rho_B"],4), round(g["Y_p"],2))
            if key in entry_map:
                e = entry_map[key]
                if e.get("pasta_phase") == g["phase"]:
                    passed += 1

        radii_gold = ctx["fixed_yp_radii"]
        for rho_d, rad_gold in radii_gold.items():
            key = (round(rho_d,4), 0.5)
            if key in entry_map:
                e = entry_map[key]
                if e.get("pasta_phase") == "droplet" and "droplet_radius" in e:
                    total += 1
                    rd = e["droplet_radius"]
                    if rd is not None and rad_gold > 0 and abs(rd - rad_gold) / rad_gold <= 0.10:
                        passed += 1
                    total += 1
                    R = rd
                    a = e.get("lattice_constant")
                    u = e.get("volume_fraction")
                    if R and a and a > 0 and u is not None:
                        calc_u = (R / a) ** 3
                        if abs(calc_u - u) <= 0.02:
                            passed += 1

        for e in entries:
            if e.get("pasta_phase") == "droplet":
                R = e.get("droplet_radius")
                a = e.get("lattice_constant")
                u = e.get("volume_fraction")
                if R and a and a > 0 and u is not None:
                    total += 1
                    calc_u = (R / a) ** 3
                    if abs(calc_u - u) <= 0.02:
                        passed += 1

        if total == 0:
            return 0.0
        return passed / total


# === block: score_1 (check id='catalyzed') ===
def score_1(artifact, step, ctx):
        entries = artifact
        gold = ctx["catalyzed_gold"]
        tol_rho = 0.005
        total = 0
        passed = 0

        for den, g in gold.items():
            total += 1
            # find closest agent entry within tol_rho
            best = None
            best_diff = float("inf")
            for e in entries:
                rho = e.get("rho_B")
                if rho is None:
                    continue
                diff = abs(rho - den)
                if diff < tol_rho and diff < best_diff:
                    best = e
                    best_diff = diff
            if best is not None:
                if best.get("pasta_phase") == g["phase"]:
                    if g["phase"] == "droplet":
                        if best.get("lattice_type") == g["lattice"]:
                            passed += 1
                    else:
                        passed += 1

        for e in entries:
            if e.get("pasta_phase") == "droplet" and "lattice_type" in e and "energy_fcc" in e and "energy_bcc" in e:
                total += 1
                lt = e["lattice_type"]
                efcc = e["energy_fcc"]
                ebcc = e["energy_bcc"]
                if lt == "fcc" and efcc < ebcc:
                    passed += 1
                elif lt == "bcc" and ebcc < efcc:
                    passed += 1

        for e in entries:
            if e.get("pasta_phase") == "droplet":
                for prefix in ["fcc", "bcc"]:
                    R = e.get(f"droplet_radius_{prefix}")
                    a = e.get(f"lattice_constant_{prefix}")
                    u = e.get(f"volume_fraction_{prefix}")
                    if R and a and a > 0 and u is not None:
                        total += 1
                        calc_u = (R / a) ** 3
                        if abs(calc_u - u) <= 0.02:
                            passed += 1

        for e in entries:
            if "Coulomb_energy_per_baryon" in e and e["Coulomb_energy_per_baryon"] is not None:
                total += 1
                if e["Coulomb_energy_per_baryon"] >= 0:
                    passed += 1

        for e in entries:
            if "proton_number_fraction" in e and e["proton_number_fraction"] is not None:
                total += 1
                if 0 <= e["proton_number_fraction"] <= 0.5:
                    passed += 1

        if total == 0:
            return 0.0
        return passed / total


_SCORERS = {
    'fixed_Yp': score_0,
    'catalyzed': score_1,
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
