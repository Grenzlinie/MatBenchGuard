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
    return {
      "reference_values": spec.get("reference_values", []),
      "tolerance_rel": spec.get("tolerance_rel", 0.3),
      "tolerance_abs": spec.get("tolerance_abs", 0.05)
    }


# === block: score_0 (check id='shape_check') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) != 9:
      return 0.0
    required = {"material","orientation","stoichiometry","energy_below_CBM","m_tunnel"}
    for entry in artifact:
      if not isinstance(entry, dict) or not required.issubset(entry.keys()):
        return 0.0
    return 1.0


# === block: score_1 (check id='mtunnel_values') ===
def score_1(artifact, step, ctx):
    refs = ctx["reference_values"]
    tol_rel = ctx["tolerance_rel"]
    tol_abs = ctx["tolerance_abs"]
    if not isinstance(artifact, list):
      return 0.0
    scores = []
    for ref in refs:
      match = None
      for entry in artifact:
        if (entry.get("material") == ref["material"] and
            entry.get("orientation") == ref["orientation"] and
            entry.get("stoichiometry") == ref["stoichiometry"]):
          match = entry
          break
      if match is None:
        scores.append(0.0)
        continue
      val = match.get("m_tunnel")
      gold = ref["m_tunnel"]
      if gold == 0.0:
        scores.append(1.0 if val == 0.0 else 0.0)
      else:
        rel_err = abs(val - gold) / abs(gold)
        if rel_err <= tol_rel or abs(val - gold) <= tol_abs:
          scores.append(1.0)
        else:
          scores.append(max(0.0, 1.0 - (rel_err - tol_rel) / 0.2))
    if not scores:
      return 0.0
    return sum(scores) / len(scores)


# === block: score_2 (check id='r_tio2_ordering') ===
def score_2(artifact, step, ctx):
    if not isinstance(artifact, list):
      return 0.0
    # find entries by orientation for r-TiO2
    vals = {}
    for e in artifact:
      if e.get("material") == "r-TiO2" and e.get("stoichiometry") == "stoichiometric":
        orient = e.get("orientation")
        if orient in ("(110)","(001)","(100)"):
          vals[orient] = e.get("m_tunnel")
    if set(vals.keys()) != {"(110)","(001)","(100)"}:
      return 0.0
    m110 = vals["(110)"]
    m001 = vals["(001)"]
    m100 = vals["(100)"]
    return 1.0 if m110 < m001 < m100 else 0.0


# === block: score_3 (check id='sto_ordering') ===
def score_3(artifact, step, ctx):
    if not isinstance(artifact, list):
      return 0.0
    vals = {}
    for e in artifact:
      if e.get("material") == "SrTiO3" and e.get("stoichiometry") == "stoichiometric":
        orient = e.get("orientation")
        if orient in ("(110)","(001)","(111)"):
          vals[orient] = e.get("m_tunnel")
    if set(vals.keys()) != {"(110)","(001)","(111)"}:
      return 0.0
    m110 = vals["(110)"]
    m001 = vals["(001)"]
    m111 = vals["(111)"]
    return 1.0 if m110 < m001 < m111 else 0.0


# === block: score_4 (check id='sr_rich_ordering') ===
def score_4(artifact, step, ctx):
    if not isinstance(artifact, list):
      return 0.0
    stoic_vals = []
    sr_rich_vals = []
    for e in artifact:
      if e.get("material") != "SrTiO3":
        continue
      m = e.get("m_tunnel")
      if m is None:
        continue
      stoich = e.get("stoichiometry","")
      if stoich == "stoichiometric":
        stoic_vals.append(m)
      elif stoich in ("Sr0.62Ti0.38O4","Sr2TiO4"):
        sr_rich_vals.append(m)
    if not stoic_vals or not sr_rich_vals:
      return 0.0
    max_stoic = max(stoic_vals)
    all_greater = all(v > max_stoic for v in sr_rich_vals)
    return 1.0 if all_greater else 0.0


_SCORERS = {
    'shape_check': score_0,
    'mtunnel_values': score_1,
    'r_tio2_ordering': score_2,
    'sto_ordering': score_3,
    'sr_rich_ordering': score_4,
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
