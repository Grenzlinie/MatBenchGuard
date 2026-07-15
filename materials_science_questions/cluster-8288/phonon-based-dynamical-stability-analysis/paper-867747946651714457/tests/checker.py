import os
import json
import csv

# === author imports / helpers ===
import json, math


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


# === block: score_0 (check id='s01') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold = step.get('gold', {})
        tol_abs = step.get('tolerance_abs', 0.0)
        if not isinstance(artifact, dict):
            return 0.0
        count = 0
        for alloy, gold_val in gold.items():
            val = artifact.get(alloy)
            if isinstance(val, (int, float)) and abs(val - gold_val) <= tol_abs:
                count += 1
        return count / len(gold) if gold else 0.0


# === block: score_1 (check id='s02') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        threshold = step['threshold_freq']
        count = 0
        for alloy in ['VTiRhAl', 'VTiRhGa', 'VTiRhIn']:
            entry = artifact.get(alloy, {})
            if entry.get('dynamical_stable', False) and entry.get('max_neg_freq', -100) > threshold:
                count += 1
        return count / 3.0


# === block: score_2 (check id='s03') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold = step['gold_derived']
        tol_rel = step['tolerance_rel']
        tol_v = step['tolerance_abs_v']
        tol_A = step['tolerance_abs_A']
        tol_B_G = step['tolerance_abs_B_G']
        tol_Cp = step['tolerance_abs_Cp']
        tol_Tmelt = step['tolerance_abs_Tmelt']
        alloys = ['VTiRhAl', 'VTiRhGa', 'VTiRhIn']
        total_checks = 0
        passed = 0
        for alloy in alloys:
            if alloy not in artifact:
                continue
            c11 = artifact[alloy].get('C11')
            c12 = artifact[alloy].get('C12')
            c44 = artifact[alloy].get('C44')
            if None in (c11, c12, c44):
                continue
            # check stability criteria
            stable = (c44 > 0) and ((c11 - c12)/2 > 0) and ((c11 + 2*c12)/3 > 0)
            total_checks += 1
            if stable:
                passed += 1
            # derive moduli
            B = (c11 + 2*c12) / 3.0
            G_v = (c11 - c12 + 3*c44) / 5.0
            denom_gr = 4*c44 + 3*(c11 - c12)
            G_r = (5*c44*(c11 - c12)) / denom_gr if denom_gr != 0 else 0
            G = (G_v + G_r) / 2.0
            denom_e = 3*B + G
            E = 9*G*B / denom_e if denom_e != 0 else 0
            denom_v = 2*(3*B + G)
            v = (3*B - 2*G) / denom_v if denom_v != 0 else 0
            denom_a = c11 - c12
            A = (2*c44) / denom_a if denom_a != 0 else 0
            Cp = c12 - c44
            B_G = B / G if G != 0 else 0
            Tmelt = 553 + 5.91 * c11
            derived = {'B': B, 'G': G, 'E': E, 'v': v, 'A': A, 'Cp': Cp, 'B_G': B_G, 'Tmelt': Tmelt}
            g = gold[alloy]
            for key in ['B', 'G', 'E']:
                total_checks += 1
                ref = g[key]
                val = derived[key]
                if abs(val - ref) <= ref * tol_rel:
                    passed += 1
            total_checks += 1
            if abs(derived['v'] - g['v']) <= tol_v:
                passed += 1
            total_checks += 1
            if abs(derived['A'] - g['A']) <= tol_A:
                passed += 1
            total_checks += 1
            if abs(derived['Cp'] - g['Cp']) <= tol_Cp:
                passed += 1
            total_checks += 1
            if abs(derived['B_G'] - g['B_G']) <= tol_B_G:
                passed += 1
            total_checks += 1
            if abs(derived['Tmelt'] - g['Tmelt']) <= tol_Tmelt:
                passed += 1
        return passed / total_checks if total_checks > 0 else 0.0


# === block: score_3 (check id='s04') ===
def score_3(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold = step['gold']
        tol_bg = step['tolerance_bandgap']
        tol_spin = step['tolerance_spin']
        alloys = ['VTiRhAl', 'VTiRhGa', 'VTiRhIn']
        total_checks = 0
        passed = 0
        for alloy in alloys:
            if alloy not in artifact:
                continue
            d = artifact[alloy]
            g = gold[alloy]
            for key in ['bandgap_majority', 'bandgap_minority']:
                total_checks += 1
                if key in d:
                    if isinstance(g[key], (int, float)) and abs(d[key] - g[key]) <= tol_bg:
                        passed += 1
            total_checks += 1
            if 'spin_polarization' in d and abs(d['spin_polarization'] - g['spin_polarization']) <= tol_spin:
                passed += 1
        return passed / total_checks if total_checks > 0 else 0.0


# === block: score_4 (check id='s05') ===
def score_4(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold = step['gold']
        tol_total = step['tolerance_total']
        tol_atom = step['tolerance_atom']
        alloys = ['VTiRhAl', 'VTiRhGa', 'VTiRhIn']
        total_checks = 0
        passed = 0
        for alloy in alloys:
            if alloy not in artifact:
                continue
            d = artifact[alloy]
            g = gold[alloy]
            total_checks += 1
            if 'total' in d and abs(d['total'] - g['total']) <= tol_total:
                passed += 1
            for atom in ['V', 'Ti', 'Rh', 'Z']:
                total_checks += 1
                if atom in d and abs(d[atom] - g[atom]) <= tol_atom:
                    passed += 1
        return passed / total_checks if total_checks > 0 else 0.0


# === block: score_5 (check id='s06') ===
def score_5(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold = step['gold']
        tol_ZT = step['tolerance_ZT']
        al_T300 = artifact.get('VTiRhAl', {}).get('T300', {})
        al_T800 = artifact.get('VTiRhAl', {}).get('T800', {})
        ga_T300 = artifact.get('VTiRhGa', {}).get('T300', {})
        ga_T800 = artifact.get('VTiRhGa', {}).get('T800', {})
        in_T300 = artifact.get('VTiRhIn', {}).get('T300', {})
        in_T800 = artifact.get('VTiRhIn', {}).get('T800', {})
        score = 0.0
        if al_T300:
            max_Al_T300 = max(al_T300.get('ZT_p', 0), al_T300.get('ZT_n', 0))
            if abs(max_Al_T300 - gold['Al_T300_max']) <= tol_ZT:
                score += 0.12
            if al_T300.get('ZT_p', 0) > al_T300.get('ZT_n', 0):
                score += 0.04
        if ga_T300:
            max_Ga_T300 = max(ga_T300.get('ZT_p', 0), ga_T300.get('ZT_n', 0))
            if abs(max_Ga_T300 - gold['Ga_T300_max']) <= tol_ZT:
                score += 0.12
            if ga_T300.get('ZT_p', 0) > ga_T300.get('ZT_n', 0):
                score += 0.04
        if in_T300:
            if abs(in_T300.get('ZT_p', 0) - gold['In_T300_p']) <= tol_ZT:
                score += 0.06
            if abs(in_T300.get('ZT_n', 0) - gold['In_T300_n']) <= tol_ZT:
                score += 0.06
        if al_T800:
            if abs(al_T800.get('ZT_p', 0) - gold['Al_T800_p']) <= tol_ZT:
                score += 0.08
            if abs(al_T800.get('ZT_n', 0) - gold['Al_T800_n']) <= tol_ZT:
                score += 0.08
        max_Al_T800 = max(al_T800.get('ZT_p', 0), al_T800.get('ZT_n', 0)) if al_T800 else 0
        max_Ga_T800 = max(ga_T800.get('ZT_p', 0), ga_T800.get('ZT_n', 0)) if ga_T800 else 0
        max_In_T800 = max(in_T800.get('ZT_p', 0), in_T800.get('ZT_n', 0)) if in_T800 else 0
        if max_Al_T800 > 0 and max_Ga_T800 > 0 and max_In_T800 > 0:
            if max_Al_T800 > max_Ga_T800 and max_Ga_T800 > max_In_T800:
                score += 0.1
        pairs = [('VTiRhAl', al_T300, al_T800), ('VTiRhGa', ga_T300, ga_T800), ('VTiRhIn', in_T300, in_T800)]
        for name, d300, d800 in pairs:
            if d300 and d800:
                max300 = max(d300.get('ZT_p', 0), d300.get('ZT_n', 0))
                max800 = max(d800.get('ZT_p', 0), d800.get('ZT_n', 0))
                if max300 > 0 and max800 > 0 and max800 < max300:
                    score += 0.04
        for d in [al_T300, al_T800, ga_T300, ga_T800, in_T300, in_T800]:
            if d:
                ztp = d.get('ZT_p', -1)
                ztn = d.get('ZT_n', -1)
                if 0 <= ztp <= 2 and 0 <= ztn <= 2:
                    score += 0.02
        return min(1.0, score)


_SCORERS = {
    's01': score_0,
    's02': score_1,
    's03': score_2,
    's04': score_3,
    's05': score_4,
    's06': score_5,
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
