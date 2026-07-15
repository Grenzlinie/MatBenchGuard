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
    import json
    def prepare(outputs_dir, spec):
        return {}


# === block: score_0 (check id='cond_n_Bi2Te2.7Se0.3_500K') ===
def score_0(artifact, step, ctx):
    cond_key = step["condition_key"]
    if cond_key not in artifact:
        return 0.0
    data = artifact[cond_key]
    T = data["temperature_K"]
    k_lat = data["kappa_lat_W_mK"]
    sigma_bulk = data["sigma_bulk_S_m"]
    S_bulk = data["S_bulk_microV_K"]
    k_elec_bulk = data["kappa_elec_bulk_W_mK"]
    sigma_bar = data["sigma_barrier_S_m"]
    S_bar = data["S_barrier_microV_K"]
    k_elec_bar = data["kappa_elec_barrier_W_mK"]
    def zT(sigma, S_uV, k_elec):
        S_V = [s*1e-6 for s in S_uV]
        return [(s**2 * sig * T) / (ke + k_lat) for s, sig, ke in zip(S_V, sigma, k_elec)]
    zT_bulk = zT(sigma_bulk, S_bulk, k_elec_bulk)
    zT_bar = zT(sigma_bar, S_bar, k_elec_bar)
    max_bulk = max(zT_bulk)
    max_bar = max(zT_bar)
    gold_bulk = step["gold_bulk"]
    gold_bar = step["gold_barrier"]
    score_bulk = min(1.0, max(0.0, max_bulk / gold_bulk)) if gold_bulk > 0 else 0.0
    score_bar = min(1.0, max(0.0, max_bar / gold_bar)) if gold_bar > 0 else 0.0
    order_score = 1.0 if max_bar > max_bulk else 0.0
    return (score_bulk + score_bar + order_score) / 3.0


# === block: score_1 (check id='cond_p_Bi0.5Sb1.5Te3_500K') ===
def score_1(artifact, step, ctx):
    cond_key = step["condition_key"]
    if cond_key not in artifact:
        return 0.0
    data = artifact[cond_key]
    T = data["temperature_K"]
    k_lat = data["kappa_lat_W_mK"]
    sigma_bulk = data["sigma_bulk_S_m"]
    S_bulk = data["S_bulk_microV_K"]
    k_elec_bulk = data["kappa_elec_bulk_W_mK"]
    sigma_bar = data["sigma_barrier_S_m"]
    S_bar = data["S_barrier_microV_K"]
    k_elec_bar = data["kappa_elec_barrier_W_mK"]
    def zT(sigma, S_uV, k_elec):
        S_V = [s*1e-6 for s in S_uV]
        return [(s**2 * sig * T) / (ke + k_lat) for s, sig, ke in zip(S_V, sigma, k_elec)]
    zT_bulk = zT(sigma_bulk, S_bulk, k_elec_bulk)
    zT_bar = zT(sigma_bar, S_bar, k_elec_bar)
    max_bulk = max(zT_bulk)
    max_bar = max(zT_bar)
    gold_bulk = step["gold_bulk"]
    gold_bar = step["gold_barrier"]
    score_bulk = min(1.0, max(0.0, max_bulk / gold_bulk)) if gold_bulk > 0 else 0.0
    score_bar = min(1.0, max(0.0, max_bar / gold_bar)) if gold_bar > 0 else 0.0
    order_score = 1.0 if max_bar > max_bulk else 0.0
    return (score_bulk + score_bar + order_score) / 3.0


# === block: score_2 (check id='cond_n_Mg2Si0.4Sn0.6_900K') ===
def score_2(artifact, step, ctx):
    cond_key = step["condition_key"]
    if cond_key not in artifact:
        return 0.0
    data = artifact[cond_key]
    T = data["temperature_K"]
    k_lat = data["kappa_lat_W_mK"]
    sigma_bulk = data["sigma_bulk_S_m"]
    S_bulk = data["S_bulk_microV_K"]
    k_elec_bulk = data["kappa_elec_bulk_W_mK"]
    sigma_bar = data["sigma_barrier_S_m"]
    S_bar = data["S_barrier_microV_K"]
    k_elec_bar = data["kappa_elec_barrier_W_mK"]
    def zT(sigma, S_uV, k_elec):
        S_V = [s*1e-6 for s in S_uV]
        return [(s**2 * sig * T) / (ke + k_lat) for s, sig, ke in zip(S_V, sigma, k_elec)]
    zT_bulk = zT(sigma_bulk, S_bulk, k_elec_bulk)
    zT_bar = zT(sigma_bar, S_bar, k_elec_bar)
    max_bulk = max(zT_bulk)
    max_bar = max(zT_bar)
    gold_bulk = step["gold_bulk"]
    gold_bar = step["gold_barrier"]
    score_bulk = min(1.0, max(0.0, max_bulk / gold_bulk)) if gold_bulk > 0 else 0.0
    score_bar = min(1.0, max(0.0, max_bar / gold_bar)) if gold_bar > 0 else 0.0
    order_score = 1.0 if max_bar > max_bulk else 0.0
    return (score_bulk + score_bar + order_score) / 3.0


# === block: score_3 (check id='cond_p_Mg2Si0.4Sn0.6_900K') ===
def score_3(artifact, step, ctx):
    cond_key = step["condition_key"]
    if cond_key not in artifact:
        return 0.0
    data = artifact[cond_key]
    T = data["temperature_K"]
    k_lat = data["kappa_lat_W_mK"]
    sigma_bulk = data["sigma_bulk_S_m"]
    S_bulk = data["S_bulk_microV_K"]
    k_elec_bulk = data["kappa_elec_bulk_W_mK"]
    sigma_bar = data["sigma_barrier_S_m"]
    S_bar = data["S_barrier_microV_K"]
    k_elec_bar = data["kappa_elec_barrier_W_mK"]
    def zT(sigma, S_uV, k_elec):
        S_V = [s*1e-6 for s in S_uV]
        return [(s**2 * sig * T) / (ke + k_lat) for s, sig, ke in zip(S_V, sigma, k_elec)]
    zT_bulk = zT(sigma_bulk, S_bulk, k_elec_bulk)
    zT_bar = zT(sigma_bar, S_bar, k_elec_bar)
    max_bulk = max(zT_bulk)
    max_bar = max(zT_bar)
    gold_bulk = step["gold_bulk"]
    gold_bar = step["gold_barrier"]
    score_bulk = min(1.0, max(0.0, max_bulk / gold_bulk)) if gold_bulk > 0 else 0.0
    score_bar = min(1.0, max(0.0, max_bar / gold_bar)) if gold_bar > 0 else 0.0
    order_score = 1.0 if max_bar > max_bulk else 0.0
    return (score_bulk + score_bar + order_score) / 3.0


# === block: score_4 (check id='cond_n_Si0.8Ge0.2_1200K') ===
def score_4(artifact, step, ctx):
    cond_key = step["condition_key"]
    if cond_key not in artifact:
        return 0.0
    data = artifact[cond_key]
    T = data["temperature_K"]
    k_lat = data["kappa_lat_W_mK"]
    sigma_bulk = data["sigma_bulk_S_m"]
    S_bulk = data["S_bulk_microV_K"]
    k_elec_bulk = data["kappa_elec_bulk_W_mK"]
    sigma_bar = data["sigma_barrier_S_m"]
    S_bar = data["S_barrier_microV_K"]
    k_elec_bar = data["kappa_elec_barrier_W_mK"]
    def zT(sigma, S_uV, k_elec):
        S_V = [s*1e-6 for s in S_uV]
        return [(s**2 * sig * T) / (ke + k_lat) for s, sig, ke in zip(S_V, sigma, k_elec)]
    zT_bulk = zT(sigma_bulk, S_bulk, k_elec_bulk)
    zT_bar = zT(sigma_bar, S_bar, k_elec_bar)
    max_bulk = max(zT_bulk)
    max_bar = max(zT_bar)
    gold_bulk = step["gold_bulk"]
    gold_bar = step["gold_barrier"]
    score_bulk = min(1.0, max(0.0, max_bulk / gold_bulk)) if gold_bulk > 0 else 0.0
    score_bar = min(1.0, max(0.0, max_bar / gold_bar)) if gold_bar > 0 else 0.0
    order_score = 1.0 if max_bar > max_bulk else 0.0
    return (score_bulk + score_bar + order_score) / 3.0


# === block: score_5 (check id='cond_p_Si0.8Ge0.2_1200K') ===
def score_5(artifact, step, ctx):
    cond_key = step["condition_key"]
    if cond_key not in artifact:
        return 0.0
    data = artifact[cond_key]
    T = data["temperature_K"]
    k_lat = data["kappa_lat_W_mK"]
    sigma_bulk = data["sigma_bulk_S_m"]
    S_bulk = data["S_bulk_microV_K"]
    k_elec_bulk = data["kappa_elec_bulk_W_mK"]
    sigma_bar = data["sigma_barrier_S_m"]
    S_bar = data["S_barrier_microV_K"]
    k_elec_bar = data["kappa_elec_barrier_W_mK"]
    def zT(sigma, S_uV, k_elec):
        S_V = [s*1e-6 for s in S_uV]
        return [(s**2 * sig * T) / (ke + k_lat) for s, sig, ke in zip(S_V, sigma, k_elec)]
    zT_bulk = zT(sigma_bulk, S_bulk, k_elec_bulk)
    zT_bar = zT(sigma_bar, S_bar, k_elec_bar)
    max_bulk = max(zT_bulk)
    max_bar = max(zT_bar)
    gold_bulk = step["gold_bulk"]
    gold_bar = step["gold_barrier"]
    score_bulk = min(1.0, max(0.0, max_bulk / gold_bulk)) if gold_bulk > 0 else 0.0
    score_bar = min(1.0, max(0.0, max_bar / gold_bar)) if gold_bar > 0 else 0.0
    order_score = 1.0 if max_bar > max_bulk else 0.0
    return (score_bulk + score_bar + order_score) / 3.0


_SCORERS = {
    'cond_n_Bi2Te2.7Se0.3_500K': score_0,
    'cond_p_Bi0.5Sb1.5Te3_500K': score_1,
    'cond_n_Mg2Si0.4Sn0.6_900K': score_2,
    'cond_p_Mg2Si0.4Sn0.6_900K': score_3,
    'cond_n_Si0.8Ge0.2_1200K': score_4,
    'cond_p_Si0.8Ge0.2_1200K': score_5,
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
