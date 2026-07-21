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
    import math

    def prepare(outputs_dir, spec):
        renorm_step = [s for s in spec.get("steps", []) if s["output_file"] == "renormalization_factors.csv"]
        if renorm_step:
            expected = renorm_step[0].get("expected", [])
        else:
            expected = []
        m_kx = math.pi / 2
        m_ky = math.pi / (2 * math.sqrt(3))
        return {"expected_renorm": expected, "m_kx": m_kx, "m_ky": m_ky}


# === block: score_0 (check id='renorm_check') ===
def score_0(artifact, step, ctx):
    import math

    def _safe_float(v):
        if v is None:
            return None
        if isinstance(v, (int, float)):
            return float(v)
        try:
            return float(v)
        except (ValueError, TypeError):
            return None


    def _safe_int(v):
        try:
            return int(v)
        except (ValueError, TypeError):
            return None


    def score(artifact, step, ctx):
        try:
            expected = ctx.get("expected_renorm", [])
            if not expected or not isinstance(artifact, list):
                return 0.0

            rows_dict = {}
            for row in artifact:
                if not isinstance(row, dict):
                    continue
                try:
                    kl = str(row.get("k_label", "")).strip().lower()
                except Exception:
                    continue
                mode = _safe_int(row.get("mode"))
                r_val = _safe_float(row.get("r_value"))
                if kl and mode is not None and r_val is not None:
                    rows_dict[(kl, mode)] = r_val

            matches = 0
            total_expected = 0
            for exp in expected:
                if not isinstance(exp, dict):
                    continue
                kl = str(exp.get("k_label", "")).strip().lower()
                mode = _safe_int(exp.get("mode"))
                ref = _safe_float(exp.get("r_value"))
                tol_rel = _safe_float(exp.get("tolerance_rel", 0.05))
                if not kl or mode is None or ref is None or tol_rel is None:
                    continue
                total_expected += 1
                key = (kl, mode)
                val = rows_dict.get(key)
                if val is not None:
                    if ref == 0:
                        if abs(val) <= 1e-9:
                            matches += 1
                    else:
                        if abs(val - ref) <= tol_rel * abs(ref):
                            matches += 1

            return matches / total_expected if total_expected else 0.0
        except Exception:
            return 0.0


# === block: score_1 (check id='disp_check') ===
def score_1(artifact, step, ctx):
    import math

    def score(artifact, step, ctx):
        if not isinstance(artifact, list) or not artifact:
            return 0.0
        m_kx = ctx["m_kx"]
        m_ky = ctx["m_ky"]
        modes = {}
        for row in artifact:
            try:
                mode = int(row["mode"])
            except:
                continue
            try:
                kx = float(row["kx"])
                ky = float(row["ky"])
                energy = float(row["energy_meV"])
            except:
                continue
            dist = math.hypot(kx, ky)
            if mode not in modes:
                modes[mode] = []
            modes[mode].append((dist, energy))
        for m in modes:
            modes[m].sort(key=lambda x: x[0])
        if not all(m in modes for m in [0,1,2]):
            return 0.0
        e0 = [en for _, en in modes[0]]
        e1 = [en for _, en in modes[1]]
        e2 = [en for _, en in modes[2]]
        sub_scores = []
        # mode0 non-decreasing
        if len(e0) < 2:
            sub_scores.append(0.0)
        else:
            monotonic = all(e0[i+1] >= e0[i] - 0.05 for i in range(len(e0)-1))
            sub_scores.append(1.0 if monotonic else 0.0)
        # mode1 flat std < 0.15 meV
        if len(e1) < 2:
            sub_scores.append(0.0)
        else:
            mean1 = sum(e1)/len(e1)
            var1 = sum((x-mean1)**2 for x in e1)/len(e1)
            std1 = math.sqrt(var1)
            sub_scores.append(1.0 if std1 < 0.15 else 0.0)
        # mode2 peak not at ends
        if len(e2) < 3:
            sub_scores.append(0.0)
        else:
            max_idx = e2.index(max(e2))
            sub_scores.append(1.0 if (max_idx != 0 and max_idx != len(e2)-1) else 0.0)
        # mode2 min at M (last point)
        if len(e2) < 2:
            sub_scores.append(0.0)
        else:
            e2_M = e2[-1]
            e2_prev = e2[-2]
            sub_scores.append(1.0 if e2_M <= e2_prev - 0.05 else 0.0)
        # modes 1 and 2 degenerate at Gamma
        if len(e1) == 0 or len(e2) == 0:
            sub_scores.append(0.0)
        else:
            e1_Gamma = e1[0]
            e2_Gamma = e2[0]
            sub_scores.append(1.0 if abs(e1_Gamma - e2_Gamma) < 0.5 else 0.0)
        return sum(sub_scores) / len(sub_scores)


_SCORERS = {
    'renorm_check': score_0,
    'disp_check': score_1,
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
