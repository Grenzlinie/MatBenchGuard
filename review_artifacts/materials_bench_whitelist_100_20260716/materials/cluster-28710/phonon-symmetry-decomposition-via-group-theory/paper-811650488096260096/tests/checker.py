import os
import json
import csv

# === author imports / helpers ===
import csv, math, json
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
    def span_irreps_counts(mode_type, L):
        chi_E = 2*L + 1
        chi_C2 = (-1)**L
        if mode_type == "S":
            chi_sigma = 1
        elif mode_type == "T":
            chi_sigma = -1
        else:
            raise ValueError
        irrep_chars = {
            "A1": (1,1,1,1),
            "A2": (1,1,-1,-1),
            "B1": (1,-1,1,-1),
            "B2": (1,-1,-1,1)
        }
        counts = {}
        for irr, chars in irrep_chars.items():
            a = (chi_E*chars[0] + chi_C2*chars[1] + chi_sigma*chars[2] + chi_sigma*chars[3]) // 4
            if a > 0:
                counts[irr] = a
        return counts

    ctx = {}
    steps = spec.get("steps", [])
    for step in steps:
        if step["id"] == "cracked_split":
            expected_multiplets = step.get("expected_multiplets", [])
            irrep_counts = {}
            for mp in expected_multiplets:
                label = mp["multiplet_label"]
                L = mp["L"]
                typ = mp["type"]
                counts = span_irreps_counts(typ, L)
                irrep_counts[label] = counts
            ctx["irrep_counts"] = irrep_counts
        if step["id"] == "group_theory":
            modes = step.get("modes", [])
            gold_decomp = {}
            for mode in modes:
                typ = mode[0]
                L = int(mode[1:])
                counts = span_irreps_counts(typ, L)
                parts = []
                for irr in ["A1","A2","B1","B2"]:
                    c = counts.get(irr, 0)
                    if c > 0:
                        if c > 1:
                            parts.append(f"{c}{irr}")
                        else:
                            parts.append(irr)
                irrep_str = "+".join(parts)
                gold_decomp[mode] = irrep_str
            ctx["group_theory_gold"] = gold_decomp
    return ctx


# === block: score_0 (check id='defect_free') ===
def score_0(artifact, step, ctx):
    gold_table = step.get("gold_table", [])
    tol_abs = step.get("tolerance_abs_kHz", 20)
    tol_rel = step.get("tolerance_rel", 0.02)
    lookup = {}
    for row in artifact:
        try:
            d = float(row["diameter_mm"])
            m = row["mode_label"].strip()
            freq = float(row["frequency_kHz"])
        except:
            continue
        lookup[(d, m)] = freq
    matched = 0
    for g in gold_table:
        d_g = float(g["diameter_mm"])
        m_g = g["mode_label"].strip()
        f_g = float(g["frequency_kHz"])
        if (d_g, m_g) in lookup:
            f_a = lookup[(d_g, m_g)]
            err = abs(f_a - f_g)
            if err <= max(tol_abs, tol_rel * f_g):
                matched += 1
    score = matched / len(gold_table) if gold_table else 0.0
    return score


# === block: score_1 (check id='cracked_split') ===
def score_1(artifact, step, ctx):
    irrep_counts = ctx.get("irrep_counts", {})
    known_gold = step.get("known_gold", [])
    tol_abs = step.get("tolerance_abs_kHz", 20)
    tol_rel = step.get("tolerance_rel", 0.02)
    agent_counts = {}
    agent_rows = {}
    for row in artifact:
        try:
            mlabel = row["multiplet_label"].strip()
            irr = row["irrep_label"].strip()
            freq = float(row["frequency_kHz"])
        except:
            continue
        if mlabel not in agent_counts:
            agent_counts[mlabel] = Counter()
        agent_counts[mlabel][irr] += 1
        agent_rows[(mlabel, irr)] = freq
    irrep_score = 0.0
    if irrep_counts:
        n = len(irrep_counts)
        good = 0
        for label, expected_counts in irrep_counts.items():
            act_counts = agent_counts.get(label, {})
            if dict(act_counts) == expected_counts:
                good += 1
        irrep_score = good / n if n>0 else 1.0
    freq_score = 0.0
    if known_gold:
        matched = 0
        for kg in known_gold:
            mlabel = kg["multiplet_label"].strip()
            irr = kg["irrep_label"].strip()
            f_g = float(kg["frequency_kHz"])
            key = (mlabel, irr)
            if key in agent_rows:
                f_a = agent_rows[key]
                err = abs(f_a - f_g)
                if err <= max(tol_abs, tol_rel * f_g):
                    matched += 1
        freq_score = matched / len(known_gold)
    score = 0.5 * irrep_score + 0.5 * freq_score
    return score


# === block: score_2 (check id='group_theory') ===
def score_2(artifact, step, ctx):
    gold = ctx.get("group_theory_gold", {})
    if not gold:
        return 1.0
    agent = {}
    for row in artifact:
        try:
            mode = row["original_mode"].strip()
            s = row["spanning_irreps"].strip()
        except:
            continue
        agent[mode] = s
    def parse(s):
        parts = s.split("+")
        c = Counter()
        for p in parts:
            p = p.strip()
            if p[0].isdigit():
                i = 0
                while i < len(p) and p[i].isdigit():
                    i+=1
                m = int(p[:i])
                irr = p[i:].strip()
                c[irr] += m
            else:
                irr = p.strip()
                c[irr] += 1
        return c
    for mode, expected_str in gold.items():
        if mode not in agent:
            return 0.0
        if parse(expected_str) != parse(agent[mode]):
            return 0.0
    return 1.0


_SCORERS = {
    'defect_free': score_0,
    'cracked_split': score_1,
    'group_theory': score_2,
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
