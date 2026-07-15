import os
import json
import csv

# === author imports / helpers ===
import json, math, os


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


# === block: score_0 (check id='01_linear_chain_model') ===
def score_0(artifact, step, ctx):
        if not artifact or not isinstance(artifact, dict):
            return 0.0
        if 'K_x' not in artifact or 'K_z' not in artifact or 'modes' not in artifact:
            return 0.0
        Kx = float(artifact['K_x'])
        Kz = float(artifact['K_z'])
        expected_Kx = 3.6e19
        expected_Kz = 7.5e19
        rel_tol = 0.01
        Kx_ok = abs(Kx - expected_Kx) / expected_Kx <= rel_tol
        Kz_ok = abs(Kz - expected_Kz) / expected_Kz <= rel_tol
        K_score = (Kx_ok + Kz_ok) / 2.0

        # expected frequencies computed from public bilayer constants
        shear_w = 19.2
        breathing_w = 27.8
        def freq(N, alpha, w):
            return w * math.sqrt(1.0 - math.cos((alpha - 1) * math.pi / N))
        expected_modes = []
        for N in [2,3,4,5,6,7,100]:
            # shear branches
            branches = []
            branches.append(N)  # α=N
            if N >= 4:
                branches.append(N-2)
            for alpha in branches:
                expected_modes.append({
                    'N': N,
                    'mode_type': 'shear',
                    'branch': f'α={alpha}',
                    'frequency_cm-1': freq(N, alpha, shear_w)
                })
            # breathing branches: even α up to N
            for alpha in range(2, N+1, 2):
                expected_modes.append({
                    'N': N,
                    'mode_type': 'breathing',
                    'branch': f'α={alpha}',
                    'frequency_cm-1': freq(N, alpha, breathing_w)
                })

        agent_modes = artifact.get('modes', [])
        if not isinstance(agent_modes, list):
            return K_score * 0.3
        freq_tol = 0.1
        total_freq_checks = len(expected_modes)
        freq_passed = 0
        for em in expected_modes:
            found = False
            for am in agent_modes:
                if (am.get('N') == em['N'] and
                    am.get('mode_type') == em['mode_type'] and
                    am.get('branch') == em['branch']):
                    fval = am.get('frequency_cm-1')
                    if fval is not None and abs(float(fval) - em['frequency_cm-1']) <= freq_tol:
                        freq_passed += 1
                    found = True
                    break
        freq_score = freq_passed / total_freq_checks if total_freq_checks else 0.0
        total = 0.3 * K_score + 0.7 * freq_score
        return total


_SCORERS = {
    '01_linear_chain_model': score_0,
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
