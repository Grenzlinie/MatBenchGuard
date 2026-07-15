import os
import json
import csv

# === author imports / helpers ===
import math
import csv
import os
import json
import collections

def delta(Vm, dm=50.0):
    return dm / ((6/math.pi) * Vm) ** (1/3)

def find_h(Vm, C=9.8, dm=50.0):
    D = delta(Vm, dm)
    target = C / (dm**3)
    lo, hi = 1e-12, D/2
    for _ in range(200):
        mid = (lo+hi)/2
        f = 1/mid**3 + 1/(D-mid)**3
        if f > target:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


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
    dm = 50.0
    C = 9.8
    ref = {}
    vm_list = [0.051, 0.121, 0.210, 0.314]
    for vm in vm_list:
        h = find_h(vm, C, dm)
        D = delta(vm, dm)
        th = math.atan(2*h/D)
        th_deg = math.degrees(th)
        K = math.sqrt(math.tan(th/2)*math.tan(th)/(1+math.tan(th/2)*math.tan(th)))
        ref[vm] = {'h': h, 'theta': th_deg, 'K': K}
    return {'ref': ref}


# === block: score_0 (check id='step01') ===
def score_0(artifact, step, ctx):
    if not artifact or len(artifact)==0:
        return 0.0
    required_cols = ['Vm', 'h_um', 'theta_deg', 'Kcl_Kmax']
    if not all(col in artifact[0] for col in required_cols):
        return 0.0
    vm_map = {}
    for r in artifact:
        try:
            vm = float(r['Vm'])
            h = float(r['h_um'])
            th = float(r['theta_deg'])
            vm_map[vm] = (h, th)
        except:
            continue
    vm_list = [0.051, 0.121, 0.210, 0.314]
    if not all(vm in vm_map for vm in vm_list):
        return 0.0
    ref = ctx['ref']
    rel_err_h = []
    rel_err_theta = []
    agent_Ks = []
    for vm in vm_list:
        rref = ref[vm]
        agent_h, agent_theta_deg = vm_map[vm]
        rel_err_h.append(abs(agent_h - rref['h']) / (rref['h'] if rref['h']>0 else 1e-12))
        rel_err_theta.append(abs(agent_theta_deg - rref['theta']) / (rref['theta'] if rref['theta']>0 else 1e-12))
        th_rad = math.radians(agent_theta_deg)
        tn = math.tan(th_rad)
        tnh = math.tan(th_rad/2)
        num = tnh * tn
        K = math.sqrt(num / (1+num))
        agent_Ks.append(K)
    h_score = 1.0 if all(e <= 0.05 for e in rel_err_h) else 0.0
    theta_score = 1.0 if all(e <= 0.05 for e in rel_err_theta) else 0.0
    rel_err_K = [abs(a - ref[vm]['K']) / (ref[vm]['K'] if ref[vm]['K']>0 else 1e-12) for a,vm in zip(agent_Ks, vm_list)]
    kcl_score = 1.0 if all(e <= 0.05 for e in rel_err_K) else 0.0
    mono = all(agent_Ks[i] < agent_Ks[i+1] for i in range(len(agent_Ks)-1))
    mono_score = 1.0 if mono else 0.0
    total = 0.3*h_score + 0.3*theta_score + 0.3*kcl_score + 0.1*mono_score
    return total


_SCORERS = {
    'step01': score_0,
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
