import os
import json
import csv

# === author imports / helpers ===
import csv, math


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
        spec_steps = spec.get('steps', [])
        ctx = {}
        for step in spec_steps:
            if step.get('output_file') == 'step_02_structural_properties.csv':
                ctx['structural_gold'] = step.get('gold', {})
            elif step.get('output_file') == 'step_04_band_gaps.csv':
                ctx['band_gap_gold'] = step.get('gold', {})
        return ctx


# === block: score_0 (check id='structural_props') ===
def score_0(artifact, step, ctx):
        gold = ctx.get('structural_gold', {})
        if not gold:
            return 0.0
        if not isinstance(artifact, list) or not artifact:
            return 0.0
        # Build agent dict keyed by (compound, structure)
        agent_dict = {}
        for row in artifact:
            key = (row.get('compound', '').strip(), row.get('structure', '').strip())
            try:
                a_eq = float(row['a_eq_angstrom'])
                B0 = float(row['B0_Mbar'])
                B0p = float(row['B0_prime'])
            except (KeyError, ValueError):
                continue
            agent_dict[key] = {'a_eq_angstrom': a_eq, 'B0_Mbar': B0, 'B0_prime': B0p}
        gold_vals = gold.get('values', [])
        tols = gold.get('tolerances', {})
        rel_a = tols.get('a_eq_angstrom_rel', 0.03)
        rel_B0 = tols.get('B0_Mbar_rel', 0.15)
        rel_B0p = tols.get('B0_prime_rel', 0.15)
        # Parameter accuracy
        total_accuracy = 0.0
        num_params = 0
        for g in gold_vals:
            key = (g['compound'], g['structure'])
            agent = agent_dict.get(key)
            if agent is None:
                num_params += 3
                continue
            num_params += 3
            for param, rel_tol in [('a_eq_angstrom', rel_a), ('B0_Mbar', rel_B0), ('B0_prime', rel_B0p)]:
                gold_val = g[param]
                agent_val = agent[param]
                if abs(agent_val - gold_val) / gold_val <= rel_tol:
                    total_accuracy += 1.0
        accuracy_score = total_accuracy / num_params if num_params > 0 else 0.0
        # Trend checks
        trend_ok = 0
        trend_total = 0
        # B1 lattice ordering
        try:
            a_B1 = {}
            for comp in ['SrS','SrSe','SrTe']:
                a_B1[comp] = agent_dict[(comp,'B1')]['a_eq_angstrom']
            if a_B1['SrS'] < a_B1['SrSe'] < a_B1['SrTe']:
                trend_ok += 1
            trend_total += 1
        except:
            trend_total += 1
        # B2 lattice ordering
        try:
            a_B2 = {}
            for comp in ['SrS','SrSe','SrTe']:
                a_B2[comp] = agent_dict[(comp,'B2')]['a_eq_angstrom']
            if a_B2['SrS'] < a_B2['SrSe'] < a_B2['SrTe']:
                trend_ok += 1
            trend_total += 1
        except:
            trend_total += 1
        # B1 bulk modulus decreasing
        try:
            B0_B1 = {}
            for comp in ['SrS','SrSe','SrTe']:
                B0_B1[comp] = agent_dict[(comp,'B1')]['B0_Mbar']
            if B0_B1['SrS'] > B0_B1['SrSe'] > B0_B1['SrTe']:
                trend_ok += 1
            trend_total += 1
        except:
            trend_total += 1
        # B2 bulk modulus decreasing
        try:
            B0_B2 = {}
            for comp in ['SrS','SrSe','SrTe']:
                B0_B2[comp] = agent_dict[(comp,'B2')]['B0_Mbar']
            if B0_B2['SrS'] > B0_B2['SrSe'] > B0_B2['SrTe']:
                trend_ok += 1
            trend_total += 1
        except:
            trend_total += 1
        trend_score = trend_ok / trend_total if trend_total > 0 else 0.0
        # Combine: parameter accuracy 80%, trend 20%
        step_score = 0.8 * accuracy_score + 0.2 * trend_score
        return step_score


# === block: score_1 (check id='band_gaps') ===
def score_1(artifact, step, ctx):
        gold = ctx.get('band_gap_gold', {})
        if not gold:
            return 0.0
        if not isinstance(artifact, list) or not artifact:
            return 0.0
        agent_dict = {}
        for row in artifact:
            compound = row.get('compound', '').strip()
            try:
                gap = float(row['indirect_gap_Gamma_X_eV'])
            except (KeyError, ValueError):
                continue
            agent_dict[compound] = gap
        gold_vals = gold.get('values', [])
        tol_rel = gold.get('tolerance_rel', 0.15)
        ok = 0
        total = 0
        for g in gold_vals:
            comp = g['compound']
            agent_gap = agent_dict.get(comp)
            total += 1
            if agent_gap is not None and abs(agent_gap - g['indirect_gap_Gamma_X_eV']) / g['indirect_gap_Gamma_X_eV'] <= tol_rel:
                ok += 1
        if total == 0:
            return 0.0
        return ok / total


_SCORERS = {
    'structural_props': score_0,
    'band_gaps': score_1,
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
