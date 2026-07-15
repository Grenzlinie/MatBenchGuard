import os
import json
import csv

# === author imports / helpers ===
import csv
import json
import os
import math

def find_band_edges(energies, dos, threshold_frac=0.05):
    data = sorted(zip(energies, dos), key=lambda x: x[0])
    if not data:
        return None, None
    sorted_e = [d[0] for d in data]
    sorted_dos = [d[1] for d in data]
    fermi_i = min(range(len(sorted_e)), key=lambda i: abs(sorted_e[i]))
    max_dos = max(sorted_dos)
    threshold = max_dos * threshold_frac if max_dos > 0 else 1e-6
    vbm = None
    for i in range(fermi_i, -1, -1):
        if sorted_dos[i] > threshold:
            vbm = sorted_e[i]
            break
    cbm = None
    for i in range(fermi_i, len(sorted_e)):
        if sorted_dos[i] > threshold:
            cbm = sorted_e[i]
            break
    return vbm, cbm


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
    rows = []
    csv_path = os.path.join(outputs_dir, "step_02_dos_data.csv")
    if os.path.exists(csv_path):
        with open(csv_path, newline='') as f:
            reader = csv.DictReader(f)
            for r in reader:
                rows.append(r)
    data_by_sys = {}
    for r in rows:
        sys = r.get("system", "").strip()
        if sys not in ["VTi", "VAl"]:
            continue
        try:
            e = float(r["energy_eV"])
            td = float(r["total_dos"])
            pd_v = float(r["pdos_V"])
            pd_os = float(r["pdos_O_support"])
            pd_ov = float(r["pdos_O_vana"])
            if sys not in data_by_sys:
                data_by_sys[sys] = {"energy": [], "total": [], "pdos_V": [], "pdos_O_sup": [], "pdos_O_van": []}
            data_by_sys[sys]["energy"].append(e)
            data_by_sys[sys]["total"].append(td)
            data_by_sys[sys]["pdos_V"].append(pd_v)
            data_by_sys[sys]["pdos_O_sup"].append(pd_os)
            data_by_sys[sys]["pdos_O_van"].append(pd_ov)
        except (ValueError, KeyError):
            continue
    ctx = {"dos_data": data_by_sys}
    return ctx


# === block: score_0 (check id='step_bandgap') ===
def score_0(artifact, step, ctx):
    import math

    def _robust_band_edges(energies, dos, threshold_frac=0.02):
        if not energies or not dos:
            return None, None
        data = sorted(zip(energies, dos), key=lambda x: x[0])
        sorted_e = [d[0] for d in data]
        sorted_dos = [d[1] for d in data]
        n = len(sorted_e)
        # index closest to Fermi (0 eV)
        fermi_idx = 0
        min_abs = float('inf')
        for i, e in enumerate(sorted_e):
            if abs(e) < min_abs:
                min_abs = abs(e)
                fermi_idx = i
        max_dos = max(sorted_dos) if sorted_dos else 0.0
        if max_dos <= 0:
            return None, None
        threshold = max_dos * threshold_frac
        vbm = None
        for i in range(fermi_idx, -1, -1):
            if sorted_dos[i] > threshold:
                vbm = sorted_e[i]
                break
        cbm = None
        for i in range(fermi_idx, n):
            if sorted_dos[i] > threshold:
                cbm = sorted_e[i]
                break
        return vbm, cbm

    vti = ctx.get("dos_data", {}).get("VTi", {})
    val = ctx.get("dos_data", {}).get("VAl", {})
    if not vti or not val:
        return 0.0
    vti_vbm, vti_cbm = _robust_band_edges(vti["energy"], vti["total"])
    val_vbm, val_cbm = _robust_band_edges(val["energy"], val["total"])
    if vti_vbm is None or vti_cbm is None or val_vbm is None or val_cbm is None:
        return 0.0
    vti_gap = vti_cbm - vti_vbm
    val_gap = val_cbm - val_vbm
    if vti_gap < val_gap:
        return 1.0
    return 0.0


# === block: score_1 (check id='step_dos_data') ===
def score_1(artifact, step, ctx):
    dos = ctx.get("dos_data", {})
    has_vti = "VTi" in dos and len(dos["VTi"]["energy"]) > 0
    has_val = "VAl" in dos and len(dos["VAl"]["energy"]) > 0
    if not has_vti or not has_val:
        return 0.0
    for sys_data in dos.values():
        if any(d < 0 for d in sys_data["total"]):
            return 0.0
    return 1.0


# === block: score_2 (check id='step_cb_offset') ===
def score_2(artifact, step, ctx):
    vti = ctx.get("dos_data", {}).get("VTi", {})
    val = ctx.get("dos_data", {}).get("VAl", {})
    if not vti or not val:
        return 0.0
    vti_vanados = [v + o for v, o in zip(vti["pdos_V"], vti["pdos_O_van"])]
    val_vanados = [v + o for v, o in zip(val["pdos_V"], val["pdos_O_van"])]
    vti_cbm, _ = find_band_edges(vti["energy"], vti_vanados)
    val_cbm, _ = find_band_edges(val["energy"], val_vanados)
    if vti_cbm is None or val_cbm is None:
        return 0.0
    if vti_cbm < val_cbm:
        return 1.0
    return 0.0


_SCORERS = {
    'step_bandgap': score_0,
    'step_dos_data': score_1,
    'step_cb_offset': score_2,
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
