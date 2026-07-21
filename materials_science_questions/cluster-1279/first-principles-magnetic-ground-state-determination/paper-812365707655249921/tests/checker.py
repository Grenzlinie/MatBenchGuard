import os
import json
import csv

# === author imports / helpers ===
import csv
import os
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
        gold = {}
        for ch in spec.get('checks', []):
            if ch.get('id') == 'magnetic_results':
                gold['expected'] = ch.get('expected', {})
                gold['tolerances'] = ch.get('tolerances', {})
                break
        return gold  # ctx


# === block: score_0 (check id='magnetic_results') ===
def score_0(artifact, step, ctx):
        if artifact is None:
            return 0.0
        if not isinstance(artifact, list) or len(artifact) != 4:
            return 0.0
        expected = ctx.get('expected', {})
        tolerances = ctx.get('tolerances', {})
        # required columns
        required_cols = {'configuration', 'energy_diff_mRy', 'Fe_moment_muB', 'Mn_moment_muB'}
        if not all(col in artifact[0] for col in required_cols):
            return 0.0
        # Convert to dict by configuration
        rows = {}
        for row in artifact:
            config = row.get('configuration', '').strip()
            rows[config] = row
        valid_configs = {'Fe↑Mn↑', 'Fe↑Mn↓', 'Fe↓Mn↑', 'Fe↓Mn↓'}
        if set(rows.keys()) != valid_configs:
            return 0.0
        # structural check scores
        score = 0.0
        # 1. File structure: columns exist and 4 rows with correct labels (0.10)
        score += 0.10
        # 2. Ground state: Fe↑Mn↑ must have energy_diff_mRy == 0 (exact float 0.0)
        gs_row = rows.get('Fe↑Mn↑')
        try:
            energy_gs = float(gs_row['energy_diff_mRy'])
        except (ValueError, TypeError, KeyError):
            energy_gs = None
        if energy_gs is not None and abs(energy_gs) < 1e-6:
            score += 0.15
        # 3. Energy ordering: 0 < Fe↑Mn↓ < Fe↓Mn↑ < Fe↓Mn↓
        order_ok = False
        try:
            e1 = float(rows['Fe↑Mn↓']['energy_diff_mRy'])
            e2 = float(rows['Fe↓Mn↑']['energy_diff_mRy'])
            e3 = float(rows['Fe↓Mn↓']['energy_diff_mRy'])
            if 0 < e1 < e2 < e3:
                order_ok = True
        except (ValueError, TypeError, KeyError):
            pass
        if order_ok:
            score += 0.15
        # 4. Energy values within tolerance (0.30)
        tol_energy = tolerances.get('energy_diff_mRy', 20.0)
        energy_ok = True
        energy_scores = 0.0
        for config, gold in expected.items():
            try:
                reported = float(rows[config]['energy_diff_mRy'])
            except (ValueError, KeyError, TypeError):
                energy_ok = False
                break
            delta = abs(reported - gold['energy'])
            if delta <= tol_energy:
                energy_scores += 1.0
            else:
                # partial based on error ratio, capped at 0
                frac = max(0.0, 1.0 - (delta - tol_energy) / (2 * tol_energy))
                energy_scores += frac
        energy_score_norm = energy_scores / 4.0  # four configs
        score += 0.30 * energy_score_norm
        # 5. Fe and Mn moments within tolerance (0.30)
        tol_moment = tolerances.get('moment_muB', 0.30)
        moment_ok = True
        moment_scores = 0.0
        total_moments = 0
        for config, gold in expected.items():
            for elem in ['Fe_moment', 'Mn_moment']:
                total_moments += 1
                try:
                    reported = float(rows[config][elem.replace('_moment','_moment_muB')])  # matching column name
                except (ValueError, KeyError, TypeError):
                    moment_ok = False
                    break
                gold_val = gold[elem]  # 'Fe_moment', 'Mn_moment'
                delta = abs(reported - gold_val)
                if delta <= tol_moment:
                    moment_scores += 1.0
                else:
                    frac = max(0.0, 1.0 - (delta - tol_moment) / (2 * tol_moment))
                    moment_scores += frac
            if not moment_ok:
                break
        moment_score_norm = moment_scores / total_moments if total_moments > 0 else 0.0
        score += 0.30 * moment_score_norm
        # Also check sign consistency: Fe↑Mn↑ -> Fe>0, Mn>0; Fe↑Mn↓ -> Fe>0, Mn<0; etc.
        # Already covered by tolerance checks, but add small bonus if signs match?
        # No extra, already included via closeness.
        return min(score, 1.0)


_SCORERS = {
    'magnetic_results': score_0,
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
