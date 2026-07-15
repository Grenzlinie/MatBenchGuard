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
    import os, json
    mae_path = os.path.join(outputs_dir, "step_01_MAE_results.json")
    ctx = {"D_fcc": None, "D_hcp": None, "mae_data": None}
    if os.path.exists(mae_path):
        with open(mae_path) as f:
            data = json.load(f)
        if isinstance(data, list) and len(data) >= 2:
            for entry in data:
                if isinstance(entry, dict) and "site" in entry:
                    site = entry["site"]
                    d_val = entry.get("D_meV", None)
                    if site == "fcc":
                        ctx["D_fcc"] = d_val
                    elif site == "hcp":
                        ctx["D_hcp"] = d_val
            ctx["mae_data"] = data
    return ctx


# === block: score_0 (check id='step_01_mae') ===
def score_0(artifact, step, ctx):
    if not artifact or not isinstance(artifact, list):
        return 0.0
    fcc_entry = None
    hcp_entry = None
    for e in artifact:
        if not isinstance(e, dict):
            continue
        s = e.get("site")
        if s == "fcc":
            fcc_entry = e
        elif s == "hcp":
            hcp_entry = e
    if fcc_entry is None or hcp_entry is None:
        return 0.0
    fcc_D = fcc_entry.get("D_meV")
    fcc_axis = fcc_entry.get("easy_axis")
    hcp_D = hcp_entry.get("D_meV")
    hcp_axis = hcp_entry.get("easy_axis")
    if not (isinstance(fcc_D, (int, float)) and isinstance(hcp_D, (int, float))):
        return 0.0
    if fcc_D >= 0 or fcc_axis != "out-of-plane":
        return 0.0
    if hcp_D <= 0 or hcp_axis != "easy-plane":
        return 0.0
    fcc_Ea = fcc_entry.get("E_a_meV")
    hcp_Ea = hcp_entry.get("E_a_meV")
    if fcc_Ea is None or hcp_Ea is None:
        return 0.0
    factor = 8.75
    fcc_expected_D = fcc_Ea / factor if factor != 0 else 0.0
    hcp_expected_D = hcp_Ea / factor if factor != 0 else 0.0
    if abs(fcc_D - fcc_expected_D) > 0.001 or abs(hcp_D - hcp_expected_D) > 0.001:
        return 0.0
    return 1.0


# === block: score_1 (check id='step_02_field') ===
def score_1(artifact, step, ctx):
    D_fcc = ctx.get("D_fcc")
    D_hcp = ctx.get("D_hcp")
    if D_fcc is None or D_hcp is None:
        return 0.0
    if not artifact or not isinstance(artifact, list):
        return 0.0

    g = 2.0
    mu_B = 0.05788
    m_vals = [-2.5, -1.5, -0.5, 0.5, 1.5, 2.5]

    def compute_excitation(D, B):
        energies = [D*(m**2) + g*mu_B*B*m for m in m_vals]
        distinct = sorted(set(energies))
        if len(distinct) < 2:
            return 0.0
        return distinct[1] - distinct[0]

    expected = {}
    for site in ["fcc", "hcp"]:
        D = D_fcc if site == "fcc" else D_hcp
        for i in range(0, 121):
            B = i/10.0
            exc = compute_excitation(D, B)
            expected[(site, f"{B:.1f}")] = exc

    agent = {}
    for row in artifact:
        if not isinstance(row, dict):
            continue
        site = row.get("site")
        B_str = row.get("B_T")
        exc_str = row.get("excitation_energy_meV")
        if site is None or B_str is None or exc_str is None:
            continue
        try:
            B_float = float(B_str)
            exc_float = float(exc_str)
        except:
            continue
        key = (site, f"{B_float:.1f}")
        agent[key] = exc_float

    tol = 0.001
    match_count = 0
    total = 0
    for key, exp_exc in expected.items():
        total += 1
        if key in agent and abs(exp_exc - agent[key]) < tol:
            match_count += 1
    point_ratio = match_count / total if total > 0 else 0.0

    def get_sorted_agent(site):
        entries = []
        for key, val in agent.items():
            if key[0] == site:
                entries.append((float(key[1]), val))
        entries.sort(key=lambda x: x[0])
        return [e[1] for e in entries], [e[0] for e in entries]

    trend_score = 0.0
    fcc_vals, _ = get_sorted_agent("fcc")
    if len(fcc_vals) >= 2 and all(fcc_vals[i+1] > fcc_vals[i] for i in range(len(fcc_vals)-1)):
        trend_score += 0.5
    hcp_vals, _ = get_sorted_agent("hcp")
    if len(hcp_vals) >= 2 and all(hcp_vals[i+1] > hcp_vals[i] for i in range(len(hcp_vals)-1)):
        trend_score += 0.5
    final_score = point_ratio * 0.5 + trend_score
    return max(0.0, min(1.0, final_score))


_SCORERS = {
    'step_01_mae': score_0,
    'step_02_field': score_1,
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
