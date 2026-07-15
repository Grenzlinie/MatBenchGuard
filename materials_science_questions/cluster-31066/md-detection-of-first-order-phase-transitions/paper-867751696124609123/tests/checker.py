import os
import json
import csv

# === author imports / helpers ===
import json, csv, math, os, collections


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
    def prepare(outputs_dir, spec):
        ctx = {}
        csv_path = os.path.join(outputs_dir, "step_02_kappa_T_data.csv")
        json_path = os.path.join(outputs_dir, "step_03_phase_boundary.json")
        # Load CSV
        data = []
        try:
            with open(csv_path) as f:
                reader = csv.DictReader(f)
                for row in reader:
                    data.append({
                        'isotope': row['isotope'].strip(),
                        'pressure_GPa': float(row['pressure_GPa']),
                        'volume_A3_per_atom': float(row['volume_A3_per_atom']),
                        'kappa_T_GPa-1': float(row['kappa_T_GPa-1'])
                    })
        except Exception:
            ctx['data'] = None
            ctx['peaks'] = {}
            ctx['recomputed_shift'] = None
            ctx['reported_shift'] = None
            return ctx
        # Group by isotope
        groups = collections.defaultdict(list)
        for d in data:
            groups[d['isotope']].append(d)
        peaks = {}
        for iso, entries in groups.items():
            entries.sort(key=lambda x: x['pressure_GPa'])
            pressures = [e['pressure_GPa'] for e in entries]
            volumes = [e['volume_A3_per_atom'] for e in entries]
            kappas = []
            n = len(pressures)
            for i in range(n):
                V = volumes[i]
                P = pressures[i]
                if n == 1:
                    kappas.append(0.0)
                    continue
                if i == 0:
                    dV = volumes[1] - volumes[0]
                    dP = pressures[1] - pressures[0]
                elif i == n - 1:
                    dV = volumes[-1] - volumes[-2]
                    dP = pressures[-1] - pressures[-2]
                else:
                    dV = volumes[i+1] - volumes[i-1]
                    dP = pressures[i+1] - pressures[i-1]
                if dP == 0:
                    kappa = float('inf')
                else:
                    kappa = - (dV / dP) / V
                kappas.append(kappa)
            # Find peak index
            finite_kappas = [k if math.isfinite(k) else -float('inf') for k in kappas]
            imax = max(range(n), key=lambda i: finite_kappas[i])
            if imax == 0 or imax == n-1 or n < 3:
                peak_p = pressures[imax]
            else:
                p = pressures
                k = kappas
                p0, p1, p2 = p[imax-1], p[imax], p[imax+1]
                k0, k1, k2 = k[imax-1], k[imax], k[imax+1]
                denom = (p0 - p1)*(p0 - p2)*(p1 - p2)
                if abs(denom) < 1e-12:
                    peak_p = p1
                else:
                    a = (p0*(k2 - k1) + p1*(k0 - k2) + p2*(k1 - k0)) / denom
                    b = (p0*p0*(k1 - k2) + p1*p1*(k2 - k0) + p2*p2*(k0 - k1)) / denom
                    if abs(a) < 1e-12:
                        peak_p = p1
                    else:
                        peak_p = -b / (2*a)
                        peak_p = max(p0, min(p2, peak_p))
            peaks[iso] = peak_p
        recomputed_shift = None
        if 'H2' in peaks and 'D2' in peaks:
            recomputed_shift = peaks['D2'] - peaks['H2']
        # Load reported JSON
        reported_shift = None
        try:
            with open(json_path) as f:
                reported = json.load(f)
                reported_shift = reported.get('isotope_shift_GPa', None)
        except:
            pass
        ctx['data'] = data
        ctx['peaks'] = peaks
        ctx['recomputed_shift'] = recomputed_shift
        ctx['reported_shift'] = reported_shift
        return ctx


# === block: score_0 (check id='step_02_schema') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        return 1.0 if ctx.get('data') is not None and len(ctx['data']) > 0 else 0.0


# === block: score_1 (check id='step_03_shift') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        shift = ctx.get('recomputed_shift')
        if shift is None:
            return 0.0
        gold = 27.0
        tol = 5.0
        max_dev = 15.0
        dev = abs(shift - gold)
        if dev <= tol:
            return 1.0
        elif dev >= max_dev:
            return 0.0
        else:
            return 1.0 - (dev - tol) / (max_dev - tol)


# === block: score_2 (check id='step_03_consistency') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        rep = ctx.get('reported_shift')
        rec = ctx.get('recomputed_shift')
        if rep is None or rec is None:
            return 0.0
        if abs(rep - rec) <= 8.0:
            return 1.0
        else:
            return 0.0


_SCORERS = {
    'step_02_schema': score_0,
    'step_03_shift': score_1,
    'step_03_consistency': score_2,
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
