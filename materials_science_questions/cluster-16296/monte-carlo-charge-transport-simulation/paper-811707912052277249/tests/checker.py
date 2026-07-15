import os
import json
import csv

# === author imports / helpers ===
import csv, os, math


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
    def prepare(outputs_dir, spec):
        return {}


# === block: score_0 (check id='value_match') ===
def score_0(artifact, step, ctx):
    if not artifact:
        return 0.0
    gold = step.get('gold_data', [])
    tolerance = step.get('relative_tolerance', 0.25)
    total_checks = 0
    passed = 0
    rows_by_T = {}
    for r in artifact:
        if not isinstance(r, dict):
            continue
        t_val = r.get('T_lattice')
        if t_val is None:
            continue
        try:
            t = float(t_val)
        except (ValueError, TypeError):
            continue
        rows_by_T[t] = r
    for gold_row in gold:
        temp = gold_row.get('T_lattice')
        if temp is None:
            continue
        agent_row = rows_by_T.get(temp)
        if agent_row is None:
            continue
        for col in ['tau43_inv','tau42_inv','tau4','tau3','fraction_eLO_43']:
            try:
                val = float(agent_row.get(col))
            except (ValueError, TypeError):
                val = None
            try:
                gold_val = float(gold_row.get(col))
            except (ValueError, TypeError):
                gold_val = None
            if val is None or gold_val is None:
                total_checks += 1
                continue
            if abs(gold_val) < 1e-12:
                ok = abs(val - gold_val) <= 1e-9
            else:
                ok = abs(val - gold_val) / abs(gold_val) <= tolerance
            if ok:
                passed += 1
            total_checks += 1
    if total_checks == 0:
        return 0.0
    return passed / total_checks


# === block: score_1 (check id='trend_check') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        trends = step.get('trends', {})
        points = 0.0
        max_points = 0.0
        # map rows by integer temperature
        temps_dict = {}
        for r in artifact:
            try:
                t = int(float(r['T_lattice']))
                temps_dict[t] = r
            except (ValueError, KeyError):
                pass
        temps = sorted(temps_dict.keys())

        # tau43_inv monotonic increase
        if trends.get('tau43_inv_monotonic'):
            max_points += 1.0
            ok = True
            for i in range(len(temps)-1):
                try:
                    v1 = float(temps_dict[temps[i]]['tau43_inv'])
                    v2 = float(temps_dict[temps[i+1]]['tau43_inv'])
                    if v1 >= v2:
                        ok = False
                        break
                except (ValueError, KeyError):
                    ok = False
                    break
            if ok:
                points += 1.0

        # fraction_eLO_43 > 0.5 at all temps
        if trends.get('fraction_eLO_43_min'):
            max_points += 1.0
            ok = True
            for t in temps:
                try:
                    f = float(temps_dict[t]['fraction_eLO_43'])
                    if f <= 0.5:
                        ok = False
                        break
                except (ValueError, KeyError):
                    ok = False
                    break
            if ok:
                points += 1.0

        # at T=200, tau43_inv > tau42_inv
        if trends.get('tau43_gt_tau42_at_200K'):
            max_points += 1.0
            if 200 in temps_dict:
                try:
                    a = float(temps_dict[200]['tau43_inv'])
                    b = float(temps_dict[200]['tau42_inv'])
                    if a > b:
                        points += 1.0
                except (ValueError, KeyError):
                    pass
            # else: fail implicitly

        if max_points == 0.0:
            return 1.0
        return points / max_points


_SCORERS = {
    'value_match': score_0,
    'trend_check': score_1,
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
