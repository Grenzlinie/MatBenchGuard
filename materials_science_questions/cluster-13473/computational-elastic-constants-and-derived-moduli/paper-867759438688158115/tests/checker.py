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
# ...
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
    # No hidden gold needed; consistency checks use only the agent's data.
    return {}


# === block: score_0 (check id='shear_modulus_check') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not rows or not isinstance(rows, list):
        return 0.0

    # group by system
    data = {"RN": {}, "FCC": {}}
    for row in rows:
        try:
            sys = str(row.get("system", "")).strip()
            if sys not in data:
                continue
            Z = int(float(row.get("Z", 0)))
            G = float(row.get("G", 0))
            G_A = float(row.get("G_A", 0))
            G_NA = float(row.get("G_NA", 0))
        except:
            continue
        data[sys][Z] = (G, G_A, G_NA)

    checks_passed = 0
    total_checks = 0

    for sys in ["RN", "FCC"]:
        sys_data = data[sys]
        Zs = sorted(sys_data.keys())
        # check identity G == G_A - G_NA
        for Z in Zs:
            G, G_A, G_NA = sys_data[Z]
            total_checks += 1
            if abs(G - (G_A - G_NA)) < max(0.01, 0.05 * (abs(G_A) + abs(G_NA) + 1e-6)):
                checks_passed += 1

        # check positivity
        for Z in Zs:
            G, G_A, G_NA = sys_data[Z]
            total_checks += 1
            if G_A > 0 and G_NA > -1e-6:
                checks_passed += 1

        # monotonic increase of G with Z
        if len(Zs) >= 2:
            total_checks += 1
            values = [sys_data[z][0] for z in Zs]
            if all(values[i] <= values[i+1] + 1e-6 for i in range(len(values)-1)):
                checks_passed += 1

    if total_checks == 0:
        return 0.0
    return max(0.0, min(1.0, checks_passed / total_checks))


# === block: score_1 (check id='order_parameters_check') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not rows or not isinstance(rows, list):
        return 0.0

    data = {"RN": {}, "FCC": {}}
    for row in rows:
        try:
            sys = str(row.get("system", "")).strip()
            if sys not in data:
                continue
            Z = int(float(row.get("Z", 0)))
            F_IS = float(row.get("F_IS", 0))
            F_6 = float(row.get("F_6", 0))
        except:
            continue
        data[sys][Z] = (F_IS, F_6)

    checks_passed = 0
    total_checks = 0

    for sys in ["RN", "FCC"]:
        sys_data = data[sys]
        Zs = sorted(sys_data.keys())
        # range check for F_IS
        for Z in Zs:
            F_IS, _ = sys_data[Z]
            total_checks += 1
            if 0.0 <= F_IS <= 1.0:
                checks_passed += 1
        # monotonic increase of F_IS with Z
        if len(Zs) >= 2:
            total_checks += 1
            fis_vals = [sys_data[z][0] for z in Zs]
            if all(fis_vals[i] <= fis_vals[i+1] + 1e-6 for i in range(len(fis_vals)-1)):
                checks_passed += 1
        # F_6 range: FCC should be near 1.0, RN near 0.3
        f6_vals = [sys_data[z][1] for z in Zs]
        total_checks += 1
        if sys == "FCC":
            if all(abs(v - 1.0) <= 0.15 for v in f6_vals):
                checks_passed += 1
        else:  # RN
            if all(abs(v - 0.3) <= 0.25 for v in f6_vals):
                checks_passed += 1
        # F_6 variation across Z should be small (std < 0.1)
        import math
        if len(f6_vals) >= 2:
            total_checks += 1
            mean_f6 = sum(f6_vals)/len(f6_vals)
            std_f6 = math.sqrt(sum((v-mean_f6)**2 for v in f6_vals)/len(f6_vals))
            if std_f6 < 0.1:
                checks_passed += 1

    if total_checks == 0:
        return 0.0
    return max(0.0, min(1.0, checks_passed / total_checks))


# === block: score_2 (check id='boson_peak_check') ===
def score_2(artifact, step, ctx):
    rows = artifact
    if not rows or not isinstance(rows, list):
        return 0.0

    data = {"RN": {}, "FCC": {}}
    for row in rows:
        try:
            sys = str(row.get("system", "")).strip()
            if sys not in data:
                continue
            Z = int(float(row.get("Z", 0)))
            w = float(row.get("omega_BP", 0))
        except:
            continue
        data[sys][Z] = w

    checks_passed = 0
    total_checks = 0

    for sys in ["RN", "FCC"]:
        sys_data = data[sys]
        Zs = sorted(sys_data.keys())

        # positivity
        for Z in Zs:
            w = sys_data[Z]
            total_checks += 1
            if w > 0:
                checks_passed += 1

        # monotonic increase with Z
        if len(Zs) >= 2:
            total_checks += 1
            w_vals = [sys_data[z] for z in Zs]
            if all(w_vals[i] <= w_vals[i+1] + 1e-6 for i in range(len(w_vals)-1)):
                checks_passed += 1

    if total_checks == 0:
        return 0.0
    return max(0.0, min(1.0, checks_passed / total_checks))


# === block: score_3 (check id='dos_consistency_check') ===
def score_3(artifact, step, ctx):
    import json, os, csv as _csv_mod
    dos_data = artifact
    bp_path = "/app/outputs/boson_peak.csv"
    if not os.path.exists(bp_path):
        return 0.0

    bp_rows = []
    with open(bp_path, newline="") as f:
        reader = _csv_mod.DictReader(f)
        for row in reader:
            bp_rows.append(row)
    # Build dict: (system, Z) -> reported omega_BP
    omega_bp_reported = {}
    for row in bp_rows:
        sys = row.get("system", "").strip()
        try:
            Z = str(int(float(row.get("Z", 0))))
            w = float(row.get("omega_BP", 0))
        except:
            continue
        omega_bp_reported[(sys, Z)] = w

    required_keys = [
        "RN_Z6", "RN_Z7", "RN_Z8", "RN_Z9",
        "FCC_Z6", "FCC_Z7", "FCC_Z8", "FCC_Z9"
    ]
    scores = []
    for key in required_keys:
        if key not in dos_data:
            continue
        data = dos_data[key]
        freqs = data.get("frequencies", [])
        dos = data.get("dos", [])
        if len(freqs) < 3 or len(dos) != len(freqs):
            continue
        # compute reduced DOS: dos / w^2
        reduced = []
        for i, w in enumerate(freqs):
            if w > 1e-6:
                reduced.append(dos[i] / (w * w))
            else:
                reduced.append(0.0)
        if not reduced:
            continue
        max_idx = max(range(len(reduced)), key=lambda i: reduced[i])
        peak_freq = freqs[max_idx]
        # get reported omega_BP for this system and Z
        parts = key.split("_")
        if len(parts) != 2:
            continue
        sys, Z_str = parts[0], parts[1]
        Z = Z_str[1:]  # e.g. '6'
        rep_w = omega_bp_reported.get((sys, Z))
        if rep_w is None:
            continue
        # tolerance: bin width max (take first bin difference) or 0.02
        if len(freqs) > 1:
            bin_width = freqs[1] - freqs[0]
        else:
            bin_width = 0.02
        tol = max(2 * bin_width, 0.02)
        if abs(peak_freq - rep_w) <= tol:
            scores.append(1.0)
        else:
            scores.append(0.0)
    if not scores:
        return 0.0
    score = sum(scores) / len(required_keys)
    return max(0.0, min(1.0, score))


_SCORERS = {
    'shear_modulus_check': score_0,
    'order_parameters_check': score_1,
    'boson_peak_check': score_2,
    'dos_consistency_check': score_3,
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