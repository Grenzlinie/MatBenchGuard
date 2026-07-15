import os
import json
import csv

# === author imports / helpers ===
import re
import json


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


# === block: score_0 (check id='check_properties') ===
def score_0(artifact, step, ctx):
        gold_table = step["gold"]
        tol = step["tolerances"]
        total = 0
        ok = 0
        for tm in ["Sc", "Ti", "V", "W"]:
            data = artifact.get(tm)
            if not isinstance(data, dict):
                continue
            g = gold_table[tm]
            # magnetic_moment
            try:
                if abs(data.get("magnetic_moment", -999) - g["magnetic_moment"]) <= tol["magnetic_moment"] + 1e-6:
                    ok += 1
            except Exception:
                pass
            total += 1
            # HOMO_LUMO_gap
            try:
                if abs(data.get("HOMO_LUMO_gap", -999) - g["HOMO_LUMO_gap"]) <= tol["HOMO_LUMO_gap"] + 1e-6:
                    ok += 1
            except Exception:
                pass
            total += 1
            # Eb
            try:
                if abs(data.get("Eb", -999) - g["Eb"]) <= tol["Eb"] + 1e-6:
                    ok += 1
            except Exception:
                pass
            total += 1
            # Ef
            try:
                if abs(data.get("Ef", -999) - g["Ef"]) <= tol["Ef"] + 1e-6:
                    ok += 1
            except Exception:
                pass
            total += 1
            # De
            try:
                if abs(data.get("De", -999) - g["De"]) <= tol["De"] + 1e-6:
                    ok += 1
            except Exception:
                pass
            total += 1
            # symmetry
            if str(data.get("symmetry", "")).strip().lower() == "d6d":
                ok += 1
            total += 1
        # isomer energies for W
        w_data = artifact.get("W", {})
        isomers = w_data.get("isomer_energies")
        if isinstance(isomers, list):
            gold_w = gold_table["W"]["isomer_energies"]
            gold_map = {item["isomer_label"]: item["relative_energy"] for item in gold_w}
            for item in isomers:
                lbl = item.get("isomer_label")
                if lbl in gold_map:
                    try:
                        if abs(item.get("relative_energy", -999) - gold_map[lbl]) <= tol["isomer_energy"] + 1e-6:
                            ok += 1
                    except Exception:
                        pass
                total += 1
        return ok / total if total > 0 else 0.0


# === block: score_1 (check id='check_xyz') ===
def score_1(artifact, step, ctx):
        required = set(step.get("required_tms", []))
        found = set()
        text = artifact.strip()
        lines = text.splitlines()
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if not line:
                i += 1
                continue
            try:
                natoms = int(line)
            except ValueError:
                i += 1
                continue
            if i + 1 >= len(lines):
                break
            comment = lines[i + 1].strip()
            m = re.search(r'TM=(\w+)', comment)
            if m and natoms == 15 and 'D6d' in comment and 'E=' in comment:
                tm = m.group(1)
                if tm in required:
                    try:
                        energy_str = comment.split('E=')[-1].split()[0]
                        energy = float(energy_str)
                    except Exception:
                        energy = None
                    if energy is not None and energy < 0:
                        found.add(tm)
            i += natoms + 2
        return len(found) / len(required) if required else 0.0


_SCORERS = {
    'check_properties': score_0,
    'check_xyz': score_1,
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
