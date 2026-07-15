import os
import json
import csv

# === author imports / helpers ===
import numpy as np
import csv
import math
import numpy.linalg as la


def birch_murnaghan(V, E0, V0, K0, K0_prime):
    x = V0 / V
    xi = 0.75 * (K0_prime - 4)
    return E0 + 1.5 * K0 * V0 * (1.5*(xi-1)*x**(2/3) + 0.75*(1-2*xi)*x**(4/3) + 0.5*xi*x**(6/3) - (2*xi-3)/4)


def fit_structure(volumes, energies):
    idx_min = np.argmin(energies)
    V0_guess = volumes[idx_min]
    E0_guess = energies[idx_min]
    K0_guess = 300.0
    K0p_guess = 4.0
    p = np.array([E0_guess, V0_guess, K0_guess, K0p_guess])
    n = len(volumes)
    for _ in range(200):
        y_pred = birch_murnaghan(volumes, *p)
        resid = energies - y_pred
        J = np.zeros((n, 4))
        h = 1e-6
        for i in range(4):
            p_plus = p.copy()
            p_plus[i] += h
            J[:, i] = (birch_murnaghan(volumes, *p_plus) - y_pred) / h
        JTJ = J.T @ J
        JTJ_damped = JTJ + 1e-3 * np.eye(4)
        try:
            delta = np.linalg.solve(JTJ_damped, J.T @ resid)
        except np.linalg.LinAlgError:
            delta = np.linalg.lstsq(JTJ_damped, J.T @ resid, rcond=None)[0]
        p_new = p + delta
        if np.max(np.abs(delta)) < 1e-8:
            p = p_new
            break
        p = p_new
    return p


def score_within_tol(val, target, tol, decay_scale=None):
    if target is None or (isinstance(target, float) and math.isnan(target)):
        return 1.0
    diff = abs(val - target)
    if diff <= tol:
        return 1.0
    if decay_scale is None:
        decay_scale = tol
    return max(0.0, 1.0 - (diff - tol) / decay_scale)


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
    output_dir = "/app/outputs"

    # Load raw energy-volume data
    ev_path = os.path.join(output_dir, "energy_volume_data.csv")
    if not os.path.exists(ev_path):
        return {"error": "missing energy_volume_data.csv"}
    with open(ev_path, newline='') as f:
        reader = csv.DictReader(f)
        all_rows = list(reader)
        if not all_rows:
            return {"error": "empty energy_volume_data.csv"}
    
    data_by_structure = {}
    for row in all_rows:
        struct = row["structure"]
        V = float(row["volume"])
        E = float(row["total_energy"])
        data_by_structure.setdefault(struct, []).append((V, E))

    fitted = {}
    structures_order = ["CoSn", "WC", "NaCl", "ZnS-B3", "CsCl"]
    for struct in structures_order:
        if struct not in data_by_structure or len(data_by_structure[struct]) < 4:
            continue
        points = data_by_structure[struct]
        V_arr = np.array([p[0] for p in points])
        E_arr = np.array([p[1] for p in points])
        try:
            popt = fit_structure(V_arr, E_arr)
            fitted[struct] = {"E0": popt[0], "V0": popt[1], "K0": popt[2], "K0_prime": popt[3]}
        except Exception:
            continue

    # Load derived_properties.csv
    derived_path = os.path.join(output_dir, "derived_properties.csv")
    derived_rows = []
    if os.path.exists(derived_path):
        with open(derived_path, newline='') as f:
            reader = csv.DictReader(f)
            derived_rows = list(reader)

    # Load electronic_properties.csv
    elec_path = os.path.join(output_dir, "electronic_properties.csv")
    elec_rows = []
    if os.path.exists(elec_path):
        with open(elec_path, newline='') as f:
            reader = csv.DictReader(f)
            elec_rows = list(reader)

    # Hidden gold from spec
    paper_derived = spec.get("paper_derived", {})
    paper_electronic = spec.get("paper_electronic", {})

    return {
        "fitted": fitted,
        "derived_rows": derived_rows,
        "elec_rows": elec_rows,
        "paper_derived": paper_derived,
        "paper_electronic": paper_electronic
    }


# === block: score_0 (check id='derived_cosn') ===
def score_0(artifact, step, ctx):
    fitted = ctx.get("fitted", {})
    derived = ctx.get("derived_rows", [])
    paper = ctx.get("paper_derived", {})

    struct = "CoSn"
    if struct not in paper:
        return 0.0

    agent_row = None
    for row in derived:
        if row.get("structure") == struct:
            agent_row = row
            break
    if agent_row is None:
        return 0.0

    paper_prop = paper[struct]

    scores = []
    # a vs paper
    a_agent = float(agent_row.get("a", 0))
    scores.append(score_within_tol(a_agent, paper_prop["a"], 0.01, 0.01))
    # c vs paper
    c_agent = float(agent_row.get("c", 0))
    scores.append(score_within_tol(c_agent, paper_prop["c"], 0.01, 0.01))
    # N_x vs paper
    nx = float(agent_row.get("N_x", 0))
    scores.append(score_within_tol(nx, paper_prop["N_x"], 0.0005, 0.0005))

    fit_prop = fitted.get(struct)
    if fit_prop:
        # E0 consistency
        e0_agent = float(agent_row.get("E0", 0))
        scores.append(score_within_tol(e0_agent, fit_prop["E0"], 0.001, 0.001))
        # V0 consistency
        v0_agent = float(agent_row.get("V0", 0))
        scores.append(score_within_tol(v0_agent, fit_prop["V0"], 0.001, 0.001))
        # K0 consistency
        k0_agent = float(agent_row.get("K0", 0))
        scores.append(score_within_tol(k0_agent, fit_prop["K0"], 0.1, 0.1))
        # K0_prime consistency
        k0p_agent = float(agent_row.get("K0_prime", 0))
        scores.append(score_within_tol(k0p_agent, fit_prop["K0_prime"], 0.01, 0.01))
    else:
        # if fitting failed, penalize heavily
        scores.extend([0.0, 0.0, 0.0, 0.0])

    return sum(scores) / len(scores) if scores else 0.0


# === block: score_1 (check id='derived_other') ===
def score_1(artifact, step, ctx):
    fitted = ctx.get("fitted", {})
    derived = ctx.get("derived_rows", [])
    paper = ctx.get("paper_derived", {})

    structures = ["WC", "NaCl", "ZnS-B3", "CsCl"]
    all_scores = []
    for struct in structures:
        paper_prop = paper.get(struct)
        if paper_prop is None:
            continue
        agent_row = None
        for row in derived:
            if row.get("structure") == struct:
                agent_row = row
                break
        if agent_row is None:
            all_scores.append(0.0)
            continue

        sub_scores = []
        # a vs paper
        a_agent = float(agent_row.get("a", 0))
        sub_scores.append(score_within_tol(a_agent, paper_prop["a"], 0.01, 0.01))
        # c if applicable (hexagonal)
        if paper_prop.get("c") is not None:
            c_agent = float(agent_row.get("c", 0))
            sub_scores.append(score_within_tol(c_agent, paper_prop["c"], 0.01, 0.01))

        fit_prop = fitted.get(struct)
        if fit_prop:
            e0_agent = float(agent_row.get("E0", 0))
            sub_scores.append(score_within_tol(e0_agent, fit_prop["E0"], 0.001, 0.001))
            v0_agent = float(agent_row.get("V0", 0))
            sub_scores.append(score_within_tol(v0_agent, fit_prop["V0"], 0.001, 0.001))
            k0_agent = float(agent_row.get("K0", 0))
            sub_scores.append(score_within_tol(k0_agent, fit_prop["K0"], 0.1, 0.1))
            k0p_agent = float(agent_row.get("K0_prime", 0))
            sub_scores.append(score_within_tol(k0p_agent, fit_prop["K0_prime"], 0.01, 0.01))
        else:
            sub_scores.extend([0.0, 0.0, 0.0, 0.0])

        if sub_scores:
            all_scores.append(sum(sub_scores) / len(sub_scores))
    return sum(all_scores) / len(all_scores) if all_scores else 0.0


# === block: score_2 (check id='stability_ordering') ===
def score_2(artifact, step, ctx):
    fitted = ctx.get("fitted", {})
    structures = ["CoSn", "WC", "NaCl", "ZnS-B3", "CsCl"]
    e0_vals = {}
    for s in structures:
        if s in fitted:
            e0_vals[s] = fitted[s]["E0"]
    if len(e0_vals) != 5:
        return 0.0

    correct = 0
    pairs = [("CoSn","WC"), ("WC","NaCl"), ("NaCl","ZnS-B3"), ("ZnS-B3","CsCl")]
    for s1, s2 in pairs:
        if e0_vals[s1] < e0_vals[s2]:
            correct += 1
    return correct / len(pairs)


# === block: score_3 (check id='electronic_properties') ===
def score_3(artifact, step, ctx):
    elec_rows = ctx.get("elec_rows", [])
    paper_elec = ctx.get("paper_electronic", {})

    structures = ["CoSn", "WC", "NaCl", "ZnS-B3", "CsCl"]
    all_scores = []
    for struct in structures:
        paper_prop = paper_elec.get(struct)
        if paper_prop is None:
            continue
        agent_row = None
        for row in elec_rows:
            if row.get("structure") == struct:
                agent_row = row
                break
        if agent_row is None:
            all_scores.append(0.0)
            continue

        sub = []
        # N_tot_EF
        n_ef = float(agent_row.get("N_tot_EF", 0))
        sub.append(score_within_tol(n_ef, paper_prop["N_tot_EF"], 0.03, 0.03))
        # q_Ta_1
        qt1 = float(agent_row.get("q_Ta_1", 0))
        sub.append(score_within_tol(qt1, paper_prop["q_Ta_1"], 0.02, 0.02))
        # q_Ta_2 if present
        if paper_prop.get("q_Ta_2") is not None:
            qt2 = float(agent_row.get("q_Ta_2", 0))
            sub.append(score_within_tol(qt2, paper_prop["q_Ta_2"], 0.02, 0.02))
        else:
            # check agent supplies NA or reasonable default
            qt2_raw = agent_row.get("q_Ta_2", "").strip().lower()
            if qt2_raw in ("", "na", "nan", "none"):
                sub.append(1.0)
            else:
                sub.append(0.0)
        # q_N
        qn = float(agent_row.get("q_N", 0))
        sub.append(score_within_tol(qn, paper_prop["q_N"], 0.02, 0.02))
        all_scores.append(sum(sub) / len(sub))
    return sum(all_scores) / len(all_scores) if all_scores else 0.0


_SCORERS = {
    'derived_cosn': score_0,
    'derived_other': score_1,
    'stability_ordering': score_2,
    'electronic_properties': score_3,
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
