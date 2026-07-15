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


# === block: score_0 (check id='mixed_doses') ===
def score_0(artifact, step, ctx):
        gold_rows = step.get('gold', [])
        gold = {}
        for r in gold_rows:
            key = (r['geometry'], float(r['energy_keV_raw']))
            gold[key] = float(r['D_mixed'])
        rows = artifact
        if not rows:
            return 0.0
        total = 0.0
        count = 0
        for row in rows:
            geom = row.get('geometry', '').strip()
            try:
                energy = float(row.get('energy_keV', 'NaN'))
            except:
                continue
            key = (geom, energy)
            if key not in gold:
                continue
            target = gold[key]
            try:
                val = float(row.get('D_mixed', 'NaN'))
            except:
                val = None
            if val is None:
                score_row = 0.0
            elif target == 0:
                score_row = 1.0 if abs(val) < 1e-12 else 0.0
            else:
                rel_err = abs(val - target) / abs(target)
                tol = 0.02
                score_row = 1.0 if rel_err <= tol else 0.0
            total += score_row
            count += 1
        return total / count if count else 0.0


# === block: score_1 (check id='penelope_doses') ===
def score_1(artifact, step, ctx):
        gold_rows = step.get('gold', [])
        gold = {}
        for r in gold_rows:
            key = (r['geometry'], float(r['energy_keV_raw']))
            gold[key] = r
        rows = artifact
        if not rows:
            return 0.0
        tol = 0.10  # flat relative tolerance to absorb systematic differences
        scores_noelastic = []
        scores_withelastic = []
        for row in rows:
            geom = row.get('geometry', '').strip()
            try:
                energy = float(row.get('energy_keV', 'NaN'))
            except:
                continue
            key = (geom, energy)
            if key not in gold:
                continue
            gr = gold[key]
            # without elastic
            D_woe_gold = float(gr['D_without_elastic'])
            try:
                D_woe_agent = float(row.get('D_without_elastic', 'NaN'))
            except:
                D_woe_agent = None
            if D_woe_agent is not None and D_woe_gold != 0:
                rel_err = abs(D_woe_agent - D_woe_gold) / abs(D_woe_gold)
                score_no = 1.0 if rel_err <= tol else 0.0
            else:
                score_no = 0.0
            scores_noelastic.append(score_no)
            # with elastic
            D_we_gold = float(gr['D_with_elastic'])
            try:
                D_we_agent = float(row.get('D_with_elastic', 'NaN'))
            except:
                D_we_agent = None
            if D_we_agent is not None and D_we_gold != 0:
                rel_err = abs(D_we_agent - D_we_gold) / abs(D_we_gold)
                score_we = 1.0 if rel_err <= tol else 0.0
            else:
                score_we = 0.0
            scores_withelastic.append(score_we)
        avg_no = sum(scores_noelastic) / len(scores_noelastic) if scores_noelastic else 0.0
        avg_we = sum(scores_withelastic) / len(scores_withelastic) if scores_withelastic else 0.0
        # Trend check: for N<-N at 5 and 10 keV, D_we > D_woe
        trend_ok = 1.0
        for energy in [5.0, 10.0]:
            key = ('N<-N', energy)
            if key not in gold:
                continue
            D_we_agent = None
            D_woe_agent = None
            for row in rows:
                geom = row.get('geometry', '').strip()
                try:
                    en = float(row.get('energy_keV', 'NaN'))
                except:
                    continue
                if geom == 'N<-N' and en == energy:
                    try:
                        D_we_agent = float(row.get('D_with_elastic', 'NaN'))
                    except:
                        pass
                    try:
                        D_woe_agent = float(row.get('D_without_elastic', 'NaN'))
                    except:
                        pass
                    break
            if D_woe_agent is None or D_we_agent is None:
                trend_ok = 0.0
            elif D_we_agent <= D_woe_agent:
                trend_ok = 0.0
        return 0.4 * avg_no + 0.4 * avg_we + 0.2 * trend_ok


# === block: score_2 (check id='lineal_energies') ===
def score_2(artifact, step, ctx):
        gold_rows = step.get('gold', [])
        gold = {}
        for r in gold_rows:
            key = (r['geometry'], float(r['energy_keV_raw']))
            gold[key] = r
        rows = artifact
        if not rows:
            return 0.0
        scores_yF = []
        scores_ymp = []
        for row in rows:
            geom = row.get('geometry', '').strip()
            try:
                energy = float(row.get('energy_keV', 'NaN'))
            except:
                continue
            key = (geom, energy)
            if key not in gold:
                continue
            gr = gold[key]
            # yF
            yF_gold = float(gr['yF'])
            try:
                yF_agent = float(row.get('yF', 'NaN'))
            except:
                yF_agent = None
            if yF_agent is not None and yF_gold != 0:
                rel_err = abs(yF_agent - yF_gold) / abs(yF_gold)
                tol = 0.10
                score_f = 1.0 if rel_err <= tol else 0.0
            elif yF_gold == 0:
                score_f = 1.0 if yF_agent is not None and abs(yF_agent) < 1e-12 else 0.0
            else:
                score_f = 0.0
            scores_yF.append(score_f)
            # ymp
            ymp_gold = float(gr['ymp'])
            try:
                ymp_agent = float(row.get('ymp', 'NaN'))
            except:
                ymp_agent = None
            if ymp_agent is not None and ymp_gold != 0:
                rel_err = abs(ymp_agent - ymp_gold) / abs(ymp_gold)
                tol = 0.10
                score_m = 1.0 if rel_err <= tol else 0.0
            elif ymp_gold == 0:
                score_m = 1.0 if ymp_agent is not None and abs(ymp_agent) < 1e-12 else 0.0
            else:
                score_m = 0.0
            scores_ymp.append(score_m)
        avg_f = sum(scores_yF) / len(scores_yF) if scores_yF else 0.0
        avg_m = sum(scores_ymp) / len(scores_ymp) if scores_ymp else 0.0
        return 0.5 * avg_f + 0.5 * avg_m


_SCORERS = {
    'mixed_doses': score_0,
    'penelope_doses': score_1,
    'lineal_energies': score_2,
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
