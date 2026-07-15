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
        for step in spec.get('steps', []):
            if step.get('id') == 'cohesive_energy_checks':
                return {'ef_mgga_minus': step.get('hidden_reference_Ef_MgGa_minus', 1.36)}
        return {'ef_mgga_minus': 1.36}


# === block: score_0 (check id='cohesive_energy_checks') ===
def score_0(artifact, step, ctx):
        import math
        energies = {}
        for row in artifact:
            try:
                sys = row.get('system')
                val_str = row.get('cohesive_energy_eV')
                if sys is None or val_str is None:
                    continue
                val = float(val_str)
            except (TypeError, ValueError):
                continue
            energies[sys] = val

        required_systems = [
            'bulk_GaN', 'bulk_Ga', 'N2', 'Mg3N2',
            'type_I_NI_+3', 'type_II_NI_+3',
            'type_I_NI_+2', 'type_II_NI_+2',
            'type_I_NI_+1', 'type_II_NI_+1',
            'type_I_NI_0', 'type_II_NI_0',
            'type_I_NI_-1', 'type_II_NI_-1',
            'channel_NI_-3',
            'MgGaN_I_a_+2', 'MgGaN_I_b_+2', 'MgGaN_I_c_+2',
            'MgGaN_I_d_+2', 'MgGaN_I_e_+2', 'MgGaN_I_f_+2',
            'MgGaN_I_a_+1', 'MgGaN_I_b_+1', 'MgGaN_I_c_+1',
            'MgGaN_I_d_+1', 'MgGaN_I_e_+1', 'MgGaN_I_f_+1',
            'MgGaN_I_a_0', 'MgGaN_I_b_0', 'MgGaN_I_c_0',
            'MgGaN_I_d_0', 'MgGaN_I_e_0', 'MgGaN_I_f_0'
        ]
        if not all(k in energies for k in required_systems):
            return 0.0

        mu_Ga = -energies['bulk_Ga']
        mu_N = -(energies['bulk_GaN'] - energies['bulk_Ga'])
        mu_Mg = -(energies['Mg3N2'] - 2*(energies['bulk_GaN'] - energies['bulk_Ga'])) / 3.0

        def ef0_NI(sys):
            return -energies[sys] - (36*mu_Ga + 37*mu_N)

        def ef0_complex(sys):
            return -energies[sys] - (35*mu_Ga + 37*mu_N + 1*mu_Mg)

        checks = {}
        charge_list = ['+3','+2','+1','0','-1']
        eps = 1e-12
        for q in charge_list:
            ti = f'type_I_NI_{q}'
            tii = f'type_II_NI_{q}'
            checks[f'type_I_vs_II_{q}'] = (ef0_NI(ti) < ef0_NI(tii) - eps)

        order_I = [ef0_NI(f'type_I_NI_{q}') for q in charge_list]
        for i in range(len(order_I)-1):
            checks[f'type_I_order_{charge_list[i]}_{charge_list[i+1]}'] = (order_I[i] < order_I[i+1] - eps)

        order_II = [ef0_NI(f'type_II_NI_{q}') for q in charge_list]
        for i in range(len(order_II)-1):
            checks[f'type_II_order_{charge_list[i]}_{charge_list[i+1]}'] = (order_II[i] < order_II[i+1] - eps)

        checks['channel_gt_typeI_0_at_E0'] = (ef0_NI('channel_NI_-3') > ef0_NI('type_I_NI_0') + eps)

        ef_channel_E3p48 = ef0_NI('channel_NI_-3') - 3*3.48
        ef_typeI0_E3p48 = ef0_NI('type_I_NI_0')
        checks['channel_lt_typeI_0_at_E3p48'] = (ef_channel_E3p48 < ef_typeI0_E3p48 - eps)

        all_NI_ef0 = [ef0_NI(sys) for sys in required_systems if sys.startswith('type_') or sys.startswith('channel_')]
        max_ef0 = max(all_NI_ef0)
        checks['channel_highest'] = (ef0_NI('channel_NI_-3') >= max_ef0 - eps)

        ef_mgga = ctx['ef_mgga_minus']
        complex_binding = {}
        for sys in required_systems:
            if not sys.startswith('MgGaN_I_'):
                continue
            parts = sys.split('_')
            charge_str = parts[-1]
            charge_val = int(charge_str)
            target_charge = charge_val + 1
            if target_charge == 3: tq = '+3'
            elif target_charge == 2: tq = '+2'
            elif target_charge == 1: tq = '+1'
            elif target_charge == 0: tq = '0'
            elif target_charge == -1: tq = '-1'
            else: continue
            if parts[2] in ('a','b','c'):
                nisys = f'type_I_NI_{tq}'
            else:
                nisys = f'type_II_NI_{tq}'
            if nisys not in energies:
                continue
            eb = ef_mgga + ef0_NI(nisys) - ef0_complex(sys)
            qkey = f'+{charge_val}' if charge_val>0 else str(charge_val)
            complex_binding.setdefault(qkey, []).append(eb)

        for q in ('+2','+1','0'):
            if q in complex_binding and len(complex_binding[q])>0:
                max_eb = max(complex_binding[q])
                checks[f'binding_pos_{q}'] = max_eb > eps
            else:
                checks[f'binding_pos_{q}'] = False

        if '+2' in complex_binding and '+1' in complex_binding and '0' in complex_binding:
            max2 = max(complex_binding['+2'])
            max1 = max(complex_binding['+1'])
            max0 = max(complex_binding['0'])
            checks['binding_order_2_gt_1'] = max2 > max1 + eps
            checks['binding_order_1_gt_0'] = max1 > max0 + eps
        else:
            checks['binding_order_2_gt_1'] = False
            checks['binding_order_1_gt_0'] = False

        all_eb = [eb for lst in complex_binding.values() for eb in lst]
        checks['binding_all_plaus'] = all(eb < 2.0 for eb in all_eb) if all_eb else True

        pos_checks = [ef0_NI(sys) > 0 for sys in required_systems if sys.startswith('type_') or sys.startswith('channel_')]
        checks['all_positive'] = all(pos_checks) and len(pos_checks)>0

        weights = {
            'type_I_vs_II_+3': 0.02, 'type_I_vs_II_+2': 0.02, 'type_I_vs_II_+1': 0.02, 'type_I_vs_II_0': 0.02, 'type_I_vs_II_-1': 0.02,
            'type_I_order_+2_+1': 0.02, 'type_I_order_+1_0': 0.02, 'type_I_order_0_-1': 0.02, 'type_I_order_+3_+2': 0.02,
            'type_II_order_+2_+1': 0.02, 'type_II_order_+1_0': 0.02, 'type_II_order_0_-1': 0.02, 'type_II_order_+3_+2': 0.02,
            'channel_gt_typeI_0_at_E0': 0.04,
            'channel_lt_typeI_0_at_E3p48': 0.04,
            'channel_highest': 0.04,
            'binding_pos_+2': 0.05, 'binding_pos_+1': 0.05, 'binding_pos_0': 0.05,
            'binding_order_2_gt_1': 0.05, 'binding_order_1_gt_0': 0.05,
            'binding_all_plaus': 0.02,
            'all_positive': 0.02
        }
        total_weight = sum(weights.values())
        score = sum(checks.get(k, False)*w for k,w in weights.items()) / total_weight if total_weight>0 else 0.0
        return score


_SCORERS = {
    'cohesive_energy_checks': score_0,
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
