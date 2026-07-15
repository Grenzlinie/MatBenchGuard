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
    steps = spec.get('steps', [])
    step = steps[0] if steps else {}
    ctx = {}
    ctx['gold_rel'] = step.get('params', {}).get('gold_relative', {})
    ctx['dev_targets'] = step.get('params', {}).get('deviation_targets', [])
    return ctx


# === block: score_0 (check id='step_03_electrostatic_analysis') ===
def score_0(artifact, step, ctx):
    import math
    from collections import defaultdict

    def find_row(rows, target_dist):
        best = None
        best_diff = float('inf')
        for r in rows:
            d = float(r['distance'])
            diff = abs(d - target_dist)
            if diff < best_diff:
                best_diff = diff
                best = r
        if best_diff > 0.5:
            return None
        return best

    gold_rel = ctx['gold_rel']
    dev_targets = ctx['dev_targets']

    groups = defaultdict(list)
    for row in artifact:
        key = (row['molecule'].strip(), row['terminal_atom'].strip())
        groups[key].append(row)

    pair_scores = []
    for pair_info in dev_targets:
        mol = pair_info['molecule']
        term = pair_info['terminal_atom']
        key = (mol, term)
        if key not in groups:
            pair_scores.append(0.0)
            continue
        rows = groups[key]
        row3 = find_row(rows, 3.0)
        row8 = find_row(rows, 8.0)
        if row3 is None or row8 is None:
            pair_scores.append(0.0)
            continue

        # recompute pct_deviations
        try:
            vq = float(row3['V_QTAIM'])
            vc = float(row3['V_CHELPG'])
            vr = float(row3['V_ref'])
            pct_q = 100 * abs(vq - vr) / (abs(vr) + 1e-12)
            pct_c = 100 * abs(vc - vr) / (abs(vr) + 1e-12)
        except Exception:
            pair_scores.append(0.0)
            continue

        # QTAIM deviation (one‑sided for 'exact': lower is better, never penalised)
        qcfg = pair_info['qtaim']
        if qcfg['type'] == 'exact':
            target = qcfg['value']
            tol = qcfg['tolerance']
            threshold = target + tol
            if pct_q <= threshold:
                score_q = 1.0
            else:
                score_q = max(0.0, 1.0 - (pct_q - threshold) / tol)
        elif qcfg['type'] == 'threshold':
            max_val = qcfg['max']
            if pct_q <= max_val:
                score_q = 1.0
            else:
                score_q = max(0.0, 1.0 - (pct_q - max_val) / (max_val + 1e-6))
        else:
            score_q = 1.0

        # CHELPG deviation (one‑sided for 'exact')
        ccfg = pair_info['chelpg']
        if ccfg['type'] == 'exact':
            target = ccfg['value']
            tol = ccfg['tolerance']
            threshold = target + tol
            if pct_c <= threshold:
                score_c = 1.0
            else:
                score_c = max(0.0, 1.0 - (pct_c - threshold) / tol)
        elif ccfg['type'] == 'threshold':
            max_val = ccfg['max']
            if pct_c <= max_val:
                score_c = 1.0
            else:
                score_c = max(0.0, 1.0 - (pct_c - max_val) / (max_val + 1e-6))
        elif ccfg['type'] == 'sign':
            if (vr > 0 and vc < 0) or (vr < 0 and vc > 0):
                score_c = 1.0
            else:
                score_c = 0.0
        elif ccfg['type'] == 'ignore':
            score_c = 1.0
        else:
            score_c = 1.0

        # relative contributions at 3 and 8 Å (unchanged closeness scoring)
        rel_scores = []
        for dist in [3.0, 8.0]:
            key_rel = (mol, term, dist)
            if key_rel not in gold_rel:
                rel_scores.append(1.0)
                continue
            gold_c, gold_d, gold_q = gold_rel[key_rel]
            try:
                if dist == 3.0:
                    rel_c = float(row3['rel_charge_contrib'])
                    rel_d = float(row3['rel_dipole_contrib'])
                    rel_q = float(row3['rel_quadrupole_contrib'])
                else:
                    rel_c = float(row8['rel_charge_contrib'])
                    rel_d = float(row8['rel_dipole_contrib'])
                    rel_q = float(row8['rel_quadrupole_contrib'])
            except Exception:
                rel_scores.append(0.0)
                continue
            def contrib_score(val, gold_val, tol=0.15):
                return max(0.0, 1.0 - abs(val - gold_val) / tol)
            sc = contrib_score(rel_c, gold_c)
            sd = contrib_score(rel_d, gold_d)
            sq = contrib_score(rel_q, gold_q)
            max_abs = max(abs(rel_c), abs(rel_d), abs(rel_q))
            norm_score = max(0.0, 1.0 - abs(max_abs - 1.0) / 0.01) if max_abs > 0 else 1.0
            rel_scores.append((sc + sd + sq + norm_score) / 4.0)
        avg_rel = sum(rel_scores) / len(rel_scores) if rel_scores else 1.0

        pair_score = (score_q + score_c + avg_rel) / 3.0
        pair_scores.append(pair_score)

    final_score = sum(pair_scores) / len(pair_scores) if pair_scores else 0.0
    return min(1.0, max(0.0, final_score))


_SCORERS = {
    'step_03_electrostatic_analysis': score_0,
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
