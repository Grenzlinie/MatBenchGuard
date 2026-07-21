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
    def prepare(outputs_dir, spec):
        target = {}
        for step in spec.get('steps', []):
            if step.get('output_file') == 'dos_and_pdos.csv':
                target = step.get('target', {})
        return {'gap_target': target.get('gap_eV', 20.0), 'gap_tol': target.get('gap_tolerance', 5.0)}


# === block: score_0 (check id='step_03_dos_and_pdos') ===
def score_0(artifact, step, ctx):
        gap_target = ctx.get('gap_target', 20.0)
        gap_tol = ctx.get('gap_tol', 5.0)
        blocks = {'FM': [], 'AF': []}
        current = None
        for row in artifact:
            # Safely extract energy_raw; if no 'energy' key or row is malformed, skip
            energy_raw = row.get('energy', '') if isinstance(row, dict) else ''
            # Detect phase comment lines
            if isinstance(energy_raw, str) and energy_raw.strip().startswith('#'):
                if 'FM' in energy_raw:
                    current = 'FM'
                elif 'AF' in energy_raw:
                    current = 'AF'
                continue
            if current is None:
                continue
            # Attempt to parse floats; skip any row that fails
            try:
                e = float(energy_raw)
                tdos = float(row.get('total_dos', ''))
                pf = float(row.get('pdos_f', ''))
                pt2g = float(row.get('pdos_ni_t2g', ''))
                peg = float(row.get('pdos_ni_eg', ''))
                blocks[current].append((e, tdos, pf, pt2g, peg))
            except (ValueError, TypeError):
                continue
        if not blocks['FM'] or not blocks['AF']:
            return 0.0
        def compute_gap(pts):
            pts.sort(key=lambda x: x[0])
            threshold = 1e-3
            groups = []
            in_group = False
            group_start = None
            for i, p in enumerate(pts):
                if p[1] > threshold:
                    if not in_group:
                        in_group = True
                        group_start = i
                else:
                    if in_group:
                        in_group = False
                        groups.append((group_start, i-1))
            if in_group:
                groups.append((group_start, len(pts)-1))
            if len(groups) < 2:
                return None
            best_gap = None
            for i in range(len(groups)-1):
                vbm = pts[groups[i][1]][0]
                cbm = pts[groups[i+1][0]][0]
                gap = cbm - vbm
                if best_gap is None or gap > best_gap:
                    best_gap = gap
            return best_gap
        gap_fm = compute_gap(blocks['FM'])
        gap_af = compute_gap(blocks['AF'])
        if gap_fm is None or gap_af is None:
            return 0.0
        gap_score = 0.0
        for g in [gap_fm, gap_af]:
            if abs(g - gap_target) <= gap_tol:
                gap_score += 1.0
        gap_score /= 2.0
        def check_orbital(pts):
            pts.sort(key=lambda x: x[0])
            threshold = 1e-3
            groups = []
            in_group = False
            group_start = None
            for i, p in enumerate(pts):
                if p[1] > threshold:
                    if not in_group:
                        in_group = True
                        group_start = i
                else:
                    if in_group:
                        in_group = False
                        groups.append((group_start, i-1))
            if in_group:
                groups.append((group_start, len(pts)-1))
            if len(groups) < 2:
                return False
            vbm_idx = groups[0][1]
            cbm_idx = groups[1][0]
            _, _, f_v, t2g_v, eg_v = pts[vbm_idx]
            _, _, f_c, t2g_c, eg_c = pts[cbm_idx]
            val_ok = (f_v + t2g_v) > eg_v
            cond_ok = (f_c + eg_c) > t2g_c
            return val_ok and cond_ok
        orbital_fm = check_orbital(blocks['FM'])
        orbital_af = check_orbital(blocks['AF'])
        orbital_score = 1.0 if (orbital_fm and orbital_af) else 0.0
        total_score = 0.6 * gap_score + 0.4 * orbital_score
        return total_score


_SCORERS = {
    'step_03_dos_and_pdos': score_0,
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
