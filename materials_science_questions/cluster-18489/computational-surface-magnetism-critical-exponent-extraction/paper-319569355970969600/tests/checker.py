import os
import json
import csv

# === author imports / helpers ===
import numpy as np
import csv

def bisect(f, a, b, xtol=1e-12, maxiter=100):
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        raise ValueError("f(a) and f(b) must have opposite signs")
    for _ in range(maxiter):
        c = (a + b) / 2.0
        fc = f(c)
        if fc == 0.0 or (b - a) / 2.0 < xtol:
            return c
        if fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc
    return (a + b) / 2.0


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


# === block: score_0 (check id='numeric_recompute') ===
def score_0(artifact, step, ctx):
    def _build_nanowire_mat(T, Sc, Ss, J1_div_J, delta_s):
        J = 1.0
        J1 = J1_div_J * J
        Js = J * (1 + delta_s)
        ccoeff = 3*Sc*T/(Sc+1)
        scoeff = 3*Ss*T/(Ss+1)
        A = np.zeros((4,4))
        A[0,0] = ccoeff - 2*J
        A[0,1] = -6*J
        A[1,0] = -J
        A[1,1] = ccoeff - 4*J
        A[1,2] = -2*J1
        A[1,3] = -J1
        A[2,1] = -2*J1
        A[2,2] = scoeff - 2*Js
        A[2,3] = -2*Js
        A[3,1] = -J1
        A[3,2] = -2*Js
        A[3,3] = scoeff - 2*Js
        return A

    def _build_nanotube_mat(T, Sc, Ss, J1_div_J, delta_s):
        J = 1.0
        J1 = J1_div_J * J
        Js = J * (1 + delta_s)
        ccoeff = 3*Sc*T/(Sc+1)
        scoeff = 3*Ss*T/(Ss+1)
        A = np.zeros((3,3))
        A[0,0] = ccoeff - 4*J
        A[0,1] = -2*J1
        A[0,2] = -J1
        A[1,0] = -2*J1
        A[1,1] = scoeff - 2*Js
        A[1,2] = -2*Js
        A[2,0] = -J1
        A[2,1] = -2*Js
        A[2,2] = scoeff - 2*Js
        return A

    def _det_val(T, geometry, Sc, Ss, J1_div_J, delta_s):
        if geometry == "nanowire":
            A = _build_nanowire_mat(T, Sc, Ss, J1_div_J, delta_s)
        elif geometry == "nanotube":
            A = _build_nanotube_mat(T, Sc, Ss, J1_div_J, delta_s)
        else:
            raise ValueError("Unknown geometry")
        return np.linalg.det(A)

    def _find_Tc(geometry, Sc, Ss, J1_div_J, delta_s, bracket=(0.01, 20.0)):
        fa = _det_val(bracket[0], geometry, Sc, Ss, J1_div_J, delta_s)
        fb = _det_val(bracket[1], geometry, Sc, Ss, J1_div_J, delta_s)
        if fa * fb > 0:
            return None  # root not bracketed (should not happen)
        return bisect(lambda T: _det_val(T, geometry, Sc, Ss, J1_div_J, delta_s), bracket[0], bracket[1], xtol=1e-12, maxiter=100)

    try:
        rows = [dict(row) for row in artifact]
    except Exception:
        return 0.0

    if not rows:
        return 0.0

    tolerance = float(step.get("tolerance", 0.001))

    passed = 0
    for row in rows:
        try:
            geom = str(row["geometry"]).strip().lower()
            if geom not in ("nanowire", "nanotube"):
                continue
            sc = float(row["Sc"])
            ss = float(row["Ss"])
            j1_div = float(row["J1_div_J"])
            ds = float(row["delta_s"])
            agent_tc = float(row["Tc"])
            tc = _find_Tc(geom, sc, ss, j1_div, ds)
            if tc is None:
                continue
            rel_err = abs(agent_tc - tc) / max(abs(tc), 1e-8)
            if rel_err < tolerance:
                passed += 1
        except Exception:
            continue

    score = passed / len(rows) if rows else 0.0
    return score


# === block: score_1 (check id='structural_ordering') ===
def score_1(artifact, step, ctx):
    try:
        rows = [dict(row) for row in artifact]
    except Exception:
        return 0.0

    if not rows:
        return 0.0

    from collections import defaultdict
    pairs = defaultdict(dict)
    for row in rows:
        try:
            geom = str(row["geometry"]).strip().lower()
            if geom not in ("nanowire", "nanotube"):
                continue
            key = (float(row["Sc"]), float(row["Ss"]), float(row["J1_div_J"]), float(row["delta_s"]))
            pairs[key][geom] = float(row["Tc"])
        except Exception:
            continue

    checked = 0
    passed = 0
    for key, vals in pairs.items():
        if "nanowire" in vals and "nanotube" in vals:
            checked += 1
            if vals["nanowire"] > vals["nanotube"]:
                passed += 1

    score = passed / checked if checked > 0 else 0.0
    return score


_SCORERS = {
    'numeric_recompute': score_0,
    'structural_ordering': score_1,
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
