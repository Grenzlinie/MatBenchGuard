import os
import json
import csv

# === author imports / helpers ===
import json, os, math


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
    def prepare(outputs_dir, spec):
        ctx = {'outputs_dir': outputs_dir}
        for step in spec.get('steps', []):
            pass
        return ctx


# === block: score_0 (check id='gas_adsorption') ===
def score_0(artifact, step, ctx):
        gold_data = step.get('gold', {})
        if not isinstance(gold_data, dict):
            return 0.0
        tolerance = step.get('energy_tolerance', 0.10)
        if not isinstance(tolerance, (int, float)):
            tolerance = 0.10

        expected_configs = {
            'Pt': ["II-Bri-A1","I-Bri-A2","II-Fcc-B1","II-Hcp-B1","I-Fcc-B1","I-Hcp-B1","I-Fcc-A2"],
            'Pd': ["II-Bri-A2","I-Bri-A2","II-Fcc-B1","II-Hcp-B1","I-Fcc-B1","I-Hcp-B1","I-Hcp-A2"]
        }

        if not isinstance(artifact, list):
            return 0.0

        agent_energies = {}
        for entry in artifact:
            if not isinstance(entry, dict):
                continue
            metal = str(entry.get('metal', '')).strip()
            cfg = str(entry.get('configuration_name', '')).strip()
            e = entry.get('E_ad_vac')
            if isinstance(e, (int, float)):
                agent_energies[(metal, cfg)] = float(e)

        metal_scores = []
        for metal in ['Pt', 'Pd']:
            configs = expected_configs.get(metal, [])
            if not configs:
                continue
            present = 0
            values = {}
            for cfg in configs:
                e_agent = agent_energies.get((metal, cfg))
                e_gold = gold_data.get(metal, {}).get(cfg)
                if e_agent is None or e_gold is None:
                    continue
                if not isinstance(e_agent, (int, float)) or not isinstance(e_gold, (int, float)):
                    continue
                if abs(e_agent - e_gold) <= tolerance:
                    present += 1
                    values[cfg] = e_agent

            total_expected = len(configs)
            score_present = present / total_expected if total_expected > 0 else 1.0

            bridge_cfgs = [c for c in configs if 'Bri' in c]
            fcc_cfgs = [c for c in configs if 'Fcc' in c]
            hcp_cfgs = [c for c in configs if 'Hcp' in c]

            bridge_ok = True
            if bridge_cfgs and fcc_cfgs and hcp_cfgs:
                b_vals = [values[c] for c in bridge_cfgs if c in values]
                f_vals = [values[c] for c in fcc_cfgs if c in values]
                h_vals = [values[c] for c in hcp_cfgs if c in values]
                if b_vals and f_vals and h_vals:
                    min_bridge = min(b_vals)
                    min_fcc = min(f_vals)
                    min_hcp = min(h_vals)
                    if not (min_bridge <= min_fcc and min_bridge <= min_hcp):
                        bridge_ok = False
                    if not (min_fcc <= min_hcp):
                        bridge_ok = False
                else:
                    bridge_ok = True
            else:
                bridge_ok = True

            fcc_hcp_ok = True
            if fcc_cfgs and hcp_cfgs:
                f_vals = [values[c] for c in fcc_cfgs if c in values]
                h_vals = [values[c] for c in hcp_cfgs if c in values]
                if f_vals and h_vals:
                    min_f = min(f_vals)
                    min_h = min(h_vals)
                    if min_f > min_h:  # fcc should be more stable (more negative)
                        fcc_hcp_ok = False

            order_score = 0.5 * bridge_ok + 0.5 * fcc_hcp_ok
            metal_score = 0.6 * score_present + 0.4 * order_score
            metal_scores.append(metal_score)

        if not metal_scores:
            return 0.0
        return float(sum(metal_scores)) / len(metal_scores)


# === block: score_1 (check id='gas_structural') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold_data = step.get('gold', {})
        len_tols = step.get('length_tolerances', {'bond':0.03,'metal':0.05})
        ang_tol = step.get('angle_tolerance', 3.0)
        # classify parameters
        bond_params = ['r_C1','r_C2','r_CM1','r_CM2','r_CM3']  # r_CM are metal-carbon bonds? Use bond tolerance
        metal_params = ['d_zmin','d_zavg','r_M1','r_M2']
        angle_params = ['theta1','theta2','alpha','beta']
        metals = ['Pt','Pd']
        total_fields = 0
        passed_fields = 0
        for metal in metals:
            gold_metal = gold_data.get(metal, {})
            agent_metal = artifact.get(metal, {}) if isinstance(artifact, dict) else {}
            for param in gold_metal:
                if param not in agent_metal:
                    continue
                total_fields += 1
                agent_val = agent_metal[param]
                gold_val = gold_metal[param]
                if not isinstance(agent_val, (int,float)):
                    continue
                if param in bond_params:
                    tol = len_tols.get('bond', 0.03)
                elif param in metal_params:
                    tol = len_tols.get('metal', 0.05)
                elif param in angle_params:
                    tol = ang_tol
                else:
                    tol = len_tols.get('bond', 0.03)  # fallback
                if abs(agent_val - gold_val) <= tol:
                    passed_fields += 1
        if total_fields == 0:
            return 0.0
        return passed_fields / total_fields


# === block: score_2 (check id='aqueous') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold_data = step.get('gold', {})
        e_tol = step.get('energy_tolerance', 0.10)
        len_tols = step.get('length_tolerances', {'bond':0.03,'metal':0.05})
        ang_tol = step.get('angle_tolerance', 3.0)
        bond_params = ['r_C1','r_C2','r_CM1','r_CM2','r_CM3']
        metal_params = ['d_zmin','d_zavg','r_M1','r_M2']
        angle_params = ['theta1','theta2','alpha','beta']
        metals = ['Pt','Pd']
        total_checks = 0
        passed_checks = 0
        for metal in metals:
            gold_metal = gold_data.get(metal, {})
            agent_metal = artifact.get(metal, {}) if isinstance(artifact, dict) else {}
            # energy check
            key_e = 'E_ad_aquo_0K'
            if key_e in gold_metal and key_e in agent_metal:
                total_checks += 1
                if abs(agent_metal[key_e] - gold_metal[key_e]) <= e_tol:
                    passed_checks += 1
            for param in gold_metal:
                if param == key_e:
                    continue
                if param not in agent_metal:
                    continue
                total_checks += 1
                agent_val = agent_metal[param]
                gold_val = gold_metal[param]
                if not isinstance(agent_val, (int,float)):
                    continue
                if param in bond_params:
                    tol = len_tols.get('bond', 0.03)
                elif param in metal_params:
                    tol = len_tols.get('metal', 0.05)
                elif param in angle_params:
                    tol = ang_tol
                else:
                    tol = 0.05
                if abs(agent_val - gold_val) <= tol:
                    passed_checks += 1
        if total_checks == 0:
            return 0.0
        return passed_checks / total_checks


# === block: score_3 (check id='solvent_reduction') ===
def score_3(artifact, step, ctx):
    def score(artifact, step, ctx):
        output_dir = ctx.get('outputs_dir', '/app/outputs')
        lo, hi = step.get('reduction_range', [20.0, 25.0])
        # load gas energies
        gas_path = os.path.join(output_dir, 'step_01_adsorption_energies_gas.json')
        aq_path = os.path.join(output_dir, 'step_03_aqueous_0K_results.json')
        def load_json(p):
            if not os.path.exists(p):
                return None
            with open(p) as f:
                return json.load(f)
        gas = load_json(gas_path)
        aq = load_json(aq_path)
        if gas is None or aq is None:
            return 0.0
        # extract most stable bridge energies per metal
        gas_map = {}
        if isinstance(gas, list):
            for item in gas:
                if isinstance(item, dict) and 'metal' in item and 'configuration_name' in item and 'E_ad_vac' in item:
                    gas_map[(item['metal'], item['configuration_name'])] = item['E_ad_vac']
        aq_map = {}
        if isinstance(aq, dict):
            for metal in ['Pt','Pd']:
                obj = aq.get(metal, {})
                if isinstance(obj, dict) and 'E_ad_aquo_0K' in obj:
                    aq_map[metal] = obj['E_ad_aquo_0K']
        bridge_cfgs = {'Pt': 'II-Bri-A1', 'Pd': 'II-Bri-A2'}
        ok = 0
        for metal in ['Pt','Pd']:
            cfg = bridge_cfgs[metal]
            e_gas = gas_map.get((metal, cfg))
            e_aq = aq_map.get(metal)
            if e_gas is None or e_aq is None:
                continue
            if e_gas >= 0:
                continue
            reduction = (e_gas - e_aq) / abs(e_gas) * 100.0
            if lo <= reduction <= hi:
                ok += 1
        if ok == 2:
            return 1.0
        elif ok == 1:
            return 0.5
        return 0.0


_SCORERS = {
    'gas_adsorption': score_0,
    'gas_structural': score_1,
    'aqueous': score_2,
    'solvent_reduction': score_3,
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
