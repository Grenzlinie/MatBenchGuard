import os
import json
import csv

# === author imports / helpers ===
import csv
from collections import defaultdict


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


# === block: score_0 (check id='step_delta_E') ===
def score_0(artifact, step, ctx):
    gold_list = step.get('gold', [])
    tol = step.get('tolerance_delta_E_eV', 0.05)
    if not gold_list:
        return 0.0
    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0

    # --- robust column name fetching (strip spaces, compare case-insensitively) ---
    def _col_val(row, candidate_keys):
        for key in candidate_keys:
            if key in row:
                return row[key]
        # fallback: scan all keys ignoring case and whitespace
        for rk in row:
            if rk.strip().lower() in [k.strip().lower() for k in candidate_keys]:
                return row[rk]
        return None

    # --- parse submitted rows ---
    rows = []
    for r in artifact:
        try:
            cfg = str(_col_val(r, ['configuration', 'Configuration'])).strip()
            conc_raw = _col_val(r, ['Li_vacancy_concentration', 'li_vacancy_concentration', 'Li vacancy concentration'])
            val_raw = _col_val(r, ['delta_E_eV', 'delta_e_ev', 'delta_E'])
            if cfg and conc_raw is not None and val_raw is not None:
                conc = float(conc_raw)
                val  = float(val_raw)
                rows.append((cfg, conc, val))
        except Exception:
            pass

    if not rows:
        return 0.0

    # --- parse gold entries ---
    gold = []
    for g in gold_list:
        try:
            cfg  = str(g.get('configuration', '')).strip()
            conc = float(g.get('Li_vacancy_concentration', 0))
            val  = float(g.get('gold_delta_E_eV', 0))
            if cfg:
                gold.append((cfg, conc, val))
        except Exception:
            pass

    if not gold:
        return 0.0

    # --- match gold entries to submitted rows (epsilon on concentration) ---
    eps_conc = 1e-4
    num_ok = 0
    num_gold = len(gold)
    used_indices = set()

    for gc, g_conc, g_val in gold:
        best_idx = -1
        best_dist = float('inf')
        best_rv = None
        for idx, (rc, r_conc, rv) in enumerate(rows):
            if idx in used_indices:
                continue
            if gc == rc:
                d = abs(g_conc - r_conc)
                if d < best_dist:
                    best_dist = d
                    best_rv = rv
                    best_idx = idx
        if best_idx >= 0 and best_dist <= eps_conc:
            if abs(best_rv - g_val) <= tol:
                num_ok += 1
            used_indices.add(best_idx)

    numeric_score = num_ok / num_gold if num_gold > 0 else 0.0

    # --- trend checks (unchanged logic) ---
    groups = defaultdict(list)
    for cfg, conc, val in rows:
        groups[cfg].append((conc, val))

    trend_violations = 0
    total_consecutive = 0
    for cfg, pairs in groups.items():
        sorted_pairs = sorted(pairs, key=lambda x: x[0])
        for i in range(len(sorted_pairs)-1):
            total_consecutive += 1
            if sorted_pairs[i+1][1] > sorted_pairs[i][1] + 1e-8:
                trend_violations += 1

    config_order = {'V@(0,1)':1, 'V@(0,2)':2, 'V@(0,3)':3, 'V@(0,4)':4}
    cross_violations = 0
    cross_pairs = 0
    concentrations_unique = sorted({round(c, 4) for _, c, _ in rows})
    for conc in concentrations_unique:
        entries = [(config_order.get(cfg, 99), val) for cfg, c, val in rows if abs(c - conc) < 1e-4 and cfg in config_order]
        entries.sort(key=lambda x: x[0])
        for i in range(len(entries)-1):
            cross_pairs += 1
            if entries[i+1][1] > entries[i][1] + 1e-8:
                cross_violations += 1

    total_trend_pairs = total_consecutive + cross_pairs
    if total_trend_pairs == 0:
        trend_score = 1.0
    else:
        trend_score = max(0.0, 1.0 - (trend_violations + cross_violations) / total_trend_pairs)

    return 0.7 * numeric_score + 0.3 * trend_score


# === block: score_1 (check id='step_magnetic_moments') ===
def score_1(artifact, step, ctx):
    gold_list = step.get('gold', [])
    tol = step.get('tolerance_moment_uB', 0.2)
    if not gold_list or not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0

    gold_dict = {}
    for g in gold_list:
        key = (g['configuration'], float(g['Li_vacancy_concentration']))
        gold_dict[key] = g['gold_moment_uB']

    rows = []
    for row in artifact:
        try:
            config = str(row['configuration']).strip()
            conc = float(row['Li_vacancy_concentration'])
            val = float(row['V_magnetic_moment_uB'])
            rows.append((config, conc, val))
        except (KeyError, ValueError):
            continue

    num_ok = 0
    for config, conc, val in rows:
        key = (config, conc)
        if key in gold_dict:
            if abs(val - gold_dict[key]) <= tol:
                num_ok += 1

    numeric_score = num_ok / len(gold_list) if gold_list else 0.0

    groups = defaultdict(list)
    for config, conc, val in rows:
        groups[config].append((conc, val))

    trend_violations = 0
    total_pairs = 0
    for config, pairs in groups.items():
        sorted_pairs = sorted(pairs, key=lambda x: x[0])
        for i in range(len(sorted_pairs)-1):
            total_pairs += 1
            if sorted_pairs[i+1][1] > sorted_pairs[i][1] + 1e-6:
                trend_violations += 1

    if total_pairs == 0:
        trend_score = 1.0
    else:
        trend_score = max(0.0, 1.0 - trend_violations / total_pairs)

    final = 0.6 * numeric_score + 0.4 * trend_score
    return final


_SCORERS = {
    'step_delta_E': score_0,
    'step_magnetic_moments': score_1,
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
