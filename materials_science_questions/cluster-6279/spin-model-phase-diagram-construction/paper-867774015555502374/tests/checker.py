import os
import json
import csv

# === author imports / helpers ===
import csv
import re


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


# === block: score_0 (check id='eta_scoring') ===
def score_0(artifact, step, ctx):
    # Read CSV rows: list of dicts with D_over_abs_J (as string maybe), temperature, eta, eta_error
    rows = artifact
    if not rows:
        return 0.0
    # Build lookup: dict of (D_over_abs_J, temperature) -> eta
    eta_dict = {}
    temps = set()
    for r in rows:
        try:
            d = float(r['D_over_abs_J'])
            t = float(r['temperature'])
            eta_val = float(r['eta'])
            eta_dict[(d, t)] = eta_val
            temps.add(t)
        except (KeyError, ValueError):
            continue

    # For scoring, consider D=0 and D=-1
    score = 0.0
    # D=0: at low T (t <= 0.1), average eta should be near 0.317
    # also no zero eta across all T for D=0
    low_temps_d0 = [t for t in temps if t <= 0.1]
    if low_temps_d0:
        vals = []
        for t in low_temps_d0:
            if (0, t) in eta_dict:
                vals.append(eta_dict[(0, t)])
        if vals:
            avg_eta_d0 = sum(vals) / len(vals)
            # target 0.317, tolerance 0.05
            if abs(avg_eta_d0 - 0.317) <= 0.05:
                score += 0.25
            else:
                # partial score based on distance
                dist = abs(avg_eta_d0 - 0.317)
                # if beyond 0.1, zero
                if dist <= 0.1:
                    score += 0.25 * (1 - (dist - 0.05) / 0.05)
        else:
            # no D=0 low-T data, penalize
            pass
    else:
        # no low T data, assume fail
        pass

    # D=0 overall non-zero (any eta <= 0.01 is a red flag)
    all_d0 = [eta_dict[(0, t)] for t in temps if (0, t) in eta_dict]
    if all_d0:
        zero_count = sum(1 for e in all_d0 if e <= 0.01)
        if zero_count == 0:
            score += 0.15
        else:
            score += 0.15 * (1 - min(1, zero_count / len(all_d0)))
    else:
        pass

    # D=-1: at low T (t <= 0.35) all eta should be <= 0.05
    low_temps_dneg1 = [t for t in temps if t <= 0.35]
    if low_temps_dneg1:
        vals = []
        for t in low_temps_dneg1:
            if (-1, t) in eta_dict:
                vals.append(eta_dict[(-1, t)])
        if vals:
            violations = [v for v in vals if v > 0.05]
            if not violations:
                score += 0.35
            else:
                # penalize by fraction of violations
                frac = len(violations) / len(vals)
                score += 0.35 * (1 - frac)
        else:
            pass

    # D=-1 at higher T (t > 0.8) some eta > 0.05
    high_temps_dneg1 = [t for t in temps if t > 0.8]
    if high_temps_dneg1:
        vals_high = [eta_dict[(-1, t)] for t in high_temps_dneg1 if (-1, t) in eta_dict]
        if vals_high:
            if any(v > 0.05 for v in vals_high):
                score += 0.15
            else:
                # no high-T eta > 0.05, likely wrong
                pass
        else:
            pass

    # Additional check that temperature range is reasonable: at least 20 distinct temps
    if len(temps) >= 20:
        score += 0.1

    return min(1.0, score)


# === block: score_1 (check id='pattern_densities_scoring') ===
def score_1(artifact, step, ctx):
    # CSV rows with D_over_abs_J, temperature, pattern_id, density
    rows = artifact
    if not rows:
        return 0.0
    # Build dict: (D_over_abs_J, pattern_id) -> density
    pattern_dens = {}
    for r in rows:
        try:
            d = int(float(r['D_over_abs_J']))
            pid = r['pattern_id'].strip()
            dens = float(r['density'])
            pattern_dens[(d, pid)] = dens
        except (KeyError, ValueError):
            continue

    # Required pattern sets
    D1_set = {'p3', '-p3', 'p7', '-p7', 'p9', '-p9'}
    Dneg1_set1 = {'p6', '-p8', '-p12'}
    Dneg1_set2 = {'-p6', 'p8', 'p12'}
    D0_mix_set1 = D1_set
    D0_mix_set2 = Dneg1_set1 | Dneg1_set2  # 6 patterns

    # All known pattern IDs from paper (up to sign)
    all_ids = ['p1'] + [f'{s}p{i}' for i in range(2,15) for s in ('','-')]

    score = 0.0

    # D=1 check
    D1_ok = True
    D1_total = 0.0
    for pid in all_ids:
        dens = pattern_dens.get((1, pid), 0.0)
        if pid in D1_set:
            D1_total += dens
            if dens <= 0:
                D1_ok = False
        else:
            if dens > 1e-6:
                D1_ok = False
    if D1_ok and abs(D1_total - 1.0) < 0.01:
        score += 0.33

    # D=-1 check: exactly one of the two sets has non-zero densities
    Dneg1_ok = False
    set1_present = all(pattern_dens.get((-1, pid), 0.0) > 1e-6 for pid in Dneg1_set1)
    set2_present = all(pattern_dens.get((-1, pid), 0.0) > 1e-6 for pid in Dneg1_set2)
    other_zero = all(pattern_dens.get((-1, pid), 0.0) <= 1e-6 for pid in all_ids if pid not in Dneg1_set1 and pid not in Dneg1_set2)
    if set1_present and other_zero and not set2_present:
        Dneg1_ok = True
    elif set2_present and other_zero and not set1_present:
        Dneg1_ok = True
    if Dneg1_ok:
        # also check total density ≈ 1
        total = sum(pattern_dens.get((-1, pid), 0.0) for pid in all_ids)
        if abs(total - 1.0) < 0.01:
            score += 0.33

    # D=0 check: all patterns in D0_mix_set1 and D0_mix_set2 must have non-zero density
    D0_ok = True
    D0_total = 0.0
    target_patterns = D0_mix_set1 | D0_mix_set2
    for pid in target_patterns:
        dens = pattern_dens.get((0, pid), 0.0)
        if dens <= 1e-6:
            D0_ok = False
        D0_total += dens
    if D0_ok and abs(D0_total - 1.0) < 0.05:
        # ratio check: sum(D0_mix_set1) / sum(D0_mix_set2) ≈ 2.7 ± 15% = 2.295 - 3.105
        sum1 = sum(pattern_dens.get((0, pid), 0.0) for pid in D0_mix_set1)
        sum2 = sum(pattern_dens.get((0, pid), 0.0) for pid in D0_mix_set2)
        if sum2 > 0:
            ratio = sum1 / sum2
            if 2.295 <= ratio <= 3.105:
                score += 0.34
            else:
                # partial credit if ratio within wider range
                if 2.0 <= ratio <= 3.5:
                    score += 0.1
        else:
            pass

    return min(1.0, score)


# === block: score_2 (check id='ground_state_regimes_scoring') ===
def score_2(artifact, step, ctx):
    text = artifact
    if not isinstance(text, str):
        return 0.0
    required_phrases = [
        r'D/\|J\|\s*>\s*0',
        r'spin-?1/?2.*frustrated',
        r'no long-range order',
        r'-1\.5\s*<\s*D/\|J\|\s*<\s*0',
        r'partially ordered',
        r'D/\|J\|\s*<\s*-1\.5',
        r'non-magnetic',
        r'all-zero',
        r'D/\|J\|\s*=\s*0',
        r'degenerate manifold'
    ]
    count = 0
    for phrase in required_phrases:
        if re.search(phrase, text, re.IGNORECASE):
            count += 1
    score = count / len(required_phrases)
    return score


_SCORERS = {
    'eta_scoring': score_0,
    'pattern_densities_scoring': score_1,
    'ground_state_regimes_scoring': score_2,
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
