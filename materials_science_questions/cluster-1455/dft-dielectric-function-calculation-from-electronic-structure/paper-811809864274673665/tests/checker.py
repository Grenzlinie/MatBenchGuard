import os
import json
import csv

# === author imports / helpers ===
import json, math

class ndarray:
    def __init__(self, data, dtype=float):
        self._data = [dtype(x) for x in data]
    def __iter__(self):
        return iter(self._data)
    def __len__(self):
        return len(self._data)
    def __getitem__(self, i):
        return self._data[i]
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return ndarray([v / other for v in self._data])
        return ndarray([v / o for v, o in zip(self._data, other._data)])
    def __rtruediv__(self, other):
        return ndarray([other / v for v in self._data])
    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return ndarray([v - other for v in self._data])
        return ndarray([v - o for v, o in zip(self._data, other._data)])
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return ndarray([v * other for v in self._data])
        return ndarray([v * o for v, o in zip(self._data, other._data)])
    def __rmul__(self, other):
        return self.__mul__(other)
    def __pow__(self, power):
        return ndarray([v ** power for v in self._data])
    def sum(self):
        return sum(self._data)
    def mean(self):
        if len(self._data) == 0:
            return 0.0
        return sum(self._data) / len(self._data)
    def __abs__(self):
        return ndarray([abs(v) for v in self._data])

def _array(data, dtype=float):
    return ndarray(list(data), dtype)

def _linspace(start, stop, num):
    if num == 1:
        return ndarray([start])
    step = (stop - start) / (num - 1)
    return ndarray([start + i * step for i in range(num)])

def _interp(x, xp, fp):
    x = list(x)
    xp = list(xp)
    fp = list(fp)
    result = []
    n = len(xp)
    for xi in x:
        if xi <= xp[0]:
            result.append(fp[0])
        elif xi >= xp[-1]:
            result.append(fp[-1])
        else:
            for i in range(n-1):
                if xp[i] <= xi <= xp[i+1]:
                    t = (xi - xp[i]) / (xp[i+1] - xp[i])
                    y = fp[i] + t * (fp[i+1] - fp[i])
                    result.append(y)
                    break
    return ndarray(result)

np = type('np', (), {
    'array': staticmethod(_array),
    'linspace': staticmethod(_linspace),
    'interp': staticmethod(_interp),
    'sqrt': staticmethod(math.sqrt),
})()


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
    # Build reference dielectric spectrum from hidden oscillators
    osc_100 = spec.get("hidden_oscillators_100", [])
    osc_001 = spec.get("hidden_oscillators_001", [])
    estep = 0.05
    emax = 35.0
    energies = [i*estep for i in range(int(emax/estep)+1)]

    def lorentz_eps(omega, oscillators):
        e1, e2 = 1.0, 0.0
        for w0, g, S in oscillators:
            w02 = w0*w0
            w2 = omega*omega
            denom = (w02 - w2)**2 + (g*omega)**2
            if denom < 1e-60:
                continue
            e1 += S * w02 * (w02 - w2) / denom
            e2 += S * w02 * g * omega / denom
        return e1, e2

    ref_eps2_100 = []
    ref_eps2_001 = []
    for w in energies:
        _, e2 = lorentz_eps(w, osc_100)
        ref_eps2_100.append(e2)
        _, e2 = lorentz_eps(w, osc_001)
        ref_eps2_001.append(e2)

    ctx = {
        "ref_eps2_100": ref_eps2_100,
        "ref_eps2_001": ref_eps2_001,
        "energy_len": len(energies)
    }
    return ctx


# === block: score_0 (check id='check_lattice') ===
def score_0(artifact, step, ctx):
    lat = artifact.get("lattice_parameters", {})
    target = step.get("target", {})
    tol = step.get("tolerance_abs", {})
    keys = ["a", "c", "u"]
    scores = []
    for k in keys:
        v = lat.get(k, None)
        tg = target.get(k)
        ta = tol.get(k, 0.001)
        if v is None or tg is None:
            scores.append(0.0)
        else:
            err = abs(v - tg)
            s = max(0.0, 1.0 - err / ta) if ta > 0 else 1.0
            scores.append(s)
    return sum(scores)/len(scores) if scores else 0.0


# === block: score_1 (check id='check_bulk') ===
def score_1(artifact, step, ctx):
    v = artifact.get("bulk_modulus_B0", None)
    target = step.get("target", None)
    tol_rel = step.get("tolerance_rel", 0.25)
    if v is None or target is None:
        return 0.0
    rel_err = abs(v - target) / abs(target) if target != 0 else abs(v - target)
    return max(0.0, 1.0 - rel_err / tol_rel)


# === block: score_2 (check id='check_elastic') ===
def score_2(artifact, step, ctx):
    ec = artifact.get("elastic_constants", {})
    target = step.get("target", {})
    tol = step.get("tolerance_rel", {})
    keys = ["C11","C12","C13","C33","C44"]
    scores = []
    for k in keys:
        v = ec.get(k, None)
        tg = target.get(k)
        tr = tol.get(k, 0.25)
        if v is None or tg is None:
            scores.append(0.0)
        else:
            rel_err = abs(v - tg) / abs(tg) if tg != 0 else abs(v - tg)
            s = max(0.0, 1.0 - rel_err / tr)
            scores.append(s)
    return sum(scores)/len(scores) if scores else 0.0


# === block: score_3 (check id='check_derived') ===
def score_3(artifact, step, ctx):
    # Recompute derived mechanical properties from elastic constants
    C = artifact.get("elastic_constants", {})
    c11 = C.get("C11"); c12 = C.get("C12"); c13 = C.get("C13"); c33 = C.get("C33"); c44 = C.get("C44")
    if any(v is None for v in [c11,c12,c13,c33,c44]):
        return 0.0
    # Compliance constants
    S11 = (c11*c33 - c13**2) / ((c11 - c12)*(c11*c33 + c12*c33 - 2*c13**2))
    S12 = (c13**2 - c12*c33) / ((c11 - c12)*(c11*c33 + c12*c33 - 2*c13**2))
    S13 = -c13 / (c11*c33 + c12*c33 - 2*c13**2)
    S33 = (c11 + c12) / (c11*c33 + c12*c33 - 2*c13**2)
    S44 = 1.0 / c44
    # Bulk moduli
    B_V = (1/9)*(2*c11 + c33) + (2/9)*(c12 + 2*c13)
    B_R = 1.0 / ( (2*S11 + S33) + 2*(S12 + 2*S13) )
    B_H = (B_R + B_V) / 2.0
    # Shear moduli
    G_V = (1/15)*(2*c11 + c33 - c12 - 2*c13) + (1/5)*(2*c44 + (c11 - c12)/2)
    G_R = 15.0 / ( 4*(2*S11 + S33) - 4*(S12 + 2*S13) + 6*(S44 + S11 - S12) )
    G_H = (G_R + G_V) / 2.0
    # Young's moduli
    def young(B, G):
        if G + 3*B == 0: return 0.0
        return 9*B*G/(G + 3*B)
    E_R = young(B_R, G_R); E_V = young(B_V, G_V); E_H = young(B_H, G_H)
    # Poisson
    def poisson(B, G):
        if B + G/3 == 0: return 0.0
        return 0.5 * (B - (2/3)*G) / (B + (1/3)*G)
    v_R = poisson(B_R, G_R); v_V = poisson(B_V, G_V); v_H = poisson(B_H, G_H)
    B_G_Hill = B_H / G_H if G_H != 0 else 0.0
    Delta_p = c33 / c11 if c11 != 0 else 0.0
    Delta_s1 = (c11 - c13) / (2*c44) if c44 != 0 else 0.0
    Delta_s2 = 2*c44 / (c11 - c12) if (c11 - c12) != 0 else 0.0

    computed = {
        "B_R": B_R, "B_V": B_V, "B_H": B_H,
        "G_R": G_R, "G_V": G_V, "G_H": G_H,
        "E_R": E_R, "E_V": E_V, "E_H": E_H,
        "v_R": v_R, "v_V": v_V, "v_H": v_H,
        "B_G_Hill": B_G_Hill,
        "Delta_p": Delta_p, "Delta_s1": Delta_s1, "Delta_s2": Delta_s2
    }

    target = step.get("target", {})
    tol_rel = step.get("tolerance_rel", {})
    scores = []
    for k, cv in computed.items():
        tg = target.get(k)
        tr = tol_rel.get(k, 0.15)
        if tg is None:
            continue
        if tg == 0:
            s = 1.0 if abs(cv) < 1e-12 else 0.0
        else:
            rel_err = abs(cv - tg) / abs(tg)
            s = max(0.0, 1.0 - rel_err / tr)
        scores.append(s)
    return sum(scores)/len(scores) if scores else 0.0


# === block: score_4 (check id='check_sound') ===
def score_4(artifact, step, ctx):
    sv = artifact.get("sound_velocities", {})
    target = step.get("target", {})
    tol_rel = step.get("tolerance_rel", 0.15)
    keys = ["vs_R","vs_V","vs_H","vp_R","vp_V","vp_H","vm_R","vm_V","vm_H"]
    scores = []
    for k in keys:
        v = sv.get(k, None)
        tg = target.get(k)
        if v is None or tg is None:
            scores.append(0.0)
        else:
            rel_err = abs(v - tg) / abs(tg) if tg != 0 else abs(v - tg)
            s = max(0.0, 1.0 - rel_err / tol_rel)
            scores.append(s)
    return sum(scores)/len(scores) if scores else 0.0


# === block: score_5 (check id='check_debye') ===
def score_5(artifact, step, ctx):
    deb = artifact.get("Debye_temperature", {})
    target = step.get("target", {})
    tol_abs = step.get("tolerance_abs", 30.0)
    keys = ["Theta_R","Theta_V","Theta_H"]
    scores = []
    for k in keys:
        v = deb.get(k, None)
        tg = target.get(k)
        if v is None or tg is None:
            scores.append(0.0)
        else:
            err = abs(v - tg)
            s = max(0.0, 1.0 - err / tol_abs)
            scores.append(s)
    return sum(scores)/len(scores) if scores else 0.0


# === block: score_6 (check id='check_bandgaps') ===
def score_6(artifact, step, ctx):
    bg = artifact.get("band_gaps", {})
    target = step.get("target", {})
    tol_abs = step.get("tolerance_abs", 0.5)
    keys = ["indirect_F_Gamma","direct_Gamma"]
    scores = []
    for k in keys:
        v = bg.get(k, None)
        tg = target.get(k)
        if v is None or tg is None:
            scores.append(0.0)
        else:
            err = abs(v - tg)
            s = max(0.0, 1.0 - err / tol_abs)
            scores.append(s)
    return sum(scores)/len(scores) if scores else 0.0


# === block: score_7 (check id='check_static_eps') ===
def score_7(artifact, step, ctx):
    se = artifact.get("static_dielectric_constants", {})
    target = step.get("target", {})
    tol_abs = step.get("tolerance_abs", 2.0)
    keys = ["epsilon0_100","epsilon0_001"]
    scores = []
    for k in keys:
        v = se.get(k, None)
        tg = target.get(k)
        if v is None or tg is None:
            scores.append(0.0)
        else:
            err = abs(v - tg)
            s = max(0.0, 1.0 - err / tol_abs)
            scores.append(s)
    return sum(scores)/len(scores) if scores else 0.0


# === block: score_8 (check id='check_dielectric_spectrum') ===
def score_8(artifact, step, ctx):
    spec = artifact.get("dielectric_spectrum", {})
    required_keys = ["epsilon1_100","epsilon2_100","epsilon1_001","epsilon2_001","energy_array"]
    if not all(k in spec for k in required_keys):
        return 0.0

    energy_agent = np.array(spec["energy_array"], dtype=float)
    e2_100_agent = np.array(spec["epsilon2_100"], dtype=float)
    e1_100_agent = np.array(spec["epsilon1_100"], dtype=float)
    e2_001_agent = np.array(spec["epsilon2_001"], dtype=float)
    e1_001_agent = np.array(spec["epsilon1_001"], dtype=float)

    ref_100 = np.array(ctx.get("ref_eps2_100", []), dtype=float)
    ref_001 = np.array(ctx.get("ref_eps2_001", []), dtype=float)

    if len(ref_100) == 0 or len(ref_001) == 0:
        return 0.0

    # Reference energy grid (0 to 35 eV, step 0.05)
    n_ref = len(ref_100)
    energy_ref = np.linspace(0.0, 35.0, n_ref)

    try:
        e2_100_interp = np.interp(energy_ref, energy_agent, e2_100_agent)
        e2_001_interp = np.interp(energy_ref, energy_agent, e2_001_agent)
        e1_100_interp = np.interp(energy_ref, energy_agent, e1_100_agent)
        e1_001_interp = np.interp(energy_ref, energy_agent, e1_001_agent)
    except Exception:
        return 0.0

    def pearson(x, y):
        if len(x) < 2:
            return 0.0
        x = np.array(x, dtype=float); y = np.array(y, dtype=float)
        mx = x.mean(); my = y.mean()
        num = ((x - mx) * (y - my)).sum()
        den = np.sqrt(((x - mx)**2).sum() * ((y - my)**2).sum())
        if den < 1e-12:
            return 1.0 if abs(mx - my) < 1e-12 else 0.0
        return num / den

    corr_100 = pearson(e2_100_interp, ref_100)
    corr_001 = pearson(e2_001_interp, ref_001)
    avg_corr = (corr_100 + corr_001) / 2.0

    static = artifact.get("static_dielectric_constants", {})
    eps0_100 = static.get("epsilon0_100")
    eps0_001 = static.get("epsilon0_001")
    tol_static = step.get("config", {}).get("static_eps_tolerance", 0.1)
    consistency_score = 0.0
    if eps0_100 is not None and len(e1_100_interp) > 0:
        if abs(e1_100_interp[0] - eps0_100) <= tol_static:
            consistency_score += 0.5
    if eps0_001 is not None and len(e1_001_interp) > 0:
        if abs(e1_001_interp[0] - eps0_001) <= tol_static:
            consistency_score += 0.5

    corr_thresh = step.get("config", {}).get("corr_threshold", 0.9)
    corr_factor = min(1.0, max(0.0, avg_corr / corr_thresh))
    score = 0.8 * corr_factor + 0.2 * consistency_score
    return max(0.0, min(1.0, score))


_SCORERS = {
    'check_lattice': score_0,
    'check_bulk': score_1,
    'check_elastic': score_2,
    'check_derived': score_3,
    'check_sound': score_4,
    'check_debye': score_5,
    'check_bandgaps': score_6,
    'check_static_eps': score_7,
    'check_dielectric_spectrum': score_8,
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
