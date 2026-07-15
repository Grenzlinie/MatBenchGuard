import os
import json
import csv

# === author imports / helpers ===
import csv, json, math, os


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
        # extract pdos step targets
        step2_cfg = None
        for s in spec.get("steps", []):
            if s["id"] == "step2_pdos":
                step2_cfg = s
                break
        targets = step2_cfg.get("targets", {}) if step2_cfg else {}
        ctx = {
            "s_target": targets.get("s_occupancy_target", 2.1),
            "s_tol": targets.get("s_tolerance_half", 0.25),
            "net_target": targets.get("net_charge_target", 0.6),
            "net_tol": targets.get("net_charge_tolerance_half", 0.2),
        }
        return ctx


# === block: score_0 (check id='step2_pdos') ===
def score_0(artifact, step, ctx):
        rows = artifact
        if not rows or any(col not in rows[0] for col in ['energy','s','px','py','pz']):
            return 0.0
        try:
            energies = []
            s_dos = []
            px_dos = []
            py_dos = []
            pz_dos = []
            for r in rows:
                energies.append(float(r['energy']))
                s_dos.append(float(r['s']))
                px_dos.append(float(r['px']))
                py_dos.append(float(r['py']))
                pz_dos.append(float(r['pz']))
        except (ValueError, KeyError):
            return 0.0
        combined = sorted(zip(energies, s_dos, px_dos, py_dos, pz_dos), key=lambda x: x[0])
        if not combined:
            return 0.0
        energies = [c[0] for c in combined]
        s_dos = [c[1] for c in combined]
        px_dos = [c[2] for c in combined]
        py_dos = [c[3] for c in combined]
        pz_dos = [c[4] for c in combined]
        if not (energies[0] <= 0 <= energies[-1]):
            return 0.0
        def integrate(x, y, limit):
            total = 0.0
            for i in range(len(x)-1):
                if x[i] >= limit:
                    break
                x1, x2 = x[i], x[i+1]
                y1, y2 = y[i], y[i+1]
                if x2 <= limit:
                    total += 0.5 * (y1 + y2) * (x2 - x1)
                else:
                    if x2 - x1 != 0:
                        ylim = y1 + (limit - x1) * (y2 - y1) / (x2 - x1)
                        total += 0.5 * (y1 + ylim) * (limit - x1)
                    break
            return total
        s_occ = integrate(energies, s_dos, 0.0)
        px_occ = integrate(energies, px_dos, 0.0)
        py_occ = integrate(energies, py_dos, 0.0)
        pz_occ = integrate(energies, pz_dos, 0.0)
        p_occ = px_occ + py_occ + pz_occ
        net = 3.0 - (s_occ + p_occ)
        s_targ = ctx['s_target']
        s_tol = ctx['s_tol']
        net_targ = ctx['net_target']
        net_tol = ctx['net_tol']
        s_score = max(0.0, 1.0 - abs(s_occ - s_targ) / s_tol)
        net_score = max(0.0, 1.0 - abs(net - net_targ) / net_tol)
        pz_dom = 1.0 if pz_occ > px_occ and pz_occ > py_occ else 0.0
        return round(0.4 * s_score + 0.4 * net_score + 0.2 * pz_dom, 6)


# === block: score_1 (check id='step3_results') ===
def score_1(artifact, step, ctx):
        rep = artifact
        if not isinstance(rep, dict):
            return 0.0
        try:
            rep_s = float(rep.get('s_occupancy'))
            rep_p = float(rep.get('p_occupancy'))
            rep_net = float(rep.get('net_charge_transfer'))
        except (TypeError, ValueError):
            return 0.0
        pdos_path = '/app/outputs/pdos.csv'
        if not os.path.exists(pdos_path):
            return 0.0
        with open(pdos_path, newline='') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        if not rows:
            return 0.0
        try:
            energies = [float(r['energy']) for r in rows]
            s_dos = [float(r['s']) for r in rows]
            px_dos = [float(r['px']) for r in rows]
            py_dos = [float(r['py']) for r in rows]
            pz_dos = [float(r['pz']) for r in rows]
        except:
            return 0.0
        combined = sorted(zip(energies, s_dos, px_dos, py_dos, pz_dos), key=lambda x: x[0])
        energies = [c[0] for c in combined]
        s_dos = [c[1] for c in combined]
        px_dos = [c[2] for c in combined]
        py_dos = [c[3] for c in combined]
        pz_dos = [c[4] for c in combined]
        def integrate(x, y, limit):
            total = 0.0
            for i in range(len(x)-1):
                if x[i] >= limit:
                    break
                x1, x2 = x[i], x[i+1]
                y1, y2 = y[i], y[i+1]
                if x2 <= limit:
                    total += 0.5*(y1+y2)*(x2-x1)
                else:
                    if x2 - x1 != 0:
                        ylim = y1 + (limit - x1)*(y2 - y1)/(x2 - x1)
                        total += 0.5*(y1 + ylim)*(limit - x1)
                    break
            return total
        s_occ = integrate(energies, s_dos, 0.0)
        px_occ = integrate(energies, px_dos, 0.0)
        py_occ = integrate(energies, py_dos, 0.0)
        pz_occ = integrate(energies, pz_dos, 0.0)
        p_occ = px_occ + py_occ + pz_occ
        net = 3.0 - (s_occ + p_occ)
        tol = step.get('tolerance_abs', 0.05)
        ok = abs(rep_s - s_occ) <= tol and abs(rep_p - p_occ) <= tol and abs(rep_net - net) <= tol
        return 1.0 if ok else 0.0


_SCORERS = {
    'step2_pdos': score_0,
    'step3_results': score_1,
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
