import os
import json
import csv

# === author imports / helpers ===
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
    ctx = {}
    for step in spec.get("steps", []):
        if "hidden_gold" in step:
            ctx[step["id"]] = step["hidden_gold"]
    return ctx


# === block: score_0 (check id='step01_phonon_freq') ===
def score_0(artifact, step, ctx):
    targets = ctx.get(step["id"], {}).get("phonon_targets", [])
    if not targets:
        return 1.0
    # collect frequencies per compound and qpoint
    freqs_map = defaultdict(list)
    for row in artifact:
        compound = row.get("compound", "")
        qp = row.get("qpoint_label", "")
        try:
            freq = float(row.get("frequency_THz", ""))
        except (ValueError, TypeError):
            freq = None
        if freq is not None:
            freqs_map[(compound, qp)].append(freq)

    matched = 0
    for t in targets:
        compound = t["compound"]
        qp = t["qpoint_label"]
        gold = t["gold"]
        tol = t.get("tol", 0.1)
        freqs = freqs_map.get((compound, qp), [])
        if any(abs(f - gold) <= tol for f in freqs):
            matched += 1
    match_score = matched / len(targets)

    # degeneracy check at Gamma for each compound
    compounds = ["KCl", "KBr", "KI"]
    deg_score = 0
    for comp in compounds:
        gamma_freqs = freqs_map.get((comp, "Gamma"), [])
        # acoustic modes near zero
        acoustic = sum(1 for f in gamma_freqs if abs(f) < 0.05)
        # expect at least two acoustics (actually three, but any 2 is ok)
        if acoustic >= 2:
            deg_score += 0.5
        # check for at least two TO modes (>0.1) within 0.1 of each other
        to_candidates = [f for f in gamma_freqs if f > 0.1]
        if len(to_candidates) >= 2:
            # check if any pair has diff <= 0.1
            has_doublet = False
            for i in range(len(to_candidates)):
                for j in range(i+1, len(to_candidates)):
                    if abs(to_candidates[i] - to_candidates[j]) <= 0.1:
                        has_doublet = True
                        break
                if has_doublet:
                    break
            if has_doublet:
                deg_score += 0.5
        else:
            # only one TO mode is a sign of missing degeneracy
            pass
    # normalise deg_score: max 1 per compound, 3 compounds
    max_deg = len(compounds)
    deg_norm = min(deg_score / max_deg, 1.0) if max_deg > 0 else 0

    w_target = 0.9
    w_degen = 0.1
    score = w_target * match_score + w_degen * deg_norm
    return min(max(score, 0.0), 1.0)


# === block: score_1 (check id='step02_debye') ===
def score_1(artifact, step, ctx):
    checkpoints = ctx.get(step["id"], {}).get("debye_checkpoints", [])
    if not checkpoints:
        return 1.0

    data = defaultdict(dict)
    for row in artifact:
        comp = row.get("compound", "")
        try:
            T = float(row.get("temperature_K", ""))
            theta = float(row.get("debye_temperature_K", ""))
        except (ValueError, TypeError):
            continue
        data[comp][T] = theta

    # monotonicity
    mono_score = 0.0
    n_comp = 0
    for comp, d in data.items():
        if not d:
            continue
        n_comp += 1
        # non-negative
        if any(theta < 0 for theta in d.values()):
            mono_factor = 0.0
        else:
            Ts = sorted(d.keys())
            epsilon = 0.1
            mono = all(d[t1] + epsilon >= d[t2] for t1, t2 in zip(Ts, Ts[1:]))
            mono_factor = 1.0 if mono else 0.0
        mono_score += mono_factor
    if n_comp > 0:
        mono_score /= n_comp

    # checkpoint comparison
    matched = 0
    total_cp = 0
    for cp in checkpoints:
        compound = cp["compound"]
        temps = cp["temperatures"]
        golds = cp["gold"]
        rel_tol = cp.get("rel_tol", 0.05)
        for T, gold in zip(temps, golds):
            total_cp += 1
            theta = data.get(compound, {}).get(T)
            if theta is not None and abs(theta - gold) <= rel_tol * abs(gold) + 1e-6:
                matched += 1
    cp_score = matched / total_cp if total_cp > 0 else 0

    w_cp = 0.7
    w_mono = 0.3
    score = w_cp * cp_score + w_mono * mono_score
    return min(max(score, 0.0), 1.0)


_SCORERS = {
    'step01_phonon_freq': score_0,
    'step02_debye': score_1,
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
