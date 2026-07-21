import os
import json
import csv

# === author imports / helpers ===
import math, json

class _Array:
    __slots__ = ('_data',)
    def __init__(self, data):
        self._data = list(data)
    def __iter__(self):
        return iter(self._data)
    def __len__(self):
        return len(self._data)
    def __getitem__(self, idx):
        return self._data[idx]
    def __ge__(self, other):
        return _Array([x >= other for x in self._data])
    def __le__(self, other):
        return _Array([x <= other for x in self._data])

class _Numpy:
    @staticmethod
    def array(iterable):
        if isinstance(iterable, _Array):
            return iterable
        return _Array(iterable)
    @staticmethod
    def where(cond):
        if isinstance(cond, _Array):
            return [i for i, v in enumerate(cond) if v]
        return [i for i, v in enumerate(cond) if v]
    @staticmethod
    def mean(seq):
        if not seq:
            return 0.0
        return sum(seq) / len(seq)

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


# === block: score_0 (check id='step_02_ge_scan') ===
def score_0(artifact, step, ctx):
    data = artifact
    rows = []
    for r in data:
        try:
            t = float(r['T'])
            th = float(r['theta'])
            al = float(r['alpha'])
            sb = float(r['S_bar'])
            m2 = float(r['m2_bar'])
            rows.append((t, th, al, sb, m2))
        except:
            continue
    if len(rows) < 2:
        return 0.0
    rows.sort(key=lambda x: x[0])
    T = np.array([r[0] for r in rows])
    theta = np.array([r[1] for r in rows])
    alpha = np.array([r[2] for r in rows])
    S_bar = np.array([r[3] for r in rows])
    m2_bar = np.array([r[4] for r in rows])
    gold = step['gold']
    tol_cfg = step['tol']
    det = step['detection']
    low_T_rows = [(t, th, al, sb, m2) for t, th, al, sb, m2 in zip(T, theta, alpha, S_bar, m2_bar) if t <= 50]
    if not low_T_rows:
        low_T_rows = [(T[0], theta[0], alpha[0], S_bar[0], m2_bar[0])]
    avg_th = np.mean([r[1] for r in low_T_rows])
    avg_al = np.mean([r[2] for r in low_T_rows])
    avg_sb = np.mean([r[3] for r in low_T_rows])
    avg_m2 = np.mean([r[4] for r in low_T_rows])
    def tolerance_score(val, ref, tol_abs):
        err = abs(val - ref)
        if err <= tol_abs:
            return 1.0
        return max(0.0, 1.0 - (err - tol_abs) / tol_abs)
    low_th = tolerance_score(avg_th, gold['low_T_theta'], tol_cfg['low_theta_abs'])
    low_al = tolerance_score(avg_al, gold['low_T_alpha'], tol_cfg['low_alpha_abs'])
    low_sb = tolerance_score(avg_sb, gold['low_T_S_bar'], tol_cfg['low_S_bar_abs'])
    low_m2 = tolerance_score(avg_m2, gold['low_T_m2_bar'], tol_cfg['low_m2_bar_abs'])
    lowT_score = (low_th + low_al + low_sb + low_m2) / 4.0

    def find_crossing(T_arr, y, thresh, increasing):
        if increasing:
            idx = np.where(y >= thresh)[0]
        else:
            idx = np.where(y <= thresh)[0]
        if len(idx) == 0:
            return None
        i = idx[0]
        if i == 0:
            return float(T_arr[0])
        x0, x1 = T_arr[i-1], T_arr[i]
        y0, y1 = y[i-1], y[i]
        if abs(y1 - y0) < 1e-12:
            return float((x0 + x1) / 2)
        return float(x0 + (x1 - x0) * (thresh - y0) / (y1 - y0))

    tc1_measure = det['Tc1_measure']
    tc1_thresh = det['Tc1_threshold']
    tc1_inc = det['Tc1_increasing']
    tc2_measure = det['Tc2_measure']
    tc2_thresh = det['Tc2_threshold']
    tc2_inc = det['Tc2_increasing']
    tc3_thresh = det['Tc3_threshold']
    tc3_inc = det['Tc3_increasing']

    y1 = theta if tc1_measure == 'theta' else alpha
    tc1 = find_crossing(T, y1, tc1_thresh, tc1_inc)
    y2 = theta if tc2_measure == 'theta' else alpha
    tc2 = find_crossing(T, y2, tc2_thresh, tc2_inc)
    tc3 = find_crossing(T, S_bar, tc3_thresh, tc3_inc)

    def tc_score(tc_ext, gold_tc, tol_rel):
        if tc_ext is None:
            return 0.0
        err = abs(tc_ext - gold_tc)
        tol = tol_rel * gold_tc
        if err <= tol:
            return 1.0
        return max(0.0, 1.0 - (err - tol) / tol)

    reltol = tol_cfg['Tc_rel']
    s1 = tc_score(tc1, gold['Tc1'], reltol)
    s2 = tc_score(tc2, gold['Tc2'], reltol)
    s3 = tc_score(tc3, gold['Tc3'], reltol)
    tc_avg = (s1 + s2 + s3) / 3.0

    seq_score = 0.0
    if tc1 is not None and tc2 is not None and tc3 is not None:
        if tc1 < tc2 < tc3:
            seq_score = 1.0
        elif tc1 < tc3 and tc2 < tc3:
            seq_score = 0.5
        else:
            seq_score = 0.0

    w_tc = 0.4
    w_seq = 0.3
    w_low = 0.3
    total = w_tc * tc_avg + w_seq * seq_score + w_low * lowT_score
    return float(total)


# === block: score_1 (check id='step_03_si_scan') ===
def score_1(artifact, step, ctx):
    data = artifact
    rows = []
    for r in data:
        try:
            t = float(r['T'])
            th = float(r['theta'])
            al = float(r['alpha'])
            sb = float(r['S_bar'])
            m2 = float(r['m2_bar'])
            rows.append((t, th, al, sb, m2))
        except:
            continue
    if len(rows) < 2:
        return 0.0
    rows.sort(key=lambda x: x[0])
    T = np.array([r[0] for r in rows])
    theta = np.array([r[1] for r in rows])
    alpha = np.array([r[2] for r in rows])
    S_bar = np.array([r[3] for r in rows])
    m2_bar = np.array([r[4] for r in rows])
    gold = step['gold']
    tol_cfg = step['tol']
    det = step['detection']
    low_T_rows = [(t, th, al, sb, m2) for t, th, al, sb, m2 in zip(T, theta, alpha, S_bar, m2_bar) if t <= 50]
    if not low_T_rows:
        low_T_rows = [(T[0], theta[0], alpha[0], S_bar[0], m2_bar[0])]
    avg_th = np.mean([r[1] for r in low_T_rows])
    avg_al = np.mean([r[2] for r in low_T_rows])
    avg_sb = np.mean([r[3] for r in low_T_rows])
    avg_m2 = np.mean([r[4] for r in low_T_rows])
    def tolerance_score(val, ref, tol_abs):
        err = abs(val - ref)
        if err <= tol_abs:
            return 1.0
        return max(0.0, 1.0 - (err - tol_abs) / tol_abs)
    low_th = tolerance_score(avg_th, gold['low_T_theta'], tol_cfg['low_theta_abs'])
    low_al = tolerance_score(avg_al, gold['low_T_alpha'], tol_cfg['low_alpha_abs'])
    low_sb = tolerance_score(avg_sb, gold['low_T_S_bar'], tol_cfg['low_S_bar_abs'])
    low_m2 = tolerance_score(avg_m2, gold['low_T_m2_bar'], tol_cfg['low_m2_bar_abs'])
    lowT_score = (low_th + low_al + low_sb + low_m2) / 4.0

    def find_crossing(T_arr, y, thresh, increasing):
        if increasing:
            idx = np.where(y >= thresh)[0]
        else:
            idx = np.where(y <= thresh)[0]
        if len(idx) == 0:
            return None
        i = idx[0]
        if i == 0:
            return float(T_arr[0])
        x0, x1 = T_arr[i-1], T_arr[i]
        y0, y1 = y[i-1], y[i]
        if abs(y1 - y0) < 1e-12:
            return float((x0 + x1) / 2)
        return float(x0 + (x1 - x0) * (thresh - y0) / (y1 - y0))

    tc1_measure = det['Tc1_measure']
    tc1_thresh = det['Tc1_threshold']
    tc1_inc = det['Tc1_increasing']
    tc2_measure = det['Tc2_measure']
    tc2_thresh = det['Tc2_threshold']
    tc2_inc = det['Tc2_increasing']
    tc3_thresh = det['Tc3_threshold']
    tc3_inc = det['Tc3_increasing']

    y1 = theta if tc1_measure == 'theta' else alpha
    tc1 = find_crossing(T, y1, tc1_thresh, tc1_inc)
    y2 = theta if tc2_measure == 'theta' else alpha
    tc2 = find_crossing(T, y2, tc2_thresh, tc2_inc)
    tc3 = find_crossing(T, S_bar, tc3_thresh, tc3_inc)

    def tc_score(tc_ext, gold_tc, tol_rel):
        if tc_ext is None:
            return 0.0
        err = abs(tc_ext - gold_tc)
        tol = tol_rel * gold_tc
        if err <= tol:
            return 1.0
        return max(0.0, 1.0 - (err - tol) / tol)

    reltol = tol_cfg['Tc_rel']
    s1 = tc_score(tc1, gold['Tc1'], reltol)
    s2 = tc_score(tc2, gold['Tc2'], reltol)
    s3 = tc_score(tc3, gold['Tc3'], reltol)
    tc_avg = (s1 + s2 + s3) / 3.0

    seq_score = 0.0
    if tc1 is not None and tc2 is not None and tc3 is not None:
        if tc1 < tc2 < tc3:
            seq_score = 1.0
        elif tc1 < tc3 and tc2 < tc3:
            seq_score = 0.5
        else:
            seq_score = 0.0

    w_tc = 0.4
    w_seq = 0.3
    w_low = 0.3
    total = w_tc * tc_avg + w_seq * seq_score + w_low * lowT_score
    return float(total)


_SCORERS = {
    'step_02_ge_scan': score_0,
    'step_03_si_scan': score_1,
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
