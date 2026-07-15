import os
import json
import csv


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


# === block: score_0 (check id='step03_transition_detection') ===
def score_0(artifact, step, ctx):
    import re, json, math

    targets = step.get('targets', {})
    target_strains = targets.get('transition_strains', [2.3, 4.8, 6.0])
    strain_tol = targets.get('strain_tolerance', 0.3)
    target_stress = targets.get('first_transition_stress_GPa', 5.6)
    stress_tol = targets.get('stress_tolerance', 0.5)
    target_burgers_norm = '1/3a[-100]'

    if not isinstance(artifact, dict):
        return 0.0

    def _norm_burgers(s):
        """Normalize a Burgers vector string to canonical '1/3a[-100]' form,
        supporting spaces, case variations, unicode minuses, and alternative
        [1-00] notation."""
        s = str(s).replace(' ', '').lower()
        s = s.replace('\u2212', '-').replace('\u2013', '-').replace('\u2014', '-')
        m = re.match(r'1/3a\[([^\[\]]+)\]', s)
        if m:
            inside = m.group(1)
            parts = inside.split('-')
            if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                s = '1/3a[' + '-' + parts[0] + parts[1] + ']'
        return s

    score_parts = 0.0

    # ---- transition strains (0 to 10% range) ----
    if 'transition_strains' in artifact and isinstance(artifact['transition_strains'], list):
        strains = artifact['transition_strains']
        if len(strains) == 3:
            for i in range(3):
                try:
                    v = float(strains[i])
                    diff = abs(v - target_strains[i])
                    if diff <= strain_tol:
                        score_parts += 0.2
                except (TypeError, ValueError):
                    pass
            # sanity: must be positive and strictly increasing
            try:
                s = [float(x) for x in strains]
                if not (0 < s[0] < s[1] < s[2] < 15.0):
                    # if strains are not monotonic, invalid; do not penalize beyond missed gold
                    pass
            except:
                pass

    # ---- first transition stress (positive) ----
    if 'first_transition_stress_GPa' in artifact:
        try:
            stress = float(artifact['first_transition_stress_GPa'])
            if abs(stress - target_stress) <= stress_tol:
                score_parts += 0.2
            # sanity: stress should be positive
            if stress <= 0:
                # not physically plausible
                pass
        except (TypeError, ValueError):
            pass

    # ---- final stair-rod Burgers vector ----
    if 'final_stair_rod_burgers' in artifact:
        try:
            if _norm_burgers(str(artifact['final_stair_rod_burgers'])) == target_burgers_norm:
                score_parts += 0.2
        except:
            pass

    return min(1.0, score_parts)


_SCORERS = {
    'step03_transition_detection': score_0,
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
