import os
import json
import csv

# === author imports / helpers ===
import csv, math, os


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
    steps = spec.get("steps", [])
    targets = {}
    for step in steps:
        if step.get("id") == "eval_dft_results":
            targets["tc_values"] = step["tc_values"]
            targets["omega_log"] = step["omega_log"]
            targets["ry_to_ev"] = step["ry_to_ev"]
            targets["natoms"] = step["natoms"]
            targets["target_N_EF"] = step["target_N_EF"]
            targets["target_lambda"] = step["target_lambda"]
            targets["tolerance_N_EF_rel"] = step["tolerance_N_EF_rel"]
            targets["tolerance_lambda_abs"] = step["tolerance_lambda_abs"]
            targets["dos_files"] = step["dos_files"]
            break
    return targets


# === block: score_0 (check id='eval_dft_results') ===
def score_0(artifact, step, ctx):
    import csv, math, os

    compound_names = ["V3Ni", "V3Pd", "V3Pt"]
    output_dir = "/app/outputs"
    weights_per_compound = 1.0 / len(compound_names)

    # ---------- recompute N_EF and lambda from raw DOS evidence ----------
    recomputed = {}
    for comp in compound_names:
        dos_file = os.path.join(output_dir, ctx['dos_files'][comp])
        if not os.path.isfile(dos_file):
            recomputed[comp] = None
            continue
        dos_data = []
        with open(dos_file, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    e = float(row['energy'])
                    d = float(row['dos'])
                    dos_data.append((e, d))
                except (KeyError, ValueError):
                    pass
        if len(dos_data) == 0:
            recomputed[comp] = None
            continue
        dos_data.sort(key=lambda x: x[0])
        dos_at_ef = None
        if not (dos_data[0][0] > 0 or dos_data[-1][0] < 0):
            for i in range(len(dos_data) - 1):
                e1, d1 = dos_data[i]
                e2, d2 = dos_data[i + 1]
                if (e1 <= 0.0 <= e2) or (e2 <= 0.0 <= e1):
                    if abs(e1 - e2) < 1e-12:
                        dos_at_ef = (d1 + d2) / 2.0
                    else:
                        t = (0.0 - e1) / (e2 - e1)
                        dos_at_ef = d1 + t * (d2 - d1)
                    break
        if dos_at_ef is None:
            recomputed[comp] = None
            continue
        n_ef_ry = dos_at_ef * ctx['ry_to_ev']
        n_cell_ev = n_ef_ry / ctx['ry_to_ev']
        n_atom_ev = n_cell_ev / ctx['natoms']
        mu_star = 0.26 * n_atom_ev / (1.0 + n_atom_ev)
        tc = ctx['tc_values'][comp]
        omega_log = ctx['omega_log']
        L = math.log(tc * 1.2 / omega_log)
        lo, hi = 0.01, 5.0
        for _ in range(60):
            mid = (lo + hi) / 2.0
            denom = mid - mu_star * (1.0 + 0.62 * mid)
            if denom == 0:
                break
            val = L + 1.04 * (1.0 + mid) / denom
            if val > 0:
                lo = mid
            else:
                hi = mid
        lam = (lo + hi) / 2.0
        recomputed[comp] = {'N_EF': n_ef_ry, 'lambda': lam}

    # ---------- cross-check dft_results.csv against recomputed values ----------
    csv_path = os.path.join(output_dir, "dft_results.csv")
    self_consistency_factor = 1.0
    if os.path.isfile(csv_path):
        with open(csv_path, newline='') as f:
            reader = csv.DictReader(f)
            csv_comps = set()
            for row in reader:
                comp = row.get('compound', '').strip()
                if comp in recomputed and recomputed[comp] is not None:
                    try:
                        n_reported = float(row['N_EF'])
                        lam_reported = float(row['lambda'])
                    except (ValueError, KeyError):
                        self_consistency_factor = 0.0
                        break
                    n_rec = recomputed[comp]['N_EF']
                    lam_rec = recomputed[comp]['lambda']
                    if (abs(n_reported - n_rec) / (abs(n_rec) + 1e-10) > 0.01 or
                            abs(lam_reported - lam_rec) > 0.01):
                        self_consistency_factor = 0.0
                        break
                    csv_comps.add(comp)
            if csv_comps != set(compound_names):
                self_consistency_factor = 0.0
    else:
        self_consistency_factor = 0.0

    # ---------- score recomputed N_EF and lambda against hidden gold ----------
    total_score = 0.0
    for comp in compound_names:
        if recomputed.get(comp) is None:
            continue
        n_ef_ry = recomputed[comp]['N_EF']
        lam = recomputed[comp]['lambda']
        # N_EF
        target_n = ctx['target_N_EF'][comp]
        rel_err = abs(n_ef_ry - target_n) / target_n
        tol_n = ctx['tolerance_N_EF_rel']
        if rel_err <= tol_n:
            n_score = 1.0
        else:
            n_score = max(0.0, 1.0 - (rel_err - tol_n) / (2 * tol_n))
        # lambda
        target_lam = ctx['target_lambda'][comp]
        abs_err = abs(lam - target_lam)
        tol_lam = ctx['tolerance_lambda_abs']
        if abs_err <= tol_lam:
            lam_score = 1.0
        else:
            lam_score = max(0.0, 1.0 - (abs_err - tol_lam) / (2 * tol_lam))
        comp_score = 0.5 * n_score + 0.5 * lam_score
        total_score += comp_score * weights_per_compound

    total_score = max(0.0, min(1.0, total_score * self_consistency_factor))
    return total_score


_SCORERS = {
    'eval_dft_results': score_0,
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
