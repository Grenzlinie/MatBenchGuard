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
    def prepare(outputs_dir, spec):
        def cube(i):
            return 8*i**3, i*((4*i-2)*(4*i-1)+1), 6*((2*i-1)**2+3*i-1)
        def octahedron(i):
            n_nc = (i+1)*(4*(i+1)**2-1)//3
            n_bnd = 2*i*(i+1) + (4*i*(i+1)*(2*i+1))//3
            n_if = 4*(i+1)**2
            return n_nc, n_bnd, n_if
        def dodecahedron_odd(i):
            n_nc = 16*i*((i+1)*(24*i+9) - 8*(i+1)*(2*i+1)) + 10*(4*i+1)
            n_bnd = 16*i*(3*(16*i+5)*(i+1) - 16*(i+1)*(2*i+1)) + 4*(23*i+3)
            n_if = 128*i*(i+1) - 184*i + 112
            return n_nc, n_bnd, n_if
        def dodecahedron_even(i):
            n_nc = 16*i*((24*i+21)*(i+1) - 8*(i+1)*(2*i+1)) + 88*(i+1)
            n_bnd = 16*i*(3*(16*i+13)*(i+1) - 16*(i+1)*(2*i+1)) + 140*(i+1)
            n_if = 128*i*(i+1) - 56*i + 136
            return n_nc, n_bnd, n_if
        def pyramid(i):
            n_nc = (i*(i+1)*(2*(2*i+1)+9))//6 + i + 1
            n_bnd = (2*i*(i+1)*(2*i+1))//3 + i*(i+1)
            n_if = 4*(i+1)**2
            return n_nc, n_bnd, n_if
        def tetrahedron(i):
            n_nc = (i*(i+1)*(2*i+1))//6 + (i+1)**2
            n_bnd = (i*(i+1)*(2*i+1))//3 + i*(i+1)
            n_if = 2*(i+1)*(i+2)
            return n_nc, n_bnd, n_if
        def quatro_111(i):
            n_nc = 9*i*(2*i+1)**2 + (2*i+1) - i*(4*i+5)*(i+1)
            n_bnd = 2*i*(3*i+1)*(12*i+5) - (4*i*(i+1)*(2*i+1) + 6*i*(i+1))
            n_if = (6*i+2)**2
            return n_nc, n_bnd, n_if
        def quatro_001(i):
            n_nc = ((2*i+7)*(5*i*i+35*i+63) + 6*(i+3)*(i*i+9*i+16) + 4*(i+1)*(i+2)*(i+3))//3
            n_bnd = 80*i*i + 340*i + 384 + (2*(i+1)*(20*i*i+49*i+30))//3
            n_if = 4*(2*i+7)**2
            return n_nc, n_bnd, n_if
        shapes = [
            ("cube",               cube,              ""),
            ("octahedron",         octahedron,        ""),
            ("dodecahedron",       dodecahedron_odd,  "odd"),
            ("dodecahedron",       dodecahedron_even, "even"),
            ("pyramid",            pyramid,           ""),
            ("tetrahedron",        tetrahedron,       ""),
            ("quatro_111",         quatro_111,        ""),
            ("quatro_001",         quatro_001,        ""),
        ]
        gold = {}
        for shape_name, func, subclass in shapes:
            for i in range(1, 8):
                gold[(shape_name, subclass, i)] = func(i)
        return {"gold": gold}


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
        def cube(i):
            return 8*i**3, i*((4*i-2)*(4*i-1)+1), 6*((2*i-1)**2+3*i-1)
        def octahedron(i):
            n_nc = (i+1)*(4*(i+1)**2-1)//3
            n_bnd = 2*i*(i+1) + (4*i*(i+1)*(2*i+1))//3
            n_if = 4*(i+1)**2
            return n_nc, n_bnd, n_if
        def dodecahedron_odd(i):
            n_nc = 16*i*((i+1)*(24*i+9) - 8*(i+1)*(2*i+1)) + 10*(4*i+1)
            n_bnd = 16*i*(3*(16*i+5)*(i+1) - 16*(i+1)*(2*i+1)) + 4*(23*i+3)
            n_if = 128*i*(i+1) - 184*i + 112
            return n_nc, n_bnd, n_if
        def dodecahedron_even(i):
            n_nc = 16*i*((24*i+21)*(i+1) - 8*(i+1)*(2*i+1)) + 88*(i+1)
            n_bnd = 16*i*(3*(16*i+13)*(i+1) - 16*(i+1)*(2*i+1)) + 140*(i+1)
            n_if = 128*i*(i+1) - 56*i + 136
            return n_nc, n_bnd, n_if
        def pyramid(i):
            n_nc = (i*(i+1)*(2*(2*i+1)+9))//6 + i + 1
            n_bnd = (2*i*(i+1)*(2*i+1))//3 + i*(i+1)
            n_if = 4*(i+1)**2
            return n_nc, n_bnd, n_if
        def tetrahedron(i):
            n_nc = (i*(i+1)*(2*i+1))//6 + (i+1)**2
            n_bnd = (i*(i+1)*(2*i+1))//3 + i*(i+1)
            n_if = 2*(i+1)*(i+2)
            return n_nc, n_bnd, n_if
        def quatro_111(i):
            n_nc = 9*i*(2*i+1)**2 + (2*i+1) - i*(4*i+5)*(i+1)
            n_bnd = 2*i*(3*i+1)*(12*i+5) - (4*i*(i+1)*(2*i+1) + 6*i*(i+1))
            n_if = (6*i+2)**2
            return n_nc, n_bnd, n_if
        def quatro_001(i):
            n_nc = (3*(2*i+7)*(i+4)**2 + (2*i+7)*(i+3)*(2*i+5) + 6*(i+3)*((i+4)**2 + i) + 4*(i+1)*(i+2)*(i+3)) // 3
            term2 = (i+1)*(20*i*i + 49*i + 30)//6
            n_bnd = 4 * (6*(i+3)**2 + term2 + 7*(2*i+3)*(i+2))
            n_if = 4*(2*i+7)**2
            return n_nc, n_bnd, n_if
        shapes = [
            ("cube",               cube,              ""),
            ("octahedron",         octahedron,        ""),
            ("dodecahedron",       dodecahedron_odd,  "odd"),
            ("dodecahedron",       dodecahedron_even, "even"),
            ("pyramid",            pyramid,           ""),
            ("tetrahedron",        tetrahedron,       ""),
            ("quatro_111",         quatro_111,        ""),
            ("quatro_001",         quatro_001,        ""),
        ]
        gold = {}
        for shape_name, func, subclass in shapes:
            for i in range(1, 8):
                gold[(shape_name, subclass, i)] = func(i)
        if not artifact or not hasattr(artifact, '__iter__'):
            return 0.0
        artifact_map = {}
        for row in artifact:
            try:
                shape = row.get("shape", "").strip()
                subclass = row.get("subclass", "").strip()
                i_val = int(row.get("i", -1))
                n_nc = int(row.get("N_NC", -1))
                n_bnd = int(row.get("N_bnd", -1))
                n_if = int(row.get("N_IF", -1))
                key = (shape, subclass, i_val)
                artifact_map[key] = (n_nc, n_bnd, n_if)
            except (ValueError, TypeError):
                continue
        correct = 0
        total = len(gold)
        for key, vals in gold.items():
            if key in artifact_map and artifact_map[key] == vals:
                correct += 1
        return correct / total if total > 0 else 0.0


_SCORERS = {
    'step_01': score_0,
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
