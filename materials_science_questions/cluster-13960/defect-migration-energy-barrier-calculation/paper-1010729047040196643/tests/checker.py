import os
import json
import csv

# === author imports / helpers ===
import math

class _np:
    log = staticmethod(math.log)
    exp = staticmethod(math.exp)

    @staticmethod
    def mean(iterable):
        s = 0.0
        n = 0
        for val in iterable:
            s += val
            n += 1
        return s / n if n else 0.0

    @staticmethod
    def array(iterable):
        return list(iterable)

    @staticmethod
    def polyfit(x, y, deg):
        if deg != 1:
            raise NotImplementedError('only linear fit supported')
        n = len(x)
        if n != len(y) or n < 2:
            raise ValueError('need at least two points')
        sumx = sum(x)
        sumy = sum(y)
        sumx2 = sum(xi * xi for xi in x)
        sumxy = sum(xi * yi for xi, yi in zip(x, y))
        denom = n * sumx2 - sumx * sumx
        if abs(denom) < 1e-30:
            raise ZeroDivisionError('singular matrix')
        slope = (n * sumxy - sumx * sumy) / denom
        intercept = (sumy - slope * sumx) / n
        return [slope, intercept]

np = _np()


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


# === block: score_0 (check id='check_md_diffusivity') ===
def score_0(artifact, step, ctx):
    kB = 8.617333262e-5
    rows = artifact
    comp_groups = {}
    for row in rows:
        comp_groups.setdefault(row['composition'], []).append(row)
    compositions = ['HEO_A', 'Z8Y']
    scores_list = []
    for comp in compositions:
        if comp not in comp_groups or len(comp_groups[comp]) < 6:
            scores_list.append(0.0)
            continue
        gold = step['parameters']['gold_compositions'][comp]
        gold_Ea = gold['Ea_eV']
        gold_D0 = gold['D0_cm2s1']
        invT = []
        lnD = []
        for r in comp_groups[comp]:
            T = float(r['temperature_K'])
            D = float(r['D_cm2_s1'])
            if D <= 0:
                continue
            invT.append(1.0 / (kB * T))
            lnD.append(np.log(D))
        if len(invT) < 3:
            scores_list.append(0.0)
            continue
        invT = np.array(invT)
        lnD = np.array(lnD)
        slope, intercept = np.polyfit(invT, lnD, 1)
        Ea = -slope * kB
        D0 = np.exp(intercept)
        diff_Ea = abs(Ea - gold_Ea)
        tol_ea = step['parameters']['ea_tolerance']
        if diff_Ea <= tol_ea:
            score_Ea = 1.0
        else:
            score_Ea = max(0.0, 1.0 - (diff_Ea - tol_ea) / tol_ea)
        log10_D0_gold = np.log10(gold_D0)
        log10_D0_agent = np.log10(D0)
        diff_log10 = abs(log10_D0_agent - log10_D0_gold)
        tol_d0 = step['parameters']['d0_log10_tolerance']
        if diff_log10 <= tol_d0:
            score_D0 = 1.0
        else:
            score_D0 = max(0.0, 1.0 - (diff_log10 - tol_d0))
        comp_score = 0.5 * score_Ea + 0.5 * score_D0
        scores_list.append(comp_score)
    md_score = float(np.mean(scores_list)) if scores_list else 0.0
    return md_score


# === block: score_1 (check id='check_neb_barrier') ===
def score_1(artifact, step, ctx):
    rows = artifact
    groups = {}
    for row in rows:
        lbl = row['composition_label']
        groups.setdefault(lbl, []).append(row)
    labels = ['Y6.25%_CeHf0', 'Y6.25%_CeHf33', 'Y6.25%_CeHf66']
    gold_means = step['parameters']['gold_means']
    comp_scores = []
    Eb_means = {}
    Er_means = {}
    for lbl in labels:
        if lbl not in groups or len(groups[lbl]) < 5:
            comp_scores.append(0.0)
            Eb_means[lbl] = 0
            Er_means[lbl] = 0
            continue
        Eb_vals = [float(r['E_b_eV']) for r in groups[lbl]]
        Er_vals = [float(r['E_r_eV']) for r in groups[lbl]]
        eb_mean = np.mean(Eb_vals)
        er_mean = np.mean(Er_vals)
        Eb_means[lbl] = eb_mean
        Er_means[lbl] = er_mean
        gold_eb = gold_means[lbl]['Eb_mean']
        gold_er = gold_means[lbl]['Er_mean']
        tol = step['parameters'].get('eb_tolerance', 0.15)
        score_eb = max(0.0, 1.0 - abs(eb_mean - gold_eb) / tol)
        score_er = max(0.0, 1.0 - abs(er_mean - gold_er) / tol)
        comp_scores.append(0.5 * score_eb + 0.5 * score_er)
    avg_comp = float(np.mean(comp_scores)) if comp_scores else 0.0
    er_order_ok = (Er_means['Y6.25%_CeHf0'] < Er_means['Y6.25%_CeHf33'] < Er_means['Y6.25%_CeHf66']) if all(l in Er_means for l in labels) else False
    eb_spread = max(Eb_means.values()) - min(Eb_means.values()) if Eb_means else 100
    eb_const_ok = eb_spread <= 0.15
    trend_score = 0.5 * (1.0 if er_order_ok else 0.0) + 0.5 * (1.0 if eb_const_ok else 0.0)
    neb_score = 0.7 * avg_comp + 0.3 * trend_score
    return float(neb_score)


_SCORERS = {
    'check_md_diffusivity': score_0,
    'check_neb_barrier': score_1,
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
