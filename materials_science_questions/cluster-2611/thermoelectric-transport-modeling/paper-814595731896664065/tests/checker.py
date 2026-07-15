import os
import json
import csv

# === author imports / helpers ===
import numpy as np
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
    def prepare(outputs_dir, spec):
        gold_step = None
        for step in spec.get("steps", spec.get("checks", [])):
            if step.get("id") == "max_ZT_summary":
                gold_step = step
                break
        if gold_step is None:
            return {"gold": {}}
        return {"gold": gold_step.get("gold", {})}


# === block: score_0 (check id='transport_consistency') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        T = step.get("params", {}).get("T", 400)
        kL = step.get("params", {}).get("kappa_L", 1.2)
        rel_tol = step.get("params", {}).get("rel_tol", 0.01)
        total_points = 0
        consistent = 0
        for compound, points in artifact.items():
            if not isinstance(points, list):
                continue
            for pt in points:
                if not all(k in pt for k in ("mu","S","sigma","kappa_e","ZT")):
                    continue
                S_uV = float(pt["S"])
                sigma = float(pt["sigma"])
                kappa_e = float(pt["kappa_e"])
                ZT_stored = float(pt["ZT"])
                S_V = S_uV * 1e-6
                ZT_computed = (S_V**2 * sigma * T) / (kappa_e + kL)
                if abs(ZT_computed - ZT_stored) / max(abs(ZT_stored), 1e-12) <= rel_tol:
                    consistent += 1
                total_points += 1
        if total_points == 0:
            return 0.0
        return consistent / total_points


# === block: score_1 (check id='max_ZT_summary') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold = ctx.get("gold", {})
        scores = []
        compounds = ["(MA)PbI3", "(MA)SnI3", "(FA)PbI3", "(FA)SnI3", "Bi2Te3"]
        bi2te3_maxZT = None
        for comp in compounds:
            if comp not in artifact or comp not in gold:
                scores.append(0.0)
                continue
            agent = artifact[comp]
            gold_comp = gold[comp]
            # max_ZT closeness
            agent_ZT = float(agent.get("max_ZT", 0.0))
            ref_ZT = float(gold_comp.get("max_ZT", 0.0))
            if ref_ZT <= 0:
                zt_score = 1.0
            else:
                rel_err = abs(agent_ZT - ref_ZT) / ref_ZT
                zt_score = max(0.0, 1.0 - (max(0.0, rel_err - 0.1) / 0.1))
            # carrier concentration closeness (abs tol 0.2)
            agent_conc = float(agent.get("carrier_concentration", 0.0))
            ref_conc = float(gold_comp.get("carrier_concentration", 0.0))
            abs_diff = abs(agent_conc - ref_conc)
            if abs_diff <= 0.2:
                conc_score = 1.0
            else:
                conc_score = max(0.0, 1.0 - (abs_diff - 0.2) / 0.2)
            comp_score = (zt_score + conc_score) / 2.0
            if comp == "Bi2Te3":
                bi2te3_maxZT = agent_ZT
            scores.append(comp_score)
        # Trend check
        if bi2te3_maxZT is not None and bi2te3_maxZT > 0:
            trend_threshold = 0.8 * bi2te3_maxZT
            for i, comp in enumerate(compounds):
                if comp == "Bi2Te3":
                    continue
                agent_perov = artifact[comp]
                perov_ZT = float(agent_perov.get("max_ZT", 0.0))
                if perov_ZT < trend_threshold:
                    scores[i] = scores[i] * 0.5
        overall = sum(scores) / len(scores) if scores else 0.0
        return overall


_SCORERS = {
    'transport_consistency': score_0,
    'max_ZT_summary': score_1,
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
