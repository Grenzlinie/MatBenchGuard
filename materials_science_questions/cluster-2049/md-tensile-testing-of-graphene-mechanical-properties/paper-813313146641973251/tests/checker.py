import os
import json
import csv

# === author imports / helpers ===
import csv, math, collections


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
    step_cfg = spec['steps'][0]
    return {'gold_values': step_cfg['gold_values'], 'tol_rel': step_cfg['tol_rel']}


# === block: score_0 (check id='leff_csv') ===
def score_0(artifact, step, ctx):
    rows = artifact if isinstance(artifact, list) else []
    if not rows:
        return 0.0

    # build dict: key = (config, length) -> list of (row_index, effective_length)
    from collections import defaultdict
    seen = defaultdict(list)
    # also collect all SWCNT rows separately (any length)
    swcnt_rows = []
    for r in rows:
        try:
            cfg = r['configuration'].strip()
            length = int(r['length_Angstrom'])
            leff = float(r['effective_length_Angstrom'])
        except (ValueError, KeyError, TypeError):
            continue
        if cfg == 'SWCNT':
            swcnt_rows.append(leff)
        else:
            seen[(cfg, length)].append(leff)

    gold = ctx['gold_values']
    tol_rel = ctx['tol_rel']

    # row-level scores
    row_scores = []
    for key_str, expected in gold.items():
        # key_str like 'DWCNT_vdW_160' or 'SWCNT_984'
        parts = key_str.rsplit('_', 1)
        if len(parts) != 2:
            continue
        cfg = parts[0]
        # for SWCNT, we ignore the length field and accept any SWCNT row
        if cfg == 'SWCNT':
            vals = swcnt_rows
        else:
            try:
                length = int(parts[1])
            except ValueError:
                continue
            vals = seen.get((cfg, length), [])
        if not vals:
            row_scores.append(0.0)
            continue
        # pick best (closest to expected)
        best_val = min(vals, key=lambda v: abs(v - expected))
        rel_err = abs(best_val - expected) / expected if expected != 0 else 0.0
        if rel_err <= tol_rel:
            row_score = 1.0
        else:
            row_score = max(0.0, 1.0 - (rel_err - tol_rel) / tol_rel)
        row_scores.append(row_score)

    gold_count = len(gold)
    if gold_count == 0:
        row_tol_avg = 0.0
    else:
        row_tol_avg = sum(row_scores) / gold_count

    # ordering checks
    ordering_ok = 0
    total_ordering = 0

    # build per-config lists for monotonicity (DWCNT only)
    from collections import defaultdict
    config_vals = defaultdict(list)
    for (cfg, length), leff_list in seen.items():
        if cfg not in ('DWCNT_vdW', 'DWCNT_covalent'):
            continue
        # use max leff for that config/length if multiple
        leff = max(leff_list)
        config_vals[cfg].append((length, leff))

    # check monotonic increase within each config
    for cfg, entries in config_vals.items():
        entries.sort(key=lambda x: x[0])
        for i in range(len(entries)-1):
            total_ordering += 1
            if entries[i+1][1] > entries[i][1]:
                ordering_ok += 1

    # check covalent > vdW for same length
    lengths_set = set()
    for cfg, entries in config_vals.items():
        for length, _ in entries:
            lengths_set.add(length)

    for length in lengths_set:
        vdw_vals = []
        cov_vals = []
        if 'DWCNT_vdW' in config_vals:
            vdw_vals = [l for l_, l in config_vals['DWCNT_vdW'] if l_ == length]
        if 'DWCNT_covalent' in config_vals:
            cov_vals = [l for l_, l in config_vals['DWCNT_covalent'] if l_ == length]
        if vdw_vals and cov_vals:
            total_ordering += 1
            if max(cov_vals) > max(vdw_vals):
                ordering_ok += 1

    # SWCNT > max DWCNT
    import math
    dwcnt_max = -math.inf
    for (cfg, length), leff_list in seen.items():
        if cfg in ('DWCNT_vdW', 'DWCNT_covalent'):
            dwcnt_max = max(dwcnt_max, max(leff_list))

    if swcnt_rows and dwcnt_max > -math.inf:
        total_ordering += 1
        if max(swcnt_rows) > dwcnt_max:
            ordering_ok += 1

    if total_ordering == 0:
        ordering_score = 1.0
    else:
        ordering_score = ordering_ok / total_ordering

    final_score = 0.8 * row_tol_avg + 0.2 * ordering_score
    return max(0.0, min(1.0, final_score))


_SCORERS = {
    'leff_csv': score_0,
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
