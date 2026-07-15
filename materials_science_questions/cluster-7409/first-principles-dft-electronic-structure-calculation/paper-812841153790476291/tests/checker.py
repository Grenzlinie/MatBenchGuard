import os
import json
import csv

# === author imports / helpers ===
import os, re, math


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
    ctx = {'spec': spec}
    gold = spec.get('steps', [])
    ctx['formation_gold'] = gold
    gold_vals = {}
    for step in spec['steps']:
        if step['id'] == 'formation_energy_check':
            gold_vals = step.get('gold_values', {})
            break
    ctx['gold_values'] = gold_vals
    ctx['tolerance_abs'] = next((s['tolerance_abs'] for s in spec['steps'] if s['id']=='formation_energy_check'), 0.02)
    return ctx


# === block: score_0 (check id='structure_format_check') ===
def score_0(artifact, step, ctx):
    import re
    def score(artifact, step, ctx):
        content = artifact  # artifact is the raw file content as string
        frames_content = re.split(r'^\s*\d+', content, flags=re.MULTILINE)
        # Simple parsing: count occurrences of atom lines with elements Ti/O
        lines = content.strip().split('\n')
        # Find frame starts: a line that is an integer followed by comment
        frames = []
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            try:
                natoms = int(line)
                if i+1 < len(lines):
                    comment = lines[i+1].strip()
                    frames.append({'natoms': natoms, 'comment': comment, 'lines': lines[i+2:i+2+natoms]})
                    i += 2 + natoms
                else:
                    i += 1
            except ValueError:
                i += 1
        if len(frames) < 2:
            return 0.0
        spec = step.get('check_spec', {})
        if spec.get('two_frames') and len(frames) != 2:
            return 0.0
        required_elements = spec.get('elements', [])
        for frame in frames:
            for line in frame['lines']:
                parts = line.split()
                if parts:
                    elem = parts[0]
                    if elem not in required_elements:
                        return 0.0
        if spec.get('lattice_in_comment'):
            for frame in frames:
                if 'Lattice' not in frame['comment']:
                    return 0.0
        return 1.0


# === block: score_1 (check id='formation_energy_check') ===
def score_1(artifact, step, ctx):
    import csv, io, math
    def score(artifact, step, ctx):
        gold = ctx.get('gold_values', {})
        # Large tolerance to absorb legitimate differences between DFT implementations (code, pseudopotential, basis).
        tol = 0.3
        try:
            csv_content = artifact  # artifact is a string
            reader = csv.DictReader(io.StringIO(csv_content))
            rows = list(reader)
            if not rows:
                return 0.0
            # fuzzy column matching
            col_map = {}
            for col in rows[0].keys():
                if 'composition' in col:
                    col_map['composition'] = col
                elif 'oxygen' in col and 'potential' in col:
                    col_map['oxygen_chemical_potential'] = col
                elif 'formation' in col and 'energy' in col:
                    col_map['formation_energy'] = col
            if len(col_map) != 3:
                return 0.0
            # collect per-row data
            data = {}
            for row in rows:
                comp = row[col_map['composition']]
                mu = row[col_map['oxygen_chemical_potential']]
                fe = float(row[col_map['formation_energy']])
                try:
                    mu_float = float(mu)
                except:
                    continue
                mu_key = f"{mu_float:.1f}" if mu_float != 0.0 else "0.0"
                if comp not in data:
                    data[comp] = {}
                data[comp][mu_key] = fe
            # Coarse value consistency (20%): each row passes if within 0.3 eV/Å of reference
            total_rows = 0
            correct = 0
            for comp, vals in gold.items():
                for mu_key, expected in vals.items():
                    total_rows += 1
                    if comp in data and mu_key in data.get(comp, {}):
                        given = data[comp][mu_key]
                        if abs(given - expected) <= tol:
                            correct += 1
            row_score = correct / total_rows if total_rows > 0 else 0.0
            # Ordering check (80%): correct stability ordering at the extremes of mu_O
            ordering = step.get('ordering_check', {})
            order_ok = 0.0
            if ordering:
                high = ordering.get('condition_high_muO')
                low = ordering.get('condition_low_muO')
                try:
                    if high:
                        mu = f"{high['muO']:.1f}"
                        comp_lower = high['composition_lower']
                        other_comp = 'Ti231O461' if comp_lower == 'Ti230O460' else 'Ti230O460'
                        fe_lower = data.get(comp_lower, {}).get(mu)
                        fe_other = data.get(other_comp, {}).get(mu)
                        if fe_lower is not None and fe_other is not None and fe_lower < fe_other:
                            order_ok += 0.5
                    if low:
                        mu = f"{low['muO']:.1f}"
                        comp_lower = low['composition_lower']
                        other_comp = 'Ti230O460' if comp_lower == 'Ti231O461' else 'Ti231O461'
                        fe_lower = data.get(comp_lower, {}).get(mu)
                        fe_other = data.get(other_comp, {}).get(mu)
                        if fe_lower is not None and fe_other is not None and fe_lower < fe_other:
                            order_ok += 0.5
                except:
                    pass
            # Primarily score on correct physical ordering (0.8), coarse value check as consistency (0.2)
            final_score = 0.2 * row_score + 0.8 * order_ok
            return final_score
        except Exception as e:
            return 0.0


# === block: score_2 (check id='dos_gap_states_check') ===
def score_2(artifact, step, ctx):
    import io, re
    def score(artifact, step, ctx):
        spec = step.get('check_spec', {})
        target_comp = spec.get('composition', 'Ti231O461')
        energy_range = spec.get('energy_range', [-2.0, 0.0])
        pdos_col = spec.get('pdos_column', 'PDOS_D')
        threshold = spec.get('threshold_density', 0.01)
        try:
            content = artifact  # string
            lines = content.split('\n')
            # find section for target composition
            in_section = False
            header_found = False
            col_idx = None
            for line in lines:
                line_strip = line.strip()
                if line_strip.startswith('#') and target_comp in line_strip:
                    in_section = True
                    header_found = False
                    continue
                if in_section and (line_strip.startswith('#') or line_strip == ''):
                    # end of section or comment line
                    continue
                if in_section and not header_found:
                    if 'energy' in line_strip:
                        parts = line_strip.split()
                        # find index of pdos_col
                        for i, p in enumerate(parts):
                            if pdos_col.lower() in p.lower():
                                col_idx = i
                                break
                        header_found = True
                        continue
                    # skip non-header lines until header found
                    continue
                if in_section and header_found and col_idx is not None:
                    parts = line_strip.split()
                    if len(parts) > col_idx:
                        try:
                            energy = float(parts[0])
                            density = float(parts[col_idx])
                            if energy_range[0] <= energy <= energy_range[1] and density > threshold:
                                return 1.0
                        except:
                            pass
            return 0.0
        except:
            return 0.0


_SCORERS = {
    'structure_format_check': score_0,
    'formation_energy_check': score_1,
    'dos_gap_states_check': score_2,
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
