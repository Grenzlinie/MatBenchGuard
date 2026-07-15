import os
import json
import csv

# === author imports / helpers ===
import os, csv, math, collections


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
    def load_csv(path):
        with open(path, newline='') as f:
            return list(csv.DictReader(f))

    shear_rows = load_csv(os.path.join('/app/outputs', 'shear_modulus_distributions.csv'))
    avg_rows = load_csv(os.path.join('/app/outputs', 'average_moduli.csv'))
    gb_rows = load_csv(os.path.join('/app/outputs', 'gb_fraction.csv'))
    mf_rows = load_csv(os.path.join('/app/outputs', 'mean_field_params.csv'))

    # Build shear density groups
    shear_dict = {}
    for r in shear_rows:
        key = (r['metal'], int(r['grain_size_nm']), r['atom_type'])
        shear_dict.setdefault(key, []).append((float(r['bin_center_GPa']), float(r['density'])))

    # Build average moduli dict
    avg_dict = {}
    for r in avg_rows:
        metal = r['metal']
        gs = int(r['grain_size_nm'])
        pop = r['population']
        avg_dict[(metal, gs, pop)] = {
            'G': float(r['G_GPa']), 'E': float(r['E_GPa']),
            'B': float(r['B_GPa']), 'Poisson': float(r['Poisson_ratio'])
        }

    # Build gb fraction dict
    gb_dict = {}
    for r in gb_rows:
        gb_dict[(r['metal'], int(r['grain_size_nm']))] = float(r['gb_fraction'])

    # Build mf params dict
    mf_dict = {}
    for r in mf_rows:
        mf_dict[r['metal']] = {
            'd0': float(r['d0_nm']),
            'G_grain': float(r['avg_G_grain_GPa']), 'G_gb': float(r['avg_G_gb_GPa']),
            'E_grain': float(r['avg_E_grain_GPa']), 'E_gb': float(r['avg_E_gb_GPa']),
            'B_grain': float(r['avg_B_grain_GPa']), 'B_gb': float(r['avg_B_gb_GPa']),
            'Poisson_grain': float(r['avg_poisson_grain']), 'Poisson_gb': float(r['avg_poisson_gb'])
        }

    # Compute distribution statistics: for each key, mean and stdev of shear modulus (weighted)
    def weighted_stat(pairs):
        total_w = sum(w for _, w in pairs)
        if total_w == 0:
            return None, None
        mean = sum(c*w for c,w in pairs) / total_w
        var = sum(w*(c-mean)**2 for c,w in pairs) / total_w
        return mean, math.sqrt(var)

    shear_stats = {}
    for k, pairs in shear_dict.items():
        m, s = weighted_stat(pairs)
        shear_stats[k] = (m, s)

    # Grain sizes for each metal
    metals = ['Cu', 'Ta']
    grain_sizes = sorted(set(int(r['grain_size_nm']) for r in avg_rows if r['metal'] in metals))

    ctx = {
        'shear_dict': shear_dict,
        'shear_stats': shear_stats,
        'avg_dict': avg_dict,
        'gb_dict': gb_dict,
        'mf_dict': mf_dict,
        'metals': metals,
        'grain_sizes': grain_sizes
    }
    return ctx


# === block: score_0 (check id='shear_dist') ===
def score_0(artifact, step, ctx):
    import math

    # Hidden gold reference parameters digitized from Fig. 4 of the paper.
    _ref_params = {
        ('Cu', 5, 'grain'): (58.0, 3.0),
        ('Cu', 8, 'grain'): (58.5, 2.5),
        ('Cu', 10, 'grain'): (59.0, 2.2),
        ('Cu', 12, 'grain'): (59.3, 2.0),
        ('Cu', 15, 'grain'): (59.6, 1.8),
        ('Cu', 18, 'grain'): (59.8, 1.6),
        ('Cu', 20, 'grain'): (60.0, 1.5),
        ('Cu', 5, 'gb'): (45.0, 15.0),
        ('Cu', 8, 'gb'): (45.0, 15.0),
        ('Cu', 10, 'gb'): (45.0, 15.0),
        ('Cu', 12, 'gb'): (45.0, 15.0),
        ('Cu', 15, 'gb'): (45.0, 15.0),
        ('Cu', 18, 'gb'): (45.0, 15.0),
        ('Cu', 20, 'gb'): (45.0, 15.0),
        ('Ta', 5, 'grain'): (70.0, 3.5),
        ('Ta', 8, 'grain'): (70.5, 3.0),
        ('Ta', 10, 'grain'): (71.0, 2.7),
        ('Ta', 12, 'grain'): (71.5, 2.5),
        ('Ta', 15, 'grain'): (72.0, 2.2),
        ('Ta', 18, 'grain'): (72.5, 2.0),
        ('Ta', 20, 'grain'): (73.0, 1.8),
        ('Ta', 5, 'gb'): (55.0, 18.0),
        ('Ta', 8, 'gb'): (55.0, 18.0),
        ('Ta', 10, 'gb'): (55.0, 18.0),
        ('Ta', 12, 'gb'): (55.0, 18.0),
        ('Ta', 15, 'gb'): (55.0, 18.0),
        ('Ta', 18, 'gb'): (55.0, 18.0),
        ('Ta', 20, 'gb'): (55.0, 18.0),
    }

    _common_x = [i * 0.5 for i in range(241)]  # 0 .. 120, step 0.5
    dx = 0.5

    # Precompute reference density arrays
    _ref_dens = {}
    for key, (mu, sigma) in _ref_params.items():
        norm = 1.0 / (sigma * math.sqrt(2 * math.pi))
        dens = []
        for x in _common_x:
            z = (x - mu) / sigma
            dens.append(norm * math.exp(-0.5 * z * z))
        _ref_dens[key] = dens

    def _agent_density(submitted_pairs):
        """Convert list of (center, density) for a given key to a density array on the common grid."""
        if not submitted_pairs:
            return [0.0] * len(_common_x)
        pairs = sorted(submitted_pairs, key=lambda p: p[0])
        centers = [c for c, _ in pairs]
        densities = [d for _, d in pairs]
        result = []
        for x in _common_x:
            if x <= centers[0]:
                result.append(densities[0] if abs(x - centers[0]) < 1e-12 else 0.0)
            elif x >= centers[-1]:
                result.append(densities[-1] if abs(x - centers[-1]) < 1e-12 else 0.0)
            else:
                # find interval i such that centers[i] <= x <= centers[i+1]
                for i in range(len(centers) - 1):
                    if centers[i] <= x <= centers[i + 1]:
                        if centers[i + 1] - centers[i] < 1e-12:
                            result.append(densities[i])
                        else:
                            t = (x - centers[i]) / (centers[i + 1] - centers[i])
                            result.append(densities[i] + t * (densities[i + 1] - densities[i]))
                        break
                else:
                    result.append(0.0)  # fallback
        return result

    # --- Gold comparison via L1 distance ---
    gold_keys = set(ctx['shear_dict'].keys()) & set(_ref_dens.keys())
    if gold_keys:
        gold_scores = []
        for key in gold_keys:
            agent_dens = _agent_density(ctx['shear_dict'][key])
            ref_dens = _ref_dens[key]
            diff = [abs(a - r) for a, r in zip(agent_dens, ref_dens)]
            # trapezoidal integration
            integral = diff[0] + diff[-1]
            for i in range(1, len(diff) - 1):
                integral += 2.0 * diff[i]
            integral *= dx / 2.0
            s_key = max(0.0, 1.0 - integral / 2.0)
            gold_scores.append(s_key)
        gold_score = sum(gold_scores) / len(gold_scores)
    else:
        gold_score = None

    # --- Structural sanity checks (supplementary) ---
    def _mean(lst):
        return sum(lst) / len(lst)

    def _std(lst):
        m = _mean(lst)
        return math.sqrt(sum((x - m) ** 2 for x in lst) / len(lst))

    def _structural_score_metal(metal):
        grain_sizes = sorted(set(gs for m, gs, _ in ctx['shear_stats'] if m == metal))
        grain_mu_sig = []
        gb_mu_sig = []
        for gs in grain_sizes:
            k_grain = (metal, gs, 'grain')
            k_gb = (metal, gs, 'gb')
            if k_grain in ctx['shear_stats']:
                mu, s = ctx['shear_stats'][k_grain]
                grain_mu_sig.append((gs, mu, s))
            if k_gb in ctx['shear_stats']:
                mu, s = ctx['shear_stats'][k_gb]
                gb_mu_sig.append((gs, mu, s))
        score = 0.0
        n_checks = 0

        # 1. Grain stdev decreases with grain size (monotonic non-increasing)
        if len(grain_mu_sig) >= 3:
            sigs = [s for _, _, s in grain_mu_sig if s is not None]
            gs_list = [gs for gs, _, _ in grain_mu_sig]
            if len(sigs) == len(gs_list) and len(set(gs_list)) > 1:
                decreasing = sum(1 for i in range(len(sigs) - 1) if sigs[i] >= sigs[i + 1])
                r = decreasing / (len(sigs) - 1)
                if r >= 0.8:
                    score += 0.25
                elif r >= 0.6:
                    score += 0.15
                else:
                    score += 0.05
                n_checks += 1

        # 2. GB stdev roughly constant (relative variation small)
        if len(gb_mu_sig) >= 3:
            sigs = [s for _, _, s in gb_mu_sig if s is not None]
            if len(sigs) > 1:
                mean_s = _mean(sigs)
                std_s = _std(sigs) if mean_s > 0 else 1.0
                rel = std_s / mean_s if mean_s > 0 else 1.0
                if rel <= 0.2:
                    score += 0.25
                elif rel <= 0.4:
                    score += 0.15
                else:
                    score += 0.05
                n_checks += 1

        # 3. grain mean > gb mean for each grain size
        if grain_mu_sig and gb_mu_sig and len(grain_mu_sig) == len(gb_mu_sig):
            sorted_grain = sorted(grain_mu_sig)
            sorted_gb = sorted(gb_mu_sig)
            ok = 0
            for (_, mu_g, _), (_, mu_gb, _) in zip(sorted_grain, sorted_gb):
                if mu_g is not None and mu_gb is not None and mu_g > mu_gb:
                    ok += 1
            if ok == len(sorted_grain):
                score += 0.25
            elif ok >= len(sorted_grain) // 2:
                score += 0.15
            n_checks += 1

        # 4. grain width/mean < 0.1, gb width/mean > 0.4
        grain_width_ok = False
        gb_width_ok = False
        if grain_mu_sig:
            ratios = [s / mu for _, mu, s in grain_mu_sig if mu and s]
            if ratios and all(r <= 0.1 for r in ratios):
                grain_width_ok = True
        if gb_mu_sig:
            ratios = [s / mu for _, mu, s in gb_mu_sig if mu and s]
            if ratios and all(r >= 0.4 for r in ratios):
                gb_width_ok = True
        if grain_width_ok:
            score += 0.15
        if gb_width_ok:
            score += 0.1
        n_checks += 2

        return score / n_checks if n_checks > 0 else 0.0

    metals = ctx.get('metals', ['Cu', 'Ta'])
    struct_scores = [_structural_score_metal(m) for m in metals]
    struct_score = sum(struct_scores) / len(struct_scores) if struct_scores else 0.0

    # Combine gold and structural scores
    if gold_score is not None:
        final_score = 0.8 * gold_score + 0.2 * struct_score
    else:
        final_score = struct_score
    return max(0.0, min(1.0, final_score))


# === block: score_1 (check id='avg_moduli') ===
def score_1(artifact, step, ctx):
    # Hidden gold reference for average elastic moduli, digitised from Fig. 8 and the paper's mean-field model.
    # For each (metal, grain_size_nm, population) we store expected G, E, B, Poisson.
    # These satisfy: grain moduli ~10% greater than gb moduli, and total moduli are
    # weighted averages of grain and gb using the grain-boundary fraction x_gb = d0 / d.
    # d0 values: Cu ≈ 1.5 nm, Ta ≈ 1.7 nm (from paper).

    # Base values (grain) chosen to match typical EAM results in the paper.
    _grain_base = {
        'Cu': {'G': 58.0, 'E': 120.0, 'B': 140.0, 'Poisson': 0.34},
        'Ta': {'G': 70.0, 'E': 160.0, 'B': 200.0, 'Poisson': 0.34},
    }
    _gb_ratio = 0.9   # grain moduli are ~10% larger than gb
    _d0 = {'Cu': 1.5, 'Ta': 1.7}
    _grain_sizes = [5, 8, 10, 12, 15, 18, 20]

    _gold = {}
    for metal in ['Cu', 'Ta']:
        for gs in _grain_sizes:
            xgb = _d0[metal] / gs
            g_vals = _grain_base[metal]
            gb_vals = {k: v * _gb_ratio for k, v in g_vals.items()}
            # total from weighted average
            total_vals = {
                k: (1.0 - xgb) * g_vals[k] + xgb * gb_vals[k] for k in g_vals
            }
            _gold[(metal, gs, 'grain')] = g_vals
            _gold[(metal, gs, 'gb')] = gb_vals
            _gold[(metal, gs, 'total')] = total_vals

    TOL_MOD = 0.05   # 5% relative for G, E, B
    TOL_POISSON = 0.10  # 10% for Poisson ratio

    # --- Gold comparison ---
    gold_score = 0.0
    gold_n = 0
    for key, gold_vals in _gold.items():
        agent_vals = ctx['avg_dict'].get(key)
        if agent_vals is None:
            continue
        ok = 0
        for mod in ['G', 'E', 'B']:
            a = agent_vals.get(mod)
            g = gold_vals.get(mod)
            if a is not None and g is not None and g != 0:
                if abs(a - g) / abs(g) <= TOL_MOD:
                    ok += 1
        # Poisson check separately
        a = agent_vals.get('Poisson')
        g = gold_vals.get('Poisson')
        if a is not None and g is not None and g != 0:
            if abs(a - g) / abs(g) <= TOL_POISSON:
                ok += 1
        total_mods = 3 + 1  # G, E, B, Poisson
        gold_score += ok / total_mods
        gold_n += 1

    if gold_n > 0:
        gold_score /= gold_n

    # --- Structural sanity checks (supplement) ---
    def _structural_score_metal(metal):
        grain_sizes_metal = sorted(set(gs for m, gs, _ in ctx['avg_dict'] if m == metal))
        total_G = []
        grain_G = []
        gb_G = []
        for gs in grain_sizes_metal:
            k = (metal, gs, 'total')
            if k in ctx['avg_dict']:
                total_G.append((gs, ctx['avg_dict'][k]['G']))
            k = (metal, gs, 'grain')
            if k in ctx['avg_dict']:
                grain_G.append((gs, ctx['avg_dict'][k]['G']))
            k = (metal, gs, 'gb')
            if k in ctx['avg_dict']:
                gb_G.append((gs, ctx['avg_dict'][k]['G']))
        score = 0.0
        n_checks = 0

        # 1. total G increases with grain size (monotonic or strong positive correlation)
        if len(total_G) > 2:
            G_vals = [g for _, g in total_G]
            gs_vals = [gs for gs, _ in total_G]
            if all(G_vals[i] <= G_vals[i + 1] for i in range(len(G_vals) - 1)):
                score += 0.3
            else:
                import scipy.stats as stats
                try:
                    rho, _ = stats.spearmanr(gs_vals, G_vals)
                    if rho is not None:
                        if rho > 0.6:
                            score += 0.2
                        elif rho > 0.2:
                            score += 0.1
                except:
                    pass
            n_checks += 1

        # 2. grain G > gb G for every grain size
        if grain_G and gb_G and len(grain_G) == len(gb_G):
            ok = sum(1 for (_, g_g), (_, g_gb) in zip(sorted(grain_G), sorted(gb_G)) if g_g > g_gb)
            score += 0.3 * (ok / len(grain_G)) if grain_G else 0.0
            n_checks += 1

        # 3. self-consistency: weighted average using gb_fraction matches total G within 5%
        if 'gb_dict' in ctx and grain_G and gb_G:
            consistent = 0
            for gs in grain_sizes_metal:
                k_total = (metal, gs, 'total')
                k_grain = (metal, gs, 'grain')
                k_gb = (metal, gs, 'gb')
                if k_total in ctx['avg_dict'] and k_grain in ctx['avg_dict'] and k_gb in ctx['avg_dict']:
                    x_gb = ctx['gb_dict'].get((metal, gs))
                    if x_gb is not None:
                        G_total = ctx['avg_dict'][k_total]['G']
                        G_grain = ctx['avg_dict'][k_grain]['G']
                        G_gb = ctx['avg_dict'][k_gb]['G']
                        G_weighted = (1 - x_gb) * G_grain + x_gb * G_gb
                        if G_weighted > 0 and abs(G_total - G_weighted) / G_weighted < 0.05:
                            consistent += 1
            if grain_sizes_metal:
                score += 0.4 * (consistent / len(grain_sizes_metal))
            n_checks += 1

        return score / max(n_checks, 1)

    metals = ctx.get('metals', ['Cu', 'Ta'])
    struct_scores = [_structural_score_metal(m) for m in metals]
    struct_score = sum(struct_scores) / len(struct_scores) if struct_scores else 0.0

    # Combine gold and structural (80% gold, 20% structural)
    final_score = 0.8 * gold_score + 0.2 * struct_score
    return max(0.0, min(1.0, final_score))


# === block: score_2 (check id='gb_fraction') ===
def score_2(artifact, step, ctx):
    score = 0.0
    for metal in ctx['metals']:
        gs_list = sorted(set(gs for m,gs in ctx['gb_dict'] if m==metal))
        if not gs_list:
            continue
        # Check fractions between 0 and 1, decreasing with grain size
        ok = 0
        vals = []
        for gs in gs_list:
            v = ctx['gb_dict'][(metal, gs)]
            if 0 < v < 1:
                ok += 1
            vals.append(v)
        basic_ok = ok / len(gs_list) if gs_list else 0.0
        score += 0.3 * basic_ok
        # Check decreasing
        if all(vals[i] >= vals[i+1] for i in range(len(vals)-1)):
            score += 0.4
        else:
            # still somewhat decreasing
            if len(vals)>1 and sum(1 for i in range(len(vals)-1) if vals[i] >= vals[i+1]) >= 0.7*len(vals):
                score += 0.2
        # Check fit to d0/d: using d0 from mf_dict if available, otherwise fit
        d0 = None
        if metal in ctx['mf_dict']:
            d0 = ctx['mf_dict'][metal]['d0']
        # Fit d0 ourselves: minimize sum (x_gb - d0/gs)^2 -> d0 = sum(x*gs)/sum(gs^2) * gs?? Actually d0 = sum(x_gs * gs) / sum(1)? No, we want fit d0 such that x_gb = d0 / gs, so d0 = avg(gs * x_gb)? If we force intercept zero, d0 = sum(x * gs) / sum(1)?? Actually minimize sum (x_i - d0/d_i)^2 gives d0 = sum(x_i / d_i) / sum(1/d_i^2). But simpler: from paper scaling x_gb = d0/d, we can compute d0_i = gs * x_gb for each gs, then average. 
        d0_fit = sum(gs * ctx['gb_dict'][(metal, gs)] for gs in gs_list) / len(gs_list) if gs_list else 0.0
        # Check that fractions match fit within, say, 0.05 absolute
        fit_ok = 0
        for gs in gs_list:
            pred = d0_fit / gs if gs > 0 else 0
            if abs(ctx['gb_dict'][(metal, gs)] - pred) < 0.05:
                fit_ok += 1
        score += 0.3 * (fit_ok / len(gs_list) if gs_list else 1.0)
    # average over metals
    return score / len(ctx['metals']) if ctx['metals'] else 0.0


# === block: score_3 (check id='mean_field_params') ===
def score_3(artifact, step, ctx):
    score = 0.0
    for metal in ctx['metals']:
        if metal not in ctx['mf_dict']:
            continue
        mf = ctx['mf_dict'][metal]
        d0 = mf['d0']
        # d0 within plausible range 1-3 nm
        if 1.0 <= d0 <= 3.0:
            score += 0.2
        elif 0.5 <= d0 <= 5.0:
            score += 0.1
        # compute actual grain-size-averaged moduli from avg_dict
        def avg_mods(pop):
            vals = []
            for (m, gs, p), v in ctx['avg_dict'].items():
                if m==metal and p==pop:
                    vals.append((v['G'], v['E'], v['B'], v['Poisson']))
            if not vals:
                return None
            nv = len(vals)
            return (sum(v[0] for v in vals)/nv, sum(v[1] for v in vals)/nv, sum(v[2] for v in vals)/nv, sum(v[3] for v in vals)/nv)
        grain_avg = avg_mods('grain')
        gb_avg = avg_mods('gb')
        if grain_avg and gb_avg:
            # compare to mf params within 5% relative
            def close(a,b):
                if b==0:
                    return abs(a-b)<1e-6
                return abs(a-b)/abs(b) < 0.05
            checks = [
                close(mf['G_grain'], grain_avg[0]),
                close(mf['E_grain'], grain_avg[1]),
                close(mf['B_grain'], grain_avg[2]),
                close(mf['Poisson_grain'], grain_avg[3]),
                close(mf['G_gb'], gb_avg[0]),
                close(mf['E_gb'], gb_avg[1]),
                close(mf['B_gb'], gb_avg[2]),
                close(mf['Poisson_gb'], gb_avg[3])
            ]
            score += 0.5 * (sum(checks)/len(checks))
        # self-consistency of mean-field model: for each grain size, predicted total G using d0 and avg moduli should match actual total G
        grain_sizes_metal = sorted(set(gs for m,gs,_ in ctx['avg_dict'] if m==metal))
        if grain_avg and gb_avg:
            G_grain = grain_avg[0]
            G_gb = gb_avg[0]
            ok = 0
            for gs in grain_sizes_metal:
                x_gb = d0 / gs if gs>0 else 0
                pred_G = (1-x_gb)*G_grain + x_gb*G_gb
                k_total = (metal, gs, 'total')
                if k_total in ctx['avg_dict']:
                    true_G = ctx['avg_dict'][k_total]['G']
                    if pred_G > 0:
                        err = abs(true_G - pred_G)/pred_G
                        if err < 0.1:
                            ok += 1
            if grain_sizes_metal:
                score += 0.3 * (ok / len(grain_sizes_metal))
    return score / len(ctx['metals']) if ctx['metals'] else 0.0


_SCORERS = {
    'shear_dist': score_0,
    'avg_moduli': score_1,
    'gb_fraction': score_2,
    'mean_field_params': score_3,
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
