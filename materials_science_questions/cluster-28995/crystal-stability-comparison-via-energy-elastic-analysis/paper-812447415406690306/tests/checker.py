import os
import json
import csv

# === author imports / helpers ===
import math


def f(x):
    """Electron-lattice kernel f(x) = 1/x^4 * (1 + (1-x^2)/(2x) * ln|(x+1)/(x-1)|)."""
    if x <= 0 or x == 1:
        return 0.0
    return (1.0 / x**4) * (1.0 + (1.0 - x**2) / (2.0 * x) * math.log(abs((x + 1) / (x - 1))))


def compute_bcc_fcc_sum(Z, lattice_type):
    """Compute S = sum_{b!=0} g f(pi b/p_F) for bcc (nu=2) or fcc (nu=4)."""
    nu = 2 if lattice_type == 'bcc' else 4
    a = 1.0
    v = a**3
    pF = math.pi * (3.0 * Z * nu / (math.pi * v))**(1.0 / 3.0)
    N = 18
    S = 0.0
    for h in range(-N, N + 1):
        for k in range(-N, N + 1):
            for l in range(-N, N + 1):
                if h == 0 and k == 0 and l == 0:
                    continue
                if lattice_type == 'bcc':
                    if (h + k + l) % 2 != 0:
                        continue
                    g_val = 4.0
                else:  # fcc
                    if not ((h % 2 == 0 and k % 2 == 0 and l % 2 == 0) or (h % 2 != 0 and k % 2 != 0 and l % 2 != 0)):
                        continue
                    g_val = 16.0
                b_mag = 2.0 * math.pi * math.sqrt(h * h + k * k + l * l)
                x = math.pi * b_mag / pF
                if x <= 1.0:
                    continue
                S += g_val * f(x)
    return S


def compute_hcp_sum(Z):
    """Compute S for hcp with ideal c/a = sqrt(8/3), a=1."""
    nu = 2
    a = 1.0
    c = a * math.sqrt(8.0 / 3.0)
    v = (math.sqrt(3.0) / 2.0) * a * a * c
    pF = math.pi * (3.0 * Z * nu / (math.pi * v))**(1.0 / 3.0)
    # Reciprocal lattice basis (hexagonal)
    b1 = (2 * math.pi / a, (2 * math.pi / a) / math.sqrt(3), 0.0)
    b2 = (0.0, (2 * math.pi / a) * 2 / math.sqrt(3), 0.0)
    b3 = (0.0, 0.0, 2 * math.pi / c)
    N = 15
    S = 0.0
    for h in range(-N, N + 1):
        for k in range(-N, N + 1):
            for l in range(-N, N + 1):
                if h == 0 and k == 0 and l == 0:
                    continue
                gx = h * b1[0] + k * b2[0] + l * b3[0]
                gy = h * b1[1] + k * b2[1] + l * b3[1]
                gz = h * b1[2] + k * b2[2] + l * b3[2]
                b_mag = math.sqrt(gx * gx + gy * gy + gz * gz)
                x = math.pi * b_mag / pF
                if x <= 1.0:
                    continue
                phase = 2 * math.pi * ((2 * h + k) / 3.0 + l / 2.0)
                g = 2.0 + 2.0 * math.cos(phase)  # equivalent to |1+exp|^2
                S += g * f(x)
    return S


def compute_all_energies():
    """Return dict (Z, lattice) -> -E_e-l in units Z^2 e^4 m / h^2."""
    Z_list = [1, 2, 6, 26]
    lattices = ['bcc', 'fcc', 'hcp']
    result = {}
    for Z in Z_list:
        for lat in lattices:
            if lat == 'hcp':
                S = compute_hcp_sum(Z)
                nu = 2
            elif lat == 'bcc':
                S = compute_bcc_fcc_sum(Z, 'bcc')
                nu = 2
            else:  # fcc
                S = compute_bcc_fcc_sum(Z, 'fcc')
                nu = 4
            value = S / (6.0 * math.pi**2 * Z * nu**2)
            result[(Z, lat)] = value
    return result


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
    expected_energies = compute_all_energies()
    return {"expected": expected_energies}


# === block: score_0 (check id='step_01_compute_energy') ===
def score_0(artifact, step, ctx):
    artifact_rows = artifact  # list of dicts
    if len(artifact_rows) != 12:
        return 0.0
    tol_rel = step.get("tolerance_rel", 1e-5)
    tol_abs = step.get("tolerance_abs", 1e-8)

    # Hardcoded expected -E_e-l values in units Z^2 e^4 m/h^2 from the paper Table 1.
    # key: (Z, lattice) -> expected energy
    expected_map = {
        (1, "bcc"): 0.0903860,
        (1, "fcc"): 0.0913073,
        (1, "hcp"): 0.0661690,
        (2, "bcc"): 0.224488,
        (2, "fcc"): 0.219672,
        (2, "hcp"): 0.189904,
        (6, "bcc"): 0.473481,
        (6, "fcc"): 0.474871,
        (6, "hcp"): 0.435366,
        (26, "bcc"): 1.034330,
        (26, "fcc"): 1.036611,
        (26, "hcp"): 0.989050,
    }

    el_map = {"hydrogen": 1, "h": 1, "helium": 2, "he": 2, "carbon": 6, "c": 6, "iron": 26, "fe": 26}
    lat_norm = lambda s: s.replace('.', '').replace(' ', '').lower()
    correct = 0
    for row in artifact_rows:
        elem = row.get("element", "").strip().lower()
        lat = row.get("lattice", "").strip()
        lat_key = lat_norm(lat)
        Z = el_map.get(elem)
        if Z is None or lat_key not in ("bcc", "fcc", "hcp"):
            continue
        key = (Z, lat_key)
        agent_val = float(row.get("energy", float('nan')))
        expected_val = expected_map[key]
        if abs(agent_val - expected_val) <= tol_rel * max(abs(expected_val), 1e-15) + tol_abs:
            correct += 1
    return correct / max(len(artifact_rows), 1)


_SCORERS = {
    'step_01_compute_energy': score_0,
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
