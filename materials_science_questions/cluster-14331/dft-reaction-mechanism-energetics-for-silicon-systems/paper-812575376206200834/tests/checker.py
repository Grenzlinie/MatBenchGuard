import os
import json
import csv

# === author imports / helpers ===
import csv
import math
from collections import defaultdict


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


# === block: score_0 (check id='barriers_and_rate_constants') ===
def score_0(artifact, step, ctx):
        if not isinstance(artifact, list) or len(artifact) != 20:
            return 0.0

        # Hard-coded gold values; hidden from the agent’s instruction materials.
        gold_barriers = {
            "P1": 84.38,
            "P2": 37.92,
            "P3": 100.69,
            "P4": 45.41
        }
        gold_rates = {
            "P1": {
                "298.15": 8.3e-50,
                "1000": 4.43e-06,
                "1500": 15.7,
                "2000": 24900.0,
                "2500": 2180000.0
            },
            "P2": {
                "298.15": 9.7e-16,
                "1000": 107000.0,
                "1500": 92900000.0,
                "2000": 2980000000.0,
                "2500": 25200000000.0
            },
            "P3": {
                "298.15": 9.1e-62,
                "1000": 2.02e-09,
                "1500": 0.0659,
                "2000": 410.0,
                "2500": 81500.0
            },
            "P4": {
                "298.15": 3.12e-21,
                "1000": 2460.0,
                "1500": 7520000.0,
                "2000": 453000000.0,
                "2500": 5570000000.0
            }
        }

        barrier_tol = step.get('barrier_tolerance_kcalmol', 2.0)
        log_rate_tol = step.get('log_rate_tolerance', 0.5)
    
        barriers = {}
        rates = defaultdict(dict)
        for row in artifact:
            p = str(row.get('pathway', '')).strip()
            if not p:
                return 0.0
            try:
                T = float(row.get('temperature_K', ''))
            except (ValueError, TypeError):
                return 0.0
            if abs(T - 298.15) < 1e-4:
                dg_str = str(row.get('delta_G_forward_kcalmol', '')).strip()
                if dg_str:
                    try:
                        barriers[p] = float(dg_str)
                    except (ValueError, TypeError):
                        barriers[p] = None
            rk_str = str(row.get('rate_constant_s-1', '')).strip()
            if rk_str:
                try:
                    rates[p][int(T) if T.is_integer() else T] = float(rk_str)
                except (ValueError, TypeError):
                    rates[p][T] = None
    
        # Barrier sub-score
        barrier_scores = []
        for p in ('P1', 'P2', 'P3', 'P4'):
            gold = gold_barriers.get(p)
            agent_val = barriers.get(p)
            if agent_val is None or gold is None:
                barrier_scores.append(0.0)
                continue
            diff = abs(agent_val - gold)
            if diff <= barrier_tol:
                barrier_scores.append(1.0)
            elif diff <= 2 * barrier_tol:
                barrier_scores.append(max(0.0, 1.0 - (diff - barrier_tol) / barrier_tol))
            else:
                barrier_scores.append(0.0)
        barrier_score = sum(barrier_scores) / len(barrier_scores) if barrier_scores else 0.0
    
        # Rate constant sub-score
        temp_order = [298.15, 1000, 1500, 2000, 2500]
        rate_check_pass = 0
        rate_check_total = 0
        for p in ('P1', 'P2', 'P3', 'P4'):
            gold_T = gold_rates.get(p, {})
            for T in temp_order:
                agent_k = rates[p].get(T)
                gold_k = gold_T.get(str(T), gold_T.get(T))
                if agent_k is None or gold_k is None or agent_k <= 0 or gold_k <= 0:
                    continue
                log_agent = math.log10(agent_k)
                log_gold = math.log10(gold_k)
                if abs(log_agent - log_gold) <= log_rate_tol:
                    rate_check_pass += 1
                rate_check_total += 1
        rate_score = rate_check_pass / rate_check_total if rate_check_total else 0.0
    
        # Ordering sub-score
        order_ok = True
        # barrier order P2 < P4 < P1 < P3
        try:
            b2 = barriers.get('P2')
            b4 = barriers.get('P4')
            b1 = barriers.get('P1')
            b3 = barriers.get('P3')
            if None in (b2, b4, b1, b3):
                order_ok = False
            elif not (b2 < b4 < b1 < b3):
                order_ok = False
        except Exception:
            order_ok = False
        # rate order at each temperature: P2 > P4 > P1 > P3
        for T in temp_order:
            try:
                k2 = rates['P2'].get(T)
                k4 = rates['P4'].get(T)
                k1 = rates['P1'].get(T)
                k3 = rates['P3'].get(T)
                if None in (k2, k4, k1, k3):
                    order_ok = False
                    break
                if not (k2 > k4 > k1 > k3):
                    order_ok = False
                    break
            except (KeyError, TypeError):
                order_ok = False
                break
        order_score = 1.0 if order_ok else 0.0
    
        final = 0.3 * barrier_score + 0.5 * rate_score + 0.2 * order_score
        return min(1.0, max(0.0, final))


_SCORERS = {
    'barriers_and_rate_constants': score_0,
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