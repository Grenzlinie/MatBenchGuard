import os
import json
import csv

# === author imports / helpers ===
import csv, os, math


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
        csv_path = os.path.join(outputs_dir, "band_structure.csv")
        ctx = {"indirect_gap": None, "direct_gap": None, "hole_lighter": None, "cbm_not_gamma": False}
        try:
            with open(csv_path, newline='') as f:
                reader = csv.DictReader(f)
                rows = list(reader)
        except Exception:
            return ctx

        # parse rows
        data = []
        for r in rows:
            try:
                kx = float(r["kx"])
                ky = float(r["ky"])
                kz = float(r["kz"])
                band = int(r["band_index"])
                energy = float(r["energy"])
                data.append((kx, ky, kz, band, energy))
            except Exception:
                continue
        if not data:
            return ctx

        # 1. global VBM and CBM
        vbm_energy = None
        cbm_energy = None
        cbm_k = None
        for (kx, ky, kz, band, e) in data:
            if band == -1:
                if vbm_energy is None or e > vbm_energy:
                    vbm_energy = e
            elif band == 0:
                if cbm_energy is None or e < cbm_energy:
                    cbm_energy = e
                    cbm_k = (kx, ky, kz)
        if vbm_energy is None or cbm_energy is None:
            return ctx
        indirect_gap = cbm_energy - vbm_energy
        ctx["indirect_gap"] = indirect_gap

        # 2. direct gap at Gamma
        gamma_valence = None
        gamma_conduction = None
        for (kx, ky, kz, band, e) in data:
            if abs(kx) < 1e-6 and abs(ky) < 1e-6 and abs(kz) < 1e-6:
                if band == -1:
                    if gamma_valence is None or e > gamma_valence:
                        gamma_valence = e
                elif band == 0:
                    if gamma_conduction is None or e < gamma_conduction:
                        gamma_conduction = e
        if gamma_valence is not None and gamma_conduction is not None:
            direct_gap = gamma_conduction - gamma_valence
            ctx["direct_gap"] = direct_gap

        # 3. CBM not at Gamma?
        if cbm_k is not None:
            kx_c, ky_c, kz_c = cbm_k
            if math.sqrt(kx_c**2 + ky_c**2 + kz_c**2) > 1e-6:
                ctx["cbm_not_gamma"] = True

        # 4. effective mass ordering from Γ‑Y segment (kx=0, kz=0)
        line = [(ky, e) for (kx, ky, kz, band, e) in data
                if band in (-1, 0) and abs(kx) < 1e-6 and abs(kz) < 1e-6]
        # valence band on line
        vals = [(ky, e) for (ky, e) in line if e <= 0]  # likely valence
        # but better filter by band index from data; we'll re-scan
        vals_v = []
        cond_c = []
        for (kx, ky, kz, band, e) in data:
            if abs(kx) < 1e-6 and abs(kz) < 1e-6:
                if band == -1:
                    vals_v.append((ky, e))
                elif band == 0:
                    cond_c.append((ky, e))
        # curvature for hole
        hole_lighter = None
        try:
            # find Gamma valence energy
            gamma_v = None
            for (ky, e) in vals_v:
                if abs(ky) < 1e-6:
                    gamma_v = e
                    break
            if gamma_v is not None:
                # find a small positive ky
                small_kys = [(ky, e) for (ky, e) in vals_v if ky > 1e-6]
                if small_kys:
                    ky_s, e_s = sorted(small_kys, key=lambda x: x[0])[0]
                    alpha_v = -(e_s - gamma_v) / (ky_s**2)
                else:
                    alpha_v = None
            else:
                alpha_v = None

            # conduction band minimum on Γ‑Y
            cbm_line = None
            k0 = None
            for (ky, e) in cond_c:
                if cbm_line is None or e < cbm_line:
                    cbm_line = e
                    k0 = ky
            if cbm_line is not None and k0 is not None:
                # find point with ky just larger than k0
                larger = [(ky, e) for (ky, e) in cond_c if ky > k0 + 1e-6]
                if larger:
                    ky_l, e_l = sorted(larger, key=lambda x: x[0])[0]
                    dk = ky_l - k0
                    alpha_c = (e_l - cbm_line) / (dk**2)
                else:
                    alpha_c = None
            else:
                alpha_c = None

            if alpha_v is not None and alpha_c is not None:
                if alpha_v > alpha_c + 1e-3:
                    hole_lighter = True
                else:
                    hole_lighter = False
        except Exception:
            pass

        ctx["hole_lighter"] = hole_lighter
        return ctx


# === block: score_0 (check id='check_band_structure') ===
def score_0(artifact, step, ctx):
        indirect = ctx.get("indirect_gap")
        direct = ctx.get("direct_gap")
        cbm_not_gamma = ctx.get("cbm_not_gamma", False)
        if indirect is None or direct is None:
            return 0.0

        target_ind = step["target_indirect_gap_eV"]
        tol_ind = step["tolerance_indirect_eV"]
        err_ind = abs(indirect - target_ind)
        if err_ind <= tol_ind:
            s_ind = 1.0
        else:
            s_ind = max(0.0, 1.0 - (err_ind - tol_ind) / (3.0 * tol_ind))

        target_dir = step["target_direct_gap_eV"]
        tol_dir = step["tolerance_direct_eV"]
        err_dir = abs(direct - target_dir)
        if err_dir <= tol_dir:
            s_dir = 1.0
        else:
            s_dir = max(0.0, 1.0 - (err_dir - tol_dir) / (3.0 * tol_dir))

        s_struct = 1.0 if cbm_not_gamma else 0.0

        return 0.5 * s_ind + 0.3 * s_dir + 0.2 * s_struct


# === block: score_1 (check id='check_results') ===
def score_1(artifact, step, ctx):
        indirect = ctx.get("indirect_gap")
        direct = ctx.get("direct_gap")
        hole_lighter = ctx.get("hole_lighter")
        if indirect is None or direct is None:
            return 0.0

        tol = step.get("tolerance_gap_match_eV", 0.1)
        rep_ind = artifact.get("indirect_gap")
        rep_dir = artifact.get("direct_gap_at_Gamma")

        s_ind = 1.0 if abs(rep_ind - indirect) <= tol else 0.0
        s_dir = 1.0 if abs(rep_dir - direct) <= tol else 0.0

        # Score ordering against the paper's expected hidden gold
        expected_ordering = step.get("expected_ordering", "hole_lighter_than_electron")
        s_ord = 0.0
        if hole_lighter is not None:
            if (hole_lighter and expected_ordering == "hole_lighter_than_electron") or \
               (not hole_lighter and expected_ordering == "electron_lighter_than_hole"):
                s_ord = 1.0

        return 0.2 * s_ind + 0.2 * s_dir + 0.6 * s_ord


_SCORERS = {
    'check_band_structure': score_0,
    'check_results': score_1,
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
