import os
import json
import csv

# === author imports / helpers ===
import re
import math

def rankdata(a):
    """Assign ranks with average for ties."""
    n = len(a)
    if n == 0:
        return []
    idx = list(range(n))
    idx.sort(key=lambda i: a[i])
    ranks = [0.0] * n
    i = 0
    while i < n:
        j = i
        while j < n and a[idx[j]] == a[idx[i]]:
            j += 1
        avg_rank = (i + j - 1) / 2.0 + 1
        for k in range(i, j):
            ranks[idx[k]] = avg_rank
        i = j
    return ranks

def spearman_rank_correlation(x, y):
    """Compute Spearman's rho between two sequences."""
    n = len(x)
    if n < 2:
        return 0.0
    rank_x = rankdata(x)
    rank_y = rankdata(y)
    d2 = sum((rx - ry) ** 2 for rx, ry in zip(rank_x, rank_y))
    rho = 1.0 - (6.0 * d2) / (n * (n**2 - 1))
    return rho


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


# === block: score_0 (check id='step-1') ===
def score_0(artifact, step, ctx):
        try:
            lines = artifact.strip().splitlines()
            frames = []
            i = 0
            while i < len(lines):
                if not lines[i].strip():
                    i += 1
                    continue
                try:
                    N = int(lines[i].strip())
                except ValueError:
                    i += 1
                    continue
                if i+1 >= len(lines):
                    break
                comment = lines[i+1].strip()
                m = re.search(r'energy\s*=\s*([-+]?[\d.]+(?:[eE][-+]?\d+)?)', comment)
                if not m:
                    i += 2 + N
                    continue
                energy = float(m.group(1))
                coords = []
                for j in range(N):
                    if i+2+j >= len(lines):
                        break
                    parts = lines[i+2+j].strip().split()
                    if len(parts) >= 4 and parts[0] == 'Au':
                        try:
                            x, y, z = float(parts[1]), float(parts[2]), float(parts[3])
                            coords.append((x, y, z))
                        except ValueError:
                            pass
                if len(coords) != N:
                    i += 2 + N
                    continue
                frames.append((N, energy, coords))
                i += 2 + N
            frames.sort(key=lambda f: f[0])
            if len(frames) < 41:
                return 0.0
            E = {}
            coords_dict = {}
            for n, en, crd in frames:
                if 2 <= n <= 44:
                    E[n] = en
                    coords_dict[n] = crd
            for n in range(2, 45):
                if n not in E:
                    return 0.0
            def compute_radius(n):
                crd = coords_dict[n]
                atoms = n
                cx = sum(c[0] for c in crd) / atoms
                cy = sum(c[1] for c in crd) / atoms
                cz = sum(c[2] for c in crd) / atoms
                max_dist = 0.0
                for (x, y, z) in crd:
                    d = math.sqrt((x - cx) ** 2 + (y - cy) ** 2 + (z - cz) ** 2)
                    if d > max_dist:
                        max_dist = d
                return max_dist
            radii = {n: compute_radius(n) for n in range(2, 45)}
            def delta2E(n):
                return E[n+1] + E[n-1] - 2 * E[n]
            d2E = {n: delta2E(n) for n in range(3, 44)}
            peaks = []
            # check edge n=3
            if d2E[3] > d2E[4]:
                peaks.append(3)
            for n in range(4, 43):
                if d2E[n] > d2E[n-1] and d2E[n] > d2E[n+1]:
                    peaks.append(n)
            # check edge n=43
            if d2E[43] > d2E[42]:
                peaks.append(43)
            def sigma(n):
                if radii[n] == 0:
                    return 0.0
                return n / (radii[n] ** 3)
            sigmas = {n: sigma(n) for n in range(2, 45)}
            def delta2sigma(n):
                return sigmas[n+1] + sigmas[n-1] - 2 * sigmas[n]
            d2sigma = {n: delta2sigma(n) for n in range(3, 44)}
            minima = []
            # check edge n=3
            if d2sigma[3] < d2sigma[4]:
                minima.append(3)
            for n in range(4, 43):
                if d2sigma[n] < d2sigma[n-1] and d2sigma[n] < d2sigma[n+1]:
                    minima.append(n)
            # check edge n=43
            if d2sigma[43] < d2sigma[42]:
                minima.append(43)
            gold_magic = step.get('magic_numbers', [7,13,19,23,26,29,34,37,40,43])
            gold_close = step.get('close_packed_sizes', [4,6,13,23,26,29,34])
            tol = step.get('tolerance', 1)
            def match_list(candidates, gold_list, tol):
                matched = 0
                for g in gold_list:
                    for c in candidates:
                        if abs(c - g) <= tol:
                            matched += 1
                            break
                return matched
            magic_matched = match_list(peaks, gold_magic, tol)
            close_matched = match_list(minima, gold_close, tol)
            magic_score = magic_matched / len(gold_magic) if gold_magic else 0.0
            close_score = close_matched / len(gold_close) if gold_close else 0.0
            ns = list(range(2, 45))
            rs = [radii[n] for n in ns]
            try:
                rho = spearman_rank_correlation(ns, rs)
            except Exception:
                rho = 0.0
            trend_score = 1.0 if rho > 0.9 else max(0.0, rho - 0.5)
            total = 0.4 * magic_score + 0.4 * close_score + 0.2 * trend_score
            return min(1.0, max(0.0, total))
        except Exception:
            return 0.0


_SCORERS = {
    'step-1': score_0,
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
