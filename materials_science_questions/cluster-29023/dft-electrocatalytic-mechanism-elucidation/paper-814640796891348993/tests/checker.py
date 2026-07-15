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
    spec_gold = {}
    for step in spec.get("steps", []):
        step_id = step.get("id")
        gold = step.get("gold_data", {})
        if step_id:
            spec_gold[step_id] = gold
    return spec_gold


# === block: score_0 (check id='step_05_adsorption_energies') ===
def score_0(artifact, step, ctx):
    def value_score(agent_val, gold_val, tol):
        if tol is None or tol <= 0:
            return 1.0
        diff = abs(agent_val - gold_val)
        if diff <= tol:
            return 1.0
        elif diff <= 2 * tol:
            return 1.0 - (diff - tol) / tol
        else:
            return 0.0

    gold = ctx.get("step_05_adsorption_energies", {})
    if not gold:
        return 0.0

    if not isinstance(artifact, list):
        return 0.0

    keys = {"pure_Co2cT": ("pure", "Co2cT"), "F-doped_Co2cT": ("F-doped", "Co2cT"), "F-doped_Co5cO": ("F-doped", "Co5cO")}
    entry_map = {}
    for item in artifact:
        cond = str(item.get("condition", "")).strip()
        site = str(item.get("site", "")).strip()
        key = cond + "_" + site
        entry_map[key] = item

    scores = []
    weights = []
    for key, (target_cond, target_site) in keys.items():
        g = gold.get(key)
        if not g:
            continue
        entry = entry_map.get(key)
        if entry is None:
            scores.append(0.0)
            weights.append(1.0)
            continue
        energy_val = entry.get("adsorption_energy_eV")
        bond_val = entry.get("bond_distance_A")
        mode_val = str(entry.get("mode", "")).strip().lower()
        # sub-score per entry: energy 0.7, bond 0.2, mode 0.1
        sub_weights = []
        sub_scores = []
        # energy
        if isinstance(energy_val, (int, float)):
            s = value_score(energy_val, g.get("energy"), g.get("tolerance_energy"))
        else:
            s = 0.0
        sub_scores.append(s)
        sub_weights.append(0.7)
        # bond (skip if gold bond is null)
        if g.get("bond") is not None:
            if isinstance(bond_val, (int, float)):
                s = value_score(bond_val, g.get("bond"), g.get("tolerance_bond"))
            else:
                s = 0.0
            sub_scores.append(s)
            sub_weights.append(0.2)
        else:
            # no bond gold, distribute its weight to energy
            sub_weights[0] += 0.2
        # mode
        gold_mode = str(g.get("mode", "")).strip().lower()
        if gold_mode:
            s = 1.0 if mode_val == gold_mode else 0.0
            sub_scores.append(s)
            sub_weights.append(0.1)
        # aggregate sub-scores
        w_sum = sum(sub_weights)
        if w_sum > 0:
            score = sum(s * w for s, w in zip(sub_scores, sub_weights)) / w_sum
        else:
            score = 0.0
        scores.append(score)
        weights.append(1.0)

    if not weights:
        return 0.0
    total_w = sum(weights)
    return sum(s * w for s, w in zip(scores, weights)) / total_w if total_w > 0 else 0.0


# === block: score_1 (check id='step_07_overpotential') ===
def score_1(artifact, step, ctx):
    def value_score(agent_val, gold_val, tol):
        if tol is None or tol <= 0:
            return 1.0
        diff = abs(agent_val - gold_val)
        if diff <= tol:
            return 1.0
        elif diff <= 2 * tol:
            return 1.0 - (diff - tol) / tol
        else:
            return 0.0

    gold = ctx.get("step_07_overpotential", {})
    gold_entries = gold.get("entries", [])
    tol = gold.get("tolerance_overpotential", 0.2)

    if not isinstance(artifact, list):
        return 0.0

    # build lookup by (condition, site)
    lookup = {}
    for item in artifact:
        cond = str(item.get("condition", "")).strip()
        site = str(item.get("site", "")).strip()
        lookup[(cond, site)] = item

    # score each entry
    overpot_scores = []
    pds_scores = []
    target_overpotentials = []
    for ge in gold_entries:
        cond = ge.get("condition")
        site = ge.get("site")
        gold_op = ge.get("overpotential")
        gold_pds = str(ge.get("pds", "")).strip().lower()
        entry = lookup.get((cond, site))
        if entry is None:
            overpot_scores.append(0.0)
            pds_scores.append(0.0)
            target_overpotentials.append(None)
            continue
        # overpotential
        agent_val = entry.get("overpotential_V")
        if isinstance(agent_val, (int, float)):
            overpot_scores.append(value_score(agent_val, gold_op, tol))
        else:
            overpot_scores.append(0.0)
        # PDS
        agent_pds = str(entry.get("potential_determining_step", "")).strip().lower()
        pds_scores.append(1.0 if agent_pds == gold_pds else 0.0)
        target_overpotentials.append(agent_val if isinstance(agent_val, (int, float)) else None)

    # trend: F-doped Co5cO < pure Co5cO
    pure_Co5cO_idx = next((i for i, ge in enumerate(gold_entries) if ge["condition"] == "pure" and ge["site"] == "Co5cO"), None)
    Fdoped_Co5cO_idx = next((i for i, ge in enumerate(gold_entries) if ge["condition"] == "F-doped" and ge["site"] == "Co5cO"), None)
    trend_ok = True
    if pure_Co5cO_idx is not None and Fdoped_Co5cO_idx is not None:
        pure_op = target_overpotentials[pure_Co5cO_idx]
        fop = target_overpotentials[Fdoped_Co5cO_idx]
        if pure_op is not None and fop is not None:
            trend_ok = fop < pure_op

    avg_overpot = sum(overpot_scores) / max(len(overpot_scores), 1)
    avg_pds = sum(pds_scores) / max(len(pds_scores), 1)
    trend_score = 1.0 if trend_ok else 0.0

    return 0.7 * avg_overpot + 0.1 * avg_pds + 0.2 * trend_score


_SCORERS = {
    'step_05_adsorption_energies': score_0,
    'step_07_overpotential': score_1,
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
