import os
import json
import csv

# === author imports / helpers ===
import csv
import math
import os


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
        ctx = {}
        return ctx


# === block: score_0 (check id='cu_isotherm') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        # artifact is list of dicts from CSV
        if not artifact:
            return 0.0
        try:
            rows = []
            for r in artifact:
                mu = float(r.get('chemical_potential', 0.0))
                n = int(float(r.get('num_atoms', 0)))
                be = float(r.get('avg_binding_energy', 0.0))
                rows.append((mu, n, be))
            rows.sort(key=lambda x: x[0])
            mus = [r[0] for r in rows]
            ns = [r[1] for r in rows]
            bes = [r[2] for r in rows]
        except Exception:
            return 0.0

        # monotonic check
        for i in range(1, len(ns)):
            if ns[i] < ns[i-1]:
                return 0.0

        gold_mus = step.get('gold_step_mu_list', [])
        gold_bes = step.get('gold_plateau_binding_energy_list', [])
        mu_tol = step.get('mu_tolerance', 0.05)
        be_tol = step.get('binding_tolerance', 0.02)
        min_step = 3  # atoms to qualify as a step

        # detect steps: find mu where N jumps
        steps = []  # list of (mu, avg_be_after step)
        i = 0
        while i < len(ns) - 1:
            if ns[i+1] - ns[i] >= min_step:
                step_mu = mus[i+1]
                # collect subsequent points until next step
                j = i + 1
                while j < len(ns) - 1 and ns[j+1] - ns[j] < min_step:
                    j += 1
                plateau_be = sum(bes[i+1:j+1]) / (j - i) if j > i else bes[i+1]
                steps.append((step_mu, plateau_be))
                i = j
            else:
                i += 1

        if not gold_mus:
            return 1.0

        matched_steps = 0
        matched_binding = 0
        used = [False]*len(steps)
        for g_mu, g_be in zip(gold_mus, gold_bes if gold_bes else [None]*len(gold_mus)):
            found = False
            for idx, (s_mu, s_be) in enumerate(steps):
                if used[idx]:
                    continue
                if abs(s_mu - g_mu) <= mu_tol:
                    used[idx] = True
                    found = True
                    if g_be is not None and abs(s_be - g_be) <= be_tol:
                        matched_binding += 1
                    break
            if found:
                matched_steps += 1

        step_score = matched_steps / len(gold_mus) if gold_mus else 1.0
        binding_score = matched_binding / len(gold_mus) if gold_mus else 1.0
        if step_score == 0.0:
            # no expected step found; give partial credit for non-decreasing and reasonable shape
            if ns[-1] > 0 and all(ns[i] <= ns[i+1] for i in range(len(ns)-1)):
                return 0.3
            return 0.0
        return 0.6 * step_score + 0.4 * binding_score


# === block: score_1 (check id='ag_isotherm') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        # artifact is list of dicts from CSV
        if not artifact:
            return 0.0
        try:
            rows = []
            for r in artifact:
                mu = float(r.get('chemical_potential', 0.0))
                n = int(float(r.get('num_atoms', 0)))
                be = float(r.get('avg_binding_energy', 0.0))
                rows.append((mu, n, be))
            rows.sort(key=lambda x: x[0])
            mus = [r[0] for r in rows]
            ns = [r[1] for r in rows]
            bes = [r[2] for r in rows]
        except Exception:
            return 0.0

        # monotonic check
        for i in range(1, len(ns)):
            if ns[i] < ns[i-1]:
                return 0.0

        gold_mus = step.get('gold_step_mu_list', [])
        gold_bes = step.get('gold_plateau_binding_energy_list', [])
        mu_tol = step.get('mu_tolerance', 0.05)
        be_tol = step.get('binding_tolerance', 0.02)
        min_step = 3

        steps = []
        i = 0
        while i < len(ns) - 1:
            if ns[i+1] - ns[i] >= min_step:
                step_mu = mus[i+1]
                j = i + 1
                while j < len(ns) - 1 and ns[j+1] - ns[j] < min_step:
                    j += 1
                plateau_be = sum(bes[i+1:j+1]) / (j - i) if j > i else bes[i+1]
                steps.append((step_mu, plateau_be))
                i = j
            else:
                i += 1

        if not gold_mus:
            return 1.0

        matched_steps = 0
        matched_binding = 0
        used = [False]*len(steps)
        for g_mu, g_be in zip(gold_mus, gold_bes if gold_bes else [None]*len(gold_mus)):
            found = False
            for idx, (s_mu, s_be) in enumerate(steps):
                if used[idx]:
                    continue
                if abs(s_mu - g_mu) <= mu_tol:
                    used[idx] = True
                    found = True
                    if g_be is not None and abs(s_be - g_be) <= be_tol:
                        matched_binding += 1
                    break
            if found:
                matched_steps += 1

        step_score = matched_steps / len(gold_mus) if gold_mus else 1.0
        binding_score = matched_binding / len(gold_mus) if gold_mus else 1.0
        if step_score == 0.0:
            if ns[-1] > 0 and all(ns[i] <= ns[i+1] for i in range(len(ns)-1)):
                return 0.3
            return 0.0
        return 0.6 * step_score + 0.4 * binding_score


_SCORERS = {
    'cu_isotherm': score_0,
    'ag_isotherm': score_1,
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
