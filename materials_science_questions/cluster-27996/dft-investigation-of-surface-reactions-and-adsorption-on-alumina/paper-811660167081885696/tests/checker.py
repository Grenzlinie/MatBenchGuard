import os
import json
import csv

# === author imports / helpers ===
import json, math


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
        gold = {}
        for step in spec.get("steps", []):
            if step.get("id") == "step_dft_energies":
                gold["dft_values"] = step.get("gold", {}).get("values", {})
                gold["dft_tolerance"] = step.get("gold", {}).get("tolerance_kcal_per_mol", 5.0)
        return gold


# === block: score_0 (check id='step_dft_energies') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold = ctx.get("dft_values", {})
        tol = ctx.get("dft_tolerance", 5.0)
        species = ["CH3OH","CH3O","CH2OH","CH2O","CHOH","CHO","COH","CO","H","H2"]
        if not isinstance(artifact, dict):
            return 0.0
        ok = 0
        for sp in species:
            val = artifact.get(sp)
            ref = gold.get(sp)
            if val is None or ref is None or not isinstance(val, (int, float)) or not isinstance(ref, (int, float)):
                continue
            if abs(val - ref) <= tol:
                ok += 1
        return ok / len(species)


# === block: score_1 (check id='step_microkinetic') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not isinstance(artifact, dict):
            return 0.0
        total = 0.0
        # --- dominant pathways ---
        pathways = artifact.get("dominant_pathways")
        if isinstance(pathways, list):
            expected = {
                "CH3OH->CH3O->CH2O->CHO->CO",
                "CH3OH->CH2OH->CHOH->CHO->CO",
                "CH3OH->CH2OH->CH2O->CHO->CO",
                "CH3OH->CH2OH->CHOH->COH->CO"
            }
            norm = set()
            for p in pathways:
                s = p.replace(" ", "").replace("→", "->")
                norm.add(s)
            matches = len(norm.intersection(expected))
            if matches >= 4:
                total += 0.3
            elif matches >= 2:
                if norm.issuperset({"CH3OH->CH3O->CH2O->CHO->CO", "CH3OH->CH2OH->CHOH->CHO->CO"}):
                    total += 0.2
                else:
                    total += 0.1
        # --- coverage_vs_T_UHV ---
        cov = artifact.get("coverage_vs_T_UHV", [])
        if isinstance(cov, list) and cov:
            co_data = [(d.get("T"), d.get("theta_CO")) for d in cov if isinstance(d, dict) and "T" in d and "theta_CO" in d]
            if co_data:
                max_T, _ = max(co_data, key=lambda x: x[1])
                if 140 <= max_T <= 180:
                    total += 0.2
                elif 130 <= max_T <= 190:
                    total += 0.1
            # COH decreasing
            coh = sorted([(d.get("T"), d.get("theta_COH")) for d in cov if isinstance(d, dict) and "T" in d and "theta_COH" in d], key=lambda x: x[0])
            if len(coh) >= 2 and coh[0][1] > coh[-1][1]:
                total += 0.1
            # vacant increasing
            vac = sorted([(d.get("T"), d.get("theta_vacant")) for d in cov if isinstance(d, dict) and "T" in d and "theta_vacant" in d], key=lambda x: x[0])
            if len(vac) >= 2 and vac[0][1] < vac[-1][1]:
                total += 0.1
        # --- rate_vs_T_highP ---
        rates = artifact.get("rate_vs_T_highP", [])
        if isinstance(rates, list):
            p_buckets = {}
            for r in rates:
                if not isinstance(r, dict): continue
                p = r.get("P"); t = r.get("T"); rate = r.get("rate")
                if p is None or t is None or rate is None: continue
                p_buckets.setdefault(p, []).append((t, rate))
            peak_in_range = False
            for p, lst in p_buckets.items():
                if p > 50:
                    peak_T, _ = max(lst, key=lambda x: x[1])
                    if 850 <= peak_T <= 950:
                        peak_in_range = True
                        break
            if peak_in_range:
                total += 0.15
        # --- apparent_activation_energy_vs_T ---
        act = artifact.get("apparent_activation_energy_vs_T", [])
        if isinstance(act, list):
            ts = sorted([(d.get("T"), d.get("H_star")) for d in act if isinstance(d, dict) and "T" in d and "H_star" in d], key=lambda x: x[0])
            if len(ts) >= 2:
                if all(ts[i][1] >= ts[i+1][1] for i in range(len(ts)-1)):
                    total += 0.15
        # --- reaction_order_vs_p ---
        order = artifact.get("reaction_order_vs_p", [])
        if isinstance(order, list):
            vals = sorted([(d.get("P"), d.get("alpha")) for d in order if isinstance(d, dict) and "P" in d and "alpha" in d], key=lambda x: x[0])
            if len(vals) >= 2:
                decreasing = all(vals[i][1] >= vals[i+1][1] for i in range(len(vals)-1))
                if decreasing and vals[0][1] > 0.8 and vals[-1][1] < 0.8:
                    total += 0.1
                elif decreasing:
                    total += 0.07
        return min(total, 1.0)


_SCORERS = {
    'step_dft_energies': score_0,
    'step_microkinetic': score_1,
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
