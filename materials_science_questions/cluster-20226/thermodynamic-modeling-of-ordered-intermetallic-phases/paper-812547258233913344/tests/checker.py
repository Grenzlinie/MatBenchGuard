import os
import json
import csv

# === author imports / helpers ===
import csv
import json
import os
import sys
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
    return {'spec': spec}


# === block: score_0 (check id='sublattice') ===
def score_0(artifact, step, ctx):
        if not artifact or len(artifact) != 4:
            return 0.0
        required = ["sublattice_number", "occupancy_V"]
        for row in artifact:
            for col in required:
                if col not in row:
                    return 0.0
        try:
            occs = [float(row["occupancy_V"]) for row in artifact]
        except:
            return 0.0
        total = sum(occs)
        hid = step.get("hidden", {})
        tol = hid.get("tolerances", {})
        sum_tol = tol.get("occupancy_sum_tol", 0.01)
        max_min = tol.get("max_occupancy_min", 0.8)
        others_max = tol.get("others_max", 0.2)
        if abs(total - 1.0) > sum_tol:
            return 0.0
        max_occ = max(occs)
        others = [o for o in occs if o < max_occ]
        if not others or len(others) != 3:
            return 0.0
        if max_occ < max_min or any(o > others_max for o in others):
            return 0.0
        return 1.0


# === block: score_1 (check id='sro') ===
def score_1(artifact, step, ctx):
    def scorer(artifact, step, ctx):
        if not artifact:
            return 0.0
        required = ["pair", "shell", "alpha"]
        data = {}
        for row in artifact:
            for col in required:
                if col not in row:
                    return 0.0
            try:
                p = str(row["pair"]).strip()
                s = int(row["shell"])
                a = float(row["alpha"])
            except:
                return 0.0
            data[(p, s)] = a
        expected_pairs = ["Co-V", "Ni-V", "Co-Ni"]
        expected_shells = [1, 2]
        if len(data) != 6:
            return 0.0
        hid = step.get("hidden", {})
        tol = hid.get("tolerances", {})
        neg_thr = tol.get("negative_threshold", -0.01)
        pos_thr = tol.get("positive_threshold", 0.01)
        near_zero = tol.get("near_zero_range", [-0.05, 0.05])
        conditions = {
            ("Co-V", 1): "negative",
            ("Ni-V", 1): "negative",
            ("Co-Ni", 1): "near_zero",
            ("Co-V", 2): "positive",
            ("Ni-V", 2): "positive",
            ("Co-Ni", 2): "near_zero"
        }
        passed = 0
        total = len(conditions)
        for (pair, shell), exp in conditions.items():
            val = data.get((pair, shell))
            if val is None:
                continue
            if exp == "negative" and val < neg_thr:
                passed += 1
            elif exp == "positive" and val > pos_thr:
                passed += 1
            elif exp == "near_zero" and near_zero[0] <= val <= near_zero[1]:
                passed += 1
        return passed / total if total > 0 else 0.0


# === block: score_2 (check id='specific_heat') ===
def score_2(artifact, step, ctx):
    def scorer(artifact, step, ctx):
        if not artifact:
            return 0.0
        required = ["temperature_K", "C_V_eV_per_atom"]
        temps = []
        cvs = []
        for row in artifact:
            for col in required:
                if col not in row:
                    return 0.0
            try:
                t = float(row["temperature_K"])
                cv = float(row["C_V_eV_per_atom"])
            except:
                return 0.0
            temps.append(t)
            cvs.append(cv)
        if not temps:
            return 0.0
        max_idx = max(range(len(cvs)), key=lambda i: cvs[i])
        peak_t = temps[max_idx]
        peak_cv = cvs[max_idx]
        hid = step.get("hidden", {})
        temp_range = hid.get("peak_temp_range", [1350, 1550])
        cv_range = hid.get("peak_height_range", [0.35, 0.55])
        if temp_range[0] <= peak_t <= temp_range[1] and cv_range[0] <= peak_cv <= cv_range[1]:
            return 1.0
        return 0.0


# === block: score_3 (check id='relaxation_msad') ===
def score_3(artifact, step, ctx):
    def scorer(artifact, step, ctx):
        if not artifact:
            return 0.0
        required = ["state", "relaxation_energy_eV_per_atom", "MSAD_A2"]
        expected_states = {"ordered_1000K", "SRO_1540K", "random_4000K"}
        state_data = {}
        for row in artifact:
            for col in required:
                if col not in row:
                    return 0.0
            try:
                s = str(row["state"]).strip()
                e = float(row["relaxation_energy_eV_per_atom"])
                m = float(row["MSAD_A2"])
            except:
                return 0.0
            if s not in expected_states:
                return 0.0
            state_data[s] = (e, m)
        if len(state_data) != 3:
            return 0.0
        hid = step.get("hidden", {})
        e_range = hid.get("relax_energy_range", [0.0, 0.05])
        m_range = hid.get("msad_range", [0.0, 0.05])
        order = ["ordered_1000K", "SRO_1540K", "random_4000K"]
        energies = [state_data[s][0] for s in order]
        msads = [state_data[s][1] for s in order]
        for e in energies:
            if not (e_range[0] <= e <= e_range[1]):
                return 0.0
        for m in msads:
            if not (m_range[0] <= m <= m_range[1]):
                return 0.0
        if hid.get("require_monotonic_increase", True):
            if not (energies[0] < energies[1] < energies[2]):
                return 0.0
            if not (msads[0] < msads[1] < msads[2]):
                return 0.0
        return 1.0


_SCORERS = {
    'sublattice': score_0,
    'sro': score_1,
    'specific_heat': score_2,
    'relaxation_msad': score_3,
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
