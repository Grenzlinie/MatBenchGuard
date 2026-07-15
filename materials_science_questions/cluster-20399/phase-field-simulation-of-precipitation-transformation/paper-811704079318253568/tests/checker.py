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


# === block: score_0 (check id='transition_values') ===
def score_0(artifact, step, ctx):
        if artifact is None:
            return 0.0
        tol = step["config"]["tolerance"]
        ref = step["config"]["reference_table"]
        total_checks = 0
        correct = 0
        for row in artifact:
            try:
                c = float(row["c"])
            except:
                continue
            re = next((r for r in ref if abs(r["c"] - c) < 1e-9), None)
            if re is None:
                continue
            # Ms/Tg check
            if re.get("Ms") is not None:
                ms_str = row.get("Ms", "").strip()
                ms_ok = False
                if ms_str and ms_str.lower() != "nan":
                    try:
                        ms = float(ms_str)
                        if abs(ms - re["Ms"]) <= tol:
                            ms_ok = True
                    except:
                        pass
                tg_str = row.get("Tg", "").strip()
                tg_nan = (not tg_str or tg_str.lower() == "nan")
                correct += (1 if ms_ok else 0) + (1 if tg_nan else 0)
                total_checks += 2
            elif re.get("Tg") is not None:
                tg_str = row.get("Tg", "").strip()
                tg_ok = False
                if tg_str and tg_str.lower() != "nan":
                    try:
                        tg = float(tg_str)
                        if abs(tg - re["Tg"]) <= tol:
                            tg_ok = True
                    except:
                        pass
                ms_str = row.get("Ms", "").strip()
                ms_nan = (not ms_str or ms_str.lower() == "nan")
                correct += (1 if tg_ok else 0) + (1 if ms_nan else 0)
                total_checks += 2
            else:
                continue
            # Tnd check
            tnd_str = row.get("Tnd", "").strip()
            if tnd_str and tnd_str.lower() != "nan":
                try:
                    tnd = float(tnd_str)
                    if abs(tnd - re["Tnd"]) <= tol:
                        correct += 1
                except:
                    pass
            total_checks += 1
        if total_checks == 0:
            return 0.0
        return correct / total_checks


# === block: score_1 (check id='zfc_curve') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        config = step["config"]
        expected_Tnd = config["expected_Tnd"]
        tol_Tnd = config["tolerance_Tnd"]
        sep_th = config["separation_threshold"]
        Tg = config["Tg"]
        low_max = config["low_temp_check_T_max"]
        noise = config.get("monotonic_increase_noise", 0.001)
        data = []
        for row in artifact:
            try:
                T = float(row["T"])
                zfc = float(row["strain_ZFC"])
                fc = float(row["strain_FC"])
                data.append((T, zfc, fc))
            except:
                continue
        if len(data) < 2:
            return 0.0
        data.sort(key=lambda x: x[0], reverse=True)  # descending T
        # branching point
        branching_T = None
        for T, zfc, fc in data:
            if fc - zfc > sep_th:
                branching_T = T
                break
        # monotonic increase (as T decreases, strain increases)
        monotonic_ok = True
        for col in (1, 2):
            prev = None
            for row in data:
                val = row[col]
                if prev is not None:
                    if val < prev - noise:
                        monotonic_ok = False
                        break
                prev = val
            if not monotonic_ok:
                break
        # low temp separation
        low_sep_ok = True
        for T, zfc, fc in data:
            if T <= low_max:
                if fc <= zfc:
                    low_sep_ok = False
                    break
        score = 0.0
        if branching_T is not None and abs(branching_T - expected_Tnd) <= tol_Tnd:
            score += 0.3
        elif branching_T is not None:
            score += 0.1
        if low_sep_ok:
            score += 0.3
        if monotonic_ok:
            score += 0.3
        if len(data) >= 20:
            score += 0.1
        return score


# === block: score_2 (check id='trends') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        data = {}
        for row in artifact:
            try:
                c = float(row["c"])
            except:
                continue
            ms_str = row.get("Ms", "").strip()
            tg_str = row.get("Tg", "").strip()
            tnd_str = row.get("Tnd", "").strip()
            ms_val = None if (not ms_str or ms_str.lower() == "nan") else float(ms_str)
            tg_val = None if (not tg_str or tg_str.lower() == "nan") else float(tg_str)
            tnd_val = None if (not tnd_str or tnd_str.lower() == "nan") else float(tnd_str)
            data[c] = (ms_val, tg_val, tnd_val)
        # Ms trend for martensitic c
        ms_cs = [0, 0.025, 0.05]
        ms_vals = [data[c][0] for c in ms_cs if c in data and data[c][0] is not None]
        ms_score = 1.0
        if len(ms_vals) < 2:
            ms_score = 0.0
        else:
            viol = sum(1 for i in range(1, len(ms_vals)) if ms_vals[i] >= ms_vals[i-1])
            ms_score = max(0.0, 1.0 - 0.5 * viol)
        # Tg trend for strain-glass c
        tg_cs = [0.075, 0.1, 0.125, 0.15, 0.2]
        tg_vals = [data[c][1] for c in tg_cs if c in data and data[c][1] is not None]
        tg_score = 1.0
        if len(tg_vals) < 2:
            tg_score = 0.0
        else:
            viol = sum(1 for i in range(1, len(tg_vals)) if tg_vals[i] >= tg_vals[i-1])
            tg_score = max(0.0, 1.0 - 0.5 * viol)
        # Tnd trend: decreasing for c<=0.075, increasing for c>=0.1
        tnd_cs = sorted(list(data.keys()))
        tnd_vals = [data[c][2] for c in tnd_cs]
        dec_vals = [v for c, v in zip(tnd_cs, tnd_vals) if c <= 0.075]
        inc_vals = [v for c, v in zip(tnd_cs, tnd_vals) if c >= 0.1]
        dec_ok = all(dec_vals[i] <= dec_vals[i-1] for i in range(1, len(dec_vals))) if len(dec_vals) >= 2 else True
        inc_ok = all(inc_vals[i] >= inc_vals[i-1] for i in range(1, len(inc_vals))) if len(inc_vals) >= 2 else True
        tnd_score = 1.0 if (dec_ok and inc_ok) else 0.5 if (dec_ok or inc_ok) else 0.0
        return 0.3 * ms_score + 0.3 * tg_score + 0.4 * tnd_score


_SCORERS = {
    'transition_values': score_0,
    'zfc_curve': score_1,
    'trends': score_2,
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
