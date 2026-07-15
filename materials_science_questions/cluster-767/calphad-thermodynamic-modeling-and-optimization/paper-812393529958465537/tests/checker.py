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
    return {}


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    import math

    tol = step.get("tolerance_abs", 0.001)
    temps = [700.0, 800.0, 900.0]

    # ----------  thermodynamic functions  ----------
    def calc_wg(Wh, Ws, Wv, T_K):
        return Wh - T_K * Ws + 1000.0 * Wv

    def calc_ge(X1, X2, X3, W23, W32, W31, W13, W21, W12, W123):
        Tmp = X3 * X2 * (0.5 - X1)
        Ge = W123 * (X2 * X3 * (1.0 - 2.0 * X1))
        Ge += W23 * (X3 * X2 * (0.5 - X1 - 2.0 * X3))
        Ge += W32 * (X3 * X2 * (0.5 - X1 - 2.0 * X2))
        Ge += W31 * (2.0 * X3 * X1 * (1.0 - X1) + Tmp)
        Ge += W21 * (2.0 * X2 * X1 * (1.0 - X1) + Tmp)
        Ge += W13 * (X3 * X3 * (1.0 - 2.0 * X1) + Tmp)
        Ge += W12 * (X2 * X2 * (1.0 - 2.0 * X1) + Tmp)
        return Ge

    def gibbs(T_K, Xor, Xab):
        Xan = 1.0 - Xor - Xab
        if Xan < 0.0 or Xab < 0.0 or Xor < 0.0:
            return float('inf')
        if Xan > 1.0 or Xab > 1.0 or Xor > 1.0:
            return float('inf')
        Lan = Xan * math.log(Xan) if Xan > 0.0 else 0.0
        Lab = Xab * math.log(Xab) if Xab > 0.0 else 0.0
        Lor = Xor * math.log(Xor) if Xor > 0.0 else 0.0
        Wabor   = calc_wg(18810.0, 10.3,   0.4602, T_K)
        Worab   = calc_wg(27320.0, 10.3,   0.3264, T_K)
        Waban   = calc_wg( 7924.0,  0.0,   0.0,    T_K)
        Wanab   = calc_wg(    0.0,  0.0,   0.0,    T_K)
        Woran   = calc_wg(40317.0,  0.0,   0.0,    T_K)
        Wanor   = calc_wg(38974.0,  0.0,  -0.1037, T_K)
        Waboran = calc_wg(12545.0,  0.0,  -1.095,  T_K)
        Ge_an = calc_ge(Xan, Xor, Xab, Worab, Wabor, Waban, Wanab, Woran, Wanor, Waboran)
        Ge_ab = calc_ge(Xab, Xan, Xor, Wanor, Woran, Worab, Wabor, Wanab, Waban, Waboran)
        Ge_or = calc_ge(Xor, Xab, Xan, Waban, Wanab, Wanor, Woran, Wabor, Worab, Waboran)
        rt = 8.31434 * T_K
        return rt * (Lab + Lan + Lor) + Xab * Ge_ab + Xan * Ge_an + Xor * Ge_or

    # ----------  spinodal search  ----------
    def spinsearch(T_K, x, y, dx, dy):
        oldg = gibbs(T_K, x, y)
        x += dx; y += dy
        lastg = gibbs(T_K, x, y)
        x += dx; y += dy
        g = gibbs(T_K, x, y)
        if g + oldg < 2.0 * lastg:
            x -= 2.0 * dx; y -= 2.0 * dy
            g = oldg
            dx = -dx; dy = -dy
            while g + oldg < 2.0 * lastg:
                oldg = lastg; lastg = g
                x += dx; y += dy
                g = gibbs(T_K, x, y)
        else:
            while g + oldg > 2.0 * lastg:
                oldg = lastg; lastg = g
                x += dx; y += dy
                g = gibbs(T_K, x, y)
        return x - dx, y - dy

    def binspin(T_K, xa, ya, xb, yb):
        dex = (xb - xa) / 20.0
        dey = (yb - ya) / 20.0
        xa, ya = spinsearch(T_K, xa, ya, dex, dey)
        xb, yb = spinsearch(T_K, xb, yb, -dex, -dey)
        return xa, ya, xb, yb

    # ----------  main minimisation loop  ----------
    def solve_equilibrium(T_C):
        T_K = T_C + 273.15
        xa, ya = 0.1, 0.8
        xb, yb = 0.8, 0.1
        xa, ya, xb, yb = binspin(T_K, xa, ya, xb, yb)

        tst1 = 0.001
        tst2 = 0.001
        stp1 = 0.0005
        stp2 = 0.0002
        stp = stp1
        last_g0 = 1.0e10
        g0 = 0.0

        while True:
            if last_g0 > g0:
                stp = stp2
            lxa, lya = xa, ya
            lxb, lyb = xb, yb
            dex = xb - xa
            dey = yb - ya
            del_len = math.sqrt(dex * dex + dey * dey)
            if del_len == 0.0:
                break
            dx = stp * dex / del_len
            dy = stp * dey / del_len

            ga = gibbs(T_K, xa, ya)
            gb = gibbs(T_K, xb, yb)

            while True:
                xat, yat = xa, ya
                xbt, ybt = xb, yb
                dela = delb = 0.5 * del_len
                last_g0_inner = 0.5 * (ga + gb)

                # search for Xa
                xa += dx; ya += dy
                del_len -= stp; dela -= stp
                fa = delb / del_len
                fb = dela / del_len
                ga = gibbs(T_K, xa, ya)
                g0 = fa * ga + fb * gb
                if g0 > last_g0_inner:
                    dx = -dx; dy = -dy; stp = -stp
                while True:
                    xa += dx; ya += dy
                    del_len -= stp; dela -= stp
                    fa = delb / del_len; fb = dela / del_len
                    if fa < 0.0:
                        break
                    ga = gibbs(T_K, xa, ya)
                    g0 = fa * ga + fb * gb
                    if g0 > last_g0_inner:
                        xa -= dx; ya -= dy
                        ga = gibbs(T_K, xa, ya)
                        del_len += stp; dela += stp
                        break
                    last_g0_inner = g0

                # search for Xb
                dela = delb = 0.5 * del_len
                last_g0_inner = 0.5 * (ga + gb)
                xb += dx; yb += dy
                del_len += stp; delb += stp
                fa = delb / del_len; fb = dela / del_len
                gb = gibbs(T_K, xb, yb)
                g0 = fa * ga + fb * gb
                if g0 > last_g0_inner:
                    dx = -dx; dy = -dy; stp = -stp
                while True:
                    xb += dx; yb += dy
                    del_len += stp; delb += stp
                    fa = delb / del_len; fb = dela / del_len
                    if fb < 0.0:
                        break
                    gb = gibbs(T_K, xb, yb)
                    g0 = fa * ga + fb * gb
                    if g0 > last_g0_inner:
                        xb -= dx; yb -= dy
                        gb = gibbs(T_K, xb, yb)
                        del_len -= stp; delb -= stp
                        break
                    last_g0_inner = g0

                if (abs(xa - xat) <= tst1 and abs(ya - yat) <= tst1 and
                    abs(xb - xbt) <= tst1 and abs(yb - ybt) <= tst1):
                    break

            # perpendicular search
            last_g0 = 0.5 * (ga + gb)
            xa += dy; ya -= dx
            g_test_a = gibbs(T_K, xa, ya)
            xb -= dy; yb += dx
            g_test_b = gibbs(T_K, xb, yb)
            g0 = 0.5 * (g_test_a + g_test_b)
            if g0 > last_g0:
                dx, dy = -dx, -dy
            while True:
                last_g0 = g0
                xa += dy; ya -= dx
                g_test_a = gibbs(T_K, xa, ya)
                xb -= dy; yb += dx
                g_test_b = gibbs(T_K, xb, yb)
                g0 = 0.5 * (g_test_a + g_test_b)
                if g0 >= last_g0:
                    break
            xa -= dy; ya += dx
            xb += dy; yb -= dx

            if (abs(xa - lxa) <= tst2 and abs(ya - lya) <= tst2 and
                abs(xb - lxb) <= tst2 and abs(yb - lyb) <= tst2):
                break

        Xor_a = xa
        Xab_a = ya
        Xor_b = xb
        Xab_b = yb
        Xan_a = 1.0 - Xor_a - Xab_a
        Xan_b = 1.0 - Xor_b - Xab_b
        return (Xor_a, Xab_a, Xan_a, Xor_b, Xab_b, Xan_b)

    expected = {}
    for T in temps:
        xa, ya, xan_a, xb, yb, xan_b = solve_equilibrium(T)
        expected[(T, 'A')] = (xa, ya, xan_a)
        expected[(T, 'B')] = (xb, yb, xan_b)

    matches = 0
    total = len(expected) * 3
    for (temp, phase), (exp_xor, exp_xab, exp_xan) in expected.items():
        row = None
        for r in artifact:
            try:
                t_val = float(r['temperature'])
            except (ValueError, KeyError):
                continue
            if abs(t_val - temp) < 1e-6 and str(r.get('phase', '')).strip().upper() == phase.upper():
                row = r
                break
        if row is None:
            continue
        try:
            x_or = float(row['Xor'])
            x_ab = float(row['Xab'])
            x_an = float(row['Xan'])
        except (ValueError, KeyError):
            continue
        if abs(x_or - exp_xor) <= tol:
            matches += 1
        if abs(x_ab - exp_xab) <= tol:
            matches += 1
        if abs(x_an - exp_xan) <= tol:
            matches += 1

    return matches / total if total > 0 else 0.0


_SCORERS = {
    'step_01': score_0,
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
