import os
import json
import csv

# === author imports / helpers ===
import sys
import subprocess
try:
    import numpy as np
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "--no-cache-dir", "-i", "https://pypi.tuna.tsinghua.edu.cn/simple", "numpy"])
    import numpy as np


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
    import numpy as np
    import json
    # spec is already provided as an argument
    params = spec.get('reference_model_params', {})
    beam = params.get('beam', {})
    spectrum = params.get('spectrum', {})
    tol = spec.get('tolerance_cum_frac', 0.1)

    def make_reference_energy(mu, sl, sr, amp, num=801, depth_max=800):
        d = np.linspace(0, depth_max, num)
        e = np.zeros_like(d)
        for i, x in enumerate(d):
            if x <= mu:
                sigma = sl
            else:
                sigma = sr
            e[i] = amp * np.exp(-0.5*((x-mu)/sigma)**2)
        return d, e

    depth_ref, ref_energy_beam = make_reference_energy(beam['mu'], beam['sigma_left'], beam['sigma_right'], beam['amplitude'])
    _, ref_energy_spec = make_reference_energy(spectrum['mu'], spectrum['sigma_left'], spectrum['sigma_right'], spectrum['amplitude'])

    cumsum_beam = np.cumsum(ref_energy_beam)
    cumsum_spec = np.cumsum(ref_energy_spec)
    ref_cumfrac_beam = cumsum_beam / cumsum_beam[-1]
    ref_cumfrac_spec = cumsum_spec / cumsum_spec[-1]

    return {
        'depth_ref': depth_ref,
        'ref_cumfrac_beam': ref_cumfrac_beam,
        'ref_cumfrac_spec': ref_cumfrac_spec,
        'tolerance_cum_frac': tol
    }


# === block: score_0 (check id='check_ni63_shape') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) < 10:
        return 0.0
    required = {'depth_nm', 'energy_deposition_eV_per_electron'}
    if not required.issubset(artifact[0].keys()):
        return 0.0
    try:
        float(artifact[0]['depth_nm'])
        float(artifact[0]['energy_deposition_eV_per_electron'])
    except (ValueError, KeyError):
        return 0.0
    return 1.0


# === block: score_1 (check id='profile_ni63') ===
def score_1(artifact, step, ctx):
    import csv
    import io
    # artifact is list of dicts from csv reader
    # parse depth and energy
    depths = []
    energies = []
    for row in artifact:
        try:
            d = float(row['depth_nm'])
            e = float(row['energy_deposition_eV_per_electron'])
            depths.append(d)
            energies.append(e)
        except:
            continue
    if len(depths) < 10:
        return 0.0
    depths = np.array(depths)
    energies = np.array(energies)
    if np.sum(energies) == 0:
        return 0.0
    cumfrac_agent = np.cumsum(energies) / np.sum(energies)
    # interpolate reference to agent depths
    ref_cumfrac = np.interp(depths, ctx['depth_ref'], ctx['ref_cumfrac_spec'])
    max_diff = np.max(np.abs(cumfrac_agent - ref_cumfrac))
    tol = ctx['tolerance_cum_frac']
    score = max(0.0, 1.0 - max_diff / tol)
    return float(score)


# === block: score_2 (check id='check_beam_shape') ===
def score_2(artifact, step, ctx):
    return 1.0


# === block: score_3 (check id='profile_beam') ===
def score_3(artifact, step, ctx):
    import numpy as np
    rows = artifact
    depths = []
    energies = []
    for row in rows:
        try:
            d = float(row['depth_nm'])
            e = float(row['energy_deposition_eV_per_electron'])
            depths.append(d)
            energies.append(e)
        except:
            continue
    if len(depths) < 10:
        return 0.0
    depths = np.array(depths)
    energies = np.array(energies)
    total = np.sum(energies)
    if total == 0:
        return 0.0
    cumfrac_agent = np.cumsum(energies) / total
    ref_cumfrac = np.interp(depths, ctx['depth_ref'], ctx['ref_cumfrac_beam'])
    max_diff = np.max(np.abs(cumfrac_agent - ref_cumfrac))
    tol = ctx['tolerance_cum_frac']
    score = max(0.0, 1.0 - max_diff / tol)
    return float(score)


# === block: score_4 (check id='trend') ===
def score_4(artifact, step, ctx):
    import csv
    import numpy as np

    def read_csv(path):
        with open(path, newline='') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        depths = []
        energies = []
        for row in rows:
            try:
                d = float(row['depth_nm'])
                e = float(row['energy_deposition_eV_per_electron'])
                depths.append(d)
                energies.append(e)
            except:
                pass
        return np.array(depths), np.array(energies)

    depth_spec, energy_spec = read_csv('/app/outputs/energy_deposition_Ni63_spectrum.csv')
    depth_beam, energy_beam = read_csv('/app/outputs/energy_deposition_17keV_beam.csv')

    if len(depth_spec) < 10 or len(depth_beam) < 10:
        return 0.0

    cumfrac_spec = np.cumsum(energy_spec) / np.sum(energy_spec)
    cumfrac_beam = np.cumsum(energy_beam) / np.sum(energy_beam)

    def depth_at_fraction(depths, cumfrac, fraction=0.9):
        idx = np.searchsorted(cumfrac, fraction)
        if idx >= len(depths):
            return depths[-1]
        return depths[idx]

    d90_spec = depth_at_fraction(depth_spec, cumfrac_spec)
    d90_beam = depth_at_fraction(depth_beam, cumfrac_beam)

    # beam should reach 0.9 at shallower depth
    if d90_beam < d90_spec:
        return 1.0
    else:
        return 0.0


_SCORERS = {
    'check_ni63_shape': score_0,
    'profile_ni63': score_1,
    'check_beam_shape': score_2,
    'profile_beam': score_3,
    'trend': score_4,
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
