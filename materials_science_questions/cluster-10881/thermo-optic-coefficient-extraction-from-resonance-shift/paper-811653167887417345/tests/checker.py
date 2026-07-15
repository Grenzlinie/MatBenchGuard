import os
import json
import csv

# === author imports / helpers ===
import json
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
        # Extract any shared config from grading_spec if needed; not used here.
        return {}


# === block: score_0 (check id='threshold_gt') ===
def score_0(artifact, step, ctx):
        # artifact is a string of a single float in scientific notation.
        try:
            val = float(artifact.strip())
        except ValueError:
            return 0.0
        gt = step['gold_threshold']
        tol_rel = step['tolerance_rel']
        if gt <= 0:
            return 1.0
        rel_err = abs(val - gt) / abs(gt)
        if rel_err <= tol_rel:
            return 1.0
        # Partial credit: linear decay up to 2*tol_rel
        decay = max(0.0, 1.0 - (rel_err - tol_rel) / tol_rel)
        return decay


# === block: score_1 (check id='reconstruction_stats') ===
def score_1(artifact, step, ctx):
        # artifact is a dict with 'nodes_retained_percent' and 'correlation_coefficient'
        nodes = artifact.get('nodes_retained_percent')
        corr = artifact.get('correlation_coefficient')
        if nodes is None or corr is None:
            return 0.0
        # nodes_retained: absolute tolerance around gold, widened to 5.0 percentage points
        gold_nodes = step['gold_nodes_retained']
        tol_abs = 5.0  # absorb legitimate toolchain spread
        if abs(nodes - gold_nodes) <= tol_abs:
            score_nodes = 1.0
        else:
            # decay based on absolute error; 0 at double tolerance
            err = abs(nodes - gold_nodes)
            score_nodes = max(0.0, 1.0 - (err - tol_abs) / tol_abs)
        # correlation: threshold_or_better, full if >= gold_correlation
        gold_corr = step['gold_correlation']
        if corr >= gold_corr:
            score_corr = 1.0
        else:
            # linear decay: 0 at corr = 0.0
            score_corr = max(0.0, corr / gold_corr)
        w = step['sub_weights']
        total = w['nodes_retained'] * score_nodes + w['correlation'] * score_corr
        return total


# === block: score_2 (check id='validation_peak') ===
def score_2(artifact, step, ctx):
        # artifact is a string with a float (mm)
        try:
            val = float(artifact.strip())
        except ValueError:
            return 0.0
        gold = step['gold_peak']
        tol = step['tolerance_abs']
        if abs(val - gold) <= tol:
            return 1.0
        # partial
        return max(0.0, 1.0 - (abs(val - gold) - tol) / tol)


# === block: score_3 (check id='wave_aberration') ===
def score_3(artifact, step, ctx):
        # artifact is a dict with rms_original, rms_reconstructed, relative_error_percent
        rms_o = artifact.get('rms_original')
        rms_r = artifact.get('rms_reconstructed')
        rel_rep = artifact.get('relative_error_percent')
        if rms_o is None or rms_r is None or rel_rep is None:
            return 0.0
        gold_o = step['gold_rms_original']
        gold_r = step['gold_rms_reconstructed']
        tol_rel = step['tolerance_rel_rms']
        # score rms_original
        if gold_o != 0:
            rel_o = abs(rms_o - gold_o) / abs(gold_o)
            score_o = 1.0 if rel_o <= tol_rel else max(0.0, 1.0 - (rel_o - tol_rel) / tol_rel)
        else:
            score_o = 1.0
        # score rms_reconstructed
        if gold_r != 0:
            rel_r = abs(rms_r - gold_r) / abs(gold_r)
            score_r = 1.0 if rel_r <= tol_rel else max(0.0, 1.0 - (rel_r - tol_rel) / tol_rel)
        else:
            score_r = 1.0
        # recompute relative error from submitted rms values
        if rms_o != 0:
            rel_err = 100.0 * abs(rms_o - rms_r) / abs(rms_o)
        else:
            rel_err = 0.0
        max_rel = step['max_relative_error_percent']
        if rel_err <= max_rel:
            score_rel = 1.0
        else:
            # decay: 0 at 2*max_rel
            score_rel = max(0.0, 1.0 - (rel_err - max_rel) / max_rel)
        w = step['sub_weights']
        total = w['rms_original'] * score_o + w['rms_reconstructed'] * score_r + w['relative_error'] * score_rel
        return total


_SCORERS = {
    'threshold_gt': score_0,
    'reconstruction_stats': score_1,
    'validation_peak': score_2,
    'wave_aberration': score_3,
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
