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
    return {}


# === block: score_0 (check id='E_accuracy') ===
def score_0(artifact, step, ctx):
            gold = step['gold']
            tol = step['tolerance_abs']
            rows = artifact
            if not rows:
                return 0.0
            count = 0
            n = min(len(rows), len(gold))
            for i in range(n):
                val = float(rows[i]['E_Ryd'])
                if abs(val - gold[i]) <= tol:
                    count += 1
            return count / n if n > 0 else 0.0


# === block: score_1 (check id='E_consistency') ===
def score_1(artifact, step, ctx):
            import math

            def compute_E(rs, rc):
                Z = 1.0
                alpha = 1.79186
                EM = -alpha * Z**(5./3.) / rs
                E0 = Z * (2.21/rs**2 - 0.916/rs - 0.115 + 0.031 * math.log(rs))
                Omega0 = (4./3.) * math.pi * rs**3
                E1 = 4.0 * math.pi * Z * (rc**2) / Omega0
                kF = (3.0 * math.pi**2 / Omega0) ** (1./3.)
                a = (8.0 * math.pi / 3.0) ** (1./3.) * rs
                Gmax = 5.0 * kF
                max_h = int(Gmax * a / (2.0 * math.pi)) + 2
                Ebs = 0.0
                for h in range(-max_h, max_h+1):
                    for k in range(-max_h, max_h+1):
                        for l in range(-max_h, max_h+1):
                            if h == 0 and k == 0 and l == 0:
                                continue
                            if (h + k + l) % 2 != 0:
                                continue
                            G2 = h**2 + k**2 + l**2
                            G = (2.0 * math.pi / a) * math.sqrt(G2)
                            if G > Gmax:
                                continue
                            q = G
                            x = q / (2.0 * kF)
                            if abs(x - 1.0) < 1e-12:
                                term = 0.5
                            else:
                                term = 0.5 + (1.0 - x**2) / (4.0 * x) * math.log(abs((x + 1.0) / (x - 1.0)))
                            chi = -0.5 * Z * (3.0 / (2.0 * kF**2)) * term
                            eps = 1.0 - (16.0 * math.pi / (Omega0 * q**2)) * chi
                            if eps == 0.0:
                                continue
                            cos_term = math.cos(G * rc)
                            v_sq = (8.0 * math.pi * Z / (Omega0 * G**2)) * cos_term
                            v_sq = v_sq * v_sq
                            Ebs += (chi / eps) * v_sq
                return EM + E0 + E1 + Ebs

            rows = artifact
            if not rows:
                return 0.0
            max_diff = 0.0
            for row in rows:
                rs = float(row['rs_bohr'])
                rc = float(row['rc_bohr'])
                agent_E = float(row['E_Ryd'])
                calc_E = compute_E(rs, rc)
                diff = abs(agent_E - calc_E)
                if diff > max_diff:
                    max_diff = diff
            threshold = 0.01
            return 1.0 if max_diff <= threshold else 0.0


# === block: score_2 (check id='B_accuracy') ===
def score_2(artifact, step, ctx):
            gold = step['gold']
            tol = step['tolerance_abs']
            rows = artifact
            if not rows:
                return 0.0
            count = 0
            n = min(len(rows), len(gold))
            for i in range(n):
                val = float(rows[i]['B_erg_per_cm2'])
                if abs(val - gold[i]) <= tol:
                    count += 1
            return count / n if n > 0 else 0.0


# === block: score_3 (check id='DeltaH_accuracy') ===
def score_3(artifact, step, ctx):
            gold = step['gold']
            tol = step['tolerance_abs']
            rows = artifact
            if not rows:
                return 0.0
            count = 0
            n = min(len(rows), len(gold))
            for i in range(n):
                val = float(rows[i]['Delta_H_mRyd'])
                if abs(val - gold[i]) <= tol:
                    count += 1
            return count / n if n > 0 else 0.0


_SCORERS = {
    'E_accuracy': score_0,
    'E_consistency': score_1,
    'B_accuracy': score_2,
    'DeltaH_accuracy': score_3,
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
