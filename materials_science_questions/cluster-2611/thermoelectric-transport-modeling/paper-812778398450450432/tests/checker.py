import os
import json
import csv

# === author imports / helpers ===
import json, csv, math


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
    steps = spec.get("steps", [])
    for step in steps:
        sid = step.get("id", "")
        if sid == "pf_values":
            gold = step.get("gold", [])
            ctx["pf_gold"] = {(r["compound"], r["temperature"]): r["pf"] for r in gold}
            ctx["pf_tol_rel"] = step.get("pf_tol_rel", 0.10)
        elif sid == "pf_trend":
            ctx["order"] = step.get("order", {})
        elif sid == "pf_consistency":
            ctx["consistency_tol_rel"] = step.get("consistency_tol_rel", 0.10)
        elif sid == "phonon_values":
            ctx["phonon_gold"] = step.get("gold", {})
            ctx["phonon_tol_abs"] = step.get("phonon_tol_abs", 10.0)
    return ctx


# === block: score_0 (check id='shape_transport') ===
def score_0(artifact, step, ctx):
    if not artifact or not isinstance(artifact, list): return 0.0
    if len(artifact) < step.get("min_rows", 9): return 0.0
    for col in step.get("required_columns", []):
        if col not in artifact[0]: return 0.0
    return 1.0


# === block: score_1 (check id='pf_values') ===
def score_1(artifact, step, ctx):
    pf_gold = ctx.get("pf_gold", {})
    if not pf_gold: return 0.0
    tol = ctx.get("pf_tol_rel", 0.10)
    total = 0.0
    count = 0
    for row in artifact:
        compound = row.get("compound", "").strip()
        try:
            temp = int(row.get("temperature", -1))
            pf = float(row.get("PF_max", -1))
        except (ValueError, TypeError):
            continue
        key = (compound, temp)
        if key not in pf_gold:
            continue
        gold_pf = pf_gold[key]
        if gold_pf == 0:
            continue
        rel_err = abs(pf - gold_pf) / abs(gold_pf)
        if rel_err <= tol:
            score = 1.0
        elif rel_err <= 3 * tol:
            score = max(0.0, 1.0 - (rel_err - tol) / (2 * tol))
        else:
            score = 0.0
        total += score
        count += 1
    if count == 0: return 0.0
    return total / count


# === block: score_2 (check id='pf_trend') ===
def score_2(artifact, step, ctx):
    order = ctx.get("order", {})
    if not order: return 0.0
    # Group by temperature
    groups = {}
    for row in artifact:
        try:
            temp = int(row["temperature"])
            compound = row["compound"].strip()
            pf = float(row["PF_max"])
        except (ValueError, KeyError, TypeError):
            continue
        groups.setdefault(temp, []).append((compound, pf))
    score = 0.0
    count = 0
    for temp, rows in groups.items():
        if len(rows) != 3:
            continue
        # compute rank by PF (higher PF gets higher rank)
        ranked = sorted(rows, key=lambda x: x[1], reverse=True)
        correct = True
        for i in range(len(ranked) - 1):
            if order.get(ranked[i][0], 0) <= order.get(ranked[i+1][0], 0):
                correct = False
                break
        score += 1.0 if correct else 0.0
        count += 1
    if count == 0: return 0.0
    return score / count


# === block: score_3 (check id='pf_consistency') ===
def score_3(artifact, step, ctx):
    tol = ctx.get("consistency_tol_rel", 0.10)
    total = 0.0
    count = 0
    for row in artifact:
        try:
            pf = float(row["PF_max"])
            S = float(row["S_max"])
            sigma = float(row["sigma_at_max"])
        except (ValueError, KeyError, TypeError):
            continue
        if S == 0:
            continue
        pf_calc = (S ** 2) * sigma
        if pf == 0:
            continue
        rel_err = abs(pf_calc - pf) / pf
        if rel_err <= tol:
            score = 1.0
        elif rel_err <= 3 * tol:
            score = max(0.0, 1.0 - (rel_err - tol) / (2 * tol))
        else:
            score = 0.0
        total += score
        count += 1
    if count == 0: return 0.0
    return total / count


# === block: score_4 (check id='shape_phonon') ===
def score_4(artifact, step, ctx):
    if not artifact or not isinstance(artifact, dict): return 0.0
    for key in step.get("required_keys", []):
        if key not in artifact: return 0.0
    return 1.0


# === block: score_5 (check id='phonon_values') ===
def score_5(artifact, step, ctx):
    gold = ctx.get("phonon_gold", {})
    if not gold: return 0.0
    tol_abs = ctx.get("phonon_tol_abs", 10.0)
    total = 0.0
    count = 0
    # TO list
    if "TO" in gold and "TO" in artifact:
        gold_to = gold["TO"]
        to_list = artifact["TO"]
        if isinstance(to_list, list) and len(gold_to) == len(to_list):
            for gv, av in zip(gold_to, to_list):
                try:
                    av = float(av)
                except (ValueError, TypeError):
                    continue
                err = abs(av - gv)
                if err <= tol_abs:
                    score = 1.0
                elif err <= 5 * tol_abs:
                    score = max(0.0, 1.0 - (err - tol_abs) / (4 * tol_abs))
                else:
                    score = 0.0
                total += score
                count += 1
    # scalar keys
    for key in ["Raman", "LO"]:
        gval = gold.get(key)
        aval = artifact.get(key)
        if gval is None or aval is None:
            continue
        try:
            aval = float(aval)
        except (ValueError, TypeError):
            continue
        err = abs(aval - gval)
        if err <= tol_abs:
            score = 1.0
        elif err <= 5 * tol_abs:
            score = max(0.0, 1.0 - (err - tol_abs) / (4 * tol_abs))
        else:
            score = 0.0
        total += score
        count += 1
    # LO-TO_split
    if "LO-TO_split" in gold and "LO-TO_split" in artifact:
        gv = gold["LO-TO_split"]
        av = artifact["LO-TO_split"]
        try:
            av = float(av)
        except (ValueError, TypeError):
            av = 0.0
        err = abs(av - gv)
        if err <= tol_abs:
            score = 1.0
        elif err <= 5 * tol_abs:
            score = max(0.0, 1.0 - (err - tol_abs) / (4 * tol_abs))
        else:
            score = 0.0
        total += score
        count += 1
    if count == 0: return 0.0
    return total / count


_SCORERS = {
    'shape_transport': score_0,
    'pf_values': score_1,
    'pf_trend': score_2,
    'pf_consistency': score_3,
    'shape_phonon': score_4,
    'phonon_values': score_5,
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
