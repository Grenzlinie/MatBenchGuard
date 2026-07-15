import os
import json
import csv

# === author imports / helpers ===
import csv, json, math, os
from collections import defaultdict


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
    import csv, os, math
    from collections import defaultdict
    path = os.path.join(outputs_dir, "enthalpy_curves.csv")
    stable = {}
    if os.path.exists(path):
        with open(path, newline='') as f:
            reader = csv.DictReader(f)
            data = []
            for row in reader:
                try:
                    p = float(row["pressure"])
                    h = float(row["enthalpy_per_fu"])
                    phase = row["phase"].strip()
                    data.append((p, h, phase))
                except:
                    pass
        if data:
            p_to_rows = defaultdict(list)
            for p, h, ph in data:
                p_to_rows[p].append((h, ph))
            for p, rows in p_to_rows.items():
                min_h, best_ph = min(rows, key=lambda x: x[0])
                stable[p] = best_ph
            pressures = sorted(stable.keys())
            if pressures:
                closest_p = min(pressures, key=lambda x: abs(x-45))
                stable_45_phase = stable[closest_p]
            else:
                stable_45_phase = None
        else:
            stable_45_phase = None
    else:
        stable_45_phase = None
    return {"stable": stable, "stable_45_phase": stable_45_phase}


# === block: score_0 (check id='step_02') ===
def score_0(artifact, step, ctx):
    import math
    stable = ctx.get("stable", {})
    if not stable:
        return 0.0
    tolerance = float(step.get("tolerance", 5.0))
    def normalize_phase(ph):
        phl = ph.lower()
        if "hexagonal" in phl or "laves" in phl:
            return "hexagonal"
        if "decomp" in phl or "element" in phl:
            return "decomp"
        if "c2" in phl or "c2/c" in phl:
            return "c2"
        if "p2_1" in phl or "p21" in phl:
            return "p21"
        return phl
    phases = []
    pressures = sorted(stable.keys())
    for p in pressures:
        ph = stable[p]
        phases.append((p, normalize_phase(ph)))
    sequence = []
    prev = None
    for p, ph in phases:
        if ph != prev:
            sequence.append((p, ph))
        prev = ph
    expected_phases = ["hexagonal", "decomp", "c2", "p21", "decomp"]
    seq_phases = [s[1] for s in sequence]
    def check_order(seq, expected):
        i = 0
        for e in expected:
            found = -1
            for j in range(i, len(seq)):
                if seq[j] == e:
                    found = j
                    break
            if found == -1:
                return False
            i = found + 1
        return True
    if not check_order(seq_phases, expected_phases):
        return 0.2
    targets = [("hexagonal", "decomp", 20.0),
               ("decomp", "c2", 35.0),
               ("c2", "p21", 54.0),
               ("p21", "decomp", 105.0)]
    score = 0.0
    for from_ph, to_ph, expected_p in targets:
        idx = None
        for i in range(len(seq_phases)-1):
            if seq_phases[i] == from_ph and seq_phases[i+1] == to_ph:
                idx = i+1
                break
        if idx is None:
            continue
        trans_p = sequence[idx][0]
        dev = abs(trans_p - expected_p)
        if dev <= tolerance:
            score += 0.25
    return min(score, 1.0)


# === block: score_1 (check id='step_03') ===
def score_1(artifact, step, ctx):
    if not artifact or not isinstance(artifact, str):
        return 0.0
    try:
        from pymatgen.io.cif import CifParser
        import io
        parser = CifParser.from_string(artifact)
        structure = parser.get_structures()[0]
        sg = structure.get_space_group_info()[0]
        sg_lower = sg.lower().replace(" ", "")
        sg_ok = ("c2/c" in sg_lower) or ("c" in sg_lower and "2" in sg_lower and "/c" in sg_lower)
        comp = structure.composition
        ca = comp.get("Ca", 0)
        li = comp.get("Li", 0)
        if ca+li == 0:
            return 0.0
        comp_ok = (abs(ca/(ca+li) - 1/3) < 0.1) and (ca > 0) and (li > 0)
        ratio_ok = (abs(li/ca - 2.0) < 0.3)
        li_sites = [s for s in structure.sites if s.species_string == "Li"]
        min_li_li = None
        for i in range(len(li_sites)):
            for j in range(i+1, len(li_sites)):
                d = li_sites[i].distance(li_sites[j])
                if min_li_li is None or d < min_li_li:
                    min_li_li = d
        pairing_ok = (min_li_li is not None and min_li_li < 2.5)
        score = 0.0
        if sg_ok:
            score += 0.4
        if comp_ok and ratio_ok:
            score += 0.3
        if pairing_ok:
            score += 0.3
        return min(score, 1.0)
    except:
        return 0.0


# === block: score_2 (check id='step_04') ===
def score_2(artifact, step, ctx):
    if not artifact or not isinstance(artifact, str):
        return 0.0
    try:
        from pymatgen.io.cif import CifParser
        parser = CifParser.from_string(artifact)
        structure = parser.get_structures()[0]
        sg = structure.get_space_group_info()[0]
        sg_lower = sg.lower().replace(" ", "")
        sg_ok = ("p2_1/c" in sg_lower) or ("p21/c" in sg_lower)
        comp = structure.composition
        ca = comp.get("Ca", 0)
        li = comp.get("Li", 0)
        if ca+li == 0:
            return 0.0
        comp_ok = (abs(li/(ca+li) - 2/3) < 0.1) and (ca > 0) and (li > 0)
        beta = structure.lattice.beta
        beta_ok = 89.0 <= beta <= 91.0
        score = 0.0
        if sg_ok:
            score += 0.4
        if comp_ok:
            score += 0.3
        if beta_ok:
            score += 0.3
        return min(score, 1.0)
    except:
        return 0.0


# === block: score_3 (check id='step_06') ===
def score_3(artifact, step, ctx):
    if not artifact:
        return 0.0
    try:
        tc = float(artifact.strip())
    except:
        return 0.0
    stable_phase_45 = ctx.get("stable_45_phase", None)
    if stable_phase_45 is None:
        return 0.0
    def norm(ph):
        phl = ph.lower()
        if "c2" in phl or "c2/c" in phl:
            return "c2"
        return phl
    if norm(stable_phase_45) != "c2":
        return 0.0
    target = 15.0
    tol = 3.0
    abs_diff = abs(tc - target)
    if abs_diff <= tol:
        return 1.0
    else:
        return max(0.0, 1.0 - (abs_diff - tol) / 2.0)


_SCORERS = {
    'step_02': score_0,
    'step_03': score_1,
    'step_04': score_2,
    'step_06': score_3,
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
