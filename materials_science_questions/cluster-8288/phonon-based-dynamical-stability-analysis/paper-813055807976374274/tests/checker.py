import os
import json
import csv

# === author imports / helpers ===
import math, json

def _score_mechanical(artifact, structure, paper):
    try:
        data = artifact[structure]
        ref = paper[structure]
        total_items = 9
        ok = 0
        # Young_modulus_2D: within 20%
        for key in ["biaxial","x_axial","y_axial"]:
            if abs(data["Young_modulus_2D"][key] - ref["Young_modulus_2D"][key]) <= 0.20 * abs(ref["Young_modulus_2D"][key]):
                ok += 1
        # intrinsic_strength: within 25%
        for key in ["biaxial","x_axial","y_axial"]:
            if abs(data["intrinsic_strength"][key] - ref["intrinsic_strength"][key]) <= 0.25 * abs(ref["intrinsic_strength"][key]):
                ok += 1
        # fracture_strain: absolute tolerance 0.02
        for key in ["biaxial","x_axial","y_axial"]:
            if abs(data["fracture_strain"][key] - ref["fracture_strain"][key]) <= 0.02:
                ok += 1
        return ok / total_items
    except (KeyError, TypeError, ZeroDivisionError):
        return 0.0


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


# === block: score_0 (check id='struct_format') ===
def score_0(artifact, step, ctx):
      # artifact is the parsed structures_optimized.json dict
      try:
        b2 = artifact["B2N4-I"]
        b3 = artifact["B3N3-I"]
        # check required keys
        for s in (b2, b3):
          lv = s["lattice_vectors"]
          ap = s["atomic_positions"]
          te = s["total_energy"]
          if not (isinstance(lv, list) and len(lv)==3 and all(len(row)==3 for row in lv)):
            return 0.0
          if not (isinstance(ap, list) and all(isinstance(a,dict) and "element" in a and "x" in a for a in ap)):
            return 0.0
        # atom counts: B2N4 should have 2 B, 4 N; B3N3 3 B, 3 N
        counts_b2 = {"B":0,"N":0}
        for a in b2["atomic_positions"]:
          el = a["element"]
          if el in counts_b2:
            counts_b2[el] += 1
        if counts_b2["B"] != 2 or counts_b2["N"] != 4:
          return 0.0
        counts_b3 = {"B":0,"N":0}
        for a in b3["atomic_positions"]:
          el = a["element"]
          if el in counts_b3:
            counts_b3[el] += 1
        if counts_b3["B"] != 3 or counts_b3["N"] != 3:
          return 0.0
        return 1.0
      except (KeyError, TypeError, IndexError):
        return 0.0


# === block: score_1 (check id='phonon_b2n4') ===
def score_1(artifact, step, ctx):
      try:
        data = artifact["B2N4-I"]
        stable = data["dynamically_stable"]
        min_freq = data["min_phonon_frequency"]
        if stable is True and min_freq > -0.5:
          return 1.0
        else:
          return 0.0
      except (KeyError, TypeError):
        return 0.0


# === block: score_2 (check id='phonon_b3n3') ===
def score_2(artifact, step, ctx):
      try:
        data = artifact["B3N3-I"]
        stable = data["dynamically_stable"]
        min_freq = data["min_phonon_frequency"]
        if stable is True and min_freq > -0.5:
          return 1.0
        else:
          return 0.0
      except (KeyError, TypeError):
        return 0.0


# === block: score_3 (check id='mech_b2n4') ===
def score_3(artifact, step, ctx):
      paper = {
        "B2N4-I": {
          "Young_modulus_2D": {"biaxial": 194, "x_axial": 206, "y_axial": 206},
          "intrinsic_strength": {"biaxial": 36, "x_axial": 40, "y_axial": 40},
          "fracture_strain": {"biaxial": 0.13, "x_axial": 0.13, "y_axial": 0.14}
        }
      }
      return _score_mechanical(artifact, "B2N4-I", paper)


# === block: score_4 (check id='mech_b3n3') ===
def score_4(artifact, step, ctx):
      paper = {
        "B3N3-I": {
          "Young_modulus_2D": {"biaxial": 127, "x_axial": 129, "y_axial": 129},
          "intrinsic_strength": {"biaxial": 27, "x_axial": 17, "y_axial": 17},
          "fracture_strain": {"biaxial": 0.16, "x_axial": 0.08, "y_axial": 0.08}
        }
      }
      return _score_mechanical(artifact, "B3N3-I", paper)


# === block: score_5 (check id='elec_b3n3') ===
def score_5(artifact, step, ctx):
      try:
        data = artifact["B3N3-I"]
        gap = data["band_gap_zero_strain"]
        trans = data["direct_indirect_transition_strain"]
        ok = 0.0
        if abs(gap - 0.06) <= 0.05:
          ok += 0.5
        if 0.04 <= trans <= 0.06:
          ok += 0.5
        return ok
      except (KeyError, TypeError):
        return 0.0


_SCORERS = {
    'struct_format': score_0,
    'phonon_b2n4': score_1,
    'phonon_b3n3': score_2,
    'mech_b2n4': score_3,
    'mech_b3n3': score_4,
    'elec_b3n3': score_5,
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
