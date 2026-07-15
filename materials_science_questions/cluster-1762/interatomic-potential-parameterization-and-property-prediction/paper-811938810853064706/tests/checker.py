import os
import json
import csv

# === author imports / helpers ===
import csv, math, numpy as np, collections


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
    steps = spec.get("steps", [])
    ctx = {}
    for step in steps:
        sid = step.get("id")
        extra = step.get("extra", {})
        if sid == "step_phonon":
            ctx["phonon"] = extra
        elif sid == "step_elastic":
            ctx["elastic"] = extra
        elif sid == "step_zpe":
            ctx["zpe"] = extra
    return ctx


# === block: score_0 (check id='step_phonon') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    fc = ctx["phonon"]["force_constants"]
    a_dict = ctx["phonon"]["lattice_a_nm"]
    mass_dict = ctx["phonon"]["mass_g"]
    tol = ctx["phonon"]["trace_tolerance"]

    from collections import defaultdict
    groups = defaultdict(list)
    for r in rows:
        try:
            metal = r["metal"].strip()
            qx = float(r["qx"])
            qy = float(r["qy"])
            qz = float(r["qz"])
            freq = float(r["frequency_THz"])
            groups[(metal, qx, qy, qz)].append(freq)
        except (ValueError, KeyError):
            continue

    if not groups:
        return 0.0

    scores = []
    for (metal, qx, qy, qz), freqs in groups.items():
        if metal not in fc or metal not in a_dict or metal not in mass_dict:
            continue
        const = fc[metal]
        a = a_dict[metal] * 1e-7  # nm to cm
        m = mass_dict[metal]  # g

        alpha1 = const["alpha1"]
        beta1  = const["beta1"]
        alpha2 = const["alpha2"]
        beta2  = const["beta2"]

        # Reduced q: zone-boundary X is (1,0,0), corresponding to wavevector π/a
        # Paper Eq. (4.1): C_α' = cos(a * q_α' / 2) = cos(π * q_red_α)
        Cx = math.cos(math.pi * qx)
        Cy = math.cos(math.pi * qy)
        Cz = math.cos(math.pi * qz)
        Sx = math.sin(math.pi * qx)
        Sy = math.sin(math.pi * qy)
        Sz = math.sin(math.pi * qz)

        base = 4.0 * (beta1 + 2.0 * alpha1)
        # Dxx
        Dxx = base - 2.0*(beta1 + alpha1)*Cx*(Cy + Cz) - 4.0*alpha1*Cy*Cz + 4.0*beta2*Sx*Sx + 4.0*alpha2*(Sy*Sy + Sz*Sz)
        # Dyy
        Dyy = base - 2.0*(beta1 + alpha1)*Cy*(Cz + Cx) - 4.0*alpha1*Cz*Cx + 4.0*beta2*Sy*Sy + 4.0*alpha2*(Sz*Sz + Sx*Sx)
        # Dzz
        Dzz = base - 2.0*(beta1 + alpha1)*Cz*(Cx + Cy) - 4.0*alpha1*Cx*Cy + 4.0*beta2*Sz*Sz + 4.0*alpha2*(Sx*Sx + Sy*Sy)

        # trace in units of 10^4 dyne/cm -> convert to dyne/cm
        Tr_expected = (Dxx + Dyy + Dzz) * 1.0e4

        # Sum of mass * omega^2 from reported frequencies (THz)
        sum_lambda = 0.0
        for f in freqs:
            omega = 2.0 * math.pi * f * 1.0e12  # rad/s
            sum_lambda += m * omega * omega  # g/s^2 = dyne/cm

        if Tr_expected <= 1e-12:
            continue
        err = abs(sum_lambda - Tr_expected) / Tr_expected
        if err <= tol:
            scores.append(1.0)
        else:
            sc = max(0.0, 1.0 - (err - tol) / tol)
            scores.append(sc)

    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_1 (check id='step_elastic') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    gold = ctx["elastic"]["gold"]
    tol = ctx["elastic"]["tolerance"]
    scores = []
    for r in rows:
        metal = r["metal"].strip()
        if metal not in gold:
            continue
        for col in ["C11", "C12", "C44"]:
            try:
                v = float(r[col])
            except (ValueError, KeyError):
                continue
            g = gold[metal][col]
            if g == 0.0:
                continue
            err = abs(v - g) / abs(g)
            if err <= tol:
                scores.append(1.0)
            else:
                sc = max(0.0, 1.0 - (err - tol) / tol)
                scores.append(sc)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_2 (check id='step_zpe') ===
def score_2(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    gold = ctx["zpe"]["gold"]
    tol = ctx["zpe"]["tolerance"]
    scores = []
    for r in rows:
        metal = r["metal"].strip()
        if metal not in gold:
            continue
        try:
            v = float(r["ZPE_cal_mol"])
        except (ValueError, KeyError):
            continue
        g = gold[metal]
        err = abs(v - g) / abs(g)
        if err <= tol:
            scores.append(1.0)
        else:
            sc = max(0.0, 1.0 - (err - tol) / tol)
            scores.append(sc)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


_SCORERS = {
    'step_phonon': score_0,
    'step_elastic': score_1,
    'step_zpe': score_2,
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
