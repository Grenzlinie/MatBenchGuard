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


# === block: score_0 (check id='cdw_binding') ===
def score_0(artifact, step, ctx):
        if artifact is None:
            return 0.0
        gold = step.get("gold", [])
        if not gold:
            return 0.0
        tolerances = step.get("tolerances", {})
        be_abs = tolerances.get("binding_energy_abs_meV", 20.0)
        be_rel = tolerances.get("binding_energy_rel", 0.3)
        cv_abs = tolerances.get("CV_percent_abs_pp", 5.0)
        chalcogen_order = step.get("chalcogen_order", ["S", "Se", "Te"])

        # Index submitted entries by (polytype, chalcogenide, supercell)
        sub_entries = {}
        for e in artifact:
            key = (e.get("polytype"), e.get("chalcogenide"), e.get("supercell"))
            if key not in sub_entries:
                sub_entries[key] = []
            sub_entries[key].append(e)

        matches = 0
        total_gold = len(gold)
        for ge in gold:
            key = (ge["polytype"], ge["chalcogenide"], ge["supercell"])
            if key not in sub_entries:
                continue
            se = sub_entries[key][0]   # use first matching entry
            # binding energy tolerance
            be_ok = False
            if "binding_energy_meV" in se and "binding_energy_meV" in ge:
                diff_be = abs(se["binding_energy_meV"] - ge["binding_energy_meV"])
                if diff_be <= be_abs:
                    be_ok = True
                else:
                    max_val = max(abs(se["binding_energy_meV"]), abs(ge["binding_energy_meV"]))
                    if max_val != 0 and diff_be / max_val <= be_rel:
                        be_ok = True
            # CV tolerance
            cv_ok = False
            if "CV_percent" in se and "CV_percent" in ge:
                diff_cv = abs(se["CV_percent"] - ge["CV_percent"])
                if diff_cv <= cv_abs:
                    cv_ok = True
            if be_ok and cv_ok:
                matches += 1

        numeric_ratio = matches / total_gold if total_gold > 0 else 0.0

        # Trend check: for each (polytype, supercell) where all three chalcogenides are present,
        # verify the agent's binding energies are non‑decreasing along S → Se → Te
        trend_pass = True
        if step.get("trend_check", False):
            groups = {}
            for ge in gold:
                key = (ge["polytype"], ge["supercell"])
                if key not in groups:
                    groups[key] = {}
                groups[key][ge["chalcogenide"]] = True   # mark presence
            for (poly, sc), _ in groups.items():
                sub_vals = []
                for ch in chalcogen_order:
                    sub_key = (poly, ch, sc)
                    if sub_key in sub_entries:
                        se = sub_entries[sub_key][0]
                        sub_vals.append(se.get("binding_energy_meV", None))
                    else:
                        sub_vals.append(None)
                if None not in sub_vals and not all(sub_vals[i] <= sub_vals[i+1] for i in range(len(sub_vals)-1)):
                    trend_pass = False
                    break

        trend_score = 1.0 if trend_pass else 0.0
        final = numeric_ratio * 0.9 + trend_score * 0.1
        return max(0.0, min(1.0, final))


# === block: score_1 (check id='ta_distances') ===
def score_1(artifact, step, ctx):
        if artifact is None:
            return 0.0
        gold = step.get("gold", [])
        if not gold:
            return 0.0
        tolerances = step.get("tolerances", {})
        pc_abs = tolerances.get("percent_change_abs_pp", 5.0)
        d_abs = tolerances.get("distance_A_abs_A", 0.5)

        # Index submitted entries by (chalcogenide, supercell, site_pair)
        sub_entries = {}
        for e in artifact:
            key = (e.get("chalcogenide"), e.get("supercell"), e.get("site_pair"))
            if key not in sub_entries:
                sub_entries[key] = []
            sub_entries[key].append(e)

        matches = 0
        total_gold = len(gold)
        for ge in gold:
            key = (ge["chalcogenide"], ge["supercell"], ge["site_pair"])
            if key not in sub_entries:
                continue
            se = sub_entries[key][0]   # use first matching entry
            pc_ok = False
            if "percent_change" in se and "percent_change" in ge:
                if abs(se["percent_change"] - ge["percent_change"]) <= pc_abs:
                    pc_ok = True
            dist_ok = False
            if "distance_A" in se and "distance_A" in ge:
                if abs(se["distance_A"] - ge["distance_A"]) <= d_abs:
                    dist_ok = True
            if pc_ok and dist_ok:
                matches += 1

        numeric_ratio = matches / total_gold if total_gold > 0 else 0.0

        # Trend check: 1T-TaTe2 AB contraction >= 8% (percent_change <= -8%)
        trend_checks = step.get("trend_checks", [])
        trend_pass = True
        for tc in trend_checks:
            params = tc.get("params", {})
            chalc = params.get("chalcogenide")
            sp = params.get("site_pair")
            max_pc = params.get("percent_change_max")
            min_hits = params.get("min_hit_count", 1)
            count = 0
            for key, entries in sub_entries.items():
                if key[0] == chalc and key[2] == sp:
                    for entry in entries:
                        pc = entry.get("percent_change")
                        if pc is not None and pc <= max_pc:
                            count += 1
            if count < min_hits:
                trend_pass = False
                break

        trend_score = 1.0 if trend_pass else 0.0
        final = numeric_ratio * 0.9 + trend_score * 0.1
        return max(0.0, min(1.0, final))


_SCORERS = {
    'cdw_binding': score_0,
    'ta_distances': score_1,
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
