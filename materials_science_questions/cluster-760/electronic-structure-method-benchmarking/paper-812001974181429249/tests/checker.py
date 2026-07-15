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
        # Gold values from Table 2, AVTZ rows (kcal/mol).
        # Tuple: (value without ZPE, value with ZPE).
        gold_values = {
            "C1": {
                "B3PW91": (0.0, 0.0),
                "B3LYP": (0.0, 0.0),
                "MP2": (0.0, 0.0),
                "CCSD(T)": (0.0, 0.0),
            },
            "Cs": {
                "B3PW91": (-0.15, 0.14),
                "B3LYP": (0.01, 0.29),
                "MP2": (-0.18, -0.02),
                "CCSD(T)": (-0.03, 0.13),
            },
            "C3": {
                "B3PW91": (1.82, 1.96),
                "B3LYP": (2.06, 2.21),
                "MP2": (1.97, 1.74),
                "CCSD(T)": (2.13, 1.90),
            },
            "TS_C1_Cs": {
                "B3PW91": (1.73, 1.48),
                "B3LYP": (1.75, 1.50),
                "MP2": (1.79, 1.49),
                "CCSD(T)": (1.81, 1.51),
            },
            "TS_Cs_C3": {
                "B3PW91": (2.81, 1.93),
                "B3LYP": (2.54, 1.67),
                "MP2": (2.83, 1.93),
                "CCSD(T)": (2.64, 1.74),
            },
        }
        return {"gold_values": gold_values}


# === block: score_0 (check id='value_agreement') ===
def score_0(artifact, step, ctx):
        gold = ctx.get("gold_values", {})
        results_list = artifact.get("results", [])
        if not isinstance(results_list, list) or not results_list:
            return 0.0

        lookup = {}
        for entry in results_list:
            struct = entry.get("structure")
            meth = entry.get("method")
            zpe = entry.get("zpe_corrected")
            val = entry.get("value")
            if struct and meth and zpe is not None and isinstance(val, (int, float)):
                lookup[(struct, meth, zpe)] = float(val)

        tolerance_standard = 0.3
        tolerance_c1 = 0.05
        total = 0
        matched = 0

        for struct, methods in gold.items():
            for method, (no_zpe, with_zpe) in methods.items():
                for zpe_flag in [False, True]:
                    expected = no_zpe if not zpe_flag else with_zpe
                    key = (struct, method, zpe_flag)
                    total += 1
                    agent_val = lookup.get(key)
                    if agent_val is None:
                        continue
                    tol = tolerance_c1 if struct == "C1" else tolerance_standard
                    if abs(agent_val - expected) <= tol:
                        matched += 1

        if total == 0:
            return 0.0
        return matched / total


# === block: score_1 (check id='sign_trend') ===
def score_1(artifact, step, ctx):
        results_list = artifact.get("results", [])
        if not isinstance(results_list, list):
            return 0.0

        signs = {}
        for entry in results_list:
            if entry.get("structure") == "Cs" and entry.get("zpe_corrected") == False:
                method = entry.get("method")
                val = entry.get("value")
                if method in ("B3PW91", "B3LYP", "MP2", "CCSD(T)") and isinstance(val, (int, float)):
                    signs[method] = float(val)

        checks = {
            "B3PW91": lambda v: v < 0.0,
            "MP2": lambda v: v < 0.0,
            "CCSD(T)": lambda v: v < 0.0,
            "B3LYP": lambda v: v > -0.05,
        }
        score = 0.0
        for method, fn in checks.items():
            if method in signs and fn(signs[method]):
                score += 0.25
        return score


# === block: score_2 (check id='functional_proximity') ===
def score_2(artifact, step, ctx):
        gold = ctx.get("gold_values", {})
        results_list = artifact.get("results", [])
        if not isinstance(results_list, list):
            return 0.0

        lookup = {}
        for entry in results_list:
            struct = entry.get("structure")
            meth = entry.get("method")
            zpe = entry.get("zpe_corrected")
            val = entry.get("value")
            if struct and meth and zpe is not None and isinstance(val, (int, float)):
                lookup[(struct, meth, zpe)] = float(val)

        # CCSD(T) reference for Cs and C3 (energy differences only)
        ref_ccsdt = {}
        for struct in ["Cs", "C3"]:
            ref_no_zpe, ref_zpe = gold[struct]["CCSD(T)"]
            ref_ccsdt[(struct, False)] = ref_no_zpe
            ref_ccsdt[(struct, True)] = ref_zpe

        def compute_mad(method):
            diffs = []
            for struct in ["Cs", "C3"]:
                for zpe_flag in [False, True]:
                    agent_val = lookup.get((struct, method, zpe_flag))
                    ref_val = ref_ccsdt.get((struct, zpe_flag))
                    if agent_val is not None and ref_val is not None:
                        diffs.append(abs(agent_val - ref_val))
            if not diffs:
                return None
            return sum(diffs) / len(diffs)

        mad_b3pw91 = compute_mad("B3PW91")
        mad_b3lyp = compute_mad("B3LYP")
        if mad_b3pw91 is None or mad_b3lyp is None:
            return 0.0
        return 1.0 if mad_b3pw91 <= mad_b3lyp else 0.0


_SCORERS = {
    'value_agreement': score_0,
    'sign_trend': score_1,
    'functional_proximity': score_2,
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
