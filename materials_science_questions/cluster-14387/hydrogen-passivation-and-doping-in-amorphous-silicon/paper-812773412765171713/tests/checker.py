import os
import json
import csv

# === author imports / helpers ===
import math


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


# === block: score_0 (check id='defect_data') ===
def score_0(artifact, step, ctx):
        rows = artifact
        delta_min = step.get("delta_E_min", 0.13)
        delta_max = step.get("delta_E_max", 0.75)
        vol_max = step.get("volume_max", 0.7)
        corr_th = step.get("correlation_threshold", -0.3)
        min_sites = step.get("min_sites", 6)
        w_delta = step.get("sub_weight_delta", 0.3)
        w_charge = step.get("sub_weight_charge", 0.2)
        w_volume = step.get("sub_weight_volume", 0.2)
        w_corr = step.get("sub_weight_corr", 0.3)
        required_cols = {"H_site_id", "delta_E_eV", "e_d_star_original", "e_d_star_defect", "volume_change_percent", "avg_bond_angle_deg"}
        if not isinstance(rows, list) or len(rows) < min_sites:
            return 0.0
        for row in rows:
            if not required_cols.issubset(row.keys()):
                return 0.0
        delta_E = []
        e_orig = []
        e_def = []
        vol_change = []
        angles = []
        for row in rows:
            try:
                de = float(row["delta_E_eV"])
                eo = float(row["e_d_star_original"])
                ed = float(row["e_d_star_defect"])
                vc = float(row["volume_change_percent"])
                ang = float(row["avg_bond_angle_deg"])
            except (ValueError, TypeError):
                return 0.0
            delta_E.append(de)
            e_orig.append(eo)
            e_def.append(ed)
            vol_change.append(vc)
            angles.append(ang)
        n = len(rows)
        # 1. delta_E range
        delta_ok = sum(1 for de in delta_E if delta_min <= de <= delta_max)
        score_delta = delta_ok / n if n > 0 else 0.0
        # 2. charge increase
        charge_ok = sum(1 for eo, ed in zip(e_orig, e_def) if ed > eo)
        score_charge = charge_ok / n if n > 0 else 0.0
        # 3. volume range
        vol_ok = sum(1 for v in vol_change if 0.0 <= v <= vol_max)
        score_volume = vol_ok / n if n > 0 else 0.0
        # 4. Pearson correlation
        if n < 2:
            score_corr = 0.0
        else:
            mean_de = sum(delta_E) / n
            mean_ang = sum(angles) / n
            cov = 0.0
            var_de = 0.0
            var_ang = 0.0
            for de, ang in zip(delta_E, angles):
                cov += (de - mean_de) * (ang - mean_ang)
                var_de += (de - mean_de) ** 2
                var_ang += (ang - mean_ang) ** 2
            cov /= (n - 1)
            std_de = math.sqrt(var_de / (n - 1))
            std_ang = math.sqrt(var_ang / (n - 1))
            if std_de == 0 or std_ang == 0:
                r = 0.0
            else:
                r = cov / (std_de * std_ang)
            if r <= corr_th:
                score_corr = 1.0
            elif r < 0:
                # negative but weaker: partial credit
                score_corr = -r / -corr_th
            else:
                score_corr = 0.0
        total = (w_delta * score_delta + w_charge * score_charge + w_volume * score_volume + w_corr * score_corr) / (w_delta + w_charge + w_volume + w_corr)
        return total


# === block: score_1 (check id='barrier') ===
def score_1(artifact, step, ctx):
        d = artifact
        if not isinstance(d, dict) or "barrier_eV" not in d:
            return 0.0
        try:
            barrier = float(d["barrier_eV"])
        except (ValueError, TypeError):
            return 0.0
        barrier_min = step.get("barrier_min", 1.5)
        if barrier < 0:
            return 0.0
        if barrier >= barrier_min:
            return 1.0
        else:
            return max(0.0, min(1.0, barrier / barrier_min))


_SCORERS = {
    'defect_data': score_0,
    'barrier': score_1,
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
