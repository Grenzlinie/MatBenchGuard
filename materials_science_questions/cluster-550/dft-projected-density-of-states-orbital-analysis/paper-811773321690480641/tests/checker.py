import os
import json
import csv

# === author imports / helpers ===
import math
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
    ref = {}
    tolerance = 0.20
    expected_heptamer = {}
    expected_ordering = {}
    expected_seq = []
    for step in steps:
        if step['id'] == 'step_03':
            ref = step.get('reference', {})
            tolerance = step.get('tolerance', 0.20)
        elif step['id'] == 'step_02':
            expected_heptamer = step.get('expected', {})
        elif step['id'] == 'step_04':
            expected_ordering = step.get('expected_ordering', {})
            expected_seq = step.get('expected_c_axis_sequence', [])
    return {
        'ref': ref,
        'tolerance': tolerance,
        'expected_heptamer': expected_heptamer,
        'expected_ordering': expected_ordering,
        'expected_seq': expected_seq
    }


# === block: score_0 (check id='step_02') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    expected = ctx.get('expected_heptamer', {})
    iso = artifact.get('isolated_site')
    center = artifact.get('heptamer_center')
    verts = artifact.get('heptamer_vertices')
    if (iso == expected.get('isolated_site') and center == expected.get('heptamer_center')
        and isinstance(verts, list) and len(verts) == 6 and all(v == 'V3' for v in verts)):
        return 1.0
    return 0.0


# === block: score_1 (check id='step_03') ===
def score_1(artifact, step, ctx):
    ref = ctx.get('ref', {})
    tolerance = ctx.get('tolerance', 0.20)
    if not isinstance(artifact, list) or not artifact:
        return 0.0
    # Map V_site -> row
    rows = {row.get('V_site'): row for row in artifact if row.get('V_site')}
    required = ['V1', 'V2', 'V3']
    if any(s not in rows for s in required):
        return 0.0
    scores = []
    for site in required:
        r = ref.get(site)
        if not r:
            return 0.0
        row = rows[site]
        try:
            p1 = float(row['PART_I'])
            p2 = float(row['PART_II'])
        except (ValueError, KeyError):
            return 0.0
        e1 = abs(p1 - r['PART_I'])
        e2 = abs(p2 - r['PART_II'])
        # normalized error: average of two errors divided by tolerance
        norm_err = (e1 + e2) / (2 * tolerance)
        site_score = max(0.0, 1.0 - norm_err)
        scores.append(site_score)
    return sum(scores) / len(scores)


# === block: score_2 (check id='step_04') ===
def score_2(artifact, step, ctx):
    expected_ordering = ctx.get('expected_ordering', {})
    expected_seq = ctx.get('expected_seq', [])
    csv_path = '/app/outputs/step_03_integrated_intensities.csv'
    if not os.path.exists(csv_path):
        return 0.0
    # Load CSV and derive ordering
    csv_rows = []
    with open(csv_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            csv_rows.append(row)
    if not csv_rows:
        return 0.0
    rows = {r['V_site']: r for r in csv_rows if r.get('V_site')}
    if not all(s in rows for s in ['V1','V2','V3']):
        return 0.0
    vals = {}
    for s in ['V1','V2','V3']:
        try:
            vals[s] = (float(rows[s]['PART_I']), float(rows[s]['PART_II']))
        except (ValueError, KeyError):
            return 0.0
    # Sort sites: primary by PART_I descending, secondary by PART_II ascending
    sorted_sites = sorted(vals.keys(), key=lambda s: (-vals[s][0], vals[s][1]))
    # Assign ordering: first is highest, last is lowest, middle intermediate
    if len(sorted_sites) != 3:
        return 0.0
    order_map = {sorted_sites[0]: 'highest', sorted_sites[1]: 'intermediate', sorted_sites[2]: 'lowest'}
    # Score ordering correctness (0.7 weight)
    ordering_score = 0.0
    if isinstance(artifact, dict) and 'ordering' in artifact:
        reported = artifact['ordering']
        if isinstance(reported, dict) and all(k in reported for k in ['V1','V2','V3']):
            if all(reported[k] == order_map[k] for k in order_map):
                ordering_score = 1.0
            else:
                ordering_score = 0.0
        else:
            ordering_score = 0.0
    else:
        ordering_score = 0.0
    # c-axis sequence score (exact match, 0.3 weight)
    seq_score = 0.0
    if isinstance(artifact, dict):
        seq = artifact.get('c_axis_sequence')
        if seq == expected_seq:
            seq_score = 1.0
        else:
            seq_score = 0.0
    return 0.7 * ordering_score + 0.3 * seq_score


_SCORERS = {
    'step_02': score_0,
    'step_03': score_1,
    'step_04': score_2,
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
