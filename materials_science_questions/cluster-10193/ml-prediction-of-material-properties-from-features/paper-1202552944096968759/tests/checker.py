import os
import json
import csv

# === author imports / helpers ===
import os, json, csv, math


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


# === block: score_0 (check id='step_04_metrics') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not isinstance(artifact, dict):
            return 0.0
        gold = step.get('config', {}).get('gold', {})
        if not isinstance(gold, dict):
            return 0.0
        props = ['surface_tension', 'viscosity', 'ionic_conductivity', 'density', 'melting_temperature', 'toxicity', 'water_activity']
        scores = []
        for prop in props:
            if prop not in artifact:
                scores.append(0.0)
                continue
            d = artifact.get(prop)
            if not isinstance(d, dict):
                scores.append(0.0)
                continue
            r2_raw = d.get('test_R2')
            if r2_raw is None:
                scores.append(0.0)
                continue
            try:
                r2 = float(r2_raw)
            except (TypeError, ValueError):
                scores.append(0.0)
                continue
            rmse_raw = d.get('test_RMSE')
            if rmse_raw is None:
                scores.append(0.0)
                continue
            try:
                rmse = float(rmse_raw)
            except (TypeError, ValueError):
                scores.append(0.0)
                continue
            gr = gold.get(prop)
            if not isinstance(gr, dict):
                scores.append(0.0)
                continue
            gr2 = gr.get('R2')
            grmse = gr.get('RMSE')
            if gr2 is None or grmse is None:
                scores.append(0.0)
                continue
            try:
                gr2 = float(gr2)
                grmse = float(grmse)
            except (TypeError, ValueError):
                scores.append(0.0)
                continue
            if r2 >= gr2 - 0.005:
                r2_s = 1.0
            elif r2 >= gr2 - 0.01:
                r2_s = 0.9
            elif r2 >= gr2 - 0.02:
                r2_s = 0.6
            elif r2 >= gr2 - 0.04:
                r2_s = 0.3
            else:
                r2_s = 0.0
            if rmse <= grmse * 1.01:
                r_s = 1.0
            elif rmse <= grmse * 1.05:
                r_s = 0.9
            elif rmse <= grmse * 1.1:
                r_s = 0.6
            elif rmse <= grmse * 1.2:
                r_s = 0.3
            else:
                r_s = 0.0
            scores.append((r2_s + r_s) / 2.0)
        if 'melting_temperature' in artifact:
            m_d = artifact.get('melting_temperature')
            if isinstance(m_d, dict) and 'test_accuracy' in m_d:
                acc_raw = m_d['test_accuracy']
                if acc_raw is not None:
                    try:
                        acc = float(acc_raw)
                    except (TypeError, ValueError):
                        acc = None
                    if acc is not None:
                        gacc_raw = gold.get('melting_temperature', {}).get('test_accuracy')
                        if gacc_raw is None:
                            gacc = 0.844
                        else:
                            try:
                                gacc = float(gacc_raw)
                            except (TypeError, ValueError):
                                gacc = 0.844
                        if acc >= gacc - 0.005:
                            a_s = 1.0
                        elif acc >= gacc - 0.01:
                            a_s = 0.9
                        elif acc >= gacc - 0.02:
                            a_s = 0.6
                        else:
                            a_s = 0.0
                        idx = props.index('melting_temperature')
                        if idx < len(scores):
                            existing = scores[idx]
                            r2_s_val = existing * 2.0 if existing is not None else 0.0
                            scores[idx] = (r2_s_val + existing * 2.0 + a_s) / 3.0
        return sum(scores) / len(scores) if scores else 0.0


# === block: score_1 (check id='step_07_counts') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        import os, csv
        pred_path = '/app/outputs/predicted_properties.csv'
        if not os.path.exists(pred_path):
            return 0.0
        criteria = step['config']['criteria']
        with open(pred_path, newline='') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        if not rows:
            return 0.0
        # try to find columns case-insensitively
        def col(name, haystack):
            for h in haystack:
                if h.lower() == name.lower():
                    return h
            return None
        cols = reader.fieldnames
        ln_eta_k = col('ln_eta', cols) or col('predicted_ln_eta', cols)
        sigma_k = col('sigma', cols) or col('predicted_sigma', cols)
        kappa_k = col('kappa', cols) or col('predicted_kappa', cols)
        logEC50_k = col('logEC50', cols) or col('predicted_logEC50', cols)
        gamma_w_k = col('gamma_w', cols) or col('predicted_gamma_w', cols)
        SA_k = col('SA', cols) or col('predicted_SA', cols)
        Tm_k = col('Tm', cols) or col('predicted_Tm', cols)
        if not all([ln_eta_k, sigma_k, kappa_k, gamma_w_k, SA_k, Tm_k]):
            return 0.0
        def is_liquid(v):
            v = str(v).strip().lower()
            return v == 'liquid' or v == 'true' or v == '1'
        co2_count = 0
        bat_count = 0
        for r in rows:
            try:
                ln = float(r[ln_eta_k])
                sigma = float(r[sigma_k])
                kappa = float(r[kappa_k])
                gw = float(r[gamma_w_k])
                sa = float(r[SA_k])
                liquid = is_liquid(r[Tm_k])
            except (ValueError, KeyError):
                continue
            if (ln < criteria['co2']['ln_eta_max'] and sigma < criteria['co2']['sigma_max'] and
                kappa >= criteria['co2']['kappa_min'] and kappa <= criteria['co2']['kappa_max'] and
                gw <= 1.0 and sa < criteria['co2']['SA_max'] and liquid):
                co2_count += 1
            if (kappa > criteria['battery']['kappa_min'] and ln < criteria['battery']['ln_eta_max'] and
                float(r.get(logEC50_k, 0.0)) > criteria['battery']['logEC50_min'] and
                sa < criteria['battery']['SA_max'] and liquid):
                bat_count += 1
        reported_co2 = int(artifact.get('co2_capture', -1))
        reported_bat = int(artifact.get('battery_electrolyte', -1))
        return 1.0 if (reported_co2 == co2_count and reported_bat == bat_count) else 0.0


# === block: score_2 (check id='step_07_top') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        import os, csv
        pred_path = '/app/outputs/predicted_properties.csv'
        if not os.path.exists(pred_path):
            return 0.0
        with open(pred_path, newline='') as f:
            reader = csv.DictReader(f)
            pred_rows = list(reader)
        pred_by_smiles = {}
        if pred_rows:
            # normalize column names
            smi_col = None
            for col in pred_rows[0].keys():
                if col.lower() == 'smiles':
                    smi_col = col
                    break
            if smi_col:
                pred_by_smiles = {r[smi_col]: r for r in pred_rows}
        rows_ok = 0
        total = len(artifact)
        if total == 0:
            return 0.0
        app_count = {'co2': 0, 'battery': 0}
        for row in artifact:
            app = row.get('application','').strip().lower()
            if app not in ('co2','battery'):
                continue
            passed = str(row.get('passed','')).strip().lower() == 'true'
            if not passed:
                continue
            smiles = row.get('SMILES','')
            pred_match = pred_by_smiles.get(smiles)
            if not pred_match:
                continue
            # check consistency of values within small tolerance
            try:
                ln = float(row.get('predicted_ln_eta',math.nan))
                sigma = float(row.get('predicted_sigma',math.nan))
                kappa = float(row.get('predicted_kappa',math.nan))
                lnec = float(row.get('predicted_logEC50',math.nan))
                gw = float(row.get('predicted_gamma_w',math.nan))
                sa = float(row.get('predicted_SA',math.nan))
                tm = row.get('predicted_Tm','')
                p_ln = float(pred_match.get('ln_eta', pred_match.get('predicted_ln_eta', math.nan)))
                p_sigma = float(pred_match.get('sigma', pred_match.get('predicted_sigma', math.nan)))
                p_kappa = float(pred_match.get('kappa', pred_match.get('predicted_kappa', math.nan)))
                p_lnec = float(pred_match.get('logEC50', pred_match.get('predicted_logEC50', math.nan)))
                p_gw = float(pred_match.get('gamma_w', pred_match.get('predicted_gamma_w', math.nan)))
                p_sa = float(pred_match.get('SA', pred_match.get('predicted_SA', math.nan)))
                ok = (abs(ln-p_ln)<0.01 and abs(sigma-p_sigma)<0.01 and abs(kappa-p_kappa)<0.01 and
                      abs(lnec-p_lnec)<0.01 and abs(gw-p_gw)<0.01 and abs(sa-p_sa)<0.01)
                if ok:
                    rows_ok += 1
                    app_count[app] = app_count.get(app,0) + 1
            except (ValueError, KeyError, TypeError):
                pass
        # must have at least 5 for each application
        if app_count.get('co2',0) < 5 or app_count.get('battery',0) < 5:
            return 0.0
        return rows_ok / total if total else 0.0


_SCORERS = {
    'step_04_metrics': score_0,
    'step_07_counts': score_1,
    'step_07_top': score_2,
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
