import os
import json
import csv

# === author imports / helpers ===
import csv, math, re, os


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


# === block: score_0 (check id='s3_ntype_dos') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        # artifact: list of dicts with keys 'energy' and 'dos'
        best = None
        for row in artifact:
            try:
                e = float(row['energy'])
                d = float(row['dos'])
            except (ValueError, KeyError):
                continue
            if best is None or abs(e) < abs(best[0]):
                best = (e, d)
        if best is None:
            return 0.0
        e, d = best
        # metallicity: finite DOS at Fermi level (>1e-9)
        return 1.0 if d > 1e-9 else 0.0


# === block: score_1 (check id='s4_ntype_pdos') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        # artifact: list of dicts with keys 'energy','d_xy','d_xz_yz','d_3z2_r2','d_x2_y2'
        best = None
        for row in artifact:
            try:
                e = float(row['energy'])
                dxy = float(row['d_xy'])
                dxz = float(row['d_xz_yz'])
                d3z = float(row['d_3z2_r2'])
                dx2 = float(row['d_x2_y2'])
            except (ValueError, KeyError):
                continue
            if best is None or abs(e) < abs(best[0]):
                best = (e, dxy, dxz, d3z, dx2)
        if best is None:
            return 0.0
        e, dxy, dxz, d3z, dx2 = best
        s = 0.0
        # occupancy
        if dxy > 0 and dxz > 0:
            s += 0.4
        # larger d_xy
        if dxy > dxz:
            s += 0.3
        # empty d_3z2 and d_x2-y2 (threshold relative to d_xy)
        threshold = 0.05 * dxy
        if d3z < threshold and dx2 < threshold:
            s += 0.3
        return s


# === block: score_2 (check id='s5_ptype_dos') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        # artifact: list of dicts with keys 'energy','total_dos','O_2p_dos','Ti_3d_dos'
        best = None
        for row in artifact:
            try:
                e = float(row['energy'])
                total = float(row['total_dos'])
                o2p = float(row['O_2p_dos'])
                ti3d = float(row['Ti_3d_dos'])
            except (ValueError, KeyError):
                continue
            if best is None or abs(e) < abs(best[0]):
                best = (e, total, o2p, ti3d)
        if best is None:
            return 0.0
        e, total, o2p, ti3d = best
        s = 0.0
        if total > 1e-9:
            s += 0.4
        if o2p > ti3d:
            s += 0.6
        return s


# === block: score_3 (check id='s6_spatial') ===
def score_3(artifact, step, ctx):
    def score(artifact, step, ctx):
        # artifact: string, single float
        try:
            val = float(artifact.strip())
        except:
            return 0.0
        ref = 7.8
        tol = 0.2
        relative_error = abs(val - ref) / ref
        return 1.0 if relative_error <= tol else 0.0


# === block: score_4 (check id='s7_vacancy') ===
def score_4(artifact, step, ctx):
    def score(artifact, step, ctx):
        # artifact: string with vacancy text
        text = artifact.lower()
        s = 0.0
        # n-type 25%: metallic, Ti 3d
        if re.search(r'n-type 25%', text) and re.search(r'metallic', text) and re.search(r'ti\s*3d', text):
            s += 0.25
        # n-type 50%: metallic, Ti 3d
        if re.search(r'n-type 50%', text) and re.search(r'metallic', text) and re.search(r'ti\s*3d', text):
            s += 0.25
        # p-type 25%: metallic, O 2p
        if re.search(r'p-type 25%', text) and re.search(r'metallic', text) and re.search(r'o\s*2p', text):
            s += 0.25
        # p-type 50%: metallic, Ti 3d
        if re.search(r'p-type 50%', text) and re.search(r'metallic', text) and re.search(r'ti\s*3d', text):
            s += 0.25
        return s


_SCORERS = {
    's3_ntype_dos': score_0,
    's4_ntype_pdos': score_1,
    's5_ptype_dos': score_2,
    's6_spatial': score_3,
    's7_vacancy': score_4,
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
