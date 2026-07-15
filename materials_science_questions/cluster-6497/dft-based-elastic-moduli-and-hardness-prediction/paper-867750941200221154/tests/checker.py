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


# === block: score_0 (check id='step_bandgap') ===
def score_0(artifact, step, ctx):
    # parse rows into lookup
        data = {}
        for row in artifact:
            try:
                rc = int(row['compression_ratio'])
                data[rc] = {'gap': float(row['band_gap_eV']), 'type': row['gap_type'].strip().lower()}
            except (KeyError, ValueError):
                return 0.0

        # sub-scores
        # a) direct at RC=0
        direct0 = 1.0 if (0 in data and data[0]['type'] == 'direct') else 0.0
        # b) metallic at RC=30
        metallic30 = 1.0 if (30 in data and data[30]['type'] == 'metallic') else 0.0
        # c) first non-direct transition at RC <= 10
        sorted_rc = sorted(data.keys())
        trans_rc = None
        for rc in sorted_rc:
            if data[rc]['type'] != 'direct':
                trans_rc = rc
                break
        trans_ok = 1.0 if (trans_rc is not None and trans_rc <= 10) else 0.0
        # d) monotonic decrease after maximum gap
        max_rc = max(data.keys(), key=lambda r: data[r]['gap'])
        rc_ordered = [r for r in sorted_rc if r >= max_rc]
        monotonic = True
        for i in range(1, len(rc_ordered)):
            if data[rc_ordered[i]]['gap'] > data[rc_ordered[i-1]]['gap'] + 0.01:
                monotonic = False
                break
        mono_ok = 1.0 if monotonic else 0.0
        # e) gap near zero at RC=30 (metallic already confirms closure)
        zero_gap = 1.0 if (30 in data and data[30]['type'] == 'metallic' and data[30]['gap'] <= 0.01) else 0.0

        total = (direct0 * 0.2 + metallic30 * 0.2 + trans_ok * 0.2 +
                 mono_ok * 0.3 + zero_gap * 0.1)
        return max(0.0, min(1.0, total))


# === block: score_1 (check id='step_transmission') ===
def score_1(artifact, step, ctx):
    # parse rows
        zigzag = {}
        armchair = {}
        for row in artifact:
            try:
                rc = int(row['compression_ratio'])
                zigzag[rc] = float(row['T_zigzag_24L'])
                armchair[rc] = float(row['T_armchair_24L'])
            except (KeyError, ValueError):
                return 0.0

        required = [0,5,10,15,20,25,30]
        # ------ zigzag scoring ------
        zigzag_score = 0.0
        if all(rc in zigzag for rc in required):
            flat_vals = [zigzag[rc] for rc in [0,5,10,15,20]]
            if min(flat_vals) > 0:
                ratio = max(flat_vals) / min(flat_vals)
                flat_ok = 1.0 if ratio <= 2.0 else 0.0
            else:
                flat_ok = 0.0
            inc25 = 1.0 if zigzag[25] >= zigzag[20] * 1.5 else 0.0
            inc30 = 1.0 if zigzag[30] >= zigzag[20] * 2.0 else 0.0
            rise_seq = 1.0 if zigzag[25] < zigzag[30] else 0.0
            zigzag_score = flat_ok * 0.4 + inc25 * 0.25 + inc30 * 0.25 + rise_seq * 0.1

        # ------ armchair scoring ------
        armchair_score = 0.0
        if all(rc in armchair for rc in required):
            # valley near 15%
            min150 = 1.0 if armchair[15] <= armchair[10] and armchair[15] <= armchair[20] else 0.0
            dec015 = 1.0 if armchair[15] < armchair[0] else 0.0
            inc1520 = 1.0 if armchair[20] > armchair[15] else 0.0
            inc20_30 = 1.0 if armchair[30] >= armchair[20] * 2.0 else 0.0
            rising_seq = 1.0 if armchair[30] > armchair[25] > armchair[20] else 0.0
            armchair_score = (min150 * 0.2 + dec015 * 0.2 + inc1520 * 0.2 +
                              inc20_30 * 0.2 + rising_seq * 0.2)

        total = (zigzag_score + armchair_score) / 2.0
        return max(0.0, min(1.0, total))


_SCORERS = {
    'step_bandgap': score_0,
    'step_transmission': score_1,
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
