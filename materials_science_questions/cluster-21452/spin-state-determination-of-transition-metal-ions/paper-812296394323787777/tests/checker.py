import os
import json
import csv

# === author imports / helpers ===
import json, csv, os, math, sys

def triangle_ground_state(ratio):
    """
    Compute ground state (S_T, S_bc) for the isosceles Mn3O triangle
    using eq 8: H = -J (S_T^2 - S_bc^2) - J* S_bc^2, with S_a=S_b=S_c=2,
    J, J* both negative.  ratio = J/J* (positive).
    """
    best_E = float('inf')
    best_ST = None
    best_Sbc = None
    for Sbc in range(0, 5):
        for ST in range(abs(2 - Sbc), 2 + Sbc + 1):
            E = -ratio * (ST * (ST + 1) - Sbc * (Sbc + 1)) - Sbc * (Sbc + 1)
            if E < best_E:
                best_E = E
                best_ST = ST
                best_Sbc = Sbc
    return best_ST, best_Sbc


def tetranuclear_ground_state(J_wb, J_bb):
    """
    Compute ground state (S_T, S_A, S_B) for the Mn4O2 butterfly core
    using eq 6: E = -J_wb[ST(ST+1)-SA(SA+1)-SB(SB+1)] - J_bb SA(SA+1).
    J_wb, J_bb are the exchange constants (both negative).
    """
    best_E = float('inf')
    best_ST = None
    best_SA = None
    best_SB = None
    for SA in range(0, 5):
        for SB in range(0, 5):
            for ST in range(abs(SA - SB), SA + SB + 1):
                E = (-J_wb) * (ST * (ST + 1) - SA * (SA + 1) - SB * (SB + 1)) - J_bb * SA * (SA + 1)
                if E < best_E:
                    best_E = E
                    best_ST = ST
                    best_SA = SA
                    best_SB = SB
    return best_ST, best_SA, best_SB


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


# === block: score_0 (check id='step1') ===
def score_0(artifact, step, ctx):
      # artifact is a dict loaded from ground_state_complex1.json
      if not isinstance(artifact, dict):
          return 0.0
      required = {'S_T', 'S_A', 'S_B'}
      if not required.issubset(artifact.keys()):
          return 0.0
      # recompute expected ground state for complex 1
      params = step.get('recompute_params', {})
      J_wb = params.get('J_wb', -5.3)
      J_bb = params.get('J_bb', -24.6)
      exp_ST, exp_SA, exp_SB = tetranuclear_ground_state(J_wb, J_bb)
      try:
          got_ST = int(artifact['S_T'])
          got_SA = int(artifact['S_A'])
          got_SB = int(artifact['S_B'])
      except (ValueError, TypeError):
          return 0.0
      if got_ST == exp_ST and got_SA == exp_SA and got_SB == exp_SB:
          return 1.0
      return 0.0


# === block: score_1 (check id='step2') ===
def score_1(artifact, step, ctx):
      # artifact is a list of dicts from CSV reading
      if not isinstance(artifact, list) or len(artifact) == 0:
          return 0.0
      required_cols = {'ratio', 'S_T', 'S_bc'}
      if not required_cols.issubset(artifact[0].keys()):
          return 0.0
      eps = float(step.get('epsilon_param', 0.05))
      points = step.get('recompute_points', [])
      if not points:
          return 0.0
      matched = 0
      for ratio in points:
          exp_ST, exp_Sbc = triangle_ground_state(ratio)
          # find nearest row within eps
          found = False
          for row in artifact:
              try:
                  r = float(row['ratio'])
              except (ValueError, TypeError):
                  continue
              if abs(r - ratio) <= eps:
                  try:
                      st = int(row['S_T'])
                      sbc = int(row['S_bc'])
                  except (ValueError, TypeError):
                      continue
                  if st == exp_ST and sbc == exp_Sbc:
                      found = True
                      break
          if found:
              matched += 1
      return matched / len(points)


# === block: score_2 (check id='step3') ===
def score_2(artifact, step, ctx):
      if not isinstance(artifact, list) or len(artifact) == 0:
          return 0.0
      required_cols = {'J_wb', 'J_bb', 'S_T', 'S_A', 'S_B'}
      if not required_cols.issubset(artifact[0].keys()):
          return 0.0
      eps = float(step.get('epsilon_param', 0.2))
      points = step.get('recompute_points', [])
      if not points:
          return 0.0
      matched = 0
      for pt in points:
          J_wb_t = float(pt['J_wb'])
          J_bb_t = float(pt['J_bb'])
          exp_ST, exp_SA, exp_SB = tetranuclear_ground_state(J_wb_t, J_bb_t)
          found = False
          for row in artifact:
              try:
                  jw = float(row['J_wb'])
                  jb = float(row['J_bb'])
              except (ValueError, TypeError):
                  continue
              if abs(jw - J_wb_t) <= eps and abs(jb - J_bb_t) <= eps:
                  try:
                      st = int(row['S_T'])
                      sa = int(row['S_A'])
                      sb = int(row['S_B'])
                  except (ValueError, TypeError):
                      continue
                  if st == exp_ST and sa == exp_SA and sb == exp_SB:
                      found = True
                      break
          if found:
              matched += 1
      return matched / len(points)


_SCORERS = {
    'step1': score_0,
    'step2': score_1,
    'step3': score_2,
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
