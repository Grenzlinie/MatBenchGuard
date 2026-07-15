import os
import json
import csv

# === author imports / helpers ===
import json


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
    ctx = {
        # ZO(3,6) gold
        "ground_state_ZO36": "AFM-G",
        "band_gap_ZO36": 155.2,
        "tol_band_gap_ZO36": 20.0,
        # ZA(3,8) gold
        "ground_state_ZA38": "FM",
        "band_gap_ZA38_tol": 1e-6,
        "total_mag_min_ZA38": 1.5,
        "total_mag_max_ZA38": 2.5,
    }
    return ctx


# === block: score_0 (check id='ZO36') ===
def score_0(artifact, step, ctx):
    try:
        data = artifact
        for key in ["ground_state","energy_NM","energy_FM","energy_AFMG","band_gap_meV","oxygen_moment_min","oxygen_moment_max"]:
            if key not in data:
                return 0.0
        # ground state
        s_gs = 1.0 if data["ground_state"] == ctx["ground_state_ZO36"] else 0.0
        # energy ordering: AFMG < NM and AFMG < FM
        try:
            e_nm = float(data["energy_NM"])
            e_fm = float(data["energy_FM"])
            e_afmg = float(data["energy_AFMG"])
            s_energy = 1.0 if e_afmg < min(e_nm, e_fm) else 0.0
        except:
            s_energy = 0.0
        # band gap
        try:
            bg = float(data["band_gap_meV"])
            if abs(bg - ctx["band_gap_ZO36"]) <= ctx["tol_band_gap_ZO36"]:
                s_gap = 1.0
            elif bg > 0:
                s_gap = 0.5
            else:
                s_gap = 0.0
        except:
            s_gap = 0.0
        # oxygen moment range
        try:
            o_min = float(data["oxygen_moment_min"])
            o_max = float(data["oxygen_moment_max"])
            if 0.1 <= o_min <= 0.4 and 0.1 <= o_max <= 0.4 and o_min <= o_max:
                s_mom = 1.0
            elif (0.1 <= o_min <= 0.4) or (0.1 <= o_max <= 0.4):
                s_mom = 0.5
            else:
                s_mom = 0.0
        except:
            s_mom = 0.0
        return 0.25 * s_gs + 0.25 * s_energy + 0.25 * s_gap + 0.25 * s_mom
    except:
        return 0.0


# === block: score_1 (check id='ZA38') ===
def score_1(artifact, step, ctx):
    try:
        data = artifact
        for key in ["ground_state","energy_NM","energy_FM","energy_AFMS","band_gap_meV","total_magnetization_muB"]:
            if key not in data:
                return 0.0
        s_gs = 1.0 if data["ground_state"] == ctx["ground_state_ZA38"] else 0.0
        try:
            e_nm = float(data["energy_NM"])
            e_fm = float(data["energy_FM"])
            e_afms = float(data["energy_AFMS"])
            s_energy = 1.0 if e_fm < min(e_nm, e_afms) else 0.0
        except:
            s_energy = 0.0
        try:
            bg = float(data["band_gap_meV"])
            s_gap = 1.0 if bg < ctx["band_gap_ZA38_tol"] else 0.0
        except:
            s_gap = 0.0
        try:
            mag = float(data["total_magnetization_muB"])
            s_mag = 1.0 if ctx["total_mag_min_ZA38"] <= mag <= ctx["total_mag_max_ZA38"] else 0.0
        except:
            s_mag = 0.0
        return 0.25 * s_gs + 0.25 * s_energy + 0.25 * s_gap + 0.25 * s_mag
    except:
        return 0.0


_SCORERS = {
    'ZO36': score_0,
    'ZA38': score_1,
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
