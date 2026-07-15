import os
import json
import csv

# === author imports / helpers ===
import math


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


# === block: score_0 (check id='step5_extract_geometry') ===
def score_0(artifact, step, ctx):
    xyz_text = artifact
    if not xyz_text:
        return 0.0
    targets = step.get("targets", [])
    if not targets:
        return 0.0

    atoms = []
    for line in xyz_text.strip().splitlines():
        parts = line.strip().split()
        if len(parts) >= 4:
            try:
                x = float(parts[-3])
                y = float(parts[-2])
                z = float(parts[-1])
                elem = parts[0]
                atoms.append((elem, (x, y, z)))
            except ValueError:
                continue

    ru_list = [pos for elem, pos in atoms if elem == "Ru"]
    si_list = [pos for elem, pos in atoms if elem == "Si"]
    h_list  = [pos for elem, pos in atoms if elem == "H"]

    if not ru_list or not si_list or not h_list:
        return 0.0

    def dist(a,b):
        return math.sqrt(sum((ai-bi)**2 for ai,bi in zip(a,b)))

    def angle_deg(a,b,c):
        # angle at b: vectors ba and bc
        v1 = (a[0]-b[0], a[1]-b[1], a[2]-b[2])
        v2 = (c[0]-b[0], c[1]-b[1], c[2]-b[2])
        dot = v1[0]*v2[0]+v1[1]*v2[1]+v1[2]*v2[2]
        norm1 = math.sqrt(sum(x*x for x in v1))
        norm2 = math.sqrt(sum(x*x for x in v2))
        if norm1==0 or norm2==0:
            return 0.0
        cos = dot/(norm1*norm2)
        cos = max(-1.0, min(1.0, cos))
        return math.degrees(math.acos(cos))

    for ru in ru_list:
        for si in si_list:
            d_ru_si = dist(ru, si)
            for h in h_list:
                d_ru_h = dist(ru, h)
                d_si_h = dist(si, h)
                ang = angle_deg(ru, h, si)
                checks = [
                    abs(d_ru_h - targets[0]["value"]) <= targets[0]["tolerance"],
                    abs(d_si_h - targets[1]["value"]) <= targets[1]["tolerance"],
                    abs(d_ru_si - targets[2]["value"]) <= targets[2]["tolerance"],
                    abs(ang - targets[3]["value"]) <= targets[3]["tolerance"],
                ]
                if all(checks):
                    return 1.0
    return 0.0


_SCORERS = {
    'step5_extract_geometry': score_0,
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
