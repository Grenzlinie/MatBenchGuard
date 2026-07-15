import os
import json
import csv


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


# === block: score_0 (check id='step_hist_initial') ===
def score_0(artifact, step, ctx):
        rows = artifact
        z = []
        vf = []
        for row in rows:
            try:
                z.append(float(row['z_bin_center']))
                vf.append(float(row['volume_fraction']))
            except (ValueError, KeyError):
                return 0.0
        if not z:
            return 0.0
        sorted_idx = sorted(range(len(z)), key=lambda i: z[i])
        sorted_z = [z[i] for i in sorted_idx]
        sorted_vf = [vf[i] for i in sorted_idx]
        n = len(sorted_z)
        z_min = sorted_z[0]
        z_max = sorted_z[-1]
        z_mid_low = z_min + 0.25 * (z_max - z_min)
        z_mid_high = z_min + 0.75 * (z_max - z_min)
        middle_vf = [v for zv, v in zip(sorted_z, sorted_vf) if z_mid_low <= zv <= z_mid_high]
        if not middle_vf:
            return 0.0
        avg_mid = sum(middle_vf) / len(middle_vf)
        edge_indices = list(range(min(3, n))) + list(range(max(0, n-3), n))
        edge_vf = [sorted_vf[i] for i in edge_indices if i < n]
        if not edge_vf:
            return 0.0
        max_edge_vf = max(edge_vf)
        peak_ratio = max_edge_vf / avg_mid if avg_mid > 0 else 0.0
        peak_threshold = step.get('params', {}).get('peak_factor_threshold', 2.0)
        depth_min = step.get('params', {}).get('depth_min_nm', 20)
        depth_max = step.get('params', {}).get('depth_max_nm', 100)
        depletion_factor = step.get('params', {}).get('depletion_factor', 0.8)
        depletion_exists = False
        for zv, vv in zip(sorted_z, sorted_vf):
            if (depth_min <= zv <= depth_max) or (z_max - depth_max <= zv <= z_max - depth_min):
                if vv <= depletion_factor * avg_mid:
                    depletion_exists = True
                    break
        peak_ok = peak_ratio < peak_threshold
        depl_ok = not depletion_exists
        return 1.0 if peak_ok and depl_ok else 0.0


# === block: score_1 (check id='step_hist_evolved') ===
def score_1(artifact, step, ctx):
        rows = artifact
        z = []
        vf = []
        for row in rows:
            try:
                z.append(float(row['z_bin_center']))
                vf.append(float(row['volume_fraction']))
            except (ValueError, KeyError):
                return 0.0
        if not z:
            return 0.0
        sorted_idx = sorted(range(len(z)), key=lambda i: z[i])
        sorted_z = [z[i] for i in sorted_idx]
        sorted_vf = [vf[i] for i in sorted_idx]
        n = len(sorted_z)
        z_min = sorted_z[0]
        z_max = sorted_z[-1]
        z_mid_low = z_min + 0.25 * (z_max - z_min)
        z_mid_high = z_min + 0.75 * (z_max - z_min)
        middle_vf = [v for zv, v in zip(sorted_z, sorted_vf) if z_mid_low <= zv <= z_mid_high]
        if not middle_vf:
            return 0.0
        avg_mid = sum(middle_vf) / len(middle_vf)
        edge_indices = list(range(min(3, n))) + list(range(max(0, n-3), n))
        edge_vf_vals = [sorted_vf[i] for i in edge_indices if i < n]
        if not edge_vf_vals:
            return 0.0
        max_edge_vf = max(edge_vf_vals)
        max_edge_z = None
        for i in edge_indices:
            if i < n and sorted_vf[i] == max_edge_vf:
                max_edge_z = sorted_z[i]
                break
        peak_factor = step.get('params', {}).get('peak_factor', 2.0)
        depth_min = step.get('params', {}).get('depth_min_nm', 20)
        depth_max = step.get('params', {}).get('depth_max_nm', 100)
        depletion_factor = step.get('params', {}).get('depletion_factor', 0.8)
        depletion_exists = False
        depletion_z = None
        for zv, vv in zip(sorted_z, sorted_vf):
            if (depth_min <= zv <= depth_max) or (z_max - depth_max <= zv <= z_max - depth_min):
                if vv <= depletion_factor * avg_mid:
                    depletion_exists = True
                    depletion_z = zv
                    break
        peak_condition = (max_edge_vf / avg_mid if avg_mid > 0 else 0.0) >= peak_factor
        total = 0.0
        if peak_condition:
            total += 0.4
        if depletion_exists:
            total += 0.4
        if peak_condition and depletion_exists and max_edge_z is not None and depletion_z is not None:
            if max_edge_z < (z_min + z_max) / 2.0:
                if depletion_z < (z_min + z_max) / 2.0 and max_edge_z < depletion_z:
                    total += 0.2
            else:
                if depletion_z > (z_min + z_max) / 2.0 and max_edge_z > depletion_z:
                    total += 0.2
        return total


_SCORERS = {
    'step_hist_initial': score_0,
    'step_hist_evolved': score_1,
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
