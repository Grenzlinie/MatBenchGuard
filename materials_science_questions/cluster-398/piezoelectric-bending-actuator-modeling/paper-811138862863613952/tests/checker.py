import os
import json
import csv

# === author imports / helpers ===
import csv, math, json, os


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
    import csv, math, json, os

    def prepare(outputs_dir, spec):
        # PZT-4 standard constants (Berlincourt 1964, IEEE 176)
        c11E = 13.9e10
        c33E = 11.5e10
        e31 = -6.5
        e33 = 15.1
        eps33S = 5.87e-9
        k33 = 0.7
        gamma = 0.58
        keff_tall = 0.59
        pi = math.pi

        one_minus_8overpi2 = 1.0 - 8.0/(pi*pi)
        k33_sq_over_1mk33sq = (k33*k33) / (1.0 - k33*k33)
        factor_k_full = 1.0 + one_minus_8overpi2 * k33_sq_over_1mk33sq
        c33_prime = c33E * factor_k_full
        const_beta = math.sqrt( (13.4 * c11E) / (0.86 * (pi**3) * c33E * factor_k_full) )
        factor_46 = (8.0/(pi*pi)) * (e33*e33) / (c33_prime * eps33S)

        step_info = spec["steps"][0]
        ar_range = step_info["aspect_ratio_range"]
        start = ar_range["start"]
        stop = ar_range["stop"]
        step = ar_range["step"]

        gold = {}
        required_ratios = []
        h2a = start
        while h2a <= stop + 1e-9:
            h2a = round(h2a, 12)
            beta = 2.0 * h2a * const_beta
            A = 1.0
            B = -(1.0 + 1.0/(beta*beta))
            C = (1.0 - gamma*gamma) / (beta*beta)
            disc = B*B - 4.0*A*C
            if disc < 0:
                disc = 0.0
            sqrt_disc = math.sqrt(disc)
            Omega1 = (-B - sqrt_disc) / (2.0*A)
            Omega2 = (-B + sqrt_disc) / (2.0*A)
            def keff_sq_div(O):
                num = (1.0 - 1.1 * gamma * (e31/e33) - O) ** 2
                denom = gamma*gamma * (2.0*O - 1.0) + (1.0 - O)**2
                return factor_46 * (num / denom)
            ksq1 = keff_sq_div(Omega1)
            ksq2 = keff_sq_div(Omega2)
            keff1 = math.sqrt(ksq1 / (1.0 + ksq1))
            keff2 = math.sqrt(ksq2 / (1.0 + ksq2))
            keff1_norm = keff1 / keff_tall
            keff2_norm = keff2 / keff_tall
            gold[h2a] = (Omega1, Omega2, keff1_norm, keff2_norm)
            required_ratios.append(h2a)
            h2a += step

        ctx = {
            "gold": gold,
            "required_ratios": required_ratios,
            "tolerances": step_info["tolerances"]
        }
        return ctx


# === block: score_0 (check id='step_01_coupled_vibration_curves') ===
def score_0(artifact, step, ctx):
        gold = ctx["gold"]
        required = set(ctx["required_ratios"])
        tolerances = ctx["tolerances"]
        if not artifact:
            return 0.0
        expected_cols = {"aspect_ratio", "omega_1", "omega_2", "keff_1_norm", "keff_2_norm"}
        first = artifact[0] if artifact else {}
        if set(first.keys()) != expected_cols:
            return 0.0
        rows_dict = {}
        for row in artifact:
            try:
                ar = round(float(row["aspect_ratio"]), 12)
            except (ValueError, KeyError, TypeError):
                return 0.0
            rows_dict[ar] = row
        present = sum(1 for ar in required if ar in rows_dict)
        ratio_frac = present / len(required) if required else 0.0
        if present == 0:
            return 0.0
        total_score = 0.0
        total_fields = 0
        for ar in required:
            if ar not in rows_dict:
                continue
            row = rows_dict[ar]
            g_vals = gold[ar]
            for i, col in enumerate(["omega_1", "omega_2", "keff_1_norm", "keff_2_norm"]):
                val = row.get(col)
                if val is None or (isinstance(val, str) and val.strip() == ''):
                    continue
                try:
                    val = float(val)
                except (ValueError, TypeError):
                    continue
                g = g_vals[i]
                tol = tolerances[col]
                rtol = tol["rtol"]
                atol = tol["atol"]
                diff = abs(val - g)
                if math.isnan(diff) or math.isinf(diff):
                    continue
                accept = diff <= rtol * abs(g) + atol
                total_score += 1.0 if accept else 0.0
                total_fields += 1
        if total_fields == 0:
            return 0.0
        return (total_score / total_fields) * ratio_frac


_SCORERS = {
    'step_01_coupled_vibration_curves': score_0,
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
