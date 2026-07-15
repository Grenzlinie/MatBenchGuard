import os
import json
import csv

# === author imports / helpers ===
import numpy as np


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
    import json
    freq_path = os.path.join(outputs_dir, "step_01_natural_frequencies.json")
    freq_val = None
    try:
        with open(freq_path) as f:
            data = json.load(f)
            freq_val = data.get("mode1_freq_hz")
    except Exception:
        pass
    return {"freq_hz": freq_val}


# === block: score_0 (check id='freq_check') ===
def score_0(artifact, step, ctx):
    gold = step.get("gold_hz", None)
    if gold is None:
        return 0.0
    val = artifact.get("mode1_freq_hz", None)
    if not isinstance(val, (int, float)):
        return 0.0
    tol_rel = step.get("tol_rel", 0.01)
    rel_err = abs(val - gold) / gold
    if rel_err <= tol_rel:
        return 1.0
    else:
        return max(0.0, 1.0 - (rel_err - tol_rel) / (4 * tol_rel))


# === block: score_1 (check id='dyn_check') ===
def score_1(artifact, step, ctx):
    if not artifact or len(artifact) == 0:
        return 0.0
    gains = {}
    for row in artifact:
        g = row.get("gain", "")
        if g not in gains:
            gains[g] = {"t": [], "def": []}
        try:
            t = float(row["time_s"])
            d = float(row["deflection_mm"])
        except (ValueError, TypeError):
            continue
        gains[g]["t"].append(t)
        gains[g]["def"].append(d)
    if "Gv0" not in gains or "Gv0.01" not in gains:
        return 0.0
    peak_un = max(abs(d) for d in gains["Gv0"]["def"])
    peak_ctrl = max(abs(d) for d in gains["Gv0.01"]["def"])
    if peak_un <= 0.0:
        return 0.0

    gold_un = step.get("gold_peak_un_mm", None)
    gold_ctrl = step.get("gold_peak_ctrl_mm", None)
    tol_peak = step.get("tol_peak", 0.05)

    score = 0.0
    if gold_un is not None and gold_ctrl is not None:
        w_mag_un = 0.35
        w_mag_ctrl = 0.25
        w_order = 0.1
        w_freq = 0.3
    
        rel_err_un = abs(peak_un - gold_un) / gold_un
        if rel_err_un <= tol_peak:
            score += w_mag_un
        else:
            score += w_mag_un * max(0.0, 1.0 - (rel_err_un - tol_peak) / (2 * tol_peak))
    
        rel_err_ctrl = abs(peak_ctrl - gold_ctrl) / gold_ctrl
        if rel_err_ctrl <= tol_peak:
            score += w_mag_ctrl
        else:
            score += w_mag_ctrl * max(0.0, 1.0 - (rel_err_ctrl - tol_peak) / (2 * tol_peak))
    
        if peak_ctrl < peak_un:
            score += w_order
    
        ref_freq = ctx.get("freq_hz", None)
        if ref_freq is not None and ref_freq > 0:
            t = np.array(gains["Gv0"]["t"])
            d = np.array(gains["Gv0"]["def"])
            if len(t) >= 10:
                dt = np.mean(np.diff(t))
                n = len(d)
                fft = np.fft.rfft(d)
                freqs = np.fft.rfftfreq(n, d=dt)
                idx = np.argmax(np.abs(fft[1:])) + 1
                dominant_freq = freqs[idx]
                if dominant_freq > 0:
                    rel_err_freq = abs(dominant_freq - ref_freq) / ref_freq
                    if rel_err_freq <= 0.05:
                        score += w_freq
                    else:
                        score += w_freq * max(0.0, 1.0 - (rel_err_freq - 0.05) / 0.1)
                else:
                    score += 0.5 * w_freq
            else:
                score += 0.5 * w_freq
        else:
            pass
    else:
        w_order = 0.5
        w_freq = 0.5
        if peak_ctrl < peak_un:
            score += w_order
        ref_freq = ctx.get("freq_hz", None)
        if ref_freq is not None and ref_freq > 0:
            t = np.array(gains["Gv0"]["t"])
            d = np.array(gains["Gv0"]["def"])
            if len(t) >= 10:
                dt = np.mean(np.diff(t))
                n = len(d)
                fft = np.fft.rfft(d)
                freqs = np.fft.rfftfreq(n, d=dt)
                idx = np.argmax(np.abs(fft[1:])) + 1
                dominant_freq = freqs[idx]
                if dominant_freq > 0:
                    rel_err = abs(dominant_freq - ref_freq) / ref_freq
                    if rel_err <= 0.05:
                        score += w_freq
                    else:
                        score += w_freq * max(0.0, 1.0 - (rel_err - 0.05) / 0.1)
                else:
                    score += 0.5 * w_freq
            else:
                score += 0.5 * w_freq
        else:
            pass

    return min(score, 1.0)


_SCORERS = {
    'freq_check': score_0,
    'dyn_check': score_1,
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
