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


# === block: score_0 (check id='check_polarizability') ===
def score_0(artifact, step, ctx):
        fields = step.get("fields", {})
        if not isinstance(artifact, dict) or not fields:
            return 0.0
        ok = 0
        for name, spec in fields.items():
            if name not in artifact:
                continue
            try:
                val = float(artifact[name])
                gold = float(spec["gold"])
                abs_tol = float(spec.get("abs_tol", 0.0))
                rel_tol = float(spec.get("rel_tol", 0.0))
                diff = abs(val - gold)
                allowed = max(abs_tol, rel_tol * abs(gold))
                if diff <= allowed:
                    ok += 1
            except (ValueError, TypeError):
                pass
        total = len(fields)
        return ok / total if total > 0 else 0.0


# === block: score_1 (check id='check_c3_coefficients') ===
def score_1(artifact, step, ctx):
        materials = step.get("materials", [])
        gold_totals = step.get("gold_totals", {})
        rel_tol = step.get("rel_tol", 0.02)
        comp_tol = step.get("component_sum_tol", 0.001)
        if not isinstance(artifact, list) or not materials:
            return 0.0
        data = {}
        for row in artifact:
            mat = row.get("material", "").strip()
            data[mat] = row
        # ---- total accuracy ----
        ok_total = 0
        n = len(materials)
        for mat in materials:
            if mat not in data or mat not in gold_totals:
                continue
            try:
                val = float(data[mat].get("C3_total", None))
                gold = float(gold_totals[mat])
                if abs(val - gold) <= rel_tol * abs(gold):
                    ok_total += 1
            except (ValueError, TypeError):
                pass
        score_total = ok_total / n if n > 0 else 0.0
        # ---- component sum consistency ----
        ok_consist = 0
        for mat in materials:
            if mat not in data:
                continue
            row = data[mat]
            try:
                comp_sum = (float(row.get("C3_core", 0)) +
                           float(row.get("C3_valence", 0)) +
                           float(row.get("C3_core_valence", 0)) +
                           float(row.get("C3_tail", 0)))
                total = float(row.get("C3_total", 0))
                if abs(comp_sum - total) <= comp_tol:
                    ok_consist += 1
            except (ValueError, TypeError):
                pass
        score_consist = ok_consist / n if n > 0 else 0.0
        # ---- ordering check ----
        try:
            pc = float(data.get("perfect_conductor", {}).get("C3_total", -1e30))
            au = float(data.get("Au", {}).get("C3_total", -1e30))
            si = float(data.get("Si", {}).get("C3_total", -1e30))
            violations = 0
            if not (pc > au + 1e-12):
                violations += 1
            if not (au > si + 1e-12):
                violations += 1
            dielectrics = ["SiO2","SiNx","ordinary_sapphire","extraordinary_sapphire","birefringent_sapphire","YAG"]
            for d in dielectrics:
                if d in data:
                    dv = float(data[d].get("C3_total", 1e30))
                    if not (si > dv + 1e-12):
                        violations += 1
            score_order = 1.0 if violations == 0 else 0.0
        except (ValueError, TypeError):
            score_order = 0.0
        # weighted combination
        w_total = float(step.get("total_weight", 0.7))
        w_consist = float(step.get("consistency_weight", 0.2))
        w_order = float(step.get("ordering_weight", 0.1))
        return score_total * w_total + score_consist * w_consist + score_order * w_order


# === block: score_2 (check id='check_f3_fitting_parameters') ===
def score_2(artifact, step, ctx):
        surfaces = step.get("surfaces", [])
        gold_params = step.get("gold_params", {})
        rel_tol = step.get("rel_tol", 0.05)
        if not isinstance(artifact, list) or not surfaces:
            return 0.0
        data = {}
        for row in artifact:
            s = row.get("surface", "").strip()
            data[s] = row
        ok = 0
        total = 0
        for surf in surfaces:
            if surf not in data or surf not in gold_params:
                continue
            row = data[surf]
            gp = gold_params[surf]
            for param in ("A1","A2","B2","B3"):
                total += 1
                try:
                    val = float(row.get(param, None))
                    gold = float(gp[param])
                    if abs(val - gold) <= rel_tol * abs(gold):
                        ok += 1
                except (ValueError, TypeError):
                    pass
        return ok / total if total > 0 else 0.0


_SCORERS = {
    'check_polarizability': score_0,
    'check_c3_coefficients': score_1,
    'check_f3_fitting_parameters': score_2,
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
