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
        phonon_path = os.path.join(outputs_dir, "phonon_modes.json")
        try:
            with open(phonon_path) as f:
                phonon = json.load(f)
            modes = phonon.get("phonon_modes", [])
            sum_intensities = sum(m.get("dielectric_intensity", 0) or 0 for m in modes if m.get("mode_type") == "IR")
        except Exception:
            modes = []
            sum_intensities = 0.0
        return {"phonon_modes": modes, "sum_intensities": sum_intensities}


# === block: score_0 (check id='band_gap') ===
def score_0(artifact, step, ctx):
        target = step.get("target", {})
        gold_indirect = target["indirect_gap"]
        gold_direct = target["direct_gap"]
        tol = target.get("tolerance", 0.15)
        indirect = artifact.get("indirect_gap")
        direct = artifact.get("direct_gap")
        def gap_score(val, gold):
            if val is None:
                return 0.0
            diff = abs(val - gold)
            if diff <= tol:
                return 1.0
            return max(0.0, 1.0 - (diff - tol) / (2 * tol))
        s1 = gap_score(indirect, gold_indirect)
        s2 = gap_score(direct, gold_direct)
        return (s1 + s2) / 2.0


# === block: score_1 (check id='phonon_modes') ===
def score_1(artifact, step, ctx):
        target = step.get("target", {})
        modes = artifact.get("phonon_modes", [])
        expected = target["mode_count"]
        tol_cnt = target.get("tolerance_count", 2)
        n = len(modes)
        if n < expected:
            cnt_score = max(0.0, 1.0 - (expected - n) / float(expected))
        elif n > expected + tol_cnt:
            cnt_score = max(0.0, 1.0 - (n - expected) / (2.0 * expected))
        else:
            cnt_score = 1.0
        dom_modes = target.get("dominant_modes", [])
        freq_tol_rel = target.get("frequency_tol_relative", 0.02)
        zstar_tol_rel = target.get("zstar_tol_relative", 0.1)
        int_tol_rel = target.get("intensity_tol_relative", 0.15)
        dom_scores = []
        for dm in dom_modes:
            freq_target = dm["TO_frequency"]
            sym_target = dm["symmetry"]
            zstar_target = dm["Z_star"]
            int_target = dm["dielectric_intensity"]
            candidates = [m for m in modes if m.get("symmetry") == sym_target and m.get("mode_type") == "IR"]
            best_score = 0.0
            for m in candidates:
                f = m.get("TO_frequency")
                z = m.get("Z_star")
                eps = m.get("dielectric_intensity")
                if f is None:
                    continue
                freq_err = abs(f - freq_target) / freq_target if freq_target != 0 else 1.0
                z_err = abs((z or 0) - zstar_target) / zstar_target if zstar_target != 0 else 1.0
                int_err = abs((eps or 0) - int_target) / int_target if int_target != 0 else 1.0
                if freq_err <= freq_tol_rel and z_err <= zstar_tol_rel and int_err <= int_tol_rel:
                    best_score = 1.0
                    break
                partial = max(0.0, 1.0 - freq_err)
                if partial > best_score:
                    best_score = partial
            dom_scores.append(best_score)
        dom_score = sum(dom_scores) / len(dom_scores) if dom_scores else 1.0
        sum_intensities = sum(m.get("dielectric_intensity", 0) or 0 for m in modes if m.get("mode_type") == "IR")
        gold_sum = target.get("sum_intensities_gold", 49.58)
        tol_sum = target.get("sum_intensities_tol_abs", 2.0)
        diff = abs(sum_intensities - gold_sum)
        if tol_sum > 0:
            sum_score = max(0.0, 1.0 - diff / (2.0 * tol_sum))
        else:
            sum_score = 1.0 if diff <= tol_sum else 0.0
        total = 0.2 * cnt_score + 0.5 * dom_score + 0.3 * sum_score
        return total


# === block: score_2 (check id='dielectric_tensor') ===
def score_2(artifact, step, ctx):
        target = step.get("target", {})
        rel_tol = target.get("relative_tolerance", 0.05)
        gold = target
        comp_scores = []
        for tensor_name in ["epsilon_infinity", "epsilon_ionic", "epsilon_0"]:
            gold_tensor = gold.get(tensor_name, {})
            agent_tensor = artifact.get(tensor_name, {})
            for key in ["xx", "yy", "zz", "average"]:
                gv = gold_tensor.get(key)
                av = agent_tensor.get(key)
                if gv is None or av is None:
                    comp_scores.append(0.0)
                else:
                    err = abs(av - gv) / abs(gv) if gv != 0 else 1.0
                    if err <= rel_tol:
                        comp_scores.append(1.0)
                    else:
                        comp_scores.append(max(0.0, 1.0 - (err - rel_tol) / (2 * rel_tol)))
        comp_score = sum(comp_scores) / len(comp_scores) if comp_scores else 0.0
        cons_score = 1.0
        try:
            e_inf = artifact.get("epsilon_infinity", {})
            e_ion = artifact.get("epsilon_ionic", {})
            e0 = artifact.get("epsilon_0", {})
            sum_err = 0.0
            for key in ["xx", "yy", "zz"]:
                v_inf = e_inf.get(key, None)
                v_ion = e_ion.get(key, None)
                v0 = e0.get(key, None)
                if None in (v_inf, v_ion, v0):
                    sum_err += 1.0
                else:
                    sum_err += abs(v0 - (v_inf + v_ion)) / (abs(v_inf) + abs(v_ion) + 1e-6)
            cons_score = max(0.0, 1.0 - sum_err / 3.0)
            ctx_sum = ctx.get("sum_intensities", None)
            if ctx_sum is not None and e_ion.get("average") is not None:
                ref_avg = ctx_sum / 3.0
                diff_avg = abs(e_ion["average"] - ref_avg) / (abs(ref_avg) + 1e-6)
                cons_score = min(cons_score, max(0.0, 1.0 - diff_avg * 10))
        except Exception:
            cons_score = 0.0
        return 0.9 * comp_score + 0.1 * cons_score


_SCORERS = {
    'band_gap': score_0,
    'phonon_modes': score_1,
    'dielectric_tensor': score_2,
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
