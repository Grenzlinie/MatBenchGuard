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
    return {}


# === block: score_0 (check id='step_01_total_energies_ordering') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    energy = {}
    for r in rows:
        phase = r.get('phase', '').strip()
        val = r.get('total_energy_per_atom_meV', '')
        if not phase or not val:
            return 0.0
        try:
            energy[phase] = float(val)
        except:
            return 0.0
    required = ['WC', 'AsNi', 't-VN', 'NaCl', 'ZnS', 'CsCl']
    if any(p not in energy for p in required):
        return 0.0
    pairs = [('WC','AsNi'), ('AsNi','t-VN'), ('t-VN','NaCl'), ('NaCl','ZnS'), ('ZnS','CsCl')]
    correct = sum(1 for a,b in pairs if energy[a] < energy[b])
    return correct / 5.0


# === block: score_1 (check id='step_02_phonon_stability') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    flags = {}
    for r in rows:
        phase = r.get('phase', '').strip()
        val = r.get('has_imaginary_modes', '').strip().lower()
        if not phase or val not in ('true','false'):
            return 0.0
        flags[phase] = (val == 'true')
    expected = {'NaCl': True, 't-VN': False, 'AsNi': False, 'WC': False}
    if any(p not in flags for p in expected):
        return 0.0
    correct = sum(1 for p in expected if flags[p] == expected[p])
    return correct / 4.0


# === block: score_2 (check id='step_03_NofEF_trends') ===
def score_2(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    data = {'NaCl-based': {}, 'WC-based': {}}
    for r in rows:
        stype = r.get('structure_type','').strip()
        config = r.get('configuration','').strip()
        val = r.get('N_E_F','')
        if not stype or not config or not val:
            return 0.0
        try:
            val = float(val)
        except:
            return 0.0
        data[stype][config] = val

    conditions = 0
    cond_results = []

    # NaCl-based vacancy trend: V32N32 > V31N31 > V30N30 > V29N29 > V28N28
    nacl_seq = ['V32N32','V31N31','V30N30','V29N29','V28N28']
    wc_seq = ['V32N32','V31N31','V30N30','V29N29','V28N28']

    nacl_vals = [data['NaCl-based'].get(c) for c in nacl_seq]
    wc_vals = [data['WC-based'].get(c) for c in wc_seq]

    nacl_ok = all(v is not None for v in nacl_vals) and all(nacl_vals[i] > nacl_vals[i+1] for i in range(len(nacl_vals)-1))
    cond_results.append(1 if nacl_ok else 0)

    wc_ok = all(v is not None for v in wc_vals) and all(wc_vals[i] < wc_vals[i+1] for i in range(len(wc_vals)-1))
    cond_results.append(1 if wc_ok else 0)

    # impurity checks
    # NaCl-based C: V32N29C3 < V32N32
    nacl_c = data['NaCl-based'].get('V32N29C3')
    nacl_stoich = data['NaCl-based'].get('V32N32')
    if nacl_c is not None and nacl_stoich is not None:
        cond_results.append(1 if nacl_c < nacl_stoich else 0)
    else:
        cond_results.append(0)

    # WC-based C: V32N29C3 > V32N32
    wc_c = data['WC-based'].get('V32N29C3')
    wc_stoich = data['WC-based'].get('V32N32')
    if wc_c is not None and wc_stoich is not None:
        cond_results.append(1 if wc_c > wc_stoich else 0)
    else:
        cond_results.append(0)

    # NaCl-based O: V32N29O3 > V32N32
    nacl_o = data['NaCl-based'].get('V32N29O3')
    if nacl_o is not None and nacl_stoich is not None:
        cond_results.append(1 if nacl_o > nacl_stoich else 0)
    else:
        cond_results.append(0)

    # WC-based O: V32N29O3 > V32N32 (based on reference at this composition)
    wc_o = data['WC-based'].get('V32N29O3')
    if wc_o is not None and wc_stoich is not None:
        cond_results.append(1 if wc_o > wc_stoich else 0)
    else:
        cond_results.append(0)

    total = len(cond_results)
    if total == 0:
        return 0.0
    return sum(cond_results) / total


_SCORERS = {
    'step_01_total_energies_ordering': score_0,
    'step_02_phonon_stability': score_1,
    'step_03_NofEF_trends': score_2,
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
