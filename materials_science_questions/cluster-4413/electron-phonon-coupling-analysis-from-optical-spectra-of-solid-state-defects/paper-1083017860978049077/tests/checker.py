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
    import json, math
    def prepare(outputs_dir, spec):
        gold_lw = spec.get('gold_linewidths', {})
        replica_offsets = spec.get('replica_offsets_ev', [-0.05, -0.07])
        replica_offset_tol = spec.get('replica_offset_tol_ev', 0.002)
        intensity_ratio_range = spec.get('intensity_ratio_range', [0.5, 2.0])
        return {
            'gold_lw': gold_lw,
            'replica_offsets': replica_offsets,
            'replica_offset_tol': replica_offset_tol,
            'intensity_ratio_range': intensity_ratio_range
        }


# === block: score_0 (check id='step_06_check') ===
def score_0(artifact, step, ctx):
    import csv, math

    def score(artifact, step, ctx):
        expected_cols = {'temperature', 'exciton_index', 'relaxation_time'}
        if not artifact or not isinstance(artifact, list) or len(artifact) == 0:
            return 0.0
        rows = artifact
        if not expected_cols.issubset(rows[0].keys()):
            return 0.0

        gold = ctx['gold_lw']
        # check gold fields exist
        if not all(k in gold for k in ['SA','SO','EA','EO','gamma0','a','b']):
            return 0.0

        # Helper: compute expected tau for exciton 1 (Toyozawa strong coupling)
        def tau_ex1(T):
            S_A, S_O, E_A, E_O = gold['SA'], gold['SO'], gold['EA'], gold['EO']
            kb = 0.086173324  # meV/K
            if T == 0:
                delta_sq = S_A * E_A
            else:
                x_A = E_A/(2.0*kb*T)
                coth_A = 1.0 / math.tanh(x_A)
                delta_A2 = S_A * E_A * coth_A
                # optical part: [exp(E_O/(2kT))-1]^-1
                exp_O = math.exp(E_O/(2.0*kb*T))
                if exp_O > 1.0:
                    delta_O2 = S_O * E_O / (exp_O - 1.0)
                else:
                    delta_O2 = 0.0
                delta_sq = delta_A2 + delta_O2
            if delta_sq <= 0:
                return 1e9
            delta = math.sqrt(delta_sq)
            tau = 2.0 / delta   # assume FWHM = 2*rate, relaxation time = 1/rate
            return tau

        # Helper: expected tau for exciton 5 (weak coupling)
        def tau_ex5(T):
            gamma0, a, b, E_O = gold['gamma0'], gold['a'], gold['b'], gold['EO']
            kb = 0.086173324
            if T == 0:
                tau = 2.0 / gamma0
            else:
                exp_term = math.exp(E_O/(kb*T)) - 1.0
                if exp_term > 0:
                    gamma = gamma0 + a*T + b / exp_term
                else:
                    gamma = gamma0 + a*T + b / 1e-6  # fallback
                tau = 2.0 / gamma
            return tau

        # collect data
        data = []
        for r in rows:
            try:
                T_val = r.get('temperature')
                if T_val is None: continue
                T = float(T_val)
                idx_val = r.get('exciton_index')
                if idx_val is None: continue
                idx = int(idx_val)
                tau_val = r.get('relaxation_time')
                if tau_val is None: continue
                tau = float(tau_val)
                data.append({'T': T, 'exciton': idx, 'tau': tau})
            except (ValueError, TypeError):
                continue
        if not data:
            return 0.0

        # check positivity
        pos_ok = all(d['tau'] > 0 for d in data)
        score_pos = 1.0 if pos_ok else 0.0

        # check monotonic decay within each exciton
        from collections import defaultdict
        by_exc = defaultdict(list)
        for d in data:
            by_exc[d['exciton']].append((d['T'], d['tau']))
        monotonic_frac = 0.0
        counts = 0
        for exc, vals in by_exc.items():
            vals.sort(key=lambda x: x[0])
            n = len(vals)
            if n < 2:
                continue
            dec_count = 0
            for i in range(n-1):
                if vals[i+1][1] <= vals[i][1] * (1 + 1e-6):
                    dec_count += 1
            monotonic_frac += dec_count / (n-1)
            counts += 1
        if counts > 0:
            score_mono = monotonic_frac / counts
        else:
            score_mono = 1.0

        # recompute expected tau for exciton 1 and 5 at sampled T from agent
        rel_tol = 0.30
        point_scores = []
        for exc, tau_func in [(1, tau_ex1), (5, tau_ex5)]:
            for d in data:
                if d['exciton'] == exc:
                    T = d['T']
                    tau_agent = d['tau']
                    tau_exp = tau_func(T)
                    if abs(tau_agent - tau_exp) <= rel_tol * max(abs(tau_exp), 1e-6):
                        point_scores.append(1.0)
                    else:
                        point_scores.append(0.0)
        if point_scores:
            score_recompute = sum(point_scores) / len(point_scores)
        else:
            score_recompute = 0.0

        # combine sub-scores
        final = score_recompute * 0.6 + score_pos * 0.1 + score_mono * 0.3
        return round(final, 4)


# === block: score_1 (check id='step_07_check') ===
def score_1(artifact, step, ctx):
    import json, math
    def score(artifact, step, ctx):
        gold = ctx['gold_lw']
        if not isinstance(artifact, dict):
            return 0.0
        if not all(k in artifact for k in ['exciton1', 'exciton5']):
            return 0.0
        tol_rel = 0.10
        tol_abs = 0.01
        fields = [('exciton1', 'SA', gold['SA']),
                  ('exciton1', 'SO', gold['SO']),
                  ('exciton1', 'EA', gold['EA']),
                  ('exciton1', 'EO', gold['EO']),
                  ('exciton5', 'gamma0', gold['gamma0']),
                  ('exciton5', 'a', gold['a']),
                  ('exciton5', 'b', gold['b'])]
        scores = []
        for group, key, target in fields:
            sub = artifact.get(group)
            if not isinstance(sub, dict):
                scores.append(0.0)
                continue
            val = sub.get(key)
            if val is None:
                scores.append(0.0)
            else:
                if abs(val - target) <= max(tol_rel * abs(target), tol_abs):
                    scores.append(1.0)
                else:
                    scores.append(0.0)
        if not scores:
            return 0.0
        return round(sum(scores)/len(scores), 4)


# === block: score_2 (check id='step_08_check') ===
def score_2(artifact, step, ctx):
    import csv, math
    def score(artifact, step, ctx):
        replica_offsets = ctx['replica_offsets']
        offset_tol = 0.005  # use 5 meV tolerance to accommodate toolchain variability
        ratio_range = ctx['intensity_ratio_range']
        if not artifact or not isinstance(artifact, list) or len(artifact) < 3:
            return 0.0
        rows = artifact
        # expect columns energy and intensity
        try:
            energies = [float(r['energy']) for r in rows]
            intensities = [float(r['intensity']) for r in rows]
        except (KeyError, ValueError):
            return 0.0
        if not energies or not intensities:
            return 0.0
        # find bright peak (max intensity)
        max_idx = intensities.index(max(intensities))
        bright_E = energies[max_idx]
        # filter points below bright line for replicas (energy < bright_E - 0.02)
        lower_mask = [i for i, e in enumerate(energies) if e < bright_E - 0.02]
        if not lower_mask:
            return 0.0
        lower_energies = [energies[i] for i in lower_mask]
        lower_intensities = [intensities[i] for i in lower_mask]
        # simple local max detection
        peaks = []
        n = len(lower_energies)
        if n < 3:
            return 0.0
        for i in range(1, n-1):
            if lower_intensities[i] > lower_intensities[i-1] and lower_intensities[i] > lower_intensities[i+1]:
                peaks.append((lower_energies[i], lower_intensities[i]))
        # also check first and last
        if lower_intensities[0] > lower_intensities[1]:
            peaks.append((lower_energies[0], lower_intensities[0]))
        if lower_intensities[-1] > lower_intensities[-2]:
            peaks.append((lower_energies[-1], lower_intensities[-1]))
        if not peaks:
            return 0.0
        # sort peaks by intensity descending, take up to 2
        peaks.sort(key=lambda x: x[1], reverse=True)
        top_peaks = peaks[:2]
        if len(top_peaks) < 1:
            return 0.0
        # compute offsets from bright peak
        offsets = [p[0] - bright_E for p in top_peaks]
        # match to expected offsets
        matched = 0
        for exp_off in replica_offsets:
            for off in offsets:
                if abs(off - exp_off) <= offset_tol:
                    matched += 1
                    break
        # score offset matching
        if len(replica_offsets) > 0:
            score_offsets = matched / len(replica_offsets)
        else:
            score_offsets = 0.0
        # intensity ratio of two top peaks
        if len(top_peaks) >= 2:
            ratio = top_peaks[1][1] / max(top_peaks[0][1], 1e-12)
            # check range
            low, high = ratio_range
            score_ratio = 1.0 if low <= ratio <= high else 0.0
        else:
            score_ratio = 0.0
        # bright peak dominance
        if max(intensities) > max([p[1] for p in peaks]):
            score_dominant = 1.0
        else:
            score_dominant = 0.0
        # combine
        final = score_offsets * 0.5 + score_ratio * 0.3 + score_dominant * 0.2
        return round(final, 4)


_SCORERS = {
    'step_06_check': score_0,
    'step_07_check': score_1,
    'step_08_check': score_2,
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
