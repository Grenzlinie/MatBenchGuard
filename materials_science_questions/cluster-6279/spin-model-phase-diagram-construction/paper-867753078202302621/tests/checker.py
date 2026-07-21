import os
import json
import csv

# === author imports / helpers ===
import math

try:
    import numpy as np
except ImportError:
    class _Ndarray:
        def __init__(self, data, shape=None):
            if isinstance(data, list):
                self.data = data
            else:
                self.data = list(data)
            self.shape = shape if shape else (len(self.data),)

        def __getitem__(self, idx):
            return self.data[idx]

        def __sub__(self, other):
            if isinstance(other, _Ndarray):
                return _Ndarray([a-b for a,b in zip(self.data, other.data)])
            else:
                return _Ndarray([x - other for x in self.data])

        def __mul__(self, other):
            if isinstance(other, _Ndarray):
                return _Ndarray([a*b for a,b in zip(self.data, other.data)])
            else:
                return _Ndarray([x * other for x in self.data])

        def __len__(self):
            return len(self.data)

        def reshape(self, *args):
            if args == (-1, 1) or args == (len(self.data), 1):
                return _Ndarray([[x] for x in self.data], shape=(len(self.data), 1))
            return self

        def __iter__(self):
            return iter(self.data)

    class _Numpy:
        pi = math.pi

        def asarray(self, x, dtype=None):
            if isinstance(x, _Ndarray):
                return x
            return _Ndarray(list(x))

        def array(self, x):
            return self.asarray(x)

        def vstack(self, tup):
            x, ones = tup
            A_data = [[x_i, 1.0] for x_i in x]
            return _Ndarray(A_data, shape=(len(x), 2))

        def ones_like(self, x):
            return [1.0] * len(x)

        class linalg:
            @staticmethod
            def lstsq(A, y, rcond=None):
                if isinstance(A, _Ndarray):
                    A = A.data
                if isinstance(y, _Ndarray):
                    y = y.data
                n = len(A)
                m = len(A[0])
                if m == 1:
                    sum_xy = sum(A[i][0] * y[i] for i in range(n))
                    sum_x2 = sum(A[i][0] ** 2 for i in range(n))
                    if sum_x2 == 0:
                        return [[0.0]], None
                    return [[sum_xy / sum_x2]], None
                if m == 2:
                    sum_x = sum(row[0] for row in A)
                    sum_y = sum(y)
                    sum_x2 = sum(row[0] ** 2 for row in A)
                    sum_xy = sum(row[0] * y[i] for i, row in enumerate(A))
                    det = n * sum_x2 - sum_x * sum_x
                    if abs(det) < 1e-15:
                        return [[0.0, 0.0]], None
                    m_val = (n * sum_xy - sum_x * sum_y) / det
                    b_val = (sum_x2 * sum_y - sum_x * sum_xy) / det
                    return [[m_val, b_val]], None
                return [[0.0] * m], None

    np = _Numpy()


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


# === block: score_0 (check id='scaling_analysis') ===
def score_0(artifact, step, ctx):
    alpha_list = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]

    # Corrected gold from digitized Fig. 3(b) of the actual paper (cond‑mat/9905311)
    gold_cfg = {
        "alpha_list": alpha_list,
        "delta_1.0": {
            "alpha_c": -0.2,
            "c":       [0.90, 0.88, 0.86, 0.84, 0.82, 0.80, 0.78, 0.76, 0.74, 0.72, 0.70, 0.70, 0.70, 0.70, 0.70, 0.70],
            "eta":     [0.15, 0.13, 0.10, 0.08, 0.06, 0.04, 0.03, 0.02, 0.01, 0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0]
        },
        "delta_0.6": {
            "alpha_c": -0.4,
            "c":       [0.85, 0.83, 0.81, 0.79, 0.77, 0.75, 0.73, 0.71, 0.70, 0.70, 0.70, 0.70, 0.70, 0.70, 0.70, 0.70],
            "eta":     [0.12, 0.10, 0.08, 0.06, 0.05, 0.04, 0.03, 0.02, 0.01, 0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0]
        }
    }

    tol_c = 0.15
    tol_eta = 0.1
    tol_ac = 0.15

    def regress(x, y, intercept=True):
        n = len(x)
        if n == 0:
            return (0.0, 0.0) if intercept else (0.0, 0.0)
        sum_x = sum(x)
        sum_y = sum(y)
        sum_xy = sum(xi * yi for xi, yi in zip(x, y))
        if intercept:
            sum_x2 = sum(xi * xi for xi in x)
            denom = n * sum_x2 - sum_x * sum_x
            if abs(denom) < 1e-15:
                return 0.0, 0.0
            m = (n * sum_xy - sum_x * sum_y) / denom
            b = (sum_y - m * sum_x) / n
            return m, b
        else:
            sum_x2 = sum(xi * xi for xi in x)
            if sum_x2 == 0:
                return 0.0, 0.0
            m = sum_xy / sum_x2
            return m, 0.0

    def compute_c_and_eta(data_points):
        c_list = []
        eta_list = []
        alphas = []
        for dp in data_points:
            alpha = dp['alpha']
            vs = dp['vs']
            energies_raw = dp.get('energies', [])
            # Use only the plateau magnetization sector M = N//2
            energies = {e['N']: e['E'] for e in energies_raw if e['M'] == e['N'] // 2}
            H_data = {h['N']: h for h in dp.get('H_plus_minus', [])}
            Ns = sorted([N for N in H_data if N in energies])
            if len(Ns) < 3:
                continue
            # c from E/N vs 1/N^2
            X = []
            Y = []
            for N in Ns:
                E0 = energies.get(N)
                if E0 is None:
                    continue
                Y.append(E0 / N)
                X.append(1.0 / (N * N))
            if len(X) < 3:
                continue
            slope, _ = regress(X, Y, intercept=True)
            c = -slope / (math.pi * vs) if vs != 0 else 0.0
            c_list.append(c)
            # eta from Δ_N vs 1/N
            Xd = []
            Yd = []
            for N in Ns:
                h = H_data.get(N)
                if h is None:
                    continue
                delta = h['H_plus'] - h['H_minus']
                if vs == 0:
                    continue
                Xd.append(1.0 / N)
                Yd.append(delta)
            if len(Xd) < 3:
                continue
            slope_d, _ = regress(Xd, Yd, intercept=False)
            eta = slope_d / (2.0 * math.pi * vs) if vs != 0 else 0.0
            eta_list.append(eta)
            alphas.append(alpha)
        return alphas, c_list, eta_list

    def find_alpha_c(alphas, etas, target=0.25):
        if len(alphas) < 2:
            return None
        signs = [e - target for e in etas]
        for i in range(len(signs)-1):
            if signs[i] * signs[i+1] <= 0 and signs[i] != signs[i+1]:
                a0, a1 = alphas[i], alphas[i+1]
                e0, e1 = etas[i], etas[i+1]
                if e1 != e0:
                    return a0 + (target - e0) * (a1 - a0) / (e1 - e0)
        return None

    def score_component(values, golds, tolerance):
        if not values or not golds:
            return 0.0
        total = 0.0
        n = 0
        for v, g in zip(values, golds):
            if tolerance <= 0:
                n += 1
                continue
            dev = abs(v - g) / tolerance
            score = max(0.0, 1.0 - dev)
            total += score
            n += 1
        if n == 0:
            return 0.0
        return total / n

    total_score = 0.0
    count = 0
    for delta_key in ['delta_1.0', 'delta_0.6']:
        if delta_key not in artifact:
            continue
        gold_cfg_delta = gold_cfg.get(delta_key)
        if not gold_cfg_delta:
            continue
        alpha_c_gold = gold_cfg_delta['alpha_c']
        c_gold = gold_cfg_delta['c']
        eta_gold = gold_cfg_delta['eta']
        data_delta = artifact[delta_key]
        data_delta = sorted(data_delta, key=lambda x: x.get('alpha', 0.0))
        alphas, cs, etas = compute_c_and_eta(data_delta)
        # score c
        if cs:
            gold_c = []
            for a in alphas:
                if a in alpha_list:
                    idx = alpha_list.index(a)
                    gold_c.append(c_gold[idx])
                else:
                    continue
            if gold_c:
                sc_c = score_component(cs[:len(gold_c)], gold_c, tol_c)
            else:
                sc_c = 0.0
        else:
            sc_c = 0.0
        # score eta
        if etas:
            gold_eta = []
            for a in alphas:
                if a in alpha_list:
                    idx = alpha_list.index(a)
                    gold_eta.append(eta_gold[idx])
                else:
                    continue
            if gold_eta:
                sc_eta = score_component(etas[:len(gold_eta)], gold_eta, tol_eta)
            else:
                sc_eta = 0.0
        else:
            sc_eta = 0.0
        # find alpha_c from computed etas (requires data that brackets the crossing)
        alpha_c_comp = find_alpha_c(alphas, etas)
        if alpha_c_comp is not None:
            dev_ac = abs(alpha_c_comp - alpha_c_gold)
            sc_ac = max(0.0, 1.0 - dev_ac / tol_ac)
        else:
            sc_ac = 0.0
        # weights
        w_c = 0.25
        w_eta = 0.25
        w_ac = 0.5
        delta_score = w_c * sc_c + w_eta * sc_eta + w_ac * sc_ac
        total_score += delta_score
        count += 1

    if count == 0:
        return 0.0
    return total_score / count


_SCORERS = {
    'scaling_analysis': score_0,
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
