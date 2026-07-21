import os
import json
import csv

# === author imports / helpers ===
import os
import math
import csv
import json
from collections import defaultdict

try:
    import numpy as np
except ImportError:
    import math as np
    np.array = lambda x: list(x)
    np.linspace = lambda a, b, n: [a + (b-a)*i/(n-1) for i in range(n)]
    np.sqrt = math.sqrt


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
        # --- Parameters from the paper (Eq. 14) ---
        params = {
            'Ag': 0.6, 'A3': 0.6, 'A5': 0.8, 'A8': 1.5,
            'QL2': 0.2, 'Q': 0.5
        }
        Ag = params['Ag']
        A3 = params['A3']
        A5 = params['A5']
        A8 = params['A8']
        QL2 = params['QL2']
        Q = params['Q']

        # Q_l = q_{m/l} / Q
        Q0 = 0.0 / Q
        Q13 = (1.0/3.0) / Q
        Q25 = (2.0/5.0) / Q
        Q38 = (3.0/8.0) / Q

        # --- Thermodynamic potentials (Eq. 7) ---
        def phi_IC(A):
            inner = 1.0 + 12.0 * Ag**2 * A
            if inner <= 0.0:
                return None
            return -(1.0/(216.0 * Ag**4)) * (inner**1.5 - (1.0 + 18.0*Ag**2*A))

        def phi_01(A, D0):
            inner = 1.0 + 0.9 * 12.0 * Ag**2 * (A - D0)
            if inner <= 0.0:
                return None
            return -(1.0/(0.54 * 216.0 * Ag**4)) * (inner**1.5 - (1.0 + 0.9*18.0*Ag**2*(A - D0)))

        def phi_13(A, D3):
            coeff = Ag**2 - A3**2
            if coeff <= 0.0:
                return None
            inner = 1.0 + 12.0 * coeff * (A - D3)
            if inner <= 0.0:
                return None
            return -(1.0/(216.0 * coeff**2)) * (inner**1.5 - (1.0 + 18.0*coeff*(A - D3)))

        def phi_ml(A, Dl, Al, l):
            inner = 1.0 + 12.0 * Ag**2 * (A - Dl)
            if inner <= 0.0:
                return None
            first = -(1.0/(216.0 * Ag**4)) * (inner**1.5 - (1.0 + 18.0*Ag**2*(A - Dl)))
            small = (Al/(6.0*Ag**2)) * (math.sqrt(inner) - 1.0)
            if small < 0.0:
                small = 0.0
            second = -(1.0/(2.0*Al)) * (small ** l)
            return first + second

        # --- Bisection root finder ---
        def bisect_root(func, a, b, tol=1e-8, max_iter=100):
            fa = func(a)
            fb = func(b)
            if fa is None or fb is None:
                return None
            if fa * fb > 0.0:
                return None
            for _ in range(max_iter):
                c = (a + b) / 2.0
                fc = func(c)
                if fc is None:
                    return None
                if abs(fc) < tol:
                    return c
                if fa * fc < 0.0:
                    b, fb = c, fc
                else:
                    a, fa = c, fc
            return (a + b) / 2.0

        # --- Generate reference boundary curves ---
        ref_curves = defaultdict(list)

        B2_start = QL2 + 1e-4
        B2_end = 2.0
        n_steps = 800

        for i in range(n_steps):
            B2 = B2_start + (B2_end - B2_start) * i / (n_steps - 1)
            if B2 <= QL2:
                continue

            D0 = 2.0 * (B2**2) * (B2 - QL2)
            D13 = (B2 - QL2) * (Q13**2 + 2.0*(B2 - QL2))
            D25 = (B2 - QL2) * (Q25**2 + 2.0*(B2 - QL2))
            D38 = (B2 - QL2) * (Q38**2 + 2.0*(B2 - QL2))

            A_search_lo = -0.5
            A_search_hi = 2.0

            # IC-C0/1: phi_IC(A) = phi_01(A, D0)
            f = lambda A: (phi_IC(A) or 1e99) - (phi_01(A, D0) or -1e99)
            A_root = bisect_root(f, A_search_lo, A_search_hi)
            if A_root is not None:
                ref_curves['IC-C0/1'].append((D0, A_root))

            # IC-C1/3: phi_IC(A) = phi_13(A, D13)
            f = lambda A: (phi_IC(A) or 1e99) - (phi_13(A, D13) or -1e99)
            A_root = bisect_root(f, A_search_lo, A_search_hi)
            if A_root is not None:
                ref_curves['IC-C1/3'].append((D0, A_root))

            # IC-C2/5: phi_IC(A) = phi_ml(A, D25, A5, 5)
            f = lambda A: (phi_IC(A) or 1e99) - (phi_ml(A, D25, A5, 5) or -1e99)
            A_root = bisect_root(f, A_search_lo, A_search_hi)
            if A_root is not None:
                ref_curves['IC-C2/5'].append((D0, A_root))

            # IC-C3/8: phi_IC(A) = phi_ml(A, D38, A8, 8)
            f = lambda A: (phi_IC(A) or 1e99) - (phi_ml(A, D38, A8, 8) or -1e99)
            A_root = bisect_root(f, A_search_lo, A_search_hi)
            if A_root is not None:
                ref_curves['IC-C3/8'].append((D0, A_root))

            # C1/3-C0/1: phi_13(A, D13) = phi_01(A, D0)
            f = lambda A: (phi_13(A, D13) or 1e99) - (phi_01(A, D0) or -1e99)
            A_root = bisect_root(f, A_search_lo, A_search_hi)
            if A_root is not None:
                ref_curves['C1/3-C0/1'].append((D0, A_root))

            # C2/5-C1/3: phi_ml(A, D25, A5, 5) = phi_13(A, D13)
            f = lambda A: (phi_ml(A, D25, A5, 5) or 1e99) - (phi_13(A, D13) or -1e99)
            A_root = bisect_root(f, A_search_lo, A_search_hi)
            if A_root is not None:
                ref_curves['C2/5-C1/3'].append((D0, A_root))

        # Convert to numpy-style lists for distance lookups
        ref_curves_final = {}
        for pp, pts in ref_curves.items():
            if pts:
                ref_curves_final[pp] = {
                    'D0': [p[0] for p in pts],
                    'A': [p[1] for p in pts]
                }

        return {'params': params, 'ref_curves': ref_curves_final}


# === block: score_0 (check id='phase_boundaries_check') ===
def score_0(artifact, step, ctx):
        # --- Fixed model parameters ---
        Ag = 0.6; A3 = 0.6; A5 = 0.8; A8 = 1.5
        QL2 = 0.2; Q = 0.5
        Q13 = (1.0/3.0) / Q
        Q25 = (2.0/5.0) / Q
        Q38 = (3.0/8.0) / Q

        # --- Thermodynamic potentials (Eq. 7) ---
        def phi_IC(A):
            inner = 1.0 + 12.0 * Ag**2 * A
            if inner <= 0.0:
                return None
            return -(1.0/(216.0 * Ag**4)) * (inner**1.5 - (1.0 + 18.0*Ag**2*A))

        def phi_01(A, D0):
            inner = 1.0 + 0.9 * 12.0 * Ag**2 * (A - D0)
            if inner <= 0.0:
                return None
            return -(1.0/(0.54 * 216.0 * Ag**4)) * (inner**1.5 - (1.0 + 0.9*18.0*Ag**2*(A - D0)))

        def phi_13(A, D3):
            coeff = Ag**2 - A3**2
            if coeff <= 0.0:
                return None
            inner = 1.0 + 12.0 * coeff * (A - D3)
            if inner <= 0.0:
                return None
            return -(1.0/(216.0 * coeff**2)) * (inner**1.5 - (1.0 + 18.0*coeff*(A - D3)))

        def phi_ml(A, Dl, Al, l):
            inner = 1.0 + 12.0 * Ag**2 * (A - Dl)
            if inner <= 0.0:
                return None
            first = -(1.0/(216.0 * Ag**4)) * (inner**1.5 - (1.0 + 18.0*Ag**2*(A - Dl)))
            small = (Al/(6.0*Ag**2)) * (math.sqrt(inner) - 1.0)
            if small < 0.0:
                small = 0.0
            second = -(1.0/(2.0*Al)) * (small ** l)
            return first + second

        # --- Map D0 -> B² by solving 2 x² (x - QL²) = D0 ---
        def get_B2(D0):
            if D0 <= 0.0:
                # smallest valid B² is QL², giving D0=0
                return QL2
            lo = QL2
            hi = max(1.0, D0)  # safe upper bound
            # ensure f(lo) <= D0, f(hi) >= D0
            f = lambda x: 2.0 * x**2 * (x - QL2)
            f_lo = f(lo)
            if f_lo > D0:
                return lo  # D0 very small, B² very close to QL²
            # expand hi until f(hi) >= D0
            while f(hi) < D0:
                hi *= 2.0
            for _ in range(80):
                mid = (lo + hi) / 2.0
                f_mid = f(mid)
                if f_mid < D0:
                    lo = mid
                else:
                    hi = mid
                if hi - lo < 1e-12:
                    break
            return (lo + hi) / 2.0

        # --- Generic root finder for A with sign scanning ---
        def solve_boundary_A(D0, pair_key):
            # Returns A (float) or None
            if D0 < 0.0:
                return None
            B2 = get_B2(D0)
            # Compute needed D_l values
            # D13 = (B² - QL²) [ Q13² + 2(B² - QL²) ]
            dB = B2 - QL2
            D13 = dB * (Q13**2 + 2.0 * dB)
            D25 = dB * (Q25**2 + 2.0 * dB)
            D38 = dB * (Q38**2 + 2.0 * dB)  # not needed for required pairs but available

            # choose the two potentials to equate
            if pair_key == 'IC-C0/1':
                fdiff = lambda A: (phi_IC(A) or 1e99) - (phi_01(A, D0) or -1e99)
            elif pair_key == 'IC-C1/3':
                fdiff = lambda A: (phi_IC(A) or 1e99) - (phi_13(A, D13) or -1e99)
            elif pair_key == 'IC-C2/5':
                fdiff = lambda A: (phi_IC(A) or 1e99) - (phi_ml(A, D25, A5, 5) or -1e99)
            elif pair_key == 'IC-C3/8':
                fdiff = lambda A: (phi_IC(A) or 1e99) - (phi_ml(A, D38, A8, 8) or -1e99)
            elif pair_key == 'C1/3-C0/1':
                fdiff = lambda A: (phi_13(A, D13) or 1e99) - (phi_01(A, D0) or -1e99)
            elif pair_key == 'C2/5-C1/3':
                fdiff = lambda A: (phi_ml(A, D25, A5, 5) or 1e99) - (phi_13(A, D13) or -1e99)
            else:
                return None

            # scan A from 0 to 2.0 for sign change
            A_start = 0.0
            A_end = 2.0
            step = 0.005
            f_prev = None
            A_prev = None
            for A_val in [A_start + i*step for i in range(int((A_end-A_start)/step)+1)]:
                f_val = fdiff(A_val)
                if f_val is None:
                    continue
                if f_prev is not None and f_val * f_prev < 0.0:
                    # root between A_prev and A_val
                    lo, hi = A_prev, A_val
                    flo, fhi = f_prev, f_val
                    for _ in range(60):
                        mid = (lo + hi) / 2.0
                        fmid = fdiff(mid)
                        if fmid is None:
                            return None
                        if abs(fmid) < 1e-8:
                            return mid
                        if flo * fmid < 0.0:
                            hi, fhi = mid, fmid
                        else:
                            lo, flo = mid, fmid
                    return (lo + hi) / 2.0
                f_prev = f_val
                A_prev = A_val
            # no sign change
            return None

        # --- Build reference curves for required pairs ---
        tolerance_A = float(step.get('tolerance_A', 0.05))
        required_pairs = step.get('required_phase_pairs', [])
        ref_curves = {}
        D0_min = 0.0
        D0_max = 0.6  # covers the phase diagram region in Fig.2
        n_ref = 600
        for pp in required_pairs:
            d0_arr = []
            a_arr = []
            for i in range(n_ref):
                d0_val = D0_min + (D0_max - D0_min) * i / (n_ref - 1)
                a_root = solve_boundary_A(d0_val, pp)
                if a_root is not None:
                    d0_arr.append(d0_val)
                    a_arr.append(a_root)
            if len(d0_arr) >= 2:
                # sort by D0
                sorted_idx = sorted(range(len(d0_arr)), key=lambda k: d0_arr[k])
                ref_curves[pp] = {
                    'D0': [d0_arr[k] for k in sorted_idx],
                    'A': [a_arr[k] for k in sorted_idx]
                }

        # --- Sub-score 1: shape gate (0.05) ---
        if artifact is None or not isinstance(artifact, list) or len(artifact) == 0:
            return 0.0
        if not all(col in (artifact[0] or {}) for col in ['phase_pair', 'D0', 'A']):
            return 0.0
        score_shape = 0.05

        # --- Parse agent points ---
        def normalize_pp(pp):
            pp = str(pp).strip()
            parts = pp.split('-')
            if len(parts) == 2:
                a_p, b_p = parts[0].strip(), parts[1].strip()
                if 'IC' in a_p and 'IC' not in b_p:
                    return a_p + '-' + b_p
                if 'IC' in b_p and 'IC' not in a_p:
                    return b_p + '-' + a_p
                if a_p > b_p:
                    return b_p + '-' + a_p
                if a_p < b_p:
                    return a_p + '-' + b_p
                return pp
            return pp

        agent_points = defaultdict(list)
        for row in artifact:
            pp_raw = row.get('phase_pair', '')
            pp = normalize_pp(pp_raw)
            try:
                d0 = float(row.get('D0', float('nan')))
                a_val = float(row.get('A', float('nan')))
            except (ValueError, TypeError):
                continue
            if math.isfinite(d0) and math.isfinite(a_val):
                agent_points[pp].append((d0, a_val))

        # --- Sub-score 2: required boundary coverage (0.20) ---
        present_pairs = []
        for req_pair in required_pairs:
            norm_req = normalize_pp(req_pair)
            if norm_req in agent_points and len(agent_points[norm_req]) >= 3:
                present_pairs.append(norm_req)
        coverage_ratio = len(present_pairs) / max(len(required_pairs), 1)
        score_coverage = 0.20 * coverage_ratio

        # --- Sub-score 3: point accuracy (0.50) using interpolation ---
        total_points = 0
        matched_points = 0

        def linear_interp(x, xs, ys):
            if len(xs) < 2:
                return ys[0] if xs else None
            if x <= xs[0]:
                return ys[0]
            if x >= xs[-1]:
                return ys[-1]
            for i in range(len(xs) - 1):
                if xs[i] <= x <= xs[i+1]:
                    frac = (x - xs[i]) / (xs[i+1] - xs[i])
                    return ys[i] + frac * (ys[i+1] - ys[i])
            return ys[-1]

        for pp, pts in agent_points.items():
            if pp not in ref_curves:
                continue
            ref_d0 = ref_curves[pp]['D0']
            ref_a = ref_curves[pp]['A']
            if len(ref_d0) < 2:
                continue
            d0_min = ref_d0[0]
            d0_max = ref_d0[-1]
            for (agent_d0, agent_a) in pts:
                if agent_d0 < d0_min - 1e-6 or agent_d0 > d0_max + 1e-6:
                    continue
                total_points += 1
                ref_a_at_d0 = linear_interp(agent_d0, ref_d0, ref_a)
                if ref_a_at_d0 is not None and abs(agent_a - ref_a_at_d0) <= tolerance_A:
                    matched_points += 1

        if total_points > 0:
            accuracy_ratio = matched_points / total_points
        else:
            accuracy_ratio = 0.0
        score_accuracy = 0.50 * accuracy_ratio

        # --- Sub-score 4: C_{2/5} region verification (0.25) ---
        score_c25 = 0.0
        pp_ic_c25 = normalize_pp('IC-C2/5')
        pp_c25_c13 = normalize_pp('C2/5-C1/3')

        if pp_ic_c25 in agent_points and pp_c25_c13 in agent_points:
            pts_ic = agent_points[pp_ic_c25]
            pts_cc = agent_points[pp_c25_c13]
            separations = []
            for (d0_a, a_a) in pts_ic:
                for (d0_b, a_b) in pts_cc:
                    if abs(d0_a - d0_b) < 0.05:
                        separations.append(abs(a_a - a_b))
            if separations:
                avg_sep = sum(separations) / len(separations)
                if avg_sep > 0.005:
                    score_c25 = 0.25
                elif avg_sep > 0.001:
                    score_c25 = 0.15
                else:
                    score_c25 = 0.05
            else:
                score_c25 = 0.10
        elif pp_ic_c25 in agent_points or pp_c25_c13 in agent_points:
            score_c25 = 0.05

        # --- Combine ---
        total_score = score_shape + score_coverage + score_accuracy + score_c25
        return min(max(total_score, 0.0), 1.0)


_SCORERS = {
    'phase_boundaries_check': score_0,
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
