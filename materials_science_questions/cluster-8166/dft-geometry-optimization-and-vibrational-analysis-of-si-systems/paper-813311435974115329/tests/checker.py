import os
import json
import csv


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
    import csv, os

    def compute_integrals(path):
        try:
            with open(path, newline='') as f:
                reader = csv.DictReader(f)
                rows = list(reader)
        except Exception:
            return None
        if not rows:
            return None
        try:
            rows.sort(key=lambda r: float(r['Energy_eV']))
            energies = [float(r['Energy_eV']) for r in rows]
        except Exception:
            return None
        if len(energies) < 2:
            return None
        step = energies[1] - energies[0]
        uniform = True
        for i in range(1, len(energies)):
            if abs((energies[i] - energies[i-1]) - step) > 1e-6 * abs(step):
                uniform = False
                break
        ad_types = ['CoF','CeF','CoU','CeU']
        windows = {
            'p-type': (-0.6, -0.1),
            'intrinsic': (-0.5, 0.0),
            'n-type': (-0.4, 0.1)
        }
        integrals = {ad: {wn: 0.0 for wn in windows} for ad in ad_types}
        if uniform:
            for i, e in enumerate(energies):
                for wname, (w_start, w_end) in windows.items():
                    if e >= w_start and e < w_end:
                        for ad in ad_types:
                            try:
                                integrals[ad][wname] += float(rows[i][f'PDOS_{ad}']) * step
                            except:
                                pass
        else:
            data = []
            for r in rows:
                try:
                    e = float(r['Energy_eV'])
                    vals = {ad: float(r[f'PDOS_{ad}']) for ad in ad_types}
                    data.append((e, vals))
                except:
                    pass
            data.sort(key=lambda x: x[0])
            for wname, (w_start, w_end) in windows.items():
                for i in range(len(data)-1):
                    e1 = data[i][0]
                    e2 = data[i+1][0]
                    if e2 < w_start - 1e-9:
                        continue
                    if e1 > w_end + 1e-9:
                        break
                    left = max(e1, w_start)
                    right = min(e2, w_end)
                    if left >= right:
                        continue
                    width = right - left
                    if e2 - e1 < 1e-12:
                        f_left = data[i][1]
                        f_right = data[i][1]
                    else:
                        t_left = (left - e1) / (e2 - e1)
                        t_right = (right - e1) / (e2 - e1)
                        f_left = {}
                        f_right = {}
                        for ad in ad_types:
                            val1 = data[i][1][ad]
                            val2 = data[i+1][1][ad]
                            f_left[ad] = val1 + (val2 - val1) * t_left
                            f_right[ad] = val1 + (val2 - val1) * t_right
                    for ad in ad_types:
                        integrals[ad][wname] += (f_left[ad] + f_right[ad]) / 2 * width
        return integrals

    ctx = {}
    pdos_path = '/app/outputs/raw_pdos.csv'
    if os.path.exists(pdos_path):
        intgl = compute_integrals(pdos_path)
        if intgl is not None:
            ctx['integrals'] = intgl
        else:
            ctx['integrals'] = {}
    else:
        ctx['integrals'] = {}
    return ctx


# === block: score_0 (check id='recompute_ordering') ===
def score_0(artifact, step, ctx):
    if not artifact:
        return 0.0
    integrals = ctx.get('integrals', {})
    if not integrals:
        return 0.0
    orderings = {
        'p-type': ['CoF','CoU','CeF','CeU'],
        'intrinsic': ['CoF','CoU','CeF','CeU'],
        'n-type': ['CoF','CeF','CoU','CeU']
    }
    plaus_ok = True
    ad_list = ['CoF','CeF','CoU','CeU']
    for ad in ad_list:
        ad_ints = integrals.get(ad, {})
        for w in ['p-type','intrinsic','n-type']:
            v = ad_ints.get(w, 0)
            if v < 0.5 or v > 50:
                plaus_ok = False
    correct = 0
    for w, order in orderings.items():
        vals = []
        missing = False
        for ad in order:
            v = integrals.get(ad, {}).get(w)
            if v is None:
                missing = True
                break
            vals.append(v)
        if missing:
            continue
        if all(vals[i] > vals[i+1] for i in range(len(vals)-1)):
            correct += 1
    score = correct / 3.0
    if not plaus_ok:
        score *= 0.5
    return score


# === block: score_1 (check id='consistency') ===
def score_1(artifact, step, ctx):
    if not artifact:
        return 0.0
    integrals = ctx.get('integrals', {})
    if not integrals:
        return 0.0
    agent_vals = {}
    try:
        for row in artifact:
            ad = row.get('adatom', '').strip()
            w = row.get('window', '').strip()
            val = float(row.get('integrated_pdos', 0))
            agent_vals[(ad,w)] = val
    except:
        return 0.0
    recomp = {}
    ad_list = ['CoF','CeF','CoU','CeU']
    for ad in ad_list:
        for w in ['p-type','intrinsic','n-type']:
            v = integrals.get(ad, {}).get(w)
            if v is None:
                return 0.0
            recomp[(ad,w)] = v
    if len(recomp) != 12:
        return 0.0
    for k, ref in recomp.items():
        rep = agent_vals.get(k)
        if rep is None:
            return 0.0
        if rep == 0 and ref == 0:
            continue
        tol = 0.1 * max(abs(ref), 1e-9)
        if abs(rep - ref) > tol:
            return 0.0
    return 1.0


_SCORERS = {
    'recompute_ordering': score_0,
    'consistency': score_1,
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
