import os
import json
import csv

# === author imports / helpers ===
import csv, json, os, re, math


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
        hidden_assets = spec.get('hidden_assets', [])
        gold_asset = None
        for a in hidden_assets:
            if a.get('purpose') == 'paper_table_I':
                gold_asset = a
                break
        if gold_asset is None:
            raise RuntimeError('Missing paper_table_I hidden asset')
        return {'gold_table': gold_asset['data']}


# === block: score_0 (check id='bulk_properties') ===
def score_0(artifact, step, ctx):
        if not artifact or not isinstance(artifact, list):
            return 0.0
        gold_table = ctx.get('gold_table')
        if not gold_table:
            return 0.0
        gold_map = {}
        for row in gold_table:
            m = str(row.get('material', '')).strip().lower()
            if m:
                gold_map[m] = row
        materials = ['mno', 'feo', 'coo', 'nio']
        total = 0
        n_fields = 5
        for material in materials:
            rows = [r for r in artifact if str(r.get('material', '')).strip().lower() == material]
            if not rows:
                continue
            row = rows[0]
            g = gold_map.get(material)
            if not g:
                continue
            # a0_angstrom
            val = row.get('a0_angstrom', '')
            if val is not None and val != '':
                try:
                    a0 = float(val)
                    ga0 = float(g.get('a0_angstrom'))
                    if abs(a0 - ga0) <= 0.05:
                        total += 1
                except Exception:
                    pass
            # mu_muB
            val = row.get('mu_muB', '')
            if val is not None and val != '':
                try:
                    mu = float(val)
                    gmu = float(g.get('mu_muB'))
                    if abs(mu - gmu) <= 0.5:
                        total += 1
                except Exception:
                    pass
            # easy_axis
            ea = row.get('easy_axis', '')
            if ea is not None and ea != '':
                try:
                    ea_str = str(ea)
                    ea_norm = re.sub(r'[\s\(\)\[\]]', '', ea_str).lower()
                    ea_norm = ea_norm.lstrip('~≈')
                    allowed = g.get('easy_axis_canonical', [])
                    if allowed and any(candidate in ea_norm for candidate in allowed):
                        total += 1
                except Exception:
                    pass
            # E_g_ind_eV
            val = row.get('E_g_ind_eV', '')
            if val is not None and val != '':
                try:
                    ev = float(val)
                    gv = float(g.get('E_g_ind_eV'))
                    if abs(ev - gv) <= 0.5:
                        total += 1
                except Exception:
                    pass
            # E_g_dir_eV
            val = row.get('E_g_dir_eV', '')
            if val is not None and val != '':
                try:
                    ev = float(val)
                    gv = float(g.get('E_g_dir_eV'))
                    if abs(ev - gv) <= 0.5:
                        total += 1
                except Exception:
                    pass
        max_score = len(materials) * n_fields
        if max_score == 0:
            return 0.0
        return min(1.0, total / max_score)


_SCORERS = {
    'bulk_properties': score_0,
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
