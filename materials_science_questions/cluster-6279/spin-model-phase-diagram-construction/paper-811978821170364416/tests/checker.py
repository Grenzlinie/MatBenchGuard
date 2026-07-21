import os
import json
import csv

# === author imports / helpers ===
import os
import csv
import collections


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
        def load_csv(path):
            with open(path, newline='') as f:
                return list(csv.DictReader(f))
        pb_path = os.path.join(outputs_dir, 'phase_boundary.csv')
        mag_path = os.path.join(outputs_dir, 'magnetization.csv')
        phase_boundary = load_csv(pb_path) if os.path.exists(pb_path) else []
        magnetization = load_csv(mag_path) if os.path.exists(mag_path) else []
        ref_alpha_c = {0.0: 1.0, 0.5: 1.4, 1.0: 1.9, 1.5: 2.4}
        tol_alpha_c = 0.15
        tol_Tc = 0.2
        return {
            'phase_boundary': phase_boundary,
            'magnetization': magnetization,
            'ref_alpha_c': ref_alpha_c,
            'tol_alpha_c': tol_alpha_c,
            'tol_Tc': tol_Tc
        }


# === block: score_0 (check id='phase_boundary_check') ===
def score_0(artifact, step, ctx):
    data = artifact
    if not data:
        return 0.0
    ref = {0.0: 1.0, 0.5: 1.4, 1.0: 1.9, 1.5: 2.4}
    tol = 0.15
    groups = collections.defaultdict(list)
    for row in data:
        try:
            d = float(row['D_over_J'])
            a = float(row['alpha'])
            tc = float(row['T_c'])
            order = row['transition_order'].strip().lower()
        except (ValueError, KeyError):
            return 0.0
        groups[d].append((a, tc, order))
    # alpha_c scoring
    scores = []
    for d in sorted(ref.keys()):
        if d not in groups:
            scores.append(0.0)
            continue
        rows = sorted(groups[d], key=lambda x: x[0])
        alpha_c = None
        for a, tc, order in rows:
            if order == 'first':
                alpha_c = a
                break
        if alpha_c is None:
            scores.append(0.0)
            continue
        diff = abs(alpha_c - ref[d])
        if diff <= tol:
            scores.append(1.0)
        else:
            scores.append(max(0.0, 1.0 - (diff - tol) / 0.5))
    avg_alpha_score = sum(scores) / len(scores) if scores else 0.0
    # order consistency
    order_ok = True
    for d, rows in groups.items():
        rows = sorted(rows, key=lambda x: x[0])
        found_first = False
        for a, tc, order in rows:
            if order == 'first':
                found_first = True
            elif found_first and order == 'second':
                order_ok = False
                break
        if not order_ok:
            break
    order_score = 1.0 if order_ok else 0.0
    return avg_alpha_score * 0.7 + order_score * 0.3


# === block: score_1 (check id='magnetization_check') ===
def score_1(artifact, step, ctx):
    phase_b = ctx['phase_boundary']
    mag = ctx['magnetization']
    tol_Tc = ctx['tol_Tc']
    if not mag or not phase_b:
        return 0.0
    # index phase boundary
    pb = {}
    for row in phase_b:
        try:
            d = float(row['D_over_J'])
            a = float(row['alpha'])
            tc = float(row['T_c'])
            order = row['transition_order'].strip().lower()
            pb[(d, a)] = {'Tc': tc, 'order': order}
        except (ValueError, KeyError):
            pass
    # group magnetization
    mag_groups = collections.defaultdict(list)
    for row in mag:
        try:
            d = float(row['D_over_J'])
            a = float(row['alpha'])
            t = float(row['temperature'])
            m = float(row['magnetization'])
            mag_groups[(d, a)].append((t, m))
        except (ValueError, KeyError):
            pass
    scores = []
    for (d, a), rows in mag_groups.items():
        if (d, a) not in pb:
            scores.append(0.0)
            continue
        info = pb[(d, a)]
        Tc = info['Tc']
        rows_sorted = sorted(rows, key=lambda x: x[0])
        temps = [r[0] for r in rows_sorted]
        mags = [r[1] for r in rows_sorted]
        # monotonic decrease
        ok = all(mags[i] >= mags[i+1] - 1e-6 for i in range(len(mags)-1)) if len(mags) > 1 else True
        if not ok:
            scores.append(0.0)
            continue
        # find implied Tc (first temp where mag <= 1e-6)
        implied_Tc = None
        for t, m in rows_sorted:
            if m <= 1e-6:
                implied_Tc = t
                break
        if implied_Tc is None:
            implied_Tc = temps[-1] + 0.1  # failed
        diff = abs(implied_Tc - Tc)
        if diff <= tol_Tc:
            scores.append(1.0)
        else:
            scores.append(max(0.0, 1.0 - (diff - tol_Tc) / 0.5))
    return sum(scores)/len(scores) if scores else 0.0


_SCORERS = {
    'phase_boundary_check': score_0,
    'magnetization_check': score_1,
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
