import os
import json
import csv

# === author imports / helpers ===
import math


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
    gold_ref = spec['steps'][0].get('gold', {})
    return {'gold': gold_ref}


# === block: score_0 (check id='results') ===
def score_0(artifact, step, ctx):
        def _score_value(val, gold, rel_tol, abs_tol=1e-6):
            if gold == 0:
                return 1.0 if abs(val) <= abs_tol else 0.0
            err = abs(val - gold) / max(abs(gold), 1.0)
            if err <= rel_tol:
                return 1.0
            elif err > 2*rel_tol:
                return 0.0
            else:
                return 1.0 - (err - rel_tol) / rel_tol

        def _consistency_score(agent, C11, C12, C44):
            # recompute VRH
            B = (C11 + 2*C12) / 3.0
            Gv = (C11 - C12 + 3*C44) / 5.0
            denom = 4*C44 + 3*(C11 - C12)
            if denom == 0:
                return 0.0
            Gr = 5*(C11 - C12)*C44 / denom
            Bvrh = B
            Gvrh = 0.5*(Gv + Gr)
            Ev = 9*Bvrh*Gvrh / (3*Bvrh + Gvrh) if (3*Bvrh + Gvrh) != 0 else 0.0
            s = 1.0
            for key, gold_key in [('B_VRH',Bvrh),('G_VRH',Gvrh),('E',Ev)]:
                if key not in agent:
                    s -= 0.33
                    continue
                if gold_key is None:
                    continue
                a = agent[key]
                diff = abs(a - gold_key)
                thresh = max(0.01*abs(gold_key), 0.5)
                s -= 0.33 * min(1.0, diff / thresh)
            return max(0.0, min(1.0, s))

        gold = ctx.get('gold', {})
        if not isinstance(artifact, dict):
            return 0.0

        configs = ['pristine','V_O48f','Zr_Gd','Gd_int2','Zr_8a','O_8a']
        ec_keys = ['C11','C12','C44']
        mod_keys = ['B_VRH','G_VRH','E']
        debye_key = 'Debye_temperature'
        fe_key = 'formation_energy'

        # tolerances
        rel_tol_ec = 0.10  # elastic constants
        rel_tol_mod = 0.10
        rel_tol_debye = 0.15
        abs_tol_fe = 0.5

        scores = {}
        # value comparison
        for cat, keys, tol, weight in [
            ('elastic_constants', ec_keys, rel_tol_ec, 0.25),
            ('moduli', mod_keys, rel_tol_mod, 0.25),
            ('debye', [debye_key], rel_tol_debye, 0.15),
            ('formation_energy', [fe_key], None, 0.1)
        ]:
            vals = []
            for cfg in configs:
                agent_cfg = artifact.get(cfg, {})
                gold_cfg = gold.get(cfg, {})
                if not gold_cfg:
                    continue
                for k in keys:
                    if k not in gold_cfg:
                        continue
                    v = agent_cfg.get(k)
                    if v is None or not isinstance(v, (int, float)):
                        vals.append(0.0)
                        continue
                    g = gold_cfg[k]
                    if cat == 'formation_energy':
                        vals.append(1.0 if abs(v - g) <= abs_tol_fe else 0.0)
                    else:
                        vals.append(_score_value(v, g, tol))
            if vals:
                scores[cat] = sum(vals)/len(vals)
            else:
                scores[cat] = 0.0

        # consistency
        consistencies = []
        for cfg in configs:
            agent_cfg = artifact.get(cfg, {})
            if not all(k in agent_cfg for k in ec_keys):
                consistencies.append(0.0)
                continue
            try:
                c11 = float(agent_cfg['C11'])
                c12 = float(agent_cfg['C12'])
                c44 = float(agent_cfg['C44'])
                consistencies.append(_consistency_score(agent_cfg, c11, c12, c44))
            except:
                consistencies.append(0.0)
        scores['consistency'] = sum(consistencies)/len(consistencies) if consistencies else 0.0

        # mechanical stability
        stability = []
        for cfg in configs:
            agent_cfg = artifact.get(cfg, {})
            if not all(k in agent_cfg for k in ec_keys):
                stability.append(0.0)
                continue
            c11 = agent_cfg['C11']
            c12 = agent_cfg['C12']
            c44 = agent_cfg['C44']
            stable = (c11 + 2*c12 > 0) and (c44 > 0) and (c11 - c12 > 0)
            stability.append(1.0 if stable else 0.0)
        scores['stability'] = sum(stability)/len(stability) if stability else 0.0

        # ordering trend: G_VRH(Zr_8a) lowest, G_VRH(Gd_int2) second lowest
        ordering_ok = 1.0
        if 'Zr_8a' in artifact and 'Gd_int2' in artifact:
            g_gdint2 = artifact['Gd_int2'].get('G_VRH')
            g_zr8a = artifact['Zr_8a'].get('G_VRH')
            if g_gdint2 is not None and g_zr8a is not None:
                # Also get others
                others = []
                for cfg in ['pristine','V_O48f','Zr_Gd','O_8a']:
                    if cfg in artifact:
                        ov = artifact[cfg].get('G_VRH')
                        if ov is not None:
                            others.append(ov)
                if all(ov > g_gdint2 for ov in others) and g_gdint2 > g_zr8a:
                    ordering_ok = 1.0
                else:
                    ordering_ok = 0.0
            else:
                ordering_ok = 0.0
        else:
            ordering_ok = 0.0
        scores['ordering'] = ordering_ok

        weights = {'elastic_constants':0.25,'moduli':0.25,'debye':0.15,'formation_energy':0.10,
                   'consistency':0.15,'stability':0.05,'ordering':0.05}
        total = sum(weights[k]*scores.get(k,0.0) for k in weights)
        return min(1.0, max(0.0, total))


_SCORERS = {
    'results': score_0,
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
