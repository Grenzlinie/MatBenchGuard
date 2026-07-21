import os
import json
import csv

# === author imports / helpers ===
import json, csv, sqlite3, random, math, os


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
    def prepare(output_dir, spec):
        ctx = {}
        th_path = os.path.join(output_dir, "threshold_energies.json")
        if os.path.exists(th_path):
            with open(th_path) as f:
                ctx["threshold"] = json.load(f)
        dc_path = os.path.join(output_dir, "defect_counts.csv")
        if os.path.exists(dc_path):
            with open(dc_path, newline='') as f:
                reader = csv.DictReader(f)
                ctx["defect_counts"] = [dict(row) for row in reader]
        return ctx


# === block: score_0 (check id='step_02') ===
def score_0(artifact, step, ctx):
    def score_step_02(artifact, step, ctx):
        try:
            data = artifact
            if data is None or not isinstance(data, dict):
                return 0.0
            fields = step.get("fields", {})
            if not isinstance(fields, dict):
                return 0.0
            scores = []
            for key, info in fields.items():
                if not isinstance(info, dict):
                    scores.append(0.0)
                    continue
                try:
                    target = float(info.get("target", 0))
                except (TypeError, ValueError):
                    target = 0.0
                try:
                    tol = float(info.get("tolerance", 1))
                except (TypeError, ValueError):
                    tol = 1.0
                val = data.get(key)
                if val is None:
                    scores.append(0.0)
                    continue
                try:
                    val = float(val)
                except (TypeError, ValueError):
                    scores.append(0.0)
                    continue
                diff = abs(val - target)
                score = 1.0 if diff <= tol else 0.0
                scores.append(score)
            if not scores:
                return 0.0
            return sum(scores) / len(scores)
        except Exception:
            return 0.0


# === block: score_1 (check id='step_04') ===
def score_1(artifact, step, ctx):
    def score_step_04(artifact, step, ctx):
        rows = artifact
        gold_rows = step["gold_rows"]
        defect_cols = step["defect_columns"]
        mult = step.get("tolerance_multiplier", 2.0)
        gold_lookup = {}
        for g in gold_rows:
            key = (g["recoil_type"].strip(), str(g["energy_eV"]))
            gold_lookup[key] = g
        total_cells = 0
        cell_scores = 0.0
        for row in rows:
            rtype = row.get("recoil_type", "").strip()
            energy = row.get("energy_eV", "").strip()
            key = (rtype, energy)
            gold = gold_lookup.get(key)
            if gold is None:
                total_cells += len(defect_cols)
                continue
            for col in defect_cols:
                total_cells += 1
                try:
                    agent_val = float(row.get(col, 0))
                except:
                    agent_val = 0.0
                gold_mean_se = gold.get(col)
                if gold_mean_se is None or len(gold_mean_se) != 2:
                    continue
                mean = gold_mean_se[0]
                se = gold_mean_se[1]
                tol = mult * se
                if tol == 0:
                    tol = max(0.01 * abs(mean), 1e-6)
                diff = abs(agent_val - mean)
                if diff <= tol:
                    cell_scores += 1.0
                else:
                    decay = (diff - tol) / (5 * tol + 1e-12)
                    cell_scores += max(0.0, 1.0 - decay)
        if total_cells == 0:
            return 0.0
        return cell_scores / total_cells


# === block: score_2 (check id='step_05') ===
def score_2(artifact, step, ctx):
    def score_step_05(artifact, step, ctx):
        kp_rows = artifact
        threshold_data = ctx.get("threshold")
        defect_data = ctx.get("defect_counts")
        if not threshold_data or not defect_data or not kp_rows:
            return 0.0
        ed = {"Ga": threshold_data.get("Ga_average", None), "N": threshold_data.get("N_average", None)}
        if None in ed.values():
            return 0.0
        defect_sum_lookup = {}
        for row in defect_data:
            rtype = row.get("recoil_type", "").strip()
            energy = row.get("energy_eV", "").strip()
            try:
                vn = float(row.get("V_N", 0))
                vga = float(row.get("V_Ga", 0))
            except:
                continue
            defect_sum_lookup[(rtype, energy)] = vn + vga
        kp_scores = []
        cons_scores = []
        for row in kp_rows:
            rtype = row.get("recoil_type", "").strip()
            energy_str = row.get("energy_eV", "").strip()
            energy = float(energy_str) if energy_str else 0.0
            ed_val = ed.get(rtype)
            if ed_val is None or ed_val == 0:
                kp_scores.append(0.0)
            else:
                expected = energy / (2 * ed_val)
                agent_kp = float(row.get("kp_predicted_vacancies", 0))
                diff_frac = abs(agent_kp - expected) / (expected + 1e-12)
                if diff_frac <= 0.01:
                    kp_scores.append(1.0)
                else:
                    kp_scores.append(max(0.0, 1.0 - diff_frac * 10))
            agent_total = float(row.get("total_vacancies", 0))
            key = (rtype, energy_str)
            expected_total = defect_sum_lookup.get(key, None)
            if expected_total is None:
                cons_scores.append(0.0)
            else:
                diff = abs(agent_total - expected_total)
                if diff <= max(0.01 * expected_total, 0.01):
                    cons_scores.append(1.0)
                else:
                    cons_scores.append(0.0)
        if not kp_scores:
            return 0.0
        kp_avg = sum(kp_scores) / len(kp_scores)
        cons_avg = sum(cons_scores) / len(cons_scores) if cons_scores else 0.0
        return 0.5 * kp_avg + 0.5 * cons_avg


_SCORERS = {
    'step_02': score_0,
    'step_04': score_1,
    'step_05': score_2,
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
