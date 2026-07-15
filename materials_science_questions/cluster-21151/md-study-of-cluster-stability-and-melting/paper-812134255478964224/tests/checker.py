import os
import json
import csv

# === author imports / helpers ===
import json, math


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


# === block: score_0 (check id='step_01_ldm_fit') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not isinstance(artifact, dict):
            return 0.0
        expected = step.get('expected', {})
        tolerances = step.get('tolerances', {})
        tolerance_map = {
            'A': tolerances.get('A_rel', 0.05),
            'B': tolerances.get('B_rel', 0.10),
            'epsilon_C': tolerances.get('epsilon_C_rel', 0.05),
            'a_c': tolerances.get('a_c_rel', 0.10),
            'a_v': tolerances.get('a_v_rel', 0.10),
            'a_s': tolerances.get('a_s_rel', 0.10),
            'a_v0': tolerances.get('a_v0_rel', 0.15),
            'a_s0': tolerances.get('a_s0_rel', 0.15),
        }
        def walk(exp, act, path=''):
            if not isinstance(act, dict):
                act = {}
            failed = 0
            total = 0
            if isinstance(exp, dict):
                for k, v in exp.items():
                    if isinstance(v, dict):
                        if isinstance(act, dict):
                            f, t = walk(v, act.get(k), path + '.' + k)
                            failed += f
                            total += t
                        else:
                            # missing group; count all leafs under this key as failed
                            # We'll recursively count leafs under v
                            def count_leaves(d):
                                if isinstance(d, dict):
                                    return sum(count_leaves(val) for val in d.values())
                                return 1
                            leaves = count_leaves(v)
                            failed += leaves
                            total += leaves
                    else:
                        total += 1
                        if k not in tolerance_map:
                            continue
                        act_val = None
                        if isinstance(act, dict):
                            act_val = act.get(k)
                        if act_val is None or not isinstance(act_val, (int, float)):
                            failed += 1
                        else:
                            gold = v
                            tol = tolerance_map[k]
                            if not isinstance(gold, (int, float)) or abs(act_val - gold) / max(abs(gold), 1e-9) > tol:
                                failed += 1
            return failed, total

        total_failed = 0
        total_fields = 0
        for pot_key in ['potential_s', 'potential_l']:
            exp_pot = expected.get(pot_key)
            if not isinstance(exp_pot, dict):
                continue
            act_pot = artifact.get(pot_key) if isinstance(artifact, dict) else None
            if exp_pot:
                f, t = walk(exp_pot, act_pot, pot_key)
                total_failed += f
                total_fields += t
        if total_fields == 0:
            return 0.0
        return max(0.0, 1.0 - total_failed / total_fields)


# === block: score_1 (check id='step_02_fragmentation_analysis') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        tol = step.get('energy_balance_tol', 0.02)
        fission_pattern = step.get('fission_pattern', {})
        coulomb_pattern = step.get('coulomb_pattern', {})
        fission = artifact.get('fission')
        coulomb = artifact.get('coulomb_explosion')

        def energy_balance_ok(data):
            if not data or not isinstance(data, dict):
                return False
            ke = data.get('total_KE')
            inn = data.get('total_IN')
            n_eps = data.get('n_epsilon')
            if None in (ke, inn, n_eps) or n_eps == 0:
                return False
            return abs(ke + inn - n_eps) / abs(n_eps) <= tol

        eb_f = 1.0 if energy_balance_ok(fission) else 0.0
        eb_c = 1.0 if energy_balance_ok(coulomb) else 0.0

        def pattern_score(data, pattern):
            if not data or not isinstance(data, dict):
                return 0.0
            n_k = data.get('n_k')
            if not isinstance(n_k, list):
                return 0.0
            fragments = {}
            for pair in n_k:
                if isinstance(pair, (list, tuple)) and len(pair) == 2:
                    k, count = pair
                    if isinstance(k, (int, float)) and isinstance(count, (int, float)):
                        fragments[int(k)] = fragments.get(int(k), 0) + int(count)
            if not fragments:
                return 0.0
            max_k = max(fragments.keys())
            total_fragments = sum(fragments.values())
            monomers = fragments.get(1, 0)
            conditions_met = 0
            conditions_total = 0
            if pattern.get('min_large_fragment_size') is not None:
                conditions_total += 1
                if max_k >= pattern['min_large_fragment_size']:
                    conditions_met += 1
            if pattern.get('max_total_fragments') is not None:
                conditions_total += 1
                if total_fragments <= pattern['max_total_fragments']:
                    conditions_met += 1
            if pattern.get('max_monomers') is not None:
                conditions_total += 1
                if monomers <= pattern['max_monomers']:
                    conditions_met += 1
            if pattern.get('min_monomers') is not None:
                conditions_total += 1
                if monomers >= pattern['min_monomers']:
                    conditions_met += 1
            if pattern.get('max_large_fragment_size') is not None:
                conditions_total += 1
                if max_k <= pattern['max_large_fragment_size']:
                    conditions_met += 1
            if conditions_total == 0:
                return 1.0
            return conditions_met / conditions_total

        pat_f = pattern_score(fission, fission_pattern)
        pat_c = pattern_score(coulomb, coulomb_pattern)

        # Gold comparison for total_KE and total_IN (paper Table III)
        # Fallback defaults: paper reported values if step config missing
        exp_fission = step.get('expected_fission')
        if not exp_fission:
            exp_fission = {'total_KE': 1472, 'total_IN': 1043}
        exp_coulomb = step.get('expected_coulomb')
        if not exp_coulomb:
            exp_coulomb = {'total_KE': 2620, 'total_IN': 140}
        gold_tol = step.get('gold_tol')
        if gold_tol is None:
            gold_tol = 0.10

        def gold_score(data, expected, field):
            if not data or not isinstance(data, dict):
                return 0.0
            act = data.get(field)
            exp_val = expected.get(field)
            if act is None or exp_val is None or not isinstance(act, (int, float)) or not isinstance(exp_val, (int, float)):
                return 0.0
            if exp_val == 0:
                return 1.0 if abs(act) <= gold_tol else 0.0
            return 1.0 if abs(act - exp_val) / abs(exp_val) <= gold_tol else 0.0

        g_ke_f = gold_score(fission, exp_fission, 'total_KE')
        g_in_f = gold_score(fission, exp_fission, 'total_IN')
        g_ke_c = gold_score(coulomb, exp_coulomb, 'total_KE')
        g_in_c = gold_score(coulomb, exp_coulomb, 'total_IN')

        score = (eb_f * 0.1 + eb_c * 0.1 + pat_f * 0.1 + pat_c * 0.1 +
                 g_ke_f * 0.15 + g_in_f * 0.15 + g_ke_c * 0.15 + g_in_c * 0.15)
        return max(0.0, min(1.0, score))


_SCORERS = {
    'step_01_ldm_fit': score_0,
    'step_02_fragmentation_analysis': score_1,
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
