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
    return {'gold': spec['gold'], 'tolerances': spec['tolerances'], 'soc_tolerance': spec['soc_tolerance'], 'summary_tolerance': spec['summary_tolerance']}


# === block: score_0 (check id='recompute_dielectric') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    gold = ctx['gold']
    tol_dc = ctx['tolerances']['static_dielectric_constant']
    tol_pl = ctx['tolerances']['plasmon_energy']
    total = 0
    passed = 0
    for compound in ['Li3AlN2', 'Li3GaN2']:
        if compound not in artifact:
            return 0.0
        for soc in ['without_SOC', 'with_SOC']:
            if soc not in artifact[compound]:
                return 0.0
            data = artifact[compound][soc]
            freq = data.get('frequency')
            eps1 = data.get('epsilon1')
            eps2 = data.get('epsilon2')
            if freq is None or eps1 is None or eps2 is None:
                return 0.0
            if len(freq) != len(eps1) or len(freq) != len(eps2) or len(freq) == 0:
                return 0.0
            idx0 = freq.index(min(freq))
            static_dc = eps1[idx0]
            eels = [eps2[i] / (eps1[i]**2 + eps2[i]**2) if (eps1[i]**2 + eps2[i]**2) != 0 else 0.0 for i in range(len(freq))]
            max_idx = max(range(len(eels)), key=lambda i: eels[i])
            plasmon_energy = freq[max_idx]
            gold_soc = gold[compound][soc]
            if abs(static_dc - gold_soc['static_dielectric_constant']) <= tol_dc:
                passed += 1
            total += 1
            if abs(plasmon_energy - gold_soc['plasmon_energy']) <= tol_pl:
                passed += 1
            total += 1
    return passed / total if total > 0 else 0.0


# === block: score_1 (check id='check_soc_effect') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    soc_tol = ctx['soc_tolerance']
    total = 0
    passed = 0
    for compound in ['Li3AlN2', 'Li3GaN2']:
        if compound not in artifact:
            return 0.0
        wo = artifact[compound].get('without_SOC')
        w = artifact[compound].get('with_SOC')
        if wo is None or w is None:
            return 0.0
        freq_wo = wo.get('frequency'); eps1_wo = wo.get('epsilon1'); eps2_wo = wo.get('epsilon2')
        freq_w = w.get('frequency'); eps1_w = w.get('epsilon1'); eps2_w = w.get('epsilon2')
        if any(x is None for x in [freq_wo, eps1_wo, eps2_wo, freq_w, eps1_w, eps2_w]):
            return 0.0
        if len(freq_wo) != len(eps1_wo) or len(freq_wo) != len(eps2_wo) or len(freq_wo) == 0:
            return 0.0
        if len(freq_w) != len(eps1_w) or len(freq_w) != len(eps2_w) or len(freq_w) == 0:
            return 0.0
        idx0_wo = freq_wo.index(min(freq_wo)); dc_wo = eps1_wo[idx0_wo]
        idx0_w = freq_w.index(min(freq_w)); dc_w = eps1_w[idx0_w]
        eels_wo = [eps2_wo[i] / (eps1_wo[i]**2 + eps2_wo[i]**2) if (eps1_wo[i]**2 + eps2_wo[i]**2) != 0 else 0.0 for i in range(len(freq_wo))]
        pl_wo = freq_wo[max(range(len(eels_wo)), key=lambda i: eels_wo[i])]
        eels_w = [eps2_w[i] / (eps1_w[i]**2 + eps2_w[i]**2) if (eps1_w[i]**2 + eps2_w[i]**2) != 0 else 0.0 for i in range(len(freq_w))]
        pl_w = freq_w[max(range(len(eels_w)), key=lambda i: eels_w[i])]
        if abs(dc_wo - dc_w) <= soc_tol:
            passed += 1
        total += 1
        if abs(pl_wo - pl_w) <= soc_tol:
            passed += 1
        total += 1
    return passed / total if total > 0 else 0.0


# === block: score_2 (check id='check_summary') ===
def score_2(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    summary_tol = ctx['summary_tolerance']
    dielectric_path = '/app/outputs/dielectric_function.json'
    try:
        with open(dielectric_path) as f:
            dielec_data = json.load(f)
    except:
        return 0.0
    if not isinstance(dielec_data, dict):
        return 0.0
    total = 0
    passed = 0
    for compound in ['Li3AlN2', 'Li3GaN2']:
        if compound not in dielec_data or compound not in artifact:
            return 0.0
        for soc in ['without_SOC', 'with_SOC']:
            if soc not in dielec_data[compound] or soc not in artifact[compound]:
                return 0.0
            d_data = dielec_data[compound][soc]
            freq = d_data.get('frequency')
            eps1 = d_data.get('epsilon1')
            eps2 = d_data.get('epsilon2')
            if freq is None or eps1 is None or eps2 is None:
                return 0.0
            if len(freq) != len(eps1) or len(freq) != len(eps2) or len(freq) == 0:
                return 0.0
            idx0 = freq.index(min(freq))
            static_dc = eps1[idx0]
            eels = [eps2[i] / (eps1[i]**2 + eps2[i]**2) if (eps1[i]**2 + eps2[i]**2) != 0 else 0.0 for i in range(len(freq))]
            max_idx = max(range(len(eels)), key=lambda i: eels[i])
            plasmon_energy = freq[max_idx]
            rep = artifact[compound][soc]
            rep_dc = rep.get('static_dielectric_constant')
            rep_pl = rep.get('plasmon_energy')
            if rep_dc is None or rep_pl is None:
                return 0.0
            if isinstance(rep_dc, (int, float)) and isinstance(rep_pl, (int, float)):
                if abs(rep_dc - static_dc) <= summary_tol:
                    passed += 1
                total += 1
                if abs(rep_pl - plasmon_energy) <= summary_tol:
                    passed += 1
                total += 1
            else:
                return 0.0
    return passed / total if total > 0 else 0.0


_SCORERS = {
    'recompute_dielectric': score_0,
    'check_soc_effect': score_1,
    'check_summary': score_2,
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
