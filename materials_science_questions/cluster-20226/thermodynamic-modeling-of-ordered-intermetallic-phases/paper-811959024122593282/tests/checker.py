import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.optimize import fsolve
import csv
import os
import json


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
        # Physical constants
        k_B = 1.380649e-23   # J/K
        N_A = 6.02214076e23  # 1/mol
        T = 400.0            # K
        kT = k_B * T

        g_A, g_B = 2, 4
        u_A = 0.0
        u_B = 5.0 * kT

        def occ(mu, u, g):
            return g / (np.exp((u - mu) / kT) + 1.0)

        def total_occ(mu):
            return occ(mu, u_A, g_A) + occ(mu, u_B, g_B)

        def mu_for_x(x):
            if x <= 0:
                return -100.0 * kT
            mu0 = 2.5 * kT
            sol = fsolve(lambda m: total_occ(m[0]) - x, mu0, maxfev=2000)
            return sol[0]

        def compute_state(x):
            mu = mu_for_x(x)
            nA = occ(mu, u_A, g_A)
            nB = occ(mu, u_B, g_B)
            def safe_log(n, g):
                t1 = 0.0 if n <= 0 else n * np.log(n)
                t2 = 0.0 if g - n <= 0 else (g - n) * np.log(g - n)
                return t1, t2
            Sa = g_A * np.log(g_A) - safe_log(nA, g_A)[0] - safe_log(nA, g_A)[1]
            Sb = g_B * np.log(g_B) - safe_log(nB, g_B)[0] - safe_log(nB, g_B)[1]
            S = k_B * (Sa + Sb)
            U = nA * u_A + nB * u_B
            return nA, nB, S, U, mu

        eps = 1e-6
        xs = np.arange(0.0, 4.05, 0.1)
        ref_rows = []
        for x in xs:
            nA, nB, S, U, mu = compute_state(x)
            if x == 0.0:
                _, _, Sr, Ur, _ = compute_state(x + eps)
                dSdx = (Sr - S) / eps
                dUdx = (Ur - U) / eps
            elif x >= 3.98:
                _, _, Sl, Ul, _ = compute_state(x - eps)
                dSdx = (S - Sl) / eps
                dUdx = (U - Ul) / eps
            else:
                _, _, Sl, Ul, _ = compute_state(x - eps)
                _, _, Sr, Ur, _ = compute_state(x + eps)
                dSdx = (Sr - Sl) / (2 * eps)
                dUdx = (Ur - Ul) / (2 * eps)
            mu_mol = mu * N_A
            S_bar = dSdx * N_A
            H_bar = dUdx * N_A
            ref_rows.append((x, nA, nB, S, U, mu_mol, S_bar, H_bar))
        ctx = {'ref_rows': ref_rows, 'xs': xs}
        return ctx


# === block: score_0 (check id='step_01_cu_model_recompute') ===
def score_0(artifact, step, ctx):
        ref_rows = ctx['ref_rows']
        if artifact is None or len(artifact) != len(ref_rows):
            return 0.0
        # check x values
        try:
            agent_xs = [float(row['x']) for row in artifact]
        except Exception:
            return 0.0
        for ax, rx in zip(agent_xs, ctx['xs']):
            if abs(ax - rx) > 1e-12:
                return 0.0

        columns = ['n_A', 'n_B', 'S', 'U', 'mu', 'S_bar', 'H_bar']
        tol_rel = 1e-4
        tol_abs = 1e-6
        total_cells = len(artifact) * len(columns)
        ok_cells = 0
        for i, (ref_row, agent_row) in enumerate(zip(ref_rows, artifact)):
            ref_vals = [ref_row[1], ref_row[2], ref_row[3], ref_row[4], ref_row[5], ref_row[6], ref_row[7]]
            for j, col in enumerate(columns):
                try:
                    aval = float(agent_row[col])
                except (ValueError, TypeError, KeyError):
                    continue
                rval = ref_vals[j]
                if abs(aval - rval) <= tol_abs + tol_rel * abs(rval):
                    ok_cells += 1
        cell_score = ok_cells / total_cells

        # Determine correct peak location from checker-owned reference
        ref_sbar = [r[6] for r in ref_rows]   # index 6 = S_bar in ref_rows
        ref_peak_idx = int(np.argmax(ref_sbar))

        # Find peak in agent's S_bar
        try:
            agent_sbar = [float(row['S_bar']) for row in artifact]
        except Exception:
            agent_sbar = []
        if len(agent_sbar) != len(ref_rows):
            peak_score = 0.0
        else:
            agent_peak_idx = int(np.argmax(agent_sbar))
            peak_score = 1.0 if agent_peak_idx == ref_peak_idx else 0.0

        # Weighted combination (0.95 cell-tolerance, 0.05 peak location)
        return 0.95 * cell_score + 0.05 * peak_score


# === block: score_1 (check id='step_01_cu_model_structural') ===
def score_1(artifact, step, ctx):
        if artifact is None or len(artifact) < 3:
            return 0.0
        try:
            xs = [float(row['x']) for row in artifact]
            sbar_vals = [float(row['S_bar']) for row in artifact]
        except Exception:
            return 0.0
        # Find index of max S_bar
        max_idx = np.argmax(sbar_vals)
        max_x = xs[max_idx]
        # Check peak between 1.5 and 2.5
        score = 0.0
        if 1.5 <= max_x <= 2.5:
            score = 1.0
        # Additional sanity: S_bar values should be > 0 (entropy per mole)
        if any(v <= 0 for v in sbar_vals):
            score *= 0.5
        return score


_SCORERS = {
    'step_01_cu_model_recompute': score_0,
    'step_01_cu_model_structural': score_1,
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
