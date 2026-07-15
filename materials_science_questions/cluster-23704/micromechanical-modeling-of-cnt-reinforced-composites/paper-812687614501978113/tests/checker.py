import os
import json
import csv

# === author imports / helpers ===
import csv
import math
import os


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
    import json
    with open('/tests/grading_spec.json') as f:
        spec = json.load(f)
    gold = spec.get('property_gold', {})
    trends = spec.get('trends', {})
    ctx = {'gold': gold, 'trends': trends}
    return ctx


# === block: score_0 (check id='results_check') ===
def score_0(artifact, step, ctx):
    artifact = artifact  # list of dicts from CSV
    ctx = ctx
    gold = ctx['gold']
    trends = ctx['trends']
    vf_order = gold['vf']
    labels = gold['labels']
    num_vf = len(vf_order)

    # Build mapping
    rows_by_vf = {}
    for row in artifact:
        try:
            vf = float(row['Vf'])
        except:
            continue
        rows_by_vf.setdefault(vf, []).append(row)

    # Detect if a 'system' column exists to disambiguate Vf=1.0
    has_system_column = any('system' in row for row in artifact) if artifact else False

    # -----------------------------------------------------------------
    # Build an ordered row list matching the gold vf_order (CNC, wrap)
    # -----------------------------------------------------------------
    ordered_rows = [None] * num_vf
    for idx, vf in enumerate(vf_order):
        if vf != 1.0:
            # Single system per Vf
            if vf in rows_by_vf and len(rows_by_vf[vf]) >= 1:
                ordered_rows[idx] = rows_by_vf[vf][0]
            else:
                ordered_rows[idx] = None
        else:
            # Vf=1.0 has two distinct systems: CNC (idx 6) and wrap-no-CNT (idx 7)
            if has_system_column:
                # Use the 'system' field to match
                cnc_row = None
                wrap_row = None
                for r in rows_by_vf.get(vf, []):
                    sys = str(r.get('system', '')).strip().lower()
                    if sys in ('cnc',):
                        cnc_row = r
                    elif sys in ('cellulose_wrap_no_cnt', 'cellulose_wrap_no_cnt'):
                        wrap_row = r
                ordered_rows[6] = cnc_row
                ordered_rows[7] = wrap_row
            else:
                # Fallback to ordering assumption (first row = CNC, second = wrap)
                if vf in rows_by_vf and len(rows_by_vf[vf]) >= 2:
                    ordered_rows[6] = rows_by_vf[vf][0]
                    ordered_rows[7] = rows_by_vf[vf][1]
                else:
                    ordered_rows[6] = None
                    ordered_rows[7] = None

    # Validate required rows are present
    def validate_rows():
        for idx, vf in enumerate(vf_order):
            if vf == 1.0 and idx == 7:
                continue  # checked together
            if vf == 1.0:
                # Need both CNC and wrap rows
                if ordered_rows[6] is None or ordered_rows[7] is None:
                    return False
            else:
                if ordered_rows[idx] is None:
                    return False
        return True
    shape_ok = 1.0 if validate_rows() else 0.0

    def get_values(prop):
        vals = []
        for idx in range(num_vf):
            row = ordered_rows[idx]
            if row is None:
                vals.append(None)
            else:
                try:
                    vals.append(float(row[prop]))
                except:
                    vals.append(None)
        return vals

    # Gold MAPE score
    props_gold = {k: gold[k] for k in gold if k not in ('vf','labels') and k in gold}
    mape_sum = 0.0
    count = 0
    for prop, gold_vals in props_gold.items():
        agent_vals = get_values(prop)
        gvs = gold_vals
        mape = 0.0
        n = 0
        for a, g in zip(agent_vals, gvs):
            if a is None or g is None:
                continue
            if g != 0:
                mape += abs(a - g) / abs(g)
            else:
                mape += 0 if a == 0 else 1.0
            n += 1
        if n > 0:
            mape /= n
            mape_sum += mape
            count += 1
    avg_mape = mape_sum / count if count else 1.0
    tol1 = 0.25
    tol2 = 0.50
    if avg_mape <= tol1:
        gold_score = 1.0
    elif avg_mape >= tol2:
        gold_score = 0.0
    else:
        gold_score = 1.0 - (avg_mape - tol1) / (tol2 - tol1)

    # Monotonic trend score
    decreasing = trends.get('decreasing', [])
    increasing = trends.get('increasing', [])
    trend_props = decreasing + increasing
    trend_total_score = 0.0
    trend_count = 0
    for prop in trend_props:
        vals = get_values(prop)
        if any(v is None for v in vals):
            continue
        pairs_total = 0
        pairs_ok = 0
        for i in range(len(vals)):
            for j in range(i+1, len(vals)):
                if prop in decreasing:
                    if vals[i] >= vals[j]:
                        pairs_ok += 1
                else:  # increasing
                    if vals[i] <= vals[j]:
                        pairs_ok += 1
                pairs_total += 1
        if pairs_total > 0:
            trend_total_score += pairs_ok / pairs_total
            trend_count += 1
    trend_score = trend_total_score / trend_count if trend_count else 0.0

    # Nanopaper sanity (positivity and modulus <= tensile modulus)
    nano_strength = get_values('nanopaper_strength_GPa')
    nano_modulus = get_values('nanopaper_modulus_GPa')
    tensile_modulus = get_values('tensile_modulus_GPa')
    nano_sanity = 0.0
    if nano_strength and nano_modulus:
        pos_ok = all(v is not None and v >= 0 for v in nano_strength) and \
                 all(v is not None and v >= 0 for v in nano_modulus)
        less_ok = True
        if tensile_modulus and any(v is not None for v in tensile_modulus):
            less_ok = all((me is None or (me is not None and fi is not None and me <= fi))
                           for me, fi in zip(nano_modulus, tensile_modulus))
        nano_sanity = (0.5 if pos_ok else 0.0) + (0.5 if less_ok else 0.0)

    # weights
    w_shape = 0.03
    w_gold = 0.60
    w_trend = 0.20
    w_nano = 0.17
    total = w_shape * shape_ok + w_gold * gold_score + w_trend * trend_score + w_nano * nano_sanity
    return total


_SCORERS = {
    'results_check': score_0,
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
