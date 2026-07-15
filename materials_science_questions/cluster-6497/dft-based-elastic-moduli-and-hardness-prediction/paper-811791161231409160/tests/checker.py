import os
import json
import csv

# === author imports / helpers ===
import csv
import math

# Emulate minimal numpy
class _np:
    @staticmethod
    def array(lst):
        return list(lst)
    @staticmethod
    def argmin(lst):
        if not lst:
            raise ValueError
        return min(range(len(lst)), key=lambda i: lst[i])

np = _np()

# Custom least-squares fit for 2nd-order Birch-Murnaghan
# func is bm2(V, V0, B0); we fit V0, B0 using a simple grid search + linear fit for B0
def curve_fit(func, xdata, ydata, p0=None, **kwargs):
    V = list(xdata)
    P = list(ydata)
    if len(V) == 0:
        return (0, 0), None
    v_min = min(V)
    v_max = max(V)
    best_V0 = None
    best_B0 = None
    best_rss = float('inf')
    # V0 should be slightly above the largest observed volume (zero-pressure volume)
    for V0_cand in range(int(v_max*100)+1, int((v_max+50)*100)+1, 10):
        V0_cand /= 100.0
        sum_b0 = 0.0
        cnt = 0
        for v, p in zip(V, P):
            x = V0_cand / v
            if x <= 0:
                continue
            denom = 1.5 * (x**(7./3.) - x**(5./3.))
            if abs(denom) < 1e-12:
                continue
            sum_b0 += p / denom
            cnt += 1
        if cnt == 0:
            continue
        B0_cand = sum_b0 / cnt
        rss = 0.0
        for v, p in zip(V, P):
            x = V0_cand / v
            p_pred = 1.5 * B0_cand * (x**(7./3.) - x**(5./3.))
            rss += (p - p_pred) ** 2
        if rss < best_rss:
            best_rss = rss
            best_V0 = V0_cand
            best_B0 = B0_cand
    if best_V0 is None:
        return (v_max, 300.0), None
    return (best_V0, best_B0), None


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
    steps = spec.get('steps', [])
    step = steps[0] if steps else {}
    gold = step.get('gold', {})
    return {
        'gold_B0': float(gold.get('B0_GPa', 348.0)),
        'gold_a0': float(gold.get('a0_A', 8.2492)),
        'gold_b0': float(gold.get('b0_A', 8.3067)),
        'gold_c0': float(gold.get('c0_A', 3.01192)),
        'tol_B0': float(step.get('tol_B0_GPa', 15.0)),
        'tol_lattice_rel': float(step.get('tol_lattice_rel', 0.02))
    }


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    def bm2(V, V0, B0):
        return 1.5 * B0 * ((V0/V)**(7./3.) - (V0/V)**(5./3.))

    rows = artifact
    pressures = []
    volumes = []
    lattices = []
    for row in rows:
        pressures.append(float(row['pressure_GPa']))
        volumes.append(float(row['volume_A3']))
        lattices.append((float(row['a_A']), float(row['b_A']), float(row['c_A'])))

    if len(pressures) < 5:
        return 0.0

    # Sort by pressure and check volume monotonic decrease
    indices = sorted(range(len(pressures)), key=lambda i: pressures[i])
    sorted_p = [pressures[i] for i in indices]
    sorted_v = [volumes[i] for i in indices]
    for i in range(1, len(sorted_v)):
        if sorted_v[i] >= sorted_v[i-1] - 1e-9:
            return 0.0

    # Zero-pressure lattice parameters from lowest pressure point
    min_idx = int(np.argmin(pressures))
    a0, b0, c0 = lattices[min_idx]

    # EOS fit
    X = np.array(volumes)
    y = np.array(pressures)
    try:
        popt, _ = curve_fit(bm2, X, y, p0=[200.0, 300.0])
        V0_fit, B0_fit = popt
    except Exception:
        return 0.0

    # B0 score
    gold_B0 = ctx['gold_B0']
    tol_B0 = ctx['tol_B0']
    B0_ok = 1.0 if abs(B0_fit - gold_B0) <= tol_B0 else 0.0

    # Lattice parameter score
    tol_rel = ctx['tol_lattice_rel']
    rel_err_a = abs(a0 - ctx['gold_a0']) / ctx['gold_a0']
    rel_err_b = abs(b0 - ctx['gold_b0']) / ctx['gold_b0']
    rel_err_c = abs(c0 - ctx['gold_c0']) / ctx['gold_c0']
    lattice_ok = 1.0 if (rel_err_a <= tol_rel and rel_err_b <= tol_rel and rel_err_c <= tol_rel) else 0.0

    return 0.8 * B0_ok + 0.2 * lattice_ok


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
