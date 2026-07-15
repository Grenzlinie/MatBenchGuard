import os
import json
import csv

# === author imports / helpers ===
import os, csv


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
    def prepare(outputs_dir, spec):
        gold_struct = {
            "HgCr2S4": {"a0_angstrom": 10.37, "B0_GPa": 90.15, "deltaH_eV": -0.98,
                        "total_magnetic_moment_mu_B": 6.0,
                        "exchange_constant_N0alpha_eV": -0.34, "exchange_constant_N0beta_eV": 0.26},
            "HgCr2Se4": {"a0_angstrom": 10.89, "B0_GPa": 72.83, "deltaH_eV": -0.84,
                         "total_magnetic_moment_mu_B": 6.0,
                         "exchange_constant_N0alpha_eV": -0.30, "exchange_constant_N0beta_eV": 0.22}
        }
        gold_transport = {
            ("HgCr2S4", 200): {"Seebeck_uV_K": 170, "power_factor_arb_units": 5.5},
            ("HgCr2S4", 400): {"Seebeck_uV_K": 240, "power_factor_arb_units": 12.0},
            ("HgCr2S4", 600): {"Seebeck_uV_K": 290, "power_factor_arb_units": 20.0},
            ("HgCr2Se4", 200): {"Seebeck_uV_K": 120, "power_factor_arb_units": 3.5},
            ("HgCr2Se4", 400): {"Seebeck_uV_K": 180, "power_factor_arb_units": 7.5},
            ("HgCr2Se4", 600): {"Seebeck_uV_K": 230, "power_factor_arb_units": 11.0}
        }
        return {"gold_struct": gold_struct, "gold_transport": gold_transport}


# === block: score_0 (check id='check_structural_magnetic') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold = ctx["gold_struct"]
        tol = {
            "a0_angstrom": 0.2,
            "B0_GPa": 20.0,
            "deltaH_eV": 0.2,
            "total_magnetic_moment_mu_B": 0.5,
            "exchange_constant_N0alpha_eV": 0.1,
            "exchange_constant_N0beta_eV": 0.1
        }
        columns = ["a0_angstrom", "B0_GPa", "deltaH_eV", "total_magnetic_moment_mu_B",
                   "exchange_constant_N0alpha_eV", "exchange_constant_N0beta_eV"]
        score = 0.0
        n = len(artifact)
        for row in artifact:
            comp = row["compound"].strip()
            if comp not in gold:
                continue
            g = gold[comp]
            for col in columns:
                try:
                    val = float(row[col])
                    gval = g[col]
                    if abs(val - gval) <= tol[col]:
                        score += 1
                except (ValueError, KeyError):
                    pass
        total_possible = len(columns) * 2   # two compounds
        if total_possible == 0:
            return 0.0
        return score / total_possible


# === block: score_1 (check id='check_transport_properties') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold = ctx["gold_transport"]
        tol_Seebeck = 30.0
        # 1. Seebeck numeric closeness
        se_score = 0.0
        n_se = len(artifact)
        for row in artifact:
            comp = row["compound"].strip()
            T = int(row["temperature_K"])
            try:
                see_val = float(row["Seebeck_uV_K"])
            except (ValueError, KeyError):
                continue
            key = (comp, T)
            if key in gold:
                if abs(see_val - gold[key]["Seebeck_uV_K"]) <= tol_Seebeck:
                    se_score += 1
        se_frac = se_score / n_se if n_se else 0.0

        # 2. Monotonicity and ordering (Seebeck)
        see_dict = {}
        for row in artifact:
            try:
                comp = row["compound"].strip()
                T = int(row["temperature_K"])
                val = float(row["Seebeck_uV_K"])
                see_dict[(comp, T)] = val
            except (ValueError, KeyError):
                pass
        monotonic_checks = 0
        for comp in ["HgCr2S4", "HgCr2Se4"]:
            vals = [see_dict.get((comp,200)), see_dict.get((comp,400)), see_dict.get((comp,600))]
            if all(v is not None for v in vals):
                if vals[0] < vals[1]: monotonic_checks += 1
                if vals[1] < vals[2]: monotonic_checks += 1
        ordering_checks = 0
        for T in [200,400,600]:
            s4 = see_dict.get(("HgCr2S4",T))
            se = see_dict.get(("HgCr2Se4",T))
            if s4 is not None and se is not None:
                if s4 > se:
                    ordering_checks += 1
        monotonic_ordering_score = (monotonic_checks + ordering_checks) / 7.0 if 7 else 0.0

        # 3. Power factor monotonicity and ordering at 600
        pf_dict = {}
        for row in artifact:
            try:
                comp = row["compound"].strip()
                T = int(row["temperature_K"])
                val = float(row["power_factor_arb_units"])
                pf_dict[(comp, T)] = val
            except (ValueError, KeyError):
                pass
        pf_monotonic_checks = 0
        for comp in ["HgCr2S4", "HgCr2Se4"]:
            vals = [pf_dict.get((comp,200)), pf_dict.get((comp,400)), pf_dict.get((comp,600))]
            if all(v is not None for v in vals):
                if vals[0] < vals[1]: pf_monotonic_checks += 1
                if vals[1] < vals[2]: pf_monotonic_checks += 1
        pf_order = 0
        pfS4 = pf_dict.get(("HgCr2S4",600))
        pfSe = pf_dict.get(("HgCr2Se4",600))
        if pfS4 is not None and pfSe is not None:
            if pfS4 > pfSe: pf_order = 1
        pf_score = (pf_monotonic_checks + pf_order) / 5.0 if 5 else 0.0

        final_score = 0.3 * se_frac + 0.4 * monotonic_ordering_score + 0.3 * pf_score
        return min(1.0, max(0.0, final_score))


_SCORERS = {
    'check_structural_magnetic': score_0,
    'check_transport_properties': score_1,
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
