import os
import json
import csv

# === author imports / helpers ===
import json, csv, os


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


# === block: score_0 (check id='check_results') ===
def score_0(artifact, step, ctx):
        rows = artifact
        if not rows or not isinstance(rows, list):
            return 0.0
        gold = step.get('gold_values', [])
        if not gold:
            return 0.0
        tol_vol_rel = float(step.get('tolerance_volume_relative', 0.05))
        tol_coh_abs = float(step.get('tolerance_cohesive_abs', 1.0))
        tol_gap_abs = float(step.get('tolerance_bandgap_abs', 0.2))
        tol_diel_abs = float(step.get('tolerance_dielectric_abs', 0.5))
        gold_dict = {}
        for g in gold:
            gold_dict[g['composition']] = g
        valid_rows = 0
        volumes = []
        cohs = []
        gaps = []
        diels = []
        for row in rows:
            if not isinstance(row, dict):
                continue
            comp_val = row.get('composition')
            if comp_val is None or comp_val == '':
                continue
            vol_val = row.get('volume_ang3')
            coh_val = row.get('cohesive_energy_eV')
            gap_val = row.get('band_gap_eV')
            diel_val = row.get('static_dielectric_const')
            if (vol_val is None or vol_val == '' or coh_val is None or coh_val == '' or
                    gap_val is None or gap_val == '' or diel_val is None or diel_val == ''):
                continue
            try:
                comp = float(comp_val)
                vol = float(vol_val)
                coh = float(coh_val)
                gap = float(gap_val)
                diel = float(diel_val)
            except (ValueError, TypeError):
                continue
            if comp not in gold_dict:
                continue
            g = gold_dict[comp]
            # volume tolerance: relative if gold non-zero, else absolute
            gold_vol = g['volume_ang3']
            vol_diff = abs(vol - gold_vol)
            vol_tol = tol_vol_rel * abs(gold_vol) if abs(gold_vol) > 0 else tol_vol_rel
            vol_ok = vol_diff <= vol_tol
            coh_ok = abs(coh - g['cohesive_energy_eV']) <= tol_coh_abs
            gap_ok = abs(gap - g['band_gap_eV']) <= tol_gap_abs
            diel_ok = abs(diel - g['static_dielectric_const']) <= tol_diel_abs
            if vol_ok and coh_ok and gap_ok and diel_ok:
                valid_rows += 1
            volumes.append((comp, vol))
            cohs.append((comp, coh))
            gaps.append((comp, gap))
            diels.append((comp, diel))
        trends_ok = True
        if len(volumes) >= 2:
            sorted_vols = sorted(volumes, key=lambda x: x[0])
            sorted_cohs = sorted(cohs, key=lambda x: x[0])
            sorted_gaps = sorted(gaps, key=lambda x: x[0])
            sorted_diels = sorted(diels, key=lambda x: x[0])
            for i in range(len(sorted_vols)-1):
                if sorted_vols[i][1] <= sorted_vols[i+1][1]:
                    trends_ok = False
                    break
            if trends_ok:
                for i in range(len(sorted_cohs)-1):
                    if sorted_cohs[i][1] <= sorted_cohs[i+1][1]:
                        trends_ok = False
                        break
            if trends_ok:
                for i in range(len(sorted_gaps)-1):
                    if sorted_gaps[i][1] >= sorted_gaps[i+1][1]:
                        trends_ok = False
                        break
            if trends_ok:
                for i in range(len(sorted_diels)-1):
                    if sorted_diels[i][1] <= sorted_diels[i+1][1]:
                        trends_ok = False
                        break
        row_score = valid_rows / 7.0
        trend_score = 1.0 if trends_ok else 0.0
        score = 0.7 * row_score + 0.3 * trend_score
        return min(1.0, max(0.0, score))


_SCORERS = {
    'check_results': score_0,
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
