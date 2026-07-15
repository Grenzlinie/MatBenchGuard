import os
import json
import csv

# === author imports / helpers ===
import csv, json, os, math


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
    gold_fe_table = spec['steps'][0]['gold_fe_table']
    return {'gold_fe_table': gold_fe_table, 'spec': spec}


# === block: score_0 (check id='fe_results') ===
def score_0(artifact, step, ctx):
    if not artifact:
        return 0.0
    gold = ctx['gold_fe_table']
    tol_rel = step.get('tolerance_relative_moduli', 0.15)
    tol_abs_p = step.get('tolerance_abs_poisson', 0.02)
    decay = step.get('decay_factor', 3.0)
    scored = 0
    N = 0
    for row in artifact:
        if not isinstance(row, dict):
            continue
        cfg = str(row.get('RVE_config', '')).strip()
        if cfg not in gold:
            continue
        g = gold[cfg]
        for prop in ['E_L', 'E_T', 'G_T']:
            v_str = row.get(prop, None)
            if v_str is None or (isinstance(v_str, str) and v_str.strip() == ''):
                sc = 0.0
            else:
                try:
                    v = float(v_str)
                except (ValueError, TypeError):
                    sc = 0.0
                else:
                    try:
                        gv = float(g[prop])
                    except (ValueError, TypeError):
                        sc = 0.0
                    else:
                        if gv != 0:
                            err = abs(v - gv) / abs(gv)
                        else:
                            err = 0.0 if abs(v) < 1e-12 else 1e9
                        if err <= tol_rel:
                            sc = 1.0
                        else:
                            sc = max(0.0, 1.0 - (err - tol_rel) / (tol_rel * decay))
            scored += sc
            N += 1
        for prop in ['v_L', 'v_T']:
            v_str = row.get(prop, None)
            if v_str is None or (isinstance(v_str, str) and v_str.strip() == ''):
                sc = 0.0
            else:
                try:
                    v = float(v_str)
                except (ValueError, TypeError):
                    sc = 0.0
                else:
                    try:
                        gv = float(g[prop])
                    except (ValueError, TypeError):
                        sc = 0.0
                    else:
                        err = abs(v - gv)
                        if err <= tol_abs_p:
                            sc = 1.0
                        else:
                            sc = max(0.0, 1.0 - (err - tol_abs_p) / (tol_abs_p * decay))
            scored += sc
            N += 1
    return scored / N if N else 0.0


# === block: score_1 (check id='halpin_tsai_results') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        groups = step['config_groups']
        expected = set()
        for glist in groups.values():
            expected.update(glist)
        seen = set(row.get('RVE_config','').strip() for row in artifact)
        if not expected.issubset(seen):
            return 0.0
        invalid = 0
        for row in artifact:
            for prop in ['E_L','E_T','G_T']:
                try:
                    if float(row[prop]) <= 0:
                        invalid += 1
                except:
                    invalid += 1
            for prop in ['v_L','v_T']:
                try:
                    v = float(row[prop])
                    if not (0 <= v <= 0.5):
                        invalid += 1
                except:
                    invalid += 1
        score_range = max(0.0, 1.0 - invalid / max(1, len(artifact)*6))
        def monotonic(configs, prop, inc):
            vals = []
            for cn in configs:
                for row in artifact:
                    if row.get('RVE_config','').strip() == cn:
                        try:
                            vals.append(float(row[prop]))
                        except:
                            vals.append(None)
                        break
            if None in vals or len(vals) != len(configs):
                return 0.0
            s = 0
            for i in range(len(vals)-1):
                if inc and vals[i+1] >= vals[i]:
                    s += 1
                elif not inc and vals[i+1] <= vals[i]:
                    s += 1
            return s / max(1, len(vals)-1)
        cc = groups['varying_clay']
        cc2 = groups['varying_cnt']
        mono = (monotonic(cc, 'E_L', True) + monotonic(cc, 'E_T', True) + monotonic(cc, 'G_T', True) +
                monotonic(cc, 'v_L', False) + monotonic(cc, 'v_T', True) +
                monotonic(cc2, 'E_L', True) + monotonic(cc2, 'E_T', True) + monotonic(cc2, 'G_T', True) +
                monotonic(cc2, 'v_L', False) + monotonic(cc2, 'v_T', True)) / 10.0
        return 0.3 * score_range + 0.7 * mono


_SCORERS = {
    'fe_results': score_0,
    'halpin_tsai_results': score_1,
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
