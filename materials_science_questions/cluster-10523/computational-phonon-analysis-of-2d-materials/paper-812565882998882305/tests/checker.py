import os
import json
import csv

# === author imports / helpers ===
try:
    import numpy as np
except ModuleNotFoundError:
    class _Np:
        @staticmethod
        def mean(seq):
            if not seq:
                return 0.0
            return sum(seq) / len(seq)
    np = _Np()


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
        csv_path = os.path.join(outputs_dir, 'energy_moment_charge_data.csv')
        ctx = {'csv_data': None, 'e0': {}, 'modes': []}
        if not os.path.exists(csv_path):
            return ctx
        with open(csv_path, newline='') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        if not rows:
            return ctx
        data = {}
        e0_candidates = {}
        for row in rows:
            mode = row.get('mode', '').strip()
            if not mode:
                continue
            try:
                u = float(row['displacement'])
                energy = float(row['energy'])
                m1 = float(row['M_Ni1'])
                m2 = float(row['M_Ni2'])
                q1 = float(row['Q_Ni1'])
                q2 = float(row['Q_Ni2'])
            except (ValueError, KeyError):
                continue
            if mode not in data:
                data[mode] = []
                e0_candidates[mode] = []
            data[mode].append((u, energy, m1, m2, q1, q2))
            if abs(u) < 1e-9:
                e0_candidates[mode].append(energy)
        for mode in data:
            data[mode].sort(key=lambda x: x[0])
            if e0_candidates.get(mode):
                ctx['e0'][mode] = np.mean(e0_candidates[mode])
            else:
                ctx['e0'][mode] = data[mode][0][1]
        ctx['csv_data'] = data
        ctx['modes'] = sorted(data.keys())
        return ctx


# === block: score_0 (check id='spin_disp') ===
def score_0(artifact, step, ctx):
        threshold = step.get('threshold', 0.03)
        min_acceptable = step.get('min_acceptable', 0.01)
        data = ctx.get('csv_data')
        if not data:
            return 0.0
        scores = []
        for mode, rows in data.items():
            if len(rows) < 2:
                continue
            nonzero = [(u, m1, m2) for (u, e, m1, m2, q1, q2) in rows if u > 1e-12]
            if not nonzero:
                continue
            nonzero.sort(key=lambda x: x[0])
            _, m1, m2 = nonzero[0]
            delta_m = abs(m1 - m2)
            if delta_m >= threshold:
                scores.append(1.0)
            elif delta_m <= min_acceptable:
                scores.append(0.0)
            else:
                scores.append((delta_m - min_acceptable) / (threshold - min_acceptable))
        if not scores:
            return 0.0
        return float(np.mean(scores))


# === block: score_1 (check id='charge_disp') ===
def score_1(artifact, step, ctx):
        threshold = step.get('threshold', 0.03)
        min_acceptable = step.get('min_acceptable', 0.01)
        data = ctx.get('csv_data')
        if not data:
            return 0.0
        scores = []
        for mode, rows in data.items():
            if len(rows) < 2:
                continue
            nonzero = [(u, q1, q2) for (u, e, m1, m2, q1, q2) in rows if u > 1e-12]
            if not nonzero:
                continue
            nonzero.sort(key=lambda x: x[0])
            _, q1, q2 = nonzero[0]
            delta_q = abs(q1 - q2)
            if delta_q >= threshold:
                scores.append(1.0)
            elif delta_q <= min_acceptable:
                scores.append(0.0)
            else:
                scores.append((delta_q - min_acceptable) / (threshold - min_acceptable))
        if not scores:
            return 0.0
        return float(np.mean(scores))


# === block: score_2 (check id='stiffness_trend') ===
def score_2(artifact, step, ctx):
        softening_ratio_max = step.get('softening_ratio_max', 0.92)
        data = ctx.get('csv_data')
        e0_dict = ctx.get('e0', {})
        if not data:
            return 0.0
        scores = []
        for mode, rows in data.items():
            e0 = e0_dict.get(mode)
            if e0 is None:
                continue
            k_vals = {}
            for u, energy, m1, m2, q1, q2 in rows:
                if u < 1e-12:
                    continue
                de = energy - e0
                k = de / (u * u)
                k_vals[u] = k
            u_small = None
            u_ref = None
            for u in sorted(k_vals.keys()):
                if u <= 0.0015 and u_small is None:
                    u_small = u
                if 0.019 <= u <= 0.021 and u_ref is None:
                    u_ref = u
            if u_small is None or u_ref is None:
                continue
            k_small = k_vals[u_small]
            k_ref = k_vals[u_ref]
            if k_ref <= 0:
                continue
            ratio = k_small / k_ref
            if ratio < softening_ratio_max:
                scores.append(1.0)
            elif ratio < 1.0:
                scores.append(max(0.0, (1.0 - ratio) / (1.0 - softening_ratio_max)))
            else:
                scores.append(0.0)
        if not scores:
            return 0.0
        return float(np.mean(scores))


# === block: score_3 (check id='coeff_consistency') ===
def score_3(artifact, step, ctx):
        a2_rel_tol = step.get('a2_rel_tol', 0.30)
        a3_rel_tol = step.get('a3_rel_tol', 0.40)
        min_a3_a2_ratio = step.get('min_a3_a2_ratio', 0.3)
        data = ctx.get('csv_data')
        e0_dict = ctx.get('e0', {})
        if not data:
            return 0.0
        json_path = os.path.join('/app/outputs', 'fitted_coefficients.json')
        if not os.path.exists(json_path):
            return 0.0
        with open(json_path) as f:
            reported = json.load(f)
        if not isinstance(reported, dict):
            return 0.0
        modes = sorted(data.keys())
        scores = []
        for mode in modes:
            e0 = e0_dict.get(mode)
            if e0 is None:
                continue
            rows = data[mode]
            us = []
            des = []
            for u, energy, m1, m2, q1, q2 in rows:
                if u < 1e-12:
                    continue
                us.append(u)
                des.append(energy - e0)
            if len(us) < 3:
                continue
            us = np.array(us)
            des = np.array(des)
            X = np.column_stack([us**2, us**3])
            try:
                coeffs, residuals, rank, sv = np.linalg.lstsq(X, des, rcond=None)
                a2_refit = float(coeffs[0])
                a3_refit = float(coeffs[1])
            except np.linalg.LinAlgError:
                continue
            mode_key = mode.replace('-', '_').strip().lower()
            if 'breathing' in mode_key and 'half' not in mode_key:
                key = 'breathing'
            elif 'half' in mode_key:
                key = 'half_breathing'
            else:
                key = mode_key
            reported_mode = reported.get(key, {})
            if not isinstance(reported_mode, dict):
                scores.append(0.0)
                continue
            rep_a2 = reported_mode.get('A2')
            rep_a3 = reported_mode.get('A3')
            if rep_a2 is None or rep_a3 is None:
                scores.append(0.0)
                continue
            try:
                rep_a2 = float(rep_a2)
                rep_a3 = float(rep_a3)
            except (TypeError, ValueError):
                scores.append(0.0)
                continue
            denom_a2 = max(abs(a2_refit), 1e-10)
            denom_a3 = max(abs(a3_refit), 1e-10)
            err_a2 = abs(rep_a2 - a2_refit) / denom_a2
            err_a3 = abs(rep_a3 - a3_refit) / denom_a3
            score_a2 = max(0.0, 1.0 - err_a2 / a2_rel_tol) if err_a2 <= a2_rel_tol else 0.0
            score_a3 = max(0.0, 1.0 - err_a3 / a3_rel_tol) if err_a3 <= a3_rel_tol else 0.0
            anharm_ok = 1.0 if (a2_refit > 0 and abs(a3_refit) / max(abs(a2_refit), 1e-10) >= min_a3_a2_ratio) else 0.5
            mode_score = 0.35 * score_a2 + 0.35 * score_a3 + 0.30 * anharm_ok
            scores.append(mode_score)
        if not scores:
            return 0.0
        return float(np.mean(scores))


# === block: score_4 (check id='band_split') ===
def score_4(artifact, step, ctx):
        threshold = step.get('threshold', 3.5)
        min_acceptable = step.get('min_acceptable', 1.0)
        band_path = os.path.join('/app/outputs', 'band_splitting.csv')
        if not os.path.exists(band_path):
            return 0.0
        with open(band_path, newline='') as f:
            reader = csv.DictReader(f)
            band_rows = list(reader)
        if not band_rows:
            return 0.0
        d_vals = []
        for row in band_rows:
            mode = row.get('mode', '').strip().lower()
            if 'full-breathing' not in mode and 'breathing' not in mode:
                continue
            try:
                u = float(row.get('displacement', 0))
            except (ValueError, TypeError):
                continue
            if abs(u - 0.03) > 1e-4:
                continue
            try:
                d = float(row.get('deformation_potential', 0))
            except (ValueError, TypeError):
                continue
            d_vals.append(d)
        if not d_vals:
            return 0.0
        d = max(d_vals)
        if d >= threshold:
            return 1.0
        elif d <= min_acceptable:
            return 0.0
        else:
            return float((d - min_acceptable) / (threshold - min_acceptable))


_SCORERS = {
    'spin_disp': score_0,
    'charge_disp': score_1,
    'stiffness_trend': score_2,
    'coeff_consistency': score_3,
    'band_split': score_4,
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
