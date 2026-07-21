import os
import json
import csv

# === author imports / helpers ===
import json, math


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


# === block: score_0 (check id='strain_analysis_full') ===
def score_0(artifact, step, ctx):
        sub_weights = step.get('sub_weights', {})
        w_delta = sub_weights.get('delta_values', 0.5)
        w_ortho = sub_weights.get('ortho_distances', 0.2)
        w_trend_om = sub_weights.get('trend_ortho_vs_mono', 0.2)
        w_trend_ct = sub_weights.get('trend_cubic_tet_min', 0.1)
        tol_a = step.get('tolerance_a', 0.02)
        tol_alpha = step.get('tolerance_alpha', 0.1)
        gold_da = step.get('gold_delta_a', {})
        gold_dalpha = step.get('gold_delta_alpha', {})
        gold_ortho_a_m211 = step.get('gold_ortho_a_minus211', 6.019)
        gold_ortho_a_121 = step.get('gold_ortho_a_1_21', 6.117)
        sub_scores = {}

        # Score delta averages directly from agent-reported values (no per-triangle recompute)
        delta_pass = 0
        total_pairs = 0
        for poly in ['cubic', 'tetragonal', 'monoclinic', 'orthorhombic']:
            entry = artifact.get(poly)
            if not isinstance(entry, dict):
                continue
            try:
                da_avg = float(entry['Delta_a_avg'])
                dalpha_avg = float(entry['Delta_alpha_avg'])
            except (KeyError, TypeError, ValueError):
                continue
            exp_da = gold_da.get(poly)
            exp_dalpha = gold_dalpha.get(poly)
            if exp_da is not None:
                total_pairs += 1
                if abs(da_avg - exp_da) <= tol_a:
                    delta_pass += 1
            if exp_dalpha is not None:
                total_pairs += 1
                if abs(dalpha_avg - exp_dalpha) <= tol_alpha:
                    delta_pass += 1
        sub_scores['delta_values'] = (delta_pass / total_pairs) if total_pairs > 0 else 0.0

        # Ortho distances
        ortho_ok = 0
        ortho_total = 0
        if 'orthorhombic' in artifact and isinstance(artifact['orthorhombic'], dict):
            ortho = artifact['orthorhombic']
            try:
                am211 = float(ortho.get('a_minus211', float('nan')))
                a121 = float(ortho.get('a_1-21', float('nan')))
            except (TypeError, ValueError):
                am211 = a121 = None
            if am211 is not None and abs(am211 - gold_ortho_a_m211) <= tol_a:
                ortho_ok += 1
            if a121 is not None and abs(a121 - gold_ortho_a_121) <= tol_a:
                ortho_ok += 1
            ortho_total = 2
        sub_scores['ortho_distances'] = (ortho_ok / ortho_total) if ortho_total > 0 else 0.0

        # Trend ortho vs mono (using reported averages)
        trend_ok = 0.0
        try:
            o_da = float(artifact['orthorhombic']['Delta_a_avg'])
            o_dalpha = float(artifact['orthorhombic']['Delta_alpha_avg'])
            m_da = float(artifact['monoclinic']['Delta_a_avg'])
            m_dalpha = float(artifact['monoclinic']['Delta_alpha_avg'])
            if o_da < m_da - 1e-9:
                trend_ok += 0.5
            if o_dalpha < m_dalpha - 1e-9:
                trend_ok += 0.5
        except (KeyError, TypeError, ValueError):
            pass
        sub_scores['trend_ortho_vs_mono'] = trend_ok

        # Trend cubic/tet min
        trend_ct = 0.0
        try:
            da_vals = {}
            dalpha_vals = {}
            for poly in ['cubic', 'tetragonal', 'monoclinic', 'orthorhombic']:
                entry = artifact[poly]
                da_vals[poly] = float(entry['Delta_a_avg'])
                dalpha_vals[poly] = float(entry['Delta_alpha_avg'])
            min_da = min(da_vals.values())
            if (min_da == da_vals['cubic'] or min_da == da_vals['tetragonal']) and min_da <= da_vals['monoclinic'] and min_da <= da_vals['orthorhombic']:
                trend_ct += 0.5
            min_dalpha = min(dalpha_vals.values())
            if (min_dalpha == dalpha_vals['cubic'] or min_dalpha == dalpha_vals['tetragonal']) and min_dalpha <= dalpha_vals['monoclinic'] and min_dalpha <= dalpha_vals['orthorhombic']:
                trend_ct += 0.5
        except (KeyError, TypeError, ValueError):
            pass
        sub_scores['trend_cubic_tet_min'] = trend_ct

        total_score = (
            sub_scores.get('delta_values', 0) * w_delta +
            sub_scores.get('ortho_distances', 0) * w_ortho +
            sub_scores.get('trend_ortho_vs_mono', 0) * w_trend_om +
            sub_scores.get('trend_cubic_tet_min', 0) * w_trend_ct
        )
        return total_score


_SCORERS = {
    'strain_analysis_full': score_0,
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
