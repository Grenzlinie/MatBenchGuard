import os
import json
import csv

# === author imports / helpers ===
import csv, math, os, json


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
    reference = spec.get('reference', {})
    if not reference:
        raise ValueError('Missing reference data in grading_spec.json')
    return {
        'ref_abs': reference['absolute_surface_energies'],
        'ref_order': reference['ordering']
    }


# === block: score_0 (check id='surface_energies_relaxed') ===
def score_0(artifact, step, ctx):
    # artifact is a list of dict rows from CSV
    if not artifact or not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0

    REQUIRED = ['surface','slab_total_energy','n_layers','bulk_energy_per_layer','surface_cell_area','computed_surface_energy','relaxed_order_rank']
    first = artifact[0]
    for col in REQUIRED:
        if col not in first:
            return 0.0

    # canonical surface name helper: extract digit sequence only (unique per surface)
    def canonical(s: str):
        return ''.join(ch for ch in s if ch.isdigit())

    # parse rows
    rows = []
    for row in artifact:
        try:
            surf = row['surface']
            E_slab = float(row['slab_total_energy'])
            n = int(row['n_layers'])
            E_bulk = float(row['bulk_energy_per_layer'])
            A = float(row['surface_cell_area'])
            comp = float(row['computed_surface_energy'])
            rows.append((surf, E_slab, n, E_bulk, A, comp))
        except (ValueError, TypeError):
            continue

    if len(rows) != 7:
        return 0.0

    # unit detection: eV vs Ha (threshold 500)
    max_abs = max(abs(r[1]) for r in rows)
    if max_abs > 500:
        conv = 16.02176634   # 1 eV/Å² -> J/m²
    else:
        conv = 435.974        # 1 Ha/Å² -> J/m²

    # recompute and check consistency
    recomputed = {}
    agent_comp = {}
    for surf, E_slab, n, E_bulk, A, comp in rows:
        E_recalc = (E_slab - n * E_bulk) / (2.0 * A) * conv
        key = canonical(surf)
        recomputed[key] = E_recalc
        agent_comp[key] = comp

    # consistency gate: all relative errors <= 1%
    for key in recomputed:
        if key not in agent_comp:
            return 0.0
        rec = recomputed[key]
        agc = agent_comp[key]
        if agc == 0:
            return 0.0
        rel = abs(rec - agc) / abs(agc)
        if rel > 0.01:
            return 0.0

    # build digit -> reference key mapping from ref_order (given by prepare)
    ref_order = ctx['ref_order']
    digit_to_ref = {canonical(k): k for k in ref_order}
    expected_set = set(digit_to_ref.keys())
    present_set = set(recomputed.keys())
    if present_set != expected_set:
        return 0.0

    # ordering score (Kendall tau)
    sorted_digits = sorted(recomputed.keys(), key=lambda k: recomputed[k])
    ref_digits = [canonical(k) for k in ref_order]

    def kendall_tau(seq1, seq2):
        # seq1, seq2 are permutations of the same set of items
        items = seq1[:]
        n = len(items)
        if n < 2:
            return 1.0
        concordant = 0
        discordant = 0
        for i in range(n):
            for j in range(i+1, n):
                a, b = items[i], items[j]
                if (seq1.index(a) < seq1.index(b)) == (seq2.index(a) < seq2.index(b)):
                    concordant += 1
                else:
                    discordant += 1
        return (concordant - discordant) / (n * (n - 1) / 2.0)

    tau = kendall_tau(sorted_digits, ref_digits)
    ordering_score = max(0.0, min(1.0, tau / 0.9)) if tau > 0 else 0.0

    # absolute tolerance score (30%)
    ref_abs = ctx['ref_abs']
    ok = 0
    for key in recomputed:
        ref_key = digit_to_ref[key]
        if ref_key not in ref_abs:
            continue
        dev = abs(recomputed[key] - ref_abs[ref_key]) / ref_abs[ref_key]
        if dev <= 0.30:
            ok += 1
    absolute_score = ok / 7.0

    # combined score
    return 0.8 * ordering_score + 0.2 * absolute_score


_SCORERS = {
    'surface_energies_relaxed': score_0,
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
