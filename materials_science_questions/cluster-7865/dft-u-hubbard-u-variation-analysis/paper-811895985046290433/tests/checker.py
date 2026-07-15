import os
import json
import csv

# === author imports / helpers ===
import os
import tarfile
import copy
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
    import os
    import sys

    def load_artifact(path):
        if not path or not os.path.exists(path):
            return None
        if path.endswith('.json'):
            import json
            try:
                with open(path) as f:
                    return json.load(f)
            except Exception:
                return None
        if path.endswith('.csv') or path.endswith('.tsv'):
            import csv
            delim = '\t' if path.endswith('.tsv') else ','
            try:
                with open(path, newline='') as f:
                    return list(csv.DictReader(f, delimiter=delim))
            except Exception:
                return None
        # For binary or unknown file types, attempt to read as text,
        # but gracefully return None if it fails.
        try:
            with open(path) as f:
                return f.read()
        except UnicodeDecodeError:
            return None
        except Exception:
            return None

    # Overwrite the global load_artifact so that the main loop uses this safe version.
    sys.modules[__name__].load_artifact = load_artifact

    return {}


# === block: score_0 (check id='bader_magnetic') ===
def score_0(artifact, step, ctx):
    data = artifact
    models_list = data.get("models", [])
    gold_model_data = step.get("gold_model_data", {})
    tol_bader = step.get("tolerance_bader_charge", 0.15)
    tol_mag = step.get("tolerance_magnetic_moment", 0.2)

    def assign_charges(expected_counts, agent_vals, tol):
        expected_list = []
        for chg, cnt in expected_counts:
            expected_list.extend([chg]*cnt)
        expected_list.sort()
        agent_list = sorted(agent_vals)
        total_err = 0.0
        exp_copy = expected_list[:]
        for ac in agent_list:
            best_idx = min(range(len(exp_copy)), key=lambda i: abs(ac - exp_copy[i]))
            total_err += abs(ac - exp_copy.pop(best_idx))
        mean_err = total_err / len(agent_list) if agent_vals else 0.0
        return mean_err

    scores = []
    for name, gd in gold_model_data.items():
        model = next((m for m in models_list if m.get("name") == name), None)
        if not model:
            scores.append(0.0)
            continue
        atoms = model.get("atoms", [])
        ce_atoms = [a for a in atoms if a.get("element") == "Ce"]
        if len(ce_atoms) != gd.get("Ce_atoms_count"):
            scores.append(0.0)
            continue
        expected_charges = [(eg["bader_charge"], eg["count"]) for eg in gd["Ce_expected"]]
        agent_charges = [a["bader_charge"] for a in ce_atoms]
        charge_err = assign_charges(expected_charges, agent_charges, tol_bader)
        score_charge = max(0.0, 1.0 - charge_err / (2*tol_bader))
        expected_moments = [(eg["magnetic_moment"], eg["count"]) for eg in gd["Ce_expected"]]
        agent_moments = [a["magnetic_moment"] for a in ce_atoms]
        moment_err = assign_charges(expected_moments, agent_moments, tol_mag)
        score_moment = max(0.0, 1.0 - moment_err / (2*tol_mag))
        scores.append(0.5*score_charge + 0.5*score_moment)
    return sum(scores)/len(scores) if scores else 0.0


# === block: score_1 (check id='formation_energy') ===
def score_1(artifact, step, ctx):
    models_list = artifact.get("models", [])
    gold_fe = step.get("gold_formation_energies", {})
    tol_fe = step.get("tolerance_formation_energy", 0.2)
    ordering = step.get("ordering", [])
    close_scores = []
    for name, expected in gold_fe.items():
        model = next((m for m in models_list if m.get("name") == name), None)
        if not model:
            close_scores.append(0.0)
            continue
        fe = model.get("formation_energy_per_Ce")
        if fe is None:
            close_scores.append(0.0)
            continue
        diff = abs(fe - expected)
        if diff <= tol_fe:
            close_scores.append(1.0)
        else:
            close_scores.append(max(0.0, 1.0 - (diff - tol_fe)/tol_fe))
    mean_close = sum(close_scores)/len(close_scores) if close_scores else 0.0

    agent_fe_dict = {}
    for m in models_list:
        fe = m.get("formation_energy_per_Ce")
        if fe is not None:
            agent_fe_dict[m["name"]] = fe

    if all(name in agent_fe_dict for name in ordering):
        correct = 0
        total_pairs = len(ordering) - 1
        for i in range(1, len(ordering)):
            prev = ordering[i-1]
            curr = ordering[i]
            if agent_fe_dict[prev] < agent_fe_dict[curr] + 0.02:
                correct += 1
        order_score = correct / total_pairs if total_pairs > 0 else 1.0
    else:
        order_score = 0.0

    return 0.6 * mean_close + 0.4 * order_score


# === block: score_2 (check id='structural_consistency') ===
def score_2(artifact, step, ctx):
    models_list = artifact.get("models", [])
    bader_th = step.get("bader_threshold", 2.2)
    mag_th = step.get("magnetic_threshold", 0.01)

    violations = 0
    total_ce = 0
    for model in models_list:
        for atom in model.get("atoms", []):
            if atom.get("element") == "Ce":
                total_ce += 1
                mu = atom.get("magnetic_moment", 0.0)
                q = atom.get("bader_charge", 0.0)
                if mu > mag_th and q > bader_th:
                    violations += 1
    if total_ce == 0:
        return 1.0
    return max(0.0, 1.0 - violations / total_ce)


# === block: score_3 (check id='elf_cube_archive') ===
def score_3(artifact, step, ctx):
    import os, tarfile
    path = os.path.join("/app/outputs", step["output_file"])
    if not os.path.isfile(path):
        return 0.0
    try:
        with tarfile.open(path, "r:gz") as tar:
            names = tar.getnames()
            required = step.get("required_files", [])
            present = all(fname in names for fname in required)
            if not present:
                return 0.0
            for fname in required:
                info = tar.getmember(fname)
                if info.size == 0:
                    return 0.0
        return 1.0
    except Exception:
        return 0.0


_SCORERS = {
    'bader_magnetic': score_0,
    'formation_energy': score_1,
    'structural_consistency': score_2,
    'elf_cube_archive': score_3,
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
