import os
import json
import csv

# === author imports / helpers ===
import csv
import os
from collections import Counter


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
        a_path = os.path.join(outputs_dir, "cluster_sizes_a_axis.csv")
        c_path = os.path.join(outputs_dir, "cluster_sizes_c_axis.csv")
    
        ctx = {
            "a_hist": None, "c_hist": None,
            "a_dimer_count": 0, "c_dimer_count": 0,
            "a_unreacted_count": 0, "c_unreacted_count": 0,
            "a_fragment_count": 0, "c_fragment_count": 0,
        }
    
        for key, path in [("a", a_path), ("c", c_path)]:
            if not os.path.exists(path):
                continue
            with open(path, newline="") as f:
                reader = csv.DictReader(f)
                rows = list(reader)
            if not rows:
                continue
            sizes = []
            for row in rows:
                try:
                    sizes.append(int(row.get("cluster_size", 0)))
                except (ValueError, TypeError):
                    sizes.append(0)
            hist = Counter(sizes)
            ctx[f"{key}_hist"] = hist
            ctx[f"{key}_dimer_count"] = hist.get(28, 0)
            ctx[f"{key}_unreacted_count"] = hist.get(14, 0)
            # fragments: clusters with 1-13 carbons
            ctx[f"{key}_fragment_count"] = sum(v for k, v in hist.items() if 1 <= k <= 13)
    
        return ctx


# === block: score_0 (check id='step_2a_a_axis') ===
def score_0(artifact, step, ctx):
        hist = ctx.get("a_hist")
        if hist is None:
            return 0.0
        rubric = step.get("rubric", {})
        if not rubric:
            return 0.0
        total = 0.0

        # 1. Dimer count
        dc = rubric.get("dimer_count", {})
        dimer_count = ctx.get("a_dimer_count", 0)
        gold = dc.get("gold", 49)
        tight_tol = dc.get("tight_tol", 10)
        wide_tol = dc.get("wide_tol", 20)
        if abs(dimer_count - gold) <= tight_tol:
            dimer_score = 1.0
        else:
            excess = max(0.0, abs(dimer_count - gold) - tight_tol)
            dimer_score = max(0.0, 1.0 - excess / max(1, wide_tol - tight_tol))
        total += dimer_score * dc.get("sub_weight", 0.35)

        # 2. Unreacted count
        uc = rubric.get("unreacted_count", {})
        unreacted_count = ctx.get("a_unreacted_count", 0)
        gold_u = uc.get("gold", 1260)
        tight_u = uc.get("tight_tol", 50)
        wide_u = uc.get("wide_tol", 100)
        if abs(unreacted_count - gold_u) <= tight_u:
            unreacted_score = 1.0
        else:
            excess_u = max(0.0, abs(unreacted_count - gold_u) - tight_u)
            unreacted_score = max(0.0, 1.0 - excess_u / max(1, wide_u - tight_u))
        total += unreacted_score * uc.get("sub_weight", 0.25)

        # 3. Dimer dominance: 28C is the most common non-14 cluster size
        dd = rubric.get("dimer_dominance", {})
        non14 = {k: v for k, v in hist.items() if k != 14 and k > 0}
        if non14:
            max_val = max(non14.values())
            top_sizes = [k for k, v in non14.items() if v == max_val]
            if 28 in top_sizes:
                dom_score = 1.0
            elif any(k in [27, 29] for k in top_sizes):
                dom_score = 0.6
            elif any(k in [26, 30] for k in top_sizes):
                dom_score = 0.3
            else:
                dom_score = 0.0
        else:
            dom_score = 0.0
        total += dom_score * dd.get("sub_weight", 0.20)

        # 4. Fragment presence
        fp = rubric.get("fragment_presence", {})
        frag_count = ctx.get("a_fragment_count", 0)
        if 20 <= frag_count <= 800:
            frag_score = 1.0
        elif 10 <= frag_count < 20 or 800 < frag_count <= 1200:
            frag_score = 0.5
        else:
            frag_score = 0.0
        total += frag_score * fp.get("sub_weight", 0.20)

        return min(1.0, max(0.0, total))


# === block: score_1 (check id='step_2b_c_axis') ===
def score_1(artifact, step, ctx):
        hist = ctx.get("c_hist")
        if hist is None:
            return 0.0
        rubric = step.get("rubric", {})
        if not rubric:
            return 0.0
        total = 0.0

        # 1. Dimer count
        dc = rubric.get("dimer_count", {})
        dimer_count = ctx.get("c_dimer_count", 0)
        gold = dc.get("gold", 23)
        tight_tol = dc.get("tight_tol", 5)
        wide_tol = dc.get("wide_tol", 10)
        if abs(dimer_count - gold) <= tight_tol:
            dimer_score = 1.0
        else:
            excess = max(0.0, abs(dimer_count - gold) - tight_tol)
            dimer_score = max(0.0, 1.0 - excess / max(1, wide_tol - tight_tol))
        total += dimer_score * dc.get("sub_weight", 0.25)

        # 2. Orientation trend: a_dimer > c_dimer
        ot = rubric.get("orientation_trend", {})
        a_dimer = ctx.get("a_dimer_count", 0)
        c_dimer = ctx.get("c_dimer_count", 0)
        if a_dimer > c_dimer:
            trend_score = 1.0
        elif a_dimer == c_dimer and a_dimer > 0:
            trend_score = 0.3
        else:
            trend_score = 0.0
        total += trend_score * ot.get("sub_weight", 0.30)

        # 3. Fragmentation trend: c_fragments > a_fragments
        ft = rubric.get("fragmentation_trend", {})
        a_frag = ctx.get("a_fragment_count", 0)
        c_frag = ctx.get("c_fragment_count", 0)
        if c_frag > a_frag:
            frag_trend_score = 1.0
        elif c_frag == a_frag and c_frag > 0:
            frag_trend_score = 0.3
        else:
            frag_trend_score = 0.0
        total += frag_trend_score * ft.get("sub_weight", 0.25)

        # 4. Unreacted count
        uc = rubric.get("unreacted_count", {})
        unreacted_count = ctx.get("c_unreacted_count", 0)
        gold_u = uc.get("gold", 1260)
        tight_u = uc.get("tight_tol", 60)
        wide_u = uc.get("wide_tol", 120)
        if abs(unreacted_count - gold_u) <= tight_u:
            unreacted_score = 1.0
        else:
            excess_u = max(0.0, abs(unreacted_count - gold_u) - tight_u)
            unreacted_score = max(0.0, 1.0 - excess_u / max(1, wide_u - tight_u))
        total += unreacted_score * uc.get("sub_weight", 0.20)

        return min(1.0, max(0.0, total))


_SCORERS = {
    'step_2a_a_axis': score_0,
    'step_2b_c_axis': score_1,
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
