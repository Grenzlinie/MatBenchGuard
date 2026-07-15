import os
import json
import csv

# === author imports / helpers ===
import csv, json, math, os


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
    steps_by_id = {s['id']: s for s in spec['steps']}
    return {'steps': steps_by_id}


# === block: score_0 (check id='ga_covariance_matrix') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, dict) or 'H_cov' not in artifact or 'S_cov' not in artifact:
        return 0.0
    for mat_name in ('H_cov', 'S_cov'):
        mat = artifact[mat_name]
        if len(mat) != 66 or any(len(row) != 66 for row in mat):
            return 0.0
        for i in range(66):
            for j in range(66):
                if abs(mat[i][j] - mat[j][i]) > 1e-6:
                    return 0.0
            if mat[i][i] <= 0:
                return 0.0
    return 1.0


# === block: score_1 (check id='raw_mkm_results') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    hidden = ctx['steps']['raw_mkm_results']['hidden']
    T_target = hidden['target_temperature']
    feed = hidden['feed_ratio']
    filt = []
    for r in rows:
        try:
            T = float(r['T'])
            fr = r.get('feed_ratio','')
            tof = float(r['TOF'])
        except:
            continue
        if abs(T - T_target) <= 1.0 and fr.strip() == feed:
            if tof <= 0:
                continue
            filt.append(tof)
    if not filt:
        return 0.0
    log10s = [math.log10(t) for t in filt]
    mean_log10 = sum(log10s)/len(log10s)
    score_log10 = max(0.0, 1.0 - abs(mean_log10 - hidden['gold_mean_log10_TOF'])/hidden['tolerance_log10'])

    # Compute E_app using two temperatures (550 K and 750 K)
    T1 = 550.0
    T2 = 750.0
    sample_groups = {}
    for r in rows:
        try:
            T = float(r['T'])
            sid = int(r['sample_id'])
            tof = float(r['TOF'])
            fr = r.get('feed_ratio','')
        except:
            continue
        if fr.strip() != feed:
            continue
        if tof <= 0:
            continue
        if abs(T - T1) <= 1.0 or abs(T - T2) <= 1.0:
            sample_groups.setdefault(sid, {})[T] = tof
    Ea_list = []
    for sid, tdict in sample_groups.items():
        if T1 in tdict and T2 in tdict:
            tof1 = tdict[T1]
            tof2 = tdict[T2]
            log10_1 = math.log10(tof1)
            log10_2 = math.log10(tof2)
            slope = (log10_2 - log10_1) / (1.0/T2 - 1.0/T1)
            Ea = -slope * 0.004574  # R*ln(10) in kcal/mol K
            Ea_list.append(Ea)
    if not Ea_list:
        score_Eapp = 0.0
    else:
        mean_Eapp = sum(Ea_list)/len(Ea_list)
        score_Eapp = max(0.0, 1.0 - abs(mean_Eapp - hidden['gold_mean_E_app_kcal_per_mol'])/hidden['tolerance_E_app'])
    return 0.5 * score_log10 + 0.5 * score_Eapp


# === block: score_2 (check id='aggregated_stats') ===
def score_2(artifact, step, ctx):
    raw_rows = ctx.get('raw_artifact','')
    if raw_rows is None:
        raw_rows = []
    if not isinstance(artifact, dict):
        return 0.0
    hidden = ctx['steps']['aggregated_stats']['hidden']

    # recompute TOF and E_app from raw CSV
    # (same as raw_mkm but using separate load)
    # We'll use the same raw_rows passed via ctx if available
    raw_csv = load_artifact('/app/outputs/ethane_odh_perturbed_results.csv')
    if raw_csv is None:
        score_tof_cons = 0.0
        score_eapp_cons = 0.0
    else:
        # recompute mean log10 TOF at 750K
        T_target = 750.0
        feed = '1:0.5'
        filt_tof = []
        for r in raw_csv:
            try:
                T = float(r['T'])
                fr = r.get('feed_ratio','')
                tof = float(r['TOF'])
            except:
                continue
            if abs(T - T_target) <= 1.0 and fr.strip() == feed and tof > 0:
                filt_tof.append(tof)
        if filt_tof:
            comp_mean_log10 = sum(math.log10(t) for t in filt_tof)/len(filt_tof)
        else:
            comp_mean_log10 = None
        # recompute E_app from 550/750K
        T1 = 550.0
        T2 = 750.0
        sample_groups = {}
        for r in raw_csv:
            try:
                T = float(r['T'])
                sid = int(r['sample_id'])
                tof = float(r['TOF'])
                fr = r.get('feed_ratio','')
            except:
                continue
            if fr.strip() != feed or tof <= 0:
                continue
            if abs(T - T1) <= 1.0 or abs(T - T2) <= 1.0:
                sample_groups.setdefault(sid, {})[T] = tof
        Ea_list = []
        for sid, tdict in sample_groups.items():
            if T1 in tdict and T2 in tdict:
                log10_1 = math.log10(tdict[T1])
                log10_2 = math.log10(tdict[T2])
                slope = (log10_2 - log10_1) / (1.0/T2 - 1.0/T1)
                Ea = -slope * 0.004574
                Ea_list.append(Ea)
        comp_mean_Eapp = sum(Ea_list)/len(Ea_list) if Ea_list else None

        # consistency with reported
        reported_tof = artifact.get('TOF',{}).get('mean_log10')
        reported_Eapp = artifact.get('E_app',{}).get('mean_kcal_per_mol')
        score_tof_cons = 1.0 if (comp_mean_log10 is not None and reported_tof is not None and abs(reported_tof - comp_mean_log10) < hidden['tolerance_log10_consistency']) else 0.0
        score_eapp_cons = 1.0 if (comp_mean_Eapp is not None and reported_Eapp is not None and abs(reported_Eapp - comp_mean_Eapp) < hidden['tolerance_E_app_consistency']) else 0.0

    # reaction orders verification
    ro_c2h6 = artifact.get('reaction_order_C2H6',{}).get('mean')
    ro_o2 = artifact.get('reaction_order_O2',{}).get('mean')
    if ro_c2h6 is not None and abs(ro_c2h6 - hidden['gold_reaction_order_C2H6']) < hidden['tol_reaction_order_C2H6']:
        score_order_c2h6 = 1.0
    else:
        score_order_c2h6 = 0.0
    if ro_o2 is not None and abs(ro_o2 - hidden['gold_reaction_order_O2']) < hidden['tol_reaction_order_O2']:
        score_order_o2 = 1.0
    else:
        score_order_o2 = 0.0

    score_order = 0.5 * (score_order_c2h6 + score_order_o2)
    score = (score_tof_cons + score_eapp_cons + score_order) / 3.0
    return score


_SCORERS = {
    'ga_covariance_matrix': score_0,
    'raw_mkm_results': score_1,
    'aggregated_stats': score_2,
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
