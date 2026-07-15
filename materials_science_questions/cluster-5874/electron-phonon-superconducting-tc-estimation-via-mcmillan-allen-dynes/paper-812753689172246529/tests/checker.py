import os
import json
import csv

# === author imports / helpers ===
import csv
import io
import os
import json

def _ff_validate_output_contract():
    """Return a list of shape violations against grading_spec['output_contract'].
    Handles headerless TSV/CSV when the contract says 'No header'."""
    spec_path = "/tests/grading_spec.json"
    if not os.path.exists(spec_path):
        return []
    with open(spec_path) as f:
        spec = json.load(f)
    contract = spec.get("output_contract", {}) or {}
    outputs = contract.get("outputs", []) or []
    out_dir = "/app/outputs"
    violations = []
    for out in outputs:
        base = str(out.get("file", "")).split("/")[-1]
        if not base:
            continue
        path = os.path.join(out_dir, base)
        if not os.path.isfile(path):
            violations.append("missing output_contract file: " + base)
            continue
        fmt = out.get("format", "")
        schema = out.get("schema", {}) or {}
        required_cols = schema.get("required_columns", []) or []
        if fmt == "json":
            try:
                data = json.load(open(path))
            except Exception as exc:
                violations.append(base + ": invalid JSON (" + str(exc) + ")")
                continue
            required = schema.get("required", {})
            fields = required.keys() if isinstance(required, dict) else (required or [])
            if isinstance(data, dict):
                for field in fields:
                    if field not in data:
                        violations.append(base + ": missing JSON field '" + str(field) + "'")
        elif fmt in ("csv", "tsv"):
            delim = "\t" if fmt == "tsv" else ","
            has_header = True  # default
            try:
                with open(path, newline="") as f:
                    reader = csv.reader(f, delimiter=delim)
                    first_row = next(reader, None)
                if first_row is None:
                    violations.append(base + ": empty or unreadable")
                    continue
                # If all required column names appear as strings in the first row, treat as header.
                # Otherwise treat as headerless.
                first_set = set(first_row)
                required_names = set(required_cols)
                if required_names and not required_names.issubset(first_set):
                    has_header = False
            except Exception as exc:
                violations.append(base + ": cannot read table (" + str(exc) + ")")
                continue
            if not required_cols:
                continue
            if has_header:
                if required_names and not required_names.issubset(first_set):
                    missing = required_names - first_set
                    violations.append(base + ": missing table column(s) " + str(missing))
            else:
                # headerless: check column count
                expected_n = len(required_cols)
                actual_n = len(first_row)
                if actual_n != expected_n:
                    violations.append(base + ": expected {} columns, got {}".format(expected_n, actual_n))
    return violations


def load_artifact(path):
    if not path or not os.path.exists(path):
        return None
    if path.endswith(".json"):
        try:
            with open(path) as f:
                return json.load(f)
        except Exception:
            return None
    if path.endswith(".csv") or path.endswith(".tsv"):
        delim = "\t" if path.endswith(".tsv") else ","
        # Determine required columns from contract schema
        spec_path = "/tests/grading_spec.json"
        required_cols = []
        if os.path.exists(spec_path):
            with open(spec_path) as f:
                spec = json.load(f)
            contract = spec.get("output_contract", {})
            outputs = contract.get("outputs", [])
            base = os.path.basename(path)
            for out in outputs:
                if out.get("file", "").split("/")[-1] == base:
                    schema = out.get("schema", {})
                    required_cols = schema.get("required_columns", [])
                    break
        with open(path, newline="") as f:
            reader = csv.reader(f, delimiter=delim)
            rows = list(reader)
        if not rows:
            return []
        first_row = rows[0]
        # decide if header row
        has_header = False
        if required_cols:
            if set(required_cols).issubset(set(first_row)):
                has_header = True
        if has_header:
            data_rows = rows[1:]
        else:
            data_rows = rows
        # Build dicts using required_cols as keys (fallback to positional indices if missing)
        keys = required_cols if len(required_cols) == len(first_row) else ["col{}".format(i) for i in range(len(first_row))]
        result = []
        for row in data_rows:
            d = {}
            for i, val in enumerate(row):
                if i < len(keys):
                    d[keys[i]] = val
            result.append(d)
        return result
    with open(path) as f:
        return f.read()


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


# === block: score_0 (check id='self_energy_check') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not artifact or len(artifact) < 10:
            return 0.0
        crit = step.get('criteria', {})
        phonon_ev = crit.get('phonon_energies_eV', [-0.016, -0.046])
        tol = crit.get('tolerance_eV', 0.005)
        dip_energy = crit.get('dip_energy_eV', -0.042)
        dip_max = crit.get('dip_ImSigma_max_eV', 0.0005)
        onset_thr = crit.get('onset_ImSigma_min_eV', 0.001)
        energies = []
        im_sigmas = []
        for row in artifact:
            try:
                e = float(row['energy'])
                s = float(row['ImSigma'])
                energies.append(e)
                im_sigmas.append(s)
            except (ValueError, KeyError):
                continue
        if not energies:
            return 0.0
        def window(arr, center, delta):
            return [i for i, v in enumerate(arr) if abs(v - center) <= delta]
        score = 0.0
        # onset at phonon 1
        idx1 = window(energies, phonon_ev[0], tol)
        if idx1 and max(im_sigmas[i] for i in idx1) > onset_thr:
            score += 0.25
        # onset at phonon 2
        idx2 = window(energies, phonon_ev[1], tol)
        if idx2 and max(im_sigmas[i] for i in idx2) > onset_thr:
            score += 0.25
        # dip
        idx_dip = window(energies, dip_energy, tol)
        if idx_dip and min(im_sigmas[i] for i in idx_dip) < dip_max:
            score += 0.5
        return min(score, 1.0)


# === block: score_1 (check id='spectral_function_check') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not artifact or len(artifact) < 10:
            return 0.0
        crit = step.get('criteria', {})
        phonon_ev = crit.get('phonon_energies_eV', [-0.016, -0.046])
        tol = crit.get('tolerance_eV', 0.005)
        min_peak_ratio = crit.get('min_peak_ratio', 0.2)
        bin_width = 0.002
        bin_sum = {}
        for row in artifact:
            try:
                e = float(row['energy'])
                w = float(row['spectral_weight'])
                bk = round(e / bin_width) * bin_width
                bin_sum[bk] = bin_sum.get(bk, 0.0) + w
            except (ValueError, KeyError):
                continue
        if not bin_sum:
            return 0.0
        # background: bins outside both phonon windows
        bg_vals = []
        for bk, val in bin_sum.items():
            in_window = any((p - tol) <= bk <= (p + tol) for p in phonon_ev)
            if not in_window:
                bg_vals.append(val)
        if not bg_vals:
            avg_bg = 0.0
        else:
            avg_bg = sum(bg_vals) / len(bg_vals)
        score = 0.0
        for p in phonon_ev:
            low = p - tol
            high = p + tol
            peak_val = max((val for bk, val in bin_sum.items() if low <= bk <= high), default=0.0)
            if avg_bg > 0 and peak_val / avg_bg > min_peak_ratio:
                score += 0.5
        return min(score, 1.0)


# === block: score_2 (check id='poles_check') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not artifact or not isinstance(artifact, list):
            return 0.0
        crit = step.get('criteria', {})
        required_n = crit.get('required_poles_per_k', 3)
        max_gamma = crit.get('max_Gamma_qp_near_kF_eV', 0.001)
        total_k = len(artifact)
        if total_k == 0:
            return 0.0
        # count of entries with correct number of poles
        correct_count = sum(1 for ent in artifact if len(ent.get('poles', [])) == required_n)
        cnt_score = correct_count / total_k
        # ordering: n=1 most negative, n=2, n=3
        ordered_count = 0
        for ent in artifact:
            poles = ent.get('poles', [])
            if len(poles) != required_n:
                continue
            try:
                # group by n (expected 1,2,3)
                by_n = {p['n']: p for p in poles}
                if all(k in by_n for k in [1,2,3]):
                    if by_n[1]['E_qp'] < by_n[2]['E_qp'] < by_n[3]['E_qp']:
                        ordered_count += 1
            except (KeyError, TypeError):
                continue
        ord_score = ordered_count / total_k
        # find k_F: entry where n=1 energy closest to zero
        best_dist = float('inf')
        best_entry = None
        for ent in artifact:
            for p in ent.get('poles', []):
                if p.get('n') == 1:
                    d = abs(p.get('E_qp', 0.0))
                    if d < best_dist:
                        best_dist = d
                        best_entry = ent
                    break
        long_lived = 0.0
        if best_entry:
            n2_vals = [p for p in best_entry.get('poles', []) if p.get('n') == 2]
            if n2_vals and n2_vals[0].get('Gamma_qp', 1.0) <= max_gamma:
                long_lived = 0.4
        total = 0.3 * cnt_score + 0.3 * ord_score + long_lived
        return min(total, 1.0)


_SCORERS = {
    'self_energy_check': score_0,
    'spectral_function_check': score_1,
    'poles_check': score_2,
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
