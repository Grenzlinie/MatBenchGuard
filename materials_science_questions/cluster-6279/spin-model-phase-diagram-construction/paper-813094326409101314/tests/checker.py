import os
import json
import csv

# === author imports / helpers ===
from PIL import Image


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
        # Override the broken load_artifact that crashes on binary files
        global load_artifact
        def load_artifact(path):
            if not path or not os.path.exists(path):
                return None
            if path.endswith('.json'):
                try:
                    with open(path) as f:
                        return json.load(f)
                except Exception:
                    return None
            if path.endswith('.csv') or path.endswith('.tsv'):
                delim = '\t' if path.endswith('.tsv') else ','
                with open(path, newline='') as f:
                    return list(csv.DictReader(f, delimiter=delim))
            # For binary/images or unknown types, return None to avoid decode crash
            return None

        steps = spec.get("steps", spec.get("checks", []))
        ref_rows = None
        min_w = 200
        min_h = 200
        for step in steps:
            if step.get("id") == "step_csv":
                ref_rows = step.get("hidden_reference_rows")
            if step.get("id") == "step_png":
                min_w = step.get("min_width", 200)
                min_h = step.get("min_height", 200)
        return {"ref_rows": ref_rows, "min_width": min_w, "min_height": min_h, "outputs_dir": outputs_dir}


# === block: score_0 (check id='step_csv') ===
def score_0(artifact, step, ctx):
        ref_rows = ctx.get("ref_rows")
        if not ref_rows or not artifact:
            return 0.0
        if not all(col in artifact[0] for col in ["K","gamma","omega","Omega","symmetry_type"]):
            return 0.0
        n = len(ref_rows)
        if n == 0:
            return 0.0
        agent_map = {}
        for row in artifact:
            try:
                k = float(row["K"])
                g = float(row["gamma"])
            except (ValueError, KeyError):
                continue
            agent_map[(k, g)] = row
        correct = 0.0
        for ref in ref_rows:
            k = float(ref["K"])
            g = float(ref["gamma"])
            agent_row = agent_map.get((k, g))
            if agent_row is None:
                continue
            if (str(agent_row.get("omega","")) == str(ref["omega"]) and
                str(agent_row.get("Omega","")) == str(ref["Omega"]) and
                str(agent_row.get("symmetry_type","")) == str(ref["symmetry_type"])):
                correct += 1.0
        return correct / n


# === block: score_1 (check id='step_png') ===
def score_1(artifact, step, ctx):
        import os
        from PIL import Image as PILImage
        fp = os.path.join(ctx["outputs_dir"], step["output_file"])
        if not os.path.exists(fp):
            return 0.0
        try:
            im = PILImage.open(fp)
            w, h = im.size
            im.close()
            if w >= ctx["min_width"] and h >= ctx["min_height"]:
                return 1.0
            else:
                return 0.0
        except Exception:
            return 0.0


_SCORERS = {
    'step_csv': score_0,
    'step_png': score_1,
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
