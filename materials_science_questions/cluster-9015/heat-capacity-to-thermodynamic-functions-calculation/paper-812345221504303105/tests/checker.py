import os
import json
import csv

# === author imports / helpers ===
import csv, json, math


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


# === block: score_0 (check id='02_condensed_functions') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold = step['gold_rows']
        tol = step['tolerances']
        agent_rows = artifact
        # Build lookup: key = (compound, phase, T_formatted)
        agent_map = {}
        for r in agent_rows:
            try:
                t = float(r['T'])
            except:
                continue
            key = (r.get('compound','').strip(), r.get('phase','').strip(), '{:.2f}'.format(round(t, 2)))
            agent_map[key] = r
        scores = []
        for gr in gold:
            gkey = (gr['compound'], gr['phase'], gr['T'])
            ar = agent_map.get(gkey)
            if ar is None:
                scores.append(0.0)
                continue
            row_sum = 0.0
            cols = ['neg_Gs_over_T','Hs_over_T','Hs','Ss','Cs']
            for c in cols:
                try:
                    gval = float(gr[c])
                    aval = float(ar[c])
                except:
                    row_sum += 0.0
                    continue
                err = abs(aval - gval)
                rel_tol = tol[c]['rel']
                abs_min = tol[c]['abs_min']
                allowed = max(rel_tol * abs(gval), abs_min)
                if err <= allowed:
                    row_sum += 1.0
            scores.append(row_sum / len(cols))
        if not scores:
            return 0.0
        return sum(scores) / len(scores)


# === block: score_1 (check id='03_ideal_gas_entropy') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold = step['gold_rows']
        agent_rows = artifact
        agent_dict = {}
        for r in agent_rows:
            agent_dict[r.get('compound','').strip()] = r
        scores = []
        for gr in gold:
            ar = agent_dict.get(gr['compound'].strip())
            if ar is None:
                scores.append(0.0)
                continue
            try:
                gval = float(gr['S_ideal_298.15'])
                aval = float(ar['S_ideal_298.15'])
            except:
                scores.append(0.0)
                continue
            err = abs(aval - gval)
            abs_tol = step['tolerances']['S_ideal_298.15']['abs']
            if err <= abs_tol:
                scores.append(1.0)
            else:
                scores.append(0.0)
        if not scores:
            return 0.0
        return sum(scores) / len(scores)


# === block: score_2 (check id='04_acrylonitrile_idealgas') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold = step['gold_rows']
        tol = step['tolerances']
        agent_rows = artifact
        agent_map = {}
        for r in agent_rows:
            try:
                t = float(r['T'])
            except:
                continue
            key = '{:.2f}'.format(round(t,2))
            agent_map[key] = r
        scores = []
        for gr in gold:
            ar = agent_map.get(gr['T'])
            if ar is None:
                scores.append(0.0)
                continue
            row_sum = 0.0
            cols = ['neg_G_over_T','H_over_T','S','Cp','ΔH_f°','ΔG_f°','log_K_f']
            for c in cols:
                try:
                    gval_str = gr[c]
                    aval_str = ar[c]
                    if gval_str == 'Inf' and aval_str == 'Inf':
                        row_sum += 1.0
                        continue
                    gval = float(gval_str)
                    aval = float(aval_str)
                except:
                    continue
                err = abs(aval - gval)
                if c in ('ΔH_f°','ΔG_f°','log_K_f'):
                    allowed = tol[c]['abs']
                else:
                    rel_tol = tol[c]['rel']
                    abs_min = tol[c]['abs_min']
                    allowed = max(rel_tol * abs(gval), abs_min)
                if err <= allowed:
                    row_sum += 1.0
            scores.append(row_sum / len(cols))
        if not scores:
            return 0.0
        return sum(scores) / len(scores)


_SCORERS = {
    '02_condensed_functions': score_0,
    '03_ideal_gas_entropy': score_1,
    '04_acrylonitrile_idealgas': score_2,
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
