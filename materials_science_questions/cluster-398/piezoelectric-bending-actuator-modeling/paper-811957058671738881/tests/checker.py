import os
import json
import csv

# === author imports / helpers ===
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


# === block: score_0 (check id='step_03_intensity_factors') ===
def score_0(artifact, step, ctx):
      # scorer for intensity_factors.json
      hom = artifact.get('homogeneous')
      grad = artifact.get('graded')
      if not isinstance(hom, dict) or not isinstance(grad, dict):
          return 0.0
      try:
          kih = float(hom['K_I_normalized'])
          kdh = float(hom['K_D_normalized'])
          kig = float(grad['K_I_normalized'])
          kdg = float(grad['K_D_normalized'])
      except (KeyError, TypeError, ValueError):
          return 0.0

      # 1) Homogeneous K_I must be 1.0
      score_h = 1.0 if abs(kih - 1.0) <= 1e-4 else 0.0

      # 2) Ratio K_D/K_I should be consistent between the two cases
      eps = 1e-12
      rh = kdh / kih if abs(kih) > eps else 0.0
      rg = kdg / kig if abs(kig) > eps else 0.0
      ratio_ok = 1.0 if abs(rh - rg) <= max(1e-6, 0.01 * abs(rh)) else 0.0

      # 3) Hidden gold for the graded case (provided by the task author in grading_spec)
      gold = step.get('gold', {}) or {}
      expected_gr = gold.get('graded')
      if isinstance(expected_gr, dict):
          try:
              exp_ki = float(expected_gr['K_I_normalized'])
              exp_kd = float(expected_gr['K_D_normalized'])
              tol_rel = float(expected_gr.get('relative_tolerance', 0.02))
              re_ki = abs(kig - exp_ki) / (abs(exp_ki) + eps)
              re_kd = abs(kdg - exp_kd) / (abs(exp_kd) + eps)
              if re_ki <= tol_rel and re_kd <= tol_rel:
                  score_g = 1.0
              else:
                  # Partial credit when close but not within tolerance
                  score_g = max(0.0, 1.0 - 0.5 * ((re_ki + re_kd) / tol_rel - 1.0))
          except (KeyError, TypeError, ValueError):
              score_g = 0.0
          # Weight: homogeneous exact 20%, ratio consistency 10%, graded match 70%
          return 0.2 * score_h + 0.1 * ratio_ok + 0.7 * score_g
      else:
          # No hidden gold – use structural only, but discourage trivial copy of homogeneous value
          not_trivial = 1.0 if abs(kig - 1.0) > 1e-4 else 0.0
          return 0.4 * score_h + 0.3 * ratio_ok + 0.3 * not_trivial


_SCORERS = {
    'step_03_intensity_factors': score_0,
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
