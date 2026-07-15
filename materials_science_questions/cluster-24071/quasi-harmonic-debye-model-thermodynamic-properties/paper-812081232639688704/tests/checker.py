import os
import json
import csv

# === author imports / helpers ===
import math


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
        R = 8.314

        def compute_alpha_metallic(dH_m_kJ, T_m, dV_V_percent):
            dH = dH_m_kJ * 1000.0
            ds_m = dH / T_m
            dv_v = dV_V_percent / 100.0
            xa = 1.0 / (1.0 + dv_v)
            xb = 1.0 - xa
            ds_pos = -R * (xa * math.log(xa) + xb * math.log(xb))
            ds_vib = ds_m - ds_pos
            return 2.0 * ds_vib / (3.0 * R) + 1.0

        alpha_fe = compute_alpha_metallic(13.80, 1811.0, 3.4)
        alpha_pb = compute_alpha_metallic(4.77, 600.61, 3.5)

        dh_se = 5400.0
        T_se = 494.0
        ds_vib_se = dh_se / T_se
        alpha_se = 2.0 * ds_vib_se / (3.0 * R) + 1.0

        h_ar = 0.3650
        h_al = 0.2863
        T_ar = 83.80
        T_al = 933.47
        alpha_aral = 0.5 * (((h_al / h_ar) ** 2) * (T_ar / T_al) + 1.0)

        d0_fe = 6 * 0.2482
        d0_se = 6 * 0.4366
        d0_pb = 6 * 0.3500
        d0_aral = 6 * 0.3650

        return {
            'debye_ratio_free_Fe.csv': {
                'alpha': alpha_fe,
                'd0': d0_fe,
                'formula': 'debye',
                'trend': 'increasing'
            },
            'debye_ratio_embedded_ArAl.csv': {
                'alpha': alpha_aral,
                'd0': d0_aral,
                'formula': 'debye',
                'trend': 'decreasing'
            },
            'einstein_ratio_Se.csv': {
                'alpha': alpha_se,
                'd0': d0_se,
                'formula': 'debye',
                'trend': 'increasing'
            },
            'alpha_v_ratio_Se_Pb.csv': {
                'materials': {
                    'Se': {'alpha': alpha_se, 'd0': d0_se},
                    'Pb': {'alpha': alpha_pb, 'd0': d0_pb}
                },
                'formula': 'alpha_v',
                'trend': 'increasing'
            }
        }


# === block: score_0 (check id='step_2') ===
def score_0(artifact, step, ctx):
    def score_fn(artifact, step, ctx):
        if artifact is None or not isinstance(artifact, (list, tuple)):
            return 0.0
        config = ctx.get(step['output_file'])
        if config is None:
            return 0.0
        alpha = float(config.get('alpha', 1.0))
        d0 = float(config.get('d0', 1.0))
        trend_dir = config.get('trend', 'increasing')
        rows = []
        for row in artifact:
            try:
                D_str = row.get('D (nm)', '')
                r_str = row.get('Theta_D_ratio (dimensionless)', '')
                if not isinstance(D_str, str) or not isinstance(r_str, str):
                    continue
                D = float(D_str.strip())
                ratio = float(r_str.strip())
                if D > d0 + 1e-12:
                    rows.append((D, ratio))
            except Exception:
                continue
        if not rows:
            return 0.0
        rows.sort(key=lambda x: x[0])
        expected = []
        for D, _ in rows:
            exp_arg = -(alpha - 1.0) / (D / d0 - 1.0)
            ratio_e = math.sqrt(math.exp(exp_arg))
            expected.append(ratio_e)
        ratio_scores = []
        for (_, r), e in zip(rows, expected):
            err = abs(r - e)
            ratio_scores.append(max(0.0, 1.0 - err / 0.02))
        ratio_acc = sum(ratio_scores) / len(ratio_scores)
        trend_ok = True
        if trend_dir == 'increasing':
            for i in range(len(rows) - 1):
                if rows[i + 1][1] < rows[i][1] - 1e-9:
                    trend_ok = False
                    break
        else:
            for i in range(len(rows) - 1):
                if rows[i + 1][1] > rows[i][1] + 1e-9:
                    trend_ok = False
                    break
        trend_score = 1.0 if trend_ok else 0.0
        return 0.9 * ratio_acc + 0.1 * trend_score


# === block: score_1 (check id='step_3') ===
def score_1(artifact, step, ctx):
    def score_fn(artifact, step, ctx):
        config = ctx[step['output_file']]
        alpha = config['alpha']
        d0 = config['d0']
        trend_dir = config['trend']
        rows = []
        for row in artifact:
            try:
                D = float(row['D (nm)'])
                ratio = float(row['Theta_D_ratio (dimensionless)'])
                if D > d0:
                    rows.append((D, ratio))
            except:
                continue
        if not rows:
            return 0.0
        rows.sort(key=lambda x: x[0])
        expected = []
        for D, _ in rows:
            exp_arg = -(alpha - 1.0) / (D / d0 - 1.0)
            ratio_e = math.sqrt(math.exp(exp_arg))
            expected.append(ratio_e)
        ratio_scores = []
        for (_,r), e in zip(rows, expected):
            err = abs(r - e)
            ratio_scores.append(max(0.0, 1.0 - err / 0.02))
        ratio_acc = sum(ratio_scores) / len(ratio_scores)
        trend_ok = True
        if trend_dir == 'increasing':
            for i in range(len(rows)-1):
                if rows[i+1][1] < rows[i][1] - 1e-9:
                    trend_ok = False
                    break
        else:
            for i in range(len(rows)-1):
                if rows[i+1][1] > rows[i][1] + 1e-9:
                    trend_ok = False
                    break
        trend_score = 1.0 if trend_ok else 0.0
        return 0.9 * ratio_acc + 0.1 * trend_score


# === block: score_2 (check id='step_4') ===
def score_2(artifact, step, ctx):
    def score_fn(artifact, step, ctx):
        config = ctx[step['output_file']]
        alpha = config['alpha']
        d0 = config['d0']
        trend_dir = config['trend']
        rows = []
        for row in artifact:
            try:
                D = float(row['D (nm)'])
                ratio = float(row['Theta_E_ratio (dimensionless)'])
                if D > d0:
                    rows.append((D, ratio))
            except:
                continue
        if not rows:
            return 0.0
        rows.sort(key=lambda x: x[0])
        expected = []
        for D, _ in rows:
            exp_arg = -(alpha - 1.0) / (D / d0 - 1.0)
            ratio_e = math.sqrt(math.exp(exp_arg))
            expected.append(ratio_e)
        ratio_scores = []
        for (_,r), e in zip(rows, expected):
            err = abs(r - e)
            ratio_scores.append(max(0.0, 1.0 - err / 0.02))
        ratio_acc = sum(ratio_scores) / len(ratio_scores)
        trend_ok = True
        if trend_dir == 'increasing':
            for i in range(len(rows)-1):
                if rows[i+1][1] < rows[i][1] - 1e-9:
                    trend_ok = False
                    break
        else:
            for i in range(len(rows)-1):
                if rows[i+1][1] > rows[i][1] + 1e-9:
                    trend_ok = False
                    break
        trend_score = 1.0 if trend_ok else 0.0
        return 0.9 * ratio_acc + 0.1 * trend_score


# === block: score_3 (check id='step_5') ===
def score_3(artifact, step, ctx):
    def score_fn(artifact, step, ctx):
        config = ctx[step['output_file']]
        materials = config['materials']
        # The correct physical trend for alpha_v(D)/alpha_v(∞) of free nanoparticles
        # is decreasing as diameter D increases (ratio → 1 for large D).
        trend_dir = 'decreasing'
        rows_by_mat = {}
        for row in artifact:
            try:
                D = float(row['D (nm)'])
                elem = row['element'].strip()
                ratio = float(row['alpha_v_ratio (dimensionless)'])
                rows_by_mat.setdefault(elem, []).append((D, ratio))
            except:
                continue
        total_score = 0.0
        count = 0
        for elem, rows in rows_by_mat.items():
            if elem not in materials:
                continue
            mat = materials[elem]
            rows = [(D,r) for D,r in rows if D > mat['d0']]
            if not rows:
                continue
            rows.sort(key=lambda x: x[0])
            expected = []
            for D, _ in rows:
                exp_arg = (mat['alpha'] - 1.0) / (D / mat['d0'] - 1.0)
                ratio_e = math.exp(exp_arg)
                expected.append(ratio_e)
            ratio_scores = []
            for (_,r), e in zip(rows, expected):
                err = abs(r - e)
                ratio_scores.append(max(0.0, 1.0 - err / 0.02))
            ratio_acc = sum(ratio_scores) / len(ratio_scores)
            trend_ok = True
            if trend_dir == 'increasing':
                for i in range(len(rows)-1):
                    if rows[i+1][1] < rows[i][1] - 1e-9:
                        trend_ok = False
                        break
            else:
                for i in range(len(rows)-1):
                    if rows[i+1][1] > rows[i][1] + 1e-9:
                        trend_ok = False
                        break
            trend_score = 1.0 if trend_ok else 0.0
            mat_score = 0.9 * ratio_acc + 0.1 * trend_score
            total_score += mat_score
            count += 1
        return total_score / count if count else 0.0


_SCORERS = {
    'step_2': score_0,
    'step_3': score_1,
    'step_4': score_2,
    'step_5': score_3,
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
