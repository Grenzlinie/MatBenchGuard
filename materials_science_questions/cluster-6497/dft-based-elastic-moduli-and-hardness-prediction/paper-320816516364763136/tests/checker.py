import os
import json
import csv

# === author imports / helpers ===
import csv
from collections import defaultdict

EV_TO_GPA = 160.21766208


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


# === block: score_0 (check id='bulk_moduli_fit') ===
def score_0(artifact, step, ctx):
        rows = artifact
        if not rows:
            return 0.0
        groups = defaultdict(list)
        for r in rows:
            key = (r.get('material',''), r.get('symmetry',''), r.get('xc',''))
            try:
                V = float(r['volume_ang3'])
                E = float(r['total_energy_eV'])
                groups[key].append((V, E))
            except:
                continue
        expected = step.get('expected_combos', [])
        tol = step.get('tolerance_relative', 0.10)
        min_pts = step.get('min_points_per_fit', 5)
        ordering_groups = step.get('ordering_groups', [])
        # Repair: remove fabricated Si60 (Ih) GGA entry not reported in the paper
        expected = [c for c in expected if not (c.get('material') == 'Si60' and c.get('symmetry') == 'Ih' and c.get('xc') == 'GGA')]
        for og in ordering_groups:
            if og.get('material') == 'Si60' and og.get('xc') == 'GGA':
                sym_rank = og.get('sym_rank', [])
                og['sym_rank'] = [s for s in sym_rank if s != 'Ih']
        # Pure-Python quadratic fit via Cramer's rule
        def polyfit_quad(V, E):
            N = len(V)
            if N < 3:
                return None
            sumV = sum(V)
            sumE = sum(E)
            sumV2 = sum(v*v for v in V)
            sumV3 = sum(v*v*v for v in V)
            sumV4 = sum(v*v*v*v for v in V)
            sumVE = sum(v*e for v,e in zip(V,E))
            sumV2E = sum(v*v*e for v,e in zip(V,E))
            # Matrix [[N, sumV, sumV2], [sumV, sumV2, sumV3], [sumV2, sumV3, sumV4]]
            def det(a,b,c,d,e,f,g,h,i):
                return a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)
            D = det(N, sumV, sumV2, sumV, sumV2, sumV3, sumV2, sumV3, sumV4)
            if abs(D) < 1e-15:
                return None
            c0 = det(sumE, sumV, sumV2, sumVE, sumV2, sumV3, sumV2E, sumV3, sumV4) / D
            c1 = det(N, sumE, sumV2, sumV, sumVE, sumV3, sumV2, sumV2E, sumV4) / D
            c2 = det(N, sumV, sumE, sumV, sumV2, sumVE, sumV2, sumV3, sumV2E) / D
            return c2, c1, c0
        computed = {}
        for key, pts in groups.items():
            if len(pts) < min_pts:
                continue
            pts_sorted = sorted(pts, key=lambda p: p[0])
            V = [p[0] for p in pts_sorted]
            E = [p[1] for p in pts_sorted]
            coeffs = polyfit_quad(V, E)
            if coeffs is None:
                continue
            c2, c1, c0 = coeffs
            if abs(c2) < 1e-15:
                continue
            V0 = -c1/(2*c2)
            B = V0 * 2 * c2 * EV_TO_GPA
            computed[key] = B
        # Bulk modulus scores
        bulk_scores = []
        for combo in expected:
            key = (combo['material'], combo['symmetry'], combo['xc'])
            target = float(combo['bulk_modulus'])
            if key not in computed:
                bulk_scores.append(0.0)
                continue
            Bc = computed[key]
            rel_err = abs(Bc - target) / target if target != 0 else abs(Bc - target)
            if rel_err <= tol:
                bulk_scores.append(1.0)
            else:
                bulk_scores.append(max(0.0, 1.0 - (rel_err - tol)/tol))
        bulk_avg = sum(bulk_scores)/len(bulk_scores) if bulk_scores else 0.0
        # Ordering scores
        order_scores = []
        for og in ordering_groups:
            mat = og['material']
            xc = og['xc']
            rank = og.get('sym_rank', ['Ih','C2h','C1'])
            vals = []
            for sym in rank:
                k = (mat, sym, xc)
                if k in computed:
                    vals.append(computed[k])
            if len(vals) < 2:
                continue
            correct = 0
            total = 0
            for i in range(len(vals)-1):
                total += 1
                if vals[i] >= vals[i+1] - 0.1:
                    correct += 1
            if total > 0:
                order_scores.append(correct / total)
        ord_avg = sum(order_scores)/len(order_scores) if order_scores else 1.0
        final = 0.8 * bulk_avg + 0.2 * ord_avg
        return float(final)


_SCORERS = {
    'bulk_moduli_fit': score_0,
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
