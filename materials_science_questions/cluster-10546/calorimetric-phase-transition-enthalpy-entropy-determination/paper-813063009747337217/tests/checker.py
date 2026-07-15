import os
import json
import csv

# === author imports / helpers ===
import csv, math, os


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
        return {"outputs_dir": outputs_dir, "spec": spec}


# === block: score_0 (check id='step01_compute_gibbs') ===
def score_0(artifact, step, ctx):
        # Recompute expected ΔG for each target temperature and compare against agent CSV.
        step_params = ctx["spec"]["steps"]
        # Find our step by id
        own_step = None
        for s in step_params:
            if s.get("id") == "step01_compute_gibbs":
                own_step = s
                break
        if own_step is None:
            return 0.0
        target_temps = own_step.get("target_temps", [])
        tolerance_abs = own_step.get("tolerance_abs", 0.5)
        if not target_temps or not isinstance(artifact, list) or len(artifact) == 0:
            return 0.0
        R = 8.314e-3  # kJ/(mol·K)
        deltaCp = 1.5 * R
        phases = {
            "dimer": {"Q": 10.5, "Teq": 280.0, "col": "G_dimer"},
            "fccl":  {"Q":  4.8, "Teq": 290.0, "col": "G_fccl"},
            "polymer":{"Q": 25.8, "Teq": 370.0, "col": "G_polymer"}
        }
        # Build list of (T, row_dict)
        rows = []
        for r in artifact:
            try:
                t = float(r.get("T", None))
            except (TypeError, ValueError):
                continue
            rows.append((t, r))
        if not rows:
            return 0.0
        rows.sort(key=lambda x: x[0])  # sort by T
        total_points = len(target_temps) * len(phases)
        within_tol_count = 0
        for t_target in target_temps:
            # Find nearest row
            best_idx = min(range(len(rows)), key=lambda i: abs(rows[i][0] - t_target))
            _, row = rows[best_idx]
            for phase_name, p in phases.items():
                Q = p["Q"]
                Teq = p["Teq"]
                col = p["col"]
                # Compute expected ΔG
                if t_target == 0.0:
                    continue
                dH = Q - deltaCp * (Teq - t_target)
                dS = (Q / Teq) - deltaCp * math.log(Teq / t_target) if t_target > 0 else 0.0
                expected = dH - t_target * dS
                try:
                    agent_val = float(row.get(col, None))
                except (TypeError, ValueError):
                    continue
                if abs(agent_val - expected) <= tolerance_abs:
                    within_tol_count += 1
        if total_points == 0:
            return 0.0
        return within_tol_count / total_points


# === block: score_1 (check id='step02_stability_summary') ===
def score_1(artifact, step, ctx):
        step_params = ctx["spec"]["steps"]
        own_step = None
        for s in step_params:
            if s.get("id") == "step02_stability_summary":
                own_step = s
                break
        if own_step is None:
            return 0.0
        required_phrases = own_step.get("required_phrases", [])
        csv_check_temps = own_step.get("csv_check_temps", {})
        # 1) Check textual phrases (case-insensitive)
        text = (artifact or "").lower()
        phrase_score = 0.0
        if required_phrases:
            matched = 0
            for phrase in required_phrases:
                if phrase.lower() in text:
                    matched += 1
            phrase_score = matched / len(required_phrases)
        # 2) Cross-check CSV ordering
        csv_path = os.path.join(ctx["outputs_dir"], "gibbs_free_energies.csv")
        csv_score = 0.0
        try:
            with open(csv_path, newline='') as f:
                reader = csv.DictReader(f)
                rows = []
                for r in reader:
                    try:
                        t = float(r["T"])
                    except (KeyError, ValueError):
                        continue
                    rows.append((t, r))
            if rows:
                rows.sort(key=lambda x: x[0])
                low_temp = csv_check_temps.get("low", 250)
                high_temp = csv_check_temps.get("high", 450)
                # nearest rows for low and high
                low_idx = min(range(len(rows)), key=lambda i: abs(rows[i][0] - low_temp))
                high_idx = min(range(len(rows)), key=lambda i: abs(rows[i][0] - high_temp))
                _, low_row = rows[low_idx]
                _, high_row = rows[high_idx]
                try:
                    G_fccl_low = float(low_row["G_fccl"])
                    G_dimer_low = float(low_row["G_dimer"])
                    G_polymer_low = float(low_row["G_polymer"])
                    G_fccl_high = float(high_row["G_fccl"])
                    G_dimer_high = float(high_row["G_dimer"])
                    G_polymer_high = float(high_row["G_polymer"])
                    # Low T: polymer most stable (lowest G)
                    low_order_ok = (G_polymer_low <= G_dimer_low) and (G_polymer_low <= G_fccl_low)
                    # High T: all G should be >= 0 (fcc is reference)
                    high_all_positive = (G_fccl_high >= -0.1) and (G_dimer_high >= -0.1) and (G_polymer_high >= -0.1)
                    if low_order_ok and high_all_positive:
                        csv_score = 1.0
                    elif low_order_ok or high_all_positive:
                        csv_score = 0.5
                except (KeyError, ValueError):
                    csv_score = 0.0
        except Exception:
            csv_score = 0.0
        return 0.5 * phrase_score + 0.5 * csv_score


_SCORERS = {
    'step01_compute_gibbs': score_0,
    'step02_stability_summary': score_1,
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
