import os
import json
import csv

# === author imports / helpers ===
import numpy as np
import csv
import os


def spearman_corr(x, y):
    """Compute Spearman correlation using rank transformation."""
    x_rank = np.argsort(np.argsort(x)).astype(float)
    y_rank = np.argsort(np.argsort(y)).astype(float)
    return np.corrcoef(x_rank, y_rank)[0, 1]


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
    try:
        rows = artifact
        # group by bare_U
        groups = {}
        for r in rows:
            u = float(r['bare_U'])
            if u not in groups:
                groups[u] = []
            groups[u].append({
                'doping': float(r['doping']),
                'hole': float(r['U_eff_hole']),
                'electron': float(r['U_eff_electron'])
            })
        if len(groups) < 2:
            return 0.0
        scores = []
        # monotonic decrease for each series
        mono_fracs = []
        for u, pts in groups.items():
            pts_sorted = sorted(pts, key=lambda x: x['doping'])
            for typ in ['hole', 'electron']:
                vals = [p[typ] for p in pts_sorted]
                cnt = 0
                for i in range(len(vals)-1):
                    if vals[i] >= vals[i+1] - 1e-6:
                        cnt += 1
                if len(vals)-1 > 0:
                    mono_fracs.append(cnt / (len(vals)-1))
        if mono_fracs:
            scores.append(np.mean(mono_fracs))
        else:
            scores.append(0.0)
        # electron−hole asymmetry
        asym_hits = []
        for u, pts in groups.items():
            for p in pts:
                if p['electron'] >= p['hole'] - 1e-6:
                    asym_hits.append(1)
                else:
                    asym_hits.append(0)
        if asym_hits:
            scores.append(np.mean(asym_hits))
        else:
            scores.append(0.0)
        # magnitude bounds
        all_ok = True
        for u, pts in groups.items():
            for p in pts:
                if not (0.0 <= p['hole'] <= u and 0.0 <= p['electron'] <= u):
                    all_ok = False
                    break
            if not all_ok:
                break
        scores.append(1.0 if all_ok else 0.0)
        # U=6t ≥ U=5t (mean comparison)
        u6 = groups.get(6, [])
        u5 = groups.get(5, [])
        if u6 and u5:
            m6h = np.mean([p['hole'] for p in u6])
            m5h = np.mean([p['hole'] for p in u5])
            m6e = np.mean([p['electron'] for p in u6])
            m5e = np.mean([p['electron'] for p in u5])
            ok = 1 if (m6h >= m5h and m6e >= m5e) else 0
            scores.append(ok)
        else:
            scores.append(0.0)
        weights = [0.4, 0.3, 0.2, 0.1]
        final = sum(w * s for w, s in zip(weights, scores))
        return max(0.0, min(1.0, final))
    except:
        return 0.0


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    try:
        rows = artifact
        if len(rows) < 20:
            return 0.0
        d = np.array([float(r['doping']) for r in rows])
        m_op = np.array([float(r['M_OP']) for r in rows])
        m_ip = np.array([float(r['M_IP']) for r in rows])
        # non-negative
        nonneg = 1.0 if (np.all(m_op >= 0) and np.all(m_ip >= 0)) else 0.0
        # M_OP >= M_IP
        ge_frac = np.mean(m_op >= m_ip - 1e-6)
        # monotonic via rank correlation
        try:
            corr_op = spearman_corr(d, m_op)
            corr_ip = spearman_corr(d, m_ip)
        except:
            corr_op = corr_ip = 0.0
        def mono_score(corr):
            if corr <= -0.5:
                return 1.0
            elif corr > 0:
                return 0.0
            else:
                return -corr / 0.5
        sop = mono_score(corr_op)
        sip = mono_score(corr_ip)
        # two-step for M_IP: slope(first half) < slope(second half)
        mid = len(d) // 2
        if mid > 1:
            c1 = np.polyfit(d[:mid], m_ip[:mid], 1)
            s1 = c1[0]
            c2 = np.polyfit(d[mid:], m_ip[mid:], 1)
            s2 = c2[0]
            two_step = 1.0 if s1 <= s2 else 0.0
        else:
            two_step = 0.0
        sub_weights = [0.1, 0.2, 0.3, 0.2, 0.2]
        sub = [nonneg, ge_frac, sop, sip, two_step]
        final = sum(w * s for w, s in zip(sub_weights, sub))
        return max(0.0, min(1.0, final))
    except:
        return 0.0


_SCORERS = {
    'step_01': score_0,
    'step_02': score_1,
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
