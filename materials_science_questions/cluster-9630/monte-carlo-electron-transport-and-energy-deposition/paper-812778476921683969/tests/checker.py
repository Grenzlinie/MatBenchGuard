import os
import json
import csv

# === author imports / helpers ===
import math
from collections import defaultdict


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
    hparams = spec.get('hidden_params', {})
    densities = hparams.get('densities', {})
    Zs = hparams.get('atomic_numbers', {})
    poly_n = hparams.get('poly_n', {})
    poly_krho = hparams.get('poly_krho', {})
    digitized_raw = hparams.get('digitized_al_ag_ranges', {})

    def eval_poly(c, Z):
        return c['a0'] + c['a1']*Z + c['a2']*Z*Z

    # Expected per-element n, k, krho
    expected_elements = {}
    for elem in ['C','Al','Cu','Ag','Au']:
        Z = Zs.get(elem, 0)
        rho = densities.get(elem, 1.0)
        n_val = eval_poly(poly_n, Z)
        krho_val = eval_poly(poly_krho, Z)
        k_val = krho_val / rho
        expected_elements[elem] = {'n': n_val, 'k': k_val, 'krho': krho_val}

    # Expected ranges from digitized experimental data for Al and Ag
    expected_ranges = {}
    for key, val in digitized_raw.items():
        parts = key.rsplit('_', 1)
        if len(parts) == 2:
            elem, E_str = parts
            try:
                E = float(E_str)
            except ValueError:
                continue
            if elem in ('Al', 'Ag'):
                expected_ranges[(elem, E)] = float(val)

    # Fallback: if no digitized data, use polynomial-derived values (should be present)
    if not expected_ranges:
        for elem in ['Al','Ag']:
            Z = Zs[elem]
            rho = densities[elem]
            n = eval_poly(poly_n, Z)
            krho = eval_poly(poly_krho, Z)
            k = krho / rho
            for E in range(1, 11):
                R = k * (E ** n)
                expected_ranges[(elem, E)] = R

    return {
        'expected_elements': expected_elements,
        'expected_ranges': expected_ranges,
        'expected_poly_n': poly_n,
        'expected_poly_krho': poly_krho,
        'densities': densities,
        'atomic_numbers': Zs
    }


# === block: score_0 (check id='ranges') ===
def score_0(artifact, step, ctx):
    expected = ctx['expected_ranges']
    agent_dict = {}
    try:
        for row in artifact:
            elem = row.get('element', '')
            if elem not in ('Al','Ag'): continue
            try:
                E = float(row['beam_energy_keV'])
                R = float(row['range_nm'])
            except (ValueError, TypeError):
                continue
            agent_dict[(elem, E)] = R
    except Exception:
        return 0.0

    scores = []
    for key, expR in expected.items():
        R = agent_dict.get(key)
        if R is None:
            scores.append(0.0)
            continue
        rel_err = abs(R - expR) / expR if expR != 0 else 1.0
        if rel_err <= 0.05:
            scores.append(1.0)
        else:
            scores.append(max(0.0, 1.0 - (rel_err - 0.05) / 0.05))
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_1 (check id='fit') ===
def score_1(artifact, step, ctx):
    data = artifact
    elements_key = 'elements'
    polynomials_key = 'polynomials'
    expected_elements = ctx['expected_elements']
    expected_poly_n = ctx['expected_poly_n']
    expected_poly_krho = ctx['expected_poly_krho']
    densities = ctx['densities']
    Zs = ctx['atomic_numbers']

    # Part A: compare agent's per-element n and krho with paper polynomial
    A_scores = []
    for elem in ['C','Al','Cu','Ag','Au']:
        agent_obj = data.get(elements_key, {}).get(elem)
        if not agent_obj:
            A_scores.append(0.0)
            continue
        n_agent = agent_obj.get('n')
        k_agent = agent_obj.get('k')
        if n_agent is None or k_agent is None:
            A_scores.append(0.0)
            continue
        exp = expected_elements[elem]
        n_diff = abs(n_agent - exp['n'])
        n_s = 1.0 if n_diff <= 0.01 else max(0.0, 1.0 - (n_diff - 0.01)/0.02)
        rho = densities[elem]
        agent_krho = k_agent * rho
        krho_diff = abs(agent_krho - exp['krho'])
        k_s = 1.0 if krho_diff <= 0.5 else max(0.0, 1.0 - (krho_diff - 0.5)/1.0)
        A_scores.append(0.5*n_s + 0.5*k_s)
    partA = sum(A_scores)/len(A_scores) if A_scores else 0.0

    # Part B: self-consistency check
    B_scores = []
    poly = data.get(polynomials_key, {})
    for poly_type in ('n', 'k_rho'):
        coeffs = poly.get(poly_type)
        if not coeffs or any(coeffs.get(k) is None for k in ('a0','a1','a2')):
            B_scores.append(0.0)
            continue
        a0, a1, a2 = coeffs['a0'], coeffs['a1'], coeffs['a2']
        for elem in ['C','Al','Cu','Ag','Au']:
            Z = Zs[elem]
            pred = a0 + a1*Z + a2*Z*Z
            agent_per = data.get(elements_key, {}).get(elem)
            if not agent_per:
                B_scores.append(0.0)
                continue
            if poly_type == 'n':
                actual = agent_per.get('n')
                tol = 0.005
            else:  # k_rho
                k_actual = agent_per.get('k')
                if k_actual is None:
                    B_scores.append(0.0)
                    continue
                actual = k_actual * densities[elem]
                tol = 0.1
            if actual is None:
                B_scores.append(0.0)
                continue
            diff = abs(pred - actual)
            if diff <= tol:
                B_scores.append(1.0)
            else:
                B_scores.append(max(0.0, 1.0 - (diff - tol) / (tol*2)))
    partB = sum(B_scores)/len(B_scores) if B_scores else 0.0

    return 0.6 * partA + 0.4 * partB


_SCORERS = {
    'ranges': score_0,
    'fit': score_1,
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
