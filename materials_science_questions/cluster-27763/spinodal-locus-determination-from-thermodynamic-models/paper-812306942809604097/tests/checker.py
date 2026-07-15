import os
import json
import csv

# === author imports / helpers ===
import math
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


# === block: score_0 (check id='tetragonal') ===
def score_0(artifact, step, ctx):
        data = artifact.get("tetragonal")
        if not isinstance(data, dict):
            return 0.0
        g2 = 0.3
        f = 0.05
        p = 2.0

        # Asymptotic free energy F^(1) (Eq.6)
        A = 1 + g2 * (2 - 179/280 * f)
        term1 = A * p**2
        cubic = g2 * (6/5 - 4/35 * f) * abs(p)**3
        quartic = g2 * (9/20 + 13/140 * f) * p**4
        F_gold = (1.0 / g2) * (term1 - cubic + quartic)

        # Binodal and spinodal jumps (Eqs.8,10)
        denom = 6/5 - 4/35 * f
        bracket = 1/g2 + (2 - 179/280 * f)
        p_b_gold = 2.0 / denom * bracket
        p_s_gold = (4.0/3.0) * (1.0/denom) * bracket

        # Binodal/spinodal equations – evaluate the RHS; boolean true if finite, negative
        bin_rhs = -g2**2 * (9/10 + 13/70*f) * (1 - 4*g2*(9/5 - 2/7*f) / (9 + 13/7*f))
        spino_rhs = -g2**2 * (9/10 + 13/70*f) * (1 - (9/2)*g2*(9/5 - 2/7*f) / (9 + 13/7*f))
        bin_expected = math.isfinite(bin_rhs) and bin_rhs < 0
        spino_expected = math.isfinite(spino_rhs) and spino_rhs < 0

        fields = [
            ("g2", g2, 1e-9),
            ("f", f, 1e-9),
            ("p", p, 1e-9),
            ("F_asymptotic", F_gold, 1e-6),
            ("p_b", p_b_gold, 1e-6),
            ("p_s", p_s_gold, 1e-6),
            ("binodal_check", bin_expected, 0),
            ("spinodal_check", spino_expected, 0),
        ]
        score = 0.0
        count = 0
        for field_name, expected, tol in fields:
            if field_name not in data:
                continue
            val = data[field_name]
            if isinstance(expected, bool):
                s = 1.0 if val == expected else 0.0
            else:
                s = 1.0 if abs(val - expected) <= tol else 0.0
            score += s
            count += 1
        return score / count if count > 0 else 0.0


# === block: score_1 (check id='rhombohedral') ===
def score_1(artifact, step, ctx):
        data = artifact.get("rhombohedral")
        if not isinstance(data, dict):
            return 0.0
        g1 = 0.2
        f = 0.05
        p = 2.0

        # Asymptotic free energy F^(2) (Eq.13) – note the z=-2 term vanishes
        A = 1 + g1 * (2 + 2/5 * f)
        term1 = A * p**2
        cubic = g1 * (6/5 + 229/630 * f) * abs(p)**3
        quartic = g1 * (9/20 + 8/63 * f) * p**4
        F_gold = (1.0 / g1) * (term1 - cubic + quartic)

        # Jumps (Eqs.16,17)
        denom = 6/5 + 229/630 * f
        bracket = 1/g1 + (2 + 2/5 * f)
        p_b_gold = 2.0 / denom * bracket
        p_s_gold = (4.0/3.0) * (1.0/denom) * bracket

        # Binodal and spinodal equations (14),(15) for g2
        bin_rhs = -g1/2 - g1**2 * (27/20 + 8/21*f) * (1 - g1*(36/25 + 229/315*f) / (9/5 + 32/63*f))
        spino_rhs = -g1/2 - g1**2 * (27/20 + 8/21*f) * (1 - (9/32)*g1*(36/25 + 229/315*f) / (9/20 + 8/63*f))
        bin_expected = math.isfinite(bin_rhs) and bin_rhs < 0
        spino_expected = math.isfinite(spino_rhs) and spino_rhs < 0

        fields = [
            ("g1", g1, 1e-9),
            ("f", f, 1e-9),
            ("p", p, 1e-9),
            ("F_asymptotic", F_gold, 1e-6),
            ("p_b", p_b_gold, 1e-6),
            ("p_s", p_s_gold, 1e-6),
            ("binodal_check", bin_expected, 0),
            ("spinodal_check", spino_expected, 0),
        ]
        score = 0.0
        count = 0
        for field_name, expected, tol in fields:
            if field_name not in data:
                continue
            val = data[field_name]
            if isinstance(expected, bool):
                s = 1.0 if val == expected else 0.0
            else:
                s = 1.0 if abs(val - expected) <= tol else 0.0
            score += s
            count += 1
        return score / count if count > 0 else 0.0


_SCORERS = {
    'tetragonal': score_0,
    'rhombohedral': score_1,
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
