import os
import json
import csv

# === author imports / helpers ===
import math
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
    with open(os.path.join(outputs_dir, "results.json")) as f:
        results = json.load(f)
    return {"data": results}


# === block: score_0 (check id='band_gap') ===
def score_0(artifact, step, ctx):
    agent = ctx["data"].get("band_gap", None)
    if agent is None:
        return 0.0
    dev = abs(agent - step["gold"])
    if dev <= step["tolerance_abs"]:
        return 1.0
    elif dev <= 3 * step["tolerance_abs"]:
        return 1.0 - (dev - step["tolerance_abs"]) / (2 * step["tolerance_abs"])
    else:
        return 0.0


# === block: score_1 (check id='eps_inf_perp') ===
def score_1(artifact, step, ctx):
    agent = ctx["data"].get("eps_inf_perp", None)
    if agent is None:
        return 0.0
    dev = abs(agent - step["gold"])
    if dev <= step["tolerance_abs"]:
        return 1.0
    elif dev <= 3 * step["tolerance_abs"]:
        return 1.0 - (dev - step["tolerance_abs"]) / (2 * step["tolerance_abs"])
    else:
        return 0.0


# === block: score_2 (check id='eps_inf_par') ===
def score_2(artifact, step, ctx):
    agent = ctx["data"].get("eps_inf_par", None)
    if agent is None:
        return 0.0
    dev = abs(agent - step["gold"])
    if dev <= step["tolerance_abs"]:
        return 1.0
    elif dev <= 3 * step["tolerance_abs"]:
        return 1.0 - (dev - step["tolerance_abs"]) / (2 * step["tolerance_abs"])
    else:
        return 0.0


# === block: score_3 (check id='born_charges') ===
def score_3(artifact, step, ctx):
    agent_bc = ctx["data"].get("born_charges", None)
    if agent_bc is None:
        return 0.0
    gold_bc = step["gold"]
    tol = step["tolerance_abs"]
    max_dev = 0.0
    for at in ["Mg", "N", "B1", "B2", "B3"]:
        ag = agent_bc.get(at, None)
        go = gold_bc.get(at, None)
        if ag is None or go is None or len(ag) != 3 or len(go) != 3:
            return 0.0
        for i in range(3):
            for j in range(3):
                max_dev = max(max_dev, abs(ag[i][j] - go[i][j]))
    if max_dev <= tol:
        return 1.0
    elif max_dev <= 3 * tol:
        return 1.0 - (max_dev - tol) / (2 * tol)
    else:
        return 0.0


# === block: score_4 (check id='phonon_frequencies') ===
def score_4(artifact, step, ctx):
    agent_phon = ctx["data"].get("phonon_frequencies", None)
    if agent_phon is None:
        return 0.0
    gold_classes = step["gold"]
    tol = step["tolerance_abs"]
    total_gold = 0
    total_matched = 0
    for cls, freqs in gold_classes.items():
        if isinstance(freqs, list):
            for gf in freqs:
                total_gold += 1
                matched = False
                for af in agent_phon:
                    af_irrep = af.get("irrep", "")
                    af_lo = af.get("lo_or_to", None)
                    af_freq = af.get("frequency", None)
                    if af_freq is None:
                        continue
                    expected_lo = None
                    if "_TO" in cls:
                        expected_irrep = cls.split("_")[0]
                        expected_lo = "TO"
                    elif "_LO" in cls:
                        expected_irrep = cls.split("_")[0]
                        expected_lo = "LO"
                    else:
                        expected_irrep = cls
                        expected_lo = None
                    if af_irrep == expected_irrep and af_lo == expected_lo:
                        if abs(af_freq - gf) <= tol:
                            matched = True
                            break
                if matched:
                    total_matched += 1
    if total_gold == 0:
        return 1.0
    return total_matched / total_gold


# === block: score_5 (check id='eps0_perp') ===
def score_5(artifact, step, ctx):
    agent = ctx["data"].get("eps0_perp", None)
    if agent is None:
        return 0.0
    dev = abs(agent - step["gold"])
    if dev <= step["tolerance_abs"]:
        return 1.0
    elif dev <= 3 * step["tolerance_abs"]:
        return 1.0 - (dev - step["tolerance_abs"]) / (2 * step["tolerance_abs"])
    else:
        return 0.0


# === block: score_6 (check id='eps0_par') ===
def score_6(artifact, step, ctx):
    agent = ctx["data"].get("eps0_par", None)
    if agent is None:
        return 0.0
    dev = abs(agent - step["gold"])
    if dev <= step["tolerance_abs"]:
        return 1.0
    elif dev <= 3 * step["tolerance_abs"]:
        return 1.0 - (dev - step["tolerance_abs"]) / (2 * step["tolerance_abs"])
    else:
        return 0.0


# === block: score_7 (check id='elastic_constants') ===
def score_7(artifact, step, ctx):
    agent_ec = ctx["data"].get("elastic_constants", None)
    if agent_ec is None:
        return 0.0
    gold_ec = step["gold"]
    tols = step["tolerance_abs"]
    max_norm_dev = 0.0
    keys = ["C11", "C12", "C13", "C14", "C33", "C44"]
    for k in keys:
        av = agent_ec.get(k, None)
        gv = gold_ec.get(k, None)
        if av is None or gv is None:
            return 0.0
        tol = tols.get(k, 50.0)
        dev = abs(av - gv)
        norm = dev / tol
        max_norm_dev = max(max_norm_dev, norm)
    if max_norm_dev <= 1.0:
        return 1.0
    elif max_norm_dev <= 3.0:
        return 1.0 - (max_norm_dev - 1.0) / 2.0
    else:
        return 0.0


# === block: score_8 (check id='bulk_modulus') ===
def score_8(artifact, step, ctx):
    agent = ctx["data"].get("bulk_modulus", None)
    if agent is None:
        return 0.0
    dev = abs(agent - step["gold"])
    if dev <= step["tolerance_abs"]:
        return 1.0
    elif dev <= 3 * step["tolerance_abs"]:
        return 1.0 - (dev - step["tolerance_abs"]) / (2 * step["tolerance_abs"])
    else:
        return 0.0


# === block: score_9 (check id='shear_modulus') ===
def score_9(artifact, step, ctx):
    agent = ctx["data"].get("shear_modulus", None)
    if agent is None:
        return 0.0
    dev = abs(agent - step["gold"])
    if dev <= step["tolerance_abs"]:
        return 1.0
    elif dev <= 3 * step["tolerance_abs"]:
        return 1.0 - (dev - step["tolerance_abs"]) / (2 * step["tolerance_abs"])
    else:
        return 0.0


_SCORERS = {
    'band_gap': score_0,
    'eps_inf_perp': score_1,
    'eps_inf_par': score_2,
    'born_charges': score_3,
    'phonon_frequencies': score_4,
    'eps0_perp': score_5,
    'eps0_par': score_6,
    'elastic_constants': score_7,
    'bulk_modulus': score_8,
    'shear_modulus': score_9,
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
