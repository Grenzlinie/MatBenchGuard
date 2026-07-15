import os
import json
import csv

# === author imports / helpers ===
import math

def spearmanr(x, y):
    n = len(x)
    rank_x = _rank(x, n)
    rank_y = _rank(y, n)
    mean_x = sum(rank_x) / n
    mean_y = sum(rank_y) / n
    num = sum((rx - mean_x) * (ry - mean_y) for rx, ry in zip(rank_x, rank_y))
    den1 = math.sqrt(sum((rx - mean_x) ** 2 for rx in rank_x))
    den2 = math.sqrt(sum((ry - mean_y) ** 2 for ry in rank_y))
    if den1 == 0.0 or den2 == 0.0:
        return 0.0, 0.0
    rho = num / (den1 * den2)
    return rho, 0.0


def _rank(vals, n):
    sorted_idx = sorted(range(n), key=lambda i: vals[i])
    ranks = [0.0] * n
    i = 0
    while i < n:
        j = i
        while j + 1 < n and vals[sorted_idx[j + 1]] == vals[sorted_idx[i]]:
            j += 1
        avg_rank = (i + j + 2) / 2.0  # ranks start at 1
        for k in range(i, j + 1):
            ranks[sorted_idx[k]] = avg_rank
        i = j + 1
    return ranks


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


# === block: score_0 (check id='lisi_correlation_check') ===
def score_0(artifact, step, ctx):
    if len(artifact) < 5:
        return 0.0
    D_Li = []
    channel = []
    for row in artifact:
        try:
            D_Li.append(float(row['D_Li']))
            channel.append(float(row['channel_area_fraction']))
        except (ValueError, KeyError):
            return 0.0
    if len(set(D_Li)) < 2 or len(set(channel)) < 2:
        return 0.0

    n = len(D_Li)
    def rank(vals):
        sorted_idx = sorted(range(n), key=lambda i: vals[i])
        ranks = [0.0] * n
        i = 0
        while i < n:
            j = i
            while j + 1 < n and vals[sorted_idx[j + 1]] == vals[sorted_idx[i]]:
                j += 1
            avg_rank = (i + j + 2) / 2.0  # ranks start at 1
            for k in range(i, j + 1):
                ranks[sorted_idx[k]] = avg_rank
            i = j + 1
        return ranks

    rank_D = rank(D_Li)
    rank_C = rank(channel)
    mean_D = sum(rank_D) / n
    mean_C = sum(rank_C) / n
    num = sum((rd - mean_D) * (rc - mean_C) for rd, rc in zip(rank_D, rank_C))
    den1 = math.sqrt(sum((rd - mean_D) ** 2 for rd in rank_D))
    den2 = math.sqrt(sum((rc - mean_C) ** 2 for rc in rank_C))
    if den1 == 0.0 or den2 == 0.0:
        return 0.0
    rho = num / (den1 * den2)
    if math.isnan(rho):
        return 0.0
    target = 0.7
    if rho >= target:
        return 1.0
    elif rho <= 0.0:
        return 0.0
    else:
        return rho / target


# === block: score_1 (check id='li2si_correlation_check') ===
def score_1(artifact, step, ctx):
    if len(artifact) < 5:
        return 0.0
    D_Li = []
    micro = []
    for row in artifact:
        try:
            D_Li.append(float(row['D_Li']))
            micro.append(float(row['total_microstructures']))
        except (ValueError, KeyError):
            return 0.0
    if len(set(D_Li)) < 2 or len(set(micro)) < 2:
        return 0.0
    rho, _ = spearmanr(D_Li, micro)
    if math.isnan(rho):
        return 0.0
    target = -0.7
    if rho <= target:
        return 1.0
    elif rho >= 0.0:
        return 0.0
    else:
        return (-rho) / (-target)


_SCORERS = {
    'lisi_correlation_check': score_0,
    'li2si_correlation_check': score_1,
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
