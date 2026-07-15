import os
import json
import csv

# === author imports / helpers ===
import os


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
    ctx = {}
    path = os.path.join(outputs_dir, "elastic_constants.csv")
    if os.path.exists(path):
        import csv
        with open(path, newline="") as f:
            reader = csv.DictReader(f)
            ctx["elastic_constants_raw"] = list(reader)
    else:
        ctx["elastic_constants_raw"] = None
    return ctx


# === block: score_0 (check id='elastic_constants') ===
def score_0(artifact, step, ctx):
    # Gold polycrystalline moduli from paper Table 1
    # For x = 0.6
    B_ref_06 = 167.4
    G_ref_06 = 100.6
    # For x = 1.0
    B_ref_10 = 157.7
    G_ref_10 = 97.8

    def _compute_moduli(C11, C12, C44):
        B = (C11 + 2.0 * C12) / 3.0
        G_V = (C11 - C12 + 3.0 * C44) / 5.0
        G_R = (5.0 * (C11 - C12) * C44) / (4.0 * C44 + 3.0 * (C11 - C12))
        G = (G_V + G_R) / 2.0
        return B, G

    if not isinstance(artifact, list) or len(artifact) < 2:
        return 0.0

    # parse rows by composition
    rows = {}
    for row in artifact:
        try:
            comp = float(row.get("composition", ""))
        except (ValueError, TypeError):
            continue
        try:
            C11 = float(row["C11"])
            C12 = float(row["C12"])
            C44 = float(row["C44"])
        except (KeyError, ValueError, TypeError):
            continue
        rows[comp] = {"C11": C11, "C12": C12, "C44": C44}

    def find_row(target):
        for c, val in rows.items():
            if abs(c - target) < 0.01:
                return val
        return None

    row06 = find_row(0.6)
    row10 = find_row(1.0)
    if row06 is None or row10 is None:
        return 0.0

    B06, G06 = _compute_moduli(row06["C11"], row06["C12"], row06["C44"])
    B10, G10 = _compute_moduli(row10["C11"], row10["C12"], row10["C44"])

    tol_rel = 0.03

    scores = []

    # Check B and G for x=0.6 and x=1.0
    for computed, ref in [(B06, B_ref_06), (G06, G_ref_06),
                          (B10, B_ref_10), (G10, G_ref_10)]:
        err_ratio = abs(computed - ref) / (abs(ref) + 1e-12)
        if err_ratio <= tol_rel:
            s = 1.0
        else:
            s = max(0.0, 1.0 - (err_ratio - tol_rel) / tol_rel)
        scores.append(s)

    # Structural trend checks
    # C11 decreases with Al: C11(0.6) > C11(1.0)
    scores.append(1.0 if row06["C11"] > row10["C11"] else 0.0)
    # C12 decreases: C12(0.6) > C12(1.0)
    scores.append(1.0 if row06["C12"] > row10["C12"] else 0.0)
    # C44 increases weakly: C44(0.6) < C44(1.0)
    scores.append(1.0 if row06["C44"] < row10["C44"] else 0.0)

    return sum(scores) / len(scores)


# === block: score_1 (check id='polycrystalline_moduli') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) < 1:
        return 0.0
    row = artifact[0]
    gold_mod = step.get("gold", {})
    tol = step.get("tolerances", {})
    paper_scores = []
    for key, gold_val in gold_mod.items():
        raw = row.get(key, "")
        if raw == "":
            continue
        try:
            val = float(raw)
        except ValueError:
            continue
        # tolerance can be relative or absolute
        tol_val = tol.get(key, 0.03)
        # for v and epsilon_max use absolute tolerance, others relative
        if key in ("v",):
            err = abs(val - gold_val)
            if err <= tol_val:
                score_i = 1.0
            else:
                # linear decay to zero at 2*tol
                score_i = max(0.0, 1.0 - (err - tol_val) / tol_val)
        else:
            denom = abs(gold_val) + 1e-12
            err_ratio = abs(val - gold_val) / denom
            if err_ratio <= tol_val:
                score_i = 1.0
            else:
                score_i = max(0.0, 1.0 - (err_ratio - tol_val) / tol_val)
        paper_scores.append(score_i)
    if not paper_scores:
        paper_avg = 0.0
    else:
        paper_avg = sum(paper_scores) / len(paper_scores)

    # consistency: recompute B and G from agent's elastic constants (x=1.0)
    elastic_raw = ctx.get("elastic_constants_raw")
    if not elastic_raw:
        return paper_avg * 0.0  # block if missing
    # find row for composition 1.0
    C11 = C12 = C44 = None
    for erow in elastic_raw:
        try:
            comp = float(erow.get("composition", ""))
        except (ValueError, TypeError):
            continue
        if abs(comp - 1.0) < 0.01:
            try:
                C11 = float(erow["C11"])
                C12 = float(erow["C12"])
                C44 = float(erow["C44"])
            except (ValueError, KeyError):
                pass
            break
    if C11 is None:
        consistency_score = 0.0
    else:
        derived_B = (C11 + 2 * C12) / 3.0
        G_V = (C11 - C12 + 3 * C44) / 5.0
        G_R = (5 * (C11 - C12) * C44) / (4 * C44 + 3 * (C11 - C12))
        derived_G = (G_V + G_R) / 2.0
        try:
            agent_B = float(row.get("B", 0))
            agent_G = float(row.get("G", 0))
        except (ValueError, TypeError):
            consistency_score = 0.0
        else:
            if (abs(agent_B - derived_B) <= 0.01 * abs(derived_B) and
                    abs(agent_G - derived_G) <= 0.01 * abs(derived_G)):
                consistency_score = 1.0
            else:
                consistency_score = 0.0
    return paper_avg * consistency_score


# === block: score_2 (check id='debye_temperature') ===
def score_2(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) < 1:
        return 0.0
    row = artifact[0]
    gold = step.get("gold", {})
    tol = step.get("tolerances", {})
    scores = []
    for key, gold_val in gold.items():
        raw = row.get(key, "")
        if raw == "":
            continue
        try:
            val = float(raw)
        except ValueError:
            continue
        tol_val = float(tol.get(key, 0.03))
        denom = abs(gold_val) + 1e-12
        err_ratio = abs(val - gold_val) / denom
        if err_ratio <= tol_val:
            score_i = 1.0
        else:
            score_i = max(0.0, 1.0 - (err_ratio - tol_val) / tol_val)
        scores.append(score_i)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_3 (check id='ideal_tensile_strength') ===
def score_3(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) < 1:
        return 0.0
    row = artifact[0]
    gold = step.get("gold", {})
    tol = step.get("tolerances", {})
    scores = []
    for key in ["sigma_max", "epsilon_max"]:
        gold_val = gold.get(key)
        if gold_val is None:
            continue
        raw = row.get(key, "")
        if raw == "":
            continue
        try:
            val = float(raw)
        except ValueError:
            continue
        tol_val = float(tol.get(key, 0.05))
        if key == "epsilon_max":  # absolute tolerance
            err = abs(val - gold_val)
            if err <= tol_val:
                score_i = 1.0
            else:
                score_i = max(0.0, 1.0 - (err - tol_val) / tol_val)
        else:
            denom = abs(gold_val) + 1e-12
            err_ratio = abs(val - gold_val) / denom
            if err_ratio <= tol_val:
                score_i = 1.0
            else:
                score_i = max(0.0, 1.0 - (err_ratio - tol_val) / tol_val)
        scores.append(score_i)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_4 (check id='curie_temperature') ===
def score_4(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) < 1:
        return 0.0
    row = artifact[0]
    gold_val = step.get("gold", {}).get("T_C")
    if gold_val is None:
        return 0.0
    raw = row.get("T_C", "")
    if raw == "":
        return 0.0
    try:
        val = float(raw)
    except ValueError:
        return 0.0
    tol_rel = float(step.get("tolerances", {}).get("T_C", 0.10))
    err_ratio = abs(val - gold_val) / (abs(gold_val) + 1e-12)
    if err_ratio <= tol_rel:
        score_i = 1.0
    else:
        score_i = max(0.0, 1.0 - (err_ratio - tol_rel) / tol_rel)
    return score_i


_SCORERS = {
    'elastic_constants': score_0,
    'polycrystalline_moduli': score_1,
    'debye_temperature': score_2,
    'ideal_tensile_strength': score_3,
    'curie_temperature': score_4,
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
