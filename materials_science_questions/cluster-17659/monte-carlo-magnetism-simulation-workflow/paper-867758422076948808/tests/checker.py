import os
import json
import csv

# === author imports / helpers ===
import csv
import math

def compute_tau(T, N, E1, E2, E3, n, kB, nu0, N_eff=None):
    if N_eff is None:
        N_eff = N
    nu1 = nu0 * math.exp(-E1 / (kB * T))
    nu2 = nu0 * math.exp(-E2 / (kB * T))
    nu3 = nu0 * math.exp(-E3 / (kB * T))
    a = nu3 / (nu2 + nu3)
    term1 = (a / nu3) * ((N_eff - 1) / 2) * (N_eff - 2 * (1 - 2*a) / (1 - a))
    term2 = (1 / nu1) * (N_eff * (1 - a) - 2 * (1 - 2*a))
    return (1 / (n * a)) * (term1 + term2)


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
    kB_meV = 8.617333262145e-5 * 1000  # meV/K
    nu0 = 1e9
    fe_params = {"E1": 4.32, "E2": 2.76, "E3": 1.72, "n": 2}
    co_params = {"E1": 10.7, "E2": 0.0034, "E3": 0.0065, "n": 4}
    return {"kB": kB_meV, "nu0": nu0, "fe": fe_params, "co": co_params}


# === block: score_0 (check id='fe_reversal') ===
def score_0(artifact, step, ctx):
    artifact_rows = artifact
    fe = ctx["fe"]
    kB = ctx["kB"]
    nu0 = ctx["nu0"]
    conditions_T_N = [
        (4.0, 10), (5.0, 10), (6.0, 10), (7.0, 10),
        (4.0, 5), (4.0, 15), (4.0, 20),
    ]
    lookup = {}
    for row in artifact_rows:
        T = float(row["temperature_K"])
        N = int(row["chain_length_N"])
        model = row["model"].strip()
        tau = float(row["reversal_time_s"])
        lookup.setdefault((T, N), {})[model] = tau

    analytical_ok = 0
    kmc_ok = 0
    trend_ok = 0
    mono_ok = 0
    mono_checks = 0
    total_cond = len(conditions_T_N)
    for (T, N) in conditions_T_N:
        if (T, N) not in lookup:
            continue
        models = lookup[(T, N)]
        if "analytical" not in models:
            continue
        tau_analytical_agent = models["analytical"]
        tau_expected = compute_tau(T, N, fe["E1"], fe["E2"], fe["E3"], fe["n"], kB, nu0)
        # exactness of analytical computation (trivial recomputation)
        rel_err_analytical = abs(tau_analytical_agent - tau_expected) / max(1e-300, tau_expected)
        if rel_err_analytical < 1e-6 or abs(tau_analytical_agent - tau_expected) < 1e-9:
            analytical_ok += 1
        # main kMC check: agent's improved_kMC must be within 50% of the expected value
        if "improved_kMC" in models:
            tau_imp = models["improved_kMC"]
            rel_err_kmc = abs(tau_imp - tau_expected) / max(1e-300, tau_expected)
            if rel_err_kmc <= 0.5:
                kmc_ok += 1
        if "improved_kMC" in models and "simple_kMC" in models:
            if models["improved_kMC"] < models["simple_kMC"]:
                trend_ok += 1

    T_list_N10 = [4.0, 5.0, 6.0, 7.0]
    mono_checks += 1
    if all((T, 10) in lookup and "improved_kMC" in lookup[(T, 10)] for T in T_list_N10):
        vals = [lookup[(T, 10)]["improved_kMC"] for T in T_list_N10]
        if all(vals[i] > vals[i+1] for i in range(len(vals)-1)):
            mono_ok += 1
    N_list_T4 = [5, 10, 15, 20]
    mono_checks += 1
    if all((4.0, N) in lookup and "improved_kMC" in lookup[(4.0, N)] for N in N_list_T4):
        vals = [lookup[(4.0, N)]["improved_kMC"] for N in N_list_T4]
        if all(vals[i] < vals[i+1] for i in range(len(vals)-1)):
            mono_ok += 1

    score_analytical = analytical_ok / total_cond if total_cond else 0
    score_kmc = kmc_ok / total_cond if total_cond else 0
    score_trend = trend_ok / total_cond if total_cond else 0
    score_mono = mono_ok / mono_checks if mono_checks else 0
    return 0.3*score_analytical + 0.4*score_kmc + 0.2*score_trend + 0.1*score_mono


# === block: score_1 (check id='co_reversal') ===
def score_1(artifact, step, ctx):
    artifact_rows = artifact
    co = ctx["co"]
    kB = ctx["kB"]
    nu0 = ctx["nu0"]

    # Hidden gold reversal times (seconds) for improved_kMC, derived from the paper's analytical
    # formula (which the paper states matches the improved kMC results) using the given barriers.
    # Gold derived at each required (T,N) condition.
    kmc_gold = {
        (10.0, 40): compute_tau(10.0, 40, co["E1"], co["E2"], co["E3"], co["n"], kB, nu0, N_eff=30),
        (15.0, 40): compute_tau(15.0, 40, co["E1"], co["E2"], co["E3"], co["n"], kB, nu0, N_eff=30),
        (20.0, 40): compute_tau(20.0, 40, co["E1"], co["E2"], co["E3"], co["n"], kB, nu0, N_eff=30),
        (30.0, 40): compute_tau(30.0, 40, co["E1"], co["E2"], co["E3"], co["n"], kB, nu0, N_eff=30),
        (10.0, 20): compute_tau(10.0, 20, co["E1"], co["E2"], co["E3"], co["n"], kB, nu0, N_eff=10),
        (10.0, 25): compute_tau(10.0, 25, co["E1"], co["E2"], co["E3"], co["n"], kB, nu0, N_eff=15),
        (10.0, 30): compute_tau(10.0, 30, co["E1"], co["E2"], co["E3"], co["n"], kB, nu0, N_eff=20),
    }
    # note: condition (10.0, 40) appears twice in the required list; we keep the same gold.

    conditions_T_N = [
        (10.0, 40), (15.0, 40), (20.0, 40), (30.0, 40),
        (10.0, 20), (10.0, 25), (10.0, 30),
    ]

    lookup = {}
    for row in artifact_rows:
        T = float(row["temperature_K"])
        N = int(row["chain_length_N"])
        model = row["model"].strip()
        tau = float(row["reversal_time_s"])
        lookup.setdefault((T, N), {})[model] = tau

    kmc_gold_ok = 0
    analytical_ok = 0
    trend_ok = 0
    mono_ok = 0
    mono_checks = 0
    total_cond = len(conditions_T_N)

    for (T, N) in conditions_T_N:
        if (T, N) not in lookup:
            continue
        models = lookup[(T, N)]
        if "analytical" not in models:
            continue
        tau_analytical_agent = models["analytical"]
        Neff = N - 10
        if Neff < 1:
            Neff = 1
        tau_expected = compute_tau(T, N, co["E1"], co["E2"], co["E3"], co["n"], kB, nu0, N_eff=Neff)
        rel_err = abs(tau_analytical_agent - tau_expected) / max(1e-300, tau_expected)
        if rel_err < 1e-6 or abs(tau_analytical_agent - tau_expected) < 1e-9:
            analytical_ok += 1

        # Main kMC check: agent's improved_kMC within factor 3 of the hidden gold value
        if "improved_kMC" in models and (T, N) in kmc_gold:
            tau_imp = models["improved_kMC"]
            gold = kmc_gold[(T, N)]
            if gold * (1/3.0) <= tau_imp <= gold * 3.0:
                kmc_gold_ok += 1

        # Trend: improved_kMC must be less than simple_kMC
        if "improved_kMC" in models and "simple_kMC" in models:
            if models["improved_kMC"] < models["simple_kMC"]:
                trend_ok += 1

    # Monotonicity checks
    T_list = [10.0, 15.0, 20.0, 30.0]
    mono_checks += 1
    if all((T, 40) in lookup and "improved_kMC" in lookup[(T, 40)] for T in T_list):
        vals = [lookup[(T, 40)]["improved_kMC"] for T in T_list]
        if all(vals[i] > vals[i+1] for i in range(len(vals)-1)):
            mono_ok += 1
    N_list = [20, 25, 30, 40]
    mono_checks += 1
    if all((10.0, N) in lookup and "improved_kMC" in lookup[(10.0, N)] for N in N_list):
        vals = [lookup[(10.0, N)]["improved_kMC"] for N in N_list]
        if all(vals[i] < vals[i+1] for i in range(len(vals)-1)):
            mono_ok += 1

    score_kmc = kmc_gold_ok / total_cond if total_cond else 0
    score_analytical = analytical_ok / total_cond if total_cond else 0
    score_trend = trend_ok / total_cond if total_cond else 0
    score_mono = mono_ok / mono_checks if mono_checks else 0
    return 0.5*score_kmc + 0.2*score_analytical + 0.2*score_trend + 0.1*score_mono


_SCORERS = {
    'fe_reversal': score_0,
    'co_reversal': score_1,
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
