import os
import json
import csv

# === author imports / helpers ===
import csv, math, os, json


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


# === block: score_0 (check id='s2_scored') ===
def score_0(artifact, step, ctx):
    val = float(artifact.strip()) if artifact else 0.0
    return 1.0 if abs(val - step['target']) <= step.get('tolerance', 5.0) else 0.0


# === block: score_1 (check id='s4_scored') ===
def score_1(artifact, step, ctx):
    import math, json, os
    from collections import defaultdict
    import numpy as np
    from scipy.optimize import curve_fit

    def _bm_eos(V, E0, V0, B0, B0p):
        """Third-order Birch-Murnaghan EOS: E(V) = E0 + 9*V0*B0/16 * ...
        Args: V (Å³/atom), E0 (eV), V0 (Å³/atom), B0 (eV/Å³), B0' (dimensionless)
        Returns: energy in eV."""
        eta = (V0 / V) ** (2 / 3)
        term = (9 * V0 * B0 / 16) * ((eta - 1) ** 2) * (1.0 + (B0p - 4) * (eta - 1) / 6.0)
        return E0 + term

    # --- scorer body ---
    if not artifact or not isinstance(artifact, list) or not artifact:
        return 0.0
    cols = set(artifact[0].keys())
    required = {'n', 'configuration_index', 'multiplicity', 'volume', 'static_energy', 'spin_label'}
    if not required.issubset(cols):
        return 0.0

    # 1. Combinatorial multiplicity check (weight 0.3)
    groups = defaultdict(int)
    for row in artifact:
        try:
            n_val = float(row['n'])
            mult = int(row['multiplicity'])
        except (ValueError, KeyError):
            return 0.0
        groups[n_val] += mult
    expected = {}
    for n_val in groups:
        k = int(round(n_val * 6))
        if k < 1 or k > 5:
            return 0.0
        expected[n_val] = math.comb(6, k)
    score_comb = 1.0 if groups == expected else 0.0

    # 2. EOS sanity check (weight 0.7) — each config must have ≥3 volumes and fit well
    config_data = defaultdict(list)
    for row in artifact:
        try:
            ci = int(row['configuration_index'])
            V = float(row['volume'])
            E = float(row['static_energy'])
        except (ValueError, KeyError):
            continue
        config_data[ci].append((V, E))

    eos_ok = 0
    total_configs = len(config_data)
    if total_configs == 0:
        score_eos = 0.0
    else:
        for ci, points in config_data.items():
            if len(points) < 3:
                continue
            points.sort(key=lambda x: x[0])
            V_arr = np.array([p[0] for p in points])
            E_arr = np.array([p[1] for p in points])
            try:
                popt, _ = curve_fit(
                    _bm_eos, V_arr, E_arr,
                    p0=[E_arr.mean(), V_arr.mean(), 1.0, 4.0],
                    bounds=([E_arr.min() - 1.0, V_arr.min() * 0.8, 0.5, 2.0],
                            [E_arr.max() + 1.0, V_arr.max() * 1.2, 2.5, 8.0]),
                    maxfev=2000
                )
                E_pred = _bm_eos(V_arr, *popt)
                ss_res = np.sum((E_arr - E_pred) ** 2)
                ss_tot = np.sum((E_arr - E_arr.mean()) ** 2)
                r2 = 1 - ss_res / ss_tot if ss_tot > 1e-12 else 0.0
                bulk_modulus = popt[2]  # in eV/Å³
                if r2 > 0.99 and 0.5 <= bulk_modulus <= 2.5:
                    eos_ok += 1
            except Exception:
                continue
        score_eos = eos_ok / total_configs

    return max(0.0, min(1.0, 0.3 * score_comb + 0.7 * score_eos))


# === block: score_2 (check id='s7_scored') ===
def score_2(artifact, step, ctx):
    # artifact: list of dicts with columns pressure_GPa, temperature_K, LS_fraction
    if not artifact or not isinstance(artifact, list) or not artifact:
        return 0.0
    cols = set(artifact[0].keys())
    if 'pressure_GPa' not in cols or 'temperature_K' not in cols or 'LS_fraction' not in cols:
        return 0.0
    # Convert to list of (T, P, n)
    data = []
    for row in artifact:
        try:
            P = float(row['pressure_GPa'])
            T = float(row['temperature_K'])
            n = float(row['LS_fraction'])
            if not (0.0 <= n <= 1.0):
                return 0.0
            data.append((T, P, n))
        except (ValueError, KeyError):
            return 0.0
    if not data:
        return 0.0

    # ---- Check 1: monotonicity for each temperature (0.15 weight) ----
    temp_groups = {}
    for T, P, n in data:
        temp_groups.setdefault(T, []).append((P, n))
    mono_ok = True
    for T, pairs in temp_groups.items():
        pairs.sort(key=lambda x: x[0])
        for i in range(1, len(pairs)):
            if pairs[i][1] < pairs[i-1][1] - 1e-6:
                mono_ok = False
                break
        if not mono_ok:
            break
    score1 = 1.0 if mono_ok else 0.0

    # ---- Check 2: room-temperature crossover range (0.15 weight) ----
    rt_data = [(P, n) for T, P, n in data if abs(T - 300.0) <= 10.0]
    score2 = 0.0
    if rt_data:
        rt_data.sort(key=lambda x: x[0])
        n_min = rt_data[0][1]
        n_max = rt_data[-1][1]
        if n_min < 0.2 and n_max > 0.8:
            score2 = 1.0
        elif n_min < 0.3 and n_max > 0.7:
            score2 = 0.5

    # ---- Check 3: numeric checkpoints (0.70 weight) ----
    # Representative (T[K], P[GPa]) -> (expected LS fraction, tolerance)
    checkpoints = [
        # 300 K: onset ~45 GPa, mid ~60 GPa, end ~80 GPa
        (300.0, 45.0, 0.05, 0.12),
        (300.0, 60.0, 0.60, 0.20),
        (300.0, 80.0, 0.95, 0.10),
        # 2000 K: onset stays ~45 GPa, mid ~70 GPa, end ~100 GPa
        (2000.0, 45.0, 0.05, 0.15),
        (2000.0, 70.0, 0.60, 0.20),
        (2000.0, 100.0, 0.95, 0.10),
        # 4000 K: onset ~45 GPa, mid ~80 GPa, end ~120 GPa
        (4000.0, 45.0, 0.10, 0.15),
        (4000.0, 80.0, 0.55, 0.25),
        (4000.0, 120.0, 0.95, 0.10),
    ]
    matched = 0
    for T_ref, P_ref, n_exp, tol in checkpoints:
        # find all points within ±10 K and ±2 GPa
        nearby = [(P, n) for T, P, n in data if abs(T - T_ref) <= 10.0 and abs(P - P_ref) <= 2.0]
        if not nearby:
            continue
        # average n of nearby points (proxy for interpolation)
        avg_n = sum(n for _, n in nearby) / len(nearby)
        if abs(avg_n - n_exp) <= tol:
            matched += 1
    score3 = matched / len(checkpoints) if checkpoints else 0.0

    # Combine weights: 0.15 + 0.15 + 0.70 = 1.0
    final_score = 0.15 * score1 + 0.15 * score2 + 0.70 * score3
    return min(final_score, 1.0)


_SCORERS = {
    's2_scored': score_0,
    's4_scored': score_1,
    's7_scored': score_2,
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
