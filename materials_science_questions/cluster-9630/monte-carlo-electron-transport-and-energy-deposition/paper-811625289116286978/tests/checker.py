import os
import json
import csv

# === author imports / helpers ===
import json
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
    return {
      "gold": {
        "power_reflection": 0.161,
        "beam_reflection": 0.29,
        "electron_penetration_depth_um": 2.1,
        "heat_penetration_depth_um": 1.4,
        "ratio_heat_to_electron": 0.6666666666666666
      },
      "params": {
        "power_reflection": {"rel_tol": 0.25},
        "beam_reflection": {"rel_tol": 0.25},
        "electron_penetration_depth_um": {"abs_tol": 0.5},
        "heat_penetration_depth_um": {"abs_tol": 0.5},
        "ratio_heat_to_electron": {"abs_tol": 0.1}
      }
    }


# === block: score_0 (check id='score_results') ===
def score_0(artifact, step, ctx):
        if not isinstance(artifact, dict):
            return 0.0
        try:
            gold = ctx["gold"]
            params = ctx["params"]
        except Exception:
            return 0.0

        # power reflection
        try:
            pr = float(artifact.get("power_reflection"))
            pr_gold = float(gold["power_reflection"])
            rel_tol = float(params["power_reflection"]["rel_tol"])
            if abs(pr_gold) < 1e-12:
                s_pr = 1.0 if abs(pr) < 1e-9 else 0.0
            else:
                s_pr = 1.0 if abs(pr - pr_gold) / abs(pr_gold) <= rel_tol else 0.0
        except Exception:
            s_pr = 0.0

        # beam reflection
        try:
            br = float(artifact.get("beam_reflection"))
            br_gold = float(gold["beam_reflection"])
            rel_tol = float(params["beam_reflection"]["rel_tol"])
            if abs(br_gold) < 1e-12:
                s_br = 1.0 if abs(br) < 1e-9 else 0.0
            else:
                s_br = 1.0 if abs(br - br_gold) / abs(br_gold) <= rel_tol else 0.0
        except Exception:
            s_br = 0.0

        # electron depth
        try:
            ed = float(artifact.get("electron_penetration_depth_um"))
            ed_gold = float(gold["electron_penetration_depth_um"])
            abs_tol = float(params["electron_penetration_depth_um"]["abs_tol"])
            s_ed = 1.0 if abs(ed - ed_gold) <= abs_tol else 0.0
        except Exception:
            s_ed = 0.0

        # heat depth
        try:
            hd = float(artifact.get("heat_penetration_depth_um"))
            hd_gold = float(gold["heat_penetration_depth_um"])
            abs_tol = float(params["heat_penetration_depth_um"]["abs_tol"])
            hd_ok = abs(hd - hd_gold) <= abs_tol
            # structural constraint: heat depth must be less than electron depth
            ed_val = float(artifact.get("electron_penetration_depth_um"))
            constraint = hd < ed_val
            s_hd = 1.0 if (hd_ok and constraint) else 0.0
        except Exception:
            s_hd = 0.0

        # ratio heat/electron
        try:
            ratio = float(artifact.get("ratio_heat_to_electron"))
            ratio_gold = float(gold["ratio_heat_to_electron"])
            abs_tol = float(params["ratio_heat_to_electron"]["abs_tol"])
            ratio_ok = (abs(ratio - ratio_gold) <= abs_tol) and (0.5 <= ratio <= 0.9)
            s_ratio = 1.0 if ratio_ok else 0.0
        except Exception:
            s_ratio = 0.0

        sub_scores = [s_pr, s_br, s_ed, s_hd, s_ratio]
        return sum(sub_scores) / len(sub_scores)


_SCORERS = {
    'score_results': score_0,
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
