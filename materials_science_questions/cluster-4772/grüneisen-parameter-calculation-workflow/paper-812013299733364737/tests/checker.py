import os
import json
import csv

# === author imports / helpers ===
import statistics


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


# === block: score_0 (check id='hugoniot_results') ===
def score_0(artifact, step, ctx):
            # reference values from correct mixture Hugoniot integration
            ref_V = [0.7065, 0.68, 0.65, 0.62, 0.59, 0.56, 0.53, 0.5, 0.47, 0.44,
                     0.41, 0.38, 0.35, 0.32, 0.29, 0.265, 0.25]
            ref_Gamma = [0.2674, 0.278, 0.29, 0.302, 0.314, 0.326, 0.338, 0.35,
                         0.362, 0.374, 0.386, 0.398, 0.41, 0.422, 0.434, 0.444, 0.45]

            rows = artifact
            if not rows:
                return 0.0
            valid_rows = [r for r in rows if all(k in r for k in ['V','P','T','Gamma_mixture','Gamma_simple_avg','c','Gamma_over_V'])]
            if len(valid_rows) < 2:
                return 0.0
            # structural checks
            count_diff_ok = sum(1 for r in valid_rows if abs(float(r['Gamma_mixture'])-float(r['Gamma_simple_avg'])) > 0.01)
            frac_diff = count_diff_ok / len(valid_rows)
            gamma_over_v_vals = [float(r['Gamma_over_V']) for r in valid_rows]
            mean_g = sum(gamma_over_v_vals)/len(gamma_over_v_vals)
            if mean_g == 0:
                cv = 0.0
            else:
                var = sum((x - mean_g)**2 for x in gamma_over_v_vals)/(len(gamma_over_v_vals))
                cv = var**0.5 / mean_g
            cv_ok = 1.0 if cv > 0.01 else 0.0

            # reference comparison for Gamma_mixture
            agent_V = [float(r['V']) for r in valid_rows]
            agent_Gamma = [float(r['Gamma_mixture']) for r in valid_rows]

            # sort agent data by V
            sorted_idx = sorted(range(len(agent_V)), key=lambda i: agent_V[i])
            agent_V_sorted = [agent_V[i] for i in sorted_idx]
            agent_Gamma_sorted = [agent_Gamma[i] for i in sorted_idx]

            # for each reference point, find nearest agent V and compute abs error in Gamma
            total_err = 0.0
            matched = 0
            for vref, gref in zip(ref_V, ref_Gamma):
                diffs = [abs(v - vref) for v in agent_V_sorted]
                min_diff = min(diffs)
                idx = diffs.index(min_diff)
                if min_diff <= 0.02:
                    g_agent = agent_Gamma_sorted[idx]
                    total_err += abs(g_agent - gref)
                    matched += 1
            if matched == 0:
                ref_score = 0.0
            else:
                mean_err = total_err / matched
                ref_score = max(0.0, min(1.0, 1.0 - (mean_err - 0.005) / (0.05 - 0.005)))
            return max(0.0, min(1.0, 0.6*ref_score + 0.2*frac_diff + 0.2*cv_ok))


_SCORERS = {
    'hugoniot_results': score_0,
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
