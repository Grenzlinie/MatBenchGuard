import os
import json
import csv

# === author imports / helpers ===
import csv
import os
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
    return {}


# === block: score_0 (check id='compile_charges') ===
def score_0(artifact, step, ctx):
    def score(artifact_rows, step, ctx):
        if not artifact_rows:
            return 0.0
        try:
            rows = list(artifact_rows)
        except Exception:
            return 0.0

        params = step.get('params', {})
        high_thresh = float(params.get('high_spin_discontinuity_threshold', 0.1))
        low_thresh = float(params.get('low_spin_smooth_threshold', 0.05))
        atoms = params.get('atoms', ['O1','O2','Fe','Cstar'])
        alphas = params.get('alpha_values', [110,120])

        def to_float(val):
            if val is None:
                return None
            if isinstance(val, (int, float)):
                return float(val)
            try:
                return float(val)
            except (ValueError, TypeError):
                return None

        try:
            data = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
            for row in rows:
                if not isinstance(row, dict):
                    continue
                spin = row.get('spin_state')
                if spin is None or (isinstance(spin, str) and spin.strip() == ''):
                    continue
                alpha_val = to_float(row.get('alpha'))
                beta_val = to_float(row.get('beta'))
                atom = row.get('atom_label')
                if atom is None or (isinstance(atom, str) and atom.strip() == ''):
                    continue
                charge_val = to_float(row.get('mulliken_charge'))
                if alpha_val is None or beta_val is None or charge_val is None:
                    continue
                data[spin][alpha_val][atom].append((beta_val, charge_val))

            for spin in data:
                for alpha in data[spin]:
                    for atom in data[spin][alpha]:
                        data[spin][alpha][atom].sort(key=lambda x: x[0])

            max_diffs = {}
            for spin in data:
                for alpha in data[spin]:
                    for atom in data[spin][alpha]:
                        pts = data[spin][alpha][atom]
                        if len(pts) < 2:
                            max_diffs[(spin, alpha, atom)] = 0.0
                            continue
                        mx = 0.0
                        for i in range(1, len(pts)):
                            diff = abs(pts[i][1] - pts[i-1][1])
                            if diff > mx:
                                mx = diff
                        max_diffs[(spin, alpha, atom)] = mx

            hs_present = False
            hs_max_alpha = {}
            for alpha in alphas:
                max_atom = max((max_diffs.get(('high', alpha, atom), 0.0) for atom in atoms), default=0.0)
                hs_max_alpha[alpha] = max_atom
                if max_atom > high_thresh:
                    hs_present = True

            ls_smooth = True
            for alpha in alphas:
                for atom in atoms:
                    if max_diffs.get(('low', alpha, atom), 0.0) > low_thresh:
                        ls_smooth = False
                        break

            mod_ok = False
            if alphas[0] in hs_max_alpha and alphas[1] in hs_max_alpha:
                if hs_max_alpha[alphas[0]] > hs_max_alpha[alphas[1]]:
                    mod_ok = True

            total = (0.5 if hs_present else 0.0) + (0.3 if ls_smooth else 0.0) + (0.2 if mod_ok else 0.0)
            return min(total, 1.0)
        except Exception:
            return 0.0


_SCORERS = {
    'compile_charges': score_0,
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
