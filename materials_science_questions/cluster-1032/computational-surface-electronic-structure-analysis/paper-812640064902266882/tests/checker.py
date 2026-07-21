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
    def prepare(outputs_dir, spec):
        gold = spec['gold']
        return {
            'gold_eigen': gold['eigenvalues'],
            'gold_split': gold['splittings'],
            'tol_e': spec['tol_eigen'],
            'tol_s': spec['tol_splitting'],
            'tol_c': spec.get('tol_consistency', 0.001)
        }


# === block: score_0 (check id='step_04_band_calc') ===
def score_0(artifact, step, ctx):
        try:
            gold_eigen = ctx['gold_eigen']
            gold_split = ctx['gold_split']
            tol_e = ctx['tol_e']
            tol_s = ctx['tol_s']
            tol_c = ctx.get('tol_consistency', 0.001)
            if not isinstance(artifact, dict):
                return 0.0
            # safe number getter – returns None if the value is missing or cannot be cast
            def _safe_float(d, key):
                try:
                    val = d[key]
                    if val is None:
                        return None
                    return float(val)
                except (KeyError, TypeError, ValueError):
                    return None
            total = 0.0
            # eigenvalue checks
            eig_keys = ['Gamma1_s','Gamma3_dxy','Gamma4_dx2y2','Gamma5_dxz_dyz','M3_dxy','M4_dx2y2','M5_dxz_dyz']
            eig_weight_each = 0.7 / 7
            gamma_obj = artifact.get('Gamma')
            m_obj = artifact.get('M')
            if isinstance(gamma_obj, dict) and isinstance(m_obj, dict):
                for k in eig_keys:
                    if k.startswith('Gamma'):
                        val = _safe_float(gamma_obj, k)
                    else:
                        val = _safe_float(m_obj, k)
                    if val is not None and abs(val - gold_eigen[k]) <= tol_e:
                        total += eig_weight_each
            # splitting checks vs gold
            split_keys = ['Delta_Gamma25_prime', 'Delta_Gamma12']
            split_weight_each = 0.2 / 2
            splittings_obj = artifact.get('splittings')
            if isinstance(splittings_obj, dict):
                for k in split_keys:
                    val = _safe_float(splittings_obj, k)
                    if val is not None and abs(val - gold_split[k]) <= tol_s:
                        total += split_weight_each
            # self‑consistency: computed splittings from eigenvalues vs reported splittings
            cons_weight_each = 0.1 / 2
            g3 = _safe_float(gamma_obj, 'Gamma3_dxy') if isinstance(gamma_obj, dict) else None
            g5 = _safe_float(gamma_obj, 'Gamma5_dxz_dyz') if isinstance(gamma_obj, dict) else None
            r25 = _safe_float(splittings_obj, 'Delta_Gamma25_prime') if isinstance(splittings_obj, dict) else None
            if g3 is not None and g5 is not None and r25 is not None:
                if abs((g5 - g3) - r25) <= tol_c:
                    total += cons_weight_each
            g1 = _safe_float(gamma_obj, 'Gamma1_s') if isinstance(gamma_obj, dict) else None
            g4 = _safe_float(gamma_obj, 'Gamma4_dx2y2') if isinstance(gamma_obj, dict) else None
            r12 = _safe_float(splittings_obj, 'Delta_Gamma12') if isinstance(splittings_obj, dict) else None
            if g1 is not None and g4 is not None and r12 is not None:
                if abs((g4 - g1) - r12) <= tol_c:
                    total += cons_weight_each
            # ordering checks
            ordering_weight = 0.1
            if g3 is not None and g5 is not None and g4 is not None:
                if g3 < g5 < g4:
                    total += ordering_weight * 0.5
            m3 = _safe_float(m_obj, 'M3_dxy') if isinstance(m_obj, dict) else None
            m5 = _safe_float(m_obj, 'M5_dxz_dyz') if isinstance(m_obj, dict) else None
            m4 = _safe_float(m_obj, 'M4_dx2y2') if isinstance(m_obj, dict) else None
            if m3 is not None and m5 is not None and m4 is not None:
                if m3 < m5 < m4:
                    total += ordering_weight * 0.5
            return min(max(total, 0.0), 1.0)
        except Exception:
            return 0.0


_SCORERS = {
    'step_04_band_calc': score_0,
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
