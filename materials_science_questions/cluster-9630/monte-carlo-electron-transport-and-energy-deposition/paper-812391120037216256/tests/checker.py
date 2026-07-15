import os
import json
import csv

# === author imports / helpers ===
import math, json, os


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
    gold_abs = spec['gold_absolute']
    gamma_C = gold_abs['C6+']['gamma_B']
    dedx_C = gold_abs['C6+']['dE_dx']
    ion_q = {'H+':1, 'C6+':6, 'Ca20+':20, 'Ni27+':27, 'Mo39+':39}
    gold_ratios = {}
    for ion, vals in gold_abs.items():
        q = ion_q[ion]
        rg = 36 * vals['gamma_B'] / (q**2 * gamma_C)
        rd = 36 * vals['dE_dx'] / (q**2 * dedx_C)
        gold_ratios[q] = {'R_gamma': rg, 'R_dE_dx': rd}

    tolerances = spec.get('tolerances', {'gamma_B_tol':0.5, 'dE_dx_tol':0.3, 'ratio_tol':0.5})
    ctx = {
        'gold_abs': gold_abs,
        'gold_ratios': gold_ratios,
        'tolerances': tolerances,
        'ion_order': ['H+', 'C6+', 'Ca20+', 'Ni27+', 'Mo39+']
    }
    return ctx


# === block: score_0 (check id='step_03_absolute_values') ===
def score_0(artifact, step, ctx):
    gold = ctx['gold_abs']
    tol_gamma = ctx['tolerances']['gamma_B_tol']
    tol_dedx = ctx['tolerances']['dE_dx_tol']
    ions = ctx['ion_order']
    scores = []
    for ion in ions:
        if ion not in artifact:
            scores.append(0.0)
            scores.append(0.0)
            continue
        for field, tol in [('gamma_B', tol_gamma), ('dE_dx', tol_dedx)]:
            val = artifact[ion].get(field)
            g = gold[ion][field]
            if val is None or g is None:
                scores.append(0.0)
                continue
            if abs(g) < 1e-12:
                err = abs(val - g)
            else:
                err = abs(val - g) / abs(g)
            if err <= tol:
                scores.append(1.0)
            else:
                s = max(0.0, 1.0 - (err - tol) / (2.0 * tol))
                scores.append(s)
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_1 (check id='step_04_normalized_ratios') ===
def score_1(artifact, step, ctx):
    tol_ratio = ctx['tolerances']['ratio_tol']
    gold_ratios = ctx['gold_ratios']
    expected_q = [1,6,20,27,39]
    # map csv to dict keyed by int Q_P
    csv_map = {}
    for row in artifact:
        try:
            q = int(row['Q_P'])
            csv_map[q] = (float(row['R_gamma']), float(row['R_dE_dx']))
        except (ValueError, KeyError):
            pass

    # 1) ratio matching scores
    ratio_scores = []
    for q in expected_q:
        if q not in csv_map or q not in gold_ratios:
            ratio_scores.append(0.0)
            continue
        rg_agent, rd_agent = csv_map[q]
        rg_gold = gold_ratios[q]['R_gamma']
        rd_gold = gold_ratios[q]['R_dE_dx']
        for agent_val, gold_val, tol in [(rg_agent, rg_gold, tol_ratio), (rd_agent, rd_gold, tol_ratio)]:
            if gold_val is None:
                s = 0.0
            elif abs(gold_val) < 1e-12:
                err = abs(agent_val - gold_val)
            else:
                err = abs(agent_val - gold_val) / abs(gold_val)
            if err <= tol:
                s = 1.0
            else:
                s = max(0.0, 1.0 - (err - tol) / (2.0 * tol))
            ratio_scores.append(s)
    ratio_match = sum(ratio_scores) / len(ratio_scores) if ratio_scores else 0.0

    # 2) monotonic trend
    sorted_q = sorted(csv_map.keys())
    rg_seq = [csv_map[q][0] for q in sorted_q if q in csv_map]
    rd_seq = [csv_map[q][1] for q in sorted_q if q in csv_map]
    def is_non_increasing(seq):
        return all(seq[i+1] <= seq[i] + 1e-9 for i in range(len(seq)-1))
    mono_rg = is_non_increasing(rg_seq) if len(rg_seq)>=2 else False
    mono_rd = is_non_increasing(rd_seq) if len(rd_seq)>=2 else False
    monotonic_score = 1.0 if (mono_rg and mono_rd) else 0.0

    # 3) consistency with absolute_values.json
    consistency_score = 0.0
    try:
        with open('/app/outputs/absolute_values.json') as f:
            abs_data = json.load(f)
        # compute ratios from abs_data
        # extract gamma_B and dE_dx from keys: H+, C6+, Ca20+, Ni27+, Mo39+
        ion_q_map = {'H+':1, 'C6+':6, 'Ca20+':20, 'Ni27+':27, 'Mo39+':39}
        gamma_C_val = abs_data.get('C6+', {}).get('gamma_B')
        dedx_C_val = abs_data.get('C6+', {}).get('dE_dx')
        if gamma_C_val is not None and dedx_C_val is not None and gamma_C_val != 0 and dedx_C_val != 0:
            ratios_from_abs = {}
            for ion, vals in abs_data.items():
                q = ion_q_map.get(ion)
                if q is None:
                    continue
                g = vals.get('gamma_B')
                d = vals.get('dE_dx')
                if g is None or d is None:
                    continue
                rg_calc = 36 * g / (q**2 * gamma_C_val)
                rd_calc = 36 * d / (q**2 * dedx_C_val)
                ratios_from_abs[q] = (rg_calc, rd_calc)
            # compare with csv_map
            matches = 0
            total = 0
            for q in expected_q:
                if q in csv_map and q in ratios_from_abs:
                    rg_csv, rd_csv = csv_map[q]
                    rg_calc, rd_calc = ratios_from_abs[q]
                    # relative difference within 1%
                    if abs(rg_csv - rg_calc) <= max(1e-6, 1e-4*abs(rg_csv)+1e-6):
                        matches += 1
                    if abs(rd_csv - rd_calc) <= max(1e-6, 1e-4*abs(rd_csv)+1e-6):
                        matches += 1
                    total += 2
            if total > 0:
                consistency_score = matches / total
            else:
                consistency_score = 1.0  # no pairs to check, give benefit of doubt
        else:
            consistency_score = 0.0
    except Exception:
        consistency_score = 0.0

    # weighted sum
    return 0.5 * ratio_match + 0.3 * monotonic_score + 0.2 * consistency_score


_SCORERS = {
    'step_03_absolute_values': score_0,
    'step_04_normalized_ratios': score_1,
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
