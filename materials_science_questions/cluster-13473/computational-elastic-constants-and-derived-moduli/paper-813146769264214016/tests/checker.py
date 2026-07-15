import os
import json
import csv

# === author imports / helpers ===
import os, json, csv, math


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
    step = spec['steps'][0]
    p = step['params']
    gold_pc = {int(k): v for k,v in p['gold_pc'].items()}
    gold_delta = {int(k): v for k,v in p['gold_delta'].items()}
    return dict(gold_pc=gold_pc, gold_delta=gold_delta,
                tol_pc=p['tol_pc'], tol_delta=p['tol_delta'],
                largest_L_count=p['largest_L_count'],
                csv_file=p['csv_file'])


# === block: score_0 (check id='step_02_results') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        import os, csv, numpy as np
        from scipy.interpolate import interp1d
        from scipy.optimize import brentq

        output_dir = '/app/outputs'
        csv_path = os.path.join(output_dir, ctx['csv_file'])
        if not os.path.exists(csv_path):
            return 0.0

        # parse CSV
        data = {}  # lm -> L -> (ps, Bs)
        with open(csv_path, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                lm = int(row['lambda_mu'])
                L = int(row['L'])
                p = float(row['p'])
                B = float(row['B'])
                data.setdefault(lm, {}).setdefault(L, ([], []))
                data[lm][L][0].append(p)
                data[lm][L][1].append(B)

        recomputed = {}
        for lm in [1, 5, 10]:
            if lm not in data or len(data[lm]) < 2:
                recomputed[lm] = (None, None)
                continue
            Ls = sorted(data[lm].keys(), reverse=True)[:ctx['largest_L_count']]
            if len(Ls) < 2:
                recomputed[lm] = (None, None)
                continue

            interps = {}
            for L in Ls:
                ps, bs = data[lm][L]
                idx = np.argsort(ps)
                ps = np.array(ps)[idx]
                bs = np.array(bs)[idx]
                # unique
                _, uidx = np.unique(ps, return_index=True)
                ps = ps[uidx]
                bs = bs[uidx]
                if len(ps) < 2:
                    continue
                interps[L] = interp1d(ps, bs, kind='cubic', fill_value='extrapolate')
            if len(interps) < 2:
                recomputed[lm] = (None, None)
                continue

            L0 = Ls[0]
            p_min = max([min(data[lm][L][0]) for L in Ls])
            p_max = min([max(data[lm][L][0]) for L in Ls])
            if p_min >= p_max:
                recomputed[lm] = (None, None)
                continue
            p_grid = np.linspace(p_min, p_max, 200)

            zeta_curves = {}
            for L in Ls[1:]:
                B0 = interps[L0](p_grid)
                Bi = interps[L](p_grid)
                mask = (B0 > 0) & (Bi > 0)
                zeta = np.full_like(p_grid, np.nan)
                zeta[mask] = np.log(B0[mask] / Bi[mask]) / np.log(L0 / L)
                zeta_curves[(L0, L)] = (p_grid, zeta)

            if len(zeta_curves) < 2:
                recomputed[lm] = (None, None)
                continue

            pairs = list(zeta_curves.keys())
            p1, z1 = zeta_curves[pairs[0]]
            p2, z2 = zeta_curves[pairs[1]]
            diff_interp = interp1d(p1, z2 - z1, kind='linear', fill_value='extrapolate')
            signs = np.sign(diff_interp(p1))
            crossings = np.where(np.diff(signs) != 0)[0]
            if len(crossings) == 0:
                recomputed[lm] = (None, None)
                continue
            try:
                a, b = float(p1[crossings[0]]), float(p1[crossings[0] + 1])
                pc_calc = brentq(diff_interp, a, b)
            except:
                recomputed[lm] = (None, None)
                continue

            zeta_cross = interp1d(p1, z1, kind='linear')(pc_calc)
            delta_calc = -zeta_cross
            recomputed[lm] = (pc_calc, delta_calc)

        # score value part
        value_score = 0.0
        for lm in [1, 5, 10]:
            if lm in recomputed and recomputed[lm][0] is not None:
                pc, delta = recomputed[lm]
                if (abs(pc - ctx['gold_pc'][lm]) <= ctx['tol_pc'] and
                    abs(delta - ctx['gold_delta'][lm]) <= ctx['tol_delta']):
                    value_score += 1.0
        value_score /= 3.0

        # trend part
        trend_ok = True
        pcs = {lm: recomputed[lm][0] for lm in [1,5,10] if lm in recomputed and recomputed[lm][0] is not None}
        deltas = {lm: recomputed[lm][1] for lm in [1,5,10] if lm in recomputed and recomputed[lm][1] is not None}
        if len(pcs) == 3 and len(deltas) == 3:
            if not (pcs[1] < pcs[5] < pcs[10]):
                trend_ok = False
            if not (deltas[1] > deltas[5] > deltas[10]):
                trend_ok = False
        else:
            trend_ok = False
        trend_score = 1.0 if trend_ok else 0.0

        return 0.8 * value_score + 0.2 * trend_score


_SCORERS = {
    'step_02_results': score_0,
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
