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


# === block: score_0 (check id='band_structure') ===
def score_0(artifact, step, ctx):
    import json, math
    artifact = artifact
    gold = step.get('gold', {})
    tols = step.get('tolerances', {})
    def numeric_score(v, g, tol):
        if not isinstance(v, (int, float)) or not isinstance(g, (int, float)):
            return 0.0
        err = abs(v - g)
        if err <= tol:
            return 1.0
        return max(0.0, 1.0 - (err - tol) / tol)
    score = 0.0
    compounds = 0
    for comp, gdata in gold.items():
        if not isinstance(artifact, list):
            break
        entries = [e for e in artifact if isinstance(e, dict) and e.get('compound') == comp]
        if not entries:
            comp_score = 0.0
        else:
            entry = entries[0]
            subs = []
            for k in ['Evi','Eci','delta_Ei','total_Eg']:
                subs.append(numeric_score(entry.get(k), gdata.get(k), tols.get(k, 0.2)))
            gap = entry.get('gap_type', '').strip().lower()
            exp_gap = gdata.get('gap_type', '').strip().lower()
            subs.append(1.0 if gap == exp_gap else 0.0)
            comp_score = sum(subs) / len(subs)
        score += comp_score
        compounds += 1
    if compounds:
        score /= compounds
    return score


# === block: score_1 (check id='effective_masses') ===
def score_1(artifact, step, ctx):
    import json, math
    artifact = artifact
    gold = step.get('gold', {})
    rel_tol = step.get('relative_tolerance', 0.2)
    score = 0.0
    compounds = 0
    for comp, gdata in gold.items():
        if not isinstance(artifact, list):
            break
        entries = [e for e in artifact if isinstance(e, dict) and e.get('compound') == comp]
        if not entries:
            comp_score = 0.0
        else:
            entry = entries[0]
            if entry.get('plane_direction', '').strip().lower() != gdata.get('plane_direction', '').strip().lower():
                comp_score = 0.0
            else:
                subs = []
                for k in ['light_hole_effective_mass', 'heavy_hole_effective_mass', 'electron_effective_mass']:
                    gv = gdata.get(k)
                    av = entry.get(k)
                    if not isinstance(av, (int, float)) or not isinstance(gv, (int, float)):
                        subs.append(0.0)
                    else:
                        denom = abs(gv) + 1e-12
                        rel_err = abs(av - gv) / denom
                        if rel_err <= rel_tol:
                            subs.append(1.0)
                        else:
                            subs.append(max(0.0, 1.0 - (rel_err - rel_tol) / rel_tol))
                comp_score = sum(subs) / len(subs)
        score += comp_score
        compounds += 1
    if compounds:
        score /= compounds
    return score


# === block: score_2 (check id='dos_data') ===
def score_2(artifact, step, ctx):
    import json, math
    artifact = artifact
    expected = step.get('expected', {})
    window_tol = step.get('window_tolerance', 0.15)
    score = 0.0
    compounds = 0
    for comp, edata in expected.items():
        if not isinstance(artifact, list):
            break
        entries = [e for e in artifact if isinstance(e, dict) and e.get('compound') == comp]
        if not entries:
            comp_score = 0.0
        else:
            entry = entries[0]
            win = entry.get('ib_energy_window')
            exp_win = edata.get('ib_window')
            win_score = 0.0
            if isinstance(win, list) and len(win) >= 2 and isinstance(exp_win, list) and len(exp_win) >= 2:
                if abs(win[0] - exp_win[0]) <= window_tol and abs(win[1] - exp_win[1]) <= window_tol:
                    win_score = 1.0
            agent_orbs = set([o.strip().lower() for o in (entry.get('dominant_orbitals', []) if isinstance(entry.get('dominant_orbitals'), list) else [])])
            exp_orbs = set([o.strip().lower() for o in (edata.get('dominant_orbitals', []) if isinstance(edata.get('dominant_orbitals'), list) else [])])
            orb_score = 1.0 if exp_orbs.issubset(agent_orbs) else 0.0
            comp_score = (win_score + orb_score) / 2.0
        score += comp_score
        compounds += 1
    if compounds:
        score /= compounds
    return score


_SCORERS = {
    'band_structure': score_0,
    'effective_masses': score_1,
    'dos_data': score_2,
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
