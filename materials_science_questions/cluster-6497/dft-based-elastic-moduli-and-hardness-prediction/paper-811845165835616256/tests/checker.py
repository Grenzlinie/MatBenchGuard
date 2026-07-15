import os
import json
import csv

# === author imports / helpers ===
import json, math


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


# === block: score_0 (check id='shape_check') ===
def score_0(artifact, step, ctx):
    # Ensure required keys exist
    if not isinstance(artifact, dict):
        return 0.0
    for k in step.get("required_keys", []):
        if k not in artifact:
            return 0.0
    cub = artifact.get("cubic", {})
    hex_ = artifact.get("hexagonal", {})
    if not isinstance(cub, dict) or not isinstance(hex_, dict):
        return 0.0
    for k in step.get("required_cubic_keys", []):
        if k not in cub:
            return 0.0
    for k in step.get("required_hexagonal_keys", []):
        if k not in hex_:
            return 0.0
    return 1.0


# === block: score_1 (check id='cubic_values') ===
def score_1(artifact, step, ctx):
    # Compare cubic elastic constants and moduli against gold with tolerance
    def score(artifact, step, ctx):
        cub = artifact.get("cubic", {})
        gold = step.get("gold", {})
        fields = step.get("fields", [])
        tol_frac = step.get("tolerance_pct", 30.0) / 100.0
        ok = 0
        total = len(fields)
        if total == 0:
            return 0.0
        for f in fields:
            v = cub.get(f)
            g = gold.get(f)
            if v is None or g is None or g == 0:
                continue
            if abs(v - g) / abs(g) <= tol_frac:
                ok += 1
        return ok / total


# === block: score_2 (check id='hexagonal_values') ===
def score_2(artifact, step, ctx):
    # Compare hexagonal elastic constants and moduli against gold with tolerance
    def score(artifact, step, ctx):
        hex_ = artifact.get("hexagonal", {})
        gold = step.get("gold", {})
        fields = step.get("fields", [])
        tol_frac = step.get("tolerance_pct", 30.0) / 100.0
        ok = 0
        total = len(fields)
        if total == 0:
            return 0.0
        for f in fields:
            v = hex_.get(f)
            g = gold.get(f)
            if v is None or g is None or g == 0:
                continue
            if abs(v - g) / abs(g) <= tol_frac:
                ok += 1
        return ok / total


# === block: score_3 (check id='G_ratio') ===
def score_3(artifact, step, ctx):
    # Check G(hex)/G(cubic) >= 1.5
    def score(artifact, step, ctx):
        cub = artifact.get("cubic", {})
        hex_ = artifact.get("hexagonal", {})
        G_cub = cub.get("G")
        G_hex = hex_.get("G")
        if G_cub is None or G_hex is None or G_cub <= 0:
            return 0.0
        ratio = G_hex / G_cub
        return 1.0 if ratio >= 1.5 else 0.0


# === block: score_4 (check id='B_diff') ===
def score_4(artifact, step, ctx):
    # Check relative bulk modulus difference <= 20%
    def score(artifact, step, ctx):
        cub = artifact.get("cubic", {})
        hex_ = artifact.get("hexagonal", {})
        B_cub = cub.get("B")
        B_hex = hex_.get("B")
        if B_cub is None or B_hex is None or (B_cub + B_hex) == 0:
            return 0.0
        diff = abs(B_cub - B_hex) / ((B_cub + B_hex) / 2.0)
        return 1.0 if diff <= 0.20 else 0.0


# === block: score_5 (check id='consistency_moduli') ===
def score_5(artifact, step, ctx):
    # Recompute B and G from c_ij and compare with reported B,G (1% tolerance)
    def score(artifact, step, ctx):
        cub = artifact.get("cubic", {})
        hex_ = artifact.get("hexagonal", {})
        def calc_cub_B(c11, c12):
            return (c11 + 2 * c12) / 3.0 if (c11 is not None and c12 is not None) else None
        def calc_cub_G(c11, c12, c44):
            return (c11 - c12 + 3 * c44) / 5.0 if None not in (c11, c12, c44) else None
        def calc_hex_B(c11, c12, c13, c33):
            return (1.0 / 9.0) * (2 * (c11 + c12) + 4 * c13 + c33) if None not in (c11, c12, c13, c33) else None
        def calc_hex_G(c11, c12, c13, c33, c44, c66):
            return (1.0 / 30.0) * (c11 + c12 + 2 * c33 - 4 * c13 + 12 * c44 + 12 * c66) if None not in (c11, c12, c13, c33, c44, c66) else None
        B_cub_r = calc_cub_B(cub.get("c11"), cub.get("c12"))
        G_cub_r = calc_cub_G(cub.get("c11"), cub.get("c12"), cub.get("c44"))
        B_hex_r = calc_hex_B(hex_.get("c11"), hex_.get("c12"), hex_.get("c13"), hex_.get("c33"))
        G_hex_r = calc_hex_G(hex_.get("c11"), hex_.get("c12"), hex_.get("c13"), hex_.get("c33"), hex_.get("c44"), hex_.get("c66"))
        tol = 0.01
        ok = 0
        total = 0
        for recomputed, reported in [(B_cub_r, cub.get("B")), (G_cub_r, cub.get("G")), (B_hex_r, hex_.get("B")), (G_hex_r, hex_.get("G"))]:
            if recomputed is not None and reported is not None and reported != 0:
                total += 1
                if abs(recomputed - reported) / abs(reported) <= tol:
                    ok += 1
        return ok / total if total > 0 else 0.0


_SCORERS = {
    'shape_check': score_0,
    'cubic_values': score_1,
    'hexagonal_values': score_2,
    'G_ratio': score_3,
    'B_diff': score_4,
    'consistency_moduli': score_5,
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
