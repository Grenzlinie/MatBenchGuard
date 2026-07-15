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
    return {}


# === block: score_0 (check id='check_black') ===
def score_0(artifact, step, ctx):
    try:
        tol = step.get('spin_tol', 0.3)
        tms = ['Sc','Ti','V','Cr','Mn','Fe','Co','Ni']
        funcs = ['PBE','PBE_U']
        gtot = step['gold_total_spin']
        gloc = step['gold_local_spin']
        gcls = step['gold_class']
        gbe = step['gold_binding_energy']
        n_spin, hit_spin = 0, 0
        n_cls, hit_cls = 0, 0
        be_sum, be_cnt = {}, {}
        for tm in tms:
            td = artifact.get(tm, {})
            if not isinstance(td, dict): continue
            for f in funcs:
                e = td.get(f, {})
                if not isinstance(e, dict): continue
                n_spin += 1
                v = e.get('total_spin_moment')
                if v is not None:
                    try:
                        if abs(float(v) - gtot.get(tm, 0)) <= tol:
                            hit_spin += 1
                    except: pass
                n_spin += 1
                v2 = e.get('local_spin_moment')
                if v2 is not None:
                    try:
                        if abs(float(v2) - gloc.get(tm, 0)) <= tol:
                            hit_spin += 1
                    except: pass
                n_cls += 1
                c = e.get('classification', '')
                if isinstance(c, str) and c.strip() == gcls.get(tm, ''):
                    hit_cls += 1
                bev = e.get('binding_energy')
                if bev is not None:
                    try:
                        bf = float(bev)
                        be_sum[tm] = be_sum.get(tm, 0.0) + bf
                        be_cnt[tm] = be_cnt.get(tm, 0) + 1
                    except: pass
        spin_score = hit_spin / n_spin if n_spin > 0 else 0.0
        cls_score = hit_cls / n_cls if n_cls > 0 else 0.0
        bind_score = 0.0
        be_avg = {tm: be_sum[tm]/be_cnt[tm] for tm in be_sum if be_cnt.get(tm,0) > 0}
        if len(be_avg) >= 6:
            be_list = [be_avg[tm] for tm in tms if tm in be_avg]
            gbe_sub = [gbe[i] for i, tm in enumerate(tms) if tm in be_avg]
            nv = len(be_list)
            if nv >= 2:
                def rankify(arr):
                    idx = sorted(range(len(arr)), key=lambda i: arr[i])
                    r = [0]*len(arr)
                    i = 0
                    while i < len(arr):
                        j = i
                        while j < len(arr) and arr[idx[j]] == arr[idx[i]]: j += 1
                        avg = (i + j - 1) / 2.0 + 1
                        for k in range(i, j): r[idx[k]] = avg
                        i = j
                    return r
                ra = rankify(be_list)
                rg = rankify(gbe_sub)
                d2 = sum((ra[i]-rg[i])**2 for i in range(nv))
                sp = 1.0 - 6.0*d2/(nv*(nv*nv-1))
                bind_score = max(0.0, min(1.0, (sp + 0.5) / 1.2))
        return 0.6*spin_score + 0.3*cls_score + 0.1*bind_score
    except:
        return 0.0


# === block: score_1 (check id='check_blue') ===
def score_1(artifact, step, ctx):
    try:
        tol = step.get('spin_tol', 0.3)
        tms = ['Sc','Ti','V','Cr','Mn','Fe','Co','Ni']
        funcs = ['PBE','PBE_U']
        gtot = step['gold_total_spin']
        gloc = step['gold_local_spin']
        gcls_pbe = step['gold_class_pbe']
        gcls_pbeu = step['gold_class_pbe_u']
        gbe = step['gold_binding_energy']
        n_spin, hit_spin = 0, 0
        n_cls, hit_cls = 0, 0
        be_sum, be_cnt = {}, {}
        for tm in tms:
            td = artifact.get(tm, {})
            if not isinstance(td, dict): continue
            for f in funcs:
                e = td.get(f, {})
                if not isinstance(e, dict): continue
                n_spin += 1
                v = e.get('total_spin_moment')
                if v is not None:
                    try:
                        if abs(float(v) - gtot.get(tm, 0)) <= tol:
                            hit_spin += 1
                    except: pass
                n_spin += 1
                v2 = e.get('local_spin_moment')
                if v2 is not None:
                    try:
                        if abs(float(v2) - gloc.get(tm, 0)) <= tol:
                            hit_spin += 1
                    except: pass
                n_cls += 1
                c = e.get('classification', '')
                if isinstance(c, str):
                    c = c.strip()
                    if f == 'PBE':
                        expected = gcls_pbe.get(tm, '')
                        if c == expected:
                            hit_cls += 1
                        elif tm == 'Ti' and expected == 'half-metal' and c == 'DMS':
                            hit_cls += 1
                    else:
                        if c == gcls_pbeu.get(tm, ''):
                            hit_cls += 1
                bev = e.get('binding_energy')
                if bev is not None:
                    try:
                        bf = float(bev)
                        be_sum[tm] = be_sum.get(tm, 0.0) + bf
                        be_cnt[tm] = be_cnt.get(tm, 0) + 1
                    except: pass
        spin_score = hit_spin / n_spin if n_spin > 0 else 0.0
        cls_score = hit_cls / n_cls if n_cls > 0 else 0.0
        bind_score = 0.0
        be_avg = {tm: be_sum[tm]/be_cnt[tm] for tm in be_sum if be_cnt.get(tm,0) > 0}
        if len(be_avg) >= 6:
            be_list = [be_avg[tm] for tm in tms if tm in be_avg]
            gbe_sub = [gbe[i] for i, tm in enumerate(tms) if tm in be_avg]
            nv = len(be_list)
            if nv >= 2:
                def rankify(arr):
                    idx = sorted(range(len(arr)), key=lambda i: arr[i])
                    r = [0]*len(arr)
                    i = 0
                    while i < len(arr):
                        j = i
                        while j < len(arr) and arr[idx[j]] == arr[idx[i]]: j += 1
                        avg = (i + j - 1) / 2.0 + 1
                        for k in range(i, j): r[idx[k]] = avg
                        i = j
                    return r
                ra = rankify(be_list)
                rg = rankify(gbe_sub)
                d2 = sum((ra[i]-rg[i])**2 for i in range(nv))
                sp = 1.0 - 6.0*d2/(nv*(nv*nv-1))
                bind_score = max(0.0, min(1.0, (sp + 0.5) / 1.2))
        return 0.6*spin_score + 0.3*cls_score + 0.1*bind_score
    except:
        return 0.0


_SCORERS = {
    'check_black': score_0,
    'check_blue': score_1,
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
