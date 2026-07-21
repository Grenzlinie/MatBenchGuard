import os
import json
import csv

# === author imports / helpers ===
import math
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


# === block: score_0 (check id='effective_moduli_check') ===
def score_0(artifact, step, ctx):
    def score(row, K_ref, G_ref, rel_tol):
        dK = abs(row['K'] - K_ref) / (abs(K_ref) if abs(K_ref) > 1e-10 else 1.0)
        dG = abs(row['G'] - G_ref) / (abs(G_ref) if abs(G_ref) > 1e-10 else 1.0)
        sK = 1.0 if dK <= rel_tol else max(0.0, 1.0 - (dK - rel_tol) / rel_tol)
        sG = 1.0 if dG <= rel_tol else max(0.0, 1.0 - (dG - rel_tol) / rel_tol)
        return 0.5 * sK + 0.5 * sG

    rows = artifact
    if not isinstance(rows, list) or len(rows) == 0:
        return 0.0
    gold = step.get('gold_rows', [])
    rel_tol = step.get('relative_tolerance', 0.15)

    gold_lookup = {}
    for g in gold:
        key = (g[0], float(g[1]), int(g[2]))
        gold_lookup[key] = (float(g[3]), float(g[4]))

    matched = 0
    row_scores = []
    for r in rows:
        try:
            sys = r.get('system', '')
            vf = float(r['volume_fraction'])
            it = int(r['interface_type'])
            K_rep = float(r['K'])
            G_rep = float(r['G'])
        except Exception:
            continue
        key = (sys, vf, it)
        if key not in gold_lookup:
            continue
        K_ref, G_ref = gold_lookup[key]
        row_scores.append(score({'K': K_rep, 'G': G_rep}, K_ref, G_ref, rel_tol))
        matched += 1

    if matched == 0:
        return 0.0
    value_score = sum(row_scores) / len(row_scores)

    trend_score = 1.0
    if step.get('trend_check', False):
        valid_trend = True
        systems = set()
        vf_set = set()
        for r in rows:
            try:
                sys = r.get('system','')
                vf = float(r['volume_fraction'])
                it = int(r['interface_type'])
                k = float(r['K'])
                g = float(r['G'])
                if it in (1,2):
                    key = (sys, vf, it)
                    if key not in gold_lookup:
                        continue
                    systems.add(sys)
                    vf_set.add((sys, vf))
            except:
                continue
        for sys in systems:
            for vf in vf_set:
                kk1 = None
                kk2 = None
                for r in rows:
                    try:
                        if r.get('system','')==sys and float(r['volume_fraction'])==vf:
                            if int(r['interface_type'])==1:
                                kk1 = float(r.get('K'))
                                kk2 = float(r.get('G'))
                    except:
                        pass
                for r in rows:
                    try:
                        if r.get('system','')==sys and float(r['volume_fraction'])==vf:
                            if int(r['interface_type'])==2:
                                kk3 = float(r.get('K'))
                                kk4 = float(r.get('G'))
                    except:
                        pass
                if kk1 is not None and kk3 is not None:
                    if kk1 <= kk3:
                        valid_trend = False
                if kk2 is not None and kk4 is not None:
                    if kk2 <= kk4:
                        valid_trend = False
        trend_score = 1.0 if valid_trend else 0.0
    return 0.7 * value_score + 0.3 * trend_score


# === block: score_1 (check id='fracture_crack_surface_check') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not isinstance(rows, list) or len(rows) < 3:
        return 0.0
    order = {}
    for r in rows:
        try:
            mid = int(r['microstructure_id'])
            tr = float(r['total_ratio'])
        except:
            continue
        if mid in (1,2,3):
            order[mid] = tr
    if 1 not in order or 2 not in order or 3 not in order:
        return 0.0
    if order[1] < order[2] < order[3]:
        return 1.0
    return 0.0


# === block: score_2 (check id='fracture_force_strain_check') ===
def score_2(artifact, step, ctx):
    rows = artifact
    if not isinstance(rows, list) or len(rows) == 0:
        return 0.0
    curves = defaultdict(list)
    for r in rows:
        try:
            mid = int(r['microstructure_id'])
            eps = float(r['strain'])
            force = float(r['force'])
        except:
            continue
        curves[mid].append((eps, force))
    peaks = {}
    for mid in (1,2,3):
        pts = sorted(curves.get(mid, []))
        if not pts:
            return 0.0
        max_f = max(f for _, f in pts)
        peaks[mid] = max_f
    if 1 not in peaks or 2 not in peaks or 3 not in peaks:
        return 0.0
    if peaks[1] < peaks[2] < peaks[3]:
        return 1.0
    return 0.0


_SCORERS = {
    'effective_moduli_check': score_0,
    'fracture_crack_surface_check': score_1,
    'fracture_force_strain_check': score_2,
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
