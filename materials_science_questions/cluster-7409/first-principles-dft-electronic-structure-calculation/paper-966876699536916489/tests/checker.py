import os
import json
import csv

# === author imports / helpers ===
import math, json


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


# === block: score_0 (check id='check_electronic_summary') ===
def score_0(artifact, step, ctx):
    try:
        data = artifact
        if not isinstance(data, dict):
            return 0.0
        gold = step['gold']
        tol_bg = step.get('tolerance_bandgap', 0.2)
        tol_mid = step.get('tolerance_midgap_energy', 0.2)
        def score_val(actual, target, tol, max_dev):
            delta = abs(actual - target)
            if delta <= tol:
                return 1.0
            return max(0.0, 1.0 - (delta - tol) / (max_dev - tol))
        max_dev_bg = 0.5
        s_pbe = score_val(data['bandgap_PBEpU'], gold['bandgap_PBEpU'], tol_bg, max_dev_bg)
        s_hse = score_val(data['bandgap_HSEscaled'], gold['bandgap_HSEscaled'], tol_bg, max_dev_bg)
        bg_score = (s_pbe + s_hse) / 2.0
        midgap = data.get('midgap_states', [])
        def match_states(agent_list, gold_list, tol):
            agent_by_label = {}
            for entry in agent_list:
                key = (entry.get('spin'), entry.get('state_label', ''))
                agent_by_label[key] = entry
            n = len(gold_list)
            if n == 0:
                return 1.0
            hits = 0
            for g in gold_list:
                key = (g['spin'], g['state_label'])
                if key in agent_by_label:
                    e = agent_by_label[key].get('energy_rel_VBM', 0)
                    occ = agent_by_label[key].get('occupied', False)
                    delta = abs(e - g['energy_rel_VBM'])
                    if delta <= tol and occ:
                        hits += 1
            return hits / n
        spin_up_gold = [{'spin': 'up', 'state_label': s['state_label'], 'energy_rel_VBM': s['energy_rel_VBM']} for s in gold['midgap_states_spin_up']]
        spin_down_gold = [{'spin': 'down', 'state_label': s['state_label'], 'energy_rel_VBM': s['energy_rel_VBM']} for s in gold['midgap_states_spin_down']]
        all_gold = spin_up_gold + spin_down_gold
        mid_score = match_states(midgap, all_gold, tol_mid)
        final_score = 0.4 * bg_score + 0.6 * mid_score
        return min(1.0, max(0.0, final_score))
    except Exception:
        return 0.0


# === block: score_1 (check id='check_table1_energy_nac') ===
def score_1(artifact, step, ctx):
    try:
        rows = artifact
        gold_rows = step['gold_rows']
        tol_e = step.get('tolerance_relative_energy', 0.05)
        tol_n = step.get('tolerance_relative_nac', 0.05)
        gold_by_orb = {r['orbitals']: r for r in gold_rows}
        total = 0.0
        count = 0
        for row in rows:
            orb = row.get('orbitals')
            if orb not in gold_by_orb:
                continue
            gr = gold_by_orb[orb]
            for col, target in [('energy', gr.get('energy')), ('scaled_energy', gr.get('scaled_energy')), ('NAC', gr.get('NAC')), ('scaled_NAC', gr.get('scaled_NAC'))]:
                val = row.get(col)
                if val is None:
                    continue
                try:
                    val_f = float(val)
                except:
                    continue
                target_f = float(target) if target is not None else None
                if target_f is None or target_f == 0:
                    continue
                rel_err = abs(val_f - target_f) / abs(target_f)
                if 'energy' in col:
                    if rel_err <= tol_e:
                        total += 1.0
                    else:
                        exceed = rel_err - tol_e
                        total += max(0.0, 1.0 - exceed / (tol_e * 2))
                else:
                    if rel_err <= tol_n:
                        total += 1.0
                    else:
                        exceed = rel_err - tol_n
                        total += max(0.0, 1.0 - exceed / (tol_n * 2))
                count += 1
        if count == 0:
            return 0.0
        score = total / count
        return min(1.0, max(0.0, score))
    except Exception:
        return 0.0


# === block: score_2 (check id='check_table2_timescales') ===
def score_2(artifact, step, ctx):
    try:
        rows = artifact
        gold_rows = step['gold_rows']
        factor = step.get('tolerance_factor', 2.0)
        gold_map = {(r['spin'], r['process']): r for r in gold_rows}
        n = len(gold_rows)
        if n == 0:
            return 0.0
        agent_map = {(r.get('spin'), r.get('process')): r for r in rows}
        ts_score = 0.0
        for (spin, proc), gr in gold_map.items():
            ar = agent_map.get((spin, proc))
            if ar is None:
                continue
            ts_agent = ar.get('timescale_ps')
            if ts_agent is None:
                continue
            try:
                ts_agent = float(ts_agent)
            except:
                continue
            ts_gold = float(gr['timescale_ps'])
            if ts_gold == 0:
                ts_gold = 1e-6
            ratio = ts_agent / ts_gold
            if 1.0 / factor <= ratio <= factor:
                ts_score += 1.0
            else:
                if 1.0 / (factor * 2) <= ratio <= factor * 2:
                    ts_score += 0.5
                else:
                    ts_score += 0.0
        if n > 0:
            ts_score = ts_score / n
        trend1 = 0.0
        trend2 = 0.0
        spin_down_es = agent_map.get(('down', 'ES_decay'))
        spin_up_es = agent_map.get(('up', 'ES_decay'))
        spin_down_trap = agent_map.get(('down', 'trapped_hole_rise'))
        spin_down_gs = agent_map.get(('down', 'GS_rise'))
        if spin_down_es and spin_up_es:
            try:
                if float(spin_down_es['timescale_ps']) < float(spin_up_es['timescale_ps']):
                    trend1 = 1.0
            except:
                pass
        if spin_down_trap and spin_down_gs:
            try:
                trap_val = float(spin_down_trap['timescale_ps'])
                gs_val = float(spin_down_gs['timescale_ps'])
                if gs_val > 5 * trap_val and gs_val > 0:
                    trend2 = 1.0
            except:
                pass
        score = 0.7 * ts_score + 0.15 * trend1 + 0.15 * trend2
        return min(1.0, max(0.0, score))
    except Exception:
        return 0.0


_SCORERS = {
    'check_electronic_summary': score_0,
    'check_table1_energy_nac': score_1,
    'check_table2_timescales': score_2,
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
