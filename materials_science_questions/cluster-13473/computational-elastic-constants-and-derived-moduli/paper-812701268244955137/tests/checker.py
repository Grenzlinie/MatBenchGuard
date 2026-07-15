import os
import json
import csv

# === author imports / helpers ===
import csv
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


# === block: score_0 (check id='structural_check') ===
def score_0(artifact, step, ctx):
    def score_structural(rows):
        import math
        from collections import defaultdict

        col_names = rows[0].keys()
        required = {'snapshot','w','Tp','box_id','center_x','center_y','center_z','G1','G2','G3','G4','G5','K'}
        if not required.issubset(col_names):
            return 0.0

        records = []
        for r in rows:
            try:
                snap = int(r['snapshot'])
                w = float(r['w'])
                Tp = float(r['Tp'])
                bx = int(r['box_id'])
                cx = float(r['center_x'])
                cy = float(r['center_y'])
                cz = float(r['center_z'])
                g1 = float(r['G1'])
                g2 = float(r['G2'])
                g3 = float(r['G3'])
                g4 = float(r['G4'])
                g5 = float(r['G5'])
                k = float(r['K'])
                records.append((Tp, snap, w, bx, cx, cy, cz, g1, g2, g3, g4, g5, k))
            except:
                continue
        if not records:
            return 0.0

        def mean(vals):
            n = len(vals)
            if n == 0:
                return 0.0
            return sum(vals) / n

        def std_dev(vals):
            n = len(vals)
            if n < 2:
                return 0.0
            m = mean(vals)
            var = sum((x - m) ** 2 for x in vals) / (n - 1)
            return math.sqrt(var)

        def pearsonr(x, y):
            n = len(x)
            if n < 2:
                return 0.0
            mx = mean(x)
            my = mean(y)
            sx = std_dev(x)
            sy = std_dev(y)
            if sx == 0.0 or sy == 0.0:
                return 0.0
            cov = sum((xi - mx) * (yi - my) for xi, yi in zip(x, y)) / (n - 1)
            r = cov / (sx * sy)
            # Clamp to [-1,1] to avoid floating point edge
            return max(-1.0, min(1.0, r))

        tp_w_data = defaultdict(list)
        for rec in records:
            tp, snap, w, *rest = rec
            tp_w_data[(tp, w)].append(rec)

        Tp_values = sorted({r[0] for r in records})
        W_values = sorted({r[2] for r in records})

        std_shear_per_tp_w = {}
        std_bulk_per_tp_w = {}
        psi_G_per_tp_w = {}
        psi_K_per_tp_w = {}

        for tp, w in tp_w_data.keys():
            recs = tp_w_data[(tp, w)]
            shear_vals = []
            bulk_vals = []
            snap_data = defaultdict(list)
            for rec in recs:
                _, snap, _, bx, cx, cy, cz, g1, g2, g3, g4, g5, k = rec
                snap_data[snap].append((bx, cx, cy, cz, g1, g2, g3, g4, g5, k))
                shear_vals.extend((g1, g2, g3, g4, g5))
                bulk_vals.append(k)
            if shear_vals:
                std_shear_per_tp_w[(tp, w)] = std_dev(shear_vals)
            else:
                std_shear_per_tp_w[(tp, w)] = None
            if bulk_vals:
                std_bulk_per_tp_w[(tp, w)] = std_dev(bulk_vals)
            else:
                std_bulk_per_tp_w[(tp, w)] = None

            psi_G_list = []
            psi_K_list = []
            for snap, snap_recs in snap_data.items():
                grid = {}
                for rec in snap_recs:
                    bx, cx, cy, cz, g1, g2, g3, g4, g5, k = rec
                    ix = int(round(cx / w))
                    iy = int(round(cy / w))
                    iz = int(round(cz / w))
                    g_mean = (g1 + g2 + g3 + g4 + g5) / 5.0
                    grid[(ix, iy, iz)] = (g_mean, k)
                if len(grid) < 2:
                    continue
                pairs = []
                for (x, y, z), (g, k) in grid.items():
                    for dx, dy, dz in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
                        nkey = (x + dx, y + dy, z + dz)
                        if nkey in grid:
                            pairs.append((g, grid[nkey][0], k, grid[nkey][1]))
                unique_pairs = []
                seen = set()
                for gA, gB, kA, kB in pairs:
                    if (gA, gB) not in seen and (gB, gA) not in seen:
                        unique_pairs.append((gA, gB, kA, kB))
                        seen.add((gA, gB))
                if unique_pairs and len(unique_pairs) >= 2:
                    gA_vals = [p[0] for p in unique_pairs]
                    gB_vals = [p[1] for p in unique_pairs]
                    kA_vals = [p[2] for p in unique_pairs]
                    kB_vals = [p[3] for p in unique_pairs]
                    rho_G = pearsonr(gA_vals, gB_vals)
                    rho_K = pearsonr(kA_vals, kB_vals)
                    psi_G_list.append(rho_G)
                    psi_K_list.append(rho_K)
            psi_G_per_tp_w[(tp, w)] = mean(psi_G_list) if psi_G_list else None
            psi_K_per_tp_w[(tp, w)] = mean(psi_K_list) if psi_K_list else None

        def mono_score(vals, direction='inc'):
            if len(vals) < 2:
                return 0.5
            steps = 0
            correct = 0
            for i in range(len(vals)-1):
                if vals[i] is not None and vals[i+1] is not None:
                    steps += 1
                    if direction == 'inc' and vals[i] <= vals[i+1]:
                        correct += 1
                    elif direction == 'dec' and vals[i] >= vals[i+1]:
                        correct += 1
            return correct / steps if steps else 0.5

        shear_tp_scores = []
        bulk_tp_scores = []
        for w in W_values:
            shear_stds = [std_shear_per_tp_w.get((tp, w)) for tp in Tp_values]
            bulk_stds = [std_bulk_per_tp_w.get((tp, w)) for tp in Tp_values]
            shear_tp_scores.append(mono_score(shear_stds, 'inc'))
            bulk_tp_scores.append(mono_score(bulk_stds, 'inc'))
        tp_mono_shear = mean(shear_tp_scores) if shear_tp_scores else 0.0
        tp_mono_bulk = mean(bulk_tp_scores) if bulk_tp_scores else 0.0
        tp_mono_score = (tp_mono_shear + tp_mono_bulk) / 2.0

        shear_w_scores = []
        bulk_w_scores = []
        for tp in Tp_values:
            shear_stds = [std_shear_per_tp_w.get((tp, w)) for w in W_values]
            bulk_stds = [std_bulk_per_tp_w.get((tp, w)) for w in W_values]
            shear_w_scores.append(mono_score(shear_stds, 'dec'))
            bulk_w_scores.append(mono_score(bulk_stds, 'dec'))
        w_mono_shear = mean(shear_w_scores) if shear_w_scores else 0.0
        w_mono_bulk = mean(bulk_w_scores) if bulk_w_scores else 0.0
        w_mono_score = (w_mono_shear + w_mono_bulk) / 2.0

        def corr_score(psi):
            if psi is None:
                return 0.0
            if abs(psi) <= 0.1:
                return 1.0
            elif abs(psi) >= 0.5:
                return 0.0
            else:
                return max(0.0, 1.0 - (abs(psi) - 0.1) / 0.4)

        corr_scores = []
        for tpw in psi_G_per_tp_w:
            cg = corr_score(psi_G_per_tp_w[tpw])
            ck = corr_score(psi_K_per_tp_w[tpw])
            corr_scores.append((cg + ck) / 2.0)
        corr_final = mean(corr_scores) if corr_scores else 0.0

        final = 0.4 * tp_mono_score + 0.2 * w_mono_score + 0.4 * corr_final
        return max(0.0, min(1.0, float(final)))

    return score_structural(artifact)


_SCORERS = {
    'structural_check': score_0,
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
