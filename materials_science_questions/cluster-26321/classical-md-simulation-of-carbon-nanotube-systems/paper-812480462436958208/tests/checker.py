import os
import json
import csv

# === author imports / helpers ===
import math
from collections import defaultdict

class _NP:
    @staticmethod
    def sqrt(x):
        return math.sqrt(x)
    @staticmethod
    def mean(seq):
        return sum(seq) / len(seq) if seq else 0.0

np = _NP()


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


# === block: score_0 (check id='energy_profile_step') ===
def score_0(artifact, step, ctx):
    ref_energies = step.get('reference_energies', {})
    rmse_full = step.get('rmse_full_credit', 3.0)
    rmse_zero = step.get('rmse_zero_credit', 10.0)
    agent_energies = {}
    for row in artifact:
        step_str = row.get('scan_step')
        energy_str = row.get('relative_energy_kcal_per_mol')
        if step_str is None or energy_str is None:
            continue
        try:
            step_num = int(step_str)
            energy = float(energy_str)
        except (ValueError, TypeError):
            continue
        agent_energies[step_num] = energy
    common_steps = set(ref_energies.keys()) & set(map(str, agent_energies.keys()))
    if not common_steps:
        result = 0.0
    else:
        errors = []
        for s in common_steps:
            ref = ref_energies[s]
            agent = agent_energies.get(int(s), None)
            if agent is not None:
                errors.append((agent - ref)**2)
        if not errors:
            rmse = 0.0
        else:
            rmse = np.sqrt(np.mean(errors))
        if rmse <= rmse_full:
            rmse_score = 1.0
        elif rmse >= rmse_zero:
            rmse_score = 0.0
        else:
            rmse_score = (rmse_zero - rmse) / (rmse_zero - rmse_full)
        max_step = max(agent_energies, key=lambda k: agent_energies[k]) if agent_energies else 0
        struct = 0.0
        if max_step == 7:
            struct += 0.5
        if 15 in agent_energies and 7 in agent_energies and agent_energies[15] < agent_energies[7]:
            struct += 0.3
        if 28 in agent_energies and 15 in agent_energies and agent_energies[28] > agent_energies[15]:
            struct += 0.2
        structural_score = min(1.0, struct)
        result = 0.6 * rmse_score + 0.4 * structural_score
    return result


# === block: score_1 (check id='results_json_step') ===
def score_1(artifact, step, ctx):
    gold = step.get('gold_values', {})
    tol = step.get('tolerances', {})
    w = step.get('weights_internal', {})
    def score_num(val, ref, tol_abs, decay=1.0):
        if val is None:
            return 0.0
        diff = abs(val - ref)
        if diff <= tol_abs:
            return 1.0
        elif diff >= tol_abs * (1 + decay):
            return 0.0
        else:
            return 1.0 - (diff - tol_abs) / (tol_abs * decay)

    score = 0.0
    for key in ['gas_phase_barrier','aqueous_barrier','activation_enthalpy','TdS','activation_free_energy','b3lyp_d3_barrier','m06x_6_31g_barrier','m06x_631g_d_barrier']:
        val = artifact.get(key, 0.0)
        g = gold.get(key, 0.0)
        t = tol.get('barrier_abs', 3.0) if 'barrier' in key else tol.get('thermo_abs', 3.0)
        score += w.get(key, 0.0) * score_num(val, g, t)

    raman_data = artifact.get('Raman_data', [])
    raman_ref = gold.get('Raman_ref', {})
    raman_score = 0.0
    n_raman = 0
    if isinstance(raman_data, list):
        for entry in raman_data:
            struct = entry.get('structure', '')
            if struct in raman_ref:
                ref = raman_ref[struct]
                n_raman += 1
                g_diff = abs(entry.get('G_freq', 0) - ref['G_freq'])
                d_diff = abs(entry.get('D_freq', 0) - ref['D_freq'])
                r_diff = abs(entry.get('G_D_ratio', 0) - ref['G_D_ratio'])
                sub = (score_num(g_diff, 0, tol['raman_freq_abs'], 0.5) +
                       score_num(d_diff, 0, tol['raman_freq_abs'], 0.5) +
                       score_num(r_diff, 0, tol['raman_ratio_abs'], 0.5)) / 3.0
                raman_score += sub
    if n_raman > 0:
        raman_score /= n_raman
    score += w.get('Raman', 0.0) * raman_score

    nmr_data = artifact.get('NMR_data', [])
    nmr_score = 0.0
    if isinstance(nmr_data, list) and len(nmr_data) > 0:
        struct_shifts = defaultdict(list)
        for entry in nmr_data:
            struct = entry.get('structure', '')
            try:
                shift = float(entry.get('chemical_shift', 0.0))
                struct_shifts[struct].append(shift)
            except:
                pass
        avg_shifts = {s: np.mean(v) for s, v in struct_shifts.items() if v}
        free_avg = avg_shifts.get('free cDDP', None)
        if free_avg is not None:
            cond1 = 1.0 if 3.5 <= free_avg <= 5.0 else 0.0
            complex_avg = avg_shifts.get('cDDP@CNTox', None)
            cond2 = 0.0
            if complex_avg is not None:
                cond2 = 1.0 if complex_avg < free_avg - 3.0 else 0.0
            cond3 = 0.0
            scan7_avg = avg_shifts.get('CNTox⇒cDDP(7)', None)
            scan11_avg = avg_shifts.get('CNTox⇒cDDP(11)', None)
            if scan7_avg is not None:
                if complex_avg is not None and scan7_avg > complex_avg and scan7_avg < free_avg + 2.0:
                    cond3 += 0.5
                elif complex_avg is not None and scan7_avg > complex_avg:
                    cond3 += 0.25
            if scan11_avg is not None:
                if complex_avg is not None and scan11_avg > complex_avg and scan11_avg < free_avg + 2.0:
                    cond3 += 0.5
                elif complex_avg is not None and scan11_avg > complex_avg:
                    cond3 += 0.25
            cond4 = 0.0
            scan15_avg = avg_shifts.get('CNTox⇒cDDP(15)', None)
            scan28_avg = avg_shifts.get('CNTox⇒cDDP(28)', None)
            if scan15_avg is not None:
                if abs(scan15_avg - free_avg) <= 1.0:
                    cond4 += 0.5
            if scan28_avg is not None:
                if abs(scan28_avg - free_avg) <= 1.0:
                    cond4 += 0.5
            nmr_score = (cond1 + cond2 + cond3 + cond4) / 4.0
        else:
            nmr_score = 0.0
    score += w.get('NMR', 0.0) * nmr_score
    result = min(1.0, max(0.0, score))


_SCORERS = {
    'energy_profile_step': score_0,
    'results_json_step': score_1,
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
