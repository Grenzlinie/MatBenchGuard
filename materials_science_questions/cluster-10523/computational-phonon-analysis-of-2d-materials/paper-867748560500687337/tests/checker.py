import os
import json
import csv

# === author imports / helpers ===
try:
    import numpy
except ImportError:
    import subprocess, sys
    subprocess.run([sys.executable, '-m', 'pip', 'install', '-q', '--no-cache-dir', '-i', 'https://pypi.tuna.tsinghua.edu.cn/simple', 'numpy'], check=True)
    import numpy
import numpy as np
import json
import os
import csv
from collections import defaultdict


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
        steps = spec.get('steps', [])
        ctx = {}
        for step in steps:
            sid = step['id']
            if sid == 'step_1':
                ctx['step_1_gold'] = step.get('gold', {})
            elif sid == 'step_2':
                ctx['step_2_gap_ranges'] = step.get('gold_bandgap_ranges', {})
        return ctx


# === block: score_0 (check id='step_1') ===
def score_0(artifact, step, ctx):
        gold = ctx.get('step_1_gold', {})
        if not gold:
            return 0.0
        dirac = artifact.get('dirac_frequencies_0deg')
        s_mode = artifact.get('bandgap_S_mode')
        a_mode = artifact.get('bandgap_A_mode')
        if (not isinstance(dirac, list) or len(dirac) != 2 or 
            not isinstance(s_mode, list) or len(s_mode) != 2 or 
            not isinstance(a_mode, list) or len(a_mode) != 2):
            return 0.0
        values = [dirac[0], dirac[1], s_mode[0], s_mode[1], a_mode[0], a_mode[1]]
        gold_vals = [
            gold['dirac_s_ghz'], gold['dirac_a_ghz'],
            gold['bandgap_s_lower'], gold['bandgap_s_upper'],
            gold['bandgap_a_lower'], gold['bandgap_a_upper']
        ]
        tol_rel = gold.get('tolerance_rel', 0.05)
        tol_abs = gold.get('tolerance_abs_ghz', 0.05)
        scores = []
        for v, gv in zip(values, gold_vals):
            tol = max(tol_abs, tol_rel * abs(gv))
            error = abs(v - gv)
            if error <= tol:
                s = 1.0
            else:
                s = max(0.0, 2.0 - error / tol)
            scores.append(s)
        return sum(scores) / len(scores)


# === block: score_1 (check id='step_2') ===
def score_1(artifact, step, ctx):
        ranges = ctx.get('step_2_gap_ranges', {})
        if not ranges:
            return 0.0
        # artifact is a list of csv.DictReader rows
        if not isinstance(artifact, list) or not artifact:
            return 0.0
        data = []
        for row in artifact:
            try:
                kx = float(row['kx'])
                f = float(row['frequency'])
                idx = int(row['mode_index'])
                itype = row.get('interface_type', None)
                data.append((kx, f, idx, itype))
            except (ValueError, KeyError):
                continue
        if not data:
            return 0.0
        kx_arr = np.array([d[0] for d in data])
        f_arr = np.array([d[1] for d in data])
        idx_arr = np.array([d[2] for d in data])
        itype_arr = [d[3] for d in data]

        def _opposite_sign_branches(kx_sub, f_sub, idx_sub, itype_sub):
            """Return 1.0 if at least two branches with opposite group‑velocity
            signs are found, else 0.0."""
            # If interface_type is consistently provided, use it directly
            if all(t is not None for t in itype_sub):
                groups = defaultdict(list)
                for k, f, it in zip(kx_sub, f_sub, itype_sub):
                    groups[it].append((k, f))
                branches = []
                for pts in groups.values():
                    if len(pts) >= 5:
                        branches.append(sorted(pts, key=lambda x: x[0]))
            else:
                # Fallback: reconstruct branches by frequency‑continuity
                # sort by kx, then build connected components with tolerance
                points = sorted(zip(kx_sub, f_sub, idx_sub), key=lambda x: x[0])
                # adjacency threshold in GHz (narrow enough to not join distinct branches)
                tol = 0.02
                n = len(points)
                adj = defaultdict(list)
                for i in range(n):
                    ki, fi = points[i][:2]
                    for j in range(i + 1, n):
                        kj, fj = points[j][:2]
                        if kj - ki > 0.05:   # only consider kx-close points
                            break
                        if abs(ki - kj) < 1e-9 or abs(fi - fj) <= tol:
                            adj[i].append(j)
                            adj[j].append(i)
                visited = set()
                comps = []
                for i in range(n):
                    if i not in visited:
                        comp = []
                        stack = [i]
                        while stack:
                            node = stack.pop()
                            if node in visited:
                                continue
                            visited.add(node)
                            comp.append(points[node])
                            stack.extend(adj[node])
                        if len(comp) >= 5:
                            comps.append(comp)
                branches = [sorted(comp, key=lambda x: x[0]) for comp in comps]

            signs = []
            for branch in branches:
                ks = np.array([p[0] for p in branch])
                fs = np.array([p[1] for p in branch])
                dk = np.diff(ks)
                df = np.diff(fs)
                slopes = df / dk
                med = np.median(slopes)
                if not np.isnan(med):
                    signs.append(np.sign(med))
            return 1.0 if (len(signs) >= 2 and (1 in signs) and (-1 in signs)) else 0.0

        def check_bandgap(lower, upper):
            mask = (f_arr >= lower) & (f_arr <= upper)
            if np.sum(mask) < 10:
                return 0.0
            return _opposite_sign_branches(
                kx_arr[mask], f_arr[mask], idx_arr[mask],
                [itype_arr[i] for i, m in enumerate(mask) if m]
            )

        s_score = check_bandgap(ranges['s_mode'][0], ranges['s_mode'][1])
        a_score = check_bandgap(ranges['a_mode'][0], ranges['a_mode'][1])
        return 0.5 * s_score + 0.5 * a_score


_SCORERS = {
    'step_1': score_0,
    'step_2': score_1,
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
