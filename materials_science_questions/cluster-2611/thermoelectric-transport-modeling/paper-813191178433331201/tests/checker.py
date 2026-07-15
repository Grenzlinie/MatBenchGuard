import os
import json
import csv

# === author imports / helpers ===
import json
import os

def get_strain_float(s):
    return float(s)

def is_monotonic_increasing(seq, eps=1e-9):
    for i in range(1, len(seq)):
        if seq[i] + eps < seq[i-1]:
            return False
    return True

def is_monotonic_decreasing(seq, eps=1e-9):
    for i in range(1, len(seq)):
        if seq[i] - eps > seq[i-1]:
            return False
    return True


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
    artifact = load_artifact(os.path.join(outputs_dir, "transport_properties.json"))
    if artifact is None:
        return {"valid": False, "data": None}

    required_strains = {"-2.0","-1.5","-1.0","-0.5","0.0","0.5","1.0","1.5","2.0"}
    required_temps = {"300","900"}
    required_dtypes = {"electron","hole"}
    required_dlevels = {"1e18","1.2e20"}

    def check_keys(obj):
        for strain in required_strains:
            sd = obj.get(strain)
            if not isinstance(sd, dict): return False
            for temp in required_temps:
                td = sd.get(temp)
                if not isinstance(td, dict): return False
                for dt in required_dtypes:
                    dd = td.get(dt)
                    if not isinstance(dd, dict): return False
                    for dl in required_dlevels:
                        entry = dd.get(dl)
                        if not isinstance(entry, dict): return False
                        for key in ["sigma_xx","sigma_zz","sigma_total","S_xx","S_zz","S_total","PF_xx","PF_zz","PF_total"]:
                            if key not in entry:
                                return False
        return True

    if not check_keys(artifact):
        return {"valid": False, "data": None}
    return {"valid": True, "data": artifact}


# === block: score_0 (check id='sigma_ratio_and_trend') ===
def score_0(artifact, step, ctx):
    if not ctx.get("valid"):
        return 0.0
    data = ctx["data"]

    strains = sorted([s for s in data.keys()], key=lambda x: float(x))
    temps = ["300","900"]
    dtypes = ["electron","hole"]
    dlevels = ["1e18","1.2e20"]

    # Monotonicity: sigma_total should increase with |strain|
    def check_mono(ax):
        idx0 = strains.index("0.0")
        neg_side = [ax[i] for i in range(0, idx0+1)]  # -2 ... 0
        pos_side = [ax[i] for i in range(idx0, len(strains))]  # 0 ... +2
        neg_ok = is_monotonic_decreasing(neg_side)
        pos_ok = is_monotonic_increasing(pos_side)
        return neg_ok and pos_ok

    mono_count = 0
    total_conds = 0
    for t in temps:
        for dt in dtypes:
            for dl in dlevels:
                ax = []
                try:
                    for s in strains:
                        val = data[s][t][dt][dl]["sigma_total"]
                        ax.append(val)
                except:
                    continue
                if check_mono(ax):
                    mono_count += 1
                total_conds += 1
    mono_score = mono_count / total_conds if total_conds > 0 else 0.0

    # Extreme ratio checks from paper-expected ratios (generous bounds)
    ratio_score = 0.0
    ratio_checks_total = 0
    ratio_checks_passed = 0

    # expected_ratios is a dict from step config, keys are stringified tuples like ("'300','electron','1e18','xx','2.0'")
    # We'll parse them back
    expected_raw = step.get("expected_ratios", {})
    if expected_raw:
        for key_str, bounds in expected_raw.items():
            try:
                # key_str like "('300','electron','1e18','xx','2.0')"
                temp, dtype, dlevel, comp, strain = eval(key_str)
            except:
                continue
            try:
                unstrained = data["0.0"][temp][dtype][dlevel]
                strained = data[strain][temp][dtype][dlevel]
                base = unstrained["sigma_xx"] if comp == "xx" else unstrained["sigma_zz"]
                val = strained["sigma_xx"] if comp == "xx" else strained["sigma_zz"]
                if base == 0:
                    continue
                ratio = val / base
                low, high = bounds
                ratio_checks_total += 1
                if low <= ratio <= high:
                    ratio_checks_passed += 1
            except:
                pass
        if ratio_checks_total > 0:
            ratio_score = ratio_checks_passed / ratio_checks_total

    # combine 80% monotonicity, 20% ratio
    score = 0.8 * mono_score + 0.2 * ratio_score
    return min(max(score, 0.0), 1.0)


# === block: score_1 (check id='seebeck_trend') ===
def score_1(artifact, step, ctx):
    if not ctx.get("valid"):
        return 0.0
    data = ctx["data"]

    strains = sorted([s for s in data.keys()], key=lambda x: float(x))
    temps = ["300","900"]
    dtypes = ["electron","hole"]
    dlevels = ["1e18","1.2e20"]

    def check_seebeck_mono(ax):
        # |S_total| should be maximal at 0 and decrease with |strain|
        idx0 = strains.index("0.0")
        neg_side = [ax[i] for i in range(0, idx0+1)]  # -2 ... 0
        pos_side = [ax[i] for i in range(idx0, len(strains))]  # 0 ... +2
        neg_ok = is_monotonic_increasing(neg_side)   # |S| increases towards zero
        pos_ok = is_monotonic_decreasing(pos_side)   # |S| decreases away from zero
        return neg_ok and pos_ok

    mono_count = 0
    total_conds = 0
    for t in temps:
        for dt in dtypes:
            for dl in dlevels:
                ax = []
                try:
                    for s in strains:
                        val = abs(data[s][t][dt][dl]["S_total"])
                        ax.append(val)
                except:
                    continue
                if check_seebeck_mono(ax):
                    mono_count += 1
                total_conds += 1

    return mono_count / total_conds if total_conds > 0 else 0.0


# === block: score_2 (check id='pf_trend') ===
def score_2(artifact, step, ctx):
    if not ctx.get("valid"):
        return 0.0
    data = ctx["data"]

    strains = sorted([s for s in data.keys()], key=lambda x: float(x))
    temps = ["300","900"]
    dtypes = ["electron","hole"]
    dlevels = ["1e18","1.2e20"]

    def check_pf_mono(ax):
        # PF_total should be maximal at 0 and decrease with |strain|
        idx0 = strains.index("0.0")
        neg_side = [ax[i] for i in range(0, idx0+1)]
        pos_side = [ax[i] for i in range(idx0, len(strains))]
        neg_ok = is_monotonic_increasing(neg_side)
        pos_ok = is_monotonic_decreasing(pos_side)
        return neg_ok and pos_ok

    mono_count = 0
    total_conds = 0
    for t in temps:
        for dt in dtypes:
            for dl in dlevels:
                ax = []
                try:
                    for s in strains:
                        val = data[s][t][dt][dl]["PF_total"]
                        ax.append(val)
                except:
                    continue
                if check_pf_mono(ax):
                    mono_count += 1
                total_conds += 1

    return mono_count / total_conds if total_conds > 0 else 0.0


_SCORERS = {
    'sigma_ratio_and_trend': score_0,
    'seebeck_trend': score_1,
    'pf_trend': score_2,
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
