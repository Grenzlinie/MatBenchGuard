import os
import json
import csv

# === author imports / helpers ===
import csv
import math
from collections import defaultdict

def parse_csv(path):
    with open(path, newline='') as f:
        return list(csv.DictReader(f))


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
        outputs = {}
        for key, fname in [
            ("stability", "step_01_stability.csv"),
            ("defect", "step_02_defect_formation.csv"),
            ("band_gaps", "step_03_band_gaps.csv"),
            ("absorption", "step_04_absorption_spectra.csv"),
        ]:
            path = os.path.join(outputs_dir, fname)
            if os.path.exists(path):
                outputs[key] = parse_csv(path)
            else:
                outputs[key] = None
        return {"outputs": outputs}


# === block: score_0 (check id='stability') ===
def score_0(artifact, step, ctx):
        def float_col(row, col):
            try:
                return float(row[col])
            except (ValueError, TypeError):
                return None
        rows = artifact
        gold = step.get("gold", {})
        compounds_present = [row.get("compound", "").strip() for row in rows]
        ternary = gold.get("ternary_compounds", ["Cu4SnS4", "Cu2SnS3", "Cu4Sn7S16"])
        present_tern = [c for c in ternary if c in compounds_present]
        score_presence = len(present_tern) / len(ternary)
    
        # collect enthalpies
        h_map = {}
        for row in rows:
            c = row.get("compound", "").strip()
            v = float_col(row, "formation_enthalpy_eV_per_atom")
            if v is not None:
                h_map[c] = v
        range_ok = all(-5.0 <= h_map.get(c, 1) <= 0.0 for c in present_tern)
        score_range = 1.0 if range_ok else 0.0
    
        # stability ordering: Cu2SnS3 should be smallest (most negative) among ternaries
        h_vals = {c: h_map[c] for c in present_tern if c in h_map}
        score_order = 0.0
        if len(h_vals) >= 3:
            if h_vals.get("Cu2SnS3", 0) <= h_vals.get("Cu4SnS4", 0) and h_vals.get("Cu2SnS3", 0) <= h_vals.get("Cu4Sn7S16", 0):
                score_order = 1.0
            elif h_vals.get("Cu2SnS3", 0) <= h_vals.get("Cu4SnS4", 0) or h_vals.get("Cu2SnS3", 0) <= h_vals.get("Cu4Sn7S16", 0):
                score_order = 0.5
        elif len(h_vals) == 2:
            other = [c for c in h_vals if c != "Cu2SnS3"]
            if other and h_vals.get("Cu2SnS3", 0) <= h_vals[other[0]]:
                score_order = 1.0
        elif len(h_vals) == 1:
            score_order = 1.0
    
        total = 0.3 * score_presence + 0.2 * score_range + 0.5 * score_order
        return min(total, 1.0)


# === block: score_1 (check id='defect') ===
def score_1(artifact, step, ctx):
        def float_col(row, col):
            try:
                return float(row[col])
            except (ValueError, TypeError):
                return None
        rows = artifact
        ctx_outputs = ctx.get("outputs", {})
        band_gaps_rows = ctx_outputs.get("band_gaps", [])
        # build gap map: compound -> { gap_type: value }
        gap_map = {}
        for r in band_gaps_rows:
            c = r.get("compound", "").strip()
            typ = r.get("gap_type", "").strip().lower()
            val = float_col(r, "quasiparticle_gap_eV")
            if c and val is not None:
                if c not in gap_map:
                    gap_map[c] = {}
                gap_map[c][typ] = val

        compounds = ["Cu4SnS4", "Cu2SnS3", "Cu4Sn7S16"]

        # parse defect rows for pinning information
        pin_rows = [row for row in rows if row.get("compound", "").strip() == "E_F_pin_range"]
        pin_range_map = {}   # compound -> (min_eV, max_eV)

        import re
        def parse_range_str(s):
            """Try to parse 'min-max' style range from string, returning (min, max) or None."""
            nums = re.findall(r'-?\d+\.?\d*(?:[eE][+-]?\d+)?', s)
            if len(nums) >= 2:
                vals = [float(v) for v in nums[:2]]
                return min(vals), max(vals)
            return None

        # first pass: look for dash-separated range in formation_energy_eV
        for pr in pin_rows:
            cs = pr.get("charge_state", "").strip()   # may hold compound name
            fev = pr.get("formation_energy_eV", "").strip()
            if fev == "":
                continue
            # try to parse as float first (single value)
            single_val = float_col(pr, "formation_energy_eV")
            if single_val is not None:
                # single floats will be processed in second step
                continue
            # not a float, maybe range string
            rng = parse_range_str(fev)
            if rng is not None:
                lo, hi = rng
                # assign compound
                comp = None
                if cs in compounds:
                    comp = cs
                elif cs == "" and not pin_range_map:
                    comp = compounds[0]
                elif cs == "" and pin_range_map:
                    # assign next unused compound
                    for c in compounds:
                        if c not in pin_range_map:
                            comp = c
                            break
                if comp is not None:
                    pin_range_map[comp] = (lo, hi)

        # second pass: handle any remaining pin_rows that contain single floats (min, max)
        float_rows = []
        for pr in pin_rows:
            cs = pr.get("charge_state", "").strip()
            single = float_col(pr, "formation_energy_eV")
            if single is not None:
                float_rows.append((cs, single))

        # group by charge_state (compound name) and derive min/max
        float_by_comp = {}
        for cs, val in float_rows:
            comp_name = cs if cs in compounds else ""
            float_by_comp.setdefault(comp_name, []).append(val)
        for comp_key, vals in float_by_comp.items():
            if comp_key == "":
                # assign to next compound not yet in pin_range_map
                for c in compounds:
                    if c not in pin_range_map:
                        if len(vals) >= 2:
                            pin_range_map[c] = (min(vals), max(vals))
                        elif len(vals) == 1:
                            pin_range_map[c] = (min(vals), max(vals))
                        break
            else:
                if comp_key not in pin_range_map and vals:
                    pin_range_map[comp_key] = (min(vals), max(vals))

        score = 0.0

        # 1. presence bonus: up to 0.3 for having ranges for all three compounds
        presence = len(pin_range_map) / 3.0
        score += 0.3 * presence

        # 2. Cu2SnS3 pinning above CBM (0.4)
        cu2sns3_gap = gap_map.get("Cu2SnS3", {}).get("direct", None)
        if cu2sns3_gap is not None:
            pin_cu2 = pin_range_map.get("Cu2SnS3")
            if pin_cu2:
                lo, hi = pin_cu2
                if lo >= cu2sns3_gap * 0.9 and hi >= cu2sns3_gap * 0.9:
                    score += 0.4
                elif lo >= cu2sns3_gap * 0.8:
                    score += 0.2

        # 3. other compounds pinning inside gap (0.4)
        other_ok = 0.0
        for comp in ["Cu4SnS4", "Cu4Sn7S16"]:
            gap_val = gap_map.get(comp, {}).get("direct", gap_map.get(comp, {}).get("indirect", None))
            if gap_val is None:
                continue
            pin_comp = pin_range_map.get(comp)
            if pin_comp:
                lo, hi = pin_comp
                if hi <= gap_val * 1.1 and lo >= -1.0:
                    other_ok += 1.0
        score += 0.4 * (other_ok / 2.0)

        return min(score, 1.0)


# === block: score_2 (check id='band_gaps') ===
def score_2(artifact, step, ctx):
        def float_col(row, col):
            try:
                return float(row[col])
            except (ValueError, TypeError):
                return None
        rows = artifact
        gold = step.get("gold", {})
        gaps_gold = gold.get("gaps", {})
        tol = gold.get("tolerance", 0.2)
        expected_types = gold.get("expected_type", {})
        # build reported map: compound -> {type: gap}
        reported = {}
        types_ok = {}
        for r in rows:
            c = r.get("compound", "").strip()
            typ = r.get("gap_type", "").strip().lower()
            val = float_col(r, "quasiparticle_gap_eV")
            if c and typ and val is not None:
                if c not in reported:
                    reported[c] = {}
                reported[c][typ] = val
                if expected_types.get(c) == typ:
                    types_ok[c] = True
        # score each compund
        score_parts = []
        for comp, gold_dict in gaps_gold.items():
            rep = reported.get(comp, {})
            for typ, exp_gap in gold_dict.items():
                rep_gap = rep.get(typ, None)
                if rep_gap is not None:
                    diff = abs(rep_gap - exp_gap)
                    if diff <= tol:
                        score_parts.append(1.0)
                    else:
                        # partial credit beyond tol, decay to zero at 2*tol
                        extra = diff - tol
                        credit = max(0.0, 1.0 - extra / (2*tol))
                        score_parts.append(credit)
                else:
                    score_parts.append(0.0)
        # also auto-correct type for basic compound (extra credit? we'll incorporate type check into weight)
        type_score = 0.0
        for comp in expected_types:
            if types_ok.get(comp, False):
                type_score += 1.0
        if expected_types:
            type_score /= len(expected_types)
        else:
            type_score = 1.0
        if score_parts:
            mean_gap = sum(score_parts) / len(score_parts)
        else:
            mean_gap = 0.0
        final = 0.8 * mean_gap + 0.2 * type_score
        return final


# === block: score_3 (check id='absorption') ===
def score_3(artifact, step, ctx):
        def float_col(row, col):
            try:
                return float(row[col])
            except (ValueError, TypeError):
                return None
        rows = artifact
        gold = step.get("gold", {})
        compounds = gold.get("expected_compounds", ["Cu4SnS4", "Cu2SnS3", "Cu4Sn7S16"])
        # group by compound
        data = defaultdict(list)
        for r in rows:
            c = r.get("compound", "").strip()
            e = float_col(r, "energy_eV")
            a = float_col(r, "absorption_coefficient_cm-1")
            if c and e is not None and a is not None:
                data[c].append((e, a))
        # check all three compounds present
        present = [c for c in compounds if c in data]
        score_pres = len(present) / len(compounds)
        score_grid = 0.0
        for c in present:
            energies = sorted([e for e, a in data[c]])
            if energies and energies[0] <= 0.1 and energies[-1] >= 2.9:
                # at least covers [0.1,2.9]
                score_grid += 1.0
        score_grid = score_grid / len(present) if present else 0.0
        # Cu2SnS3 max absorption > threshold
        score_max = 0.0
        if "Cu2SnS3" in data:
            max_abs = max(a for e, a in data["Cu2SnS3"])
            if max_abs >= 1e5:
                score_max += 0.4
            elif max_abs >= 1e4:
                score_max += 0.2
        if "Cu4SnS4" in data:
            max_abs = max(a for e, a in data["Cu4SnS4"])
            if max_abs >= 1e5:
                score_max += 0.3
            elif max_abs >= 1e4:
                score_max += 0.1
        # Cu4Sn7S16 lower absorption near onset
        score_comp = 0.0
        if "Cu4Sn7S16" in data and "Cu2SnS3" in data:
            # compare absorption at energy around 1.0-1.2 eV
            def get_abs_at(compound, target_energy, window=0.1):
                vals = []
                for e, a in data.get(compound, []):
                    if abs(e - target_energy) <= window:
                        vals.append(a)
                if vals:
                    return sum(vals) / len(vals)
                return None
            a_cu4sn7s16 = get_abs_at("Cu4Sn7S16", 0.9, 0.15)
            a_cu2sns3 = get_abs_at("Cu2SnS3", 0.9, 0.15)
            if a_cu4sn7s16 is not None and a_cu2sns3 is not None and a_cu4sn7s16 < a_cu2sns3 * 0.7:
                score_comp = 0.3
            elif a_cu4sn7s16 is not None and a_cu2sns3 is not None and a_cu4sn7s16 < a_cu2sns3:
                score_comp = 0.15
        final = 0.2 * score_pres + 0.2 * score_grid + score_max + score_comp
        return min(final, 1.0)


_SCORERS = {
    'stability': score_0,
    'defect': score_1,
    'band_gaps': score_2,
    'absorption': score_3,
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
