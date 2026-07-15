import os
import json
import csv

# === author imports / helpers ===
import os, json, csv, math


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
        # hidden gold from steps
        steps = spec.get("steps", [])
        ctx = {"step_gold": {}}
        for step in steps:
            ctx["step_gold"][step["id"]] = {k: step[k] for k in ("expected", "target", "tolerance", "reference_curve", "rmsd_tolerance", "dependencies", "formula", "columns") if k in step}
        return ctx


# === block: score_0 (check id='harmonic_frequencies') ===
def score_0(artifact, step, ctx):
            gold = ctx["step_gold"]["harmonic_frequencies"]
            expected = gold["expected"]
            tol = gold["tolerance"]
            branch_col = gold["columns"]["branch_col"]
            value_col = gold["columns"]["value_col"]
            if artifact is None:
                return 0.0
            # artifact is already a list of dicts (parsed CSV)
            found = {}
            for r in artifact:
                try:
                    b = int(r[branch_col])
                    v = float(r[value_col])
                    found[b] = v
                except (ValueError, KeyError):
                    continue
            if not expected:
                return 0.0
            correct = 0
            for b_str, exp_val in expected.items():
                try:
                    b = int(b_str)
                except (ValueError, KeyError):
                    continue
                if b in found and abs(found[b] - exp_val) <= tol:
                    correct += 1
            return correct / len(expected)


# === block: score_1 (check id='gruneisen_constants') ===
def score_1(artifact, step, ctx):
            gold = ctx["step_gold"]["gruneisen_constants"]
            expected = gold["expected"]
            tol = gold["tolerance"]
            branch_col = gold["columns"]["branch_col"]
            value_col = gold["columns"]["value_col"]
            try:
                rows = list(csv.DictReader(open(artifact)))
            except Exception:
                return 0.0
            found = {}
            for r in rows:
                try:
                    b = int(r[branch_col])
                    v = float(r[value_col])
                    found[b] = v
                except (ValueError, KeyError):
                    continue
            if not expected:
                return 0.0
            correct = 0
            for b, exp_val in expected.items():
                if b in found and abs(found[b] - exp_val) <= tol:
                    correct += 1
            return correct / len(expected)


# === block: score_2 (check id='compressibility') ===
def score_2(artifact, step, ctx):
            gold = ctx["step_gold"]["compressibility"]
            target = gold["target"]
            tol = gold["tolerance"]
            try:
                with open(artifact) as f:
                    val = float(f.read().strip())
            except Exception:
                return 0.0
            if abs(val - target) <= tol:
                return 1.0
            else:
                return 0.0


# === block: score_3 (check id='thermal_expansion') ===
def score_3(artifact, step, ctx):
            gold = ctx["step_gold"]["thermal_expansion"]
            ref_curve = gold["reference_curve"]
            rmsd_tol = gold["rmsd_tolerance"]
            T_col = gold["columns"]["T_col"]
            eps_col = gold["columns"]["epsilon_col"]
            try:
                rows = list(csv.DictReader(open(artifact)))
            except Exception:
                return 0.0
            if not rows:
                return 0.0
            agent_T = []
            agent_eps = []
            for r in rows:
                try:
                    t = float(r[T_col])
                    e = float(r[eps_col])
                    agent_T.append(t)
                    agent_eps.append(e)
                except (ValueError, KeyError):
                    continue
            if not agent_T:
                return 0.0
            # linearly interpolate agent at reference T points
            ref_T = [pt[0] for pt in ref_curve]
            ref_eps = [pt[1] for pt in ref_curve]
            # simple interpolation using nearest? better: use piecewise linear
            def interp(T_target, T_list, V_list):
                if T_target <= T_list[0]:
                    return V_list[0]
                if T_target >= T_list[-1]:
                    return V_list[-1]
                for i in range(len(T_list)-1):
                    if T_list[i] <= T_target <= T_list[i+1]:
                        frac = (T_target - T_list[i]) / (T_list[i+1] - T_list[i])
                        return V_list[i] + frac * (V_list[i+1] - V_list[i])
                return V_list[-1]
            agent_interp = [interp(rt, agent_T, agent_eps) for rt in ref_T]
            # compute rmsd
            sq_diffs = [(ai - ri)**2 for ai, ri in zip(agent_interp, ref_eps)]
            rmsd = math.sqrt(sum(sq_diffs) / len(sq_diffs))
            if rmsd <= rmsd_tol:
                return 1.0
            elif rmsd <= rmsd_tol * 2:
                return max(0.0, 1.0 - (rmsd - rmsd_tol) / rmsd_tol)
            else:
                return 0.0


# === block: score_4 (check id='implicit_shift_consistency') ===
def score_4(artifact, step, ctx):
            gold = ctx["step_gold"]["implicit_shift_consistency"]
            deps = gold["dependencies"]
            tol = gold["tolerance"]
            # load gruneisen
            gru_path = os.path.join("/app/outputs", deps["gruneisen"])
            try:
                gru_rows = list(csv.DictReader(open(gru_path)))
            except Exception:
                return 0.0
            gamma = {}
            for r in gru_rows:
                try:
                    b = int(r["branch"])
                    gamma[b] = float(r["gamma"])
                except (ValueError, KeyError):
                    continue
            # load thermal expansion
            th_path = os.path.join("/app/outputs", deps["thermal_expansion"])
            try:
                th_rows = list(csv.DictReader(open(th_path)))
            except Exception:
                return 0.0
            temp_eps = {}
            for r in th_rows:
                try:
                    t = float(r["T_K"])
                    e = float(r["epsilon"])
                    temp_eps[t] = e
                except (ValueError, KeyError):
                    continue
            # load implicit shift
            try:
                shift_rows = list(csv.DictReader(open(artifact)))
            except Exception:
                return 0.0
            if not shift_rows:
                return 0.0
            # branches 4-12
            branches = list(range(4, 13))
            total = 0
            ok = 0
            for r in shift_rows:
                try:
                    t_val = float(r["T_K"])
                except (ValueError, KeyError):
                    continue
                eps = temp_eps.get(t_val)
                if eps is None:
                    continue
                for b in branches:
                    col = f"branch_{b}"
                    try:
                        agent_shift = float(r[col])
                    except (ValueError, KeyError):
                        continue
                    g = gamma.get(b)
                    if g is None:
                        continue
                    expected_shift = math.exp(-g * eps) - 1.0
                    if abs(agent_shift - expected_shift) <= tol:
                        ok += 1
                    total += 1
            if total == 0:
                return 0.0
            return ok / total


_SCORERS = {
    'harmonic_frequencies': score_0,
    'gruneisen_constants': score_1,
    'compressibility': score_2,
    'thermal_expansion': score_3,
    'implicit_shift_consistency': score_4,
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
