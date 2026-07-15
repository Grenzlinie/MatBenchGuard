import os
import json
import csv

# === author imports / helpers ===
import csv, math


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


# === block: score_0 (check id='fetp_bandgap') ===
def score_0(artifact, step, ctx):
    import csv, os
    submitted = (artifact or '').strip().lower()
    bs_path = '/app/outputs/feTP_band_structure.csv'

    def recompute_gap():
        try:
            with open(bs_path, newline='') as f:
                reader = csv.DictReader(f)
                rows = list(reader)
                if not rows:
                    return None
                energies_up = []
                # Detect column layout
                if 'energy_up' in rows[0]:
                    # Separate columns for each spin channel
                    for r in rows:
                        try:
                            energies_up.append(float(r['energy_up']))
                        except (ValueError, KeyError):
                            continue
                elif any(c.lower().startswith('spin') for c in rows[0]):
                    spin_col = next(c for c in rows[0] if c.lower().startswith('spin'))
                    energy_col = next(c for c in rows[0] if c.lower().startswith('energy'))
                    for r in rows:
                        spin = r[spin_col].strip().lower()
                        if spin in ('up', 'majority', '1', 'true'):
                            try:
                                energies_up.append(float(r[energy_col]))
                            except (ValueError, KeyError):
                                continue
                else:
                    return None   # unknown format
                if not energies_up:
                    return None
                occupied = [e for e in energies_up if e <= 0.0]
                unoccupied = [e for e in energies_up if e > 0.0]
                if not occupied and not unoccupied:
                    return None
                if not occupied:
                    # only unoccupied states; not metallic, gap = min(unoccupied)
                    return min(unoccupied)
                if not unoccupied:
                    # only occupied states; treat as metallic if any band touches Fermi level
                    # (could be incomplete band range; return None to fallback)
                    return None
                # Check for band crossing: any occupied energy very close to 0 or unoccupied very close to 0
                crossover = any(e > -0.01 for e in occupied) or any(e < 0.01 for e in unoccupied)
                if crossover:
                    return 0.0   # metallic
                max_occ = max(occupied)
                min_unocc = min(unoccupied)
                return min_unocc - max_occ
        except Exception:
            return None

    if os.path.exists(bs_path):
        gap = recompute_gap()
        if gap is not None:
            if gap <= 0.1:
                if submitted == 'metallic' or (submitted.replace('.','',1).isdigit() and float(submitted) <= 0.1):
                    return 1.0
                else:
                    return 0.0
            else:
                # Non-metallic reproduction; threshold not met → 0.0
                return 0.0

    # Fallback: original text-based logic
    if submitted == 'metallic':
        return 1.0
    try:
        val = float(submitted)
        if val <= 0.1:
            return 1.0
        return 0.0
    except:
        return 0.0


# === block: score_1 (check id='fetpno_results') ===
def score_1(artifact, step, ctx):
    lines = (artifact or '').strip().splitlines()
    if len(lines) < 2:
        return 0.0
    try:
        gap = float(lines[0].strip())
        angle = float(lines[1].strip())
        gap_score = 1.0 if gap >= 0.5 else gap / 0.5
        dev = abs(angle - 148.0)
        angle_score = max(0.0, 1.0 - dev / 10.0)
        return min(1.0, gap_score * angle_score)
    except:
        return 0.0


# === block: score_2 (check id='fetp_pdos') ===
def score_2(artifact, step, ctx):
    if not artifact or len(artifact) < 2:
        return 0.0
    try:
        energies = [float(row['energy']) for row in artifact]
        dE = energies[1] - energies[0]
        total = 0.0
        for row in artifact:
            e = float(row['energy'])
            if -1.0 <= e <= 1.0:
                d_yz = float(row.get('d_yz_Fe', 0))
                pz_meso = float(row.get('pz_meso_C', 0))
                pz_beta = float(row.get('pz_beta_C', 0))
                if d_yz < 0 or pz_meso < 0 or pz_beta < 0:
                    return 0.0
                total += (d_yz + pz_meso + pz_beta) * dE
        return 1.0 if total >= 0.1 else 0.0
    except:
        return 0.0


_SCORERS = {
    'fetp_bandgap': score_0,
    'fetpno_results': score_1,
    'fetp_pdos': score_2,
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
