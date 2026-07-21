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


# === block: score_0 (check id='step_effective_modulus') ===
def score_0(artifact, step, ctx):
      gold = step['parameters']['gold']
      rtol = step['parameters']['relative_tolerance']
      by_conc = {}
      for row in artifact:
        try:
          c = float(row['concentration'])
          v = float(row['shear_modulus_GPa'])
          by_conc[c] = v
        except (ValueError, KeyError):
          continue
      if not by_conc:
        return 0.0
      passes = 0
      for g in gold:
        cg = g['concentration']
        vg = g['shear_modulus_GPa']
        if cg not in by_conc:
          continue
        va = by_conc[cg]
        if abs(va - vg) <= rtol * vg:
          passes += 1
      return passes / len(gold) if gold else 0.0


# === block: score_1 (check id='step_stress_concentration') ===
def score_1(artifact, step, ctx):
      params = step['parameters']
      tol = params['abs_tolerance']
      sym_tol = params['symmetry_tolerance']
      max_cons_tol = params['max_row_consistency_tolerance']
      min_pts = params['min_points']
      gold0 = params['gold_value_at_zero']
      gold_max = params['gold_max']

      numeric_rows = []
      max_row_val = None
      for row in artifact:
        x = row.get('x1', '').strip()
        try:
          val = float(row['stress_concentration_11'])
        except (ValueError, KeyError):
          continue
        if x == 'max':
          max_row_val = val
        else:
          try:
            xf = float(x)
            numeric_rows.append((xf, val))
          except ValueError:
            continue

      if len(numeric_rows) < min_pts:
        return 0.0

      # find value at x1=0 (exact or nearest)
      val0 = None
      best_diff = float('inf')
      for xf, v in numeric_rows:
        d = abs(xf - 0.0)
        if d < best_diff:
          best_diff = d
          val0 = v
      if val0 is None:
        return 0.0

      # compute max from numeric rows
      numeric_max = max(v for _, v in numeric_rows)

      # sub-scores
      s0 = 1.0 if abs(val0 - gold0) <= tol else max(0.0, 1.0 - abs(val0 - gold0) / (5 * tol))
      smax = 1.0 if abs(numeric_max - gold_max) <= tol else max(0.0, 1.0 - abs(numeric_max - gold_max) / (5 * tol))

      # symmetry
      values_by_x = {}
      for xf, v in numeric_rows:
        key = round(xf, 10)
        if key in values_by_x:
          continue
        values_by_x[key] = v
      pos_xs = sorted([k for k in values_by_x if k > 0])
      neg_sym = 0
      total_sym = len(pos_xs)
      for xp in pos_xs:
        xn = -xp
        if xn in values_by_x:
          if abs(values_by_x[xp] - values_by_x[xn]) <= sym_tol:
            neg_sym += 1
      sym_score = neg_sym / total_sym if total_sym > 0 else 1.0

      # max row consistency
      max_cons_score = 0.0
      if max_row_val is not None and abs(max_row_val - numeric_max) <= max_cons_tol:
        max_cons_score = 1.0

      return 0.1 * (1.0 if len(numeric_rows) >= min_pts else 0.0) + \
             0.3 * s0 + \
             0.3 * smax + \
             0.2 * sym_score + \
             0.1 * max_cons_score


_SCORERS = {
    'step_effective_modulus': score_0,
    'step_stress_concentration': score_1,
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
