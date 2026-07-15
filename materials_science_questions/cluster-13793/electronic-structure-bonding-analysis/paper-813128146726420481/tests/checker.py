import os
import json
import csv

# === author imports / helpers ===
import re


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
        import os, json
        pure_path = os.path.join(outputs_dir, "pure_bond_orders.json")
        alloy_path = os.path.join(outputs_dir, "alloy_bond_orders.json")
        ctx = {}
        if os.path.exists(pure_path):
            with open(pure_path) as f:
                ctx["pure_artifact"] = json.load(f)
        if os.path.exists(alloy_path):
            with open(alloy_path) as f:
                ctx["alloy_artifact"] = json.load(f)
        return ctx


# === block: score_0 (check id='pure_bond_orders') ===
def score_0(artifact, step, ctx):
        if artifact is None:
            return 0.0
        gold = step["gold"]
        bond_tol = step["bond_tol"]
        ratio_tol = step["ratio_tol"]
        order_weight = step["order_bonus_weight"]
        fields = ["Mn4_H", "M_H", "Zr1_H", "total_M_H", "Mn1_Mn4", "Mn1_M", "M_Mn4", "Zr1_Mn4", "Zr1_M", "ratio"]
        for f in fields:
            if f not in artifact:
                return 0.0
        scores = []
        for f in fields:
            val = artifact[f]
            g = gold[f]
            tol = ratio_tol if f == "ratio" else bond_tol
            if tol <= 0:
                s = 1.0 if abs(val - g) < 1e-9 else 0.0
            else:
                s = max(0.0, 1.0 - abs(val - g) / tol)
            scores.append(s)
        numeric_score = sum(scores) / len(scores)
        order_score = 1.0 if artifact.get("Mn4_H", 0) > artifact.get("Zr1_H", 0) else 0.0
        total = (1 - order_weight) * numeric_score + order_weight * order_score
        return total


# === block: score_1 (check id='alloy_bond_orders') ===
def score_1(artifact, step, ctx):
        if artifact is None:
            return 0.0
        gold = step["gold"]
        bond_tol = step["bond_tol"]
        ratio_tol = step["ratio_tol"]
        pure_total = step["pure_total_M_H"]
        total_frac = step["total_M_H_tol_frac"]
        eps = step["monotonic_epsilon"]
        w_num = step["element_num_weight"]
        w_cons = step["total_conservation_weight"]
        w_mono = step["monotonic_weight"]
        elements = ["V", "Fe", "Co", "Ni"]
        fields = ["Mn4_H", "M_H", "Zr1_H", "total_M_H", "Mn1_Mn4", "Mn1_M", "M_Mn4", "Zr1_Mn4", "Zr1_M", "ratio"]
        for el in elements:
            if el not in artifact:
                return 0.0
            el_data = artifact[el]
            for f in fields:
                if f not in el_data:
                    return 0.0
        elem_scores = []
        cons_scores = []
        for el in elements:
            el_data = artifact[el]
            g = gold[el]
            sc = []
            for f in fields:
                val = el_data[f]
                gval = g[f]
                tol = ratio_tol if f == "ratio" else bond_tol
                if tol <= 0:
                    s = 1.0 if abs(val - gval) < 1e-9 else 0.0
                else:
                    s = max(0.0, 1.0 - abs(val - gval) / tol)
                sc.append(s)
            elem_scores.append(sum(sc) / len(sc))
            total_val = el_data.get("total_M_H", 0)
            if abs(total_val - pure_total) <= total_frac * pure_total:
                cons_scores.append(1.0)
            else:
                cons_scores.append(0.0)
        num_avg = sum(elem_scores) / len(elem_scores)
        cons_avg = sum(cons_scores) / len(cons_scores)
        ratios = [artifact[el]["ratio"] for el in elements]
        monotonic = True
        for i in range(len(ratios)-1):
            if ratios[i] > ratios[i+1] + eps:
                monotonic = False
                break
        mono_score = 1.0 if monotonic else 0.0
        return w_num * num_avg + w_cons * cons_avg + w_mono * mono_score


# === block: score_2 (check id='trend_report') ===
def score_2(artifact, step, ctx):
        if artifact is None:
            return 0.0
        text = artifact if isinstance(artifact, str) else ""
        alloy = ctx.get("alloy_artifact")
        c1 = 1 if ("Mn-H > Zr-H" in text or "Mn-H bond order exceeds Zr-H" in text) else 0
        c2 = 1 if ("within 20%" in text or re.search(r'total.*M[-H].*within\s*20\s*%', text, re.IGNORECASE)) else 0
        c3 = 0
        if alloy is not None:
            ratios_text = {}
            for line in text.split('\n'):
                m = re.match(r'\s*([A-Za-z]+)\s+ratio\s*:\s*([\d.]+)', line)
                if m:
                    ratios_text[m.group(1)] = float(m.group(2))
            keys = ["V", "Fe", "Co", "Ni"]
            if all(k in ratios_text for k in keys):
                ok = True
                for k in keys:
                    if abs(ratios_text[k] - alloy[k]["ratio"]) > 0.02:
                        ok = False
                        break
                if ok:
                    c3 = 1
        c4 = 1 if re.search(r'monotonically\s+increasing|ratio\s+increases?\s+monotonically|monotonic\s+increase', text, re.IGNORECASE) else 0
        return (c1 + c2 + c3 + c4) / 4.0


_SCORERS = {
    'pure_bond_orders': score_0,
    'alloy_bond_orders': score_1,
    'trend_report': score_2,
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
