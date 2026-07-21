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


# === block: score_0 (check id='diffusion_ordering') ===
def score_0(artifact, step, ctx):
    diff = artifact.get("diffusion", {})
    temps = ["291","296","311","321","348"]
    total = 0
    ok = 0
    for t in temps:
        entry = diff.get(t)
        if not isinstance(entry, dict):
            continue
        shell_raw = entry.get("shell")
        bulk_raw = entry.get("bulk")
        if shell_raw is None or bulk_raw is None:
            continue
        try:
            shell = float(shell_raw)
            bulk = float(bulk_raw)
        except (TypeError, ValueError):
            continue
        # shell < bulk
        total += 1
        if shell < bulk:
            ok += 1
        # bulk < pure (when pure is available)
        pure_raw = entry.get("pure")
        if pure_raw is not None:
            try:
                pure = float(pure_raw)
                total += 1
                if bulk < pure:
                    ok += 1
            except (TypeError, ValueError):
                pass
    if total == 0:
        return 0.0
    return ok / total


# === block: score_1 (check id='density_first_shell') ===
def score_1(artifact, step, ctx):
    density = artifact.get("density_first_shell", {})
    expected = {
        "291": True,
        "296": True,
        "311": False,
        "321": False,
        "348": False
    }
    total = 0
    ok = 0
    for t, exp in expected.items():
        entry = density.get(t)
        if isinstance(entry, dict) and "higher_than_bulk" in entry:
            total += 1
            if bool(entry["higher_than_bulk"]) == exp:
                ok += 1
    if total == 0:
        return 0.0
    return ok / total


# === block: score_2 (check id='charge_oscillation') ===
def score_2(artifact, step, ctx):
    arr = artifact.get("charge_oscillation", [])
    if not isinstance(arr, list) or len(arr) < 2:
        return 0.0
    has_alternation = False
    for i in range(len(arr)-1):
        s1 = str(arr[i]).strip()
        s2 = str(arr[i+1]).strip()
        if s1 in ("+", "-") and s2 in ("+", "-") and s1 != s2:
            has_alternation = True
            break
    return 1.0 if has_alternation else 0.0


# === block: score_3 (check id='hb_correlation') ===
def score_3(artifact, step, ctx):
    hb = artifact.get("hb_correlation", {})
    temps = ["291","296","311","321","348"]
    total = 0
    ok = 0
    for t in temps:
        entry = hb.get(t)
        if not isinstance(entry, dict):
            continue
        shell_rank = entry.get("shell_decay_rank")
        bulk_rank = entry.get("bulk_decay_rank")
        if shell_rank is not None:
            total += 1
            if int(shell_rank) == -1:
                ok += 1
        if bulk_rank is not None:
            total += 1
            if int(bulk_rank) == 1:
                ok += 1
    if total == 0:
        return 0.0
    return ok / total


# === block: score_4 (check id='hb_counts') ===
def score_4(artifact, step, ctx):
    hb = artifact.get("hb_counts", {})
    temps = ["291","296","311","321","348"]
    total = 0
    ok = 0
    for t in temps:
        entry = hb.get(t)
        if not isinstance(entry, dict):
            continue
        shell = entry.get("shell")
        bulk = entry.get("bulk")
        if shell is None or bulk is None:
            continue
        try:
            if shell + 1e-9 < bulk:
                total += 1
                ok += 1
            else:
                total += 1
        except Exception:
            pass
    if total == 0:
        return 0.0
    return ok / total


_SCORERS = {
    'diffusion_ordering': score_0,
    'density_first_shell': score_1,
    'charge_oscillation': score_2,
    'hb_correlation': score_3,
    'hb_counts': score_4,
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
