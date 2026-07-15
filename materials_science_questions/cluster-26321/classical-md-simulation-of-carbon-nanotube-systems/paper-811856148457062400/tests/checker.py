import os
import json
import csv

# === author imports / helpers ===
import os, csv, json, math
from collections import defaultdict


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
        ctx = {"csv_valid": False, "n_configs": 0, "q_left_avg": None, "q_right_avg": None, "delta_u_approx": None}
        csv_path = os.path.join(outputs_dir, "cheLPG_charges.csv")
        if not os.path.exists(csv_path):
            return ctx
        try:
            with open(csv_path, newline='') as f:
                reader = csv.DictReader(f)
                rows = list(reader)
            required_cols = {"config_id","atom_index","element","x","y","z","charge"}
            if not rows:
                return ctx
            if not required_cols.issubset(rows[0].keys()):
                return ctx
            all_rows_parsed = []
            carbon_rows = []
            for r in rows:
                try:
                    cfg = int(r["config_id"])
                    atom = int(r["atom_index"])
                    elem = r["element"].strip()
                    x = float(r["x"])
                    y = float(r["y"])
                    z = float(r["z"])
                    ch = float(r["charge"])
                    all_rows_parsed.append((cfg, atom, elem, x, y, z, ch))
                    if elem == "C":
                        carbon_rows.append((cfg, x, y, z, ch))
                except (ValueError, KeyError):
                    continue
            config_ids = set(cfg for cfg,_,_,_,_,_,_ in all_rows_parsed)
            ctx["n_configs"] = len(config_ids)
            if ctx["n_configs"] != 4:
                return ctx
            cfgs_c = defaultdict(list)
            for cfg, x, y, z, ch in carbon_rows:
                cfgs_c[cfg].append((x,y,z,ch))
            q_left_list = []
            q_right_list = []
            for cfg, atoms in cfgs_c.items():
                if not atoms:
                    continue
                z_coords = [a[2] for a in atoms]
                z_mid = (min(z_coords) + max(z_coords)) / 2.0
                q_left = sum(ch for (_,_,z,ch) in atoms if z < z_mid)
                q_right = sum(ch for (_,_,z,ch) in atoms if z >= z_mid)
                q_left_list.append(q_left)
                q_right_list.append(q_right)
            if len(q_left_list) != ctx["n_configs"]:
                return ctx
            ctx["q_left_avg"] = sum(q_left_list)/len(q_left_list)
            ctx["q_right_avg"] = sum(q_right_list)/len(q_right_list)
            # approximate point-charge potential
            ke = 14.4  # V·Å (1/(4πε0))*e*1e10 ≈ 14.4
            eps = 0.1  # Å
            u_left_cfgs = []
            u_right_cfgs = []
            for cfg in config_ids:
                cfg_rows = [r for r in all_rows_parsed if r[0]==cfg]
                c_rows = [r for r in cfg_rows if r[2]=="C"]
                if not c_rows:
                    continue
                z_vals = [r[5] for r in c_rows]
                z_min = min(z_vals)
                z_max = max(z_vals)
                left_atoms = [r for r in c_rows if abs(r[5]-z_min)<1e-8]
                x_left = sum(r[3] for r in left_atoms)/len(left_atoms) if left_atoms else 0
                y_left = sum(r[4] for r in left_atoms)/len(left_atoms) if left_atoms else 0
                right_atoms = [r for r in c_rows if abs(r[5]-z_max)<1e-8]
                x_right = sum(r[3] for r in right_atoms)/len(right_atoms) if right_atoms else 0
                y_right = sum(r[4] for r in right_atoms)/len(right_atoms) if right_atoms else 0
                p_left = (x_left, y_left, z_min - eps)
                p_right = (x_right, y_right, z_max + eps)
                U_left = 0.0
                U_right = 0.0
                for r in cfg_rows:
                    ch = r[6]
                    dx = r[3] - p_left[0]
                    dy = r[4] - p_left[1]
                    dz = r[5] - p_left[2]
                    d = math.hypot(dx, dy, dz)
                    if d < 1e-12:
                        d = 1e-12
                    U_left += ke * ch / d
                    dx = r[3] - p_right[0]
                    dy = r[4] - p_right[1]
                    dz = r[5] - p_right[2]
                    d = math.hypot(dx, dy, dz)
                    if d < 1e-12:
                        d = 1e-12
                    U_right += ke * ch / d
                u_left_cfgs.append(U_left)
                u_right_cfgs.append(U_right)
            if u_left_cfgs:
                avg_U_left = sum(u_left_cfgs)/len(u_left_cfgs)
                avg_U_right = sum(u_right_cfgs)/len(u_right_cfgs)
                delta_U_V = avg_U_right - avg_U_left
                ctx["delta_u_approx"] = delta_U_V * 1000.0  # mV
            ctx["csv_valid"] = True
        except Exception:
            ctx["csv_valid"] = False
        return ctx


# === block: score_0 (check id='charges_csv_structure') ===
def score_0(artifact, step, ctx):
        global outputs_dir
        outputs_dir = "/app/outputs"
        if not (ctx.get("csv_valid") and ctx.get("n_configs") == 4):
            return 0.0
        # Plausibility gate: the CSV must contain carbon atoms with non‑zero charges,
        # and must include hydrogen and oxygen atoms (representing water molecules).
        try:
            carbon_count = 0
            any_nonzero = False
            elements_seen = set()
            total_atoms = 0
            with open(os.path.join(outputs_dir, "cheLPG_charges.csv"), newline='') as f:
                reader = csv.DictReader(f)
                for r in reader:
                    total_atoms += 1
                    elem = r["element"].strip()
                    elements_seen.add(elem)
                    if elem == "C":
                        carbon_count += 1
                        if abs(float(r["charge"])) > 1e-12:
                            any_nonzero = True
            if not {"C", "H", "O"}.issubset(elements_seen):
                return 0.0
            if carbon_count < 20 or not any_nonzero:
                return 0.0
            if total_atoms < 100:   # a realistic snapshot should have many atoms
                return 0.0
        except Exception:
            return 0.0
        return 1.0


# === block: score_1 (check id='charges_end_charges_recompute') ===
def score_1(artifact, step, ctx):
        if not ctx.get("csv_valid"):
            return 0.0
        ql = ctx["q_left_avg"]
        qr = ctx["q_right_avg"]
        targets = step.get("targets", {})
        gold_left = targets.get("Q_left_e", 0.134)
        gold_right = targets.get("Q_right_e", -0.005)
        tol = targets.get("tolerance_abs_e", 0.02)
        score_ql = 1.0 if abs(ql - gold_left) <= tol else 0.0
        score_qr = 1.0 if abs(qr - gold_right) <= tol else 0.0
        return (score_ql + score_qr) / 2.0


# === block: score_2 (check id='json_terminals') ===
def score_2(artifact, step, ctx):
        json_path = os.path.join(outputs_dir, step["output_file"])
        if not os.path.exists(json_path):
            return 0.0
        try:
            with open(json_path) as f:
                data = json.load(f)
            if not isinstance(data, dict):
                return 0.0
            required_keys = {"delta_U_mV", "Q_left_e", "Q_right_e", "description"}
            if not required_keys.issubset(data.keys()):
                return 0.0
            targets = step.get("targets", {})
            T_delta = targets.get("delta_U_mV", 17.2)
            tol_delta = targets.get("delta_U_tol_mV", 3.0)
            T_Qleft = targets.get("Q_left_e", 0.134)
            T_Qright = targets.get("Q_right_e", -0.005)
            tol_Q = targets.get("Q_tol_e", 0.02)
            delta = float(data["delta_U_mV"])
            Ql = float(data["Q_left_e"])
            Qr = float(data["Q_right_e"])
            sc_delta = 1.0 if abs(delta - T_delta) <= tol_delta else 0.0
            sc_Ql = 1.0 if abs(Ql - T_Qleft) <= tol_Q else 0.0
            sc_Qr = 1.0 if abs(Qr - T_Qright) <= tol_Q else 0.0
            return 0.6 * sc_delta + 0.2 * sc_Ql + 0.2 * sc_Qr
        except Exception:
            return 0.0


# === block: score_3 (check id='consistency_json_vs_csv') ===
def score_3(artifact, step, ctx):
        if not ctx.get("csv_valid"):
            return 0.0
        json_path = os.path.join(outputs_dir, step["output_file"])
        if not os.path.exists(json_path):
            return 0.0
        try:
            with open(json_path) as f:
                data = json.load(f)
            if not isinstance(data, dict):
                return 0.0
            required_keys = {"delta_U_mV", "Q_left_e", "Q_right_e"}
            if not required_keys.issubset(data.keys()):
                return 0.0
            reported_Ql = float(data["Q_left_e"])
            reported_Qr = float(data["Q_right_e"])
            reported_delta = float(data["delta_U_mV"])
            tols = step.get("consistency_tols", {})
            tol_Q = tols.get("Q_tol_e", 0.01)
            tol_delta = tols.get("delta_U_tol_mV", 5.0)
            match_Ql = abs(reported_Ql - ctx["q_left_avg"]) <= tol_Q
            match_Qr = abs(reported_Qr - ctx["q_right_avg"]) <= tol_Q
            match_delta = abs(reported_delta - ctx["delta_u_approx"]) <= tol_delta
            return 1.0 if match_Ql and match_Qr and match_delta else 0.0
        except Exception:
            return 0.0


_SCORERS = {
    'charges_csv_structure': score_0,
    'charges_end_charges_recompute': score_1,
    'json_terminals': score_2,
    'consistency_json_vs_csv': score_3,
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
