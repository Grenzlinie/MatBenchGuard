import os
import json
import csv

# === author imports / helpers ===
import os, csv


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
        ctx = {}
        f1 = os.path.join(outputs_dir, "step_01_field_enhancement_factors.csv")
        if os.path.exists(f1):
            with open(f1, newline='') as f:
                reader = csv.DictReader(f)
                ctx["beta_A_rows"] = list(reader)
        else:
            ctx["beta_A_rows"] = []
        f2 = os.path.join(outputs_dir, "step_02_binding_energies.csv")
        if os.path.exists(f2):
            with open(f2, newline='') as f:
                reader = csv.DictReader(f)
                ctx["binding_rows"] = list(reader)
        else:
            ctx["binding_rows"] = []
        steps = spec.get("steps", [])
        for s in steps:
            if s["id"] == "step_02_binding_energies_check":
                ctx["step2_params"] = s.get("params", {})
        return ctx


# === block: score_0 (check id='step_01_field_enhancement_check') ===
def score_0(artifact, step, ctx):
        gold = step.get("target", {})
        tol = step.get("tolerance_abs", 0.015)
        rows_by_b = {}
        for row in artifact:
            try:
                b_val = float(row["b_E_value"])
            except (ValueError, KeyError):
                continue
            rows_by_b[b_val] = row
        total = 0.0
        count = 0
        for b_str, expected in gold.items():
            b_val = float(b_str)
            if b_val in rows_by_b:
                count += 1
                try:
                    beta = float(rows_by_b[b_val]["beta_A"])
                    if abs(beta - expected) <= tol:
                        total += 1.0
                except (ValueError, KeyError):
                    pass
        if count == 0:
            return 0.0
        return total / count


# === block: score_1 (check id='step_02_binding_energies_check') ===
def score_1(artifact, step, ctx):
        rows2 = artifact
        beta_rows = ctx.get("beta_A_rows", [])
        params = ctx.get("step2_params", {})
        b_A = float(params.get("b_A", 0.143))
        F_ext = float(params.get("F_ext", 56.0))
        eta_map = params.get("eta_map", {})
        Delta_B_disp = float(params.get("Delta_B_disp", 0.010))
        tol_conv_raw = float(params.get("tolerance_conv", 0.005))
        tol_diff_raw = float(params.get("tolerance_diff", 0.005))
        # Enforce a floor of 0.005 eV to be consistent with β_A tolerance and paper precision
        tol_conv = max(tol_conv_raw, 0.005)
        tol_diff = max(tol_diff_raw, 0.005)

        beta_map = {}
        for row in beta_rows:
            try:
                b_val = float(row["b_E_value"])
                beta_map[b_val] = float(row["beta_A"])
            except (ValueError, KeyError):
                pass

        conv_map = {}
        diff_map = {}
        for row in rows2:
            try:
                b_val = float(row["b_E_value"])
                conv_map[b_val] = float(row["Delta_B_conv"])
                diff_map[b_val] = float(row["Delta_B_diff"])
            except (ValueError, KeyError):
                pass

        required_be = [2.00, 7.00]
        conv_ok = 0.0
        diff_ok = 0.0
        n = len(required_be)
        if n == 0:
            return 0.0
        for b_val in required_be:
            if b_val not in beta_map or b_val not in conv_map or b_val not in diff_map:
                continue
            beta = beta_map[b_val]
            conv_expected_mev = 0.5 * b_A * (beta**2 - 1.0) * (F_ext**2)
            conv_expected = conv_expected_mev / 1000.0   # meV -> eV
            conv_submitted = conv_map[b_val]
            if abs(conv_submitted - conv_expected) <= tol_conv:
                conv_ok += 1.0

            eta = float(eta_map.get(str(b_val), 0.5))
            diff_expected = (1 - eta) * conv_expected + 0.5 * Delta_B_disp
            diff_submitted = diff_map[b_val]
            if abs(diff_submitted - diff_expected) <= tol_diff:
                diff_ok += 1.0

        conv_score = conv_ok / n
        diff_score = diff_ok / n
        trend_ok = 1.0 if (2.00 in diff_map and 7.00 in diff_map and diff_map[2.00] < diff_map[7.00]) else 0.0
        return 0.4 * conv_score + 0.4 * diff_score + 0.2 * trend_ok


_SCORERS = {
    'step_01_field_enhancement_check': score_0,
    'step_02_binding_energies_check': score_1,
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
