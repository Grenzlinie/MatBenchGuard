import os
import json
import csv

# === author imports / helpers ===
import os
from collections import defaultdict

def parse_dos_dat(content):
    data = []
    for line in content.strip().splitlines():
        parts = line.strip().split()
        if len(parts) >= 3:
            data.append((float(parts[0]), float(parts[1]), float(parts[2])))
    return data

def parse_bands_dat(content):
    data = []
    for line in content.strip().splitlines():
        parts = line.strip().split()
        if len(parts) >= 5:
            data.append((float(parts[0]), float(parts[1]), float(parts[2]), int(parts[3]), float(parts[4])))
    return data


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
    ba_dos_content = load_artifact(os.path.join(outputs_dir, 'dos_BaFe2As2.dat'))
    la_dos_content = load_artifact(os.path.join(outputs_dir, 'dos_LaOFeAs.dat'))
    ba_bands_content = load_artifact(os.path.join(outputs_dir, 'bands_BaFe2As2.dat'))
    la_bands_content = load_artifact(os.path.join(outputs_dir, 'bands_LaOFeAs.dat'))

    ctx = {
        'ba_dos_data': parse_dos_dat(ba_dos_content) if ba_dos_content else [],
        'la_dos_data': parse_dos_dat(la_dos_content) if la_dos_content else [],
        'ba_bands_data': parse_bands_dat(ba_bands_content) if ba_bands_content else [],
        'la_bands_data': parse_bands_dat(la_bands_content) if la_bands_content else [],
    }
    return ctx


# === block: score_0 (check id='dos_BaFe2As2_audit') ===
def score_0(artifact, step, ctx):
    data = ctx.get('ba_dos_data', [])
    if not data:
        return 0.0
    fe_max = max(row[2] for row in data)
    if fe_max > 0:
        return 1.0
    return 0.0


# === block: score_1 (check id='dos_LaOFeAs_audit') ===
def score_1(artifact, step, ctx):
    data = ctx.get('la_dos_data', [])
    if not data:
        return 0.0
    fe_max = max(row[2] for row in data)
    if fe_max > 0:
        return 1.0
    return 0.0


# === block: score_2 (check id='bands_BaFe2As2_audit') ===
def score_2(artifact, step, ctx):
    data = ctx.get('ba_bands_data', [])
    if not data:
        return 0.0
    eigenvals = [row[4] for row in data]
    has_neg = any(v < 0 for v in eigenvals)
    has_pos = any(v > 0 for v in eigenvals)
    return 1.0 if has_neg and has_pos else 0.0


# === block: score_3 (check id='bands_LaOFeAs_audit') ===
def score_3(artifact, step, ctx):
    data = ctx.get('la_bands_data', [])
    if not data:
        return 0.0
    eigenvals = [row[4] for row in data]
    has_neg = any(v < 0 for v in eigenvals)
    has_pos = any(v > 0 for v in eigenvals)
    return 1.0 if has_neg and has_pos else 0.0


# === block: score_4 (check id='fermi_surface_topology') ===
def score_4(artifact, step, ctx):
    def count_bands_at_k(bands_data, kx_target, ky_target, kz_target, condition):
        eps = 1e-6
        band_vals = defaultdict(list)
        for (kx,ky,kz,idx,e) in bands_data:
            if abs(kx-kx_target)<eps and abs(ky-ky_target)<eps and abs(kz-kz_target)<eps:
                band_vals[idx].append(e)
        count = 0
        for idx, es in band_vals.items():
            if condition(es[0]):
                count += 1
        return count

    ba_bands = ctx.get('ba_bands_data', [])
    la_bands = ctx.get('la_bands_data', [])

    holes_ba = count_bands_at_k(ba_bands, 0.0, 0.0, 0.0, lambda e: e < 0)
    electrons_ba = count_bands_at_k(ba_bands, 0.5, 0.0, 0.0, lambda e: e < 0)
    holes_la = count_bands_at_k(la_bands, 0.0, 0.0, 0.0, lambda e: e < 0)
    electrons_la = count_bands_at_k(la_bands, 0.5, 0.0, 0.0, lambda e: e < 0)

    expected = step.get('expected', {})
    if (holes_ba == expected.get('Ba_holes', 3) and electrons_ba == expected.get('Ba_electrons', 2) and
        holes_la == expected.get('La_holes', 3) and electrons_la == expected.get('La_electrons', 2)):
        return 1.0
    else:
        return 0.0


# === block: score_5 (check id='bandwidth_comparison') ===
def score_5(artifact, step, ctx):
    def compute_bandwidth(dos_data):
        fe_vals = [row[2] for row in dos_data]
        energies = [row[0] for row in dos_data]
        max_fe = max(fe_vals)
        if max_fe <= 0:
            return 0.0
        threshold = 0.1 * max_fe
        min_e = None
        max_e = None
        for e, val in zip(energies, fe_vals):
            if val >= threshold:
                if min_e is None or e < min_e:
                    min_e = e
                if max_e is None or e > max_e:
                    max_e = e
        if min_e is None or max_e is None:
            return 0.0
        return max_e - min_e

    ba_dos = ctx.get('ba_dos_data', [])
    la_dos = ctx.get('la_dos_data', [])
    bw_ba = compute_bandwidth(ba_dos)
    bw_la = compute_bandwidth(la_dos)
    diff = bw_ba - bw_la
    target_diff = step.get('target_difference_eV', 0.30)
    tolerance = step.get('tolerance_eV', 0.15)
    deviation = abs(diff - target_diff)
    if deviation <= tolerance:
        score = 1.0
    else:
        score = max(0.0, 1.0 - (deviation - tolerance) / tolerance)
    return score


_SCORERS = {
    'dos_BaFe2As2_audit': score_0,
    'dos_LaOFeAs_audit': score_1,
    'bands_BaFe2As2_audit': score_2,
    'bands_LaOFeAs_audit': score_3,
    'fermi_surface_topology': score_4,
    'bandwidth_comparison': score_5,
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
